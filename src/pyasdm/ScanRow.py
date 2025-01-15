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
# File ScanRow.py
#

import pyasdm.ScanTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.ScanIntent import ScanIntent


from pyasdm.enumerations.CalDataOrigin import CalDataOrigin


from pyasdm.enumerations.CalibrationFunction import CalibrationFunction


from pyasdm.enumerations.CalibrationSet import CalibrationSet


from pyasdm.enumerations.AntennaMotionPattern import AntennaMotionPattern


from xml.dom import minidom

import copy


class ScanRow:
    """
    The ScanRow class is a row of a ScanTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a ScanRow.
        When row is None, create an empty row attached to table, which must be a ScanTable.
        When row is given, copy those values in to the new row. The row argument must be a ScanRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.ScanTable):
            raise ValueError("table must be a ScanTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._scanNumber = 0

        self._startTime = ArrayTime()

        self._endTime = ArrayTime()

        self._numIntent = 0

        self._numSubscan = 0

        self._scanIntent = []  # this is a list of ScanIntent []

        self._calDataType = []  # this is a list of CalDataOrigin []

        self._calibrationOnLine = []  # this is a list of bool []

        self._calibrationFunctionExists = False

        self._calibrationFunction = []  # this is a list of CalibrationFunction []

        self._calibrationSetExists = False

        self._calibrationSet = []  # this is a list of CalibrationSet []

        self._calPatternExists = False

        self._calPattern = []  # this is a list of AntennaMotionPattern []

        self._numFieldExists = False

        self._numField = 0

        self._fieldNameExists = False

        self._fieldName = []  # this is a list of str []

        self._sourceNameExists = False

        self._sourceName = None

        # extrinsic attributes

        self._execBlockId = Tag()

        if row is not None:
            if not isinstance(row, ScanRow):
                raise ValueError("row must be a ScanRow")

            # copy constructor

            self._execBlockId = Tag(row._execBlockId)

            self._scanNumber = row._scanNumber

            self._startTime = ArrayTime(row._startTime)

            self._endTime = ArrayTime(row._endTime)

            self._numIntent = row._numIntent

            self._numSubscan = row._numSubscan

            # scanIntent is a  list , make a deep copy
            self._scanIntent = copy.deepcopy(row._scanIntent)

            # calDataType is a  list , make a deep copy
            self._calDataType = copy.deepcopy(row._calDataType)

            # calibrationOnLine is a  list , make a deep copy
            self._calibrationOnLine = copy.deepcopy(row._calibrationOnLine)

            # by default set systematically calibrationFunction's value to something not None

            if row._calibrationFunctionExists:

                # calibrationFunction is a list, make a deep copy
                self.calibrationFunction = copy.deepcopy(row.calibrationFunction)

                self._calibrationFunctionExists = True

            # by default set systematically calibrationSet's value to something not None

            if row._calibrationSetExists:

                # calibrationSet is a list, make a deep copy
                self.calibrationSet = copy.deepcopy(row.calibrationSet)

                self._calibrationSetExists = True

            # by default set systematically calPattern's value to something not None

            if row._calPatternExists:

                # calPattern is a list, make a deep copy
                self.calPattern = copy.deepcopy(row.calPattern)

                self._calPatternExists = True

            # by default set systematically numField's value to something not None

            if row._numFieldExists:

                self._numField = row._numField

                self._numFieldExists = True

            # by default set systematically fieldName's value to something not None

            if row._fieldNameExists:

                # fieldName is a list, make a deep copy
                self.fieldName = copy.deepcopy(row.fieldName)

                self._fieldNameExists = True

            # by default set systematically sourceName's value to something not None

            if row._sourceNameExists:

                self._sourceName = row._sourceName

                self._sourceNameExists = True

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

        result += Parser.valueToXML("scanNumber", self._scanNumber)

        result += Parser.extendedValueToXML("startTime", self._startTime)

        result += Parser.extendedValueToXML("endTime", self._endTime)

        result += Parser.valueToXML("numIntent", self._numIntent)

        result += Parser.valueToXML("numSubscan", self._numSubscan)

        result += Parser.listEnumValueToXML("scanIntent", self._scanIntent)

        result += Parser.listEnumValueToXML("calDataType", self._calDataType)

        result += Parser.listValueToXML("calibrationOnLine", self._calibrationOnLine)

        if self._calibrationFunctionExists:

            result += Parser.listEnumValueToXML(
                "calibrationFunction", self._calibrationFunction
            )

        if self._calibrationSetExists:

            result += Parser.listEnumValueToXML("calibrationSet", self._calibrationSet)

        if self._calPatternExists:

            result += Parser.listEnumValueToXML("calPattern", self._calPattern)

        if self._numFieldExists:

            result += Parser.valueToXML("numField", self._numField)

        if self._fieldNameExists:

            result += Parser.listValueToXML("fieldName", self._fieldName)

        if self._sourceNameExists:

            result += Parser.valueToXML("sourceName", self._sourceName)

        # extrinsic attributes

        result += Parser.extendedValueToXML("execBlockId", self._execBlockId)

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
                "xmlrow is not a string or a minidom.Element", "ScanTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "ScanTable")

        # intrinsic attribute values

        scanNumberNode = rowdom.getElementsByTagName("scanNumber")[0]

        self._scanNumber = int(scanNumberNode.firstChild.data.strip())

        startTimeNode = rowdom.getElementsByTagName("startTime")[0]

        self._startTime = ArrayTime(startTimeNode.firstChild.data.strip())

        endTimeNode = rowdom.getElementsByTagName("endTime")[0]

        self._endTime = ArrayTime(endTimeNode.firstChild.data.strip())

        numIntentNode = rowdom.getElementsByTagName("numIntent")[0]

        self._numIntent = int(numIntentNode.firstChild.data.strip())

        numSubscanNode = rowdom.getElementsByTagName("numSubscan")[0]

        self._numSubscan = int(numSubscanNode.firstChild.data.strip())

        scanIntentNode = rowdom.getElementsByTagName("scanIntent")[0]

        scanIntentStr = scanIntentNode.firstChild.data.strip()
        self._scanIntent = Parser.stringListToLists(
            scanIntentStr, ScanIntent, "Scan", False
        )

        calDataTypeNode = rowdom.getElementsByTagName("calDataType")[0]

        calDataTypeStr = calDataTypeNode.firstChild.data.strip()
        self._calDataType = Parser.stringListToLists(
            calDataTypeStr, CalDataOrigin, "Scan", False
        )

        calibrationOnLineNode = rowdom.getElementsByTagName("calibrationOnLine")[0]

        calibrationOnLineStr = calibrationOnLineNode.firstChild.data.strip()

        self._calibrationOnLine = Parser.stringListToLists(
            calibrationOnLineStr, bool, "Scan", False
        )

        calibrationFunctionNode = rowdom.getElementsByTagName("calibrationFunction")
        if len(calibrationFunctionNode) > 0:

            calibrationFunctionStr = calibrationFunctionNode[0].firstChild.data.strip()
            self._calibrationFunction = Parser.stringListToLists(
                calibrationFunctionStr, CalibrationFunction, "Scan", False
            )

            self._calibrationFunctionExists = True

        calibrationSetNode = rowdom.getElementsByTagName("calibrationSet")
        if len(calibrationSetNode) > 0:

            calibrationSetStr = calibrationSetNode[0].firstChild.data.strip()
            self._calibrationSet = Parser.stringListToLists(
                calibrationSetStr, CalibrationSet, "Scan", False
            )

            self._calibrationSetExists = True

        calPatternNode = rowdom.getElementsByTagName("calPattern")
        if len(calPatternNode) > 0:

            calPatternStr = calPatternNode[0].firstChild.data.strip()
            self._calPattern = Parser.stringListToLists(
                calPatternStr, AntennaMotionPattern, "Scan", False
            )

            self._calPatternExists = True

        numFieldNode = rowdom.getElementsByTagName("numField")
        if len(numFieldNode) > 0:

            self._numField = int(numFieldNode[0].firstChild.data.strip())

            self._numFieldExists = True

        fieldNameNode = rowdom.getElementsByTagName("fieldName")
        if len(fieldNameNode) > 0:

            fieldNameStr = fieldNameNode[0].firstChild.data.strip()

            self._fieldName = Parser.stringListToLists(fieldNameStr, str, "Scan", False)

            self._fieldNameExists = True

        sourceNameNode = rowdom.getElementsByTagName("sourceName")
        if len(sourceNameNode) > 0:

            self._sourceName = str(sourceNameNode[0].firstChild.data.strip())

            self._sourceNameExists = True

        # extrinsic attribute values

        execBlockIdNode = rowdom.getElementsByTagName("execBlockId")[0]

        self._execBlockId = Tag(execBlockIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._execBlockId.toBin(eos)

        eos.writeInt(self._scanNumber)

        self._startTime.toBin(eos)

        self._endTime.toBin(eos)

        eos.writeInt(self._numIntent)

        eos.writeInt(self._numSubscan)

        eos.writeInt(len(self._scanIntent))
        for i in range(len(self._scanIntent)):

            eos.writeString(self._scanIntent[i].toString())

        eos.writeInt(len(self._calDataType))
        for i in range(len(self._calDataType)):

            eos.writeString(self._calDataType[i].toString())

        eos.writeInt(len(self._calibrationOnLine))
        for i in range(len(self._calibrationOnLine)):

            eos.writeBool(self._calibrationOnLine[i])

        eos.writeBool(self._calibrationFunctionExists)
        if self._calibrationFunctionExists:

            eos.writeInt(len(self._calibrationFunction))
            for i in range(len(self._calibrationFunction)):

                eos.writeString(self._calibrationFunction[i].toString())

        eos.writeBool(self._calibrationSetExists)
        if self._calibrationSetExists:

            eos.writeInt(len(self._calibrationSet))
            for i in range(len(self._calibrationSet)):

                eos.writeString(self._calibrationSet[i].toString())

        eos.writeBool(self._calPatternExists)
        if self._calPatternExists:

            eos.writeInt(len(self._calPattern))
            for i in range(len(self._calPattern)):

                eos.writeString(self._calPattern[i].toString())

        eos.writeBool(self._numFieldExists)
        if self._numFieldExists:

            eos.writeInt(self._numField)

        eos.writeBool(self._fieldNameExists)
        if self._fieldNameExists:

            eos.writeInt(len(self._fieldName))
            for i in range(len(self._fieldName)):

                eos.writeStr(self._fieldName[i])

        eos.writeBool(self._sourceNameExists)
        if self._sourceNameExists:

            eos.writeStr(self._sourceName)

    @staticmethod
    def execBlockIdFromBin(row, eis):
        """
        Set the execBlockId in row from the EndianInput (eis) instance.
        """

        row._execBlockId = Tag.fromBin(eis)

    @staticmethod
    def scanNumberFromBin(row, eis):
        """
        Set the scanNumber in row from the EndianInput (eis) instance.
        """

        row._scanNumber = eis.readInt()

    @staticmethod
    def startTimeFromBin(row, eis):
        """
        Set the startTime in row from the EndianInput (eis) instance.
        """

        row._startTime = ArrayTime.fromBin(eis)

    @staticmethod
    def endTimeFromBin(row, eis):
        """
        Set the endTime in row from the EndianInput (eis) instance.
        """

        row._endTime = ArrayTime.fromBin(eis)

    @staticmethod
    def numIntentFromBin(row, eis):
        """
        Set the numIntent in row from the EndianInput (eis) instance.
        """

        row._numIntent = eis.readInt()

    @staticmethod
    def numSubscanFromBin(row, eis):
        """
        Set the numSubscan in row from the EndianInput (eis) instance.
        """

        row._numSubscan = eis.readInt()

    @staticmethod
    def scanIntentFromBin(row, eis):
        """
        Set the scanIntent in row from the EndianInput (eis) instance.
        """

        scanIntentDim1 = eis.readInt()
        thisList = []
        for i in range(scanIntentDim1):
            thisValue = ScanIntent.from_int(eis.readInt())
            thisList.append(thisValue)
        row._scanIntent = thisList

    @staticmethod
    def calDataTypeFromBin(row, eis):
        """
        Set the calDataType in row from the EndianInput (eis) instance.
        """

        calDataTypeDim1 = eis.readInt()
        thisList = []
        for i in range(calDataTypeDim1):
            thisValue = CalDataOrigin.from_int(eis.readInt())
            thisList.append(thisValue)
        row._calDataType = thisList

    @staticmethod
    def calibrationOnLineFromBin(row, eis):
        """
        Set the calibrationOnLine in row from the EndianInput (eis) instance.
        """

        calibrationOnLineDim1 = eis.readInt()
        thisList = []
        for i in range(calibrationOnLineDim1):
            thisValue = eis.readBool()
            thisList.append(thisValue)
        row._calibrationOnLine = thisList

    @staticmethod
    def calibrationFunctionFromBin(row, eis):
        """
        Set the optional calibrationFunction in row from the EndianInput (eis) instance.
        """
        row._calibrationFunctionExists = eis.readBool()
        if row._calibrationFunctionExists:

            calibrationFunctionDim1 = eis.readInt()
            thisList = []
            for i in range(calibrationFunctionDim1):
                thisValue = CalibrationFunction.from_int(eis.readInt())
                thisList.append(thisValue)
            row._calibrationFunction = thisList

    @staticmethod
    def calibrationSetFromBin(row, eis):
        """
        Set the optional calibrationSet in row from the EndianInput (eis) instance.
        """
        row._calibrationSetExists = eis.readBool()
        if row._calibrationSetExists:

            calibrationSetDim1 = eis.readInt()
            thisList = []
            for i in range(calibrationSetDim1):
                thisValue = CalibrationSet.from_int(eis.readInt())
                thisList.append(thisValue)
            row._calibrationSet = thisList

    @staticmethod
    def calPatternFromBin(row, eis):
        """
        Set the optional calPattern in row from the EndianInput (eis) instance.
        """
        row._calPatternExists = eis.readBool()
        if row._calPatternExists:

            calPatternDim1 = eis.readInt()
            thisList = []
            for i in range(calPatternDim1):
                thisValue = AntennaMotionPattern.from_int(eis.readInt())
                thisList.append(thisValue)
            row._calPattern = thisList

    @staticmethod
    def numFieldFromBin(row, eis):
        """
        Set the optional numField in row from the EndianInput (eis) instance.
        """
        row._numFieldExists = eis.readBool()
        if row._numFieldExists:

            row._numField = eis.readInt()

    @staticmethod
    def fieldNameFromBin(row, eis):
        """
        Set the optional fieldName in row from the EndianInput (eis) instance.
        """
        row._fieldNameExists = eis.readBool()
        if row._fieldNameExists:

            fieldNameDim1 = eis.readInt()
            thisList = []
            for i in range(fieldNameDim1):
                thisValue = eis.readStr()
                thisList.append(thisValue)
            row._fieldName = thisList

    @staticmethod
    def sourceNameFromBin(row, eis):
        """
        Set the optional sourceName in row from the EndianInput (eis) instance.
        """
        row._sourceNameExists = eis.readBool()
        if row._sourceNameExists:

            row._sourceName = eis.readStr()

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["execBlockId"] = ScanRow.execBlockIdFromBin
        _fromBinMethods["scanNumber"] = ScanRow.scanNumberFromBin
        _fromBinMethods["startTime"] = ScanRow.startTimeFromBin
        _fromBinMethods["endTime"] = ScanRow.endTimeFromBin
        _fromBinMethods["numIntent"] = ScanRow.numIntentFromBin
        _fromBinMethods["numSubscan"] = ScanRow.numSubscanFromBin
        _fromBinMethods["scanIntent"] = ScanRow.scanIntentFromBin
        _fromBinMethods["calDataType"] = ScanRow.calDataTypeFromBin
        _fromBinMethods["calibrationOnLine"] = ScanRow.calibrationOnLineFromBin

        _fromBinMethods["calibrationFunction"] = ScanRow.calibrationFunctionFromBin
        _fromBinMethods["calibrationSet"] = ScanRow.calibrationSetFromBin
        _fromBinMethods["calPattern"] = ScanRow.calPatternFromBin
        _fromBinMethods["numField"] = ScanRow.numFieldFromBin
        _fromBinMethods["fieldName"] = ScanRow.fieldNameFromBin
        _fromBinMethods["sourceName"] = ScanRow.sourceNameFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = ScanRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Scan",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

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


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the scanNumber field, which is part of the key, after this row has been added to this table."
            )

        self._scanNumber = int(scanNumber)

    # ===> Attribute startTime

    _startTime = ArrayTime()

    def getStartTime(self):
        """
        Get startTime.
        return startTime as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._startTime)

    def setStartTime(self, startTime):
        """
        Set startTime with the specified ArrayTime value.
        startTime The ArrayTime value to which startTime is to be set.
        The value of startTime can be anything allowed by the ArrayTime constructor.

        """

        self._startTime = ArrayTime(startTime)

    # ===> Attribute endTime

    _endTime = ArrayTime()

    def getEndTime(self):
        """
        Get endTime.
        return endTime as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._endTime)

    def setEndTime(self, endTime):
        """
        Set endTime with the specified ArrayTime value.
        endTime The ArrayTime value to which endTime is to be set.
        The value of endTime can be anything allowed by the ArrayTime constructor.

        """

        self._endTime = ArrayTime(endTime)

    # ===> Attribute numIntent

    _numIntent = 0

    def getNumIntent(self):
        """
        Get numIntent.
        return numIntent as int
        """

        return self._numIntent

    def setNumIntent(self, numIntent):
        """
        Set numIntent with the specified int value.
        numIntent The int value to which numIntent is to be set.


        """

        self._numIntent = int(numIntent)

    # ===> Attribute numSubscan

    _numSubscan = 0

    def getNumSubscan(self):
        """
        Get numSubscan.
        return numSubscan as int
        """

        return self._numSubscan

    def setNumSubscan(self, numSubscan):
        """
        Set numSubscan with the specified int value.
        numSubscan The int value to which numSubscan is to be set.


        """

        self._numSubscan = int(numSubscan)

    # ===> Attribute scanIntent

    _scanIntent = None  # this is a 1D list of ScanIntent

    def getScanIntent(self):
        """
        Get scanIntent.
        return scanIntent as ScanIntent []
        """

        return copy.deepcopy(self._scanIntent)

    def setScanIntent(self, scanIntent):
        """
        Set scanIntent with the specified ScanIntent []  value.
        scanIntent The ScanIntent []  value to which scanIntent is to be set.


        """

        # value must be a list
        if not isinstance(scanIntent, list):
            raise ValueError("The value of scanIntent must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(scanIntent)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of scanIntent is not correct")

            # the type of the values in the list must be ScanIntent
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(scanIntent, ScanIntent):
                raise ValueError(
                    "type of the first value in scanIntent is not ScanIntent as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._scanIntent = copy.deepcopy(scanIntent)
        except Exception as exc:
            raise ValueError("Invalid scanIntent : " + str(exc))

    # ===> Attribute calDataType

    _calDataType = None  # this is a 1D list of CalDataOrigin

    def getCalDataType(self):
        """
        Get calDataType.
        return calDataType as CalDataOrigin []
        """

        return copy.deepcopy(self._calDataType)

    def setCalDataType(self, calDataType):
        """
        Set calDataType with the specified CalDataOrigin []  value.
        calDataType The CalDataOrigin []  value to which calDataType is to be set.


        """

        # value must be a list
        if not isinstance(calDataType, list):
            raise ValueError("The value of calDataType must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(calDataType)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of calDataType is not correct")

            # the type of the values in the list must be CalDataOrigin
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(calDataType, CalDataOrigin):
                raise ValueError(
                    "type of the first value in calDataType is not CalDataOrigin as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._calDataType = copy.deepcopy(calDataType)
        except Exception as exc:
            raise ValueError("Invalid calDataType : " + str(exc))

    # ===> Attribute calibrationOnLine

    _calibrationOnLine = None  # this is a 1D list of bool

    def getCalibrationOnLine(self):
        """
        Get calibrationOnLine.
        return calibrationOnLine as bool []
        """

        return copy.deepcopy(self._calibrationOnLine)

    def setCalibrationOnLine(self, calibrationOnLine):
        """
        Set calibrationOnLine with the specified bool []  value.
        calibrationOnLine The bool []  value to which calibrationOnLine is to be set.


        """

        # value must be a list
        if not isinstance(calibrationOnLine, list):
            raise ValueError("The value of calibrationOnLine must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(calibrationOnLine)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of calibrationOnLine is not correct")

            # the type of the values in the list must be bool
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(calibrationOnLine, bool):
                raise ValueError(
                    "type of the first value in calibrationOnLine is not bool as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._calibrationOnLine = copy.deepcopy(calibrationOnLine)
        except Exception as exc:
            raise ValueError("Invalid calibrationOnLine : " + str(exc))

    # ===> Attribute calibrationFunction, which is optional
    _calibrationFunctionExists = False

    _calibrationFunction = None  # this is a 1D list of CalibrationFunction

    def isCalibrationFunctionExists(self):
        """
        The attribute calibrationFunction is optional. Return True if this attribute exists.
        return True if and only if the calibrationFunction attribute exists.
        """
        return self._calibrationFunctionExists

    def getCalibrationFunction(self):
        """
        Get calibrationFunction, which is optional.
        return calibrationFunction as CalibrationFunction []
        raises ValueError If calibrationFunction does not exist.
        """
        if not self._calibrationFunctionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + calibrationFunction
                + " attribute in table Scan does not exist!"
            )

        return copy.deepcopy(self._calibrationFunction)

    def setCalibrationFunction(self, calibrationFunction):
        """
        Set calibrationFunction with the specified CalibrationFunction []  value.
        calibrationFunction The CalibrationFunction []  value to which calibrationFunction is to be set.


        """

        # value must be a list
        if not isinstance(calibrationFunction, list):
            raise ValueError("The value of calibrationFunction must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(calibrationFunction)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of calibrationFunction is not correct")

            # the type of the values in the list must be CalibrationFunction
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(calibrationFunction, CalibrationFunction):
                raise ValueError(
                    "type of the first value in calibrationFunction is not CalibrationFunction as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._calibrationFunction = copy.deepcopy(calibrationFunction)
        except Exception as exc:
            raise ValueError("Invalid calibrationFunction : " + str(exc))

        self._calibrationFunctionExists = True

    def clearCalibrationFunction(self):
        """
        Mark calibrationFunction, which is an optional field, as non-existent.
        """
        self._calibrationFunctionExists = False

    # ===> Attribute calibrationSet, which is optional
    _calibrationSetExists = False

    _calibrationSet = None  # this is a 1D list of CalibrationSet

    def isCalibrationSetExists(self):
        """
        The attribute calibrationSet is optional. Return True if this attribute exists.
        return True if and only if the calibrationSet attribute exists.
        """
        return self._calibrationSetExists

    def getCalibrationSet(self):
        """
        Get calibrationSet, which is optional.
        return calibrationSet as CalibrationSet []
        raises ValueError If calibrationSet does not exist.
        """
        if not self._calibrationSetExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + calibrationSet
                + " attribute in table Scan does not exist!"
            )

        return copy.deepcopy(self._calibrationSet)

    def setCalibrationSet(self, calibrationSet):
        """
        Set calibrationSet with the specified CalibrationSet []  value.
        calibrationSet The CalibrationSet []  value to which calibrationSet is to be set.


        """

        # value must be a list
        if not isinstance(calibrationSet, list):
            raise ValueError("The value of calibrationSet must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(calibrationSet)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of calibrationSet is not correct")

            # the type of the values in the list must be CalibrationSet
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(calibrationSet, CalibrationSet):
                raise ValueError(
                    "type of the first value in calibrationSet is not CalibrationSet as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._calibrationSet = copy.deepcopy(calibrationSet)
        except Exception as exc:
            raise ValueError("Invalid calibrationSet : " + str(exc))

        self._calibrationSetExists = True

    def clearCalibrationSet(self):
        """
        Mark calibrationSet, which is an optional field, as non-existent.
        """
        self._calibrationSetExists = False

    # ===> Attribute calPattern, which is optional
    _calPatternExists = False

    _calPattern = None  # this is a 1D list of AntennaMotionPattern

    def isCalPatternExists(self):
        """
        The attribute calPattern is optional. Return True if this attribute exists.
        return True if and only if the calPattern attribute exists.
        """
        return self._calPatternExists

    def getCalPattern(self):
        """
        Get calPattern, which is optional.
        return calPattern as AntennaMotionPattern []
        raises ValueError If calPattern does not exist.
        """
        if not self._calPatternExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + calPattern
                + " attribute in table Scan does not exist!"
            )

        return copy.deepcopy(self._calPattern)

    def setCalPattern(self, calPattern):
        """
        Set calPattern with the specified AntennaMotionPattern []  value.
        calPattern The AntennaMotionPattern []  value to which calPattern is to be set.


        """

        # value must be a list
        if not isinstance(calPattern, list):
            raise ValueError("The value of calPattern must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(calPattern)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of calPattern is not correct")

            # the type of the values in the list must be AntennaMotionPattern
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(calPattern, AntennaMotionPattern):
                raise ValueError(
                    "type of the first value in calPattern is not AntennaMotionPattern as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._calPattern = copy.deepcopy(calPattern)
        except Exception as exc:
            raise ValueError("Invalid calPattern : " + str(exc))

        self._calPatternExists = True

    def clearCalPattern(self):
        """
        Mark calPattern, which is an optional field, as non-existent.
        """
        self._calPatternExists = False

    # ===> Attribute numField, which is optional
    _numFieldExists = False

    _numField = 0

    def isNumFieldExists(self):
        """
        The attribute numField is optional. Return True if this attribute exists.
        return True if and only if the numField attribute exists.
        """
        return self._numFieldExists

    def getNumField(self):
        """
        Get numField, which is optional.
        return numField as int
        raises ValueError If numField does not exist.
        """
        if not self._numFieldExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numField
                + " attribute in table Scan does not exist!"
            )

        return self._numField

    def setNumField(self, numField):
        """
        Set numField with the specified int value.
        numField The int value to which numField is to be set.


        """

        self._numField = int(numField)

        self._numFieldExists = True

    def clearNumField(self):
        """
        Mark numField, which is an optional field, as non-existent.
        """
        self._numFieldExists = False

    # ===> Attribute fieldName, which is optional
    _fieldNameExists = False

    _fieldName = None  # this is a 1D list of str

    def isFieldNameExists(self):
        """
        The attribute fieldName is optional. Return True if this attribute exists.
        return True if and only if the fieldName attribute exists.
        """
        return self._fieldNameExists

    def getFieldName(self):
        """
        Get fieldName, which is optional.
        return fieldName as str []
        raises ValueError If fieldName does not exist.
        """
        if not self._fieldNameExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + fieldName
                + " attribute in table Scan does not exist!"
            )

        return copy.deepcopy(self._fieldName)

    def setFieldName(self, fieldName):
        """
        Set fieldName with the specified str []  value.
        fieldName The str []  value to which fieldName is to be set.


        """

        # value must be a list
        if not isinstance(fieldName, list):
            raise ValueError("The value of fieldName must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(fieldName)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of fieldName is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(fieldName, str):
                raise ValueError(
                    "type of the first value in fieldName is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._fieldName = copy.deepcopy(fieldName)
        except Exception as exc:
            raise ValueError("Invalid fieldName : " + str(exc))

        self._fieldNameExists = True

    def clearFieldName(self):
        """
        Mark fieldName, which is an optional field, as non-existent.
        """
        self._fieldNameExists = False

    # ===> Attribute sourceName, which is optional
    _sourceNameExists = False

    _sourceName = None

    def isSourceNameExists(self):
        """
        The attribute sourceName is optional. Return True if this attribute exists.
        return True if and only if the sourceName attribute exists.
        """
        return self._sourceNameExists

    def getSourceName(self):
        """
        Get sourceName, which is optional.
        return sourceName as str
        raises ValueError If sourceName does not exist.
        """
        if not self._sourceNameExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sourceName
                + " attribute in table Scan does not exist!"
            )

        return self._sourceName

    def setSourceName(self, sourceName):
        """
        Set sourceName with the specified str value.
        sourceName The str value to which sourceName is to be set.


        """

        self._sourceName = str(sourceName)

        self._sourceNameExists = True

    def clearSourceName(self):
        """
        Mark sourceName, which is an optional field, as non-existent.
        """
        self._sourceNameExists = False

    # Extrinsic Table Attributes

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

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the execBlockId field, which is part of the key, after this row has been added to this table."
            )

        self._execBlockId = Tag(execBlockId)

    # Links

    def getExecBlockUsingExecBlockId(self):
        """
        Returns the row in the ExecBlock table having ExecBlock.execBlockId == execBlockId

        """

        return self._table.getContainer().getExecBlock().getRowByKey(self._execBlockId)

    # comparison methods

    def compareNoAutoInc(
        self,
        execBlockId,
        scanNumber,
        startTime,
        endTime,
        numIntent,
        numSubscan,
        scanIntent,
        calDataType,
        calibrationOnLine,
    ):
        """
        Compare each attribute except the autoincrementable one of this ScanRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # execBlockId is a Tag, compare using the equals method.
        if not self._execBlockId.equals(execBlockId):
            return False

        # scanNumber is a int, compare using the == operator.
        if not (self._scanNumber == scanNumber):
            return False

        # startTime is a ArrayTime, compare using the equals method.
        if not self._startTime.equals(startTime):
            return False

        # endTime is a ArrayTime, compare using the equals method.
        if not self._endTime.equals(endTime):
            return False

        # numIntent is a int, compare using the == operator.
        if not (self._numIntent == numIntent):
            return False

        # numSubscan is a int, compare using the == operator.
        if not (self._numSubscan == numSubscan):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._scanIntent) != len(scanIntent):
            return False
        for indx in range(len(scanIntent)):

            # scanIntent is a list of ScanIntent, compare using == operator.
            if not (self._scanIntent[indx] == scanIntent[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._calDataType) != len(calDataType):
            return False
        for indx in range(len(calDataType)):

            # calDataType is a list of CalDataOrigin, compare using == operator.
            if not (self._calDataType[indx] == calDataType[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._calibrationOnLine) != len(calibrationOnLine):
            return False
        for indx in range(len(calibrationOnLine)):

            # calibrationOnLine is a list of bool, compare using == operator.
            if not (self._calibrationOnLine[indx] == calibrationOnLine[indx]):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getStartTime(),
            otherRow.getEndTime(),
            otherRow.getNumIntent(),
            otherRow.getNumSubscan(),
            otherRow.getScanIntent(),
            otherRow.getCalDataType(),
            otherRow.getCalibrationOnLine(),
        )

    def compareRequiredValue(
        self,
        startTime,
        endTime,
        numIntent,
        numSubscan,
        scanIntent,
        calDataType,
        calibrationOnLine,
    ):

        # startTime is a ArrayTime, compare using the equals method.
        if not self._startTime.equals(startTime):
            return False

        # endTime is a ArrayTime, compare using the equals method.
        if not self._endTime.equals(endTime):
            return False

        # numIntent is a int, compare using the == operator.
        if not (self._numIntent == numIntent):
            return False

        # numSubscan is a int, compare using the == operator.
        if not (self._numSubscan == numSubscan):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._scanIntent) != len(scanIntent):
            return False
        for indx in range(len(scanIntent)):

            # scanIntent is a list of ScanIntent, compare using == operator.
            if not (self._scanIntent[indx] == scanIntent[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._calDataType) != len(calDataType):
            return False
        for indx in range(len(calDataType)):

            # calDataType is a list of CalDataOrigin, compare using == operator.
            if not (self._calDataType[indx] == calDataType[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._calibrationOnLine) != len(calibrationOnLine):
            return False
        for indx in range(len(calibrationOnLine)):

            # calibrationOnLine is a list of bool, compare using == operator.
            if not (self._calibrationOnLine[indx] == calibrationOnLine[indx]):
                return False

        return True


# initialize the dictionary that maps fields to init methods
ScanRow.initFromBinMethods()
