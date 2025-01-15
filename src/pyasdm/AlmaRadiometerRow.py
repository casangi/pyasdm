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
# File AlmaRadiometerRow.py
#

import pyasdm.AlmaRadiometerTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from xml.dom import minidom

import copy


class AlmaRadiometerRow:
    """
    The AlmaRadiometerRow class is a row of a AlmaRadiometerTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a AlmaRadiometerRow.
        When row is None, create an empty row attached to table, which must be a AlmaRadiometerTable.
        When row is given, copy those values in to the new row. The row argument must be a AlmaRadiometerRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.AlmaRadiometerTable):
            raise ValueError("table must be a AlmaRadiometerTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._almaRadiometerId = Tag()

        self._numAntennaExists = False

        self._numAntenna = 0

        # extrinsic attributes

        self._spectralWindowIdExists = False

        self._spectralWindowId = []  # this is a list of Tag []

        if row is not None:
            if not isinstance(row, AlmaRadiometerRow):
                raise ValueError("row must be a AlmaRadiometerRow")

            # copy constructor

            self._almaRadiometerId = Tag(row._almaRadiometerId)

            # by default set systematically numAntenna's value to something not None

            if row._numAntennaExists:

                self._numAntenna = row._numAntenna

                self._numAntennaExists = True

            # by default set systematically spectralWindowId's value to something not None

            if row._spectralWindowIdExists:

                # spectralWindowId is a list, let's populate self._spectralWindowId element by element.
                if self._spectralWindowId is None:
                    self._spectralWindowId = []
                for i in range(len(row._spectralWindowId)):

                    self._spectralWindowId.append(Tag(row._spectralWindowId[i]))

                self._spectralWindowIdExists = True

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

        result += Parser.extendedValueToXML("almaRadiometerId", self._almaRadiometerId)

        if self._numAntennaExists:

            result += Parser.valueToXML("numAntenna", self._numAntenna)

        # extrinsic attributes

        if self._spectralWindowIdExists:

            result += Parser.listExtendedValueToXML(
                "spectralWindowId", self._spectralWindowId
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
                "xmlrow is not a string or a minidom.Element", "AlmaRadiometerTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException(
                "the argument is not a row", "AlmaRadiometerTable"
            )

        # intrinsic attribute values

        almaRadiometerIdNode = rowdom.getElementsByTagName("almaRadiometerId")[0]

        self._almaRadiometerId = Tag(almaRadiometerIdNode.firstChild.data.strip())

        numAntennaNode = rowdom.getElementsByTagName("numAntenna")
        if len(numAntennaNode) > 0:

            self._numAntenna = int(numAntennaNode[0].firstChild.data.strip())

            self._numAntennaExists = True

        # extrinsic attribute values

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")
        if len(spectralWindowIdNode) > 0:

            spectralWindowIdStr = spectralWindowIdNode[0].firstChild.data.strip()

            self._spectralWindowId = Parser.stringListToLists(
                spectralWindowIdStr, Tag, "AlmaRadiometer", True
            )

            self._spectralWindowIdExists = True

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._almaRadiometerId.toBin(eos)

        eos.writeBool(self._numAntennaExists)
        if self._numAntennaExists:

            eos.writeInt(self._numAntenna)

        eos.writeBool(self._spectralWindowIdExists)
        if self._spectralWindowIdExists:

            Tag.listToBin(self._spectralWindowId, eos)

    @staticmethod
    def almaRadiometerIdFromBin(row, eis):
        """
        Set the almaRadiometerId in row from the EndianInput (eis) instance.
        """

        row._almaRadiometerId = Tag.fromBin(eis)

    @staticmethod
    def numAntennaFromBin(row, eis):
        """
        Set the optional numAntenna in row from the EndianInput (eis) instance.
        """
        row._numAntennaExists = eis.readBool()
        if row._numAntennaExists:

            row._numAntenna = eis.readInt()

    @staticmethod
    def spectralWindowIdFromBin(row, eis):
        """
        Set the optional spectralWindowId in row from the EndianInput (eis) instance.
        """
        row._spectralWindowIdExists = eis.readBool()
        if row._spectralWindowIdExists:

            row._spectralWindowId = Tag.from1DBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["almaRadiometerId"] = AlmaRadiometerRow.almaRadiometerIdFromBin

        _fromBinMethods["numAntenna"] = AlmaRadiometerRow.numAntennaFromBin
        _fromBinMethods["spectralWindowId"] = AlmaRadiometerRow.spectralWindowIdFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = AlmaRadiometerRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " AlmaRadiometer",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute almaRadiometerId

    _almaRadiometerId = Tag()

    def getAlmaRadiometerId(self):
        """
        Get almaRadiometerId.
        return almaRadiometerId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._almaRadiometerId)

    def setAlmaRadiometerId(self, almaRadiometerId):
        """
        Set almaRadiometerId with the specified Tag value.
        almaRadiometerId The Tag value to which almaRadiometerId is to be set.
        The value of almaRadiometerId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the almaRadiometerId field, which is part of the key, after this row has been added to this table."
            )

        self._almaRadiometerId = Tag(almaRadiometerId)

    # ===> Attribute numAntenna, which is optional
    _numAntennaExists = False

    _numAntenna = 0

    def isNumAntennaExists(self):
        """
        The attribute numAntenna is optional. Return True if this attribute exists.
        return True if and only if the numAntenna attribute exists.
        """
        return self._numAntennaExists

    def getNumAntenna(self):
        """
        Get numAntenna, which is optional.
        return numAntenna as int
        raises ValueError If numAntenna does not exist.
        """
        if not self._numAntennaExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numAntenna
                + " attribute in table AlmaRadiometer does not exist!"
            )

        return self._numAntenna

    def setNumAntenna(self, numAntenna):
        """
        Set numAntenna with the specified int value.
        numAntenna The int value to which numAntenna is to be set.


        """

        self._numAntenna = int(numAntenna)

        self._numAntennaExists = True

    def clearNumAntenna(self):
        """
        Mark numAntenna, which is an optional field, as non-existent.
        """
        self._numAntennaExists = False

    # Extrinsic Table Attributes

    # ===> Attribute spectralWindowId, which is optional
    _spectralWindowIdExists = False

    _spectralWindowId = []  # this is a list of Tag []

    def isSpectralWindowIdExists(self):
        """
        The attribute spectralWindowId is optional. Return True if this attribute exists.
        return True if and only if the spectralWindowId attribute exists.
        """
        return self._spectralWindowIdExists

    def getSpectralWindowId(self):
        """
        Get spectralWindowId, which is optional.
        return spectralWindowId as Tag []
        raises ValueError If spectralWindowId does not exist.
        """
        if not self._spectralWindowIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + spectralWindowId
                + " attribute in table AlmaRadiometer does not exist!"
            )

        return copy.deepcopy(self._spectralWindowId)

    def setSpectralWindowId(self, spectralWindowId):
        """
        Set spectralWindowId with the specified Tag []  value.
        spectralWindowId The Tag []  value to which spectralWindowId is to be set.
        The value of spectralWindowId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(spectralWindowId, list):
            raise ValueError("The value of spectralWindowId must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(spectralWindowId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of spectralWindowId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(spectralWindowId, Tag):
                raise ValueError(
                    "type of the first value in spectralWindowId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._spectralWindowId = copy.deepcopy(spectralWindowId)
        except Exception as exc:
            raise ValueError("Invalid spectralWindowId : " + str(exc))

        self._spectralWindowIdExists = True

    def clearSpectralWindowId(self):
        """
        Mark spectralWindowId, which is an optional field, as non-existent.
        """
        self._spectralWindowIdExists = False

    # Links

    def setOneSpectralWindowId(self, index, spectralWindowId):
        """
        Set spectralWindowId[index] with the specified Tag value.
        index The index in spectralWindowId where to set the Tag value.
        spectralWindowId The Tag value to which spectralWindowId[index] is to be set.
        Raises an exception if that value does not already exist in this row
        """
        if not self._spectralWindowIdExists():
            raise ValueError(
                "The optional attribute, spectralWindowId, does not exist in this row. This value can not be set using this method."
            )
        self._spectralWindowId[index] = Tag(spectralWindowId)

    # ===> hasmany link from a row of AlmaRadiometer table to many rows of SpectralWindow table.

    def addSpectralWindowId(self, id):
        """
        Append a Tag to spectralWindowId
        id the Tag to be appended to spectralWindowId
        """
        if isinstance(id, list):
            for thisValue in id:
                self._spectralWindowId.append(Tag(thisValue))
        else:
            self._spectralWindowId.append(Tag(id))

        if not self._spectralWindowIdExists:
            self._spectralWindowIdExists = True

    def getOneSpectralWindowId(self, i):
        """
        Returns the Tag stored in spectralWindowId at position i.
        """
        return self._spectralWindowId[i]

    def getSpectralWindowUsingSpectralWindowId(self, i):
        """
        Returns the SpectralWindowRow linked to this row via the Tag stored in spectralWindowId
        at position i.
        """

        return (
            self._table.getContainer()
            .getSpectralWindow()
            .getRowByKey(self._spectralWindowId[i])
        )

    def getSpectralWindowsUsingSpectralWindowId(self):
        """
        Returns the array of SpectralWindowRow linked to this row via the Tags stored in spectralWindowId
        """
        result = []
        for thisItem in self._spectralWindowId:
            result.append(
                self._table.getContainer().getSpectralWindow().getRowByKey(thisItem)
            )

        return result

    # comparison methods

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return True

    def compareRequiredValue(
        self,
    ):

        return True


# initialize the dictionary that maps fields to init methods
AlmaRadiometerRow.initFromBinMethods()
