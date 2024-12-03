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
# File ObservationRow.py
#

import pyasdm.ObservationTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from xml.dom import minidom

import copy


class ObservationRow:
    """
    The ObservationRow class is a row of a ObservationTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a ObservationRow.
        When row is None, create an empty row attached to table, which must be a ObservationTable.
        When row is given, copy those values in to the new row. The row argument must be a ObservationRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.ObservationTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        if row is not None:
            if not isinstance(row, ObservationRow):
                raise ValueError("row must be a MainRow")

            self._observationId = Tag(row._observationId)

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

        result += Parser.extendedValueToXML("observationId", self._observationId)

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
                "xmlrow is not a string or a minidom.Element", "ObservationTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "ObservationTable")

        # intrinsic attribute values

        observationIdNode = rowdom.getElementsByTagName("observationId")[0]

        self._observationId = Tag(observationIdNode.firstChild.data)

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

    # ===> Attribute observationId

    _observationId = Tag()

    def getObservationId(self):
        """
        Get observationId.
        return observationId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._observationId)

    def setObservationId(self, observationId):
        """
        Set observationId with the specified Tag value.
        observationId The Tag value to which observationId is to be set.
        The value of observationId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the observationId field, which is part of the key, after this row has been added to this table."
            )

        self._observationId = Tag(observationId)

    # Extrinsic Table Attributes

    # Links

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
