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
# File SBSummaryRow.py
#

import pyasdm.SBSummaryTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.SBType import SBType


from pyasdm.enumerations.DirectionReferenceCode import DirectionReferenceCode


from xml.dom import minidom

import copy


class SBSummaryRow:
    """
    The SBSummaryRow class is a row of a SBSummaryTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a SBSummaryRow.
        When row is None, create an empty row attached to table, which must be a SBSummaryTable.
        When row is given, copy those values in to the new row. The row argument must be a SBSummaryRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.SBSummaryTable):
            raise ValueError("table must be a SBSummaryTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._sBSummaryId = Tag()

        self._sbSummaryUID = EntityRef()

        self._projectUID = EntityRef()

        self._obsUnitSetUID = EntityRef()

        self._frequency = None

        self._frequencyBand = ReceiverBand.from_int(0)

        self._sbType = SBType.from_int(0)

        self._sbDuration = Interval()

        self._numObservingMode = 0

        self._observingMode = []  # this is a list of str []

        self._numberRepeats = 0

        self._numScienceGoal = 0

        self._scienceGoal = []  # this is a list of str []

        self._numWeatherConstraint = 0

        self._weatherConstraint = []  # this is a list of str []

        self._centerDirectionExists = False

        self._centerDirection = []  # this is a list of Angle []

        self._centerDirectionCodeExists = False

        self._centerDirectionCode = DirectionReferenceCode.from_int(0)

        self._centerDirectionEquinoxExists = False

        self._centerDirectionEquinox = ArrayTime()

        if row is not None:
            if not isinstance(row, SBSummaryRow):
                raise ValueError("row must be a SBSummaryRow")

            # copy constructor

            self._sBSummaryId = Tag(row._sBSummaryId)

            self._sbSummaryUID = EntityRef(row._sbSummaryUID)

            self._projectUID = EntityRef(row._projectUID)

            self._obsUnitSetUID = EntityRef(row._obsUnitSetUID)

            self._frequency = row._frequency

            # We force the attribute of the result to be not None
            if row._frequencyBand is None:
                self._frequencyBand = ReceiverBand.from_int(0)
            else:
                self._frequencyBand = ReceiverBand(row._frequencyBand)

            # We force the attribute of the result to be not None
            if row._sbType is None:
                self._sbType = SBType.from_int(0)
            else:
                self._sbType = SBType(row._sbType)

            self._sbDuration = Interval(row._sbDuration)

            self._numObservingMode = row._numObservingMode

            # observingMode is a  list , make a deep copy
            self._observingMode = copy.deepcopy(row._observingMode)

            self._numberRepeats = row._numberRepeats

            self._numScienceGoal = row._numScienceGoal

            # scienceGoal is a  list , make a deep copy
            self._scienceGoal = copy.deepcopy(row._scienceGoal)

            self._numWeatherConstraint = row._numWeatherConstraint

            # weatherConstraint is a  list , make a deep copy
            self._weatherConstraint = copy.deepcopy(row._weatherConstraint)

            # by default set systematically centerDirection's value to something not None

            if row._centerDirectionExists:

                # centerDirection is a list, make a deep copy
                self._centerDirection = copy.deepcopy(row._centerDirection)

                self._centerDirectionExists = True

            # by default set systematically centerDirectionCode's value to something not None

            self._centerDirectionCode = DirectionReferenceCode.from_int(0)

            if row._centerDirectionCodeExists:

                if row._centerDirectionCode is not None:
                    self._centerDirectionCode = row._centerDirectionCode

                self._centerDirectionCodeExists = True

            # by default set systematically centerDirectionEquinox's value to something not None

            if row._centerDirectionEquinoxExists:

                self._centerDirectionEquinox = ArrayTime(row._centerDirectionEquinox)

                self._centerDirectionEquinoxExists = True

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

        result += Parser.extendedValueToXML("sBSummaryId", self._sBSummaryId)

        result += Parser.extendedValueToXML("sbSummaryUID", self._sbSummaryUID)

        result += Parser.extendedValueToXML("projectUID", self._projectUID)

        result += Parser.extendedValueToXML("obsUnitSetUID", self._obsUnitSetUID)

        result += Parser.valueToXML("frequency", self._frequency)

        result += Parser.valueToXML(
            "frequencyBand", ReceiverBand.name(self._frequencyBand)
        )

        result += Parser.valueToXML("sbType", SBType.name(self._sbType))

        result += Parser.extendedValueToXML("sbDuration", self._sbDuration)

        result += Parser.valueToXML("numObservingMode", self._numObservingMode)

        result += Parser.listValueToXML("observingMode", self._observingMode)

        result += Parser.valueToXML("numberRepeats", self._numberRepeats)

        result += Parser.valueToXML("numScienceGoal", self._numScienceGoal)

        result += Parser.listValueToXML("scienceGoal", self._scienceGoal)

        result += Parser.valueToXML("numWeatherConstraint", self._numWeatherConstraint)

        result += Parser.listValueToXML("weatherConstraint", self._weatherConstraint)

        if self._centerDirectionExists:

            result += Parser.listExtendedValueToXML(
                "centerDirection", self._centerDirection
            )

        if self._centerDirectionCodeExists:

            result += Parser.valueToXML(
                "centerDirectionCode",
                DirectionReferenceCode.name(self._centerDirectionCode),
            )

        if self._centerDirectionEquinoxExists:

            result += Parser.extendedValueToXML(
                "centerDirectionEquinox", self._centerDirectionEquinox
            )

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
                "xmlrow is not a string or a minidom.Element", "SBSummaryTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "SBSummaryTable")

        # intrinsic attribute values

        sBSummaryIdNode = rowdom.getElementsByTagName("sBSummaryId")[0]

        self._sBSummaryId = Tag(sBSummaryIdNode.firstChild.data.strip())

        sbSummaryUIDNode = rowdom.getElementsByTagName("sbSummaryUID")[0]

        self._sbSummaryUID = EntityRef(sbSummaryUIDNode.toxml())

        projectUIDNode = rowdom.getElementsByTagName("projectUID")[0]

        self._projectUID = EntityRef(projectUIDNode.toxml())

        obsUnitSetUIDNode = rowdom.getElementsByTagName("obsUnitSetUID")[0]

        self._obsUnitSetUID = EntityRef(obsUnitSetUIDNode.toxml())

        frequencyNode = rowdom.getElementsByTagName("frequency")[0]

        self._frequency = float(frequencyNode.firstChild.data.strip())

        frequencyBandNode = rowdom.getElementsByTagName("frequencyBand")[0]

        self._frequencyBand = ReceiverBand.newReceiverBand(
            frequencyBandNode.firstChild.data.strip()
        )

        sbTypeNode = rowdom.getElementsByTagName("sbType")[0]

        self._sbType = SBType.newSBType(sbTypeNode.firstChild.data.strip())

        sbDurationNode = rowdom.getElementsByTagName("sbDuration")[0]

        self._sbDuration = Interval(sbDurationNode.firstChild.data.strip())

        numObservingModeNode = rowdom.getElementsByTagName("numObservingMode")[0]

        self._numObservingMode = int(numObservingModeNode.firstChild.data.strip())

        observingModeNode = rowdom.getElementsByTagName("observingMode")[0]

        observingModeStr = observingModeNode.firstChild.data.strip()

        self._observingMode = Parser.stringListToLists(
            observingModeStr, str, "SBSummary", False
        )

        numberRepeatsNode = rowdom.getElementsByTagName("numberRepeats")[0]

        self._numberRepeats = int(numberRepeatsNode.firstChild.data.strip())

        numScienceGoalNode = rowdom.getElementsByTagName("numScienceGoal")[0]

        self._numScienceGoal = int(numScienceGoalNode.firstChild.data.strip())

        scienceGoalNode = rowdom.getElementsByTagName("scienceGoal")[0]

        scienceGoalStr = scienceGoalNode.firstChild.data.strip()

        self._scienceGoal = Parser.stringListToLists(
            scienceGoalStr, str, "SBSummary", False
        )

        numWeatherConstraintNode = rowdom.getElementsByTagName("numWeatherConstraint")[
            0
        ]

        self._numWeatherConstraint = int(
            numWeatherConstraintNode.firstChild.data.strip()
        )

        weatherConstraintNode = rowdom.getElementsByTagName("weatherConstraint")[0]

        weatherConstraintStr = weatherConstraintNode.firstChild.data.strip()

        self._weatherConstraint = Parser.stringListToLists(
            weatherConstraintStr, str, "SBSummary", False
        )

        centerDirectionNode = rowdom.getElementsByTagName("centerDirection")
        if len(centerDirectionNode) > 0:

            centerDirectionStr = centerDirectionNode[0].firstChild.data.strip()

            self._centerDirection = Parser.stringListToLists(
                centerDirectionStr, Angle, "SBSummary", True
            )

            self._centerDirectionExists = True

        centerDirectionCodeNode = rowdom.getElementsByTagName("centerDirectionCode")
        if len(centerDirectionCodeNode) > 0:

            self._centerDirectionCode = (
                DirectionReferenceCode.newDirectionReferenceCode(
                    centerDirectionCodeNode[0].firstChild.data.strip()
                )
            )

            self._centerDirectionCodeExists = True

        centerDirectionEquinoxNode = rowdom.getElementsByTagName(
            "centerDirectionEquinox"
        )
        if len(centerDirectionEquinoxNode) > 0:

            self._centerDirectionEquinox = ArrayTime(
                centerDirectionEquinoxNode[0].firstChild.data.strip()
            )

            self._centerDirectionEquinoxExists = True

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._sBSummaryId.toBin(eos)

        self._sbSummaryUID.toBin(eos)

        self._projectUID.toBin(eos)

        self._obsUnitSetUID.toBin(eos)

        eos.writeFloat(self._frequency)

        eos.writeString(str(self._frequencyBand))

        eos.writeString(str(self._sbType))

        self._sbDuration.toBin(eos)

        eos.writeInt(self._numObservingMode)

        eos.writeInt(len(self._observingMode))
        for i in range(len(self._observingMode)):

            eos.writeStr(self._observingMode[i])

        eos.writeInt(self._numberRepeats)

        eos.writeInt(self._numScienceGoal)

        eos.writeInt(len(self._scienceGoal))
        for i in range(len(self._scienceGoal)):

            eos.writeStr(self._scienceGoal[i])

        eos.writeInt(self._numWeatherConstraint)

        eos.writeInt(len(self._weatherConstraint))
        for i in range(len(self._weatherConstraint)):

            eos.writeStr(self._weatherConstraint[i])

        eos.writeBool(self._centerDirectionExists)
        if self._centerDirectionExists:

            Angle.listToBin(self._centerDirection, eos)

        eos.writeBool(self._centerDirectionCodeExists)
        if self._centerDirectionCodeExists:

            eos.writeString(str(self._centerDirectionCode))

        eos.writeBool(self._centerDirectionEquinoxExists)
        if self._centerDirectionEquinoxExists:

            self._centerDirectionEquinox.toBin(eos)

    @staticmethod
    def sBSummaryIdFromBin(row, eis):
        """
        Set the sBSummaryId in row from the EndianInput (eis) instance.
        """

        row._sBSummaryId = Tag.fromBin(eis)

    @staticmethod
    def sbSummaryUIDFromBin(row, eis):
        """
        Set the sbSummaryUID in row from the EndianInput (eis) instance.
        """

        row._sbSummaryUID = EntityRef.fromBin(eis)

    @staticmethod
    def projectUIDFromBin(row, eis):
        """
        Set the projectUID in row from the EndianInput (eis) instance.
        """

        row._projectUID = EntityRef.fromBin(eis)

    @staticmethod
    def obsUnitSetUIDFromBin(row, eis):
        """
        Set the obsUnitSetUID in row from the EndianInput (eis) instance.
        """

        row._obsUnitSetUID = EntityRef.fromBin(eis)

    @staticmethod
    def frequencyFromBin(row, eis):
        """
        Set the frequency in row from the EndianInput (eis) instance.
        """

        row._frequency = eis.readFloat()

    @staticmethod
    def frequencyBandFromBin(row, eis):
        """
        Set the frequencyBand in row from the EndianInput (eis) instance.
        """

        row._frequencyBand = ReceiverBand.literal(eis.readString())

    @staticmethod
    def sbTypeFromBin(row, eis):
        """
        Set the sbType in row from the EndianInput (eis) instance.
        """

        row._sbType = SBType.literal(eis.readString())

    @staticmethod
    def sbDurationFromBin(row, eis):
        """
        Set the sbDuration in row from the EndianInput (eis) instance.
        """

        row._sbDuration = Interval.fromBin(eis)

    @staticmethod
    def numObservingModeFromBin(row, eis):
        """
        Set the numObservingMode in row from the EndianInput (eis) instance.
        """

        row._numObservingMode = eis.readInt()

    @staticmethod
    def observingModeFromBin(row, eis):
        """
        Set the observingMode in row from the EndianInput (eis) instance.
        """

        observingModeDim1 = eis.readInt()
        thisList = []
        for i in range(observingModeDim1):
            thisValue = eis.readStr()
            thisList.append(thisValue)
        row._observingMode = thisList

    @staticmethod
    def numberRepeatsFromBin(row, eis):
        """
        Set the numberRepeats in row from the EndianInput (eis) instance.
        """

        row._numberRepeats = eis.readInt()

    @staticmethod
    def numScienceGoalFromBin(row, eis):
        """
        Set the numScienceGoal in row from the EndianInput (eis) instance.
        """

        row._numScienceGoal = eis.readInt()

    @staticmethod
    def scienceGoalFromBin(row, eis):
        """
        Set the scienceGoal in row from the EndianInput (eis) instance.
        """

        scienceGoalDim1 = eis.readInt()
        thisList = []
        for i in range(scienceGoalDim1):
            thisValue = eis.readStr()
            thisList.append(thisValue)
        row._scienceGoal = thisList

    @staticmethod
    def numWeatherConstraintFromBin(row, eis):
        """
        Set the numWeatherConstraint in row from the EndianInput (eis) instance.
        """

        row._numWeatherConstraint = eis.readInt()

    @staticmethod
    def weatherConstraintFromBin(row, eis):
        """
        Set the weatherConstraint in row from the EndianInput (eis) instance.
        """

        weatherConstraintDim1 = eis.readInt()
        thisList = []
        for i in range(weatherConstraintDim1):
            thisValue = eis.readStr()
            thisList.append(thisValue)
        row._weatherConstraint = thisList

    @staticmethod
    def centerDirectionFromBin(row, eis):
        """
        Set the optional centerDirection in row from the EndianInput (eis) instance.
        """
        row._centerDirectionExists = eis.readBool()
        if row._centerDirectionExists:

            row._centerDirection = Angle.from1DBin(eis)

    @staticmethod
    def centerDirectionCodeFromBin(row, eis):
        """
        Set the optional centerDirectionCode in row from the EndianInput (eis) instance.
        """
        row._centerDirectionCodeExists = eis.readBool()
        if row._centerDirectionCodeExists:

            row._centerDirectionCode = DirectionReferenceCode.literal(eis.readString())

    @staticmethod
    def centerDirectionEquinoxFromBin(row, eis):
        """
        Set the optional centerDirectionEquinox in row from the EndianInput (eis) instance.
        """
        row._centerDirectionEquinoxExists = eis.readBool()
        if row._centerDirectionEquinoxExists:

            row._centerDirectionEquinox = ArrayTime.fromBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["sBSummaryId"] = SBSummaryRow.sBSummaryIdFromBin
        _fromBinMethods["sbSummaryUID"] = SBSummaryRow.sbSummaryUIDFromBin
        _fromBinMethods["projectUID"] = SBSummaryRow.projectUIDFromBin
        _fromBinMethods["obsUnitSetUID"] = SBSummaryRow.obsUnitSetUIDFromBin
        _fromBinMethods["frequency"] = SBSummaryRow.frequencyFromBin
        _fromBinMethods["frequencyBand"] = SBSummaryRow.frequencyBandFromBin
        _fromBinMethods["sbType"] = SBSummaryRow.sbTypeFromBin
        _fromBinMethods["sbDuration"] = SBSummaryRow.sbDurationFromBin
        _fromBinMethods["numObservingMode"] = SBSummaryRow.numObservingModeFromBin
        _fromBinMethods["observingMode"] = SBSummaryRow.observingModeFromBin
        _fromBinMethods["numberRepeats"] = SBSummaryRow.numberRepeatsFromBin
        _fromBinMethods["numScienceGoal"] = SBSummaryRow.numScienceGoalFromBin
        _fromBinMethods["scienceGoal"] = SBSummaryRow.scienceGoalFromBin
        _fromBinMethods["numWeatherConstraint"] = (
            SBSummaryRow.numWeatherConstraintFromBin
        )
        _fromBinMethods["weatherConstraint"] = SBSummaryRow.weatherConstraintFromBin

        _fromBinMethods["centerDirection"] = SBSummaryRow.centerDirectionFromBin
        _fromBinMethods["centerDirectionCode"] = SBSummaryRow.centerDirectionCodeFromBin
        _fromBinMethods["centerDirectionEquinox"] = (
            SBSummaryRow.centerDirectionEquinoxFromBin
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

        row = SBSummaryRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " SBSummary",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute sBSummaryId

    _sBSummaryId = Tag()

    def getSBSummaryId(self):
        """
        Get sBSummaryId.
        return sBSummaryId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._sBSummaryId)

    def setSBSummaryId(self, sBSummaryId):
        """
        Set sBSummaryId with the specified Tag value.
        sBSummaryId The Tag value to which sBSummaryId is to be set.
        The value of sBSummaryId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the sBSummaryId field, which is part of the key, after this row has been added to this table."
            )

        self._sBSummaryId = Tag(sBSummaryId)

    # ===> Attribute sbSummaryUID

    _sbSummaryUID = EntityRef()

    def getSbSummaryUID(self):
        """
        Get sbSummaryUID.
        return sbSummaryUID as EntityRef
        """

        # make sure it is a copy of EntityRef
        return EntityRef(self._sbSummaryUID)

    def setSbSummaryUID(self, sbSummaryUID):
        """
        Set sbSummaryUID with the specified EntityRef value.
        sbSummaryUID The EntityRef value to which sbSummaryUID is to be set.
        The value of sbSummaryUID can be anything allowed by the EntityRef constructor.

        """

        self._sbSummaryUID = EntityRef(sbSummaryUID)

    # ===> Attribute projectUID

    _projectUID = EntityRef()

    def getProjectUID(self):
        """
        Get projectUID.
        return projectUID as EntityRef
        """

        # make sure it is a copy of EntityRef
        return EntityRef(self._projectUID)

    def setProjectUID(self, projectUID):
        """
        Set projectUID with the specified EntityRef value.
        projectUID The EntityRef value to which projectUID is to be set.
        The value of projectUID can be anything allowed by the EntityRef constructor.

        """

        self._projectUID = EntityRef(projectUID)

    # ===> Attribute obsUnitSetUID

    _obsUnitSetUID = EntityRef()

    def getObsUnitSetUID(self):
        """
        Get obsUnitSetUID.
        return obsUnitSetUID as EntityRef
        """

        # make sure it is a copy of EntityRef
        return EntityRef(self._obsUnitSetUID)

    def setObsUnitSetUID(self, obsUnitSetUID):
        """
        Set obsUnitSetUID with the specified EntityRef value.
        obsUnitSetUID The EntityRef value to which obsUnitSetUID is to be set.
        The value of obsUnitSetUID can be anything allowed by the EntityRef constructor.

        """

        self._obsUnitSetUID = EntityRef(obsUnitSetUID)

    # ===> Attribute frequency

    _frequency = None

    def getFrequency(self):
        """
        Get frequency.
        return frequency as float
        """

        return self._frequency

    def setFrequency(self, frequency):
        """
        Set frequency with the specified float value.
        frequency The float value to which frequency is to be set.


        """

        self._frequency = float(frequency)

    # ===> Attribute frequencyBand

    _frequencyBand = ReceiverBand.from_int(0)

    def getFrequencyBand(self):
        """
        Get frequencyBand.
        return frequencyBand as ReceiverBand
        """

        return self._frequencyBand

    def setFrequencyBand(self, frequencyBand):
        """
        Set frequencyBand with the specified ReceiverBand value.
        frequencyBand The ReceiverBand value to which frequencyBand is to be set.


        """

        self._frequencyBand = ReceiverBand(frequencyBand)

    # ===> Attribute sbType

    _sbType = SBType.from_int(0)

    def getSbType(self):
        """
        Get sbType.
        return sbType as SBType
        """

        return self._sbType

    def setSbType(self, sbType):
        """
        Set sbType with the specified SBType value.
        sbType The SBType value to which sbType is to be set.


        """

        self._sbType = SBType(sbType)

    # ===> Attribute sbDuration

    _sbDuration = Interval()

    def getSbDuration(self):
        """
        Get sbDuration.
        return sbDuration as Interval
        """

        # make sure it is a copy of Interval
        return Interval(self._sbDuration)

    def setSbDuration(self, sbDuration):
        """
        Set sbDuration with the specified Interval value.
        sbDuration The Interval value to which sbDuration is to be set.
        The value of sbDuration can be anything allowed by the Interval constructor.

        """

        self._sbDuration = Interval(sbDuration)

    # ===> Attribute numObservingMode

    _numObservingMode = 0

    def getNumObservingMode(self):
        """
        Get numObservingMode.
        return numObservingMode as int
        """

        return self._numObservingMode

    def setNumObservingMode(self, numObservingMode):
        """
        Set numObservingMode with the specified int value.
        numObservingMode The int value to which numObservingMode is to be set.


        """

        self._numObservingMode = int(numObservingMode)

    # ===> Attribute observingMode

    _observingMode = None  # this is a 1D list of str

    def getObservingMode(self):
        """
        Get observingMode.
        return observingMode as str []
        """

        return copy.deepcopy(self._observingMode)

    def setObservingMode(self, observingMode):
        """
        Set observingMode with the specified str []  value.
        observingMode The str []  value to which observingMode is to be set.


        """

        # value must be a list
        if not isinstance(observingMode, list):
            raise ValueError("The value of observingMode must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(observingMode)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of observingMode is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(observingMode, str):
                raise ValueError(
                    "type of the first value in observingMode is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._observingMode = copy.deepcopy(observingMode)
        except Exception as exc:
            raise ValueError("Invalid observingMode : " + str(exc))

    # ===> Attribute numberRepeats

    _numberRepeats = 0

    def getNumberRepeats(self):
        """
        Get numberRepeats.
        return numberRepeats as int
        """

        return self._numberRepeats

    def setNumberRepeats(self, numberRepeats):
        """
        Set numberRepeats with the specified int value.
        numberRepeats The int value to which numberRepeats is to be set.


        """

        self._numberRepeats = int(numberRepeats)

    # ===> Attribute numScienceGoal

    _numScienceGoal = 0

    def getNumScienceGoal(self):
        """
        Get numScienceGoal.
        return numScienceGoal as int
        """

        return self._numScienceGoal

    def setNumScienceGoal(self, numScienceGoal):
        """
        Set numScienceGoal with the specified int value.
        numScienceGoal The int value to which numScienceGoal is to be set.


        """

        self._numScienceGoal = int(numScienceGoal)

    # ===> Attribute scienceGoal

    _scienceGoal = None  # this is a 1D list of str

    def getScienceGoal(self):
        """
        Get scienceGoal.
        return scienceGoal as str []
        """

        return copy.deepcopy(self._scienceGoal)

    def setScienceGoal(self, scienceGoal):
        """
        Set scienceGoal with the specified str []  value.
        scienceGoal The str []  value to which scienceGoal is to be set.


        """

        # value must be a list
        if not isinstance(scienceGoal, list):
            raise ValueError("The value of scienceGoal must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(scienceGoal)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of scienceGoal is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(scienceGoal, str):
                raise ValueError(
                    "type of the first value in scienceGoal is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._scienceGoal = copy.deepcopy(scienceGoal)
        except Exception as exc:
            raise ValueError("Invalid scienceGoal : " + str(exc))

    # ===> Attribute numWeatherConstraint

    _numWeatherConstraint = 0

    def getNumWeatherConstraint(self):
        """
        Get numWeatherConstraint.
        return numWeatherConstraint as int
        """

        return self._numWeatherConstraint

    def setNumWeatherConstraint(self, numWeatherConstraint):
        """
        Set numWeatherConstraint with the specified int value.
        numWeatherConstraint The int value to which numWeatherConstraint is to be set.


        """

        self._numWeatherConstraint = int(numWeatherConstraint)

    # ===> Attribute weatherConstraint

    _weatherConstraint = None  # this is a 1D list of str

    def getWeatherConstraint(self):
        """
        Get weatherConstraint.
        return weatherConstraint as str []
        """

        return copy.deepcopy(self._weatherConstraint)

    def setWeatherConstraint(self, weatherConstraint):
        """
        Set weatherConstraint with the specified str []  value.
        weatherConstraint The str []  value to which weatherConstraint is to be set.


        """

        # value must be a list
        if not isinstance(weatherConstraint, list):
            raise ValueError("The value of weatherConstraint must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(weatherConstraint)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of weatherConstraint is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(weatherConstraint, str):
                raise ValueError(
                    "type of the first value in weatherConstraint is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._weatherConstraint = copy.deepcopy(weatherConstraint)
        except Exception as exc:
            raise ValueError("Invalid weatherConstraint : " + str(exc))

    # ===> Attribute centerDirection, which is optional
    _centerDirectionExists = False

    _centerDirection = None  # this is a 1D list of Angle

    def isCenterDirectionExists(self):
        """
        The attribute centerDirection is optional. Return True if this attribute exists.
        return True if and only if the centerDirection attribute exists.
        """
        return self._centerDirectionExists

    def getCenterDirection(self):
        """
        Get centerDirection, which is optional.
        return centerDirection as Angle []
        raises ValueError If centerDirection does not exist.
        """
        if not self._centerDirectionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + centerDirection
                + " attribute in table SBSummary does not exist!"
            )

        return copy.deepcopy(self._centerDirection)

    def setCenterDirection(self, centerDirection):
        """
        Set centerDirection with the specified Angle []  value.
        centerDirection The Angle []  value to which centerDirection is to be set.
        The value of centerDirection can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(centerDirection, list):
            raise ValueError("The value of centerDirection must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(centerDirection)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of centerDirection is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(centerDirection, Angle):
                raise ValueError(
                    "type of the first value in centerDirection is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._centerDirection = copy.deepcopy(centerDirection)
        except Exception as exc:
            raise ValueError("Invalid centerDirection : " + str(exc))

        self._centerDirectionExists = True

    def clearCenterDirection(self):
        """
        Mark centerDirection, which is an optional field, as non-existent.
        """
        self._centerDirectionExists = False

    # ===> Attribute centerDirectionCode, which is optional
    _centerDirectionCodeExists = False

    _centerDirectionCode = DirectionReferenceCode.from_int(0)

    def isCenterDirectionCodeExists(self):
        """
        The attribute centerDirectionCode is optional. Return True if this attribute exists.
        return True if and only if the centerDirectionCode attribute exists.
        """
        return self._centerDirectionCodeExists

    def getCenterDirectionCode(self):
        """
        Get centerDirectionCode, which is optional.
        return centerDirectionCode as DirectionReferenceCode
        raises ValueError If centerDirectionCode does not exist.
        """
        if not self._centerDirectionCodeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + centerDirectionCode
                + " attribute in table SBSummary does not exist!"
            )

        return self._centerDirectionCode

    def setCenterDirectionCode(self, centerDirectionCode):
        """
        Set centerDirectionCode with the specified DirectionReferenceCode value.
        centerDirectionCode The DirectionReferenceCode value to which centerDirectionCode is to be set.


        """

        self._centerDirectionCode = DirectionReferenceCode(centerDirectionCode)

        self._centerDirectionCodeExists = True

    def clearCenterDirectionCode(self):
        """
        Mark centerDirectionCode, which is an optional field, as non-existent.
        """
        self._centerDirectionCodeExists = False

    # ===> Attribute centerDirectionEquinox, which is optional
    _centerDirectionEquinoxExists = False

    _centerDirectionEquinox = ArrayTime()

    def isCenterDirectionEquinoxExists(self):
        """
        The attribute centerDirectionEquinox is optional. Return True if this attribute exists.
        return True if and only if the centerDirectionEquinox attribute exists.
        """
        return self._centerDirectionEquinoxExists

    def getCenterDirectionEquinox(self):
        """
        Get centerDirectionEquinox, which is optional.
        return centerDirectionEquinox as ArrayTime
        raises ValueError If centerDirectionEquinox does not exist.
        """
        if not self._centerDirectionEquinoxExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + centerDirectionEquinox
                + " attribute in table SBSummary does not exist!"
            )

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._centerDirectionEquinox)

    def setCenterDirectionEquinox(self, centerDirectionEquinox):
        """
        Set centerDirectionEquinox with the specified ArrayTime value.
        centerDirectionEquinox The ArrayTime value to which centerDirectionEquinox is to be set.
        The value of centerDirectionEquinox can be anything allowed by the ArrayTime constructor.

        """

        self._centerDirectionEquinox = ArrayTime(centerDirectionEquinox)

        self._centerDirectionEquinoxExists = True

    def clearCenterDirectionEquinox(self):
        """
        Mark centerDirectionEquinox, which is an optional field, as non-existent.
        """
        self._centerDirectionEquinoxExists = False

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(
        self,
        sbSummaryUID,
        projectUID,
        obsUnitSetUID,
        frequency,
        frequencyBand,
        sbType,
        sbDuration,
        numObservingMode,
        observingMode,
        numberRepeats,
        numScienceGoal,
        scienceGoal,
        numWeatherConstraint,
        weatherConstraint,
    ):
        """
        Compare each attribute except the autoincrementable one of this SBSummaryRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # sbSummaryUID is a EntityRef, compare using the equals method.
        if not self._sbSummaryUID.equals(sbSummaryUID):
            return False

        # projectUID is a EntityRef, compare using the equals method.
        if not self._projectUID.equals(projectUID):
            return False

        # obsUnitSetUID is a EntityRef, compare using the equals method.
        if not self._obsUnitSetUID.equals(obsUnitSetUID):
            return False

        # frequency is a float, compare using the == operator.
        if not (self._frequency == frequency):
            return False

        # frequencyBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._frequencyBand.getValue() == frequencyBand.getValue()):
            return False

        # sbType is a SBType, compare using the == operator on the getValue() output
        if not (self._sbType.getValue() == sbType.getValue()):
            return False

        # sbDuration is a Interval, compare using the equals method.
        if not self._sbDuration.equals(sbDuration):
            return False

        # numObservingMode is a int, compare using the == operator.
        if not (self._numObservingMode == numObservingMode):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._observingMode) != len(observingMode):
            return False
        for indx in range(len(observingMode)):

            # observingMode is a list of str, compare using == operator.
            if not (self._observingMode[indx] == observingMode[indx]):
                return False

        # numberRepeats is a int, compare using the == operator.
        if not (self._numberRepeats == numberRepeats):
            return False

        # numScienceGoal is a int, compare using the == operator.
        if not (self._numScienceGoal == numScienceGoal):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._scienceGoal) != len(scienceGoal):
            return False
        for indx in range(len(scienceGoal)):

            # scienceGoal is a list of str, compare using == operator.
            if not (self._scienceGoal[indx] == scienceGoal[indx]):
                return False

        # numWeatherConstraint is a int, compare using the == operator.
        if not (self._numWeatherConstraint == numWeatherConstraint):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._weatherConstraint) != len(weatherConstraint):
            return False
        for indx in range(len(weatherConstraint)):

            # weatherConstraint is a list of str, compare using == operator.
            if not (self._weatherConstraint[indx] == weatherConstraint[indx]):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getSbSummaryUID(),
            otherRow.getProjectUID(),
            otherRow.getObsUnitSetUID(),
            otherRow.getFrequency(),
            otherRow.getFrequencyBand(),
            otherRow.getSbType(),
            otherRow.getSbDuration(),
            otherRow.getNumObservingMode(),
            otherRow.getObservingMode(),
            otherRow.getNumberRepeats(),
            otherRow.getNumScienceGoal(),
            otherRow.getScienceGoal(),
            otherRow.getNumWeatherConstraint(),
            otherRow.getWeatherConstraint(),
        )

    def compareRequiredValue(
        self,
        sbSummaryUID,
        projectUID,
        obsUnitSetUID,
        frequency,
        frequencyBand,
        sbType,
        sbDuration,
        numObservingMode,
        observingMode,
        numberRepeats,
        numScienceGoal,
        scienceGoal,
        numWeatherConstraint,
        weatherConstraint,
    ):

        # sbSummaryUID is a EntityRef, compare using the equals method.
        if not self._sbSummaryUID.equals(sbSummaryUID):
            return False

        # projectUID is a EntityRef, compare using the equals method.
        if not self._projectUID.equals(projectUID):
            return False

        # obsUnitSetUID is a EntityRef, compare using the equals method.
        if not self._obsUnitSetUID.equals(obsUnitSetUID):
            return False

        # frequency is a float, compare using the == operator.
        if not (self._frequency == frequency):
            return False

        # frequencyBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._frequencyBand.getValue() == frequencyBand.getValue()):
            return False

        # sbType is a SBType, compare using the == operator on the getValue() output
        if not (self._sbType.getValue() == sbType.getValue()):
            return False

        # sbDuration is a Interval, compare using the equals method.
        if not self._sbDuration.equals(sbDuration):
            return False

        # numObservingMode is a int, compare using the == operator.
        if not (self._numObservingMode == numObservingMode):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._observingMode) != len(observingMode):
            return False
        for indx in range(len(observingMode)):

            # observingMode is a list of str, compare using == operator.
            if not (self._observingMode[indx] == observingMode[indx]):
                return False

        # numberRepeats is a int, compare using the == operator.
        if not (self._numberRepeats == numberRepeats):
            return False

        # numScienceGoal is a int, compare using the == operator.
        if not (self._numScienceGoal == numScienceGoal):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._scienceGoal) != len(scienceGoal):
            return False
        for indx in range(len(scienceGoal)):

            # scienceGoal is a list of str, compare using == operator.
            if not (self._scienceGoal[indx] == scienceGoal[indx]):
                return False

        # numWeatherConstraint is a int, compare using the == operator.
        if not (self._numWeatherConstraint == numWeatherConstraint):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._weatherConstraint) != len(weatherConstraint):
            return False
        for indx in range(len(weatherConstraint)):

            # weatherConstraint is a list of str, compare using == operator.
            if not (self._weatherConstraint[indx] == weatherConstraint[indx]):
                return False

        return True


# initialize the dictionary that maps fields to init methods
SBSummaryRow.initFromBinMethods()
