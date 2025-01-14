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
# File SeeingRow.py
#

import pyasdm.SeeingTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from xml.dom import minidom

import copy


class SeeingRow:
    """
    The SeeingRow class is a row of a SeeingTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a SeeingRow.
        When row is None, create an empty row attached to table, which must be a SeeingTable.
        When row is given, copy those values in to the new row. The row argument must be a SeeingRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.SeeingTable):
            raise ValueError("table must be a SeeingTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._timeInterval = ArrayTimeInterval()

        self._numBaseLength = 0

        self._baseLength = []  # this is a list of Length []

        self._phaseRms = []  # this is a list of Angle []

        self._seeing = None

        self._exponent = None

        if row is not None:
            if not isinstance(row, SeeingRow):
                raise ValueError("row must be a SeeingRow")

            # copy constructor

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._numBaseLength = row._numBaseLength

            # baseLength is a  list , make a deep copy
            self._baseLength = copy.deepcopy(row._baseLength)

            # phaseRms is a  list , make a deep copy
            self._phaseRms = copy.deepcopy(row._phaseRms)

            self._seeing = row._seeing

            self._exponent = row._exponent

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

        result += Parser.extendedValueToXML("timeInterval", self._timeInterval)

        result += Parser.valueToXML("numBaseLength", self._numBaseLength)

        result += Parser.listExtendedValueToXML("baseLength", self._baseLength)

        result += Parser.listExtendedValueToXML("phaseRms", self._phaseRms)

        result += Parser.valueToXML("seeing", self._seeing)

        result += Parser.valueToXML("exponent", self._exponent)

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
                "xmlrow is not a string or a minidom.Element", "SeeingTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "SeeingTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        numBaseLengthNode = rowdom.getElementsByTagName("numBaseLength")[0]

        self._numBaseLength = int(numBaseLengthNode.firstChild.data.strip())

        baseLengthNode = rowdom.getElementsByTagName("baseLength")[0]

        baseLengthStr = baseLengthNode.firstChild.data.strip()

        self._baseLength = Parser.stringListToLists(
            baseLengthStr, Length, "Seeing", True
        )

        phaseRmsNode = rowdom.getElementsByTagName("phaseRms")[0]

        phaseRmsStr = phaseRmsNode.firstChild.data.strip()

        self._phaseRms = Parser.stringListToLists(phaseRmsStr, Angle, "Seeing", True)

        seeingNode = rowdom.getElementsByTagName("seeing")[0]

        self._seeing = float(seeingNode.firstChild.data.strip())

        exponentNode = rowdom.getElementsByTagName("exponent")[0]

        self._exponent = float(exponentNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._timeInterval.toBin(eos)

        eos.writeInt(self._numBaseLength)

        Length.listToBin(self._baseLength, eos)

        Angle.listToBin(self._phaseRms, eos)

        eos.writeFloat(self._seeing)

        eos.writeFloat(self._exponent)

    @staticmethod
    def timeIntervalFromBin(row, eis):
        """
        Set the timeInterval in row from the EndianInput (eis) instance.
        """

        row._timeInterval = ArrayTimeInterval.fromBin(eis)

    @staticmethod
    def numBaseLengthFromBin(row, eis):
        """
        Set the numBaseLength in row from the EndianInput (eis) instance.
        """

        row._numBaseLength = eis.readInt()

    @staticmethod
    def baseLengthFromBin(row, eis):
        """
        Set the baseLength in row from the EndianInput (eis) instance.
        """

        row._baseLength = Length.from1DBin(eis)

    @staticmethod
    def phaseRmsFromBin(row, eis):
        """
        Set the phaseRms in row from the EndianInput (eis) instance.
        """

        row._phaseRms = Angle.from1DBin(eis)

    @staticmethod
    def seeingFromBin(row, eis):
        """
        Set the seeing in row from the EndianInput (eis) instance.
        """

        row._seeing = eis.readFloat()

    @staticmethod
    def exponentFromBin(row, eis):
        """
        Set the exponent in row from the EndianInput (eis) instance.
        """

        row._exponent = eis.readFloat()

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["timeInterval"] = SeeingRow.timeIntervalFromBin
        _fromBinMethods["numBaseLength"] = SeeingRow.numBaseLengthFromBin
        _fromBinMethods["baseLength"] = SeeingRow.baseLengthFromBin
        _fromBinMethods["phaseRms"] = SeeingRow.phaseRmsFromBin
        _fromBinMethods["seeing"] = SeeingRow.seeingFromBin
        _fromBinMethods["exponent"] = SeeingRow.exponentFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = SeeingRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Seeing",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute timeInterval

    _timeInterval = ArrayTimeInterval()

    def getTimeInterval(self):
        """
        Get timeInterval.
        return timeInterval as ArrayTimeInterval
        """

        # make sure it is a copy of ArrayTimeInterval
        return ArrayTimeInterval(self._timeInterval)

    def setTimeInterval(self, timeInterval):
        """
        Set timeInterval with the specified ArrayTimeInterval value.
        timeInterval The ArrayTimeInterval value to which timeInterval is to be set.
        The value of timeInterval can be anything allowed by the ArrayTimeInterval constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the timeInterval field, which is part of the key, after this row has been added to this table."
            )

        self._timeInterval = ArrayTimeInterval(timeInterval)

    # ===> Attribute numBaseLength

    _numBaseLength = 0

    def getNumBaseLength(self):
        """
        Get numBaseLength.
        return numBaseLength as int
        """

        return self._numBaseLength

    def setNumBaseLength(self, numBaseLength):
        """
        Set numBaseLength with the specified int value.
        numBaseLength The int value to which numBaseLength is to be set.


        """

        self._numBaseLength = int(numBaseLength)

    # ===> Attribute baseLength

    _baseLength = None  # this is a 1D list of Length

    def getBaseLength(self):
        """
        Get baseLength.
        return baseLength as Length []
        """

        return copy.deepcopy(self._baseLength)

    def setBaseLength(self, baseLength):
        """
        Set baseLength with the specified Length []  value.
        baseLength The Length []  value to which baseLength is to be set.
        The value of baseLength can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(baseLength, list):
            raise ValueError("The value of baseLength must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(baseLength)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of baseLength is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(baseLength, Length):
                raise ValueError(
                    "type of the first value in baseLength is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._baseLength = copy.deepcopy(baseLength)
        except Exception as exc:
            raise ValueError("Invalid baseLength : " + str(exc))

    # ===> Attribute phaseRms

    _phaseRms = None  # this is a 1D list of Angle

    def getPhaseRms(self):
        """
        Get phaseRms.
        return phaseRms as Angle []
        """

        return copy.deepcopy(self._phaseRms)

    def setPhaseRms(self, phaseRms):
        """
        Set phaseRms with the specified Angle []  value.
        phaseRms The Angle []  value to which phaseRms is to be set.
        The value of phaseRms can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(phaseRms, list):
            raise ValueError("The value of phaseRms must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(phaseRms)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of phaseRms is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(phaseRms, Angle):
                raise ValueError(
                    "type of the first value in phaseRms is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phaseRms = copy.deepcopy(phaseRms)
        except Exception as exc:
            raise ValueError("Invalid phaseRms : " + str(exc))

    # ===> Attribute seeing

    _seeing = None

    def getSeeing(self):
        """
        Get seeing.
        return seeing as float
        """

        return self._seeing

    def setSeeing(self, seeing):
        """
        Set seeing with the specified float value.
        seeing The float value to which seeing is to be set.


        """

        self._seeing = float(seeing)

    # ===> Attribute exponent

    _exponent = None

    def getExponent(self):
        """
        Get exponent.
        return exponent as float
        """

        return self._exponent

    def setExponent(self, exponent):
        """
        Set exponent with the specified float value.
        exponent The float value to which exponent is to be set.


        """

        self._exponent = float(exponent)

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(
        self, timeInterval, numBaseLength, baseLength, phaseRms, seeing, exponent
    ):
        """
        Compare each attribute except the autoincrementable one of this SeeingRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # numBaseLength is a int, compare using the == operator.
        if not (self._numBaseLength == numBaseLength):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._baseLength) != len(baseLength):
            return False
        for indx in range(len(baseLength)):

            # baseLength is a list of Length, compare using the almostEquals method.
            if not self._baseLength[indx].almostEquals(
                baseLength[indx], self.getTable().getBaseLengthEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseRms) != len(phaseRms):
            return False
        for indx in range(len(phaseRms)):

            # phaseRms is a list of Angle, compare using the almostEquals method.
            if not self._phaseRms[indx].almostEquals(
                phaseRms[indx], self.getTable().getPhaseRmsEqTolerance()
            ):
                return False

        # seeing is a float, compare using the == operator.
        if not (self._seeing == seeing):
            return False

        # exponent is a float, compare using the == operator.
        if not (self._exponent == exponent):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumBaseLength(),
            otherRow.getBaseLength(),
            otherRow.getPhaseRms(),
            otherRow.getSeeing(),
            otherRow.getExponent(),
        )

    def compareRequiredValue(
        self, numBaseLength, baseLength, phaseRms, seeing, exponent
    ):

        # numBaseLength is a int, compare using the == operator.
        if not (self._numBaseLength == numBaseLength):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._baseLength) != len(baseLength):
            return False
        for indx in range(len(baseLength)):

            # baseLength is a list of Length, compare using the almostEquals method.
            if not self._baseLength[indx].almostEquals(
                baseLength[indx], self.getTable().getBaseLengthEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseRms) != len(phaseRms):
            return False
        for indx in range(len(phaseRms)):

            # phaseRms is a list of Angle, compare using the almostEquals method.
            if not self._phaseRms[indx].almostEquals(
                phaseRms[indx], self.getTable().getPhaseRmsEqTolerance()
            ):
                return False

        # seeing is a float, compare using the == operator.
        if not (self._seeing == seeing):
            return False

        # exponent is a float, compare using the == operator.
        if not (self._exponent == exponent):
            return False

        return True


# initialize the dictionary that maps fields to init methods
SeeingRow.initFromBinMethods()
