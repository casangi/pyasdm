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
# File SubscanRow.py
#

import pyasdm.SubscanTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.SubscanIntent import SubscanIntent


from pyasdm.enumerations.SwitchingMode import SwitchingMode


from pyasdm.enumerations.CorrelatorCalibration import CorrelatorCalibration


from xml.dom import minidom

import copy


class SubscanRow:
    """
    The SubscanRow class is a row of a SubscanTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a SubscanRow.
        When row is None, create an empty row attached to table, which must be a SubscanTable.
        When row is given, copy those values in to the new row. The row argument must be a SubscanRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.SubscanTable):
            raise ValueError("table must be a SubscanTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._scanNumber = 0

        self._subscanNumber = 0

        self._startTime = ArrayTime()

        self._endTime = ArrayTime()

        self._fieldName = None

        self._subscanIntent = SubscanIntent.from_int(0)

        self._subscanModeExists = False

        self._subscanMode = SwitchingMode.from_int(0)

        self._numIntegration = 0

        self._numSubintegration = []  # this is a list of int []

        self._correlatorCalibrationExists = False

        self._correlatorCalibration = CorrelatorCalibration.from_int(0)

        # extrinsic attributes

        self._execBlockId = Tag()

        if row is not None:
            if not isinstance(row, SubscanRow):
                raise ValueError("row must be a SubscanRow")

            # copy constructor

            self._execBlockId = Tag(row._execBlockId)

            self._scanNumber = row._scanNumber

            self._subscanNumber = row._subscanNumber

            self._startTime = ArrayTime(row._startTime)

            self._endTime = ArrayTime(row._endTime)

            self._fieldName = row._fieldName

            # We force the attribute of the result to be not None
            if row._subscanIntent is None:
                self._subscanIntent = SubscanIntent.from_int(0)
            else:
                self._subscanIntent = SubscanIntent(row._subscanIntent)

            self._numIntegration = row._numIntegration

            # numSubintegration is a  list , make a deep copy
            self._numSubintegration = copy.deepcopy(row._numSubintegration)

            # by default set systematically subscanMode's value to something not None

            self._subscanMode = SwitchingMode.from_int(0)

            if row._subscanModeExists:

                if row._subscanMode is not None:
                    self._subscanMode = row._subscanMode

                self._subscanModeExists = True

            # by default set systematically correlatorCalibration's value to something not None

            self._correlatorCalibration = CorrelatorCalibration.from_int(0)

            if row._correlatorCalibrationExists:

                if row._correlatorCalibration is not None:
                    self._correlatorCalibration = row._correlatorCalibration

                self._correlatorCalibrationExists = True

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

        result += Parser.valueToXML("subscanNumber", self._subscanNumber)

        result += Parser.extendedValueToXML("startTime", self._startTime)

        result += Parser.extendedValueToXML("endTime", self._endTime)

        result += Parser.valueToXML("fieldName", self._fieldName)

        result += Parser.valueToXML(
            "subscanIntent", SubscanIntent.name(self._subscanIntent)
        )

        if self._subscanModeExists:

            result += Parser.valueToXML(
                "subscanMode", SwitchingMode.name(self._subscanMode)
            )

        result += Parser.valueToXML("numIntegration", self._numIntegration)

        result += Parser.listValueToXML("numSubintegration", self._numSubintegration)

        if self._correlatorCalibrationExists:

            result += Parser.valueToXML(
                "correlatorCalibration",
                CorrelatorCalibration.name(self._correlatorCalibration),
            )

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
                "xmlrow is not a string or a minidom.Element", "SubscanTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "SubscanTable")

        # intrinsic attribute values

        scanNumberNode = rowdom.getElementsByTagName("scanNumber")[0]

        self._scanNumber = int(scanNumberNode.firstChild.data.strip())

        subscanNumberNode = rowdom.getElementsByTagName("subscanNumber")[0]

        self._subscanNumber = int(subscanNumberNode.firstChild.data.strip())

        startTimeNode = rowdom.getElementsByTagName("startTime")[0]

        self._startTime = ArrayTime(startTimeNode.firstChild.data.strip())

        endTimeNode = rowdom.getElementsByTagName("endTime")[0]

        self._endTime = ArrayTime(endTimeNode.firstChild.data.strip())

        fieldNameNode = rowdom.getElementsByTagName("fieldName")[0]

        self._fieldName = str(fieldNameNode.firstChild.data.strip())

        subscanIntentNode = rowdom.getElementsByTagName("subscanIntent")[0]

        self._subscanIntent = SubscanIntent.newSubscanIntent(
            subscanIntentNode.firstChild.data.strip()
        )

        subscanModeNode = rowdom.getElementsByTagName("subscanMode")
        if len(subscanModeNode) > 0:

            self._subscanMode = SwitchingMode.newSwitchingMode(
                subscanModeNode[0].firstChild.data.strip()
            )

            self._subscanModeExists = True

        numIntegrationNode = rowdom.getElementsByTagName("numIntegration")[0]

        self._numIntegration = int(numIntegrationNode.firstChild.data.strip())

        numSubintegrationNode = rowdom.getElementsByTagName("numSubintegration")[0]

        numSubintegrationStr = numSubintegrationNode.firstChild.data.strip()

        self._numSubintegration = Parser.stringListToLists(
            numSubintegrationStr, int, "Subscan", False
        )

        correlatorCalibrationNode = rowdom.getElementsByTagName("correlatorCalibration")
        if len(correlatorCalibrationNode) > 0:

            self._correlatorCalibration = (
                CorrelatorCalibration.newCorrelatorCalibration(
                    correlatorCalibrationNode[0].firstChild.data.strip()
                )
            )

            self._correlatorCalibrationExists = True

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

        eos.writeInt(self._subscanNumber)

        self._startTime.toBin(eos)

        self._endTime.toBin(eos)

        eos.writeStr(self._fieldName)

        eos.writeString(self._subscanIntent.toString())

        eos.writeInt(self._numIntegration)

        eos.writeInt(len(self._numSubintegration))
        for i in range(len(self._numSubintegration)):

            eos.writeInt(self._numSubintegration[i])

        eos.writeBool(self._subscanModeExists)
        if self._subscanModeExists:

            eos.writeString(self._subscanMode.toString())

        eos.writeBool(self._correlatorCalibrationExists)
        if self._correlatorCalibrationExists:

            eos.writeString(self._correlatorCalibration.toString())

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
    def subscanNumberFromBin(row, eis):
        """
        Set the subscanNumber in row from the EndianInput (eis) instance.
        """

        row._subscanNumber = eis.readInt()

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
    def fieldNameFromBin(row, eis):
        """
        Set the fieldName in row from the EndianInput (eis) instance.
        """

        row._fieldName = eis.readStr()

    @staticmethod
    def subscanIntentFromBin(row, eis):
        """
        Set the subscanIntent in row from the EndianInput (eis) instance.
        """

        row._subscanIntent = SubscanIntent.from_int(eis.readInt())

    @staticmethod
    def numIntegrationFromBin(row, eis):
        """
        Set the numIntegration in row from the EndianInput (eis) instance.
        """

        row._numIntegration = eis.readInt()

    @staticmethod
    def numSubintegrationFromBin(row, eis):
        """
        Set the numSubintegration in row from the EndianInput (eis) instance.
        """

        numSubintegrationDim1 = eis.readInt()
        thisList = []
        for i in range(numSubintegrationDim1):
            thisValue = eis.readInt()
            thisList.append(thisValue)
        row._numSubintegration = thisList

    @staticmethod
    def subscanModeFromBin(row, eis):
        """
        Set the optional subscanMode in row from the EndianInput (eis) instance.
        """
        row._subscanModeExists = eis.readBool()
        if row._subscanModeExists:

            row._subscanMode = SwitchingMode.from_int(eis.readInt())

    @staticmethod
    def correlatorCalibrationFromBin(row, eis):
        """
        Set the optional correlatorCalibration in row from the EndianInput (eis) instance.
        """
        row._correlatorCalibrationExists = eis.readBool()
        if row._correlatorCalibrationExists:

            row._correlatorCalibration = CorrelatorCalibration.from_int(eis.readInt())

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["execBlockId"] = SubscanRow.execBlockIdFromBin
        _fromBinMethods["scanNumber"] = SubscanRow.scanNumberFromBin
        _fromBinMethods["subscanNumber"] = SubscanRow.subscanNumberFromBin
        _fromBinMethods["startTime"] = SubscanRow.startTimeFromBin
        _fromBinMethods["endTime"] = SubscanRow.endTimeFromBin
        _fromBinMethods["fieldName"] = SubscanRow.fieldNameFromBin
        _fromBinMethods["subscanIntent"] = SubscanRow.subscanIntentFromBin
        _fromBinMethods["numIntegration"] = SubscanRow.numIntegrationFromBin
        _fromBinMethods["numSubintegration"] = SubscanRow.numSubintegrationFromBin

        _fromBinMethods["subscanMode"] = SubscanRow.subscanModeFromBin
        _fromBinMethods["correlatorCalibration"] = (
            SubscanRow.correlatorCalibrationFromBin
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

        row = SubscanRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Subscan",
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


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the subscanNumber field, which is part of the key, after this row has been added to this table."
            )

        self._subscanNumber = int(subscanNumber)

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

    # ===> Attribute fieldName

    _fieldName = None

    def getFieldName(self):
        """
        Get fieldName.
        return fieldName as str
        """

        return self._fieldName

    def setFieldName(self, fieldName):
        """
        Set fieldName with the specified str value.
        fieldName The str value to which fieldName is to be set.


        """

        self._fieldName = str(fieldName)

    # ===> Attribute subscanIntent

    _subscanIntent = SubscanIntent.from_int(0)

    def getSubscanIntent(self):
        """
        Get subscanIntent.
        return subscanIntent as SubscanIntent
        """

        return self._subscanIntent

    def setSubscanIntent(self, subscanIntent):
        """
        Set subscanIntent with the specified SubscanIntent value.
        subscanIntent The SubscanIntent value to which subscanIntent is to be set.


        """

        self._subscanIntent = SubscanIntent(subscanIntent)

    # ===> Attribute subscanMode, which is optional
    _subscanModeExists = False

    _subscanMode = SwitchingMode.from_int(0)

    def isSubscanModeExists(self):
        """
        The attribute subscanMode is optional. Return True if this attribute exists.
        return True if and only if the subscanMode attribute exists.
        """
        return self._subscanModeExists

    def getSubscanMode(self):
        """
        Get subscanMode, which is optional.
        return subscanMode as SwitchingMode
        raises ValueError If subscanMode does not exist.
        """
        if not self._subscanModeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + subscanMode
                + " attribute in table Subscan does not exist!"
            )

        return self._subscanMode

    def setSubscanMode(self, subscanMode):
        """
        Set subscanMode with the specified SwitchingMode value.
        subscanMode The SwitchingMode value to which subscanMode is to be set.


        """

        self._subscanMode = SwitchingMode(subscanMode)

        self._subscanModeExists = True

    def clearSubscanMode(self):
        """
        Mark subscanMode, which is an optional field, as non-existent.
        """
        self._subscanModeExists = False

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

    # ===> Attribute numSubintegration

    _numSubintegration = None  # this is a 1D list of int

    def getNumSubintegration(self):
        """
        Get numSubintegration.
        return numSubintegration as int []
        """

        return copy.deepcopy(self._numSubintegration)

    def setNumSubintegration(self, numSubintegration):
        """
        Set numSubintegration with the specified int []  value.
        numSubintegration The int []  value to which numSubintegration is to be set.


        """

        # value must be a list
        if not isinstance(numSubintegration, list):
            raise ValueError("The value of numSubintegration must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(numSubintegration)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of numSubintegration is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not Parser.checkListType(numSubintegration, int):
                raise ValueError(
                    "type of the first value in numSubintegration is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._numSubintegration = copy.deepcopy(numSubintegration)
        except Exception as exc:
            raise ValueError("Invalid numSubintegration : " + str(exc))

    # ===> Attribute correlatorCalibration, which is optional
    _correlatorCalibrationExists = False

    _correlatorCalibration = CorrelatorCalibration.from_int(0)

    def isCorrelatorCalibrationExists(self):
        """
        The attribute correlatorCalibration is optional. Return True if this attribute exists.
        return True if and only if the correlatorCalibration attribute exists.
        """
        return self._correlatorCalibrationExists

    def getCorrelatorCalibration(self):
        """
        Get correlatorCalibration, which is optional.
        return correlatorCalibration as CorrelatorCalibration
        raises ValueError If correlatorCalibration does not exist.
        """
        if not self._correlatorCalibrationExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + correlatorCalibration
                + " attribute in table Subscan does not exist!"
            )

        return self._correlatorCalibration

    def setCorrelatorCalibration(self, correlatorCalibration):
        """
        Set correlatorCalibration with the specified CorrelatorCalibration value.
        correlatorCalibration The CorrelatorCalibration value to which correlatorCalibration is to be set.


        """

        self._correlatorCalibration = CorrelatorCalibration(correlatorCalibration)

        self._correlatorCalibrationExists = True

    def clearCorrelatorCalibration(self):
        """
        Mark correlatorCalibration, which is an optional field, as non-existent.
        """
        self._correlatorCalibrationExists = False

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
        subscanNumber,
        startTime,
        endTime,
        fieldName,
        subscanIntent,
        numIntegration,
        numSubintegration,
    ):
        """
        Compare each attribute except the autoincrementable one of this SubscanRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # execBlockId is a Tag, compare using the equals method.
        if not self._execBlockId.equals(execBlockId):
            return False

        # scanNumber is a int, compare using the == operator.
        if not (self._scanNumber == scanNumber):
            return False

        # subscanNumber is a int, compare using the == operator.
        if not (self._subscanNumber == subscanNumber):
            return False

        # startTime is a ArrayTime, compare using the equals method.
        if not self._startTime.equals(startTime):
            return False

        # endTime is a ArrayTime, compare using the equals method.
        if not self._endTime.equals(endTime):
            return False

        # fieldName is a str, compare using the == operator.
        if not (self._fieldName == fieldName):
            return False

        # subscanIntent is a SubscanIntent, compare using the == operator on the getValue() output
        if not (self._subscanIntent.getValue() == subscanIntent.getValue()):
            return False

        # numIntegration is a int, compare using the == operator.
        if not (self._numIntegration == numIntegration):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._numSubintegration) != len(numSubintegration):
            return False
        for indx in range(len(numSubintegration)):

            # numSubintegration is a list of int, compare using == operator.
            if not (self._numSubintegration[indx] == numSubintegration[indx]):
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
            otherRow.getFieldName(),
            otherRow.getSubscanIntent(),
            otherRow.getNumIntegration(),
            otherRow.getNumSubintegration(),
        )

    def compareRequiredValue(
        self,
        startTime,
        endTime,
        fieldName,
        subscanIntent,
        numIntegration,
        numSubintegration,
    ):

        # startTime is a ArrayTime, compare using the equals method.
        if not self._startTime.equals(startTime):
            return False

        # endTime is a ArrayTime, compare using the equals method.
        if not self._endTime.equals(endTime):
            return False

        # fieldName is a str, compare using the == operator.
        if not (self._fieldName == fieldName):
            return False

        # subscanIntent is a SubscanIntent, compare using the == operator on the getValue() output
        if not (self._subscanIntent.getValue() == subscanIntent.getValue()):
            return False

        # numIntegration is a int, compare using the == operator.
        if not (self._numIntegration == numIntegration):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._numSubintegration) != len(numSubintegration):
            return False
        for indx in range(len(numSubintegration)):

            # numSubintegration is a list of int, compare using == operator.
            if not (self._numSubintegration[indx] == numSubintegration[indx]):
                return False

        return True


# initialize the dictionary that maps fields to init methods
SubscanRow.initFromBinMethods()
