# ALMA - Atacama Large Millimeter Array
# (c) European Southern Observatory, 2025
# (c) Associated Universities Inc., 2025
# Copyright by ESO (in the framework of the ALMA collaboration),
# Copyright by AUI (in the framework of the ALMA collaboration),
# All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307  USA
#
# File BDFReader.py
#

import sys
import re
import os
from enum import Enum, auto
import codecs
from xml.dom import minidom
import numpy as np

from .BDFHeader import BDFHeader

from pyasdm.exceptions.BDFReaderException import BDFReaderException


class BDFReader:
    """
    A class to read the contents of a BDF file in a sequential way, as a stream of bytes.
    Methods are provided to return the different parts (actual times,
    actual durations, cross data, auto data, zero lags, and flags) recorded
    at each inegration. Methods are also provided to return the meta information relevant
    to the entire file as well as to the individual integrations.

    This code is based on the c++ class of the same name as well as the python
    code in pyBDFExplorer.py (which is also based on the c++ class).
    """

    # possible states
    class _States(Enum):
        S_NO_BDF = auto()
        S_AT_BEGINNING = auto()
        S_READING = auto()
        S_AT_END = auto()

    # possible transitions
    class _Transitions(Enum):
        T_OPEN = auto()
        T_QUERY = auto()
        T_TEST_END = auto()
        T_READ = auto()
        T_READ_NEXT = auto()
        T_READ_ALL = auto()
        T_CLOSE = auto()

    _currentState = _States.S_NO_BDF

    def _getCurrentState(self):
        """
        Returns a string representation of the current state.

        This is useful to enhance the raised exceptions by adding the current state to
        the message.
        """
        result = "Unknown, this should NEVER happen."
        if self._currentState == self._States.S_NO_BDF:
            result = "unopened, no BDF available"
        elif self._currentState == self._States.S_AT_BEGINNING:
            result = "at the beginning of the BDF"
        elif self._currentState == self._States.S_READING:
            result = "reading the BDF"
        elif self._currentState == self._States.S_AT_END:
            result = "at the end of the BDF"
        return result

    def _checkState(self, transition, methodName):
        """
        check that the transition requestioned by methodName is allowed given the current state.

        The _currentState value (a _States enum value) limits what transitions are allowed.
        This method checks that a transition is allowed. The calling method name is provided so
        that if a transition is not allowed that the raised exception has a more useful message.

        raises a BDFReaderException if the transition is not allowed.

        Parameters
        ----------
        transition : _Transitions
            A _Transitions enum value, the transition to check.
        methodName : str
            The name of the calling method, to be used when raising an exception for an illegal transition.

        Raises
        ------
        BDFReaderException :
            When the transition is not allowed by for the _currentState.
        """

        # return when the transition is allowed by the current state
        if self._currentState == self._States.S_NO_BDF:
            if transition == self._Transitions.T_OPEN:
                return

        elif self._currentState == self._States.S_AT_BEGINNING:
            if transition in (
                self._Transitions.T_QUERY,
                self._Transitions.T_TEST_END,
                self._Transitions.T_READ,
                self._Transitions.T_READ_NEXT,
                self._Transitions.T_READ_ALL,
                self._Transitions.T_CLOSE,
            ):
                return

        elif self._currentState == self._States.S_READING:
            if transition in (
                self._Transitions.T_TEST_END,
                self._Transitions.T_READ,
                self._Transitions.T_READ_NEXT,
                self._Transitions.T_READ_ALL,
                self._Transitions.T_QUERY,
                self._Transitions.T_CLOSE,
            ):
                return

        elif self._currentState == self._States.S_AT_END:
            if transition in (
                self._Transitions.T_TEST_END,
                self._Transitions.T_QUERY,
                self._Transitions.T_READ_NEXT,
                self._Transitions.T_READ_ALL,
                self._Transitions.T_CLOSE,
            ):
                return

        # end of if/elif on _currentState

        # any other combination of transition and current state raises this exception
        raise BDFReaderException(
            "Invalid call of method '"
            + methodName
            + "' in the current context: "
            + self._getCurrentState()
            + "."
        )

    def reset(self):
        """
        Reinitializes this instance to it's initial state.

        An open file is closed an all internal values are set to their initial state.
        """

        if self._f is not None:
            if not self._f.closed:
                self._f.close()
            self._f = None
        self._currentState = self._States.S_NO_BDF

        self._boundary_1 = (
            None  # the string indicating the top level boundary definition
        )
        self._currentLine = None  # the line most recently read by _nextLine
        self._integrationIndex = -1  # no integration read yet
        self._integrationStartsAt = -1
        self._path = None  # the path that is opened, when opened
        self._sdmDataHeaderDOM = (
            None  # the initial (main) BDF data header as a DOM instance
        )
        self._bdfHeaderData = (
            BDFHeader()
        )  # initialized from the sdmDataHeader XML via a DOM

    def __init__(self):
        """
        Initialize internal values.

        This instance is not yet connected to a BDF.
        """
        self._path = None  # the path to the BDF
        self._f = None  # the opened file object
        self.reset()

    def open(self, bdfPath):
        """
        Open a file expected to contain BDF data, read and parse the global header.

        On exit the first block of data (subscan, integration, or subintegration) is
        ready to be read by the getData method.

        Parameters
        ----------
        bdfPath : str or MainRow
            The path to the BDF file.

        Raises
        ------
        BDFReaderException :
            When a file has previously been opened. Use 'close' or 'reset' to re-use this instance.
        """

        # only allowed if not already open
        self._checkState(self._Transitions.T_OPEN, "open")

        self._sdmDataHeaderDOM = (
            None  # the initial (main) BDF data header as a DOM instance
        )

        self._path = bdfPath
        try:
            self._f = open(self._path, mode="rb")
        except Exception as exc:
            raise BDFReaderException(
                "Error while opening '"
                + self._path
                + "'. The exception was "
                + str(exc)
            ) from None
        # I don't think this can happen without throwing an exception
        if self._f is None:
            raise BDFReaderException(
                "Unable to open '" + self._path + "'. No exception was raised."
            )

        self._boundary_1 = self._requireMIMEHeader()
        self._requireSDMDataHeaderMIMEPart()
        self._integrationIndex = -1  # no integration read yet

        self._currentState = self._States.S_AT_BEGINNING

    def getPath(self):
        """
        Return the path of the currently opened file. Returns None if no path is opened.
        """
        return self._path

    def getHeader(self):
        """
        Return the BDFHeader instance.

        If not yet open this raises a BDFReaderException
        """

        self._checkState(self._Transitions.T_QUERY, "getHeader")
        return self._bdfHeaderData

    def position(self):
        """
        Returns the current position in bytes of the BDF file.
        """
        if self._f is None:
            return None
        return self._f.tell()

    def close(self):
        """
        Equivalent to reset, closes any opened file and sets the internal values to
        their initial state.
        """
        self.reset()

    def currentIntegrationIndex(self):
        """
        Return the index of the current block of data (subscan, integration, or subintegration).

        This is the integration index of the block of data most recently returned by getSubset

        The indexing is 0 based.
        """

        self._checkState(self._Transitions.T_QUERY, "currentIntegrationIndex")
        return self._integrationIndex

    def currentIntegrationStartsAt(self):
        """
        Return the position in bytes in the file of the current block of data (subscan, integration, or subintegration).

        This is the position of the block of data most recently returned by getSubset
        """

        self._checkState(self._Transitions.T_QUERY, "currentIntegrationIndex")
        return self._integrationStartsAt

    def title(self):
        """
        Return the title found in the primary BDF header
        """

        self._checkState(self._Transitions.T_QUERY, "title")
        return self._bdfHeaderData.getTitle()

    def byteOrder(self):
        """
        Return the byte order found in the primary BDF header.

        Returns
        -------
        A ByteOrder instance set using the byteOrder found in the primary BDF header.
        """

        self._checkState(self._Transitions.T_QUERY, "byteOrder")
        return self._bdfHeaderData.getByteOrder()

    def startTime(self):
        """
        Return the start time found in the primary BDF header.

        Returns
        -------
        An int holding the startTime value (nanoseconds) found in the primary BDF header.
        """

        self._checkState(self._Transitions.T_QUERY, "startTime")
        return self._bdfHeaderData.getStartTime()

    def numTime(self):
        """
        Return the numTime value found in the primary BDF header.

        This is only ever non-zero for packed data.

        Returns
        -------
        An int holding the numTime value found in the primary BDF header.
        """

        self._checkState(self._Transitions.T_QUERY, "numTime")
        return self._bdfHeaderData.getNumTime()

    def dataOID(self):
        """
        Return the dataOID value found in the primary BDF header.
        """

        self._checkState(self._Transitions.T_QUERY, "dataOID")
        return self._bdfHeaderData.getDataOID()

    def execBlockUID(self):
        """
        Return the UID of the ExecBlock found in the primary BDF header.
        """

        self._checkState(self._Transitions.T_QUERY, "execBlockUID")
        return self._bdfHeaderData.getExecBlockUID()

    def execBlockNum(self):
        """
        Return the number of the ExecBlock found in the projectPath in the primary BDF header.
        """

        self._checkState(self._Transitions.T_QUERY, "execBlockNum")
        return self._bdfHeaderData.getExecBlockNum()

    def scanNum(self):
        """
        Return the number of the scan found in the projectPath in the primary BDF header.
        """

        self._checkState(self._Transitions.T_QUERY, "scanNum")
        return self._bdfHeaderData.getScanNum()

    def subscanNum(self):
        """
        Return the number of the subscan found in the projectPath in the primary BDF header.
        """

        self._checkState(self._Transitions.T_QUERY, "subscanNum")
        return self._bdfHeaderData.getSubscanNum()

    def numAntenna(self):
        """
        Return the number of antenna found in the projectPath in the primary BDF header.
        """

        self._checkState(self._Transitions.T_QUERY, "numAntenna")
        return self._bdfHeaderData.getNumAntenna()

    def correlationMode(self):
        """
        Return the correlation mode found in the primary BDF header.

        Returns a CorrelationMode enumeration instance.
        """

        self._checkState(self._Transitions.T_QUERY, "correlationMode")
        return self._bdfHeaderData.getCorrelationMode()

    def spectralResolutionType(self):
        """
        Return the spectral resolution type found in the primary BDF header.

        spectralResolutionType is optional in a BDF header. The return
        value is None if that value is not found.

        Returns a SpectralResolutionType enumeration instance or None if
        no spectralResolutionType value is found (non-correlator data).
        """

        self._checkState(self._Transitions.T_QUERY, "spectralResolutionType")
        return self._bdfHeaderData.getSpectralResolutionType()

    def processorType(self):
        """
        Return the processor type found in the primary BDF header.

        Returns a ProcessorType enumeration instance
        """

        self._checkState(self._Transitions.T_QUERY, "processorType")
        return self._bdfHeaderData.getProcessorType()

    def correlatorType(self):
        """
        Return the correlator type found in the primary BDF header.

        Returns a CorrelatorType enumeration instance
        """

        self._checkState(self._Transitions.T_QUERY, "correlatorType")
        return self._bdfHeaderData.correlatorType()

    def hasPackedData(self):
        """
        True if the binary data are all packed in one subset covering multipled times.

        Returns a boolean.
        """

        self._checkState(self._Transitions.T_QUERY, "hasPackedData")
        return self._bdfHeaderData.hasPackedData()

    def isTP(self):
        """
        True if this is total power data.

        Returns a boolean.
        """

        self._checkState(self._Transitions.T_QUERY, "isTP")
        return self._bdfHeaderData.isTP()

    def isWVR(self):
        """
        True if this is WVR data.

        Returns a boolean.
        """

        self._checkState(self._Transitions.T_QUERY, "isWVR")
        return self._bdfHeaderData.isWVR()

    def isCorrelation(self):
        """
        True if the processorType is CORRELATOR

        Returns a boolean.
        """

        self._checkState(self._Transitions.T_QUERY, "isCorrelation")
        return self._bdfHeaderData.isCorrelation()

    def hasSubset(self):
        """
        Returns True if and only if there are still data to read in the BDF file.
        """
        self._checkState(self._Transitions.T_TEST_END, "hasSubset")
        atEnd = self._currentLine == (b"--" + self._boundary_1 + b"--")
        if atEnd:
            self._currentState = self._States.S_AT_END
        return not atEnd

    def getSubset(self):
        """
        Returns an SDM Data Subset (one integration) as a dictionary.

        This reads the next subset found at the current location in the file.
        """
        self._checkState(self._Transitions.T_READ, "getSubset")
        self._integrationIndex += 1
        sdmSubset = self._requireSDMDataSubsetMIMEPart()
        # this line isn't used, but the file should be advanced to the next line
        line = self._nextLine()
        self._currentState = self._States.S_READING
        return sdmSubset

    # the c++ code offers nextSubsets and allRemainingSubsets methods that return
    # a reference to a vector of subsets. Here, that would be implemented by
    # repeated calls to getSubset until hasSubset is False or (for nextSubsets)
    # the requested number of subsets had been read, with the result returned as
    # a list. There's minimal benefit over simply calling getSubset as needed so
    # they are not implemented here. That is where the T_READ_NEXT and T_READ_ALL
    # transitions are used in the c++ code.

    def _nextLine(self):
        """
        A method which reads the next line of text and returns it.
        If the line ends in a newline, it is stripped before the line is returned.
        This method is only for internal use.
        """
        line = self._f.readline()
        # line is bytes type, comparision with "/n" or b"/n" doesn't work, but endswith does
        if line.endswith(b"\n"):
            line = line[:-1]
        self._currentLine = line
        return line

    def _headerField2Pair(self, hf):
        """
        A method which decomposes a MIME header into a (name, value) pair and returns that pair.
        Leading and trailing whitespace is removed from name and value. A colon separates the name from the value.
        This method is only for internal use.
        """
        name = None
        value = None
        colonIndex = hf.find(b":")
        if colonIndex == -1:
            raise BDFReaderException(
                "could not detect a well formed MIME header field in '" + str(hf) + "'"
            )
        if colonIndex > 0:
            name = hf[:colonIndex]
            name = name.strip()
        if colonIndex < len(hf) - 1:
            value = hf[colonIndex + 1 :]
            value = value.strip()
        # null values are OK
        return (name, value)

    def _requireHeaderField(self, hf):
        """
        A method which consumes a MIME header and returns the (name, value) pair it has found in that header.
        This method is only for internal use.
        """
        name, value = self._headerField2Pair(self._nextLine())
        if name.upper() != codecs.encode(hf, "utf-8"):
            raise BDFReaderException(
                "Did not find expected field '"
                + hf
                + "' in '"
                + self._currentLine.decode("utf-8")
                + "'."
            )
        return name, value

    def _unquote(self, s):
        """
        A utility method which returns an unquoted version of a quoted string (leading and trailing quotes are removed)
        s is assumed to b a bytes type
        This method is only for internal use.
        """
        if len(s) < 2:
            return s
        if (s[0] == ord('"') and s[-1] == ord('"')) or (
            s[0] == ord("'") and s[-1] == ord("'")
        ):
            return s[1:-1]
        return s

    def _skipUntilEmptyLine(self, maxSkips):
        """
        A method which skips all the lines read from the current position until it finds an
        empty line or it reaches the maximum number of skips.
        This method is only for inernal use.
        """
        numSkip = 0
        line = self._nextLine()
        while len(line) > 0 and numSkip <= maxSkips:
            line = self._nextLine()
            numSkip += 1
        if numSkip > maxSkips:
            raise BDFReaderException(
                "could not find an empty line in less than " + str(maxSkips + 1)
                << " lines."
            )

    def _accumulateUntilBoundary(self, boundary, maxLines):
        """
        A method which accumulates all of the lines of text until it reaches a
        boundary line whose value is equal to the parameter 'boundary' or
        until it reaches a number of read lines equal to maxLines.
        Returns the lines ready in one value (bytes type).
        This method is only for inernal use.
        """
        numLines = 0
        line = self._nextLine()
        result = b""
        while numLines <= maxLines and line.find(b"--" + boundary) != 0:
            result += line
            numLines += 1
            line = self._nextLine()

        if numLines > maxLines:
            raise BDFReaderException(
                "could not find the boundary string '"
                + boundary.decode("utf-8")
                + "' in less than "
                + str(maxLines + 1)
                + " lines."
            )

        return result

    def _requireBoundary(self, boundary, maxLines):
        """
        A method which reads lines of text until it finds a boundary line whose value is
        equal to the parameter 'boundary' or until it reaches a number of read lins
        equal to maxLines.
        Returns nothing.
        This method is only for internal use.
        """
        numLines = 0
        line = self._nextLine()
        while numLines <= maxLines and line.find(b"--" + boundary) != 0:
            numLines += 1
            line = self._nextLine()

        if numLines > maxLines:
            raise BDFReaderException(
                "could not find the boundary string '"
                + boundary.decode("utf-8")
                + "' in less than "
                + str(maxLines + 1)
                + " lines."
            )

    def _requireBoundaryInCT(self, ctValue):
        """
        A method which looks for the BOUNDARY definition in a CONTENT-TYPE MIME header and returns
        the unquoted version of that definition.
        This method is only for internal use.
        """
        cvValueItems = [item.strip() for item in ctValue.split(b";")]
        cvValueItemsNameValue = [item.partition(b"=") for item in cvValueItems]
        boundaryValues = [
            item[2]
            for item in cvValueItemsNameValue
            if item[0].upper() == b"BOUNDARY" and item[2] != ""
        ]
        if boundaryValues == []:
            raise BDFReaderException(
                "count not found a boundary definition in '"
                + ctValue.decode("utf-8")
                + "'."
            )
        else:
            return self._unquote(boundaryValues[0])

    def _requireMIMEHeader(self):
        """
        A method which consumes the toplevel MIME header present in the BDF.
        It returns the toplevel BOUNDARY definition.
        This method is only for internal use.
        """
        # "MIME-VERSION: 1.0"
        line = self._nextLine()
        name, value = self._headerField2Pair(line)
        if not line.endswith(b"IME-Version: 1.0"):
            raise BDFReaderException(
                "'MIME-VERSION: 1.0' missing at the very beginning of the file '"
                + self._path
                + "'."
            )

        # CONTENT-TYPE
        name, value = self._requireHeaderField("CONTENT-TYPE")

        # extract level 1 boundary from value
        self._boundary_1 = self._requireBoundaryInCT(value)

        # CONTENT-DESCRIPTION
        name, value = self._requireHeaderField("CONTENT-DESCRIPTION")

        # CONTENT_LOCATION
        name, value = self._requireHeaderField("CONTENT-LOCATION")

        # skip until an empty line is found, skipping at most 10 lines
        self._skipUntilEmptyLine(10)

        return self._boundary_1

    def _requireSDMDataHeaderMIMEPart(self):
        """
        Reads the 1st part (in the MIME meaning) of the BDF, extracts its content,
        which is an XML document known as the SDM data header, and parses it into
        a DOM document.
        Returns nothing.
        This method is only for internal use.
        """
        # Requires the presence of boundary_1
        self._requireBoundary(self._boundary_1, 0)

        # ignore header fields (do not require these)
        # CONTENT-TYPE, CONTENT-TRANSFER-ENCODING, CONTENT-LOCATION

        # look for an empty line at most 10 lines from the the current location
        self._skipUntilEmptyLine(10)

        # extract the header, everything until the next boundary but at most 100 lines
        sdmDataHeader = self._accumulateUntilBoundary(self._boundary_1, 100)

        # parse the XML into a DOM document
        dom = minidom.parseString(sdmDataHeader)
        self._sdmDataHeaderDOM = dom

        # the primary data header (sdmDataHeader element)
        try:
            dataHeaderElem = dom.getElementsByTagName("sdmDataHeader")[0]
            self._bdfHeaderData.fromDOM(dataHeaderElem)

        except Exception as exc:
            import traceback
            traceback.print_exc()
            raise BDFReaderException(
                "Unexpected exception while parsing the main BDF header: '"
                + str(exc)
                + "."
            ) from None

        # it's useful to construct a dict of the sizes of the binary parts which have non-zero size
        self._binaryPartSize = {}
        for partName in self._bdfHeaderData.getBinaryTypes():
            if self._bdfHeaderData.hasBinary(partName):
                self._binaryPartSize[partName] = self._bdfHeaderData.getSize(partName)

    def _skipAsLongAsLineStartsWith(self, startStr):
        """
        Skip so long as the current line starts with startStr (as a bytes type).

        This method name comes from c++ and is confusing. It's intended to be used for
        the case where there are 2 successive MIME boundary occurrences (CAS-8151).
        It skips ahead using nextline until the currentLine does not start with that
        string of characters. Then it sets the position in the file to the start of
        the previous line read, without reading that line. So, currentLine will reflect
        the line that was just read but nextLine will re-read that same line.

        This returns nothing
        """
        curpos = 0
        while self._currentLine.find(startStr) == 0:
            curpos = self.position()
            self._nextLine()

        self._setPosition(curpos)

    def _requireSDMDataSubsetMIMEPart(self):
        self._integrationStartsAt = self.position()

        # CAS-8151, apparently there are cases where there are two occurrences of the MIME bouneary instead of only one
        self._skipAsLongAsLineStartsWith(b"--" + self._boundary_1)
        # CONTENT-TYPE
        name, value = self._requireHeaderField("CONTENT-TYPE")
        # that gives boundary_2
        self._boundary_2 = self._requireBoundaryInCT(value)

        # CONTENT-DESCRIPTION
        name, value = self._requireHeaderField("CONTENT-DESCRIPTION")

        # and move to boundary_2, must be within the next 10 lines
        self._requireBoundary(self._boundary_2, 10)
        # and skip until the empty line is reached, or 10 lines
        self._skipUntilEmptyLine(10)

        # read the SDM Data Subset header, assume it can't be more than 100 lines
        sdmDataSubsetHeader = self._accumulateUntilBoundary(self._boundary_2, 100)

        sdmDataSubsetHeaderDOM = minidom.parseString(sdmDataSubsetHeader)
        # it's all in the firstChild node
        sdmDataSubsetHeaderDOM = sdmDataSubsetHeaderDOM.firstChild
        if sdmDataSubsetHeaderDOM.nodeName != "sdmDataSubsetHeader":
            raise BDFReaderException(
                "Unexpected XML node found where sdmDataSubsetHeader is expected.: %s"
                % sdmDataSubsetHeaderDOM.nodeName
            )
        projectPath = sdmDataSubsetHeaderDOM.attributes.getNamedItem(
            "projectPath"
        ).value
        projectPathParts = projectPath.split("/")
        # drop the last part if projectPath ends in a "/"
        if projectPath.endswith('/'):
            projectPathParts = projectPathParts[:-1]
        numPathParts = len(projectPathParts)
        if self.isCorrelation():
            # correlator data should have 4 of 5 parts here
            if ((numPathParts < 4) or (numPathParts > 5)):
                raise BDFReaderException(
                    "Invalid string for projectPath, expectes 4 or 5 parts '"
                    + projectPath
                    + "'"
                )
        else:
            # TP data should have 3 or 4 parts here
            if ((numPathParts < 3) or (numPathParts > 4)):
                raise BDFReaderException(
                    "Invalid string for projectPath, expects 3 or 4 parts '"
                    + projectPath
                    + "'"
                    )
            
        execBlockNum = int(projectPathParts[0])
        scanNum = int(projectPathParts[1])
        subscanNum = int(projectPathParts[2])
        intNum = 0
        subIntNum = 0
        if numPathParts > 3:
            intNum = int(projectPathParts[3])
        if numPathParts > 4:
            subIntNum = int(projectPathParts[4])

        # the first 3 values should match those for this BDF
        if (
            (execBlockNum != self._bdfHeaderData.getExecBlockNum())
            or (scanNum != self._bdfHeaderData.getScanNum())
            or (subscanNum != self._bdfHeaderData.getSubscanNum())
        ):
            raise BDFReaderException(
                "The project path of this data subset '"
                + projectPath
                + "' is not compatible with the project path announced in the global header"
                + " '"
                + self._bdfHeaderData.projectPath()
                + "'"
            )

        # TBD : SDMDataSubset should be a class, reset it here

        aborted = False
        stopTime = None
        abortReason = None
        abortedObservationElements = sdmDataSubsetHeaderDOM.getElementsByTagName(
            "abortedObservation"
        )
        if len(abortedObservationElements) > 0:
            # aborted subscan
            aborted = True
            # it must have stopTime and reason
            abortedNode = abotedObservationElements[0]
            stopTime = abortedNode.getElementsByTagName("stopTime")
            if stopTime is None or len(stopTime) == 0:
                raise BDFReaderException(
                    "expected 'stopTime' element not found in aborted subscan at integrationIndex "
                    + str(self._integrationIndex)
                )
            stopTime = int(stopTime[0].childNodes[0].nodeValue)
            reason = abortedNode.getElementsByTagName("reason")
            if reason is None or len(reason) == 0:
                raise BDFReaderException(
                    "expected 'reason' element not found in aborted subscan at integrationIndex "
                    + str(self._integrationIndex)
                )
            abortReason = reason[0].childNodes[0].nodeValue

        schedulePeriodTime = sdmDataSubsetHeaderDOM.getElementsByTagName(
            "schedulePeriodTime"
        )
        if schedulePeriodTime is None or len(schedulePeriodTime) == 0:
            raise BDFReaderException(
                "expected 'schedulePeriodTime' element not found in subscan at integrationIndex "
                + str(self._integrationIndex)
            )
        schedulePeriodTime = schedulePeriodTime[0]
        integrationMidpoint = int(
            (schedulePeriodTime.getElementsByTagName("time"))[0].childNodes[0].nodeValue
        )
        integrationInterval = int(
            (schedulePeriodTime.getElementsByTagName("interval"))[0]
            .childNodes[0]
            .nodeValue
        )

        # if it's aborted, this can probably be skipped, but it should also be harmless to not skip it just in case there's more there to be skipped over
        # no aborted scans available yet to test this on

        actualTimesDesc = {}
        actualTimesDesc["present"] = False
        actualTimesDesc["startsAt"] = -1
        actualTimesDesc["arr"] = None
        actualTimesDesc["type"] = "INT64_TYPE"
        actualTimesDesc["np_type"] = np.dtype(np.int64)

        actualDurationsDesc = {}
        actualDurationsDesc["present"] = False
        actualDurationsDesc["startsAt"] = -1
        actualDurationsDesc["arr"] = None
        actualDurationsDesc["type"] = "INT64_TYPE"
        actualDurationsDesc["np_type"] = np.dtype(np.int64)

        crossDataDesc = {}
        crossDataDesc["present"] = False
        crossDataDesc["startsAt"] = -1
        crossDataDesc["arr"] = None
        crossDataDesc["type"] = None
        crossDataDesc["np_type"] = None

        # the actual crossDataDesc varies among these types
        npInt16 = np.dtype(np.int16)
        npInt32 = np.dtype(np.int32)
        npFloat32 = np.dtype(np.float32)

        autoDataDesc = {}
        autoDataDesc["present"] = False
        autoDataDesc["startsAt"] = -1
        autoDataDesc["arr"] = None
        autoDataDesc["type"] = "FLOAT32_TYPE"
        autoDataDesc["np_type"] = np.dtype(np.float32)

        flagsDesc = {}
        flagsDesc["present"] = False
        flagsDesc["startsAt"] = -1
        flagsDesc["arr"] = None
        flagsDesc["type"] = "INT32_TYPE"
        flagsDesc["np_type"] = np.dtype(np.int32)

        zeroLagsDesc = {}
        zeroLagsDesc["present"] = False
        zeroLagsDesc["startsAt"] = -1
        zeroLagsDesc["arr"] = None
        zeroLagsDesc["type"] = "FLOAT32_TYPE"
        zeroLagsDesc["np_type"] = np.dtype(np.float32)

        # adjust the numpy data types when the byte order is not native
        if not self._bdfHeaderData.getByteOrder().isNative():
            np_byteOrder = "<"
            if self._bdfHeaderData.getByteOrder().getByteOrder() == "big":
                np_byteOrder = ">"

            actualTimesDesc["np_type"] = actualTimesDesc["np_type"].newbyteorder(
                np_byteOrder
            )
            actualDurationsDesc["np_type"] = actualDurationsDesc[
                "np_type"
            ].newbyteorder(np_byteOrder)
            autoDataDesc["np_type"] = autoDataDesc["np_type"].newbyteorder(np_byteOrder)
            flagsDesc["np_type"] = flagsDesc["np_type"].newbyteorder(np_byteOrder)
            zeroLagsDesc["np_type"] = zeroLagsDesc["np_type"].newbyteorder(np_byteOrder)
            npInt16 = npInt16.newbyteorder(np_byteOrder)
            npInt32 = npInt32.newbyteorder(np_byteOrder)
            npFloat32 = npFloat32.newbyteorder(np_byteOrder)

        dataPath = None

        done = False
        while not done:
            name, value = self._requireHeaderField("CONTENT-TYPE")
            name, value = self._requireHeaderField("CONTENT-LOCATION")

            # what part is this?
            result = re.match(
                b"(([0-9]+/)+)(actualDurations|actualTimes|autoData|crossData|zeroLags|flags)\\.bin",
                value.lstrip().rstrip(),
            )
            if result == None:
                raise BDFReaderException(
                    "Could not identify the part name in '"
                    + value.decode("utf-8")
                    + "'."
                )

            binaryPartName = result.group(3)
            dataPath = result.group(1)

            if binaryPartName.decode("utf-8") not in self._binaryPartSize:
                raise BDFReaderException(
                    "The size of '"
                    + binaryPartName.decode("utf-8")
                    + "' was not announced in the data header!"
                )
            if self._binaryPartSize[binaryPartName.decode("utf-8")] == 0:
                raise BDFReaderException(
                    "The size of '"
                    + binaryPartName.decode("utf-8")
                    + "' was announced as null. I was not expecting a '"
                    + binaryPartName.decode("utf-8")
                    + "' attachment here."
                )

            if binaryPartName == b"crossData":
                # crossData must be in the minidom and it must have a type element
                elements = sdmDataSubsetHeaderDOM.getElementsByTagName("crossData")
                if len(elements) == 0:
                    raise BDFReaderException(
                        "Missing expected 'crossData' element in '%s'"
                        % sdmDataSubsetHeaderDOM.toprettyxml()
                    )

                crossDataType = elements[0].getAttribute("type")
                if len(crossDataType) == 0:
                    raise BDFReaderException(
                        "Missing expected 'type' attribute in element '%s'."
                        % elements[0].nodeName
                    )

                crossDataDesc["type"] = crossDataType

            self._skipUntilEmptyLine(10)

            # TBD - binaryPartName can be used to know the "type" and then there should be
            # a dict of type to numberOfBytesPerValue, would require restructuring the dicts used here
            numberOfBytesPerValue = None
            if binaryPartName == b"actualDurations" or binaryPartName == b"actualTimes":
                numberOfBytesPerValue = 8
            elif binaryPartName == b"autoData":
                numberOfBytesPerValue = 4
            elif binaryPartName == b"crossData":
                if crossDataType == "INT16_TYPE":
                    numberOfBytesPerValue = 2
                    crossDataDesc["np_type"] = npInt16
                elif crossDataType == "INT32_TYPE":
                    numberOfBytesPerValue = 4
                    crossDataDesc["np_type"] = npInt32
                elif crossDataType == "FLOAT32_TYPE":
                    numberOfBytesPerValue = 4
                    crossDataDesc["np_type"] = npFloat32
            elif binaryPartName == b"flags":
                numberOfBytesPerValue = 4
            elif binaryPartName == b"zeroLags":
                numberOfBytesPerValue = 4

            # I don't believe this can ever happen, TBD - raise a better exception here
            if numberOfBytesPerValue is None:
                raise BDFReaderException(
                    "unrecognized binary part name or data type for that part : '"
                    + binaryPartName.decode("utf-8")
                    + "'."
                )

            numberOfElementsToRead = self._binaryPartSize[
                binaryPartName.decode("utf-8")
            ]
            numberOfBytesToRead = numberOfBytesPerValue * numberOfElementsToRead

            # with restructuring, this can also be cleaner - TBD
            # actual number of bytes read
            nReadBytes = None
            if binaryPartName == b"zeroLags":
                zeroLagsDesc["present"] = True
                zeroLagsDesc["startsAt"] = self.position()
                dt = zeroLagsDesc["np_type"]
                zeroLagsDesc["arr"] = np.fromfile(
                    self._f, dtype=dt, count=numberOfElementsToRead
                )
                nReadBytes = zeroLagsDesc["arr"].size * numberOfBytesPerValue
            elif binaryPartName == b"actualTimes":
                actualTimesDesc["present"] = True
                actualTimesDesc["startsAt"] = self.position()
                dt = actualTimesDesc["np_type"]
                actualTimesDesc["arr"] = np.fromfile(
                    self._f, dtype=dt, count=numberOfElementsToRead
                )
                nReadBytes = len(actualTimesDesc["arr"]) * numberOfBytesPerValue
            elif binaryPartName == b"actualDurations":
                actualDurationsDesc["present"] = True
                actualDurationsDesc["startsAt"] = self.position()
                dt = actualDurationsDesc["np_type"]
                actualDurationsDesc["arr"] = np.fromfile(
                    self._f, dtype=dt, count=numberOfElementsToRead
                )
                nReadBytes = len(actualDurationsDesc["arr"]) * numberOfBytesPerValue
            elif binaryPartName == b"crossData":
                crossDataDesc["present"] = True
                crossDataDesc["startsAt"] = self.position()
                dt = crossDataDesc["np_type"]
                crossDataDesc["arr"] = np.fromfile(
                    self._f, dtype=dt, count=numberOfElementsToRead
                )
                nReadBytes = len(crossDataDesc["arr"]) * numberOfBytesPerValue
            elif binaryPartName == b"autoData":
                autoDataDesc["present"] = True
                autoDataDesc["startsAt"] = self.position()
                dt = autoDataDesc["np_type"]
                autoDataDesc["arr"] = np.fromfile(
                    self._f, dtype=dt, count=numberOfElementsToRead
                )
                nReadBytes = len(autoDataDesc["arr"]) * numberOfBytesPerValue
            elif binaryPartName == b"flags":
                flagsDesc["present"] = True
                flagsDesc["startsAt"] = self.position()
                dt = flagsDesc["np_type"]
                flagsDesc["arr"] = np.fromfile(
                    self._f, dtype=dt, count=numberOfElementsToRead
                )
                nReadBytes = len(flagsDesc["arr"]) * numberOfBytesPerValue
            else:
                # should never reach here ! but just in case
                bytes = self._f.read(numberOfBytesToRead)
                nReadBytes = len(bytes)
                print(
                    "Unknown binary part name '(%s)' with %s bytes to read, skipping in case it's possible to continue, this should never happen!"
                    % (binaryPartName.decode("utf-8"), numberOfBytesToRead)
                )

            if nReadBytes < numberOfBytesToRead:
                raise BDFReaderException(
                    "End of file reached while reading binary attachment '"
                    + binaryPartName.decode("utf")
                    + "'."
                )

            line = (
                self._nextLine()
            )  # absorb the nl right after the last byte of the binary attachment
            line = self._nextLine()  # this should be boundary_2

            if line.find(b"--" + self._boundary_2.strip(b'"')) != 0:
                raise BDFReaderException(
                    "Processing integration # "
                    + str(self._integrationIndex)
                    + ":Unexpected '"
                    + line.decode("utf-8")
                    + "' after the binary part '"
                    + binaryPartName.decode("utf-8")
                    + "'."
                )

            # is this the end?
            done = line == b"--" + self._boundary_2.strip(b'"') + b"--"

        # TBD - this struct could be assembed earlier and used more efficiently in the middle
        # TBD - pyBDFExplorer returns sdmDataSubsetHeaderDOM here, is that useful?
        return {
            "projectPath": projectPath,
            "integrationNumber": intNum,
            "subIntegrationNumber": subIntNum,
            "midpointInNanoSeconds": integrationMidpoint,
            "intervalInNanoSeconds": integrationInterval,
            "aborted": aborted,
            "stopTime": stopTime,
            "abortReason": abortReason,
            "actualTimes": actualTimesDesc,
            "actualDurations": actualDurationsDesc,
            "crossData": crossDataDesc,
            "autoData": autoDataDesc,
            "flags": flagsDesc,
            "zeroLags": zeroLagsDesc,
        }

    def _setPosition(self, newpos):
        """
        Set the position of the BDF to the location given by newpos (bytes).
        This is intended for inernal use because it may confuse the public methods if this is
        used out of the normal sequence.
        """
        self._f.seek(newpos, 0)

    def printSubset(self, subset):
        # not for release
        # prints a subset, prining up to the first 10 elements of each type
        # does not use self
        print("projectPath = " + subset["projectPath"])
        print("time = %s" % subset["midpointInNanoSeconds"])
        print("interval = %s" % subset["intervalInNanoSeconds"])
        floatItems = ["autoData", "zeroLags"]
        if "crossData" in subset and subset["crossData"]["present"]:
            print("crossDataType = " + subset["crossData"]["type"])
            if subset["crossData"]["type"] == "FLOAT32_TYPE":
                floatItems.append("crossData")
        print("Binary attachments :")
        for item in [
            "actualTimes",
            "actualDurations",
            "flags",
            "crossData",
            "autoData",
            "zeroLags",
        ]:
            if (item in subset) and subset[item]["present"]:
                nOut = min(10, subset[item]["arr"].size)
                outStr = "%s (%s values ) = " % (
                    (item[0].upper() + item[1:]),
                    subset[item]["arr"].size,
                )
                nOut = min(10, subset[item]["arr"].size)
                floatFormat = item in floatItems
                for itemVal in subset[item]["arr"][0:nOut]:
                    if floatFormat:
                        outStr = outStr + " " + f"{itemVal:.6f}"
                    else:
                        outStr = outStr + " " + str(itemVal)
                if nOut < subset[item]["arr"].size:
                    outStr = outStr + "..."
                print(outStr)
