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
# File CalSeeingRow.py
#

import pyasdm.CalSeeingTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.AtmPhaseCorrection import AtmPhaseCorrection


from xml.dom import minidom

import copy


class CalSeeingRow:
    """
    The CalSeeingRow class is a row of a CalSeeingTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalSeeingRow.
        When row is None, create an empty row attached to table, which must be a CalSeeingTable.
        When row is given, copy those values in to the new row. The row argument must be a CalSeeingRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalSeeingTable):
            raise ValueError("table must be a CalSeeingTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._frequencyRange = []  # this is a list of Frequency []

        self._integrationTime = Interval()

        self._numBaseLengths = 0

        self._baselineLengths = []  # this is a list of Length []

        self._phaseRMS = []  # this is a list of Angle []

        self._seeing = Angle()

        self._seeingError = Angle()

        self._exponentExists = False

        self._exponent = None

        self._outerScaleExists = False

        self._outerScale = Length()

        self._outerScaleRMSExists = False

        self._outerScaleRMS = Angle()

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalSeeingRow):
                raise ValueError("row must be a CalSeeingRow")

            # copy constructor

            # We force the attribute of the result to be not None.
            if row._atmPhaseCorrection is None:
                self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)
            else:
                self._atmPhaseCorrection = AtmPhaseCorrection(row._atmPhaseCorrection)

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            # frequencyRange is a  list , make a deep copy
            self._frequencyRange = copy.deepcopy(row._frequencyRange)

            self._integrationTime = Interval(row._integrationTime)

            self._numBaseLengths = row._numBaseLengths

            # baselineLengths is a  list , make a deep copy
            self._baselineLengths = copy.deepcopy(row._baselineLengths)

            # phaseRMS is a  list , make a deep copy
            self._phaseRMS = copy.deepcopy(row._phaseRMS)

            self._seeing = Angle(row._seeing)

            self._seeingError = Angle(row._seeingError)

            # by default set systematically exponent's value to something not None

            if row._exponentExists:

                self._exponent = row._exponent

                self._exponentExists = True

            # by default set systematically outerScale's value to something not None

            if row._outerScaleExists:

                self._outerScale = Length(row._outerScale)

                self._outerScaleExists = True

            # by default set systematically outerScaleRMS's value to something not None

            if row._outerScaleRMSExists:

                self._outerScaleRMS = Angle(row._outerScaleRMS)

                self._outerScaleRMSExists = True

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

        result += Parser.valueToXML(
            "atmPhaseCorrection", AtmPhaseCorrection.name(self._atmPhaseCorrection)
        )

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.listExtendedValueToXML("frequencyRange", self._frequencyRange)

        result += Parser.extendedValueToXML("integrationTime", self._integrationTime)

        result += Parser.valueToXML("numBaseLengths", self._numBaseLengths)

        result += Parser.listExtendedValueToXML(
            "baselineLengths", self._baselineLengths
        )

        result += Parser.listExtendedValueToXML("phaseRMS", self._phaseRMS)

        result += Parser.extendedValueToXML("seeing", self._seeing)

        result += Parser.extendedValueToXML("seeingError", self._seeingError)

        if self._exponentExists:

            result += Parser.valueToXML("exponent", self._exponent)

        if self._outerScaleExists:

            result += Parser.extendedValueToXML("outerScale", self._outerScale)

        if self._outerScaleRMSExists:

            result += Parser.extendedValueToXML("outerScaleRMS", self._outerScaleRMS)

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
                "xmlrow is not a string or a minidom.Element", "CalSeeingTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalSeeingTable")

        # intrinsic attribute values

        atmPhaseCorrectionNode = rowdom.getElementsByTagName("atmPhaseCorrection")[0]

        self._atmPhaseCorrection = AtmPhaseCorrection.newAtmPhaseCorrection(
            atmPhaseCorrectionNode.firstChild.data.strip()
        )

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        frequencyRangeNode = rowdom.getElementsByTagName("frequencyRange")[0]

        frequencyRangeStr = frequencyRangeNode.firstChild.data.strip()

        self._frequencyRange = Parser.stringListToLists(
            frequencyRangeStr, Frequency, "CalSeeing", True
        )

        integrationTimeNode = rowdom.getElementsByTagName("integrationTime")[0]

        self._integrationTime = Interval(integrationTimeNode.firstChild.data.strip())

        numBaseLengthsNode = rowdom.getElementsByTagName("numBaseLengths")[0]

        self._numBaseLengths = int(numBaseLengthsNode.firstChild.data.strip())

        baselineLengthsNode = rowdom.getElementsByTagName("baselineLengths")[0]

        baselineLengthsStr = baselineLengthsNode.firstChild.data.strip()

        self._baselineLengths = Parser.stringListToLists(
            baselineLengthsStr, Length, "CalSeeing", True
        )

        phaseRMSNode = rowdom.getElementsByTagName("phaseRMS")[0]

        phaseRMSStr = phaseRMSNode.firstChild.data.strip()

        self._phaseRMS = Parser.stringListToLists(phaseRMSStr, Angle, "CalSeeing", True)

        seeingNode = rowdom.getElementsByTagName("seeing")[0]

        self._seeing = Angle(seeingNode.firstChild.data.strip())

        seeingErrorNode = rowdom.getElementsByTagName("seeingError")[0]

        self._seeingError = Angle(seeingErrorNode.firstChild.data.strip())

        exponentNode = rowdom.getElementsByTagName("exponent")
        if len(exponentNode) > 0:

            self._exponent = float(exponentNode[0].firstChild.data.strip())

            self._exponentExists = True

        outerScaleNode = rowdom.getElementsByTagName("outerScale")
        if len(outerScaleNode) > 0:

            self._outerScale = Length(outerScaleNode[0].firstChild.data.strip())

            self._outerScaleExists = True

        outerScaleRMSNode = rowdom.getElementsByTagName("outerScaleRMS")
        if len(outerScaleRMSNode) > 0:

            self._outerScaleRMS = Angle(outerScaleRMSNode[0].firstChild.data.strip())

            self._outerScaleRMSExists = True

        # extrinsic attribute values

        calDataIdNode = rowdom.getElementsByTagName("calDataId")[0]

        self._calDataId = Tag(calDataIdNode.firstChild.data.strip())

        calReductionIdNode = rowdom.getElementsByTagName("calReductionId")[0]

        self._calReductionId = Tag(calReductionIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        eos.writeString(str(self._atmPhaseCorrection))

        self._calDataId.toBin(eos)

        self._calReductionId.toBin(eos)

        self._startValidTime.toBin(eos)

        self._endValidTime.toBin(eos)

        Frequency.listToBin(self._frequencyRange, eos)

        self._integrationTime.toBin(eos)

        eos.writeInt(self._numBaseLengths)

        Length.listToBin(self._baselineLengths, eos)

        Angle.listToBin(self._phaseRMS, eos)

        self._seeing.toBin(eos)

        self._seeingError.toBin(eos)

        eos.writeBool(self._exponentExists)
        if self._exponentExists:

            eos.writeFloat(self._exponent)

        eos.writeBool(self._outerScaleExists)
        if self._outerScaleExists:

            self._outerScale.toBin(eos)

        eos.writeBool(self._outerScaleRMSExists)
        if self._outerScaleRMSExists:

            self._outerScaleRMS.toBin(eos)

    @staticmethod
    def atmPhaseCorrectionFromBin(row, eis):
        """
        Set the atmPhaseCorrection in row from the EndianInput (eis) instance.
        """

        row._atmPhaseCorrection = AtmPhaseCorrection.literal(eis.readString())

    @staticmethod
    def calDataIdFromBin(row, eis):
        """
        Set the calDataId in row from the EndianInput (eis) instance.
        """

        row._calDataId = Tag.fromBin(eis)

    @staticmethod
    def calReductionIdFromBin(row, eis):
        """
        Set the calReductionId in row from the EndianInput (eis) instance.
        """

        row._calReductionId = Tag.fromBin(eis)

    @staticmethod
    def startValidTimeFromBin(row, eis):
        """
        Set the startValidTime in row from the EndianInput (eis) instance.
        """

        row._startValidTime = ArrayTime.fromBin(eis)

    @staticmethod
    def endValidTimeFromBin(row, eis):
        """
        Set the endValidTime in row from the EndianInput (eis) instance.
        """

        row._endValidTime = ArrayTime.fromBin(eis)

    @staticmethod
    def frequencyRangeFromBin(row, eis):
        """
        Set the frequencyRange in row from the EndianInput (eis) instance.
        """

        row._frequencyRange = Frequency.from1DBin(eis)

    @staticmethod
    def integrationTimeFromBin(row, eis):
        """
        Set the integrationTime in row from the EndianInput (eis) instance.
        """

        row._integrationTime = Interval.fromBin(eis)

    @staticmethod
    def numBaseLengthsFromBin(row, eis):
        """
        Set the numBaseLengths in row from the EndianInput (eis) instance.
        """

        row._numBaseLengths = eis.readInt()

    @staticmethod
    def baselineLengthsFromBin(row, eis):
        """
        Set the baselineLengths in row from the EndianInput (eis) instance.
        """

        row._baselineLengths = Length.from1DBin(eis)

    @staticmethod
    def phaseRMSFromBin(row, eis):
        """
        Set the phaseRMS in row from the EndianInput (eis) instance.
        """

        row._phaseRMS = Angle.from1DBin(eis)

    @staticmethod
    def seeingFromBin(row, eis):
        """
        Set the seeing in row from the EndianInput (eis) instance.
        """

        row._seeing = Angle.fromBin(eis)

    @staticmethod
    def seeingErrorFromBin(row, eis):
        """
        Set the seeingError in row from the EndianInput (eis) instance.
        """

        row._seeingError = Angle.fromBin(eis)

    @staticmethod
    def exponentFromBin(row, eis):
        """
        Set the optional exponent in row from the EndianInput (eis) instance.
        """
        row._exponentExists = eis.readBool()
        if row._exponentExists:

            row._exponent = eis.readFloat()

    @staticmethod
    def outerScaleFromBin(row, eis):
        """
        Set the optional outerScale in row from the EndianInput (eis) instance.
        """
        row._outerScaleExists = eis.readBool()
        if row._outerScaleExists:

            row._outerScale = Length.fromBin(eis)

    @staticmethod
    def outerScaleRMSFromBin(row, eis):
        """
        Set the optional outerScaleRMS in row from the EndianInput (eis) instance.
        """
        row._outerScaleRMSExists = eis.readBool()
        if row._outerScaleRMSExists:

            row._outerScaleRMS = Angle.fromBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["atmPhaseCorrection"] = CalSeeingRow.atmPhaseCorrectionFromBin
        _fromBinMethods["calDataId"] = CalSeeingRow.calDataIdFromBin
        _fromBinMethods["calReductionId"] = CalSeeingRow.calReductionIdFromBin
        _fromBinMethods["startValidTime"] = CalSeeingRow.startValidTimeFromBin
        _fromBinMethods["endValidTime"] = CalSeeingRow.endValidTimeFromBin
        _fromBinMethods["frequencyRange"] = CalSeeingRow.frequencyRangeFromBin
        _fromBinMethods["integrationTime"] = CalSeeingRow.integrationTimeFromBin
        _fromBinMethods["numBaseLengths"] = CalSeeingRow.numBaseLengthsFromBin
        _fromBinMethods["baselineLengths"] = CalSeeingRow.baselineLengthsFromBin
        _fromBinMethods["phaseRMS"] = CalSeeingRow.phaseRMSFromBin
        _fromBinMethods["seeing"] = CalSeeingRow.seeingFromBin
        _fromBinMethods["seeingError"] = CalSeeingRow.seeingErrorFromBin

        _fromBinMethods["exponent"] = CalSeeingRow.exponentFromBin
        _fromBinMethods["outerScale"] = CalSeeingRow.outerScaleFromBin
        _fromBinMethods["outerScaleRMS"] = CalSeeingRow.outerScaleRMSFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CalSeeingRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalSeeing",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute atmPhaseCorrection

    _atmPhaseCorrection = AtmPhaseCorrection.from_int(0)

    def getAtmPhaseCorrection(self):
        """
        Get atmPhaseCorrection.
        return atmPhaseCorrection as AtmPhaseCorrection
        """

        return self._atmPhaseCorrection

    def setAtmPhaseCorrection(self, atmPhaseCorrection):
        """
        Set atmPhaseCorrection with the specified AtmPhaseCorrection value.
        atmPhaseCorrection The AtmPhaseCorrection value to which atmPhaseCorrection is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the atmPhaseCorrection field, which is part of the key, after this row has been added to this table."
            )

        self._atmPhaseCorrection = AtmPhaseCorrection(atmPhaseCorrection)

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

    # ===> Attribute frequencyRange

    _frequencyRange = None  # this is a 1D list of Frequency

    def getFrequencyRange(self):
        """
        Get frequencyRange.
        return frequencyRange as Frequency []
        """

        return copy.deepcopy(self._frequencyRange)

    def setFrequencyRange(self, frequencyRange):
        """
        Set frequencyRange with the specified Frequency []  value.
        frequencyRange The Frequency []  value to which frequencyRange is to be set.
        The value of frequencyRange can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(frequencyRange, list):
            raise ValueError("The value of frequencyRange must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(frequencyRange)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of frequencyRange is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(frequencyRange, Frequency):
                raise ValueError(
                    "type of the first value in frequencyRange is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._frequencyRange = copy.deepcopy(frequencyRange)
        except Exception as exc:
            raise ValueError("Invalid frequencyRange : " + str(exc))

    # ===> Attribute integrationTime

    _integrationTime = Interval()

    def getIntegrationTime(self):
        """
        Get integrationTime.
        return integrationTime as Interval
        """

        # make sure it is a copy of Interval
        return Interval(self._integrationTime)

    def setIntegrationTime(self, integrationTime):
        """
        Set integrationTime with the specified Interval value.
        integrationTime The Interval value to which integrationTime is to be set.
        The value of integrationTime can be anything allowed by the Interval constructor.

        """

        self._integrationTime = Interval(integrationTime)

    # ===> Attribute numBaseLengths

    _numBaseLengths = 0

    def getNumBaseLengths(self):
        """
        Get numBaseLengths.
        return numBaseLengths as int
        """

        return self._numBaseLengths

    def setNumBaseLengths(self, numBaseLengths):
        """
        Set numBaseLengths with the specified int value.
        numBaseLengths The int value to which numBaseLengths is to be set.


        """

        self._numBaseLengths = int(numBaseLengths)

    # ===> Attribute baselineLengths

    _baselineLengths = None  # this is a 1D list of Length

    def getBaselineLengths(self):
        """
        Get baselineLengths.
        return baselineLengths as Length []
        """

        return copy.deepcopy(self._baselineLengths)

    def setBaselineLengths(self, baselineLengths):
        """
        Set baselineLengths with the specified Length []  value.
        baselineLengths The Length []  value to which baselineLengths is to be set.
        The value of baselineLengths can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(baselineLengths, list):
            raise ValueError("The value of baselineLengths must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(baselineLengths)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of baselineLengths is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(baselineLengths, Length):
                raise ValueError(
                    "type of the first value in baselineLengths is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._baselineLengths = copy.deepcopy(baselineLengths)
        except Exception as exc:
            raise ValueError("Invalid baselineLengths : " + str(exc))

    # ===> Attribute phaseRMS

    _phaseRMS = None  # this is a 1D list of Angle

    def getPhaseRMS(self):
        """
        Get phaseRMS.
        return phaseRMS as Angle []
        """

        return copy.deepcopy(self._phaseRMS)

    def setPhaseRMS(self, phaseRMS):
        """
        Set phaseRMS with the specified Angle []  value.
        phaseRMS The Angle []  value to which phaseRMS is to be set.
        The value of phaseRMS can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(phaseRMS, list):
            raise ValueError("The value of phaseRMS must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(phaseRMS)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of phaseRMS is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(phaseRMS, Angle):
                raise ValueError(
                    "type of the first value in phaseRMS is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phaseRMS = copy.deepcopy(phaseRMS)
        except Exception as exc:
            raise ValueError("Invalid phaseRMS : " + str(exc))

    # ===> Attribute seeing

    _seeing = Angle()

    def getSeeing(self):
        """
        Get seeing.
        return seeing as Angle
        """

        # make sure it is a copy of Angle
        return Angle(self._seeing)

    def setSeeing(self, seeing):
        """
        Set seeing with the specified Angle value.
        seeing The Angle value to which seeing is to be set.
        The value of seeing can be anything allowed by the Angle constructor.

        """

        self._seeing = Angle(seeing)

    # ===> Attribute seeingError

    _seeingError = Angle()

    def getSeeingError(self):
        """
        Get seeingError.
        return seeingError as Angle
        """

        # make sure it is a copy of Angle
        return Angle(self._seeingError)

    def setSeeingError(self, seeingError):
        """
        Set seeingError with the specified Angle value.
        seeingError The Angle value to which seeingError is to be set.
        The value of seeingError can be anything allowed by the Angle constructor.

        """

        self._seeingError = Angle(seeingError)

    # ===> Attribute exponent, which is optional
    _exponentExists = False

    _exponent = None

    def isExponentExists(self):
        """
        The attribute exponent is optional. Return True if this attribute exists.
        return True if and only if the exponent attribute exists.
        """
        return self._exponentExists

    def getExponent(self):
        """
        Get exponent, which is optional.
        return exponent as float
        raises ValueError If exponent does not exist.
        """
        if not self._exponentExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + exponent
                + " attribute in table CalSeeing does not exist!"
            )

        return self._exponent

    def setExponent(self, exponent):
        """
        Set exponent with the specified float value.
        exponent The float value to which exponent is to be set.


        """

        self._exponent = float(exponent)

        self._exponentExists = True

    def clearExponent(self):
        """
        Mark exponent, which is an optional field, as non-existent.
        """
        self._exponentExists = False

    # ===> Attribute outerScale, which is optional
    _outerScaleExists = False

    _outerScale = Length()

    def isOuterScaleExists(self):
        """
        The attribute outerScale is optional. Return True if this attribute exists.
        return True if and only if the outerScale attribute exists.
        """
        return self._outerScaleExists

    def getOuterScale(self):
        """
        Get outerScale, which is optional.
        return outerScale as Length
        raises ValueError If outerScale does not exist.
        """
        if not self._outerScaleExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + outerScale
                + " attribute in table CalSeeing does not exist!"
            )

        # make sure it is a copy of Length
        return Length(self._outerScale)

    def setOuterScale(self, outerScale):
        """
        Set outerScale with the specified Length value.
        outerScale The Length value to which outerScale is to be set.
        The value of outerScale can be anything allowed by the Length constructor.

        """

        self._outerScale = Length(outerScale)

        self._outerScaleExists = True

    def clearOuterScale(self):
        """
        Mark outerScale, which is an optional field, as non-existent.
        """
        self._outerScaleExists = False

    # ===> Attribute outerScaleRMS, which is optional
    _outerScaleRMSExists = False

    _outerScaleRMS = Angle()

    def isOuterScaleRMSExists(self):
        """
        The attribute outerScaleRMS is optional. Return True if this attribute exists.
        return True if and only if the outerScaleRMS attribute exists.
        """
        return self._outerScaleRMSExists

    def getOuterScaleRMS(self):
        """
        Get outerScaleRMS, which is optional.
        return outerScaleRMS as Angle
        raises ValueError If outerScaleRMS does not exist.
        """
        if not self._outerScaleRMSExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + outerScaleRMS
                + " attribute in table CalSeeing does not exist!"
            )

        # make sure it is a copy of Angle
        return Angle(self._outerScaleRMS)

    def setOuterScaleRMS(self, outerScaleRMS):
        """
        Set outerScaleRMS with the specified Angle value.
        outerScaleRMS The Angle value to which outerScaleRMS is to be set.
        The value of outerScaleRMS can be anything allowed by the Angle constructor.

        """

        self._outerScaleRMS = Angle(outerScaleRMS)

        self._outerScaleRMSExists = True

    def clearOuterScaleRMS(self):
        """
        Mark outerScaleRMS, which is an optional field, as non-existent.
        """
        self._outerScaleRMSExists = False

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

    def getCalDataUsingCalDataId(self):
        """
        Returns the row in the CalData table having CalData.calDataId == calDataId

        """

        return self._table.getContainer().getCalData().getRowByKey(self._calDataId)

    def getCalReductionUsingCalReductionId(self):
        """
        Returns the row in the CalReduction table having CalReduction.calReductionId == calReductionId

        """

        return (
            self._table.getContainer()
            .getCalReduction()
            .getRowByKey(self._calReductionId)
        )

    # comparison methods

    def compareNoAutoInc(
        self,
        atmPhaseCorrection,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        frequencyRange,
        integrationTime,
        numBaseLengths,
        baselineLengths,
        phaseRMS,
        seeing,
        seeingError,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalSeeingRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # atmPhaseCorrection is a AtmPhaseCorrection, compare using the == operator on the getValue() output
        if not (self._atmPhaseCorrection.getValue() == atmPhaseCorrection.getValue()):
            return False

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

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._frequencyRange) != len(frequencyRange):
            return False
        for indx in range(len(frequencyRange)):

            # frequencyRange is a list of Frequency, compare using the almostEquals method.
            if not self._frequencyRange[indx].almostEquals(
                frequencyRange[indx], self.getTable().getFrequencyRangeEqTolerance()
            ):
                return False

        # integrationTime is a Interval, compare using the equals method.
        if not self._integrationTime.equals(integrationTime):
            return False

        # numBaseLengths is a int, compare using the == operator.
        if not (self._numBaseLengths == numBaseLengths):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._baselineLengths) != len(baselineLengths):
            return False
        for indx in range(len(baselineLengths)):

            # baselineLengths is a list of Length, compare using the almostEquals method.
            if not self._baselineLengths[indx].almostEquals(
                baselineLengths[indx], self.getTable().getBaselineLengthsEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseRMS) != len(phaseRMS):
            return False
        for indx in range(len(phaseRMS)):

            # phaseRMS is a list of Angle, compare using the almostEquals method.
            if not self._phaseRMS[indx].almostEquals(
                phaseRMS[indx], self.getTable().getPhaseRMSEqTolerance()
            ):
                return False

        # seeing is a Angle, compare using the almostEquals method.
        if not self._seeing.almostEquals(
            seeing, self.getTable().getSeeingEqTolerance()
        ):
            return False

        # seeingError is a Angle, compare using the almostEquals method.
        if not self._seeingError.almostEquals(
            seeingError, self.getTable().getSeeingErrorEqTolerance()
        ):
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
            otherRow.getFrequencyRange(),
            otherRow.getIntegrationTime(),
            otherRow.getNumBaseLengths(),
            otherRow.getBaselineLengths(),
            otherRow.getPhaseRMS(),
            otherRow.getSeeing(),
            otherRow.getSeeingError(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        frequencyRange,
        integrationTime,
        numBaseLengths,
        baselineLengths,
        phaseRMS,
        seeing,
        seeingError,
    ):

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._frequencyRange) != len(frequencyRange):
            return False
        for indx in range(len(frequencyRange)):

            # frequencyRange is a list of Frequency, compare using the almostEquals method.
            if not self._frequencyRange[indx].almostEquals(
                frequencyRange[indx], self.getTable().getFrequencyRangeEqTolerance()
            ):
                return False

        # integrationTime is a Interval, compare using the equals method.
        if not self._integrationTime.equals(integrationTime):
            return False

        # numBaseLengths is a int, compare using the == operator.
        if not (self._numBaseLengths == numBaseLengths):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._baselineLengths) != len(baselineLengths):
            return False
        for indx in range(len(baselineLengths)):

            # baselineLengths is a list of Length, compare using the almostEquals method.
            if not self._baselineLengths[indx].almostEquals(
                baselineLengths[indx], self.getTable().getBaselineLengthsEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseRMS) != len(phaseRMS):
            return False
        for indx in range(len(phaseRMS)):

            # phaseRMS is a list of Angle, compare using the almostEquals method.
            if not self._phaseRMS[indx].almostEquals(
                phaseRMS[indx], self.getTable().getPhaseRMSEqTolerance()
            ):
                return False

        # seeing is a Angle, compare using the almostEquals method.
        if not self._seeing.almostEquals(
            seeing, self.getTable().getSeeingEqTolerance()
        ):
            return False

        # seeingError is a Angle, compare using the almostEquals method.
        if not self._seeingError.almostEquals(
            seeingError, self.getTable().getSeeingErrorEqTolerance()
        ):
            return False

        return True


# initialize the dictionary that maps fields to init methods
CalSeeingRow.initFromBinMethods()
