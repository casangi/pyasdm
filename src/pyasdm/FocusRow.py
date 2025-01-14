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
# File FocusRow.py
#

import pyasdm.FocusTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from xml.dom import minidom

import copy


class FocusRow:
    """
    The FocusRow class is a row of a FocusTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a FocusRow.
        When row is None, create an empty row attached to table, which must be a FocusTable.
        When row is given, copy those values in to the new row. The row argument must be a FocusRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.FocusTable):
            raise ValueError("table must be a FocusTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._timeInterval = ArrayTimeInterval()

        self._focusTracking = None

        self._focusOffset = []  # this is a list of Length []

        self._focusRotationOffset = []  # this is a list of Angle []

        self._measuredFocusPositionExists = False

        self._measuredFocusPosition = []  # this is a list of Length []

        self._measuredFocusRotationExists = False

        self._measuredFocusRotation = []  # this is a list of Angle []

        # extrinsic attributes

        self._antennaId = Tag()

        self._focusModelId = 0

        if row is not None:
            if not isinstance(row, FocusRow):
                raise ValueError("row must be a FocusRow")

            # copy constructor

            self._antennaId = Tag(row._antennaId)

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._focusTracking = row._focusTracking

            # focusOffset is a  list , make a deep copy
            self._focusOffset = copy.deepcopy(row._focusOffset)

            # focusRotationOffset is a  list , make a deep copy
            self._focusRotationOffset = copy.deepcopy(row._focusRotationOffset)

            self._focusModelId = row._focusModelId

            # by default set systematically measuredFocusPosition's value to something not None

            if row._measuredFocusPositionExists:

                # measuredFocusPosition is a list, make a deep copy
                self.measuredFocusPosition = copy.deepcopy(row.measuredFocusPosition)

                self._measuredFocusPositionExists = True

            # by default set systematically measuredFocusRotation's value to something not None

            if row._measuredFocusRotationExists:

                # measuredFocusRotation is a list, make a deep copy
                self.measuredFocusRotation = copy.deepcopy(row.measuredFocusRotation)

                self._measuredFocusRotationExists = True

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

        result += Parser.extendedValueToXML("timeInterval", self._timeInterval)

        result += Parser.valueToXML("focusTracking", self._focusTracking)

        result += Parser.listExtendedValueToXML("focusOffset", self._focusOffset)

        result += Parser.listExtendedValueToXML(
            "focusRotationOffset", self._focusRotationOffset
        )

        if self._measuredFocusPositionExists:

            result += Parser.listExtendedValueToXML(
                "measuredFocusPosition", self._measuredFocusPosition
            )

        if self._measuredFocusRotationExists:

            result += Parser.listExtendedValueToXML(
                "measuredFocusRotation", self._measuredFocusRotation
            )

        # extrinsic attributes

        result += Parser.extendedValueToXML("antennaId", self._antennaId)

        result += Parser.valueToXML("focusModelId", self._focusModelId)

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
                "xmlrow is not a string or a minidom.Element", "FocusTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "FocusTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        focusTrackingNode = rowdom.getElementsByTagName("focusTracking")[0]

        self._focusTracking = bool(focusTrackingNode.firstChild.data.strip())

        focusOffsetNode = rowdom.getElementsByTagName("focusOffset")[0]

        focusOffsetStr = focusOffsetNode.firstChild.data.strip()

        self._focusOffset = Parser.stringListToLists(
            focusOffsetStr, Length, "Focus", True
        )

        focusRotationOffsetNode = rowdom.getElementsByTagName("focusRotationOffset")[0]

        focusRotationOffsetStr = focusRotationOffsetNode.firstChild.data.strip()

        self._focusRotationOffset = Parser.stringListToLists(
            focusRotationOffsetStr, Angle, "Focus", True
        )

        measuredFocusPositionNode = rowdom.getElementsByTagName("measuredFocusPosition")
        if len(measuredFocusPositionNode) > 0:

            measuredFocusPositionStr = measuredFocusPositionNode[
                0
            ].firstChild.data.strip()

            self._measuredFocusPosition = Parser.stringListToLists(
                measuredFocusPositionStr, Length, "Focus", True
            )

            self._measuredFocusPositionExists = True

        measuredFocusRotationNode = rowdom.getElementsByTagName("measuredFocusRotation")
        if len(measuredFocusRotationNode) > 0:

            measuredFocusRotationStr = measuredFocusRotationNode[
                0
            ].firstChild.data.strip()

            self._measuredFocusRotation = Parser.stringListToLists(
                measuredFocusRotationStr, Angle, "Focus", True
            )

            self._measuredFocusRotationExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        self._antennaId = Tag(antennaIdNode.firstChild.data.strip())

        focusModelIdNode = rowdom.getElementsByTagName("focusModelId")[0]

        self._focusModelId = int(focusModelIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._antennaId.toBin(eos)

        self._timeInterval.toBin(eos)

        eos.writeBool(self._focusTracking)

        Length.listToBin(self._focusOffset, eos)

        Angle.listToBin(self._focusRotationOffset, eos)

        eos.writeInt(self._focusModelId)

        eos.writeBool(self._measuredFocusPositionExists)
        if self._measuredFocusPositionExists:

            Length.listToBin(self._measuredFocusPosition, eos)

        eos.writeBool(self._measuredFocusRotationExists)
        if self._measuredFocusRotationExists:

            Angle.listToBin(self._measuredFocusRotation, eos)

    @staticmethod
    def antennaIdFromBin(row, eis):
        """
        Set the antennaId in row from the EndianInput (eis) instance.
        """

        row._antennaId = Tag.fromBin(eis)

    @staticmethod
    def timeIntervalFromBin(row, eis):
        """
        Set the timeInterval in row from the EndianInput (eis) instance.
        """

        row._timeInterval = ArrayTimeInterval.fromBin(eis)

    @staticmethod
    def focusTrackingFromBin(row, eis):
        """
        Set the focusTracking in row from the EndianInput (eis) instance.
        """

        row._focusTracking = eis.readBool()

    @staticmethod
    def focusOffsetFromBin(row, eis):
        """
        Set the focusOffset in row from the EndianInput (eis) instance.
        """

        row._focusOffset = Length.from1DBin(eis)

    @staticmethod
    def focusRotationOffsetFromBin(row, eis):
        """
        Set the focusRotationOffset in row from the EndianInput (eis) instance.
        """

        row._focusRotationOffset = Angle.from1DBin(eis)

    @staticmethod
    def focusModelIdFromBin(row, eis):
        """
        Set the focusModelId in row from the EndianInput (eis) instance.
        """

        row._focusModelId = eis.readInt()

    @staticmethod
    def measuredFocusPositionFromBin(row, eis):
        """
        Set the optional measuredFocusPosition in row from the EndianInput (eis) instance.
        """
        row._measuredFocusPositionExists = eis.readBool()
        if row._measuredFocusPositionExists:

            row._measuredFocusPosition = Length.from1DBin(eis)

    @staticmethod
    def measuredFocusRotationFromBin(row, eis):
        """
        Set the optional measuredFocusRotation in row from the EndianInput (eis) instance.
        """
        row._measuredFocusRotationExists = eis.readBool()
        if row._measuredFocusRotationExists:

            row._measuredFocusRotation = Angle.from1DBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaId"] = FocusRow.antennaIdFromBin
        _fromBinMethods["timeInterval"] = FocusRow.timeIntervalFromBin
        _fromBinMethods["focusTracking"] = FocusRow.focusTrackingFromBin
        _fromBinMethods["focusOffset"] = FocusRow.focusOffsetFromBin
        _fromBinMethods["focusRotationOffset"] = FocusRow.focusRotationOffsetFromBin
        _fromBinMethods["focusModelId"] = FocusRow.focusModelIdFromBin

        _fromBinMethods["measuredFocusPosition"] = FocusRow.measuredFocusPositionFromBin
        _fromBinMethods["measuredFocusRotation"] = FocusRow.measuredFocusRotationFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = FocusRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Focus",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute timeInterval

    _timeInterval = ArrayTimeInterval()

    def getTimeInterval(self):
        """
        Get timeInterval.
        return timeInterval as ArrayTimeInterval
        """

        # make sure it is a copy of ArrayTimeInterval
        return ArrayTimeInterval(self._timeInterval)

    def setTimeInterval(self, timeInterval):
        """
        Set timeInterval with the specified ArrayTimeInterval value.
        timeInterval The ArrayTimeInterval value to which timeInterval is to be set.
        The value of timeInterval can be anything allowed by the ArrayTimeInterval constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the timeInterval field, which is part of the key, after this row has been added to this table."
            )

        self._timeInterval = ArrayTimeInterval(timeInterval)

    # ===> Attribute focusTracking

    _focusTracking = None

    def getFocusTracking(self):
        """
        Get focusTracking.
        return focusTracking as bool
        """

        return self._focusTracking

    def setFocusTracking(self, focusTracking):
        """
        Set focusTracking with the specified bool value.
        focusTracking The bool value to which focusTracking is to be set.


        """

        self._focusTracking = bool(focusTracking)

    # ===> Attribute focusOffset

    _focusOffset = None  # this is a 1D list of Length

    def getFocusOffset(self):
        """
        Get focusOffset.
        return focusOffset as Length []
        """

        return copy.deepcopy(self._focusOffset)

    def setFocusOffset(self, focusOffset):
        """
        Set focusOffset with the specified Length []  value.
        focusOffset The Length []  value to which focusOffset is to be set.
        The value of focusOffset can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(focusOffset, list):
            raise ValueError("The value of focusOffset must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(focusOffset)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of focusOffset is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(focusOffset, Length):
                raise ValueError(
                    "type of the first value in focusOffset is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._focusOffset = copy.deepcopy(focusOffset)
        except Exception as exc:
            raise ValueError("Invalid focusOffset : " + str(exc))

    # ===> Attribute focusRotationOffset

    _focusRotationOffset = None  # this is a 1D list of Angle

    def getFocusRotationOffset(self):
        """
        Get focusRotationOffset.
        return focusRotationOffset as Angle []
        """

        return copy.deepcopy(self._focusRotationOffset)

    def setFocusRotationOffset(self, focusRotationOffset):
        """
        Set focusRotationOffset with the specified Angle []  value.
        focusRotationOffset The Angle []  value to which focusRotationOffset is to be set.
        The value of focusRotationOffset can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(focusRotationOffset, list):
            raise ValueError("The value of focusRotationOffset must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(focusRotationOffset)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of focusRotationOffset is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(focusRotationOffset, Angle):
                raise ValueError(
                    "type of the first value in focusRotationOffset is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._focusRotationOffset = copy.deepcopy(focusRotationOffset)
        except Exception as exc:
            raise ValueError("Invalid focusRotationOffset : " + str(exc))

    # ===> Attribute measuredFocusPosition, which is optional
    _measuredFocusPositionExists = False

    _measuredFocusPosition = None  # this is a 1D list of Length

    def isMeasuredFocusPositionExists(self):
        """
        The attribute measuredFocusPosition is optional. Return True if this attribute exists.
        return True if and only if the measuredFocusPosition attribute exists.
        """
        return self._measuredFocusPositionExists

    def getMeasuredFocusPosition(self):
        """
        Get measuredFocusPosition, which is optional.
        return measuredFocusPosition as Length []
        raises ValueError If measuredFocusPosition does not exist.
        """
        if not self._measuredFocusPositionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + measuredFocusPosition
                + " attribute in table Focus does not exist!"
            )

        return copy.deepcopy(self._measuredFocusPosition)

    def setMeasuredFocusPosition(self, measuredFocusPosition):
        """
        Set measuredFocusPosition with the specified Length []  value.
        measuredFocusPosition The Length []  value to which measuredFocusPosition is to be set.
        The value of measuredFocusPosition can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(measuredFocusPosition, list):
            raise ValueError("The value of measuredFocusPosition must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(measuredFocusPosition)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of measuredFocusPosition is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(measuredFocusPosition, Length):
                raise ValueError(
                    "type of the first value in measuredFocusPosition is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._measuredFocusPosition = copy.deepcopy(measuredFocusPosition)
        except Exception as exc:
            raise ValueError("Invalid measuredFocusPosition : " + str(exc))

        self._measuredFocusPositionExists = True

    def clearMeasuredFocusPosition(self):
        """
        Mark measuredFocusPosition, which is an optional field, as non-existent.
        """
        self._measuredFocusPositionExists = False

    # ===> Attribute measuredFocusRotation, which is optional
    _measuredFocusRotationExists = False

    _measuredFocusRotation = None  # this is a 1D list of Angle

    def isMeasuredFocusRotationExists(self):
        """
        The attribute measuredFocusRotation is optional. Return True if this attribute exists.
        return True if and only if the measuredFocusRotation attribute exists.
        """
        return self._measuredFocusRotationExists

    def getMeasuredFocusRotation(self):
        """
        Get measuredFocusRotation, which is optional.
        return measuredFocusRotation as Angle []
        raises ValueError If measuredFocusRotation does not exist.
        """
        if not self._measuredFocusRotationExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + measuredFocusRotation
                + " attribute in table Focus does not exist!"
            )

        return copy.deepcopy(self._measuredFocusRotation)

    def setMeasuredFocusRotation(self, measuredFocusRotation):
        """
        Set measuredFocusRotation with the specified Angle []  value.
        measuredFocusRotation The Angle []  value to which measuredFocusRotation is to be set.
        The value of measuredFocusRotation can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(measuredFocusRotation, list):
            raise ValueError("The value of measuredFocusRotation must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(measuredFocusRotation)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of measuredFocusRotation is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(measuredFocusRotation, Angle):
                raise ValueError(
                    "type of the first value in measuredFocusRotation is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._measuredFocusRotation = copy.deepcopy(measuredFocusRotation)
        except Exception as exc:
            raise ValueError("Invalid measuredFocusRotation : " + str(exc))

        self._measuredFocusRotationExists = True

    def clearMeasuredFocusRotation(self):
        """
        Mark measuredFocusRotation, which is an optional field, as non-existent.
        """
        self._measuredFocusRotationExists = False

    # Extrinsic Table Attributes

    # ===> Attribute antennaId

    _antennaId = Tag()

    def getAntennaId(self):
        """
        Get antennaId.
        return antennaId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._antennaId)

    def setAntennaId(self, antennaId):
        """
        Set antennaId with the specified Tag value.
        antennaId The Tag value to which antennaId is to be set.
        The value of antennaId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the antennaId field, which is part of the key, after this row has been added to this table."
            )

        self._antennaId = Tag(antennaId)

    # ===> Attribute focusModelId

    _focusModelId = 0

    def getFocusModelId(self):
        """
        Get focusModelId.
        return focusModelId as int
        """

        return self._focusModelId

    def setFocusModelId(self, focusModelId):
        """
        Set focusModelId with the specified int value.
        focusModelId The int value to which focusModelId is to be set.


        """

        self._focusModelId = int(focusModelId)

    # Links

    def getAntennaUsingAntennaId(self):
        """
        Returns the row in the Antenna table having Antenna.antennaId == antennaId

        """

        return self._table.getContainer().getAntenna().getRowByKey(self._antennaId)

    # ===> Slice link from a row of Focus table to a collection of row of FocusModel table.
    def getFocusModels(self):
        """
        Get the collection of rows in the FocusModel table having focusModelId == this.focusModelId
        """

        return (
            self._table.getContainer()
            .getFocusModel()
            .getRowByFocusModelId(self._focusModelId)
        )

    # comparison methods

    def compareNoAutoInc(
        self,
        antennaId,
        timeInterval,
        focusTracking,
        focusOffset,
        focusRotationOffset,
        focusModelId,
    ):
        """
        Compare each attribute except the autoincrementable one of this FocusRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaId is a Tag, compare using the equals method.
        if not self._antennaId.equals(antennaId):
            return False

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # focusTracking is a bool, compare using the == operator.
        if not (self._focusTracking == focusTracking):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._focusOffset) != len(focusOffset):
            return False
        for indx in range(len(focusOffset)):

            # focusOffset is a list of Length, compare using the almostEquals method.
            if not self._focusOffset[indx].almostEquals(
                focusOffset[indx], self.getTable().getFocusOffsetEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._focusRotationOffset) != len(focusRotationOffset):
            return False
        for indx in range(len(focusRotationOffset)):

            # focusRotationOffset is a list of Angle, compare using the almostEquals method.
            if not self._focusRotationOffset[indx].almostEquals(
                focusRotationOffset[indx],
                self.getTable().getFocusRotationOffsetEqTolerance(),
            ):
                return False

        # focusModelId is a int, compare using the == operator.
        if not (self._focusModelId == focusModelId):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getFocusTracking(),
            otherRow.getFocusOffset(),
            otherRow.getFocusRotationOffset(),
            otherRow.getFocusModelId(),
        )

    def compareRequiredValue(
        self, focusTracking, focusOffset, focusRotationOffset, focusModelId
    ):

        # focusTracking is a bool, compare using the == operator.
        if not (self._focusTracking == focusTracking):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._focusOffset) != len(focusOffset):
            return False
        for indx in range(len(focusOffset)):

            # focusOffset is a list of Length, compare using the almostEquals method.
            if not self._focusOffset[indx].almostEquals(
                focusOffset[indx], self.getTable().getFocusOffsetEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._focusRotationOffset) != len(focusRotationOffset):
            return False
        for indx in range(len(focusRotationOffset)):

            # focusRotationOffset is a list of Angle, compare using the almostEquals method.
            if not self._focusRotationOffset[indx].almostEquals(
                focusRotationOffset[indx],
                self.getTable().getFocusRotationOffsetEqTolerance(),
            ):
                return False

        # focusModelId is a int, compare using the == operator.
        if not (self._focusModelId == focusModelId):
            return False

        return True


# initialize the dictionary that maps fields to init methods
FocusRow.initFromBinMethods()
