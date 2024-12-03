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
# File ProcessorRow.py
#

import pyasdm.ProcessorTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.ProcessorType import ProcessorType


from pyasdm.enumerations.ProcessorSubType import ProcessorSubType


from xml.dom import minidom

import copy


class ProcessorRow:
    """
    The ProcessorRow class is a row of a ProcessorTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a ProcessorRow.
        When row is None, create an empty row attached to table, which must be a ProcessorTable.
        When row is given, copy those values in to the new row. The row argument must be a ProcessorRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.ProcessorTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._processorType = ProcessorType.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._processorSubType = ProcessorSubType.from_int(0)

        if row is not None:
            if not isinstance(row, ProcessorRow):
                raise ValueError("row must be a MainRow")

            self._processorId = Tag(row._processorId)

            self._modeId = Tag(row._modeId)

            # We force the attribute of the result to be not None
            if row._processorType is None:
                self._processorType = ProcessorType.from_int(0)
            else:
                self._processorType = ProcessorType(row._processorType)

            # We force the attribute of the result to be not None
            if row._processorSubType is None:
                self._processorSubType = ProcessorSubType.from_int(0)
            else:
                self._processorSubType = ProcessorSubType(row._processorSubType)

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

        result += Parser.extendedValueToXML("processorId", self._processorId)

        result += Parser.extendedValueToXML("modeId", self._modeId)

        result += Parser.valueToXML(
            "processorType", ProcessorType.name(self._processorType)
        )

        result += Parser.valueToXML(
            "processorSubType", ProcessorSubType.name(self._processorSubType)
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
                "xmlrow is not a string or a minidom.Element", "ProcessorTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "ProcessorTable")

        # intrinsic attribute values

        processorIdNode = rowdom.getElementsByTagName("processorId")[0]

        self._processorId = Tag(processorIdNode.firstChild.data)

        modeIdNode = rowdom.getElementsByTagName("modeId")[0]

        self._modeId = Tag(modeIdNode.firstChild.data)

        processorTypeNode = rowdom.getElementsByTagName("processorType")[0]

        self._processorType = ProcessorType.newProcessorType(
            processorTypeNode.firstChild.data
        )

        processorSubTypeNode = rowdom.getElementsByTagName("processorSubType")[0]

        self._processorSubType = ProcessorSubType.newProcessorSubType(
            processorSubTypeNode.firstChild.data
        )

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

    # ===> Attribute processorId

    _processorId = Tag()

    def getProcessorId(self):
        """
        Get processorId.
        return processorId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._processorId)

    def setProcessorId(self, processorId):
        """
        Set processorId with the specified Tag value.
        processorId The Tag value to which processorId is to be set.
        The value of processorId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the processorId field, which is part of the key, after this row has been added to this table."
            )

        self._processorId = Tag(processorId)

    # ===> Attribute modeId

    _modeId = Tag()

    def getModeId(self):
        """
        Get modeId.
        return modeId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._modeId)

    def setModeId(self, modeId):
        """
        Set modeId with the specified Tag value.
        modeId The Tag value to which modeId is to be set.
        The value of modeId can be anything allowed by the Tag constructor.

        """

        self._modeId = Tag(modeId)

    # ===> Attribute processorType

    _processorType = ProcessorType.from_int(0)

    def getProcessorType(self):
        """
        Get processorType.
        return processorType as ProcessorType
        """

        return self._processorType

    def setProcessorType(self, processorType):
        """
        Set processorType with the specified ProcessorType value.
        processorType The ProcessorType value to which processorType is to be set.


        """

        self._processorType = ProcessorType(processorType)

    # ===> Attribute processorSubType

    _processorSubType = ProcessorSubType.from_int(0)

    def getProcessorSubType(self):
        """
        Get processorSubType.
        return processorSubType as ProcessorSubType
        """

        return self._processorSubType

    def setProcessorSubType(self, processorSubType):
        """
        Set processorSubType with the specified ProcessorSubType value.
        processorSubType The ProcessorSubType value to which processorSubType is to be set.


        """

        self._processorSubType = ProcessorSubType(processorSubType)

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(self, modeId, processorType, processorSubType):
        """
        Compare each attribute except the autoincrementable one of this ProcessorRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # modeId is a Tag, compare using the equals method.
        if not self._modeId.equals(modeId):
            return False

        # processorType is a ProcessorType, compare using the == operator on the getValue() output
        if not (self._processorType.getValue() == processorType.getValue()):
            return False

        # processorSubType is a ProcessorSubType, compare using the == operator on the getValue() output
        if not (self._processorSubType.getValue() == processorSubType.getValue()):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getModeId(),
            otherRow.getProcessorType(),
            otherRow.getProcessorSubType(),
        )

    def compareRequiredValue(self, modeId, processorType, processorSubType):

        # modeId is a Tag, compare using the equals method.
        if not self._modeId.equals(modeId):
            return False

        # processorType is a ProcessorType, compare using the == operator on the getValue() output
        if not (self._processorType.getValue() == processorType.getValue()):
            return False

        # processorSubType is a ProcessorSubType, compare using the == operator on the getValue() output
        if not (self._processorSubType.getValue() == processorSubType.getValue()):
            return False

        return True
