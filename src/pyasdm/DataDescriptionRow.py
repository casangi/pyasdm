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
# File DataDescriptionRow.py
#

import pyasdm.DataDescriptionTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from xml.dom import minidom

import copy


class DataDescriptionRow:
    """
    The DataDescriptionRow class is a row of a DataDescriptionTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a DataDescriptionRow.
        When row is None, create an empty row attached to table, which must be a DataDescriptionTable.
        When row is given, copy those values in to the new row. The row argument must be a DataDescriptionRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.DataDescriptionTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._dataDescriptionId = Tag()

        # extrinsic attributes

        self._polOrHoloId = Tag()

        self._pulsarIdExists = False

        self._pulsarId = Tag()

        self._spectralWindowId = Tag()

        if row is not None:
            if not isinstance(row, DataDescriptionRow):
                raise ValueError("row must be a MainRow")

            # copy constructor

            self._dataDescriptionId = Tag(row._dataDescriptionId)

            self._polOrHoloId = Tag(row._polOrHoloId)

            self._spectralWindowId = Tag(row._spectralWindowId)

            # by default set systematically pulsarId's value to something not None

            if row._pulsarIdExists:

                self._pulsarId = Tag(row._pulsarId)

                self._pulsarIdExists = True

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
            "dataDescriptionId", self._dataDescriptionId
        )

        # extrinsic attributes

        result += Parser.extendedValueToXML("polOrHoloId", self._polOrHoloId)

        if self._pulsarIdExists:

            result += Parser.extendedValueToXML("pulsarId", self._pulsarId)

        result += Parser.extendedValueToXML("spectralWindowId", self._spectralWindowId)

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
                "xmlrow is not a string or a minidom.Element", "DataDescriptionTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException(
                "the argument is not a row", "DataDescriptionTable"
            )

        # intrinsic attribute values

        dataDescriptionIdNode = rowdom.getElementsByTagName("dataDescriptionId")[0]

        self._dataDescriptionId = Tag(dataDescriptionIdNode.firstChild.data.strip())

        # extrinsic attribute values

        polOrHoloIdNode = rowdom.getElementsByTagName("polOrHoloId")[0]

        self._polOrHoloId = Tag(polOrHoloIdNode.firstChild.data.strip())

        pulsarIdNode = rowdom.getElementsByTagName("pulsarId")
        if len(pulsarIdNode) > 0:

            self._pulsarId = Tag(pulsarIdNode[0].firstChild.data.strip())

            self._pulsarIdExists = True

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")[0]

        self._spectralWindowId = Tag(spectralWindowIdNode.firstChild.data.strip())

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

    # ===> Attribute dataDescriptionId

    _dataDescriptionId = Tag()

    def getDataDescriptionId(self):
        """
        Get dataDescriptionId.
        return dataDescriptionId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._dataDescriptionId)

    def setDataDescriptionId(self, dataDescriptionId):
        """
        Set dataDescriptionId with the specified Tag value.
        dataDescriptionId The Tag value to which dataDescriptionId is to be set.
        The value of dataDescriptionId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the dataDescriptionId field, which is part of the key, after this row has been added to this table."
            )

        self._dataDescriptionId = Tag(dataDescriptionId)

    # Extrinsic Table Attributes

    # ===> Attribute polOrHoloId

    _polOrHoloId = Tag()

    def getPolOrHoloId(self):
        """
        Get polOrHoloId.
        return polOrHoloId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._polOrHoloId)

    def setPolOrHoloId(self, polOrHoloId):
        """
        Set polOrHoloId with the specified Tag value.
        polOrHoloId The Tag value to which polOrHoloId is to be set.
        The value of polOrHoloId can be anything allowed by the Tag constructor.

        """

        self._polOrHoloId = Tag(polOrHoloId)

    # ===> Attribute pulsarId, which is optional
    _pulsarIdExists = False

    _pulsarId = Tag()

    def isPulsarIdExists(self):
        """
        The attribute pulsarId is optional. Return True if this attribute exists.
        return True if and only if the pulsarId attribute exists.
        """
        return self._pulsarIdExists

    def getPulsarId(self):
        """
        Get pulsarId, which is optional.
        return pulsarId as Tag
        raises ValueError If pulsarId does not exist.
        """
        if not self._pulsarIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + pulsarId
                + " attribute in table DataDescription does not exist!"
            )

        # make sure it is a copy of Tag
        return Tag(self._pulsarId)

    def setPulsarId(self, pulsarId):
        """
        Set pulsarId with the specified Tag value.
        pulsarId The Tag value to which pulsarId is to be set.
        The value of pulsarId can be anything allowed by the Tag constructor.

        """

        self._pulsarId = Tag(pulsarId)

        self._pulsarIdExists = True

    def clearPulsarId(self):
        """
        Mark pulsarId, which is an optional field, as non-existent.
        """
        self._pulsarIdExists = False

    # ===> Attribute spectralWindowId

    _spectralWindowId = Tag()

    def getSpectralWindowId(self):
        """
        Get spectralWindowId.
        return spectralWindowId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._spectralWindowId)

    def setSpectralWindowId(self, spectralWindowId):
        """
        Set spectralWindowId with the specified Tag value.
        spectralWindowId The Tag value to which spectralWindowId is to be set.
        The value of spectralWindowId can be anything allowed by the Tag constructor.

        """

        self._spectralWindowId = Tag(spectralWindowId)

    # Links

    def getPolarizationUsingPolOrHoloId(self):
        """
        Returns the row in the Polarization table having Polarization.polOrHoloId == polOrHoloId

        """

        return (
            self._table.getContainer().getPolarization().getRowByKey(self._polOrHoloId)
        )

    def getSpectralWindowUsingSpectralWindowId(self):
        """
        Returns the row in the SpectralWindow table having SpectralWindow.spectralWindowId == spectralWindowId

        """

        return (
            self._table.getContainer()
            .getSpectralWindow()
            .getRowByKey(self._spectralWindowId)
        )

    def getPulsarUsingPulsarId(self):
        """
        Returns the row in the Pulsar table having Pulsar.pulsarId == pulsarId

        Raise ValueError if the optional pulsarId does not exist for this row.

        """

        if not _pulsarIdExists:
            raise ValueError("pulsarId does not exist for this row.")

        return self._table.getContainer().getPulsar().getRowByKey(self._pulsarId)

    # comparison methods

    def compareNoAutoInc(self, polOrHoloId, spectralWindowId):
        """
        Compare each attribute except the autoincrementable one of this DataDescriptionRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # polOrHoloId is a Tag, compare using the equals method.
        if not self._polOrHoloId.equals(polOrHoloId):
            return False

        # spectralWindowId is a Tag, compare using the equals method.
        if not self._spectralWindowId.equals(spectralWindowId):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getPolOrHoloId(), otherRow.getSpectralWindowId()
        )

    def compareRequiredValue(self, polOrHoloId, spectralWindowId):

        # polOrHoloId is a Tag, compare using the equals method.
        if not self._polOrHoloId.equals(polOrHoloId):
            return False

        # spectralWindowId is a Tag, compare using the equals method.
        if not self._spectralWindowId.equals(spectralWindowId):
            return False

        return True
