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
# File BDFHeader.py
#

import pyasdm.ByteOrder

import pyasdm.enumerations.AtmPhaseCorrection
import pyasdm.enumerations.AxisName
import pyasdm.enumerations.CorrelationMode
import pyasdm.enumerations.CorrelatorType
import pyasdm.enumerations.NetSideband
import pyasdm.enumerations.ProcessorType
import pyasdm.enumerations.SpectralResolutionType
import pyasdm.enumerations.StokesParameter

import pyasdm.exceptions.BDFReaderException

import numpy as np


class BDFHeader:
    """
    A class to hold the values from the primary header of a BDF.

    This code is based on several c++ classes as well used to
    read BDFs.
    """

    # the value names are preceded by underscores ("_") to
    # indicate that they should be treated as private, leaving
    # the getting and setting to member functions that can
    # check on the appropriateness of the value as necessary.

    def __init__(self):
        """
        Initialize the class attributes to their defaults.
        """
        self._schemaVersion = 0  # int in c++
        self._byteOrder = pyasdm.ByteOrder()  # native byte order
        # projectPath is kept in its parts : execBlockNum, scanNum, subscanNum
        self._execBlockNum = 0  # an unsigned integer in c++
        self._scanNum = 0  # an unsigned integer in c++
        self._subscanNum = 0  # an unsigned integer in c++
        self._startTime = 0  # an unsigned long long in c++

        # dimensionality and numTime are set when preent, only 1 of them should be non-zero
        self._dimensionality = 0
        self._numTime = 0

        self._dataOID = None
        self._execBlockUID = None
        self._title = None
        self._numAntenna = 0  # an unsigned integer in c++
        self._correlationMode = None  # a CorrelationMode enumeration when set
        self._spectralResolutionType = (
            None  # a SpectralResolutionType enumeration when set
        )
        self._processorType = None  # a ProcessorType enumeration when set

        self._dataStruct = {
            "apc": [],  # list of AtmPhaseCorrection instances
            "basebands": [],  # list of basebands instances, name and a spectral window struct
            "flags": {
                "size": 0,
                "axes": [],
            },  # unsigned int, list AxisName enumerations
            "actualTimes": {"size": 0, "axes": []},
            "actualDurations": {"size": 0, "axes": []},
            "zeroLags": {
                "size": 0,
                "axes": [],
                "correlatorType": None,
            },  # CorrelatorType enumeration
            "crossData": {"size": 0, "axes": []},
            "autoData": {"size": 0, "axes": [], "normalized": False},
        }

        # the binary type names in _dataStruct, each of these is a structure with a "size" and "axes" value
        self._binTypes = [
            "flags",
            "actualTimes",
            "actualDurations",
            "zeroLags",
            "crossData",
            "autoData",
        ]

    def getBinaryTypes(self):
        """
        Return a list of the known types of binary data.
        """
        return self._binTypes

    def projectPath(self):
        """
        Return the project path using execBlockNum, scanNum, and subscanNum.
        """
        return "%s/%s/%s/" % (self._execBlockNum, self._scanNum, self._subscanNum)

    def getSize(self, binaryType):
        """
        Get the size of the named binary type.
        """
        if binaryType not in self._binTypes:
            raise ValueError("unrecognized binaryType value")
        return self._dataStruct[binaryType]["size"]

    def getAxes(self, binaryType):
        """
        Get the AxisNames enumeration list for the given binary type.
        """
        if binaryType not in self._binTypes:
            raise ValueError("unrecognized binaryType value")
        return self._dataStruct[binaryType]["axes"]

    def getAxesNames(self, binaryType):
        """
        Return a list of axes names (strings) for the given binary type.
        """
        axesList = self.getAxes(binaryType)
        result = []
        for axis in axesList:
            result.append(axis.getName())
        return result

    def hasBinary(self, binaryType):
        """
        Does the given binaryType have a size > 0?
        """
        return self.getSize(binaryType) > 0

    def isAutoDataNormalized(self):
        """
        Returns True if this has autoData and the normalized value is True
        """
        result = False
        if self.hasBinary("autoData"):
            result = self._dataStruct["autoData"]["normalized"]
        return result

    def zeroLagsCorrelatorType(self):
        """
        Returns the correlatorType for the zeroLags. Returns None if
        not set (zeroLags is not present or this was not set).
        """
        return self._dataStruct["zeroLags"]["correlatorType"]

    def correlatorType(self):
        """
        Return the CorrelatorType if the processorType is CORRELATOR, else None.

        Note that what is actually returned is the correlatorType from the zeroLags section.

        Returns a CorrelatorType enumeration or None if not CORRELATOR data or not set.
        """
        if self.getProcessorType() == pyasdm.enumerations.ProcessorType.CORRELATOR:
            return self.zeroLagsCorrelatorType()
        return None

    def hasPackedData(self):
        """
        Returns True if and only if all of the integrations are grouped in one subset.

        This returns true if dimensionality returns 0.
        """
        return self.getDimensionality() == 0

    def isTP(self):
        """
        Returns True if and only if the string "Total Power" appears in the title.

        Note: as per the comments in SDMDataObject.cc this relies an un-said
        convension used to form the title. Apparently it's difficult to be sure
        what data is Total Power only data.
        """
        return self.getTitle().find("Total Power") >= 0

    def isWVR(self):
        """
        Returns True if and only if the string "WVR" appears in the title.

        Note: as per the comments in SDMDataObject.cc this relies an un-said
        convension used to form the title. Apparently it's difficult to be sure
        what data is WVR data.
        """
        return self.getTitle().find("WVR") >= 0

    def isCorrelation(self):
        """
        Return True if and only if the ProcessorTpe is CORELLATOR
        """
        return self.getProcessorType() == pyasdm.enumerations.ProcessorType.CORRELATOR

    def __str__(self):
        """
        Return a string representation of this global BDF header.

        This can be printed but is not the XML form of the header.
        """
        result = ""
        result += "XML Schema version = %s" % self.getSchemaVersion() + "\n"
        result += "Byte order = %s" % self.getByteOrder() + "\n"
        result += "startTime = %s" % self.getStartTime() + "\n"
        result += "dataOID = %s" % self.getDataOID() + "\n"
        result += "title = %s" % self.getTitle() + "\n"
        if self.getDimensionality() > 0:
            result += "dimensionality = %s" % self.getDimensionality() + "\n"
        else:
            result += "numTime = %s" % self.getNumTime() + "\n"
        result += "execBlockUID = %s" % self.getExecBlockUID() + "\n"
        result += "execBlockNum = %s" % self.getExecBlockNum() + "\n"
        result += "scanNum = %s" % self.getScanNum() + "\n"
        result += "subscanNum = %s" % self.getSubscanNum() + "\n"
        result += "numAntenna = %s" % self.getNumAntenna() + "\n"
        result += "correlationMode = %s" % self.getCorrelationMode() + "\n"
        spectralResolutionType = self.getSpectralResolutionType()
        if spectralResolutionType is not None:
            result += "spectralResolutionType = %s" % spectralResolutionType + "\n"
        result += "processorType = %s" % self.getProcessorType() + "\n"
        if self.getCorrelationMode() != pyasdm.enumerations.CorrelationMode.AUTO_ONLY:
            apcString = " ".join(map(str, self.getAPClist()))
            if len(apcString) > 0:
                result += "atmospheric phase correction = %s" % apcString + "\n"
            else:
                result += "NOTE: no atmospheric phase correction found but one was expected.\n"

        basebandsList = self.getBasebandsList()
        if len(basebandsList) > 0:
            basebandCount = 0
            for baseband in basebandsList:
                result += "baseband #%s:" % basebandCount + "\n"
                result += "\tname = %s" % baseband["name"] + "\n"
                spwCount = 0
                for spectralWindow in baseband["spectralWindows"]:
                    result += "\tspectralWindow #%s:" % spwCount + "\n"
                    result += "\t\tsw = %s" % spectralWindow["sw"] + "\n"

                    if (
                        self.getCorrelationMode()
                        == pyasdm.enumerations.CorrelationMode.CROSS_ONLY
                    ):
                        crossPolStr = " ".join(
                            map(str, spectralWindow["crossPolProducts"])
                        )
                        result += "\t\tcrossPolProducts = %s" % crossPolStr + "\n"
                        if spectralWindow["scaleFactor"] is not None:
                            result += (
                                "\t\tscaleFactor = %.5f" % spectralWindow["scaleFactor"]
                                + "\n"
                            )
                        else:
                            result += "\t\tNOTE: expected scaleFactor is missing.\n"
                        result += (
                            "\t\tnumSpectralPoint = %s"
                            % spectralWindow["numSpectralPoint"]
                            + "\n"
                        )
                        result += "\t\tnumBin = %s" % spectralWindow["numBin"] + "\n"
                    elif (
                        self.getCorrelationMode()
                        == pyasdm.enumerations.CorrelationMode.AUTO_ONLY
                    ):
                        sdPolStr = " ".join(map(str, spectralWindow["sdPolProducts"]))
                        result += "\t\tsdPolProducts = %s" % sdPolStr + "\n"
                        result += (
                            "\t\tnumSpectralPoint = %s"
                            % spectralWindow["numSpectralPoint"]
                            + "\n"
                        )
                        result += "\t\tnumBin = %s" % spectralWindow["numBin"] + "\n"
                    elif (
                        self.getCorrelationMode()
                        == pyasdm.enumerations.CorrelationMode.CROSS_AND_AUTO
                    ):
                        crossPolStr = " ".join(
                            map(str, spectralWindow["crossPolProducts"])
                        )
                        result += "\t\tcrossPolProducts = %s" % crossPolStr + "\n"
                        sdPolStr = " ".join(map(str, spectralWindow["sdPolProducts"]))
                        result += "\t\tsdPolProducts = %s" % sdPolStr + "\n"
                        if spectralWindow["scaleFactor"] is not None:
                            result += (
                                "\t\tscaleFactor = %.5f" % spectralWindow["scaleFactor"]
                                + "\n"
                            )
                        else:
                            result += "\t\tNOTE: expected scaleFactor is missing"
                        result += (
                            "\t\tnumSpectralPoint = %s"
                            % spectralWindow["numSpectralPoint"]
                            + "\n"
                        )
                        result += "\t\tnumBin = %s" % spectralWindow["numBin"] + "\n"

                    # else add nothing related to correlationMode

                    result += (
                        "\t\tsideband = %s" % spectralWindow["sideband"].getName()
                        + "\n"
                    )

                    spwCount += 1
                basebandCount += 1

        result += "flags:" + "\n"
        result += "\tsize = %s" % self.getSize("flags") + "\n"
        axesListStr = " ".join(map(str, self.getAxes("flags")))
        result += "\taxes = %s" % axesListStr + "\n"

        result += "actualTimes:" + "\n"
        result += "\tsize = %s" % self.getSize("actualTimes") + "\n"
        axesListStr = " ".join(map(str, self.getAxes("actualTimes")))
        result += "\taxes = %s" % axesListStr + "\n"

        result += "actualDurations:" + "\n"
        result += "\tsize = %s" % self.getSize("actualDurations") + "\n"
        axesListStr = " ".join(map(str, self.getAxes("actualDurations")))
        result += "\taxes = %s" % axesListStr + "\n"

        if (
            (self.getProcessorType() == pyasdm.enumerations.ProcessorType.CORRELATOR)
            and (self.zeroLagsCorrelatorType() != pyasdm.enumerations.CorrelatorType.FX)
            and (self.getSize("zeroLags") > 0)
        ):
            result += "zeroLags:" + "\n"
            result += "\tsize = %s" % self.getSize("zeroLags") + "\n"
            axesListStr = " ".join(map(str, self.getAxes("zeroLags")))
            result += "\taxes = %s" % axesListStr + "\n"
            result += "\tcorrelatorType = %s" % self.zeroLagsCorrelatorType() + "\n"

        if self.getCorrelationMode() == pyasdm.enumerations.CorrelationMode.CROSS_ONLY:
            result += "crossData:" + "\n"
            result += "\tsize = %s" % self.getSize("crossData") + "\n"
            axesListStr = " ".join(map(str, self.getAxes("crossData")))
            result += "\taxes = %s" % axesListStr + "\n"

        elif self.getCorrelationMode() == pyasdm.enumerations.CorrelationMode.AUTO_ONLY:
            result += "autoData:" + "\n"
            result += "\tsize = %s" % self.getSize("autoData") + "\n"
            axesListStr = " ".join(map(str, self.getAxes("autoData")))
            result += "\taxes = %s" % axesListStr + "\n"
            result += "\tnormalized = %s" % self.isAutoDataNormalized() + "\n"

        elif (
            self.getCorrelationMode()
            == pyasdm.enumerations.CorrelationMode.CROSS_AND_AUTO
        ):
            result += "crossData:" + "\n"
            result += "\tsize = %s" % self.getSize("crossData") + "\n"
            axesListStr = " ".join(map(str, self.getAxes("crossData")))
            result += "\taxes = %s" % axesListStr + "\n"

            result += "autoData:" + "\n"
            result += "\tsize = %s" % self.getSize("autoData") + "\n"
            axesListStr = " ".join(map(str, self.getAxes("autoData")))
            result += "\taxes = %s" % axesListStr + "\n"
            result += "\tnormalized = %s" % self.isAutoDataNormalized() + "\n"

        return result

    # getters and setters
    def setSchemaVersion(self, schemaVersion):
        """
        sets schemaVersion, it always uses int(schemaVersion) so that the value returned by
        the getter should be an int
        schemaVersion here can be a string, for example
        """
        self._schemaVersion = int(schemaVersion)

    def getSchemaVersion(self):
        """
        gets schemaVersion
        """
        return self._schemaVersion

    def setByteOrder(self, byteOrder):
        """
        Sets the byte order using byteOrder, which must be a string value that the
        ByteOrder class recognizes
        """
        self._byteOrder.fromString(byteOrder)

    def getByteOrder(self):
        """
        gets byteOrder, a ByteOrder instance
        """
        return self._byteOrder

    def setExecBlockNum(self, execBlockNum):
        """
        set the exec block num, always uses int(execBlockNum), can not be negative
        """
        newExecBlockNum = int(execBlockNum)
        if newExecBlockNum < 0:
            raise ValueError("execBlockNum can not be negative")

        self._execBlockNum = newExecBlockNum

    def getExecBlockNum(self):
        """
        gets the exectBlockNum
        """
        return self._execBlockNum

    def setScanNum(self, scanNum):
        """
        set the scan num, always uses int(scanNum), can not be negative
        """
        newScanNum = int(scanNum)
        if newScanNum < 0:
            raise ValueError("scanNum can not be negative")

        self._scanNum = newScanNum

    def getScanNum(self):
        """
        gets the scanNum
        """
        return self._scanNum

    def setSubscanNum(self, subscanNum):
        """
        set the scan num, always uses int(scanNum), can not be negative
        """
        newSubscanNum = int(subscanNum)
        if newSubscanNum < 0:
            raise ValueError("subscanNum can not be negative")

        self._subscanNum = newSubscanNum

    def getSubscanNum(self):
        """
        gets the subscanNum
        """
        return self._subscanNum

    def setDimensionality(self, dimensionality):
        """
        set the dimensionality, always uses int(dimensionality)
        dimensionality must be >= 0, if > 0 then numTime must be zero when this is set
        """
        newDimensionality = int(dimensionality)
        if newDimensionality < 0:
            raise ValueError("dimensionality must be >= 0")
        if newDimensionality > 0 and self._numTime > 0:
            raise ValueError(
                "dimensionality can not be set to a non-zero value when numTime is positive"
            )

        self._dimensionality = newDimensionality

    def getDimensionality(self):
        """
        gets the dimensionality
        """
        return self._dimensionality

    def setNumTime(self, numTime):
        """
        set the numTime, always uses int(numTime)
        numTime must be >= 0, if > 0 then dimensionality must be zero when this is set
        """
        newNumTime = int(numTime)
        if newNumTime < 0:
            raise ValueError("numTime must be >= 0")
        if newNumTime > 0 and self._dimensionality > 0:
            raise ValueError(
                "numTime can not be set to a non-zero value when dimensionality is positive"
            )

        self._numTime = newNumTime

    def getNumTime(self):
        """
        gets the numTime
        """
        return self._numTime

    def setStartTime(self, startTime):
        """
        set the startTime, always uses int(startTime), can not be negative
        """
        newStartTime = int(startTime)
        if newStartTime < 0:
            raise ValueError("startTime can not be negative")

        self._startTime = newStartTime

    def getStartTime(self):
        """
        gets the startTime
        """
        return self._startTime

    def setDataOID(self, dataOID):
        """
        sets the dataOID, this can be any string
        """
        # just to make sure it's a string
        self._dataOID = str(dataOID)

    def getDataOID(self):
        """
        get the dataOID
        """
        return self._dataOID

    def setTitle(self, title):
        """
        sets the title, this can be any string
        """
        # just to make sure it's a string
        self._title = str(title)

    def getTitle(self):
        """
        get the title
        """
        return self._title

    def setExecBlockUID(self, execBlockUID):
        """
        sets the execBlockUID, this can be any string
        """
        # just to make sure it's a string
        self._execBlockUID = str(execBlockUID)

    def getExecBlockUID(self):
        """
        get the execBlockUID
        """
        return self._execBlockUID

    def setNumAntenna(self, numAntenna):
        """
        set the numAntenna, always uses int(numAntenna), can not be negative
        """
        numAntenna = int(numAntenna)
        if numAntenna < 0:
            raise ValueError("numAntenna can not be negative")

        self._numAntenna = numAntenna

    def getNumAntenna(self):
        """
        gets the numAntenna
        """
        return self._numAntenna

    def setCorrelationMode(self, correlationMode):
        """
        sets the correlationMode, correlationMode is any value that can be used for the CorrelationMode enumeration
        """
        self._correlationMode = pyasdm.enumerations.CorrelationMode.literal(
            correlationMode
        )

    def getCorrelationMode(self):
        """
        gets the correlationMode
        """
        return self._correlationMode

    def setSpectralResolutionType(self, spectralResolutionType):
        """
        sets the spectralResolutionType, spectralResolutionType is any value that can be used for the SpectralResolutionType enumeration
        """
        self._spectralResolutionType = (
            pyasdm.enumerations.SpectralResolutionType.literal(spectralResolutionType)
        )

    def getSpectralResolutionType(self):
        """
        gets the spectralResolutionType
        """
        return self._spectralResolutionType

    def setProcessorType(self, processorType):
        """
        sets the processorType, processorType is any value that can be used for the ProcessorType enumeration
        """
        self._processorType = pyasdm.enumerations.ProcessorType.literal(processorType)

    def getProcessorType(self):
        """
        gets the processorType
        """
        return self._processorType

    def setAPClist(self, apcList):
        """
        Sets the apc list in the data struct.
        apcList must be a list of AtmPhaseCorrection instances
        """
        if not isinstance(apcList, list):
            raise ValueError("apcList must be a list")

        for item in apcList:
            if not isinstance(item, pyasdm.enumerations.AtmPhaseCorrection):
                raise ValueError(
                    "apcList must be a list of AtmPhaseCorrection instances"
                )

        self._dataStruct["apc"] = apcList

    def getAPClist(self):
        """
        Returns the apc list from the data struct.
        """
        return self._dataStruct["apc"]

    def getBasebandsList(self):
        """
        Returns the basebands list, a list of structs, from the data struct
        """
        return self._dataStruct["basebands"]

    def _setBinaryStruct(self, binaryNode):
        """
        Internal method that sets the values of the data struct appropriate to the name
        of binary, which must be one of flags, actualTimes, actualDurations, crossData,
        autoData, or zeroLags.
        """
        self._dataStruct[binaryNode.nodeName]["size"] = int(
            self._getRequiredAttributeValue(binaryNode, "size")
        )
        axesStrList = self._getRequiredAttributeValue(binaryNode, "axes").split()
        axesList = []
        for axisStr in axesStrList:
            axesList.append(pyasdm.enumerations.AxisName.literal(axisStr))
        self._dataStruct[binaryNode.nodeName]["axes"] = axesList
        if binaryNode.nodeName == "autoData":
            normalizedAttrValue = self._getRequiredAttributeValue(binaryNode, "normalized")
            # this should be either 'true' or 'false', store as a boolean value
            if normalizedAttrValue == "true":
                self._dataStruct[binaryNode.nodeName]["normalized"] = True
            elif normalizedAttrValue == "false":
                self._dataStruct[binaryNode.nodeName]["normalized"] = False
            else:
                raise ValueError("unrecognized 'normalized' value for autoData, must be either 'true' or 'false', value is '" + normalizedAttrValue + "'")
                
        elif binaryNode.nodeName == "zeroLags":
            correlatorTypeValue = self._getRequiredAttributeValue(
                binaryNode, "correlatorType"
            )
            self._dataStruct[binaryNode.nodeName]["correlatorType"] = (
                pyasdm.enumerations.CorrelatorType.literal(correlatorTypeValue)
            )

    def _getAttributeValue(self, nodeElement, attrName):
        """
        Get an attribute by name from an element without regard to the namespace.

        BDF files are not consistent in their use of namespaces for attribute names.
        Some of the time the attribute is not in a namespace and there are examples of
        some attributes being found in different namespaces in different BDFs. A few
        examples have been seen where the same attribute is in a namespace and repeated
        outside of a namespace.

        Possibly this is just an historical anomaly and possibly it represents different
        implementations across different telescopes.

        The DOM (minidom) attribute access for elements is clumsy with namespaces.
        The python implementation requires the namespace to be given exactly.
        Where the c++ code that does the same parsing of the same XML will find a named
        attribute without regard of the namespace it may be found in. Some testing of
        the c++ code shows that if a named attribute appears outside of any namespace and
        also qualified with a namespace in the same XML that the value outside of the
        namespace is preferred.

        This routine returns the value using the attribute name as is (no namespace) if
        that exists. Otherwise it finds the value of first attribute with a matching name of the
        form <namespace>:attrName.

        This returnes None if the attribute is not found.

        @param nodeElement the XML node element from which the value of named attribute is to be found.
        @param attrName a string giving the name of the attribute (no namespace prefix)
        @returns the value of attrName in nodeElement if found, else None. The value of an attribute is always returned a string.
        """

        # this finds the value if no namespace is involved
        if nodeElement.hasAttribute(attrName):
            return nodeElement.getAttribute(attrName)

        # look through the attributes individually, finding the first one in a namespace that matches.
        for itemName, itemValue in nodeElement.attributes.items():
            # only care about itemName if it has a colon (namespace)
            indx = itemName.find(":")
            if (
                (indx >= 0)
                and ((indx + 1) < len(itemName))
                and (itemName[(indx + 1) :] == attrName)
            ):
                # found it
                return itemValue

        return None

    def _getRequiredAttributeValue(self, nodeElement, attrName):
        """
        Use _getAttributeValue and raise an exception if the attribute name is not found.

        @param nodeElement the XML node element from which the value of named attribute is to be found.
        @param attrName a string giving the name of the attribute (no namespace prefix)
        @returns the value of attrName in nodeElement if found, else raise BDFReaderException. The value of an attribute is always returned a string.
        """
        attrValue = self._getAttributeValue(nodeElement, attrName)
        if attrValue is None:
            raise pyasdm.exceptions.BDFReaderException(
                "Required attribute " + attrName + " not found in BDF header"
            )
        return attrValue

    def fromDOM(self, dataHeaderElem):
        """
        set this from a minidom that is an sdmDataHeader element
        """

        self.setSchemaVersion(
            self._getRequiredAttributeValue(dataHeaderElem, "schemaVersion")
        )
        self.setByteOrder(self._getRequiredAttributeValue(dataHeaderElem, "byteOrder"))
        projectPath = self._getRequiredAttributeValue(dataHeaderElem, "projectPath")
        projectPathParts = projectPath.split("/")
        # in general a projectPath can have 3 to 5 parts : execBlock / scanNum / subscanNum / integrationNum / subintegrationNum
        # here, it should only have the first 3 parts, there is a trailing / so 4 parts with an empty 4th part is OK
        if len(projectPathParts) > 4 or (
            len(projectPathParts) == 4 and len(projectPathParts[3]) != 0
        ):
            raise pyasdm.exceptions.BDFReaderException(
                "Invalid string for projectPath '" + projectPath + "'"
            )

        self.setExecBlockNum(projectPathParts[0])
        self.setScanNum(projectPathParts[1])
        self.setSubscanNum(projectPathParts[2])

        childNode = dataHeaderElem.firstChild

        self.setDimensionality(0)
        self.setNumTime(0)

        while childNode is not None:
            if childNode.nodeName == "startTime":
                self.setStartTime(childNode.firstChild.data)
            if childNode.nodeName == "dataOID":
                # get the href value from here
                self.setDataOID(self._getRequiredAttributeValue(childNode, "href"))
                # and the title
                self.setTitle(self._getRequiredAttributeValue(childNode, "title"))
            if childNode.nodeName == "dimensionality":
                self.setDimensionality(childNode.firstChild.data)
            if childNode.nodeName == "numTime":
                self.setNumTime(childNode.firstChild.data)
            if childNode.nodeName == "execBlock":
                # the href value is the execBlockUID
                self.setExecBlockUID(self._getRequiredAttributeValue(childNode, "href"))
            if childNode.nodeName == "numAntenna":
                self.setNumAntenna(childNode.firstChild.data)
            if childNode.nodeName == "correlationMode":
                self.setCorrelationMode(childNode.firstChild.data)
            if childNode.nodeName == "spectralResolution":
                self.setSpectralResolutionType(childNode.firstChild.data)
            if childNode.nodeName == "processorType":
                self.setProcessorType(childNode.firstChild.data)
            if childNode.nodeName == "dataStruct":
                # this node is used to fill out the elements of the dataStruct
                # AtmPhaseCorrection list is empty unless this data includes CROSS data
                apcEnumList = []
                if (self.getCorrelationMode().getName() == "CROSS_ONLY") or (
                    self.getCorrelationMode().getName() == "CROSS_AND_AUTO"
                ):
                    # apc is an atttribute that is expected here
                    # it is a space-separated list of AtmPhaseCorrection enumeration names
                    apcList = self._getRequiredAttributeValue(childNode, "apc").split()
                    for apcName in apcList:
                        apcEnumList.append(
                            pyasdm.enumerations.AtmPhaseCorrection.literal(apcName)
                        )
                self.setAPClist(apcEnumList)

                # the child nodes
                # list of baseband structs to be assembled here
                basebands = []
                dsChildNode = childNode.firstChild
                while dsChildNode is not None:
                    if dsChildNode.nodeName == "baseband":
                        thisBaseband = {}
                        thisBaseband["name"] = self._getRequiredAttributeValue(
                            dsChildNode, "name"
                        )
                        # ths children describe the associated spectral windows
                        bbChildNode = dsChildNode.firstChild
                        spectralWindows = []
                        while bbChildNode is not None:
                            if bbChildNode.nodeName == "spectralWindow":
                                thisSpectralWindow = {
                                    "crossPolProducts": [],
                                    "sdPolProducts": [],
                                    "scaleFactor": None,
                                    "numSpectralPoint": None,
                                    "numBin": None,
                                    "sideband": None,
                                    "sw": None,
                                }
                                # the "swbb" attribute is ignored, it could be used as a name
                                corrModeName = self.getCorrelationMode().getName()
                                thisSpectralWindow["sw"] = (
                                    self._getRequiredAttributeValue(bbChildNode, "sw")
                                )
                                if (
                                    corrModeName == "CROSS_ONLY"
                                    or corrModeName == "CROSS_AND_AUTO"
                                ):
                                    # cross data values
                                    crossPolStrList = self._getRequiredAttributeValue(
                                        bbChildNode, "crossPolProducts"
                                    ).split()
                                    crossPolList = []
                                    for crossPolStr in crossPolStrList:
                                        crossPolList.append(
                                            pyasdm.enumerations.StokesParameter.literal(
                                                crossPolStr
                                            )
                                        )
                                        thisSpectralWindow["crossPolProducts"] = (
                                            crossPolList
                                        )
                                        # scale factor is a 32-bit float, keep that precision
                                        thisSpectralWindow["scaleFactor"] = np.float32(
                                            self._getRequiredAttributeValue(
                                                bbChildNode, "scaleFactor"
                                            )
                                        )
                                if (
                                    corrModeName == "AUTO_ONLY"
                                    or corrModeName == "CROSS_AND_AUTO"
                                ):
                                    # auto data values
                                    sdPolStrList = self._getRequiredAttributeValue(
                                        bbChildNode, "sdPolProducts"
                                    ).split()
                                    sdPolList = []
                                    for sdPolStr in sdPolStrList:
                                        sdPolList.append(
                                            pyasdm.enumerations.StokesParameter.literal(
                                                sdPolStr
                                            )
                                        )
                                    thisSpectralWindow["sdPolProducts"] = sdPolList
                                # all types
                                thisSpectralWindow["numSpectralPoint"] = int(
                                    self._getRequiredAttributeValue(
                                        bbChildNode, "numSpectralPoint"
                                    )
                                )
                                thisSpectralWindow["numBin"] = int(
                                    self._getRequiredAttributeValue(
                                        bbChildNode, "numBin"
                                    )
                                )
                                sidebandStr = self._getRequiredAttributeValue(
                                    bbChildNode, "sideband"
                                )
                                thisSpectralWindow["sideband"] = (
                                    pyasdm.enumerations.NetSideband.literal(sidebandStr)
                                )

                                spectralWindows.append(thisSpectralWindow)
                            bbChildNode = bbChildNode.nextSibling
                        thisBaseband["spectralWindows"] = spectralWindows
                        basebands.append(thisBaseband)

                    if dsChildNode.nodeName in self._binTypes:
                        self._setBinaryStruct(dsChildNode)

                    dsChildNode = dsChildNode.nextSibling

                # need to add the basebands assembed here
                self._dataStruct["basebands"] = basebands

                # the c++ code spends several lines to associate spectral window IDs but that code seems
                # to never be used as there's nothing that actually sets the relevant field in the SpectralWindow
                # class necessary to use that code. So, ignore that here

            childNode = childNode.nextSibling
