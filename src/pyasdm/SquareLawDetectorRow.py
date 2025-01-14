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
# File SquareLawDetectorRow.py
#

import pyasdm.SquareLawDetectorTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.DetectorBandType import DetectorBandType


from xml.dom import minidom

import copy


class SquareLawDetectorRow:
    """
    The SquareLawDetectorRow class is a row of a SquareLawDetectorTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a SquareLawDetectorRow.
        When row is None, create an empty row attached to table, which must be a SquareLawDetectorTable.
        When row is given, copy those values in to the new row. The row argument must be a SquareLawDetectorRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.SquareLawDetectorTable):
            raise ValueError("table must be a SquareLawDetectorTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._squareLawDetectorId = Tag()

        self._numBand = 0

        self._bandType = DetectorBandType.from_int(0)

        if row is not None:
            if not isinstance(row, SquareLawDetectorRow):
                raise ValueError("row must be a SquareLawDetectorRow")

            # copy constructor

            self._squareLawDetectorId = Tag(row._squareLawDetectorId)

            self._numBand = row._numBand

            # We force the attribute of the result to be not None
            if row._bandType is None:
                self._bandType = DetectorBandType.from_int(0)
            else:
                self._bandType = DetectorBandType(row._bandType)

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

        result += Parser.extendedValueToXML(
            "squareLawDetectorId", self._squareLawDetectorId
        )

        result += Parser.valueToXML("numBand", self._numBand)

        result += Parser.valueToXML("bandType", DetectorBandType.name(self._bandType))

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
                "xmlrow is not a string or a minidom.Element", "SquareLawDetectorTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException(
                "the argument is not a row", "SquareLawDetectorTable"
            )

        # intrinsic attribute values

        squareLawDetectorIdNode = rowdom.getElementsByTagName("squareLawDetectorId")[0]

        self._squareLawDetectorId = Tag(squareLawDetectorIdNode.firstChild.data.strip())

        numBandNode = rowdom.getElementsByTagName("numBand")[0]

        self._numBand = int(numBandNode.firstChild.data.strip())

        bandTypeNode = rowdom.getElementsByTagName("bandType")[0]

        self._bandType = DetectorBandType.newDetectorBandType(
            bandTypeNode.firstChild.data.strip()
        )

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._squareLawDetectorId.toBin(eos)

        eos.writeInt(self._numBand)

        eos.writeString(self._bandType.toString())

    @staticmethod
    def squareLawDetectorIdFromBin(row, eis):
        """
        Set the squareLawDetectorId in row from the EndianInput (eis) instance.
        """

        row._squareLawDetectorId = Tag.fromBin(eis)

    @staticmethod
    def numBandFromBin(row, eis):
        """
        Set the numBand in row from the EndianInput (eis) instance.
        """

        row._numBand = eis.readInt()

    @staticmethod
    def bandTypeFromBin(row, eis):
        """
        Set the bandType in row from the EndianInput (eis) instance.
        """

        row._bandType = DetectorBandType.from_int(eis.readInt())

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["squareLawDetectorId"] = (
            SquareLawDetectorRow.squareLawDetectorIdFromBin
        )
        _fromBinMethods["numBand"] = SquareLawDetectorRow.numBandFromBin
        _fromBinMethods["bandType"] = SquareLawDetectorRow.bandTypeFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = SquareLawDetectorRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " SquareLawDetector",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute squareLawDetectorId

    _squareLawDetectorId = Tag()

    def getSquareLawDetectorId(self):
        """
        Get squareLawDetectorId.
        return squareLawDetectorId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._squareLawDetectorId)

    def setSquareLawDetectorId(self, squareLawDetectorId):
        """
        Set squareLawDetectorId with the specified Tag value.
        squareLawDetectorId The Tag value to which squareLawDetectorId is to be set.
        The value of squareLawDetectorId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the squareLawDetectorId field, which is part of the key, after this row has been added to this table."
            )

        self._squareLawDetectorId = Tag(squareLawDetectorId)

    # ===> Attribute numBand

    _numBand = 0

    def getNumBand(self):
        """
        Get numBand.
        return numBand as int
        """

        return self._numBand

    def setNumBand(self, numBand):
        """
        Set numBand with the specified int value.
        numBand The int value to which numBand is to be set.


        """

        self._numBand = int(numBand)

    # ===> Attribute bandType

    _bandType = DetectorBandType.from_int(0)

    def getBandType(self):
        """
        Get bandType.
        return bandType as DetectorBandType
        """

        return self._bandType

    def setBandType(self, bandType):
        """
        Set bandType with the specified DetectorBandType value.
        bandType The DetectorBandType value to which bandType is to be set.


        """

        self._bandType = DetectorBandType(bandType)

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(self, numBand, bandType):
        """
        Compare each attribute except the autoincrementable one of this SquareLawDetectorRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # numBand is a int, compare using the == operator.
        if not (self._numBand == numBand):
            return False

        # bandType is a DetectorBandType, compare using the == operator on the getValue() output
        if not (self._bandType.getValue() == bandType.getValue()):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(otherRow.getNumBand(), otherRow.getBandType())

    def compareRequiredValue(self, numBand, bandType):

        # numBand is a int, compare using the == operator.
        if not (self._numBand == numBand):
            return False

        # bandType is a DetectorBandType, compare using the == operator on the getValue() output
        if not (self._bandType.getValue() == bandType.getValue()):
            return False

        return True


# initialize the dictionary that maps fields to init methods
SquareLawDetectorRow.initFromBinMethods()
