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
# File TotalPowerRow.py
#

import pyasdm.TotalPowerTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from xml.dom import minidom

import copy


class TotalPowerRow:
    """
    The TotalPowerRow class is a row of a TotalPowerTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a TotalPowerRow.
        When row is None, create an empty row attached to table, which must be a TotalPowerTable.
        When row is given, copy those values in to the new row. The row argument must be a TotalPowerRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.TotalPowerTable):
            raise ValueError("table must be a TotalPowerTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._time = ArrayTime()

        self._scanNumber = 0

        self._subscanNumber = 0

        self._integrationNumber = 0

        self._uvw = []  # this is a list of Length []  []

        self._exposure = []  # this is a list of Interval []  []

        self._timeCentroid = []  # this is a list of ArrayTime []  []

        self._floatData = []  # this is a list of float []  []  []

        self._flagAnt = []  # this is a list of int []

        self._flagPol = []  # this is a list of int []  []

        self._interval = Interval()

        self._subintegrationNumberExists = False

        self._subintegrationNumber = 0

        # extrinsic attributes

        self._configDescriptionId = Tag()

        self._execBlockId = Tag()

        self._fieldId = Tag()

        self._stateId = []  # this is a list of Tag []

        if row is not None:
            if not isinstance(row, TotalPowerRow):
                raise ValueError("row must be a TotalPowerRow")

            # copy constructor

            self._time = ArrayTime(row._time)

            self._configDescriptionId = Tag(row._configDescriptionId)

            self._fieldId = Tag(row._fieldId)

            self._scanNumber = row._scanNumber

            self._subscanNumber = row._subscanNumber

            self._integrationNumber = row._integrationNumber

            # uvw is a  list , make a deep copy
            self._uvw = copy.deepcopy(row._uvw)

            # exposure is a  list , make a deep copy
            self._exposure = copy.deepcopy(row._exposure)

            # timeCentroid is a  list , make a deep copy
            self._timeCentroid = copy.deepcopy(row._timeCentroid)

            # floatData is a  list , make a deep copy
            self._floatData = copy.deepcopy(row._floatData)

            # flagAnt is a  list , make a deep copy
            self._flagAnt = copy.deepcopy(row._flagAnt)

            # flagPol is a  list , make a deep copy
            self._flagPol = copy.deepcopy(row._flagPol)

            self._interval = Interval(row._interval)

            # stateId is a list, let's populate self._stateId element by element.
            if self._stateId is None:
                self._stateId = []

            for i in range(len(row._stateId)):

                self._stateId.append(Tag(row._stateId[i]))

            self._execBlockId = Tag(row._execBlockId)

            # by default set systematically subintegrationNumber's value to something not None

            if row._subintegrationNumberExists:

                self._subintegrationNumber = row._subintegrationNumber

                self._subintegrationNumberExists = True

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

        result += Parser.valueToXML("scanNumber", self._scanNumber)

        result += Parser.valueToXML("subscanNumber", self._subscanNumber)

        result += Parser.valueToXML("integrationNumber", self._integrationNumber)

        result += Parser.listExtendedValueToXML("uvw", self._uvw)

        result += Parser.listExtendedValueToXML("exposure", self._exposure)

        result += Parser.listExtendedValueToXML("timeCentroid", self._timeCentroid)

        result += Parser.listValueToXML("floatData", self._floatData)

        result += Parser.listValueToXML("flagAnt", self._flagAnt)

        result += Parser.listValueToXML("flagPol", self._flagPol)

        result += Parser.extendedValueToXML("interval", self._interval)

        if self._subintegrationNumberExists:

            result += Parser.valueToXML(
                "subintegrationNumber", self._subintegrationNumber
            )

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
                "xmlrow is not a string or a minidom.Element", "TotalPowerTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "TotalPowerTable")

        # intrinsic attribute values

        timeNode = rowdom.getElementsByTagName("time")[0]

        self._time = ArrayTime(timeNode.firstChild.data.strip())

        scanNumberNode = rowdom.getElementsByTagName("scanNumber")[0]

        self._scanNumber = int(scanNumberNode.firstChild.data.strip())

        subscanNumberNode = rowdom.getElementsByTagName("subscanNumber")[0]

        self._subscanNumber = int(subscanNumberNode.firstChild.data.strip())

        integrationNumberNode = rowdom.getElementsByTagName("integrationNumber")[0]

        self._integrationNumber = int(integrationNumberNode.firstChild.data.strip())

        uvwNode = rowdom.getElementsByTagName("uvw")[0]

        uvwStr = uvwNode.firstChild.data.strip()

        self._uvw = Parser.stringListToLists(uvwStr, Length, "TotalPower", True)

        exposureNode = rowdom.getElementsByTagName("exposure")[0]

        exposureStr = exposureNode.firstChild.data.strip()

        self._exposure = Parser.stringListToLists(
            exposureStr, Interval, "TotalPower", True
        )

        timeCentroidNode = rowdom.getElementsByTagName("timeCentroid")[0]

        timeCentroidStr = timeCentroidNode.firstChild.data.strip()

        self._timeCentroid = Parser.stringListToLists(
            timeCentroidStr, ArrayTime, "TotalPower", True
        )

        floatDataNode = rowdom.getElementsByTagName("floatData")[0]

        floatDataStr = floatDataNode.firstChild.data.strip()

        self._floatData = Parser.stringListToLists(
            floatDataStr, float, "TotalPower", False
        )

        flagAntNode = rowdom.getElementsByTagName("flagAnt")[0]

        flagAntStr = flagAntNode.firstChild.data.strip()

        self._flagAnt = Parser.stringListToLists(flagAntStr, int, "TotalPower", False)

        flagPolNode = rowdom.getElementsByTagName("flagPol")[0]

        flagPolStr = flagPolNode.firstChild.data.strip()

        self._flagPol = Parser.stringListToLists(flagPolStr, int, "TotalPower", False)

        intervalNode = rowdom.getElementsByTagName("interval")[0]

        self._interval = Interval(intervalNode.firstChild.data.strip())

        subintegrationNumberNode = rowdom.getElementsByTagName("subintegrationNumber")
        if len(subintegrationNumberNode) > 0:

            self._subintegrationNumber = int(
                subintegrationNumberNode[0].firstChild.data.strip()
            )

            self._subintegrationNumberExists = True

        # extrinsic attribute values

        configDescriptionIdNode = rowdom.getElementsByTagName("configDescriptionId")[0]

        self._configDescriptionId = Tag(configDescriptionIdNode.firstChild.data.strip())

        execBlockIdNode = rowdom.getElementsByTagName("execBlockId")[0]

        self._execBlockId = Tag(execBlockIdNode.firstChild.data.strip())

        fieldIdNode = rowdom.getElementsByTagName("fieldId")[0]

        self._fieldId = Tag(fieldIdNode.firstChild.data.strip())

        stateIdNode = rowdom.getElementsByTagName("stateId")[0]

        stateIdStr = stateIdNode.firstChild.data.strip()

        self._stateId = Parser.stringListToLists(stateIdStr, Tag, "TotalPower", True)

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._time.toBin(eos)

        self._configDescriptionId.toBin(eos)

        self._fieldId.toBin(eos)

        eos.writeInt(self._scanNumber)

        eos.writeInt(self._subscanNumber)

        eos.writeInt(self._integrationNumber)

        Length.listToBin(self._uvw, eos)

        Interval.listToBin(self._exposure, eos)

        ArrayTime.listToBin(self._timeCentroid, eos)

        # null array case, unsure if this is possible but this should work
        if self._floatData is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            floatData_dims = Parser.getListDims(self._floatData)
        # assumes it really is 3D
        eos.writeInt(floatData_dims[0])
        eos.writeInt(floatData_dims[1])
        eos.writeInt(floatData_dims[2])
        for i in range(floatData_dims[0]):
            for j in range(floatData_dims[1]):
                for k in range(floatData_dims[2]):
                    eos.writeFloat(self._floatData[i][j][k])

        eos.writeInt(len(self._flagAnt))
        for i in range(len(self._flagAnt)):

            eos.writeInt(self._flagAnt[i])

        # null array case, unsure if this is possible but this should work
        if self._flagPol is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            flagPol_dims = Parser.getListDims(self._flagPol)
        # assumes it really is 2D
        eos.writeInt(flagPol_dims[0])
        eos.writeInt(flagPol_dims[1])
        for i in range(flagPol_dims[0]):
            for j in range(flagPol_dims[1]):
                eos.writeInt(self._flagPol[i][j])

        self._interval.toBin(eos)

        Tag.listToBin(self._stateId, eos)

        self._execBlockId.toBin(eos)

        eos.writeBool(self._subintegrationNumberExists)
        if self._subintegrationNumberExists:

            eos.writeInt(self._subintegrationNumber)

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
    def integrationNumberFromBin(row, eis):
        """
        Set the integrationNumber in row from the EndianInput (eis) instance.
        """

        row._integrationNumber = eis.readInt()

    @staticmethod
    def uvwFromBin(row, eis):
        """
        Set the uvw in row from the EndianInput (eis) instance.
        """

        row._uvw = Length.from2DBin(eis)

    @staticmethod
    def exposureFromBin(row, eis):
        """
        Set the exposure in row from the EndianInput (eis) instance.
        """

        row._exposure = Interval.from2DBin(eis)

    @staticmethod
    def timeCentroidFromBin(row, eis):
        """
        Set the timeCentroid in row from the EndianInput (eis) instance.
        """

        row._timeCentroid = ArrayTime.from2DBin(eis)

    @staticmethod
    def floatDataFromBin(row, eis):
        """
        Set the floatData in row from the EndianInput (eis) instance.
        """

        floatDataDim1 = eis.readInt()
        floatDataDim2 = eis.readInt()
        floatDataDim3 = eis.readInt()
        thisList = []
        for i in range(floatDataDim1):
            thisList_j = []
            for j in range(floatDataDim2):
                thisList_k = []
                for k in range(floatDataDim3):
                    thisValue = eis.readFloat()
                    thisList_k.append(thisValue)
                thisList_j.append(thisList_k)
            thisList.append(thisList_j)
        row.floatData = thisList

    @staticmethod
    def flagAntFromBin(row, eis):
        """
        Set the flagAnt in row from the EndianInput (eis) instance.
        """

        flagAntDim1 = eis.readInt()
        thisList = []
        for i in range(flagAntDim1):
            thisValue = eis.readInt()
            thisList.append(thisValue)
        row._flagAnt = thisList

    @staticmethod
    def flagPolFromBin(row, eis):
        """
        Set the flagPol in row from the EndianInput (eis) instance.
        """

        flagPolDim1 = eis.readInt()
        flagPolDim2 = eis.readInt()
        thisList = []
        for i in range(flagPolDim1):
            thisList_j = []
            for j in range(flagPolDim2):
                thisValue = eis.readInt()
                thisList_j.append(thisValue)
            thisList.append(thisList_j)
        row.flagPol = thisList

    @staticmethod
    def intervalFromBin(row, eis):
        """
        Set the interval in row from the EndianInput (eis) instance.
        """

        row._interval = Interval.fromBin(eis)

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
    def subintegrationNumberFromBin(row, eis):
        """
        Set the optional subintegrationNumber in row from the EndianInput (eis) instance.
        """
        row._subintegrationNumberExists = eis.readBool()
        if row._subintegrationNumberExists:

            row._subintegrationNumber = eis.readInt()

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["time"] = TotalPowerRow.timeFromBin
        _fromBinMethods["configDescriptionId"] = (
            TotalPowerRow.configDescriptionIdFromBin
        )
        _fromBinMethods["fieldId"] = TotalPowerRow.fieldIdFromBin
        _fromBinMethods["scanNumber"] = TotalPowerRow.scanNumberFromBin
        _fromBinMethods["subscanNumber"] = TotalPowerRow.subscanNumberFromBin
        _fromBinMethods["integrationNumber"] = TotalPowerRow.integrationNumberFromBin
        _fromBinMethods["uvw"] = TotalPowerRow.uvwFromBin
        _fromBinMethods["exposure"] = TotalPowerRow.exposureFromBin
        _fromBinMethods["timeCentroid"] = TotalPowerRow.timeCentroidFromBin
        _fromBinMethods["floatData"] = TotalPowerRow.floatDataFromBin
        _fromBinMethods["flagAnt"] = TotalPowerRow.flagAntFromBin
        _fromBinMethods["flagPol"] = TotalPowerRow.flagPolFromBin
        _fromBinMethods["interval"] = TotalPowerRow.intervalFromBin
        _fromBinMethods["stateId"] = TotalPowerRow.stateIdFromBin
        _fromBinMethods["execBlockId"] = TotalPowerRow.execBlockIdFromBin

        _fromBinMethods["subintegrationNumber"] = (
            TotalPowerRow.subintegrationNumberFromBin
        )

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = TotalPowerRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " TotalPower",
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

    # ===> Attribute integrationNumber

    _integrationNumber = 0

    def getIntegrationNumber(self):
        """
        Get integrationNumber.
        return integrationNumber as int
        """

        return self._integrationNumber

    def setIntegrationNumber(self, integrationNumber):
        """
        Set integrationNumber with the specified int value.
        integrationNumber The int value to which integrationNumber is to be set.


        """

        self._integrationNumber = int(integrationNumber)

    # ===> Attribute uvw

    _uvw = None  # this is a 2D list of Length

    def getUvw(self):
        """
        Get uvw.
        return uvw as Length []  []
        """

        return copy.deepcopy(self._uvw)

    def setUvw(self, uvw):
        """
        Set uvw with the specified Length []  []  value.
        uvw The Length []  []  value to which uvw is to be set.
        The value of uvw can be anything allowed by the Length []  []  constructor.

        """

        # value must be a list
        if not isinstance(uvw, list):
            raise ValueError("The value of uvw must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(uvw)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of uvw is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(uvw, Length):
                raise ValueError(
                    "type of the first value in uvw is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._uvw = copy.deepcopy(uvw)
        except Exception as exc:
            raise ValueError("Invalid uvw : " + str(exc))

    # ===> Attribute exposure

    _exposure = None  # this is a 2D list of Interval

    def getExposure(self):
        """
        Get exposure.
        return exposure as Interval []  []
        """

        return copy.deepcopy(self._exposure)

    def setExposure(self, exposure):
        """
        Set exposure with the specified Interval []  []  value.
        exposure The Interval []  []  value to which exposure is to be set.
        The value of exposure can be anything allowed by the Interval []  []  constructor.

        """

        # value must be a list
        if not isinstance(exposure, list):
            raise ValueError("The value of exposure must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(exposure)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of exposure is not correct")

            # the type of the values in the list must be Interval
            # note : this only checks the first value found
            if not Parser.checkListType(exposure, Interval):
                raise ValueError(
                    "type of the first value in exposure is not Interval as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._exposure = copy.deepcopy(exposure)
        except Exception as exc:
            raise ValueError("Invalid exposure : " + str(exc))

    # ===> Attribute timeCentroid

    _timeCentroid = None  # this is a 2D list of ArrayTime

    def getTimeCentroid(self):
        """
        Get timeCentroid.
        return timeCentroid as ArrayTime []  []
        """

        return copy.deepcopy(self._timeCentroid)

    def setTimeCentroid(self, timeCentroid):
        """
        Set timeCentroid with the specified ArrayTime []  []  value.
        timeCentroid The ArrayTime []  []  value to which timeCentroid is to be set.
        The value of timeCentroid can be anything allowed by the ArrayTime []  []  constructor.

        """

        # value must be a list
        if not isinstance(timeCentroid, list):
            raise ValueError("The value of timeCentroid must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(timeCentroid)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of timeCentroid is not correct")

            # the type of the values in the list must be ArrayTime
            # note : this only checks the first value found
            if not Parser.checkListType(timeCentroid, ArrayTime):
                raise ValueError(
                    "type of the first value in timeCentroid is not ArrayTime as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._timeCentroid = copy.deepcopy(timeCentroid)
        except Exception as exc:
            raise ValueError("Invalid timeCentroid : " + str(exc))

    # ===> Attribute floatData

    _floatData = None  # this is a 2D list of float

    def getFloatData(self):
        """
        Get floatData.
        return floatData as float []  []  []
        """

        return copy.deepcopy(self._floatData)

    def setFloatData(self, floatData):
        """
        Set floatData with the specified float []  []  []  value.
        floatData The float []  []  []  value to which floatData is to be set.


        """

        # value must be a list
        if not isinstance(floatData, list):
            raise ValueError("The value of floatData must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(floatData)

            shapeOK = len(listDims) == 3

            if not shapeOK:
                raise ValueError("shape of floatData is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(floatData, float):
                raise ValueError(
                    "type of the first value in floatData is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._floatData = copy.deepcopy(floatData)
        except Exception as exc:
            raise ValueError("Invalid floatData : " + str(exc))

    # ===> Attribute flagAnt

    _flagAnt = None  # this is a 1D list of int

    def getFlagAnt(self):
        """
        Get flagAnt.
        return flagAnt as int []
        """

        return copy.deepcopy(self._flagAnt)

    def setFlagAnt(self, flagAnt):
        """
        Set flagAnt with the specified int []  value.
        flagAnt The int []  value to which flagAnt is to be set.


        """

        # value must be a list
        if not isinstance(flagAnt, list):
            raise ValueError("The value of flagAnt must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(flagAnt)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of flagAnt is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not Parser.checkListType(flagAnt, int):
                raise ValueError(
                    "type of the first value in flagAnt is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._flagAnt = copy.deepcopy(flagAnt)
        except Exception as exc:
            raise ValueError("Invalid flagAnt : " + str(exc))

    # ===> Attribute flagPol

    _flagPol = None  # this is a 2D list of int

    def getFlagPol(self):
        """
        Get flagPol.
        return flagPol as int []  []
        """

        return copy.deepcopy(self._flagPol)

    def setFlagPol(self, flagPol):
        """
        Set flagPol with the specified int []  []  value.
        flagPol The int []  []  value to which flagPol is to be set.


        """

        # value must be a list
        if not isinstance(flagPol, list):
            raise ValueError("The value of flagPol must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(flagPol)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of flagPol is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not Parser.checkListType(flagPol, int):
                raise ValueError(
                    "type of the first value in flagPol is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._flagPol = copy.deepcopy(flagPol)
        except Exception as exc:
            raise ValueError("Invalid flagPol : " + str(exc))

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

    # ===> Attribute subintegrationNumber, which is optional
    _subintegrationNumberExists = False

    _subintegrationNumber = 0

    def isSubintegrationNumberExists(self):
        """
        The attribute subintegrationNumber is optional. Return True if this attribute exists.
        return True if and only if the subintegrationNumber attribute exists.
        """
        return self._subintegrationNumberExists

    def getSubintegrationNumber(self):
        """
        Get subintegrationNumber, which is optional.
        return subintegrationNumber as int
        raises ValueError If subintegrationNumber does not exist.
        """
        if not self._subintegrationNumberExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + subintegrationNumber
                + " attribute in table TotalPower does not exist!"
            )

        return self._subintegrationNumber

    def setSubintegrationNumber(self, subintegrationNumber):
        """
        Set subintegrationNumber with the specified int value.
        subintegrationNumber The int value to which subintegrationNumber is to be set.


        """

        self._subintegrationNumber = int(subintegrationNumber)

        self._subintegrationNumberExists = True

    def clearSubintegrationNumber(self):
        """
        Mark subintegrationNumber, which is an optional field, as non-existent.
        """
        self._subintegrationNumberExists = False

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
            listDims = Parser.getListDims(stateId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of stateId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not Parser.checkListType(stateId, Tag):
                raise ValueError(
                    "type of the first value in stateId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._stateId = copy.deepcopy(stateId)
        except Exception as exc:
            raise ValueError("Invalid stateId : " + str(exc))

    # Links

    def setOneStateId(self, index, stateId):
        """
        Set stateId[index] with the specified Tag value.
        index The index in stateId where to set the Tag value.
        stateId The Tag value to which stateId[index] is to be set.

        """

        self._stateId[index] = Tag(stateId)

    # ===> hasmany link from a row of TotalPower table to many rows of State table.

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

    def getFieldUsingFieldId(self):
        """
        Returns the row in the Field table having Field.fieldId == fieldId

        """

        return self._table.getContainer().getField().getRowByKey(self._fieldId)

    def getConfigDescriptionUsingConfigDescriptionId(self):
        """
        Returns the row in the ConfigDescription table having ConfigDescription.configDescriptionId == configDescriptionId

        """

        return (
            self._table.getContainer()
            .getConfigDescription()
            .getRowByKey(self._configDescriptionId)
        )

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
        scanNumber,
        subscanNumber,
        integrationNumber,
        uvw,
        exposure,
        timeCentroid,
        floatData,
        flagAnt,
        flagPol,
        interval,
        stateId,
        execBlockId,
    ):
        """
        Compare each attribute except the autoincrementable one of this TotalPowerRow with
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

        # scanNumber is a int, compare using the == operator.
        if not (self._scanNumber == scanNumber):
            return False

        # subscanNumber is a int, compare using the == operator.
        if not (self._subscanNumber == subscanNumber):
            return False

        # integrationNumber is a int, compare using the == operator.
        if not (self._integrationNumber == integrationNumber):
            return False

        # We compare two 2D arrays (lists).
        if uvw is not None:
            if self._uvw is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            uvw_dims = Parser.getListDims(uvw)
            this_uvw_dims = Parser.getListDims(self._uvw)
            if uvw_dims != this_uvw_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(uvw_dims[0]):
                for j in range(uvw_dims[1]):

                    # uvw is a Length, compare using the almostEquals method.
                    if not (
                        self._uvw[i][j].almostEquals(
                            uvw[i][j], self.getTable().getUvwEqTolerance()
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if exposure is not None:
            if self._exposure is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            exposure_dims = Parser.getListDims(exposure)
            this_exposure_dims = Parser.getListDims(self._exposure)
            if exposure_dims != this_exposure_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(exposure_dims[0]):
                for j in range(exposure_dims[1]):

                    # exposure is an array of Interval, compare using equals method.
                    if not (self._exposure[i][j].equals(exposure[i][j])):
                        return False

        # We compare two 2D arrays (lists).
        if timeCentroid is not None:
            if self._timeCentroid is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            timeCentroid_dims = Parser.getListDims(timeCentroid)
            this_timeCentroid_dims = Parser.getListDims(self._timeCentroid)
            if timeCentroid_dims != this_timeCentroid_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(timeCentroid_dims[0]):
                for j in range(timeCentroid_dims[1]):

                    # timeCentroid is an array of ArrayTime, compare using equals method.
                    if not (self._timeCentroid[i][j].equals(timeCentroid[i][j])):
                        return False

        # We compare two 3D arrays.
        # Compare firstly their dimensions and then their values.
        if floatData is not None:
            if self._floatData is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            floatData_dims = Parser.getListDims(floatData)
            this_floatData_dims = Parser.getListDims(self._floatData)
            if floatData_dims != this_floatData_dims:
                return False
            # assumes they are both 3D arrays, the internal one should be
            for i in range(floatData_dims[0]):
                for j in range(floatData_dims[1]):
                    for k in range(floatData_dims[2]):

                        # floatData is an array of float, compare using == operator.
                        if not (self._floatData[i][j][k] == floatData[i][j][k]):
                            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._flagAnt) != len(flagAnt):
            return False
        for indx in range(len(flagAnt)):

            # flagAnt is a list of int, compare using == operator.
            if not (self._flagAnt[indx] == flagAnt[indx]):
                return False

        # We compare two 2D arrays (lists).
        if flagPol is not None:
            if self._flagPol is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            flagPol_dims = Parser.getListDims(flagPol)
            this_flagPol_dims = Parser.getListDims(self._flagPol)
            if flagPol_dims != this_flagPol_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(flagPol_dims[0]):
                for j in range(flagPol_dims[1]):

                    # flagPol is an array of int, compare using == operator.
                    if not (self._flagPol[i][j] == flagPol[i][j]):
                        return False

        # interval is a Interval, compare using the equals method.
        if not self._interval.equals(interval):
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
            otherRow.getScanNumber(),
            otherRow.getSubscanNumber(),
            otherRow.getIntegrationNumber(),
            otherRow.getUvw(),
            otherRow.getExposure(),
            otherRow.getTimeCentroid(),
            otherRow.getFloatData(),
            otherRow.getFlagAnt(),
            otherRow.getFlagPol(),
            otherRow.getInterval(),
            otherRow.getStateId(),
            otherRow.getExecBlockId(),
        )

    def compareRequiredValue(
        self,
        scanNumber,
        subscanNumber,
        integrationNumber,
        uvw,
        exposure,
        timeCentroid,
        floatData,
        flagAnt,
        flagPol,
        interval,
        stateId,
        execBlockId,
    ):

        # scanNumber is a int, compare using the == operator.
        if not (self._scanNumber == scanNumber):
            return False

        # subscanNumber is a int, compare using the == operator.
        if not (self._subscanNumber == subscanNumber):
            return False

        # integrationNumber is a int, compare using the == operator.
        if not (self._integrationNumber == integrationNumber):
            return False

        # We compare two 2D arrays (lists).
        if uvw is not None:
            if self._uvw is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            uvw_dims = Parser.getListDims(uvw)
            this_uvw_dims = Parser.getListDims(self._uvw)
            if uvw_dims != this_uvw_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(uvw_dims[0]):
                for j in range(uvw_dims[1]):

                    # uvw is a Length, compare using the almostEquals method.
                    if not (
                        self._uvw[i][j].almostEquals(
                            uvw[i][j], self.getTable().getUvwEqTolerance()
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if exposure is not None:
            if self._exposure is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            exposure_dims = Parser.getListDims(exposure)
            this_exposure_dims = Parser.getListDims(self._exposure)
            if exposure_dims != this_exposure_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(exposure_dims[0]):
                for j in range(exposure_dims[1]):

                    # exposure is an array of Interval, compare using equals method.
                    if not (self._exposure[i][j].equals(exposure[i][j])):
                        return False

        # We compare two 2D arrays (lists).
        if timeCentroid is not None:
            if self._timeCentroid is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            timeCentroid_dims = Parser.getListDims(timeCentroid)
            this_timeCentroid_dims = Parser.getListDims(self._timeCentroid)
            if timeCentroid_dims != this_timeCentroid_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(timeCentroid_dims[0]):
                for j in range(timeCentroid_dims[1]):

                    # timeCentroid is an array of ArrayTime, compare using equals method.
                    if not (self._timeCentroid[i][j].equals(timeCentroid[i][j])):
                        return False

        # We compare two 3D arrays.
        # Compare firstly their dimensions and then their values.
        if floatData is not None:
            if self._floatData is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            floatData_dims = Parser.getListDims(floatData)
            this_floatData_dims = Parser.getListDims(self._floatData)
            if floatData_dims != this_floatData_dims:
                return False
            # assumes they are both 3D arrays, the internal one should be
            for i in range(floatData_dims[0]):
                for j in range(floatData_dims[1]):
                    for k in range(floatData_dims[2]):

                        # floatData is an array of float, compare using == operator.
                        if not (self._floatData[i][j][k] == floatData[i][j][k]):
                            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._flagAnt) != len(flagAnt):
            return False
        for indx in range(len(flagAnt)):

            # flagAnt is a list of int, compare using == operator.
            if not (self._flagAnt[indx] == flagAnt[indx]):
                return False

        # We compare two 2D arrays (lists).
        if flagPol is not None:
            if self._flagPol is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            flagPol_dims = Parser.getListDims(flagPol)
            this_flagPol_dims = Parser.getListDims(self._flagPol)
            if flagPol_dims != this_flagPol_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(flagPol_dims[0]):
                for j in range(flagPol_dims[1]):

                    # flagPol is an array of int, compare using == operator.
                    if not (self._flagPol[i][j] == flagPol[i][j]):
                        return False

        # interval is a Interval, compare using the equals method.
        if not self._interval.equals(interval):
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
TotalPowerRow.initFromBinMethods()
