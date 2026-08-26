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
#
# File TableStreamReader.py
#

from enum import Enum, auto
import codecs
from xml.dom import minidom
import os

from pyasdm import ASDM
from pyasdm import PointingTable
from pyasdm import PointingRow

from pyasdm.ByteOrder import ByteOrder
from pyasdm.EndianInput import EndianInput
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException


class TableStreamReader:
    """
    Follows the c++ TableStreamReader class.

    Read a file containing an ASDM table as a stream.

    The purpose of this class is to provide the programmer with a way to read a file containing an ASDM table by successive
    slices. Each slice is transformed into the in memory representation of the rows which have been read. A slice can be specified
    in two ways :

    A number of rows. See method nextNrows.
    A number of bytes. See method untilNBytes.

    Remarks
    This class has been meant as an alternative to the historical ASDM methods getXXX which load
    entirely the tables into memory.
    This class allows to read a table completely independenty of the ASDM it belongs to and of the other tables of the ASDM.

    In the c++, this is a templated class, where the template T gives the table class and R the row class.

    For demonstration here I will use the PointingTable and PointRow classes as fixed here.

    The next step will be to merge these capabilities into those classes.  Likely that only makes
    sense if the unique row checking part is disabled, which it should probably default to in all cases.

    Not explicitly mentioned in the comments in the c++ code, but this assumes the
    table is stored in binary form. The table name is required to end in '.bin'
    """

    # private values in the c++ class
    _boundary_1 = ""  # initially unset
    _tablePath = ""  # the path to the table
    _tableFile = None  # the file object, when opened
    _currentLine = None  # the most recent line
    _fileSizeInBytes = None
    _endBoundarySizeInBytes = None
    _eis = None  # EndianInput instance
    _attributesSeq = None  # attributes list
    _asdm = None  # the parent ASDM
    _rows = []  # a list of rows that have been read in this chunk
    _whereRowsStart = None  # location in the file at the start of the rows

    # possible states
    class _States(Enum):
        S_CLOSED = auto()
        S_OPENED = auto()

    # possible transitions
    class _Transitions(Enum):
        T_OPEN = auto()
        T_CHECK = auto()
        T_RESET = auto()
        T_READ = auto()
        T_CLOSE = auto()

    _currentState = _States.S_CLOSED

    def _checkState(self, transition, methodName):
        """
        check that the transition requested by methodName is allowed given the current state.

        The _currentState value (a _States enum value) limits what transitions are allowed.
        This method checks that a transition is allowed. The calling method name
        is provided so that if a transition is not allowed that the raised exception has a more
        useful message.

        raises ConversionException if the transition is not allowed.

        Parameters
        ----------
        transition : _Transitions
            A _Transitions enum value, the transition to check.
        methodName : str
            The name of the calling method, to be used when raising an exception for an illegal transition.

        Raises
        ------
        ConversionException :
            When the transition is not allowed for by the _currentState.
        """

        # return for all of the cases where the transition is allowed
        if self._currentState == self._States.S_CLOSED:
            if transition == self._Transitions.T_OPEN:
                return

        elif self._currentState == self._States.S_OPENED:
            if transition in (
                self._Transitions.T_CHECK,
                self._Transitions.T_RESET,
                self._Transitions.T_READ,
                self._Transitions.T_CLOSE,
            ):
                return

        # if it gets here, it's not allowed
        raise ConversionException(
            "Invalid call of method '"
            + methodName
            + "' in the current context: "
            + self._getCurrentState()
            + "."
        )

    def _getCurrentState(self):
        """
        Returns a string representation of the current state.

        This is useful to enhance the raised exceptions by adding the current state to
        the message.
        """
        result = "Unknown, this should NEVER happen."
        if self._currentState == self._States.S_CLOSED:
            result = "closed"
        elif self._currentState == self._States.S_OPENED:
            result = "opened"

        return result

    def _clear(self):
        self._rows = []

    def __init__(self):
        """
        Initialize internal values.
        """
        self._currentState = self._States.S_CLOSED
        self._readbuffer = None
        self._boundary_1 = ""

    def _nextLine(self):
        """
        A method which reads the next line of text and returns it.
        If the line ends in a newline, it is stripped before the line is returned.
        This method is only for internal use.
        """
        line = self._tableFile.readline()
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
            raise ConversionException(
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
            raise ConversionException(
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
            raise ConversionException(
                "count not found a boundary definition in '"
                + ctValue.decode("utf-8")
                + "'."
            )
        else:
            return self._unquote(boundaryValues[0])

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
            raise ConversionException(
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
            raise ConversionException(
                "could not find the boundary string '"
                + boundary.decode("utf-8")
                + "' in less than "
                + str(maxLines + 1)
                + " lines."
            )

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
            raise ConversionException(
                "could not find an empty line in less than " + str(maxSkips + 1)
                << " lines."
            )

    def _requireMIMEHeader(self):
        """
        A method which consumes the toplevel MIME header present in the binary file.
        It returns the toplevel BOUNDARY definition.
        This method is only for internal use.
        """
        # "MIME-VERSION: 1.0"
        line = self._nextLine()
        name, value = self._headerField2Pair(line)
        if not line.endswith(b"IME-Version: 1.0"):
            raise ConversionException(
                "'MIME-VERSION: 1.0' missing at the very beginning of the file '"
                + self._path
                + "'."
            )

        # CONTENT-TYPE
        name, value = self._requireHeaderField("CONTENT-TYPE")

        # extract level 1 boundary from value
        boundary_1 = self._requireBoundaryInCT(value)

        # skip until an empty line is found, skipping at most 10 lines
        self._skipUntilEmptyLine(10)

        return boundary_1

    def open(self, directory):
        """
        Open a file expected to contain an ASDM table of type PointingTable
        with rows of type PointingRow (the c++ is templated on those as T and R,
        this is a specific example).

        Paramters
        ---------
        directory : str
            The path to the directory containing the table bin file, Pointing.bin
        """

        # must not already be opened
        self._checkState(self._Transitions.T_OPEN, "open")

        self._tablePath = directory + "/" + "Pointing" + ".bin"

        try:
            self._tableFile = open(self._tablePath, "rb")
        except Exception as exc:
            raise ConversionException(
                "Error while opening "
                + self._tablePath
                + ". The exception was "
                + str(exc),
                "Pointing",
            )

        # determine the size of the file.
        self._fileSizeInBytes = os.path.getsize(self._tablePath)

        # and start by parsing the content.
        self._boundary_1 = self._requireMIMEHeader()

        self._requireBoundary(self._boundary_1, 0)

        self._skipUntilEmptyLine(10)
        xmlHeader = self._accumulateUntilBoundary(self._boundary_1, 100)

        xmldom = minidom.parseString(xmlHeader)

        if not xmldom.hasChildNodes():
            # should probably close this here
            raise ConversionException("XML is not properly structured.", "Pointing")

        self._attributesSeq = []
        byteOrderStr = None
        versionStr = "-1"

        hdrdom = xmldom.firstChild
        if hdrdom.nodeName == "ASDMBinaryTable":
            # old style of binary data
            # assume Big_Endian and the default order of the elements
            byteOrderStr = "Big_Endian"

            self._attributesSeq.append("antennaId")
            self._attributesSeq.append("timeInterval")
            self._attributesSeq.append("numSample")
            self._attributesSeq.append("encoder")
            self._attributesSeq.append("pointingTracking")
            self._attributesSeq.append("usePolynomials")
            self._attributesSeq.append("timeOrigin")
            self._attributesSeq.append("numTerm")
            self._attributesSeq.append("pointingDirection")
            self._attributesSeq.append("target")
            self._attributesSeq.append("offset")
            self._attributesSeq.append("pointingModelId")
            self._attributesSeq.append("overTheTop")
            self._attributesSeq.append("sourceOffset")
            self._attributesSeq.append("sourceOffsetReferenceCode")
            self._attributesSeq.append("sourceOffsetEquinox")
            self._attributesSeq.append("sampledTimeInterval")
        else:
            # insist that this is a Pointing table
            if hdrdom.nodeName != "PointingTable":
                # should probably close this here
                raise ConversionException(
                    "XML Header is not from the expected table.", "Pointing"
                )

            # schemaVersion becomes versionStr
            if (
                hdrdom.hasAttributes()
                and hdrdom.attributes.getNamedItem("schemaVersion") is not None
            ):
                versionStr = hdrdom.attributes.getNamedItem("schemaVersion").value

            if not hdrdom.hasChildNodes():
                # should probably close this here
                raise ConversionException(
                    "The XML header is missing all of the expected elements.",
                    "Pointing",
                )

            # loop through the child nodes, looking for BuldStoreRef and Attributes
            for hdrnode in hdrdom.childNodes:
                if hdrnode.nodeName == "BulkStoreRef":
                    if byteOrderStr is not None:
                        # should probably close this here
                        raise ConversionException(
                            "More than one BulkStoreRef element seen. Invalid XML header.",
                            "Pointing",
                        )
                    if not hdrnode.hasAttributes():
                        # should probably close this here
                        raise ConversionException(
                            "BulkStoreRef does not contain any attributes. Invalid XML header.",
                            "Pointing",
                        )
                    byteOrderAttr = hdrnode.attributes.getNamedItem("byteOrder")
                    if byteOrderAttr is None:
                        # should probably close this here
                        raise ConversionException(
                            "byteOrder attribute not found in BulkStoreRef element. Invalid XML header.",
                            "Pointing",
                        )
                    byteOrderStr = byteOrderAttr.value
                elif hdrnode.nodeName == "Attributes":
                    if len(self._attributesSeq) > 0:
                        # should probably close this here
                        raise ConversionException(
                            "More than one Attributes node seen. Invalid XML header.",
                            "Pointing",
                        )
                    if not hdrnode.hasChildNodes():
                        # should probably close this here
                        raise ConversionException(
                            "Attributes element has no child nodes. Invalid XML header.",
                            "Pointing",
                        )
                    for attrnode in hdrnode.childNodes:
                        if attrnode.nodeType == attrnode.ELEMENT_NODE:
                            self._attributesSeq.append(str(attrnode.nodeName))

        if byteOrderStr is None:
            # should probably close this here
            raise ConversionException(
                "BulkStoreRef element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "Pointing",
            )

        if len(self._attributesSeq) == 0:
            # should probably close this here
            raise ConversionException(
                "Attributes element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "Pointing",
            )

        byteOrder = ByteOrder(byteOrderStr)

        self._skipUntilEmptyLine(10)

        self._eis = EndianInput(self._tableFile, byteOrder)

        # not sure if this should be saved
        self._entity = Entity.fromBin(self._eis)

        # containerEntity is not used, but it is next
        containerEntity = Entity.fromBin(self._eis)

        # number of rows, the value from the ASDM should be used
        numRows = self._eis.readInt()

        # this is where the rows start
        self._whereRowsStart = self._eis.tell()

        # find where the rows end, get near the end
        self._eis.seek(self._fileSizeInBytes - 100)

        # the accumulateUntilBoundary looks at "lines" but itmight be
        # starting from inside the binary part where null values might be found.
        # At most, there might be 100 bytes of null, or 100 lines. So limit
        # the search to 100 lines before giving up.
        lastPart = self._accumulateUntilBoundary(self._boundary_1, 100)

        # the full size of the boundary and everything after it
        self._endBoundarySizeInBytes = 100 - len(lastPart)

        # reset back to the start of rows
        self._eis.seek(self._whereRowsStart)

        self._currentState = self._States.S_OPENED

    def reset(self):
        """
        Reposition the read head to the beginning of the table.
        The internal storage containing the result of the last read operation is cleared.
        """
        self._checkState(self._Transitions.T_RESET, "TableStreamReader.reset")
        self._clear()
        self._eis.seek(self._whereRowsStart)

    def nextNrows(self, nrows):
        """
        Reads at most nrows in the file, creates as many representation of these rows and return the
        list containing those representations.

        Parameters
        ----------
        nrows : int
            the maximum number of rows to read.

        Returns a list of PointintRow instances
        """
        self._checkState(self._Transitions.T_READ, "TableStreamReader.nextNrows")
        self._clear()
        nread = 0
        asdm = ASDM()
        ptab = asdm.getPointing()
        while self.hasRows() and nread < nrows:
            self._rows.append(PointingRow.fromBin(self._eis, ptab, self._attributesSeq))
            nread += 1

        return self._rows

    def untilNbytes(self, nbytes):
        """
        Reads as many rows as possible in the file, keeps their in memory representation
        until the number of read bytes is greater than or equal to a number of
        bytes, n, passed as a parameter to the method.

        Parameters
        ----------
        nbytes : int
            the maximum number of bytes to read


        Return the list of PointingRow instances read
        """
        self._checkState(self._Transitions.T_READ, "TableStreamReader.untilNbytes")
        self._clear()
        whereAmI = self._eis.tell()
        if not self.hasRows():
            return self._rows

        asdm = ASDM()
        ptab = asdm.getPointing()

        while ((self._eis.tell() - whereAmI) < nbytes) and self.hasRows():
            self._rows.append(PointingRow.fromBin(self._eis, ptab, self._attributesSeq))

        return self._rows

    def hasRows(self):
        """
        Returns True if the end of the file has not been reached./
        """
        self._checkState(self._Transitions.T_CHECK, "TableStreamReader.hasRows")
        return self._eis.tell() < (self._fileSizeInBytes - self._endBoundarySizeInBytes)

    def close(self):
        """
        Releases all of the resources and closes the opened file
        """
        self._checkState(self._Transitions.T_CLOSE, "TableStreamReader.close")
        self._clear()

        # there's no harm in closing both, or closing them if they're already closed
        self._eis.close()
        self._tableFile.close()

        # there's probably other things here that should be initialized if this migth be reused
        self._currentState = self._States.S_CLOSED
