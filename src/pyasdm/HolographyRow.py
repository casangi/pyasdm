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
# File HolographyRow.py
#

import pyasdm.HolographyTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.HolographyChannelType import HolographyChannelType


from xml.dom import minidom

import copy


class HolographyRow:
    """
    The HolographyRow class is a row of a HolographyTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a HolographyRow.
        When row is None, create an empty row attached to table, which must be a HolographyTable.
        When row is given, copy those values in to the new row. The row argument must be a HolographyRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.HolographyTable):
            raise ValueError("table must be a HolographyTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._holographyId = Tag()

        self._distance = Length()

        self._focus = Length()

        self._numCorr = 0

        self._type = []  # this is a list of HolographyChannelType []

        if row is not None:
            if not isinstance(row, HolographyRow):
                raise ValueError("row must be a HolographyRow")

            # copy constructor

            self._holographyId = Tag(row._holographyId)

            self._distance = Length(row._distance)

            self._focus = Length(row._focus)

            self._numCorr = row._numCorr

            # type is a  list , make a deep copy
            self._type = copy.deepcopy(row._type)

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

        result += Parser.extendedValueToXML("holographyId", self._holographyId)

        result += Parser.extendedValueToXML("distance", self._distance)

        result += Parser.extendedValueToXML("focus", self._focus)

        result += Parser.valueToXML("numCorr", self._numCorr)

        result += Parser.listEnumValueToXML("type", self._type)

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
                "xmlrow is not a string or a minidom.Element", "HolographyTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "HolographyTable")

        # intrinsic attribute values

        holographyIdNode = rowdom.getElementsByTagName("holographyId")[0]

        self._holographyId = Tag(holographyIdNode.firstChild.data.strip())

        distanceNode = rowdom.getElementsByTagName("distance")[0]

        self._distance = Length(distanceNode.firstChild.data.strip())

        focusNode = rowdom.getElementsByTagName("focus")[0]

        self._focus = Length(focusNode.firstChild.data.strip())

        numCorrNode = rowdom.getElementsByTagName("numCorr")[0]

        self._numCorr = int(numCorrNode.firstChild.data.strip())

        typeNode = rowdom.getElementsByTagName("type")[0]

        typeStr = typeNode.firstChild.data.strip()
        self._type = Parser.stringListToLists(
            typeStr, HolographyChannelType, "Holography", False
        )

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._holographyId.toBin(eos)

        self._distance.toBin(eos)

        self._focus.toBin(eos)

        eos.writeInt(self._numCorr)

        eos.writeInt(len(self._type))
        for i in range(len(self._type)):

            eos.writeString(self._type[i].toString())

    @staticmethod
    def holographyIdFromBin(row, eis):
        """
        Set the holographyId in row from the EndianInput (eis) instance.
        """

        row._holographyId = Tag.fromBin(eis)

    @staticmethod
    def distanceFromBin(row, eis):
        """
        Set the distance in row from the EndianInput (eis) instance.
        """

        row._distance = Length.fromBin(eis)

    @staticmethod
    def focusFromBin(row, eis):
        """
        Set the focus in row from the EndianInput (eis) instance.
        """

        row._focus = Length.fromBin(eis)

    @staticmethod
    def numCorrFromBin(row, eis):
        """
        Set the numCorr in row from the EndianInput (eis) instance.
        """

        row._numCorr = eis.readInt()

    @staticmethod
    def typeFromBin(row, eis):
        """
        Set the type in row from the EndianInput (eis) instance.
        """

        typeDim1 = eis.readInt()
        thisList = []
        for i in range(typeDim1):
            thisValue = HolographyChannelType.from_int(eis.readInt())
            thisList.append(thisValue)
        row._type = thisList

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["holographyId"] = HolographyRow.holographyIdFromBin
        _fromBinMethods["distance"] = HolographyRow.distanceFromBin
        _fromBinMethods["focus"] = HolographyRow.focusFromBin
        _fromBinMethods["numCorr"] = HolographyRow.numCorrFromBin
        _fromBinMethods["type"] = HolographyRow.typeFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = HolographyRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Holography",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute holographyId

    _holographyId = Tag()

    def getHolographyId(self):
        """
        Get holographyId.
        return holographyId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._holographyId)

    def setHolographyId(self, holographyId):
        """
        Set holographyId with the specified Tag value.
        holographyId The Tag value to which holographyId is to be set.
        The value of holographyId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the holographyId field, which is part of the key, after this row has been added to this table."
            )

        self._holographyId = Tag(holographyId)

    # ===> Attribute distance

    _distance = Length()

    def getDistance(self):
        """
        Get distance.
        return distance as Length
        """

        # make sure it is a copy of Length
        return Length(self._distance)

    def setDistance(self, distance):
        """
        Set distance with the specified Length value.
        distance The Length value to which distance is to be set.
        The value of distance can be anything allowed by the Length constructor.

        """

        self._distance = Length(distance)

    # ===> Attribute focus

    _focus = Length()

    def getFocus(self):
        """
        Get focus.
        return focus as Length
        """

        # make sure it is a copy of Length
        return Length(self._focus)

    def setFocus(self, focus):
        """
        Set focus with the specified Length value.
        focus The Length value to which focus is to be set.
        The value of focus can be anything allowed by the Length constructor.

        """

        self._focus = Length(focus)

    # ===> Attribute numCorr

    _numCorr = 0

    def getNumCorr(self):
        """
        Get numCorr.
        return numCorr as int
        """

        return self._numCorr

    def setNumCorr(self, numCorr):
        """
        Set numCorr with the specified int value.
        numCorr The int value to which numCorr is to be set.


        """

        self._numCorr = int(numCorr)

    # ===> Attribute type

    _type = None  # this is a 1D list of HolographyChannelType

    def getType(self):
        """
        Get type.
        return type as HolographyChannelType []
        """

        return copy.deepcopy(self._type)

    def setType(self, type):
        """
        Set type with the specified HolographyChannelType []  value.
        type The HolographyChannelType []  value to which type is to be set.


        """

        # value must be a list
        if not isinstance(type, list):
            raise ValueError("The value of type must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(type)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of type is not correct")

            # the type of the values in the list must be HolographyChannelType
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(type, HolographyChannelType):
                raise ValueError(
                    "type of the first value in type is not HolographyChannelType as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._type = copy.deepcopy(type)
        except Exception as exc:
            raise ValueError("Invalid type : " + str(exc))

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(self, distance, focus, numCorr, type):
        """
        Compare each attribute except the autoincrementable one of this HolographyRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # distance is a Length, compare using the almostEquals method.
        if not self._distance.almostEquals(
            distance, self.getTable().getDistanceEqTolerance()
        ):
            return False

        # focus is a Length, compare using the almostEquals method.
        if not self._focus.almostEquals(focus, self.getTable().getFocusEqTolerance()):
            return False

        # numCorr is a int, compare using the == operator.
        if not (self._numCorr == numCorr):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._type) != len(type):
            return False
        for indx in range(len(type)):

            # type is a list of HolographyChannelType, compare using == operator.
            if not (self._type[indx] == type[indx]):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getDistance(),
            otherRow.getFocus(),
            otherRow.getNumCorr(),
            otherRow.getType(),
        )

    def compareRequiredValue(self, distance, focus, numCorr, type):

        # distance is a Length, compare using the almostEquals method.
        if not self._distance.almostEquals(
            distance, self.getTable().getDistanceEqTolerance()
        ):
            return False

        # focus is a Length, compare using the almostEquals method.
        if not self._focus.almostEquals(focus, self.getTable().getFocusEqTolerance()):
            return False

        # numCorr is a int, compare using the == operator.
        if not (self._numCorr == numCorr):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._type) != len(type):
            return False
        for indx in range(len(type)):

            # type is a list of HolographyChannelType, compare using == operator.
            if not (self._type[indx] == type[indx]):
                return False

        return True


# initialize the dictionary that maps fields to init methods
HolographyRow.initFromBinMethods()
