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
# File DopplerRow.py
#

import pyasdm.DopplerTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.DopplerReferenceCode import DopplerReferenceCode


from xml.dom import minidom

import copy


class DopplerRow:
    """
    The DopplerRow class is a row of a DopplerTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a DopplerRow.
        When row is None, create an empty row attached to table, which must be a DopplerTable.
        When row is given, copy those values in to the new row. The row argument must be a DopplerRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.DopplerTable):
            raise ValueError("table must be a DopplerTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._dopplerId = 0

        self._transitionIndex = 0

        self._velDef = DopplerReferenceCode.from_int(0)

        # extrinsic attributes

        self._sourceId = 0

        if row is not None:
            if not isinstance(row, DopplerRow):
                raise ValueError("row must be a DopplerRow")

            # copy constructor

            self._dopplerId = row._dopplerId

            self._sourceId = row._sourceId

            self._transitionIndex = row._transitionIndex

            # We force the attribute of the result to be not None
            if row._velDef is None:
                self._velDef = DopplerReferenceCode.from_int(0)
            else:
                self._velDef = DopplerReferenceCode(row._velDef)

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

        result += Parser.valueToXML("dopplerId", self._dopplerId)

        result += Parser.valueToXML("transitionIndex", self._transitionIndex)

        result += Parser.valueToXML("velDef", DopplerReferenceCode.name(self._velDef))

        # extrinsic attributes

        result += Parser.valueToXML("sourceId", self._sourceId)

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
                "xmlrow is not a string or a minidom.Element", "DopplerTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "DopplerTable")

        # intrinsic attribute values

        dopplerIdNode = rowdom.getElementsByTagName("dopplerId")[0]

        self._dopplerId = int(dopplerIdNode.firstChild.data.strip())

        transitionIndexNode = rowdom.getElementsByTagName("transitionIndex")[0]

        self._transitionIndex = int(transitionIndexNode.firstChild.data.strip())

        velDefNode = rowdom.getElementsByTagName("velDef")[0]

        self._velDef = DopplerReferenceCode.newDopplerReferenceCode(
            velDefNode.firstChild.data.strip()
        )

        # extrinsic attribute values

        sourceIdNode = rowdom.getElementsByTagName("sourceId")[0]

        self._sourceId = int(sourceIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        eos.writeInt(self._dopplerId)

        eos.writeInt(self._sourceId)

        eos.writeInt(self._transitionIndex)

        eos.writeString(str(self._velDef))

    @staticmethod
    def dopplerIdFromBin(row, eis):
        """
        Set the dopplerId in row from the EndianInput (eis) instance.
        """

        row._dopplerId = eis.readInt()

    @staticmethod
    def sourceIdFromBin(row, eis):
        """
        Set the sourceId in row from the EndianInput (eis) instance.
        """

        row._sourceId = eis.readInt()

    @staticmethod
    def transitionIndexFromBin(row, eis):
        """
        Set the transitionIndex in row from the EndianInput (eis) instance.
        """

        row._transitionIndex = eis.readInt()

    @staticmethod
    def velDefFromBin(row, eis):
        """
        Set the velDef in row from the EndianInput (eis) instance.
        """

        row._velDef = DopplerReferenceCode.literal(eis.readString())

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["dopplerId"] = DopplerRow.dopplerIdFromBin
        _fromBinMethods["sourceId"] = DopplerRow.sourceIdFromBin
        _fromBinMethods["transitionIndex"] = DopplerRow.transitionIndexFromBin
        _fromBinMethods["velDef"] = DopplerRow.velDefFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = DopplerRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Doppler",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute dopplerId

    _dopplerId = 0

    def getDopplerId(self):
        """
        Get dopplerId.
        return dopplerId as int
        """

        return self._dopplerId

    def setDopplerId(self, dopplerId):
        """
        Set dopplerId with the specified int value.
        dopplerId The int value to which dopplerId is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the dopplerId field, which is part of the key, after this row has been added to this table."
            )

        self._dopplerId = int(dopplerId)

    # ===> Attribute transitionIndex

    _transitionIndex = 0

    def getTransitionIndex(self):
        """
        Get transitionIndex.
        return transitionIndex as int
        """

        return self._transitionIndex

    def setTransitionIndex(self, transitionIndex):
        """
        Set transitionIndex with the specified int value.
        transitionIndex The int value to which transitionIndex is to be set.


        """

        self._transitionIndex = int(transitionIndex)

    # ===> Attribute velDef

    _velDef = DopplerReferenceCode.from_int(0)

    def getVelDef(self):
        """
        Get velDef.
        return velDef as DopplerReferenceCode
        """

        return self._velDef

    def setVelDef(self, velDef):
        """
        Set velDef with the specified DopplerReferenceCode value.
        velDef The DopplerReferenceCode value to which velDef is to be set.


        """

        self._velDef = DopplerReferenceCode(velDef)

    # Extrinsic Table Attributes

    # ===> Attribute sourceId

    _sourceId = 0

    def getSourceId(self):
        """
        Get sourceId.
        return sourceId as int
        """

        return self._sourceId

    def setSourceId(self, sourceId):
        """
        Set sourceId with the specified int value.
        sourceId The int value to which sourceId is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the sourceId field, which is part of the key, after this row has been added to this table."
            )

        self._sourceId = int(sourceId)

    # Links

    # ===> Slice link from a row of Doppler table to a collection of row of Source table.
    def getSources(self):
        """
        Get the collection of rows in the Source table having sourceId == this.sourceId
        """

        return self._table.getContainer().getSource().getRowBySourceId(self._sourceId)

    # comparison methods

    def compareNoAutoInc(self, sourceId, transitionIndex, velDef):
        """
        Compare each attribute except the autoincrementable one of this DopplerRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # sourceId is a int, compare using the == operator.
        if not (self._sourceId == sourceId):
            return False

        # transitionIndex is a int, compare using the == operator.
        if not (self._transitionIndex == transitionIndex):
            return False

        # velDef is a DopplerReferenceCode, compare using the == operator on the getValue() output
        if not (self._velDef.getValue() == velDef.getValue()):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getTransitionIndex(), otherRow.getVelDef()
        )

    def compareRequiredValue(self, transitionIndex, velDef):

        # transitionIndex is a int, compare using the == operator.
        if not (self._transitionIndex == transitionIndex):
            return False

        # velDef is a DopplerReferenceCode, compare using the == operator on the getValue() output
        if not (self._velDef.getValue() == velDef.getValue()):
            return False

        return True


# initialize the dictionary that maps fields to init methods
DopplerRow.initFromBinMethods()
