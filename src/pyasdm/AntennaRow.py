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
# File AntennaRow.py
#

import pyasdm.AntennaTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.AntennaMake import AntennaMake


from pyasdm.enumerations.AntennaType import AntennaType


from xml.dom import minidom

import copy


class AntennaRow:
    """
    The AntennaRow class is a row of a AntennaTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a AntennaRow.
        When row is None, create an empty row attached to table, which must be a AntennaTable.
        When row is given, copy those values in to the new row. The row argument must be a AntennaRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.AntennaTable):
            raise ValueError("table must be a AntennaTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._antennaId = Tag()

        self._name = None

        self._antennaMake = AntennaMake.from_int(0)

        self._antennaType = AntennaType.from_int(0)

        self._dishDiameter = Length()

        self._position = []  # this is a list of Length []

        self._offset = []  # this is a list of Length []

        self._time = ArrayTime()

        # extrinsic attributes

        self._assocAntennaIdExists = False

        self._assocAntennaId = Tag()

        self._stationId = Tag()

        if row is not None:
            if not isinstance(row, AntennaRow):
                raise ValueError("row must be a AntennaRow")

            # copy constructor

            self._antennaId = Tag(row._antennaId)

            self._name = row._name

            # We force the attribute of the result to be not None
            if row._antennaMake is None:
                self._antennaMake = AntennaMake.from_int(0)
            else:
                self._antennaMake = AntennaMake(row._antennaMake)

            # We force the attribute of the result to be not None
            if row._antennaType is None:
                self._antennaType = AntennaType.from_int(0)
            else:
                self._antennaType = AntennaType(row._antennaType)

            self._dishDiameter = Length(row._dishDiameter)

            # position is a  list , make a deep copy
            self._position = copy.deepcopy(row._position)

            # offset is a  list , make a deep copy
            self._offset = copy.deepcopy(row._offset)

            self._time = ArrayTime(row._time)

            self._stationId = Tag(row._stationId)

            # by default set systematically assocAntennaId's value to something not None

            if row._assocAntennaIdExists:

                self._assocAntennaId = Tag(row._assocAntennaId)

                self._assocAntennaIdExists = True

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

        result += Parser.extendedValueToXML("antennaId", self._antennaId)

        result += Parser.valueToXML("name", self._name)

        result += Parser.valueToXML("antennaMake", AntennaMake.name(self._antennaMake))

        result += Parser.valueToXML("antennaType", AntennaType.name(self._antennaType))

        result += Parser.extendedValueToXML("dishDiameter", self._dishDiameter)

        result += Parser.listExtendedValueToXML("position", self._position)

        result += Parser.listExtendedValueToXML("offset", self._offset)

        result += Parser.extendedValueToXML("time", self._time)

        # extrinsic attributes

        if self._assocAntennaIdExists:

            result += Parser.extendedValueToXML("assocAntennaId", self._assocAntennaId)

        result += Parser.extendedValueToXML("stationId", self._stationId)

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
                "xmlrow is not a string or a minidom.Element", "AntennaTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "AntennaTable")

        # intrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        self._antennaId = Tag(antennaIdNode.firstChild.data.strip())

        nameNode = rowdom.getElementsByTagName("name")[0]

        self._name = str(nameNode.firstChild.data.strip())

        antennaMakeNode = rowdom.getElementsByTagName("antennaMake")[0]

        self._antennaMake = AntennaMake.newAntennaMake(
            antennaMakeNode.firstChild.data.strip()
        )

        antennaTypeNode = rowdom.getElementsByTagName("antennaType")[0]

        self._antennaType = AntennaType.newAntennaType(
            antennaTypeNode.firstChild.data.strip()
        )

        dishDiameterNode = rowdom.getElementsByTagName("dishDiameter")[0]

        self._dishDiameter = Length(dishDiameterNode.firstChild.data.strip())

        positionNode = rowdom.getElementsByTagName("position")[0]

        positionStr = positionNode.firstChild.data.strip()

        self._position = Parser.stringListToLists(positionStr, Length, "Antenna", True)

        offsetNode = rowdom.getElementsByTagName("offset")[0]

        offsetStr = offsetNode.firstChild.data.strip()

        self._offset = Parser.stringListToLists(offsetStr, Length, "Antenna", True)

        timeNode = rowdom.getElementsByTagName("time")[0]

        self._time = ArrayTime(timeNode.firstChild.data.strip())

        # extrinsic attribute values

        assocAntennaIdNode = rowdom.getElementsByTagName("assocAntennaId")
        if len(assocAntennaIdNode) > 0:

            self._assocAntennaId = Tag(assocAntennaIdNode[0].firstChild.data.strip())

            self._assocAntennaIdExists = True

        stationIdNode = rowdom.getElementsByTagName("stationId")[0]

        self._stationId = Tag(stationIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._antennaId.toBin(eos)

        eos.writeStr(self._name)

        eos.writeString(self._antennaMake.toString())

        eos.writeString(self._antennaType.toString())

        self._dishDiameter.toBin(eos)

        Length.listToBin(self._position, eos)

        Length.listToBin(self._offset, eos)

        self._time.toBin(eos)

        self._stationId.toBin(eos)

        eos.writeBool(self._assocAntennaIdExists)
        if self._assocAntennaIdExists:

            self._assocAntennaId.toBin(eos)

    @staticmethod
    def antennaIdFromBin(row, eis):
        """
        Set the antennaId in row from the EndianInput (eis) instance.
        """

        row._antennaId = Tag.fromBin(eis)

    @staticmethod
    def nameFromBin(row, eis):
        """
        Set the name in row from the EndianInput (eis) instance.
        """

        row._name = eis.readStr()

    @staticmethod
    def antennaMakeFromBin(row, eis):
        """
        Set the antennaMake in row from the EndianInput (eis) instance.
        """

        row._antennaMake = AntennaMake.from_int(eis.readInt())

    @staticmethod
    def antennaTypeFromBin(row, eis):
        """
        Set the antennaType in row from the EndianInput (eis) instance.
        """

        row._antennaType = AntennaType.from_int(eis.readInt())

    @staticmethod
    def dishDiameterFromBin(row, eis):
        """
        Set the dishDiameter in row from the EndianInput (eis) instance.
        """

        row._dishDiameter = Length.fromBin(eis)

    @staticmethod
    def positionFromBin(row, eis):
        """
        Set the position in row from the EndianInput (eis) instance.
        """

        row._position = Length.from1DBin(eis)

    @staticmethod
    def offsetFromBin(row, eis):
        """
        Set the offset in row from the EndianInput (eis) instance.
        """

        row._offset = Length.from1DBin(eis)

    @staticmethod
    def timeFromBin(row, eis):
        """
        Set the time in row from the EndianInput (eis) instance.
        """

        row._time = ArrayTime.fromBin(eis)

    @staticmethod
    def stationIdFromBin(row, eis):
        """
        Set the stationId in row from the EndianInput (eis) instance.
        """

        row._stationId = Tag.fromBin(eis)

    @staticmethod
    def assocAntennaIdFromBin(row, eis):
        """
        Set the optional assocAntennaId in row from the EndianInput (eis) instance.
        """
        row._assocAntennaIdExists = eis.readBool()
        if row._assocAntennaIdExists:

            row._assocAntennaId = Tag.fromBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaId"] = AntennaRow.antennaIdFromBin
        _fromBinMethods["name"] = AntennaRow.nameFromBin
        _fromBinMethods["antennaMake"] = AntennaRow.antennaMakeFromBin
        _fromBinMethods["antennaType"] = AntennaRow.antennaTypeFromBin
        _fromBinMethods["dishDiameter"] = AntennaRow.dishDiameterFromBin
        _fromBinMethods["position"] = AntennaRow.positionFromBin
        _fromBinMethods["offset"] = AntennaRow.offsetFromBin
        _fromBinMethods["time"] = AntennaRow.timeFromBin
        _fromBinMethods["stationId"] = AntennaRow.stationIdFromBin

        _fromBinMethods["assocAntennaId"] = AntennaRow.assocAntennaIdFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = AntennaRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Antenna",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

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

    # ===> Attribute name

    _name = None

    def getName(self):
        """
        Get name.
        return name as str
        """

        return self._name

    def setName(self, name):
        """
        Set name with the specified str value.
        name The str value to which name is to be set.


        """

        self._name = str(name)

    # ===> Attribute antennaMake

    _antennaMake = AntennaMake.from_int(0)

    def getAntennaMake(self):
        """
        Get antennaMake.
        return antennaMake as AntennaMake
        """

        return self._antennaMake

    def setAntennaMake(self, antennaMake):
        """
        Set antennaMake with the specified AntennaMake value.
        antennaMake The AntennaMake value to which antennaMake is to be set.


        """

        self._antennaMake = AntennaMake(antennaMake)

    # ===> Attribute antennaType

    _antennaType = AntennaType.from_int(0)

    def getAntennaType(self):
        """
        Get antennaType.
        return antennaType as AntennaType
        """

        return self._antennaType

    def setAntennaType(self, antennaType):
        """
        Set antennaType with the specified AntennaType value.
        antennaType The AntennaType value to which antennaType is to be set.


        """

        self._antennaType = AntennaType(antennaType)

    # ===> Attribute dishDiameter

    _dishDiameter = Length()

    def getDishDiameter(self):
        """
        Get dishDiameter.
        return dishDiameter as Length
        """

        # make sure it is a copy of Length
        return Length(self._dishDiameter)

    def setDishDiameter(self, dishDiameter):
        """
        Set dishDiameter with the specified Length value.
        dishDiameter The Length value to which dishDiameter is to be set.
        The value of dishDiameter can be anything allowed by the Length constructor.

        """

        self._dishDiameter = Length(dishDiameter)

    # ===> Attribute position

    _position = None  # this is a 1D list of Length

    def getPosition(self):
        """
        Get position.
        return position as Length []
        """

        return copy.deepcopy(self._position)

    def setPosition(self, position):
        """
        Set position with the specified Length []  value.
        position The Length []  value to which position is to be set.
        The value of position can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(position, list):
            raise ValueError("The value of position must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(position)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of position is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(position, Length):
                raise ValueError(
                    "type of the first value in position is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._position = copy.deepcopy(position)
        except Exception as exc:
            raise ValueError("Invalid position : " + str(exc))

    # ===> Attribute offset

    _offset = None  # this is a 1D list of Length

    def getOffset(self):
        """
        Get offset.
        return offset as Length []
        """

        return copy.deepcopy(self._offset)

    def setOffset(self, offset):
        """
        Set offset with the specified Length []  value.
        offset The Length []  value to which offset is to be set.
        The value of offset can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(offset, list):
            raise ValueError("The value of offset must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(offset)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of offset is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(offset, Length):
                raise ValueError(
                    "type of the first value in offset is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._offset = copy.deepcopy(offset)
        except Exception as exc:
            raise ValueError("Invalid offset : " + str(exc))

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

        """

        self._time = ArrayTime(time)

    # Extrinsic Table Attributes

    # ===> Attribute assocAntennaId, which is optional
    _assocAntennaIdExists = False

    _assocAntennaId = Tag()

    def isAssocAntennaIdExists(self):
        """
        The attribute assocAntennaId is optional. Return True if this attribute exists.
        return True if and only if the assocAntennaId attribute exists.
        """
        return self._assocAntennaIdExists

    def getAssocAntennaId(self):
        """
        Get assocAntennaId, which is optional.
        return assocAntennaId as Tag
        raises ValueError If assocAntennaId does not exist.
        """
        if not self._assocAntennaIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + assocAntennaId
                + " attribute in table Antenna does not exist!"
            )

        # make sure it is a copy of Tag
        return Tag(self._assocAntennaId)

    def setAssocAntennaId(self, assocAntennaId):
        """
        Set assocAntennaId with the specified Tag value.
        assocAntennaId The Tag value to which assocAntennaId is to be set.
        The value of assocAntennaId can be anything allowed by the Tag constructor.

        """

        self._assocAntennaId = Tag(assocAntennaId)

        self._assocAntennaIdExists = True

    def clearAssocAntennaId(self):
        """
        Mark assocAntennaId, which is an optional field, as non-existent.
        """
        self._assocAntennaIdExists = False

    # ===> Attribute stationId

    _stationId = Tag()

    def getStationId(self):
        """
        Get stationId.
        return stationId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._stationId)

    def setStationId(self, stationId):
        """
        Set stationId with the specified Tag value.
        stationId The Tag value to which stationId is to be set.
        The value of stationId can be anything allowed by the Tag constructor.

        """

        self._stationId = Tag(stationId)

    # Links

    # ===> Optional link from a row of Antenna table to a row of Antenna table.

    def isAssociatedAntennaExists(self):
        """
        The link to table Antenna is optional. Return True if this link exists.
        """
        return self._assocAntennaIdExists

    def getAssociatedAntenna(self):
        """
        Get the optional row in table Antenna by traversing the defined link to that table.
        return A row in Antenna table.
        raises NoSuchRow if there is no such row in table Antenna or the link does not exist.
        """

        if not self._assocAntennaIdExists:
            raise NoSuchRow("Antenna", "Antenna", True)

        return self._table.getContainer().getAntenna().getRowByKey(antennaId)

    def setAssociatedAntennaLink(self, AssocAntennaId):
        """
        Set the values of the link attributes needed to link this row to a row in table Antenna.
        """

        self._assocAntennaId = assocAntennaId
        self._assocAntennaIdExists = True

    def getStationUsingStationId(self):
        """
        Returns the row in the Station table having Station.stationId == stationId

        """

        return self._table.getContainer().getStation().getRowByKey(self._stationId)

    # comparison methods

    def compareNoAutoInc(
        self,
        name,
        antennaMake,
        antennaType,
        dishDiameter,
        position,
        offset,
        time,
        stationId,
    ):
        """
        Compare each attribute except the autoincrementable one of this AntennaRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # name is a str, compare using the == operator.
        if not (self._name == name):
            return False

        # antennaMake is a AntennaMake, compare using the == operator on the getValue() output
        if not (self._antennaMake.getValue() == antennaMake.getValue()):
            return False

        # antennaType is a AntennaType, compare using the == operator on the getValue() output
        if not (self._antennaType.getValue() == antennaType.getValue()):
            return False

        # dishDiameter is a Length, compare using the almostEquals method.
        if not self._dishDiameter.almostEquals(
            dishDiameter, self.getTable().getDishDiameterEqTolerance()
        ):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._position) != len(position):
            return False
        for indx in range(len(position)):

            # position is a list of Length, compare using the almostEquals method.
            if not self._position[indx].almostEquals(
                position[indx], self.getTable().getPositionEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._offset) != len(offset):
            return False
        for indx in range(len(offset)):

            # offset is a list of Length, compare using the almostEquals method.
            if not self._offset[indx].almostEquals(
                offset[indx], self.getTable().getOffsetEqTolerance()
            ):
                return False

        # time is a ArrayTime, compare using the equals method.
        if not self._time.equals(time):
            return False

        # stationId is a Tag, compare using the equals method.
        if not self._stationId.equals(stationId):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getName(),
            otherRow.getAntennaMake(),
            otherRow.getAntennaType(),
            otherRow.getDishDiameter(),
            otherRow.getPosition(),
            otherRow.getOffset(),
            otherRow.getTime(),
            otherRow.getStationId(),
        )

    def compareRequiredValue(
        self,
        name,
        antennaMake,
        antennaType,
        dishDiameter,
        position,
        offset,
        time,
        stationId,
    ):

        # name is a str, compare using the == operator.
        if not (self._name == name):
            return False

        # antennaMake is a AntennaMake, compare using the == operator on the getValue() output
        if not (self._antennaMake.getValue() == antennaMake.getValue()):
            return False

        # antennaType is a AntennaType, compare using the == operator on the getValue() output
        if not (self._antennaType.getValue() == antennaType.getValue()):
            return False

        # dishDiameter is a Length, compare using the almostEquals method.
        if not self._dishDiameter.almostEquals(
            dishDiameter, self.getTable().getDishDiameterEqTolerance()
        ):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._position) != len(position):
            return False
        for indx in range(len(position)):

            # position is a list of Length, compare using the almostEquals method.
            if not self._position[indx].almostEquals(
                position[indx], self.getTable().getPositionEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._offset) != len(offset):
            return False
        for indx in range(len(offset)):

            # offset is a list of Length, compare using the almostEquals method.
            if not self._offset[indx].almostEquals(
                offset[indx], self.getTable().getOffsetEqTolerance()
            ):
                return False

        # time is a ArrayTime, compare using the equals method.
        if not self._time.equals(time):
            return False

        # stationId is a Tag, compare using the equals method.
        if not self._stationId.equals(stationId):
            return False

        return True


# initialize the dictionary that maps fields to init methods
AntennaRow.initFromBinMethods()
