# ALMA - Atacama Large Millimeter Array
# (c) European Southern Observatory, 2002
# (c) Associated Universities Inc., 2002
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
# Warning!
#  --------------------------------------------------------------------
# | This is generated code!  Do not modify this file.                  |
# | If you do, all changes will be lost when the file is re-generated. |
#  --------------------------------------------------------------------
#
# File MainRow.py
#

import os

import pyasdm.MainTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.TimeSampling import TimeSampling


from xml.dom import minidom

import copy


class MainRow:
    """
    The MainRow class is a row of a MainTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a MainRow.
        When row is None, create an empty row attached to table, which must be a MainTable.
        When row is given, copy those values in to the new row. The row argument must be a MainRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.MainTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._time = ArrayTime()

        self._numAntenna = 0

        self._timeSampling = TimeSampling.from_int(0)

        self._interval = Interval()

        self._numIntegration = 0

        self._scanNumber = 0

        self._subscanNumber = 0

        self._dataSize = 0

        self._dataUID = EntityRef()

        # extrinsic attributes

        self._configDescriptionId = Tag()

        self._execBlockId = Tag()

        self._fieldId = Tag()

        self._stateId = []  # this is a list of Tag []

        if row is not None:
            if not isinstance(row, MainRow):
                raise ValueError("row must be a MainRow")

            # copy constructor

            self._time = ArrayTime(row._time)

            self._configDescriptionId = Tag(row._configDescriptionId)

            self._fieldId = Tag(row._fieldId)

            self._numAntenna = row._numAntenna

            # We force the attribute of the result to be not None
            if row._timeSampling is None:
                self._timeSampling = TimeSampling.from_int(0)
            else:
                self._timeSampling = TimeSampling(row._timeSampling)

            self._interval = Interval(row._interval)

            self._numIntegration = row._numIntegration

            self._scanNumber = row._scanNumber

            self._subscanNumber = row._subscanNumber

            self._dataSize = row._dataSize

            self._dataUID = EntityRef(row._dataUID)

            # stateId is a list, let's populate self._stateId element by element.
            if self._stateId is None:
                self._stateId = []

            for i in range(len(row._stateId)):

                self._stateId.append(Tag(row._stateId[i]))

            self._execBlockId = Tag(row._execBlockId)

    def isAdded(self):
        self._hasBeenAdded = True

    def getTable(self):
        """
        Return the table to which this row belongs.
        """
        return self._table

    def toXML(self):
        """
        Return this row in the form of an XML string.
        """
        result = ""

        result += "<row> \n"

        # intrinsic attributes

        result += Parser.extendedValueToXML("time", self._time)

        result += Parser.valueToXML("numAntenna", self._numAntenna)

        result += Parser.valueToXML(
            "timeSampling", TimeSampling.name(self._timeSampling)
        )

        result += Parser.extendedValueToXML("interval", self._interval)

        result += Parser.valueToXML("numIntegration", self._numIntegration)

        result += Parser.valueToXML("scanNumber", self._scanNumber)

        result += Parser.valueToXML("subscanNumber", self._subscanNumber)

        result += Parser.valueToXML("dataSize", self._dataSize)

        result += Parser.extendedValueToXML("dataUID", self._dataUID)

        # extrinsic attributes

        result += Parser.extendedValueToXML(
            "configDescriptionId", self._configDescriptionId
        )

        result += Parser.extendedValueToXML("execBlockId", self._execBlockId)

        result += Parser.extendedValueToXML("fieldId", self._fieldId)

        result += Parser.listExtendedValueToXML("stateId", self._stateId)

        # links, if any

        result += "</row>\n"
        return result

    def setFromXML(self, xmlrow):
        """
        Fill the values of this row from an XML string
        that was produced by the toXML() method.
        If xmlrow is a minidom.Element with a nodeName of row then
        it will be used as is. Anything else that is not a string
        is an error.
        """
        rowdom = None
        if isinstance(xmlrow, str):
            xmldom = minidom.parseString(xmlrow)
            rowdom = xmldom.firstChild
        elif isinstance(xmlrow, minidom.Element):
            rowdom = xmlrow
        else:
            raise ConversionException(
                "xmlrow is not a string or a minidom.Element", "MainTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "MainTable")

        # intrinsic attribute values

        timeNode = rowdom.getElementsByTagName("time")[0]

        self._time = ArrayTime(timeNode.firstChild.data.strip())

        numAntennaNode = rowdom.getElementsByTagName("numAntenna")[0]

        self._numAntenna = int(numAntennaNode.firstChild.data.strip())

        timeSamplingNode = rowdom.getElementsByTagName("timeSampling")[0]

        self._timeSampling = TimeSampling.newTimeSampling(
            timeSamplingNode.firstChild.data.strip()
        )

        intervalNode = rowdom.getElementsByTagName("interval")[0]

        self._interval = Interval(intervalNode.firstChild.data.strip())

        numIntegrationNode = rowdom.getElementsByTagName("numIntegration")[0]

        self._numIntegration = int(numIntegrationNode.firstChild.data.strip())

        scanNumberNode = rowdom.getElementsByTagName("scanNumber")[0]

        self._scanNumber = int(scanNumberNode.firstChild.data.strip())

        subscanNumberNode = rowdom.getElementsByTagName("subscanNumber")[0]

        self._subscanNumber = int(subscanNumberNode.firstChild.data.strip())

        dataSizeNode = rowdom.getElementsByTagName("dataSize")[0]

        self._dataSize = int(dataSizeNode.firstChild.data.strip())

        dataUIDNode = rowdom.getElementsByTagName("dataUID")[0]

        self._dataUID = EntityRef(dataUIDNode.toxml())

        # extrinsic attribute values

        configDescriptionIdNode = rowdom.getElementsByTagName("configDescriptionId")[0]

        self._configDescriptionId = Tag(configDescriptionIdNode.firstChild.data.strip())

        execBlockIdNode = rowdom.getElementsByTagName("execBlockId")[0]

        self._execBlockId = Tag(execBlockIdNode.firstChild.data.strip())

        fieldIdNode = rowdom.getElementsByTagName("fieldId")[0]

        self._fieldId = Tag(fieldIdNode.firstChild.data.strip())

        stateIdNode = rowdom.getElementsByTagName("stateId")[0]

        stateIdStr = stateIdNode.firstChild.data.strip()

        self._stateId = Parser.stringListToLists(stateIdStr, Tag, "Main", True)

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._time.toBin(eos)

        self._configDescriptionId.toBin(eos)

        self._fieldId.toBin(eos)

        eos.writeInt(self._numAntenna)

        eos.writeString(str(self._timeSampling))

        self._interval.toBin(eos)

        eos.writeInt(self._numIntegration)

        eos.writeInt(self._scanNumber)

        eos.writeInt(self._subscanNumber)

        eos.writeInt(self._dataSize)

        self._dataUID.toBin(eos)

        Tag.listToBin(self._stateId, eos)

        self._execBlockId.toBin(eos)

    @staticmethod
    def timeFromBin(row, eis):
        """
        Set the time in row from the EndianInput (eis) instance.
        """

        row._time = ArrayTime.fromBin(eis)

    @staticmethod
    def configDescriptionIdFromBin(row, eis):
        """
        Set the configDescriptionId in row from the EndianInput (eis) instance.
        """

        row._configDescriptionId = Tag.fromBin(eis)

    @staticmethod
    def fieldIdFromBin(row, eis):
        """
        Set the fieldId in row from the EndianInput (eis) instance.
        """

        row._fieldId = Tag.fromBin(eis)

    @staticmethod
    def numAntennaFromBin(row, eis):
        """
        Set the numAntenna in row from the EndianInput (eis) instance.
        """

        row._numAntenna = eis.readInt()

    @staticmethod
    def timeSamplingFromBin(row, eis):
        """
        Set the timeSampling in row from the EndianInput (eis) instance.
        """

        row._timeSampling = TimeSampling.literal(eis.readString())

    @staticmethod
    def intervalFromBin(row, eis):
        """
        Set the interval in row from the EndianInput (eis) instance.
        """

        row._interval = Interval.fromBin(eis)

    @staticmethod
    def numIntegrationFromBin(row, eis):
        """
        Set the numIntegration in row from the EndianInput (eis) instance.
        """

        row._numIntegration = eis.readInt()

    @staticmethod
    def scanNumberFromBin(row, eis):
        """
        Set the scanNumber in row from the EndianInput (eis) instance.
        """

        row._scanNumber = eis.readInt()

    @staticmethod
    def subscanNumberFromBin(row, eis):
        """
        Set the subscanNumber in row from the EndianInput (eis) instance.
        """

        row._subscanNumber = eis.readInt()

    @staticmethod
    def dataSizeFromBin(row, eis):
        """
        Set the dataSize in row from the EndianInput (eis) instance.
        """

        row._dataSize = eis.readInt()

    @staticmethod
    def dataUIDFromBin(row, eis):
        """
        Set the dataUID in row from the EndianInput (eis) instance.
        """

        row._dataUID = EntityRef.fromBin(eis)

    @staticmethod
    def stateIdFromBin(row, eis):
        """
        Set the stateId in row from the EndianInput (eis) instance.
        """

        row._stateId = Tag.from1DBin(eis)

    @staticmethod
    def execBlockIdFromBin(row, eis):
        """
        Set the execBlockId in row from the EndianInput (eis) instance.
        """

        row._execBlockId = Tag.fromBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["time"] = MainRow.timeFromBin
        _fromBinMethods["configDescriptionId"] = MainRow.configDescriptionIdFromBin
        _fromBinMethods["fieldId"] = MainRow.fieldIdFromBin
        _fromBinMethods["numAntenna"] = MainRow.numAntennaFromBin
        _fromBinMethods["timeSampling"] = MainRow.timeSamplingFromBin
        _fromBinMethods["interval"] = MainRow.intervalFromBin
        _fromBinMethods["numIntegration"] = MainRow.numIntegrationFromBin
        _fromBinMethods["scanNumber"] = MainRow.scanNumberFromBin
        _fromBinMethods["subscanNumber"] = MainRow.subscanNumberFromBin
        _fromBinMethods["dataSize"] = MainRow.dataSizeFromBin
        _fromBinMethods["dataUID"] = MainRow.dataUIDFromBin
        _fromBinMethods["stateId"] = MainRow.stateIdFromBin
        _fromBinMethods["execBlockId"] = MainRow.execBlockIdFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = MainRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Main",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute time

    _time = ArrayTime()

    def getTime(self):
        """
        Get time.
        return time as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._time)

    def setTime(self, time):
        """
        Set time with the specified ArrayTime value.
        time The ArrayTime value to which time is to be set.
        The value of time can be anything allowed by the ArrayTime constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the time field, which is part of the key, after this row has been added to this table."
            )

        self._time = ArrayTime(time)

    # ===> Attribute numAntenna

    _numAntenna = 0

    def getNumAntenna(self):
        """
        Get numAntenna.
        return numAntenna as int
        """

        return self._numAntenna

    def setNumAntenna(self, numAntenna):
        """
        Set numAntenna with the specified int value.
        numAntenna The int value to which numAntenna is to be set.


        """

        self._numAntenna = int(numAntenna)

    # ===> Attribute timeSampling

    _timeSampling = TimeSampling.from_int(0)

    def getTimeSampling(self):
        """
        Get timeSampling.
        return timeSampling as TimeSampling
        """

        return self._timeSampling

    def setTimeSampling(self, timeSampling):
        """
        Set timeSampling with the specified TimeSampling value.
        timeSampling The TimeSampling value to which timeSampling is to be set.


        """

        self._timeSampling = TimeSampling(timeSampling)

    # ===> Attribute interval

    _interval = Interval()

    def getInterval(self):
        """
        Get interval.
        return interval as Interval
        """

        # make sure it is a copy of Interval
        return Interval(self._interval)

    def setInterval(self, interval):
        """
        Set interval with the specified Interval value.
        interval The Interval value to which interval is to be set.
        The value of interval can be anything allowed by the Interval constructor.

        """

        self._interval = Interval(interval)

    # ===> Attribute numIntegration

    _numIntegration = 0

    def getNumIntegration(self):
        """
        Get numIntegration.
        return numIntegration as int
        """

        return self._numIntegration

    def setNumIntegration(self, numIntegration):
        """
        Set numIntegration with the specified int value.
        numIntegration The int value to which numIntegration is to be set.


        """

        self._numIntegration = int(numIntegration)

    # ===> Attribute scanNumber

    _scanNumber = 0

    def getScanNumber(self):
        """
        Get scanNumber.
        return scanNumber as int
        """

        return self._scanNumber

    def setScanNumber(self, scanNumber):
        """
        Set scanNumber with the specified int value.
        scanNumber The int value to which scanNumber is to be set.


        """

        self._scanNumber = int(scanNumber)

    # ===> Attribute subscanNumber

    _subscanNumber = 0

    def getSubscanNumber(self):
        """
        Get subscanNumber.
        return subscanNumber as int
        """

        return self._subscanNumber

    def setSubscanNumber(self, subscanNumber):
        """
        Set subscanNumber with the specified int value.
        subscanNumber The int value to which subscanNumber is to be set.


        """

        self._subscanNumber = int(subscanNumber)

    # ===> Attribute dataSize

    _dataSize = 0

    def getDataSize(self):
        """
        Get dataSize.
        return dataSize as int
        """

        return self._dataSize

    def setDataSize(self, dataSize):
        """
        Set dataSize with the specified int value.
        dataSize The int value to which dataSize is to be set.


        """

        self._dataSize = int(dataSize)

    # ===> Attribute dataUID

    _dataUID = EntityRef()

    def getDataUID(self):
        """
        Get dataUID.
        return dataUID as EntityRef
        """

        # make sure it is a copy of EntityRef
        return EntityRef(self._dataUID)

    def setDataUID(self, dataUID):
        """
        Set dataUID with the specified EntityRef value.
        dataUID The EntityRef value to which dataUID is to be set.
        The value of dataUID can be anything allowed by the EntityRef constructor.

        """

        self._dataUID = EntityRef(dataUID)

    def getBDFPath(self):
        """
        Return a path to the BDF using dataUID and the directory of this ASDM.

        This takes the dataUID value and the directory of the container in
        the table this row is attached to and it returns a string containing
        the path where that BDF should be found.
        """
        bdfName = str(self.getDataUID().getEntityId())
        # convert "/" and ":" to "_"
        bdfName = bdfName.replace("/", "_")
        bdfName = bdfName.replace(":", "_")

        result = os.path.join(
            self._table.getContainer().getDirectory(), "ASDMBinary", bdfName
        )
        return result

    # Extrinsic Table Attributes

    # ===> Attribute configDescriptionId

    _configDescriptionId = Tag()

    def getConfigDescriptionId(self):
        """
        Get configDescriptionId.
        return configDescriptionId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._configDescriptionId)

    def setConfigDescriptionId(self, configDescriptionId):
        """
        Set configDescriptionId with the specified Tag value.
        configDescriptionId The Tag value to which configDescriptionId is to be set.
        The value of configDescriptionId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the configDescriptionId field, which is part of the key, after this row has been added to this table."
            )

        self._configDescriptionId = Tag(configDescriptionId)

    # ===> Attribute execBlockId

    _execBlockId = Tag()

    def getExecBlockId(self):
        """
        Get execBlockId.
        return execBlockId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._execBlockId)

    def setExecBlockId(self, execBlockId):
        """
        Set execBlockId with the specified Tag value.
        execBlockId The Tag value to which execBlockId is to be set.
        The value of execBlockId can be anything allowed by the Tag constructor.

        """

        self._execBlockId = Tag(execBlockId)

    # ===> Attribute fieldId

    _fieldId = Tag()

    def getFieldId(self):
        """
        Get fieldId.
        return fieldId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._fieldId)

    def setFieldId(self, fieldId):
        """
        Set fieldId with the specified Tag value.
        fieldId The Tag value to which fieldId is to be set.
        The value of fieldId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the fieldId field, which is part of the key, after this row has been added to this table."
            )

        self._fieldId = Tag(fieldId)

    # ===> Attribute stateId

    _stateId = []  # this is a list of Tag []

    def getStateId(self):
        """
        Get stateId.
        return stateId as Tag []
        """

        return copy.deepcopy(self._stateId)

    def setStateId(self, stateId):
        """
        Set stateId with the specified Tag []  value.
        stateId The Tag []  value to which stateId is to be set.
        The value of stateId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(stateId, list):
            raise ValueError("The value of stateId must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(stateId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of stateId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(stateId, Tag):
                raise ValueError(
                    "type of the first value in stateId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._stateId = copy.deepcopy(stateId)
        except Exception as exc:
            raise ValueError("Invalid stateId : " + str(exc))

    # Links

    def getConfigDescriptionUsingConfigDescriptionId(self):
        """
        Returns the row in the ConfigDescription table having ConfigDescription.configDescriptionId == configDescriptionId

        """

        return (
            self._table.getContainer()
            .getConfigDescription()
            .getRowByKey(self._configDescriptionId)
        )

    def getFieldUsingFieldId(self):
        """
        Returns the row in the Field table having Field.fieldId == fieldId

        """

        return self._table.getContainer().getField().getRowByKey(self._fieldId)

    def setOneStateId(self, index, stateId):
        """
        Set stateId[index] with the specified Tag value.
        index The index in stateId where to set the Tag value.
        stateId The Tag value to which stateId[index] is to be set.

        """

        self._stateId[index] = Tag(stateId)

    # ===> hasmany link from a row of Main table to many rows of State table.

    def addStateId(self, id):
        """
        Append a Tag to stateId
        id the Tag to be appended to stateId
        """
        if isinstance(id, list):
            for thisValue in id:
                self._stateId.append(Tag(thisValue))
        else:
            self._stateId.append(Tag(id))

    def getOneStateId(self, i):
        """
        Returns the Tag stored in stateId at position i.
        """
        return self._stateId[i]

    def getStateUsingStateId(self, i):
        """
        Returns the StateRow linked to this row via the Tag stored in stateId
        at position i.
        """

        return self._table.getContainer().getState().getRowByKey(self._stateId[i])

    def getStatesUsingStateId(self):
        """
        Returns the array of StateRow linked to this row via the Tags stored in stateId
        """
        result = []
        for thisItem in self._stateId:
            result.append(self._table.getContainer().getState().getRowByKey(thisItem))

        return result

    def getExecBlockUsingExecBlockId(self):
        """
        Returns the row in the ExecBlock table having ExecBlock.execBlockId == execBlockId

        """

        return self._table.getContainer().getExecBlock().getRowByKey(self._execBlockId)

    # comparison methods

    def compareNoAutoInc(
        self,
        time,
        configDescriptionId,
        fieldId,
        numAntenna,
        timeSampling,
        interval,
        numIntegration,
        scanNumber,
        subscanNumber,
        dataSize,
        dataUID,
        stateId,
        execBlockId,
    ):
        """
        Compare each attribute except the autoincrementable one of this MainRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # time is a ArrayTime, compare using the equals method.
        if not self._time.equals(time):
            return False

        # configDescriptionId is a Tag, compare using the equals method.
        if not self._configDescriptionId.equals(configDescriptionId):
            return False

        # fieldId is a Tag, compare using the equals method.
        if not self._fieldId.equals(fieldId):
            return False

        # numAntenna is a int, compare using the == operator.
        if not (self._numAntenna == numAntenna):
            return False

        # timeSampling is a TimeSampling, compare using the == operator on the getValue() output
        if not (self._timeSampling.getValue() == timeSampling.getValue()):
            return False

        # interval is a Interval, compare using the equals method.
        if not self._interval.equals(interval):
            return False

        # numIntegration is a int, compare using the == operator.
        if not (self._numIntegration == numIntegration):
            return False

        # scanNumber is a int, compare using the == operator.
        if not (self._scanNumber == scanNumber):
            return False

        # subscanNumber is a int, compare using the == operator.
        if not (self._subscanNumber == subscanNumber):
            return False

        # dataSize is a int, compare using the == operator.
        if not (self._dataSize == dataSize):
            return False

        # dataUID is a EntityRef, compare using the equals method.
        if not self._dataUID.equals(dataUID):
            return False

        # stateId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._stateId) != len(stateId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._stateId)):
            if not (self._stateId[indx].equals(stateId[indx])):
                return False

        # execBlockId is a Tag, compare using the equals method.
        if not self._execBlockId.equals(execBlockId):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumAntenna(),
            otherRow.getTimeSampling(),
            otherRow.getInterval(),
            otherRow.getNumIntegration(),
            otherRow.getScanNumber(),
            otherRow.getSubscanNumber(),
            otherRow.getDataSize(),
            otherRow.getDataUID(),
            otherRow.getStateId(),
            otherRow.getExecBlockId(),
        )

    def compareRequiredValue(
        self,
        numAntenna,
        timeSampling,
        interval,
        numIntegration,
        scanNumber,
        subscanNumber,
        dataSize,
        dataUID,
        stateId,
        execBlockId,
    ):

        # numAntenna is a int, compare using the == operator.
        if not (self._numAntenna == numAntenna):
            return False

        # timeSampling is a TimeSampling, compare using the == operator on the getValue() output
        if not (self._timeSampling.getValue() == timeSampling.getValue()):
            return False

        # interval is a Interval, compare using the equals method.
        if not self._interval.equals(interval):
            return False

        # numIntegration is a int, compare using the == operator.
        if not (self._numIntegration == numIntegration):
            return False

        # scanNumber is a int, compare using the == operator.
        if not (self._scanNumber == scanNumber):
            return False

        # subscanNumber is a int, compare using the == operator.
        if not (self._subscanNumber == subscanNumber):
            return False

        # dataSize is a int, compare using the == operator.
        if not (self._dataSize == dataSize):
            return False

        # dataUID is a EntityRef, compare using the equals method.
        if not self._dataUID.equals(dataUID):
            return False

        # stateId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._stateId) != len(stateId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._stateId)):
            if not (self._stateId[indx].equals(stateId[indx])):
                return False

        # execBlockId is a Tag, compare using the equals method.
        if not self._execBlockId.equals(execBlockId):
            return False

        return True


# initialize the dictionary that maps fields to init methods
MainRow.initFromBinMethods()
