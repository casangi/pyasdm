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
import codecs
from xml.dom import minidom
import numpy as np

from pyasdm.bdf.BDFHeader import BDFHeader

from pyasdm.ByteOrder import ByteOrder
from pyasdm.enumerations.CorrelationMode import CorrelationMode
from pyasdm.enumerations.CorrelatorType import CorrelatorType
from pyasdm.enumerations.SpectralResolutionType import SpectralResolutionType
from pyasdm.enumerations.ProcessorType import ProcessorType
from pyasdm.enumerations.AtmPhaseCorrection import AtmPhaseCorrection
from pyasdm.enumerations.StokesParameter import StokesParameter
from pyasdm.enumerations.AxisName import AxisName

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

    def reset(self):
        # reinitializes the internal values to their initial state, closes any open file
        if self._f is not None:
            if not self._f.closed:
                self._f.close()
            self._f = None

        self._boundary_1 = None # the string indicating the top level boundary definition
        self._currentLine = None # the line most recently read by _nextLine
        self._integrationIndex = -1 # no integration read yet
        self._path = None # the path that is opened, when opened
        self._sdmDataHeaderDOM = None # the initial (main) BDF data header as a DOM instance
        self._bdfHeaderData = BDFHeader()  # initialized from the sdmDataHeader XML via a DOM

    def __init__(self) :
        """
        Initialize internal values. The open method is used to connect to a BDF.
        """
        self._path = None # the path to the BDF
        self._f = None # the opened file object
        self.reset()

    def open(self, bdfPath):
        """
        Open a file expected to contain BDF data, read and parse the global header.
        On exit the first block of data (subscan, integration, or subintegration) is
        ready to be read by the getData method.
        """
        # TBD : implement the checkState equivalent to only allow certain operations
        # when the object is in certain states. Throws an exception otherwise.
        # self.checkState(self._T_OPEN, "open")

        self.reset()
        self._sdmDataHeaderDOM = None # the initial (main) BDF data header as a DOM instance

        self._path = bdfPath
        try:
            self._f = open(bdfPath, mode='rb')
        except Exception as exc:
            raise BDFReaderException("Error while opening '" + bdfPath + "'. The exception was " + str(exc)) from None
        # I don't think this can happen without throwing an exception
        if self._f is None:
            raise BDFReaderException("Unable to open '" + bdfpath + "'. No exception was raised.")

        self._boundary_1 = self._requireMIMEHeader()
        self._requireSDMDataHeaderMIMEPart()
        self._integrationIndex = -1    # no integration read yet

        # TBD set current state when the state processing is in place, at beginning

    def getPath(self):
        """
        Return the path of the currently opened file. Returns None of no path is opened.
        """
        return self._path

    def close(self):
        """
        Equivalent to reset, closes any opened file and sets the internal values to 
        their initial state.
        """
        self.reset()

    def hasSubset(self):
        """
        Returns True if and only if there are still data to read in the BDF file.
        """
        # TBD : work out when the packedDataReader is needed here, pyBDFExplorer uses
        # that, the c++ code just checks that the current line isn't the last line, which has already been stripped of the newline
        result = (self._currentLine is not None) and self._currentLine != b"--" + self._boundary_1 + b"--"
        return result

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
            raise BDFReaderException("could not detect a well formed MIME header field in '" + hf + "'")
        if colonIndex > 0:
            name = hf[:colonIndex]
            name = name.strip()
        if colonIndex < len(hf)-1:
            value = hf[colonIndex+1:]
            value = value.strip()
        # null values are OK
        return (name, value)

    def _requireHeaderField(self, hf):
        """
        A method which consumes a MIME header and returns the (name, value) pair it has found in that header.
        This method is only for internal use.
        """
        name,value = self._headerField2Pair(self._nextLine())
        if name.upper() != codecs.encode(hf,'utf-8'):
            raise BDFReaderException("Did not find expected field '" + hf + "' in '" + self._currentLine.decode('utf-8') + "'.")
        return name, value

    def _unquote(self, s):
        """
        A utility method which returns an unquoted version of a quoted string (leading and trailing quotes are removed)
        s is assumed to b a bytes type
        This method is only for internal use.
        """
        if len(s) < 2:
            return s
        if (s[0] == ord('"') and s[-1] == ord('"')) or (s[0] == ord["'"] and s[-1] == ord("'")):
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
            raise BDFReaderException("could not find an empty line in less than " + str(maxSkips+1) << " lines.")

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
        while numLines <= maxLines and line.find(b"--"+boundary) != 0:
            result += line
            numLines += 1
            line = self._nextLine()

        if numLines > maxLines:
            raise BDFReaderException("could not find the boundary string '" + boundary.decode('utf-8') + "' in less than " + str(maxLines+1) + " lines.")

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
            raise BDFReaderException("could not find the boundary string '" + boundary.decode('utf-8') + "' in less than " + str(maxLines+1) + " lines.")

    def _requireBoundaryInCT(self, ctValue):
        """
        A method which looks for the BOUNDARY definition in a CONTENT-TYPE MIME header and returns
        the unquoted version of that definition.
        This method is only for internal use.
        """
        cvValueItems = [item.strip() for item in ctValue.split(b";")]
        cvValueItemsNameValue = [item.partition(b"=") for item in cvValueItems]
        boundaryValues = [item[2] for item in cvValueItemsNameValue if item[0].upper() == b'BOUNDARY' and item[2] != '']
        if boundaryValues == []:
            raise BDFReaderException("count not found a boundary definition in '" + ctValue.decode('utf-8') + "'.")
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
            raise BDFReaderException("'MIME-VERSION: 1.0' missing at the very beginning of the file '" + self._path + "'.")

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
        self._requireBoundary(self._boundary_1, 0);

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
            raise BDFReaderException("Unexpected exception while parsing the main BDF header: '" + str(exc) + ".") from None
        
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
        while (self._currentLine.find(startStr)==0):
            curpos = self.position()
            self._nextLine()

        self._setPosition(curpos)

    def _requireSDMDataSubsetMIMEPart(self):
        # CAS-8151, apparently there are cases where there are two occurrences of the MIME bouneary instead of only one
        self._skipAsLongAsLineStartsWith(b"--"+self._boundary_1)
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

        # TBD : SDMDataSubset should be a class, reset it here

        actualTimesDesc            = {}
        actualTimesDesc["present"] = False
        actualTimesDesc["base"]    = -1
        actualTimesDesc["arr"]   = None
        actualTimesDesc["type"]    = "INT64_TYPE"
        actualTimesDesc["np_type"] = np.dtype(np.int64)

        actualDurationsDesc            = {}
        actualDurationsDesc["present"] = False
        actualDurationsDesc["base"]    = -1
        actualDurationsDesc["arr"]   = None
        actualDurationsDesc["type"]    = "INT64_TYPE"
        actualDurationsDesc["np_type"] = np.dtype(np.int64)

        crossDataDesc            = {}
        crossDataDesc["present"] = False
        crossDataDesc["base"]    = -1
        crossDataDesc["arr"]   = None
        crossDataDesc["type"]    = None
        crossDataDesc["np_type"] = None

        # the actual crossDataDesc varies among these types
        npInt16= np.dtype(np.int16)
        npInt32 = np.dtype(np.int32)
        npFloat32 = np.dtype(np.float32)

        autoDataDesc            = {}
        autoDataDesc["present"] = False
        autoDataDesc["base"]    = -1
        autoDataDesc["arr"]   = None
        autoDataDesc["type"]    = "FLOAT32_TYPE"
        autoDataDesc["np_type"] = np.dtype(np.float32)
        
        flagsDesc            = {}
        flagsDesc["present"] = False
        flagsDesc["base"]    = -1
        flagsDesc["arr"]   = None
        flagsDesc["type"]    = "INT32_TYPE"
        flagsDesc["np_type"] = np.dtype(np.int32)
        
        zeroLagsDesc            = {}
        zeroLagsDesc["present"] = False
        zeroLagsDesc["base"]    = -1
        zeroLagsDesc["arr"]   = None
        zeroLagsDesc["type"]    = "FLOAT32_TYPE"
        zeroLagsDesc["np_type"] = np.dtype(np.float32)

        # adjust the numpy data types when the byte order is not native
        if not self._bdfHeaderData.getByteOrder().isNative():
            np_byteOrder = "<"
            if self._bdfHeaderData.getByteOrder().getByteOrder() == "big":
                np_byteOrder = ">"
                
            actualTimesDesc["np_type"] = actualTimesDesc["np_type"].newbyteorder(np_byteOrder)
            actualDurationsDesc["np_type"] = actualDurationsDesc["np_type"].newbyteorder(np_byteOrder)
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
            result = re.match(b"(([0-9]+/)+)(actualDurations|actualTimes|autoData|crossData|zeroLags|flags)\\.bin", value.lstrip().rstrip())
            if result == None:
                raise BDFReaderException("Could not identify the part name in '" + value.decode('utf-8') + "'.")

            binaryPartName = result.group(3)
            dataPath = result.group(1)

            if binaryPartName.decode('utf-8') not in self._binaryPartSize:
                raise BDFReaderException("The size of '" + binaryPartName.decode('utf-8') + "' was not announced in the data header!")
            if self._binaryPartSize[binaryPartName.decode('utf-8')] == 0:
                raise BDFReaderException("The size of '" + binaryPartName.decode('utf-8') + "' was announced as null. I was not expecting a '" + binaryPartName.decode('utf-8') + "' attachment here.")

            if binaryPartName == b"crossData":
                # crossData must be in the minidom and it must have a type element
                elements = sdmDataSubsetHeaderDOM.getElementsByTagName("crossData")
                if len(elements) == 0:
                    raise BDFReaderException("Missing expected 'crossData' element in '%s'" % sdmDataSubsetHeaderDOM.toprettyxml())

                crossDataType = elements[0].getAttribute("type")
                if len(crossDataType) == 0:
                    raise BDFReaderException("Missing expected 'type' attribute in element '%s'." % elements[0].nodeName)

                crossDataDesc['type'] = crossDataType

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
                    crossDataDesc['np_type'] = npInt16
                elif crossDataType == "INT32_TYPE":
                    numberOfBytesPerValue = 4
                    crossDataDesc['np_type'] = npInt32
                elif crossDataType == "FLOAT32_TYPE":
                    numberOfBytesPerValue = 4
                    crossDataDesc['np_type'] = npFloat32
            elif binaryPartName == b"flags":
                numberOfBytesPerValue = 4
            elif binaryPartName == b"zeroLags":
                numberOfBytesPerValue = 4

            # I don't believe this can ever happen, TBD - raise a better exception here
            if numberOfBytesPerValue is None:
                raise BDFReaderException("unrecognized binary part name or data type for that part : '" + binaryPartName.decode('utf-8') + "'.")

            numberOfElementsToRead = self._binaryPartSize[binaryPartName.decode('utf-8')]
            numberOfBytesToRead = numberOfBytesPerValue * numberOfElementsToRead

            # with restructuring, this can also be cleaner - TBD
            # actual number of bytes read
            nReadBytes = None
            if binaryPartName == b"zeroLags":
                zeroLagsDesc["present"] = True
                zeroLagsDesc["base"] = self.position()
                dt = zeroLagsDesc["np_type"]
                zeroLagsDesc["arr"] = np.fromfile(self._f, dtype=dt, count=numberOfElementsToRead)
                nReadBytes = zeroLagsDesc["arr"].size * numberOfBytesPerValue
            elif binaryPartName == b"actualTimes":
                actualTimesDesc["present"] = True
                actualTimesDesc["base"] = self.position()
                dt = actualTimesDesc["np_type"]
                actualTimesDesc["arr"] = np.fromfile(self._f, dtype=dt, count=numberOfElementsToRead)
                nReadBytes = len(actualTimesDesc["arr"]) * numberOfBytesPerValue
            elif binaryPartName == b"actualDurations":
                actualDurationsDesc["present"] = True
                actualDurationsDesc["base"] = self.position()
                dt = actualDurationsDesc["np_type"]
                actualDurationsDesc["arr"] = np.fromfile(self._f, dtype=dt, count=numberOfElementsToRead)
                nReadBytes = len(actuaDurationsDesc["arr"]) * numberOfBytesPerValue
            elif binaryPartName == b"crossData":
                crossDataDesc["present"] = True
                crossDataDesc["base"] = self.position()
                dt = crossDataDesc["np_type"]
                crossDataDesc["arr"] = np.fromfile(self._f, dtype=dt, count=numberOfElementsToRead)
                nReadBytes = len(crossDataDesc["arr"]) * numberOfBytesPerValue
            elif binaryPartName == b"autoData":
                autoDataDesc["present"] = True
                autoDataDesc["base"] = self.position()
                dt = autoDataDesc["np_type"]
                autoDataDesc["arr"] = np.fromfile(self._f, dtype=dt, count=numberOfElementsToRead)
                nReadBytes = len(autoDataDesc["arr"]) * numberOfBytesPerValue
            elif binaryPartName == b"flags":
                flagsDesc["present"] = True
                flagsDesc["base"] = self.position()
                dt = flagsDesc["np_type"]
                flagsDesc["arr"] = np.fromfile(self._f, dtype=dt, count=numberOfElementsToRead)
                nReadBytes = len(flagsDesc["arr"]) * numberOfBytesPerValue
            else:
                # should never reach here ! but just in case
                bytes = self._f.read(numberOfBytesToRead)
                nReadBytes = len(bytes)
                print("Unknown binary part name '(%s)' with %s bytes to read, skipping in case it's possible to continue, this should never happen!" % (binaryPartName.decode('utf-8'), numberOfBytesToRead))

            if nReadBytes < numberOfBytesToRead:
                raise BDFReaderException("End of file reached while reading binary attachment '" + binaryPartName.decode('utf') + "'.")

            line = self._nextLine() # absorb the nl right after the last byte of the binary attachment
            line = self._nextLine() # this should be boundary_2

            if line.find(b"--"+self._boundary_2.strip(b'"')) != 0:
                raise BDFReaderException("Processing integration # " + self._integration + ":Unexpected '" + line.decode('utf-8') + "' after the binary part '" + binaryPartName.decode('utf-8') + "'.")

            # is this the end?
            done = line == b"--" + self._boundary_2.strip(b'"') + b"--"

        integrationMidpoint = int((sdmDataSubsetHeaderDOM.getElementsByTagName("time"))[0].childNodes[0].nodeValue)
        integrationInterval = int((sdmDataSubsetHeaderDOM.getElementsByTagName("interval"))[0].childNodes[0].nodeValue)

        # TBD - this struct could be assembed earlier and used more efficiently in the middle
        # TBD - pyBDFExplorer returns sdmDataSubsetHeaderDOM here, is that useful?
        return {'midpointInNanoSeconds' : integrationMidpoint,
                'intervalInNanoSeconds' : integrationInterval,
                'actualTimes' : actualTimesDesc,
                'actualDurations' : actualDurationsDesc,
                'crossData' : crossDataDesc,
                'autoData' : autoDataDesc,
                'flags' : flagsDesc,
                'zeroLags' : zeroLagsDesc}

    def position(self):
        """
        Returns the current position in bytes of the BDF file.
        """
        if self._f is None:
            return None
        return self._f.tell()

    def _setPosition(self, newpos):
        """
        Set the position of the BDF to the location given by newpos (bytes).
        This is intended for inernal use because it may confuse the public methods if this is
        used out of the normal sequence.
        """
        self._f.seek(newpos,0)

    def getSubset(self):
        """
        Returns an SDM Data Subset (one integration) as a dictionary.
        """
        self._integrationIndex += 1
        sdmSubset = self._requireSDMDataSubsetMIMEPart()
        # this line isn't used, bnut it should be advanced to the next line
        line = self._nextLine()
        return sdmSubset

    def printAllBinary(self):
        for binName in self._bdfHeaderData.getBinaryTypes():
            if self._bdfHeaderData.hasBinary(binName):
                ok = True
                if binName == "zeroLags":
                    ok = (self._bdfHeaderData.getProcessorType().getName() == "CORRELATOR") and (self._bdfHeaderData.zeroLagsCorrelatorType().getName() != "FX")
                if ok:
                    print("%s:" % binName)
                    print("\tsize = %s" % self._bdfHeaderData.getSize(binName))
                    axesListStr = ""
                    for axis in self._bdfHeaderData.getAxes(binName):
                        if len(axesListStr)>0:
                            axesListStr += " "
                        axesListStr += axis.getName()
                    print("\taxes = %s" % axesListStr)
                    if binName == "zeroLags":
                        print("\tcorrelatorType = %s" % self._bdfHeaderData.zeroLagsCorrelatorType().getName())
                    elif binName == "autoData":
                        print("\tnormalized = %s" % self._bdfHeaderData.isAutoDataNormalized())

    def printBDFHeader(self):
        print("XML Schema version = %s" % self._bdfHeaderData.getSchemaVersion())
        print("Byte order = %s" % self._bdfHeaderData.getByteOrder().toString())
        print("startTime = %s" % self._bdfHeaderData.getStartTime())
        print("projectPath = %s" % self._bdfHeaderData.projectPath())
        print("dataOID = %s" % self._bdfHeaderData.getDataOID())
        print("title = %s" % self._bdfHeaderData.getTitle())
        if (self._bdfHeaderData.getDimensionality() > 0):
            print("dimensionality = %s" % self._bdfHeaderData.getDimensionality())
        else:
            print("numTime = %s" % self._bdfHeaderData,getNumTime())
        print("execBlockUID = %s" % self._bdfHeaderData.getExecBlockUID())
        print("execBlockNum = %s" % self._bdfHeaderData.getExecBlockNum())
        print("scanNum = %s" % self._bdfHeaderData.getScanNum())
        print("subscanNum = %s" % self._bdfHeaderData.getSubscanNum())
        print("numAntenna = %s" % self._bdfHeaderData.getNumAntenna())
        print("correlationMode = %s" % self._bdfHeaderData.getCorrelationMode().getName())
        spectralResolutionType = self._bdfHeaderData.getSpectralResolutionType()
        if spectralResolutionType is not None:
            print("spectralResolutionType = %s" % spectralResolutionType.getName())
        else:
            print("spectralResolutionType not found in sdmDataHeader")
        print("processorType = %s" % self._bdfHeaderData.getProcessorType().getName())
        apcList = self._bdfHeaderData.getAPClist()
        if len(apcList) > 0:
            apcString = ""
            for apc in apcList:
                if len(apcString) > 0:
                    apcString += " "
                apcString += apc.getName()
            print("atmospheric phase correction = %s" % apcString)
        basebandsList = self._bdfHeaderData.getBasebandsList()
        if len(basebandsList) > 0:
            basebandCount = 0
            for baseband in basebandsList:
                print("baseband #%s:" % basebandCount)
                print("\tname = %s" % baseband["name"])
                spwCount = 0
                for spectralWindow in baseband["spectralWindows"]:
                    print("\tspectralWindow #%s:" % spwCount)
                    print("\t\tsw = %s" % spectralWindow["sw"])
                    crossPolStr = ""
                    for crossPolProduct in spectralWindow["crossPolProducts"]:
                        if len(crossPolStr) > 0:
                            crossPolStr += " "
                        crossPolStr += crossPolProduct.getName()
                    if len(crossPolStr) > 0:
                        print("\t\tcrossPolProducts = %s" % crossPolStr)
                    sdPolStr = ""
                    for sdPolProduct in spectralWindow["sdPolProducts"]:
                        if len(sdPolStr) > 0:
                            sdPolStr += " "
                        sdPolStr += sdPolProduct.getName()
                    if len(sdPolStr) > 0:
                        print("\t\tsdPolProducts = %s" % sdPolStr)
                    if spectralWindow['scaleFactor'] is not None:
                        print("\t\tscaleFactor = %.5f" % spectralWindow['scaleFactor'])
                    print("\t\tnumSpectralPoint = %s" % spectralWindow['numSpectralPoint'])
                    print("\t\tnumBin = %s" % spectralWindow['numBin'])
                    print("\t\tsideband = %s" % spectralWindow['sideband'].getName())
                    spwCount += 1
                basebandCount += 1
        self.printAllBinary()
        print("")

    def printSubset(self, subset):
        # not for release
        # prins a subset, prining up to the first 10 elements of each type
        # does not use self
        print("Midpoint : %s" % subset['midpointInNanoSeconds'])
        print("Interval : %s" % subset['intervalInNanoSeconds'])
        for item in subset:
            if isinstance(subset[item],dict):
                if subset[item]['present']:
                    nOut = min(10, subset[item]['arr'].size)
                    outStr = "%s : %s" % (item,subset[item]['arr'][0:nOut])
                    if (nOut == 10):
                        outStr = outStr + " ... "
                    outStr = outStr + " size = " + str(subset[item]['arr'].size)
                    print(item + " : " + outStr)
        
