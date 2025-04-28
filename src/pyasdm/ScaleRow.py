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
# File ScaleRow.py
#

import pyasdm.ScaleTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.TimeScale import TimeScale


from pyasdm.enumerations.DataScale import DataScale


from pyasdm.enumerations.DataScale import DataScale


from pyasdm.enumerations.WeightType import WeightType


from xml.dom import minidom

import copy


class ScaleRow:
    """
    The ScaleRow class is a row of a ScaleTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a ScaleRow.
        When row is None, create an empty row attached to table, which must be a ScaleTable.
        When row is given, copy those values in to the new row. The row argument must be a ScaleRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.ScaleTable):
            raise ValueError("table must be a ScaleTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._scaleId = Tag()

        self._timeScale = TimeScale.from_int(0)

        self._crossDataScale = DataScale.from_int(0)

        self._autoDataScale = DataScale.from_int(0)

        self._weightType = WeightType.from_int(0)

        if row is not None:
            if not isinstance(row, ScaleRow):
                raise ValueError("row must be a ScaleRow")

            # copy constructor

            self._scaleId = Tag(row._scaleId)

            # We force the attribute of the result to be not None
            if row._timeScale is None:
                self._timeScale = TimeScale.from_int(0)
            else:
                self._timeScale = TimeScale(row._timeScale)

            # We force the attribute of the result to be not None
            if row._crossDataScale is None:
                self._crossDataScale = DataScale.from_int(0)
            else:
                self._crossDataScale = DataScale(row._crossDataScale)

            # We force the attribute of the result to be not None
            if row._autoDataScale is None:
                self._autoDataScale = DataScale.from_int(0)
            else:
                self._autoDataScale = DataScale(row._autoDataScale)

            # We force the attribute of the result to be not None
            if row._weightType is None:
                self._weightType = WeightType.from_int(0)
            else:
                self._weightType = WeightType(row._weightType)

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

        result += Parser.extendedValueToXML("scaleId", self._scaleId)

        result += Parser.valueToXML("timeScale", TimeScale.name(self._timeScale))

        result += Parser.valueToXML(
            "crossDataScale", DataScale.name(self._crossDataScale)
        )

        result += Parser.valueToXML(
            "autoDataScale", DataScale.name(self._autoDataScale)
        )

        result += Parser.valueToXML("weightType", WeightType.name(self._weightType))

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
                "xmlrow is not a string or a minidom.Element", "ScaleTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "ScaleTable")

        # intrinsic attribute values

        scaleIdNode = rowdom.getElementsByTagName("scaleId")[0]

        self._scaleId = Tag(scaleIdNode.firstChild.data.strip())

        timeScaleNode = rowdom.getElementsByTagName("timeScale")[0]

        self._timeScale = TimeScale.newTimeScale(timeScaleNode.firstChild.data.strip())

        crossDataScaleNode = rowdom.getElementsByTagName("crossDataScale")[0]

        self._crossDataScale = DataScale.newDataScale(
            crossDataScaleNode.firstChild.data.strip()
        )

        autoDataScaleNode = rowdom.getElementsByTagName("autoDataScale")[0]

        self._autoDataScale = DataScale.newDataScale(
            autoDataScaleNode.firstChild.data.strip()
        )

        weightTypeNode = rowdom.getElementsByTagName("weightType")[0]

        self._weightType = WeightType.newWeightType(
            weightTypeNode.firstChild.data.strip()
        )

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._scaleId.toBin(eos)

        eos.writeString(str(self._timeScale))

        eos.writeString(str(self._crossDataScale))

        eos.writeString(str(self._autoDataScale))

        eos.writeString(str(self._weightType))

    @staticmethod
    def scaleIdFromBin(row, eis):
        """
        Set the scaleId in row from the EndianInput (eis) instance.
        """

        row._scaleId = Tag.fromBin(eis)

    @staticmethod
    def timeScaleFromBin(row, eis):
        """
        Set the timeScale in row from the EndianInput (eis) instance.
        """

        row._timeScale = TimeScale.literal(eis.readString())

    @staticmethod
    def crossDataScaleFromBin(row, eis):
        """
        Set the crossDataScale in row from the EndianInput (eis) instance.
        """

        row._crossDataScale = DataScale.literal(eis.readString())

    @staticmethod
    def autoDataScaleFromBin(row, eis):
        """
        Set the autoDataScale in row from the EndianInput (eis) instance.
        """

        row._autoDataScale = DataScale.literal(eis.readString())

    @staticmethod
    def weightTypeFromBin(row, eis):
        """
        Set the weightType in row from the EndianInput (eis) instance.
        """

        row._weightType = WeightType.literal(eis.readString())

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["scaleId"] = ScaleRow.scaleIdFromBin
        _fromBinMethods["timeScale"] = ScaleRow.timeScaleFromBin
        _fromBinMethods["crossDataScale"] = ScaleRow.crossDataScaleFromBin
        _fromBinMethods["autoDataScale"] = ScaleRow.autoDataScaleFromBin
        _fromBinMethods["weightType"] = ScaleRow.weightTypeFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = ScaleRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Scale",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute scaleId

    _scaleId = Tag()

    def getScaleId(self):
        """
        Get scaleId.
        return scaleId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._scaleId)

    def setScaleId(self, scaleId):
        """
        Set scaleId with the specified Tag value.
        scaleId The Tag value to which scaleId is to be set.
        The value of scaleId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the scaleId field, which is part of the key, after this row has been added to this table."
            )

        self._scaleId = Tag(scaleId)

    # ===> Attribute timeScale

    _timeScale = TimeScale.from_int(0)

    def getTimeScale(self):
        """
        Get timeScale.
        return timeScale as TimeScale
        """

        return self._timeScale

    def setTimeScale(self, timeScale):
        """
        Set timeScale with the specified TimeScale value.
        timeScale The TimeScale value to which timeScale is to be set.


        """

        self._timeScale = TimeScale(timeScale)

    # ===> Attribute crossDataScale

    _crossDataScale = DataScale.from_int(0)

    def getCrossDataScale(self):
        """
        Get crossDataScale.
        return crossDataScale as DataScale
        """

        return self._crossDataScale

    def setCrossDataScale(self, crossDataScale):
        """
        Set crossDataScale with the specified DataScale value.
        crossDataScale The DataScale value to which crossDataScale is to be set.


        """

        self._crossDataScale = DataScale(crossDataScale)

    # ===> Attribute autoDataScale

    _autoDataScale = DataScale.from_int(0)

    def getAutoDataScale(self):
        """
        Get autoDataScale.
        return autoDataScale as DataScale
        """

        return self._autoDataScale

    def setAutoDataScale(self, autoDataScale):
        """
        Set autoDataScale with the specified DataScale value.
        autoDataScale The DataScale value to which autoDataScale is to be set.


        """

        self._autoDataScale = DataScale(autoDataScale)

    # ===> Attribute weightType

    _weightType = WeightType.from_int(0)

    def getWeightType(self):
        """
        Get weightType.
        return weightType as WeightType
        """

        return self._weightType

    def setWeightType(self, weightType):
        """
        Set weightType with the specified WeightType value.
        weightType The WeightType value to which weightType is to be set.


        """

        self._weightType = WeightType(weightType)

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(self, timeScale, crossDataScale, autoDataScale, weightType):
        """
        Compare each attribute except the autoincrementable one of this ScaleRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # timeScale is a TimeScale, compare using the == operator on the getValue() output
        if not (self._timeScale.getValue() == timeScale.getValue()):
            return False

        # crossDataScale is a DataScale, compare using the == operator on the getValue() output
        if not (self._crossDataScale.getValue() == crossDataScale.getValue()):
            return False

        # autoDataScale is a DataScale, compare using the == operator on the getValue() output
        if not (self._autoDataScale.getValue() == autoDataScale.getValue()):
            return False

        # weightType is a WeightType, compare using the == operator on the getValue() output
        if not (self._weightType.getValue() == weightType.getValue()):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getTimeScale(),
            otherRow.getCrossDataScale(),
            otherRow.getAutoDataScale(),
            otherRow.getWeightType(),
        )

    def compareRequiredValue(
        self, timeScale, crossDataScale, autoDataScale, weightType
    ):

        # timeScale is a TimeScale, compare using the == operator on the getValue() output
        if not (self._timeScale.getValue() == timeScale.getValue()):
            return False

        # crossDataScale is a DataScale, compare using the == operator on the getValue() output
        if not (self._crossDataScale.getValue() == crossDataScale.getValue()):
            return False

        # autoDataScale is a DataScale, compare using the == operator on the getValue() output
        if not (self._autoDataScale.getValue() == autoDataScale.getValue()):
            return False

        # weightType is a WeightType, compare using the == operator on the getValue() output
        if not (self._weightType.getValue() == weightType.getValue()):
            return False

        return True


# initialize the dictionary that maps fields to init methods
ScaleRow.initFromBinMethods()
