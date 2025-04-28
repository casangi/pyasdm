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
# File CalReductionRow.py
#

import pyasdm.CalReductionTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.InvalidatingCondition import InvalidatingCondition


from xml.dom import minidom

import copy


class CalReductionRow:
    """
    The CalReductionRow class is a row of a CalReductionTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalReductionRow.
        When row is None, create an empty row attached to table, which must be a CalReductionTable.
        When row is given, copy those values in to the new row. The row argument must be a CalReductionRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalReductionTable):
            raise ValueError("table must be a CalReductionTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._calReductionId = Tag()

        self._numApplied = 0

        self._appliedCalibrations = []  # this is a list of str []

        self._numParam = 0

        self._paramSet = []  # this is a list of str []

        self._numInvalidConditions = 0

        self._invalidConditions = []  # this is a list of InvalidatingCondition []

        self._timeReduced = ArrayTime()

        self._messages = None

        self._software = None

        self._softwareVersion = None

        if row is not None:
            if not isinstance(row, CalReductionRow):
                raise ValueError("row must be a CalReductionRow")

            # copy constructor

            self._calReductionId = Tag(row._calReductionId)

            self._numApplied = row._numApplied

            # appliedCalibrations is a  list , make a deep copy
            self._appliedCalibrations = copy.deepcopy(row._appliedCalibrations)

            self._numParam = row._numParam

            # paramSet is a  list , make a deep copy
            self._paramSet = copy.deepcopy(row._paramSet)

            self._numInvalidConditions = row._numInvalidConditions

            # invalidConditions is a  list , make a deep copy
            self._invalidConditions = copy.deepcopy(row._invalidConditions)

            self._timeReduced = ArrayTime(row._timeReduced)

            self._messages = row._messages

            self._software = row._software

            self._softwareVersion = row._softwareVersion

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

        result += Parser.extendedValueToXML("calReductionId", self._calReductionId)

        result += Parser.valueToXML("numApplied", self._numApplied)

        result += Parser.listValueToXML(
            "appliedCalibrations", self._appliedCalibrations
        )

        result += Parser.valueToXML("numParam", self._numParam)

        result += Parser.listValueToXML("paramSet", self._paramSet)

        result += Parser.valueToXML("numInvalidConditions", self._numInvalidConditions)

        result += Parser.listEnumValueToXML(
            "invalidConditions", self._invalidConditions
        )

        result += Parser.extendedValueToXML("timeReduced", self._timeReduced)

        result += Parser.valueToXML("messages", self._messages)

        result += Parser.valueToXML("software", self._software)

        result += Parser.valueToXML("softwareVersion", self._softwareVersion)

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
                "xmlrow is not a string or a minidom.Element", "CalReductionTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalReductionTable")

        # intrinsic attribute values

        calReductionIdNode = rowdom.getElementsByTagName("calReductionId")[0]

        self._calReductionId = Tag(calReductionIdNode.firstChild.data.strip())

        numAppliedNode = rowdom.getElementsByTagName("numApplied")[0]

        self._numApplied = int(numAppliedNode.firstChild.data.strip())

        appliedCalibrationsNode = rowdom.getElementsByTagName("appliedCalibrations")[0]

        appliedCalibrationsStr = appliedCalibrationsNode.firstChild.data.strip()

        self._appliedCalibrations = Parser.stringListToLists(
            appliedCalibrationsStr, str, "CalReduction", False
        )

        numParamNode = rowdom.getElementsByTagName("numParam")[0]

        self._numParam = int(numParamNode.firstChild.data.strip())

        paramSetNode = rowdom.getElementsByTagName("paramSet")[0]

        paramSetStr = paramSetNode.firstChild.data.strip()

        self._paramSet = Parser.stringListToLists(
            paramSetStr, str, "CalReduction", False
        )

        numInvalidConditionsNode = rowdom.getElementsByTagName("numInvalidConditions")[
            0
        ]

        self._numInvalidConditions = int(
            numInvalidConditionsNode.firstChild.data.strip()
        )

        invalidConditionsNode = rowdom.getElementsByTagName("invalidConditions")[0]

        invalidConditionsStr = invalidConditionsNode.firstChild.data.strip()
        self._invalidConditions = Parser.stringListToLists(
            invalidConditionsStr, InvalidatingCondition, "CalReduction", False
        )

        timeReducedNode = rowdom.getElementsByTagName("timeReduced")[0]

        self._timeReduced = ArrayTime(timeReducedNode.firstChild.data.strip())

        messagesNode = rowdom.getElementsByTagName("messages")[0]

        self._messages = str(messagesNode.firstChild.data.strip())

        softwareNode = rowdom.getElementsByTagName("software")[0]

        self._software = str(softwareNode.firstChild.data.strip())

        softwareVersionNode = rowdom.getElementsByTagName("softwareVersion")[0]

        self._softwareVersion = str(softwareVersionNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._calReductionId.toBin(eos)

        eos.writeInt(self._numApplied)

        eos.writeInt(len(self._appliedCalibrations))
        for i in range(len(self._appliedCalibrations)):

            eos.writeStr(self._appliedCalibrations[i])

        eos.writeInt(self._numParam)

        eos.writeInt(len(self._paramSet))
        for i in range(len(self._paramSet)):

            eos.writeStr(self._paramSet[i])

        eos.writeInt(self._numInvalidConditions)

        eos.writeInt(len(self._invalidConditions))
        for i in range(len(self._invalidConditions)):

            eos.writeString(str(self._invalidConditions[i]))

        self._timeReduced.toBin(eos)

        eos.writeStr(self._messages)

        eos.writeStr(self._software)

        eos.writeStr(self._softwareVersion)

    @staticmethod
    def calReductionIdFromBin(row, eis):
        """
        Set the calReductionId in row from the EndianInput (eis) instance.
        """

        row._calReductionId = Tag.fromBin(eis)

    @staticmethod
    def numAppliedFromBin(row, eis):
        """
        Set the numApplied in row from the EndianInput (eis) instance.
        """

        row._numApplied = eis.readInt()

    @staticmethod
    def appliedCalibrationsFromBin(row, eis):
        """
        Set the appliedCalibrations in row from the EndianInput (eis) instance.
        """

        appliedCalibrationsDim1 = eis.readInt()
        thisList = []
        for i in range(appliedCalibrationsDim1):
            thisValue = eis.readStr()
            thisList.append(thisValue)
        row._appliedCalibrations = thisList

    @staticmethod
    def numParamFromBin(row, eis):
        """
        Set the numParam in row from the EndianInput (eis) instance.
        """

        row._numParam = eis.readInt()

    @staticmethod
    def paramSetFromBin(row, eis):
        """
        Set the paramSet in row from the EndianInput (eis) instance.
        """

        paramSetDim1 = eis.readInt()
        thisList = []
        for i in range(paramSetDim1):
            thisValue = eis.readStr()
            thisList.append(thisValue)
        row._paramSet = thisList

    @staticmethod
    def numInvalidConditionsFromBin(row, eis):
        """
        Set the numInvalidConditions in row from the EndianInput (eis) instance.
        """

        row._numInvalidConditions = eis.readInt()

    @staticmethod
    def invalidConditionsFromBin(row, eis):
        """
        Set the invalidConditions in row from the EndianInput (eis) instance.
        """

        invalidConditionsDim1 = eis.readInt()
        thisList = []
        for i in range(invalidConditionsDim1):
            thisValue = InvalidatingCondition.literal(eis.readString())
            thisList.append(thisValue)
        row._invalidConditions = thisList

    @staticmethod
    def timeReducedFromBin(row, eis):
        """
        Set the timeReduced in row from the EndianInput (eis) instance.
        """

        row._timeReduced = ArrayTime.fromBin(eis)

    @staticmethod
    def messagesFromBin(row, eis):
        """
        Set the messages in row from the EndianInput (eis) instance.
        """

        row._messages = eis.readStr()

    @staticmethod
    def softwareFromBin(row, eis):
        """
        Set the software in row from the EndianInput (eis) instance.
        """

        row._software = eis.readStr()

    @staticmethod
    def softwareVersionFromBin(row, eis):
        """
        Set the softwareVersion in row from the EndianInput (eis) instance.
        """

        row._softwareVersion = eis.readStr()

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["calReductionId"] = CalReductionRow.calReductionIdFromBin
        _fromBinMethods["numApplied"] = CalReductionRow.numAppliedFromBin
        _fromBinMethods["appliedCalibrations"] = (
            CalReductionRow.appliedCalibrationsFromBin
        )
        _fromBinMethods["numParam"] = CalReductionRow.numParamFromBin
        _fromBinMethods["paramSet"] = CalReductionRow.paramSetFromBin
        _fromBinMethods["numInvalidConditions"] = (
            CalReductionRow.numInvalidConditionsFromBin
        )
        _fromBinMethods["invalidConditions"] = CalReductionRow.invalidConditionsFromBin
        _fromBinMethods["timeReduced"] = CalReductionRow.timeReducedFromBin
        _fromBinMethods["messages"] = CalReductionRow.messagesFromBin
        _fromBinMethods["software"] = CalReductionRow.softwareFromBin
        _fromBinMethods["softwareVersion"] = CalReductionRow.softwareVersionFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CalReductionRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalReduction",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute calReductionId

    _calReductionId = Tag()

    def getCalReductionId(self):
        """
        Get calReductionId.
        return calReductionId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._calReductionId)

    def setCalReductionId(self, calReductionId):
        """
        Set calReductionId with the specified Tag value.
        calReductionId The Tag value to which calReductionId is to be set.
        The value of calReductionId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the calReductionId field, which is part of the key, after this row has been added to this table."
            )

        self._calReductionId = Tag(calReductionId)

    # ===> Attribute numApplied

    _numApplied = 0

    def getNumApplied(self):
        """
        Get numApplied.
        return numApplied as int
        """

        return self._numApplied

    def setNumApplied(self, numApplied):
        """
        Set numApplied with the specified int value.
        numApplied The int value to which numApplied is to be set.


        """

        self._numApplied = int(numApplied)

    # ===> Attribute appliedCalibrations

    _appliedCalibrations = None  # this is a 1D list of str

    def getAppliedCalibrations(self):
        """
        Get appliedCalibrations.
        return appliedCalibrations as str []
        """

        return copy.deepcopy(self._appliedCalibrations)

    def setAppliedCalibrations(self, appliedCalibrations):
        """
        Set appliedCalibrations with the specified str []  value.
        appliedCalibrations The str []  value to which appliedCalibrations is to be set.


        """

        # value must be a list
        if not isinstance(appliedCalibrations, list):
            raise ValueError("The value of appliedCalibrations must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(appliedCalibrations)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of appliedCalibrations is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(appliedCalibrations, str):
                raise ValueError(
                    "type of the first value in appliedCalibrations is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._appliedCalibrations = copy.deepcopy(appliedCalibrations)
        except Exception as exc:
            raise ValueError("Invalid appliedCalibrations : " + str(exc))

    # ===> Attribute numParam

    _numParam = 0

    def getNumParam(self):
        """
        Get numParam.
        return numParam as int
        """

        return self._numParam

    def setNumParam(self, numParam):
        """
        Set numParam with the specified int value.
        numParam The int value to which numParam is to be set.


        """

        self._numParam = int(numParam)

    # ===> Attribute paramSet

    _paramSet = None  # this is a 1D list of str

    def getParamSet(self):
        """
        Get paramSet.
        return paramSet as str []
        """

        return copy.deepcopy(self._paramSet)

    def setParamSet(self, paramSet):
        """
        Set paramSet with the specified str []  value.
        paramSet The str []  value to which paramSet is to be set.


        """

        # value must be a list
        if not isinstance(paramSet, list):
            raise ValueError("The value of paramSet must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(paramSet)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of paramSet is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(paramSet, str):
                raise ValueError(
                    "type of the first value in paramSet is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._paramSet = copy.deepcopy(paramSet)
        except Exception as exc:
            raise ValueError("Invalid paramSet : " + str(exc))

    # ===> Attribute numInvalidConditions

    _numInvalidConditions = 0

    def getNumInvalidConditions(self):
        """
        Get numInvalidConditions.
        return numInvalidConditions as int
        """

        return self._numInvalidConditions

    def setNumInvalidConditions(self, numInvalidConditions):
        """
        Set numInvalidConditions with the specified int value.
        numInvalidConditions The int value to which numInvalidConditions is to be set.


        """

        self._numInvalidConditions = int(numInvalidConditions)

    # ===> Attribute invalidConditions

    _invalidConditions = None  # this is a 1D list of InvalidatingCondition

    def getInvalidConditions(self):
        """
        Get invalidConditions.
        return invalidConditions as InvalidatingCondition []
        """

        return copy.deepcopy(self._invalidConditions)

    def setInvalidConditions(self, invalidConditions):
        """
        Set invalidConditions with the specified InvalidatingCondition []  value.
        invalidConditions The InvalidatingCondition []  value to which invalidConditions is to be set.


        """

        # value must be a list
        if not isinstance(invalidConditions, list):
            raise ValueError("The value of invalidConditions must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(invalidConditions)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of invalidConditions is not correct")

            # the type of the values in the list must be InvalidatingCondition
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(invalidConditions, InvalidatingCondition):
                raise ValueError(
                    "type of the first value in invalidConditions is not InvalidatingCondition as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._invalidConditions = copy.deepcopy(invalidConditions)
        except Exception as exc:
            raise ValueError("Invalid invalidConditions : " + str(exc))

    # ===> Attribute timeReduced

    _timeReduced = ArrayTime()

    def getTimeReduced(self):
        """
        Get timeReduced.
        return timeReduced as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._timeReduced)

    def setTimeReduced(self, timeReduced):
        """
        Set timeReduced with the specified ArrayTime value.
        timeReduced The ArrayTime value to which timeReduced is to be set.
        The value of timeReduced can be anything allowed by the ArrayTime constructor.

        """

        self._timeReduced = ArrayTime(timeReduced)

    # ===> Attribute messages

    _messages = None

    def getMessages(self):
        """
        Get messages.
        return messages as str
        """

        return self._messages

    def setMessages(self, messages):
        """
        Set messages with the specified str value.
        messages The str value to which messages is to be set.


        """

        self._messages = str(messages)

    # ===> Attribute software

    _software = None

    def getSoftware(self):
        """
        Get software.
        return software as str
        """

        return self._software

    def setSoftware(self, software):
        """
        Set software with the specified str value.
        software The str value to which software is to be set.


        """

        self._software = str(software)

    # ===> Attribute softwareVersion

    _softwareVersion = None

    def getSoftwareVersion(self):
        """
        Get softwareVersion.
        return softwareVersion as str
        """

        return self._softwareVersion

    def setSoftwareVersion(self, softwareVersion):
        """
        Set softwareVersion with the specified str value.
        softwareVersion The str value to which softwareVersion is to be set.


        """

        self._softwareVersion = str(softwareVersion)

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(
        self,
        numApplied,
        appliedCalibrations,
        numParam,
        paramSet,
        numInvalidConditions,
        invalidConditions,
        timeReduced,
        messages,
        software,
        softwareVersion,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalReductionRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # numApplied is a int, compare using the == operator.
        if not (self._numApplied == numApplied):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._appliedCalibrations) != len(appliedCalibrations):
            return False
        for indx in range(len(appliedCalibrations)):

            # appliedCalibrations is a list of str, compare using == operator.
            if not (self._appliedCalibrations[indx] == appliedCalibrations[indx]):
                return False

        # numParam is a int, compare using the == operator.
        if not (self._numParam == numParam):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._paramSet) != len(paramSet):
            return False
        for indx in range(len(paramSet)):

            # paramSet is a list of str, compare using == operator.
            if not (self._paramSet[indx] == paramSet[indx]):
                return False

        # numInvalidConditions is a int, compare using the == operator.
        if not (self._numInvalidConditions == numInvalidConditions):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._invalidConditions) != len(invalidConditions):
            return False
        for indx in range(len(invalidConditions)):

            # invalidConditions is a list of InvalidatingCondition, compare using == operator.
            if not (self._invalidConditions[indx] == invalidConditions[indx]):
                return False

        # timeReduced is a ArrayTime, compare using the equals method.
        if not self._timeReduced.equals(timeReduced):
            return False

        # messages is a str, compare using the == operator.
        if not (self._messages == messages):
            return False

        # software is a str, compare using the == operator.
        if not (self._software == software):
            return False

        # softwareVersion is a str, compare using the == operator.
        if not (self._softwareVersion == softwareVersion):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumApplied(),
            otherRow.getAppliedCalibrations(),
            otherRow.getNumParam(),
            otherRow.getParamSet(),
            otherRow.getNumInvalidConditions(),
            otherRow.getInvalidConditions(),
            otherRow.getTimeReduced(),
            otherRow.getMessages(),
            otherRow.getSoftware(),
            otherRow.getSoftwareVersion(),
        )

    def compareRequiredValue(
        self,
        numApplied,
        appliedCalibrations,
        numParam,
        paramSet,
        numInvalidConditions,
        invalidConditions,
        timeReduced,
        messages,
        software,
        softwareVersion,
    ):

        # numApplied is a int, compare using the == operator.
        if not (self._numApplied == numApplied):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._appliedCalibrations) != len(appliedCalibrations):
            return False
        for indx in range(len(appliedCalibrations)):

            # appliedCalibrations is a list of str, compare using == operator.
            if not (self._appliedCalibrations[indx] == appliedCalibrations[indx]):
                return False

        # numParam is a int, compare using the == operator.
        if not (self._numParam == numParam):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._paramSet) != len(paramSet):
            return False
        for indx in range(len(paramSet)):

            # paramSet is a list of str, compare using == operator.
            if not (self._paramSet[indx] == paramSet[indx]):
                return False

        # numInvalidConditions is a int, compare using the == operator.
        if not (self._numInvalidConditions == numInvalidConditions):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._invalidConditions) != len(invalidConditions):
            return False
        for indx in range(len(invalidConditions)):

            # invalidConditions is a list of InvalidatingCondition, compare using == operator.
            if not (self._invalidConditions[indx] == invalidConditions[indx]):
                return False

        # timeReduced is a ArrayTime, compare using the equals method.
        if not self._timeReduced.equals(timeReduced):
            return False

        # messages is a str, compare using the == operator.
        if not (self._messages == messages):
            return False

        # software is a str, compare using the == operator.
        if not (self._software == software):
            return False

        # softwareVersion is a str, compare using the == operator.
        if not (self._softwareVersion == softwareVersion):
            return False

        return True


# initialize the dictionary that maps fields to init methods
CalReductionRow.initFromBinMethods()
