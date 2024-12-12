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
# File CalGainRow.py
#

import pyasdm.CalGainTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from xml.dom import minidom

import copy


class CalGainRow:
    """
    The CalGainRow class is a row of a CalGainTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalGainRow.
        When row is None, create an empty row attached to table, which must be a CalGainTable.
        When row is given, copy those values in to the new row. The row argument must be a CalGainRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalGainTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._gain = None

        self._gainValid = None

        self._fit = None

        self._fitWeight = None

        self._totalGainValid = None

        self._totalFit = None

        self._totalFitWeight = None

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalGainRow):
                raise ValueError("row must be a MainRow")

            # copy constructor

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            self._gain = row._gain

            self._gainValid = row._gainValid

            self._fit = row._fit

            self._fitWeight = row._fitWeight

            self._totalGainValid = row._totalGainValid

            self._totalFit = row._totalFit

            self._totalFitWeight = row._totalFitWeight

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

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.valueToXML("gain", self._gain)

        result += Parser.valueToXML("gainValid", self._gainValid)

        result += Parser.valueToXML("fit", self._fit)

        result += Parser.valueToXML("fitWeight", self._fitWeight)

        result += Parser.valueToXML("totalGainValid", self._totalGainValid)

        result += Parser.valueToXML("totalFit", self._totalFit)

        result += Parser.valueToXML("totalFitWeight", self._totalFitWeight)

        # extrinsic attributes

        result += Parser.extendedValueToXML("calDataId", self._calDataId)

        result += Parser.extendedValueToXML("calReductionId", self._calReductionId)

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
                "xmlrow is not a string or a minidom.Element", "CalGainTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalGainTable")

        # intrinsic attribute values

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        gainNode = rowdom.getElementsByTagName("gain")[0]

        self._gain = float(gainNode.firstChild.data.strip())

        gainValidNode = rowdom.getElementsByTagName("gainValid")[0]

        self._gainValid = bool(gainValidNode.firstChild.data.strip())

        fitNode = rowdom.getElementsByTagName("fit")[0]

        self._fit = float(fitNode.firstChild.data.strip())

        fitWeightNode = rowdom.getElementsByTagName("fitWeight")[0]

        self._fitWeight = float(fitWeightNode.firstChild.data.strip())

        totalGainValidNode = rowdom.getElementsByTagName("totalGainValid")[0]

        self._totalGainValid = bool(totalGainValidNode.firstChild.data.strip())

        totalFitNode = rowdom.getElementsByTagName("totalFit")[0]

        self._totalFit = float(totalFitNode.firstChild.data.strip())

        totalFitWeightNode = rowdom.getElementsByTagName("totalFitWeight")[0]

        self._totalFitWeight = float(totalFitWeightNode.firstChild.data.strip())

        # extrinsic attribute values

        calDataIdNode = rowdom.getElementsByTagName("calDataId")[0]

        self._calDataId = Tag(calDataIdNode.firstChild.data.strip())

        calReductionIdNode = rowdom.getElementsByTagName("calReductionId")[0]

        self._calReductionId = Tag(calReductionIdNode.firstChild.data.strip())

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

    # ===> Attribute startValidTime

    _startValidTime = ArrayTime()

    def getStartValidTime(self):
        """
        Get startValidTime.
        return startValidTime as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._startValidTime)

    def setStartValidTime(self, startValidTime):
        """
        Set startValidTime with the specified ArrayTime value.
        startValidTime The ArrayTime value to which startValidTime is to be set.
        The value of startValidTime can be anything allowed by the ArrayTime constructor.

        """

        self._startValidTime = ArrayTime(startValidTime)

    # ===> Attribute endValidTime

    _endValidTime = ArrayTime()

    def getEndValidTime(self):
        """
        Get endValidTime.
        return endValidTime as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._endValidTime)

    def setEndValidTime(self, endValidTime):
        """
        Set endValidTime with the specified ArrayTime value.
        endValidTime The ArrayTime value to which endValidTime is to be set.
        The value of endValidTime can be anything allowed by the ArrayTime constructor.

        """

        self._endValidTime = ArrayTime(endValidTime)

    # ===> Attribute gain

    _gain = None

    def getGain(self):
        """
        Get gain.
        return gain as float
        """

        return self._gain

    def setGain(self, gain):
        """
        Set gain with the specified float value.
        gain The float value to which gain is to be set.


        """

        self._gain = float(gain)

    # ===> Attribute gainValid

    _gainValid = None

    def getGainValid(self):
        """
        Get gainValid.
        return gainValid as bool
        """

        return self._gainValid

    def setGainValid(self, gainValid):
        """
        Set gainValid with the specified bool value.
        gainValid The bool value to which gainValid is to be set.


        """

        self._gainValid = bool(gainValid)

    # ===> Attribute fit

    _fit = None

    def getFit(self):
        """
        Get fit.
        return fit as float
        """

        return self._fit

    def setFit(self, fit):
        """
        Set fit with the specified float value.
        fit The float value to which fit is to be set.


        """

        self._fit = float(fit)

    # ===> Attribute fitWeight

    _fitWeight = None

    def getFitWeight(self):
        """
        Get fitWeight.
        return fitWeight as float
        """

        return self._fitWeight

    def setFitWeight(self, fitWeight):
        """
        Set fitWeight with the specified float value.
        fitWeight The float value to which fitWeight is to be set.


        """

        self._fitWeight = float(fitWeight)

    # ===> Attribute totalGainValid

    _totalGainValid = None

    def getTotalGainValid(self):
        """
        Get totalGainValid.
        return totalGainValid as bool
        """

        return self._totalGainValid

    def setTotalGainValid(self, totalGainValid):
        """
        Set totalGainValid with the specified bool value.
        totalGainValid The bool value to which totalGainValid is to be set.


        """

        self._totalGainValid = bool(totalGainValid)

    # ===> Attribute totalFit

    _totalFit = None

    def getTotalFit(self):
        """
        Get totalFit.
        return totalFit as float
        """

        return self._totalFit

    def setTotalFit(self, totalFit):
        """
        Set totalFit with the specified float value.
        totalFit The float value to which totalFit is to be set.


        """

        self._totalFit = float(totalFit)

    # ===> Attribute totalFitWeight

    _totalFitWeight = None

    def getTotalFitWeight(self):
        """
        Get totalFitWeight.
        return totalFitWeight as float
        """

        return self._totalFitWeight

    def setTotalFitWeight(self, totalFitWeight):
        """
        Set totalFitWeight with the specified float value.
        totalFitWeight The float value to which totalFitWeight is to be set.


        """

        self._totalFitWeight = float(totalFitWeight)

    # Extrinsic Table Attributes

    # ===> Attribute calDataId

    _calDataId = Tag()

    def getCalDataId(self):
        """
        Get calDataId.
        return calDataId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._calDataId)

    def setCalDataId(self, calDataId):
        """
        Set calDataId with the specified Tag value.
        calDataId The Tag value to which calDataId is to be set.
        The value of calDataId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the calDataId field, which is part of the key, after this row has been added to this table."
            )

        self._calDataId = Tag(calDataId)

    # ===> Attribute calReductionId

    _calReductionId = Tag()

    def getCalReductionId(self):
        """
        Get calReductionId.
        return calReductionId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._calReductionId)

    def setCalReductionId(self, calReductionId):
        """
        Set calReductionId with the specified Tag value.
        calReductionId The Tag value to which calReductionId is to be set.
        The value of calReductionId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the calReductionId field, which is part of the key, after this row has been added to this table."
            )

        self._calReductionId = Tag(calReductionId)

    # Links

    def getCalReductionUsingCalReductionId(self):
        """
        Returns the row in the CalReduction table having CalReduction.calReductionId == calReductionId

        """

        return (
            self._table.getContainer()
            .getCalReduction()
            .getRowByKey(self._calReductionId)
        )

    def getCalDataUsingCalDataId(self):
        """
        Returns the row in the CalData table having CalData.calDataId == calDataId

        """

        return self._table.getContainer().getCalData().getRowByKey(self._calDataId)

    # comparison methods

    def compareNoAutoInc(
        self,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        gain,
        gainValid,
        fit,
        fitWeight,
        totalGainValid,
        totalFit,
        totalFitWeight,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalGainRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # calDataId is a Tag, compare using the equals method.
        if not self._calDataId.equals(calDataId):
            return False

        # calReductionId is a Tag, compare using the equals method.
        if not self._calReductionId.equals(calReductionId):
            return False

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # gain is a float, compare using the == operator.
        if not (self._gain == gain):
            return False

        # gainValid is a bool, compare using the == operator.
        if not (self._gainValid == gainValid):
            return False

        # fit is a float, compare using the == operator.
        if not (self._fit == fit):
            return False

        # fitWeight is a float, compare using the == operator.
        if not (self._fitWeight == fitWeight):
            return False

        # totalGainValid is a bool, compare using the == operator.
        if not (self._totalGainValid == totalGainValid):
            return False

        # totalFit is a float, compare using the == operator.
        if not (self._totalFit == totalFit):
            return False

        # totalFitWeight is a float, compare using the == operator.
        if not (self._totalFitWeight == totalFitWeight):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getStartValidTime(),
            otherRow.getEndValidTime(),
            otherRow.getGain(),
            otherRow.getGainValid(),
            otherRow.getFit(),
            otherRow.getFitWeight(),
            otherRow.getTotalGainValid(),
            otherRow.getTotalFit(),
            otherRow.getTotalFitWeight(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        gain,
        gainValid,
        fit,
        fitWeight,
        totalGainValid,
        totalFit,
        totalFitWeight,
    ):

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # gain is a float, compare using the == operator.
        if not (self._gain == gain):
            return False

        # gainValid is a bool, compare using the == operator.
        if not (self._gainValid == gainValid):
            return False

        # fit is a float, compare using the == operator.
        if not (self._fit == fit):
            return False

        # fitWeight is a float, compare using the == operator.
        if not (self._fitWeight == fitWeight):
            return False

        # totalGainValid is a bool, compare using the == operator.
        if not (self._totalGainValid == totalGainValid):
            return False

        # totalFit is a float, compare using the == operator.
        if not (self._totalFit == totalFit):
            return False

        # totalFitWeight is a float, compare using the == operator.
        if not (self._totalFitWeight == totalFitWeight):
            return False

        return True
