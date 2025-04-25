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
        self._schemaVersion = 0   # int in c++
        self._byteOrder = pyasdm.ByteOrder.ByteOrder() # native byte order
        # projectPath is kept in its parts : execBlockNum, scanNum, subscanNum
        self._execBlockNum = 0  # an unsigned integer in c++
        self._scanNum = 0 # an unsigned integer in c++
        self._subscanNum = 0 # an unsigned integer in c++
        self._startTime = 0 # an unsigned long long in c++

        # dimensionality and numTime are set when preent, only 1 of them should be non-zero
        self._dimensionality = 0
        self._numTime = 0

        self._dataOID = None
        self._execBlockUID = None
        self._title = None
        self._numAntenna = 0 # an unsigned integer in c++
        self._correlationMode = None # a CorrelationMode enumeration when set
        self._spectralResolutionType = None # a SpectralResolutionType enumeration when set
        self._processorType = None # a ProcessorType enumeration when set

        self._dataStruct = {
            'apc':[],         # list of AtmPhaseCorrection instances
            'basebands':[],   # list of basebands instances, name and a spectral window struct
            'flags':{'size':0,'axes':[]},  # unsigned int, list AxisName enumerations
            'actualTimes':{'size':0,'axes':[]},
            'actualDurations':{'size':0,'axes':[]},
            'zeroLags':{'size':0,'axes':[],'correlatorType':None}, # CorrelatorType enumeration
            'crossData':{'size':0,'axes':[]},
            'autoData':{'size':0,'axes':[],'normalized':False}
            }

        # the binary type names in _dataStruct, each of these is a structure with a "size" and "axes" value
        self._binTypes = ['flags','actualTimes','actualDurations','zeroLags','crossData','autoData']

    def getBinaryTypes(self):
        """
        Return a list of the known types of binary data.
        """
        return self._binTypes

    def projectPath(self):
        """
        Return the project path using execBlockNum, scanNum, and subscanNum.
        """
        return ("%s/%s/%s/" % (self._execBlockNum, self._scanNum, self._subscanNum))

    def getSize(self, binaryType):
        """
        Get the size of the named binary type.
        """
        if binaryType not in self._binTypes:
            raise ValueError("unrecognized binaryType value")
        return self._dataStruct[binaryType]['size']

    def getAxes(self, binaryType):
        """
        Get the AxisNames enumeration list for the given binary type.
        """
        if binaryType not in self._binTypes:
            raise ValueError("unrecognized binaryType value")
        return self._dataStruct[binaryType]['axes']

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
        return (self.getSize(binaryType) > 0)

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
            raise ValueError("dimensionality can not be set to a non-zero value when numTime is positive")
        
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
            raise ValueError("numTime can not be set to a non-zero value when dimensionality is positive")
        
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
        self._correlationMode = pyasdm.enumerations.CorrelationMode.CorrelationMode.literal(correlationMode)

    def getCorrelationMode(self):
        """
        gets the correlationMode
        """
        return self._correlationMode

    def setSpectralResolutionType(self, spectralResolutionType):
        """
        sets the spectralResolutionType, spectralResolutionType is any value that can be used for the SpectralResolutionType enumeration
        """
        self._spectralResolutionType = pyasdm.enumerations.SpectralResolutionType.SpectralResolutionType.literal(spectralResolutionType)

    def getSpectralResolutionType(self):
        """
        gets the spectralResolutionType
        """
        return self._spectralResolutionType

    def setProcessorType(self, processorType):
        """
        sets the processorType, processorType is any value that can be used for the ProcessorType enumeration
        """
        self._processorType = pyasdm.enumerations.ProcessorType.ProcessorType.literal(processorType)

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
            if not isinstance(item, pyasdm.enumerations.AtmPhaseCorrection.AtmPhaseCorrection):
                raise ValueError("apcList must be a list of AtmPhaseCorrection instances")

        self._dataStruct['apc'] = apcList

    def getAPClist(self):
        """
        Returns the apc list from the data struct.
        """
        return self._dataStruct['apc']

    def getBasebandsList(self):
        """
        Returns the basebands list, a list of structs, from the data struct
        """
        return self._dataStruct['basebands']

    def _setBinaryStruct(self, binaryNode):
        """
        Internal method that sets the values of the data struct appropriate to the name
        of binary, which must be one of flags, actualTimes, actualDurations, crossData,
        autoData, or zeroLags.
        """
        self._dataStruct[binaryNode.nodeName]['size'] = int(binaryNode.attributes.getNamedItem("size").value)
        axesStrList = binaryNode.attributes.getNamedItem("axes").value.split()
        axesList = []
        for axisStr in axesStrList:
            axesList.append(pyasdm.enumerations.AxisName.AxisName.literal(axisStr))
        self._dataStruct[binaryNode.nodeName]['axes'] = axesList
        if binaryNode.nodeName == "autoData":
            self._dataStruct[binaryNode.nodeName]['normalized'] = bool(binaryNode.attributes.getNamedItem("normalized").value)
        elif binaryNode.nodeName == "zeroLags":
            correlatorTypeValue = binaryNode.attributes.getNamedItem("correlatorType").value
            self._dataStruct[binaryNode.nodeName]['correlatorType'] = pyasdm.enumerations.CorrelatorType.CorrelatorType.literal(correlatorTypeValue)
    
    def fromDOM(self, dataHeaderElem):
        """
        set this from a minidom that is an sdmDataHeader element
        """

        # schemaVersion is found sometimes in the xvers namespace and sometimes not in a namespace
        # the c++ code finds it either way, when both are present it finds the one not in a namespace
        # so look for that first
        schemaVersionAttr = dataHeaderElem.attributes.getNamedItem("schemaVersion")
        if schemaVersionAttr is None:
            schemaVersionAttr = dataHeaderElem.attributes.getNamedItem("xvers:schemaVersion")
        self.setSchemaVersion(schemaVersionAttr.value)
        
        self.setByteOrder(dataHeaderElem.attributes.getNamedItem("byteOrder").value)
        
        projectPath = dataHeaderElem.attributes.getNamedItem("projectPath").value
        projectPathParts = projectPath.split("/")
        # in general a projectPath can have 3 to 5 parts : execBlock / scanNum / subscanNum / integrationNum / subintegrationNum
        # here, it should only have the first 3 parts, there is a trailing / so 4 parts with an empty 4th part is OK
        if len(projectPathParts) > 4 or (len(projectPathParts) == 4 and len(projectPathParts[3]) != 0):
            raise pyasdm.exceptions.BDFReaderException.BDFReaderException("Invalid string for projectPath '" + projectPath + "'")
        
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
                # get the href value from here, in the xlink namespace
                self.setDataOID(childNode.attributes.getNamedItem("xlink:href").value)
                # and the title
                self.setTitle(childNode.attributes.getNamedItem("xlink:title").value)
            if childNode.nodeName == "dimensionality":
                self.setDimensionality(childNode.firstChild.data)
            if childNode.nodeName == "numTime":
                self.setNumTime(childNode.firstChild.data)
            if childNode.nodeName == "execBlock":
                    # get the href value, xlink namespace, namespace may be missing, prefer non-namespace version
                execBlockAttr = childNode.attributes.getNamedItem("href")
                if execBlockAttr is None:
                    execBlockAttr = childNode.attributes.getNamedItem("xlink:href")
                self.setExecBlockUID(execBlockAttr.value)
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
                if (self.getCorrelationMode().getName() == "CROSS_ONLY") or (self.getCorrelationMode().getName() == "CROSS_AND_AUTO"):
                    # apc is an atttribute that is expected here
                    # it is a space-separated list of AtmPhaseCorrection enumeration names
                    apcList = childNode.attributes.getNamedItem("apc").value.split()
                    for apcName in apcList:
                        apcEnumList.append(pyasdm.enumerations.AtmPhaseCorrection.AtmPhaseCorrection.literal(apcName))
                self.setAPClist(apcEnumList)
                        
                # the child nodes
                # list of baseband structs to be assembled here
                basebands = []
                dsChildNode = childNode.firstChild
                while dsChildNode is not None:
                    if dsChildNode.nodeName == "baseband":
                        thisBaseband = {}
                        thisBaseband["name"] = dsChildNode.attributes.getNamedItem('name').value
                        # ths children describe the associated spectral windows
                        bbChildNode = dsChildNode.firstChild
                        spectralWindows = []
                        while bbChildNode is not None:
                            if bbChildNode.nodeName == 'spectralWindow':
                                thisSpectralWindow = {'crossPolProducts':[],
                                                      'sdPolProducts':[],
                                                      'scaleFactor':None,
                                                      'numSpectralPoint':None,
                                                      'numBin':None,
                                                      'sideband':None,
                                                      'sw':None}
                                # the "swbb" attribute is ignored, it could be used as a name
                                corrModeName = self.getCorrelationMode().getName()
                                thisSpectralWindow['sw'] = bbChildNode.attributes.getNamedItem('sw').value
                                if corrModeName == "CROSS_ONLY" or corrModeName == "CROSS_AND_AUTO":
                                    # cross data values
                                    crossPolStrList = bbChildNode.attributes.getNamedItem('crossPolProducts').value.split()
                                    crossPolList = []
                                    for crossPolStr in crossPolStrList:
                                        crossPolList.append(pyasdm.enumerations.StokesParameter.StokesParameter.literal(crossPolStr))
                                        thisSpectralWindow['crossPolProducts'] = crossPolList
                                        # scale factor is a 32-bit float, keep that precision
                                        thisSpectralWindow['scaleFactor'] = np.float32(bbChildNode.attributes.getNamedItem('scaleFactor').value)
                                if corrModeName == "AUTO_ONLY" or corrModeName == "CROSS_AND_AUTO":
                                    # auto data values
                                    sdPolStrList = bbChildNode.attributes.getNamedItem('sdPolProducts').value.split()
                                    sdPolList = []
                                    for sdPolStr in sdPolStrList:
                                        sdPolList.append(pyasdm.enumerations.StokesParameter.StokesParameter.literal(sdPolStr))
                                    thisSpectralWindow['sdPolProducts'] = sdPolList
                                # all types
                                thisSpectralWindow['numSpectralPoint'] = int(bbChildNode.attributes.getNamedItem('numSpectralPoint').value)
                                thisSpectralWindow['numBin'] = int(bbChildNode.attributes.getNamedItem('numBin').value)
                                sidebandStr = bbChildNode.attributes.getNamedItem('sideband').value
                                thisSpectralWindow['sideband'] = pyasdm.enumerations.NetSideband.NetSideband.literal(sidebandStr)
                                
                                spectralWindows.append(thisSpectralWindow)
                            bbChildNode = bbChildNode.nextSibling
                        thisBaseband["spectralWindows"] = spectralWindows
                        basebands.append(thisBaseband)

                    if dsChildNode.nodeName in self._binTypes:
                        self._setBinaryStruct(dsChildNode)
                        
                    dsChildNode = dsChildNode.nextSibling
                                    
                # need to add the basebands assembed here
                self._dataStruct['basebands'] = basebands

                # the c++ code spends several lines to associate spectral window IDs but that code seems
                # to never be used as there's nothing that actually sets the relevant field in the SpectralWindow
                # class necessary to use that code. So, ignore that here

            childNode= childNode.nextSibling

