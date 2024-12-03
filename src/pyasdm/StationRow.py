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
# File StationRow.py
#

import pyasdm.StationTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.StationType import StationType


from xml.dom import minidom

import copy


class StationRow:
    """
    The StationRow class is a row of a StationTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a StationRow.
        When row is None, create an empty row attached to table, which must be a StationTable.
        When row is given, copy those values in to the new row. The row argument must be a StationRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.StationTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._type = StationType.from_int(0)

        if row is not None:
            if not isinstance(row, StationRow):
                raise ValueError("row must be a MainRow")

            self._stationId = Tag(row._stationId)

            self._name = row._name

            # position is a  list , make a deep copy
            self._position = copy.deepcopy(row._position)

            # We force the attribute of the result to be not None
            if row._type is None:
                self._type = StationType.from_int(0)
            else:
                self._type = StationType(row._type)

            # by default set systematically time's value to something not None

            if row._timeExists:

                self._time = ArrayTime(row._time)

                self._timeExists = True

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

        result += Parser.extendedValueToXML("stationId", self._stationId)

        result += Parser.valueToXML("name", self._name)

        result += Parser.listExtendedValueToXML("position", self._position)

        result += Parser.valueToXML("type", StationType.name(self._type))

        if self._timeExists:

            result += Parser.extendedValueToXML("time", self._time)

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
                "xmlrow is not a string or a minidom.Element", "StationTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "StationTable")

        # intrinsic attribute values

        stationIdNode = rowdom.getElementsByTagName("stationId")[0]

        self._stationId = Tag(stationIdNode.firstChild.data)

        nameNode = rowdom.getElementsByTagName("name")[0]

        self._name = str(nameNode.firstChild.data)

        positionNode = rowdom.getElementsByTagName("position")[0]

        positionStr = positionNode.firstChild.data
        self._position = Parser.stringListToLists(positionStr, Length, "Station")

        typeNode = rowdom.getElementsByTagName("type")[0]

        self._type = StationType.newStationType(typeNode.firstChild.data)

        timeNode = rowdom.getElementsByTagName("time")
        if len(timeNode) > 0:

            self._time = ArrayTime(timeNode[0].firstChild.data)

            self._timeExists = True

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

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

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the stationId field, which is part of the key, after this row has been added to this table."
            )

        self._stationId = Tag(stationId)

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

    # ===> Attribute type

    _type = StationType.from_int(0)

    def getType(self):
        """
        Get type.
        return type as StationType
        """

        return self._type

    def setType(self, type):
        """
        Set type with the specified StationType value.
        type The StationType value to which type is to be set.


        """

        self._type = StationType(type)

    # ===> Attribute time, which is optional
    _timeExists = False

    _time = ArrayTime()

    def isTimeExists(self):
        """
        The attribute time is optional. Return True if this attribute exists.
        return True if and only if the time attribute exists.
        """
        return self._timeExists

    def getTime(self):
        """
        Get time, which is optional.
        return time as ArrayTime
        raises ValueError If time does not exist.
        """
        if not self._timeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + time
                + " attribute in table Station does not exist!"
            )

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._time)

    def setTime(self, time):
        """
        Set time with the specified ArrayTime value.
        time The ArrayTime value to which time is to be set.
        The value of time can be anything allowed by the ArrayTime constructor.

        """

        self._time = ArrayTime(time)

        self._timeExists = True

    def clearTime(self):
        """
        Mark time, which is an optional field, as non-existent.
        """
        self._timeExists = False

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(self, name, position, type):
        """
        Compare each attribute except the autoincrementable one of this StationRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # name is a str, compare using the == operator.
        if not (self._name == name):
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

        # type is a StationType, compare using the == operator on the getValue() output
        if not (self._type.getValue() == type.getValue()):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getName(), otherRow.getPosition(), otherRow.getType()
        )

    def compareRequiredValue(self, name, position, type):

        # name is a str, compare using the == operator.
        if not (self._name == name):
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

        # type is a StationType, compare using the == operator on the getValue() output
        if not (self._type.getValue() == type.getValue()):
            return False

        return True
