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
# File PulsarRow.py
#

import pyasdm.PulsarTable

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


class PulsarRow:
    """
    The PulsarRow class is a row of a PulsarTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a PulsarRow.
        When row is None, create an empty row attached to table, which must be a PulsarTable.
        When row is given, copy those values in to the new row. The row argument must be a PulsarRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.PulsarTable):
            raise ValueError("table must be a PulsarTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._pulsarId = Tag()

        self._refTime = ArrayTime()

        self._refPulseFreq = Frequency()

        self._refPhase = None

        self._numBin = 0

        self._numPolyExists = False

        self._numPoly = 0

        self._phasePolyExists = False

        self._phasePoly = []  # this is a list of float []

        self._timeSpanExists = False

        self._timeSpan = Interval()

        self._startPhaseBinExists = False

        self._startPhaseBin = []  # this is a list of float []

        self._endPhaseBinExists = False

        self._endPhaseBin = []  # this is a list of float []

        self._dispersionMeasureExists = False

        self._dispersionMeasure = None

        self._refFrequencyExists = False

        self._refFrequency = Frequency()

        if row is not None:
            if not isinstance(row, PulsarRow):
                raise ValueError("row must be a PulsarRow")

            # copy constructor

            self._pulsarId = Tag(row._pulsarId)

            self._refTime = ArrayTime(row._refTime)

            self._refPulseFreq = Frequency(row._refPulseFreq)

            self._refPhase = row._refPhase

            self._numBin = row._numBin

            # by default set systematically numPoly's value to something not None

            if row._numPolyExists:

                self._numPoly = row._numPoly

                self._numPolyExists = True

            # by default set systematically phasePoly's value to something not None

            if row._phasePolyExists:

                # phasePoly is a list, make a deep copy
                self.phasePoly = copy.deepcopy(row.phasePoly)

                self._phasePolyExists = True

            # by default set systematically timeSpan's value to something not None

            if row._timeSpanExists:

                self._timeSpan = Interval(row._timeSpan)

                self._timeSpanExists = True

            # by default set systematically startPhaseBin's value to something not None

            if row._startPhaseBinExists:

                # startPhaseBin is a list, make a deep copy
                self.startPhaseBin = copy.deepcopy(row.startPhaseBin)

                self._startPhaseBinExists = True

            # by default set systematically endPhaseBin's value to something not None

            if row._endPhaseBinExists:

                # endPhaseBin is a list, make a deep copy
                self.endPhaseBin = copy.deepcopy(row.endPhaseBin)

                self._endPhaseBinExists = True

            # by default set systematically dispersionMeasure's value to something not None

            if row._dispersionMeasureExists:

                self._dispersionMeasure = row._dispersionMeasure

                self._dispersionMeasureExists = True

            # by default set systematically refFrequency's value to something not None

            if row._refFrequencyExists:

                self._refFrequency = Frequency(row._refFrequency)

                self._refFrequencyExists = True

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

        result += Parser.extendedValueToXML("pulsarId", self._pulsarId)

        result += Parser.extendedValueToXML("refTime", self._refTime)

        result += Parser.extendedValueToXML("refPulseFreq", self._refPulseFreq)

        result += Parser.valueToXML("refPhase", self._refPhase)

        result += Parser.valueToXML("numBin", self._numBin)

        if self._numPolyExists:

            result += Parser.valueToXML("numPoly", self._numPoly)

        if self._phasePolyExists:

            result += Parser.listValueToXML("phasePoly", self._phasePoly)

        if self._timeSpanExists:

            result += Parser.extendedValueToXML("timeSpan", self._timeSpan)

        if self._startPhaseBinExists:

            result += Parser.listValueToXML("startPhaseBin", self._startPhaseBin)

        if self._endPhaseBinExists:

            result += Parser.listValueToXML("endPhaseBin", self._endPhaseBin)

        if self._dispersionMeasureExists:

            result += Parser.valueToXML("dispersionMeasure", self._dispersionMeasure)

        if self._refFrequencyExists:

            result += Parser.extendedValueToXML("refFrequency", self._refFrequency)

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
                "xmlrow is not a string or a minidom.Element", "PulsarTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "PulsarTable")

        # intrinsic attribute values

        pulsarIdNode = rowdom.getElementsByTagName("pulsarId")[0]

        self._pulsarId = Tag(pulsarIdNode.firstChild.data.strip())

        refTimeNode = rowdom.getElementsByTagName("refTime")[0]

        self._refTime = ArrayTime(refTimeNode.firstChild.data.strip())

        refPulseFreqNode = rowdom.getElementsByTagName("refPulseFreq")[0]

        self._refPulseFreq = Frequency(refPulseFreqNode.firstChild.data.strip())

        refPhaseNode = rowdom.getElementsByTagName("refPhase")[0]

        self._refPhase = float(refPhaseNode.firstChild.data.strip())

        numBinNode = rowdom.getElementsByTagName("numBin")[0]

        self._numBin = int(numBinNode.firstChild.data.strip())

        numPolyNode = rowdom.getElementsByTagName("numPoly")
        if len(numPolyNode) > 0:

            self._numPoly = int(numPolyNode[0].firstChild.data.strip())

            self._numPolyExists = True

        phasePolyNode = rowdom.getElementsByTagName("phasePoly")
        if len(phasePolyNode) > 0:

            phasePolyStr = phasePolyNode[0].firstChild.data.strip()

            self._phasePoly = Parser.stringListToLists(
                phasePolyStr, float, "Pulsar", False
            )

            self._phasePolyExists = True

        timeSpanNode = rowdom.getElementsByTagName("timeSpan")
        if len(timeSpanNode) > 0:

            self._timeSpan = Interval(timeSpanNode[0].firstChild.data.strip())

            self._timeSpanExists = True

        startPhaseBinNode = rowdom.getElementsByTagName("startPhaseBin")
        if len(startPhaseBinNode) > 0:

            startPhaseBinStr = startPhaseBinNode[0].firstChild.data.strip()

            self._startPhaseBin = Parser.stringListToLists(
                startPhaseBinStr, float, "Pulsar", False
            )

            self._startPhaseBinExists = True

        endPhaseBinNode = rowdom.getElementsByTagName("endPhaseBin")
        if len(endPhaseBinNode) > 0:

            endPhaseBinStr = endPhaseBinNode[0].firstChild.data.strip()

            self._endPhaseBin = Parser.stringListToLists(
                endPhaseBinStr, float, "Pulsar", False
            )

            self._endPhaseBinExists = True

        dispersionMeasureNode = rowdom.getElementsByTagName("dispersionMeasure")
        if len(dispersionMeasureNode) > 0:

            self._dispersionMeasure = float(
                dispersionMeasureNode[0].firstChild.data.strip()
            )

            self._dispersionMeasureExists = True

        refFrequencyNode = rowdom.getElementsByTagName("refFrequency")
        if len(refFrequencyNode) > 0:

            self._refFrequency = Frequency(refFrequencyNode[0].firstChild.data.strip())

            self._refFrequencyExists = True

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._pulsarId.toBin(eos)

        self._refTime.toBin(eos)

        self._refPulseFreq.toBin(eos)

        eos.writeFloat(self._refPhase)

        eos.writeInt(self._numBin)

        eos.writeBool(self._numPolyExists)
        if self._numPolyExists:

            eos.writeInt(self._numPoly)

        eos.writeBool(self._phasePolyExists)
        if self._phasePolyExists:

            eos.writeInt(len(self._phasePoly))
            for i in range(len(self._phasePoly)):

                eos.writeFloat(self._phasePoly[i])

        eos.writeBool(self._timeSpanExists)
        if self._timeSpanExists:

            self._timeSpan.toBin(eos)

        eos.writeBool(self._startPhaseBinExists)
        if self._startPhaseBinExists:

            eos.writeInt(len(self._startPhaseBin))
            for i in range(len(self._startPhaseBin)):

                eos.writeFloat(self._startPhaseBin[i])

        eos.writeBool(self._endPhaseBinExists)
        if self._endPhaseBinExists:

            eos.writeInt(len(self._endPhaseBin))
            for i in range(len(self._endPhaseBin)):

                eos.writeFloat(self._endPhaseBin[i])

        eos.writeBool(self._dispersionMeasureExists)
        if self._dispersionMeasureExists:

            eos.writeFloat(self._dispersionMeasure)

        eos.writeBool(self._refFrequencyExists)
        if self._refFrequencyExists:

            self._refFrequency.toBin(eos)

    @staticmethod
    def pulsarIdFromBin(row, eis):
        """
        Set the pulsarId in row from the EndianInput (eis) instance.
        """

        row._pulsarId = Tag.fromBin(eis)

    @staticmethod
    def refTimeFromBin(row, eis):
        """
        Set the refTime in row from the EndianInput (eis) instance.
        """

        row._refTime = ArrayTime.fromBin(eis)

    @staticmethod
    def refPulseFreqFromBin(row, eis):
        """
        Set the refPulseFreq in row from the EndianInput (eis) instance.
        """

        row._refPulseFreq = Frequency.fromBin(eis)

    @staticmethod
    def refPhaseFromBin(row, eis):
        """
        Set the refPhase in row from the EndianInput (eis) instance.
        """

        row._refPhase = eis.readFloat()

    @staticmethod
    def numBinFromBin(row, eis):
        """
        Set the numBin in row from the EndianInput (eis) instance.
        """

        row._numBin = eis.readInt()

    @staticmethod
    def numPolyFromBin(row, eis):
        """
        Set the optional numPoly in row from the EndianInput (eis) instance.
        """
        row._numPolyExists = eis.readBool()
        if row._numPolyExists:

            row._numPoly = eis.readInt()

    @staticmethod
    def phasePolyFromBin(row, eis):
        """
        Set the optional phasePoly in row from the EndianInput (eis) instance.
        """
        row._phasePolyExists = eis.readBool()
        if row._phasePolyExists:

            phasePolyDim1 = eis.readInt()
            thisList = []
            for i in range(phasePolyDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._phasePoly = thisList

    @staticmethod
    def timeSpanFromBin(row, eis):
        """
        Set the optional timeSpan in row from the EndianInput (eis) instance.
        """
        row._timeSpanExists = eis.readBool()
        if row._timeSpanExists:

            row._timeSpan = Interval.fromBin(eis)

    @staticmethod
    def startPhaseBinFromBin(row, eis):
        """
        Set the optional startPhaseBin in row from the EndianInput (eis) instance.
        """
        row._startPhaseBinExists = eis.readBool()
        if row._startPhaseBinExists:

            startPhaseBinDim1 = eis.readInt()
            thisList = []
            for i in range(startPhaseBinDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._startPhaseBin = thisList

    @staticmethod
    def endPhaseBinFromBin(row, eis):
        """
        Set the optional endPhaseBin in row from the EndianInput (eis) instance.
        """
        row._endPhaseBinExists = eis.readBool()
        if row._endPhaseBinExists:

            endPhaseBinDim1 = eis.readInt()
            thisList = []
            for i in range(endPhaseBinDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._endPhaseBin = thisList

    @staticmethod
    def dispersionMeasureFromBin(row, eis):
        """
        Set the optional dispersionMeasure in row from the EndianInput (eis) instance.
        """
        row._dispersionMeasureExists = eis.readBool()
        if row._dispersionMeasureExists:

            row._dispersionMeasure = eis.readFloat()

    @staticmethod
    def refFrequencyFromBin(row, eis):
        """
        Set the optional refFrequency in row from the EndianInput (eis) instance.
        """
        row._refFrequencyExists = eis.readBool()
        if row._refFrequencyExists:

            row._refFrequency = Frequency.fromBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["pulsarId"] = PulsarRow.pulsarIdFromBin
        _fromBinMethods["refTime"] = PulsarRow.refTimeFromBin
        _fromBinMethods["refPulseFreq"] = PulsarRow.refPulseFreqFromBin
        _fromBinMethods["refPhase"] = PulsarRow.refPhaseFromBin
        _fromBinMethods["numBin"] = PulsarRow.numBinFromBin

        _fromBinMethods["numPoly"] = PulsarRow.numPolyFromBin
        _fromBinMethods["phasePoly"] = PulsarRow.phasePolyFromBin
        _fromBinMethods["timeSpan"] = PulsarRow.timeSpanFromBin
        _fromBinMethods["startPhaseBin"] = PulsarRow.startPhaseBinFromBin
        _fromBinMethods["endPhaseBin"] = PulsarRow.endPhaseBinFromBin
        _fromBinMethods["dispersionMeasure"] = PulsarRow.dispersionMeasureFromBin
        _fromBinMethods["refFrequency"] = PulsarRow.refFrequencyFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = PulsarRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Pulsar",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute pulsarId

    _pulsarId = Tag()

    def getPulsarId(self):
        """
        Get pulsarId.
        return pulsarId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._pulsarId)

    def setPulsarId(self, pulsarId):
        """
        Set pulsarId with the specified Tag value.
        pulsarId The Tag value to which pulsarId is to be set.
        The value of pulsarId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the pulsarId field, which is part of the key, after this row has been added to this table."
            )

        self._pulsarId = Tag(pulsarId)

    # ===> Attribute refTime

    _refTime = ArrayTime()

    def getRefTime(self):
        """
        Get refTime.
        return refTime as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._refTime)

    def setRefTime(self, refTime):
        """
        Set refTime with the specified ArrayTime value.
        refTime The ArrayTime value to which refTime is to be set.
        The value of refTime can be anything allowed by the ArrayTime constructor.

        """

        self._refTime = ArrayTime(refTime)

    # ===> Attribute refPulseFreq

    _refPulseFreq = Frequency()

    def getRefPulseFreq(self):
        """
        Get refPulseFreq.
        return refPulseFreq as Frequency
        """

        # make sure it is a copy of Frequency
        return Frequency(self._refPulseFreq)

    def setRefPulseFreq(self, refPulseFreq):
        """
        Set refPulseFreq with the specified Frequency value.
        refPulseFreq The Frequency value to which refPulseFreq is to be set.
        The value of refPulseFreq can be anything allowed by the Frequency constructor.

        """

        self._refPulseFreq = Frequency(refPulseFreq)

    # ===> Attribute refPhase

    _refPhase = None

    def getRefPhase(self):
        """
        Get refPhase.
        return refPhase as float
        """

        return self._refPhase

    def setRefPhase(self, refPhase):
        """
        Set refPhase with the specified float value.
        refPhase The float value to which refPhase is to be set.


        """

        self._refPhase = float(refPhase)

    # ===> Attribute numBin

    _numBin = 0

    def getNumBin(self):
        """
        Get numBin.
        return numBin as int
        """

        return self._numBin

    def setNumBin(self, numBin):
        """
        Set numBin with the specified int value.
        numBin The int value to which numBin is to be set.


        """

        self._numBin = int(numBin)

    # ===> Attribute numPoly, which is optional
    _numPolyExists = False

    _numPoly = 0

    def isNumPolyExists(self):
        """
        The attribute numPoly is optional. Return True if this attribute exists.
        return True if and only if the numPoly attribute exists.
        """
        return self._numPolyExists

    def getNumPoly(self):
        """
        Get numPoly, which is optional.
        return numPoly as int
        raises ValueError If numPoly does not exist.
        """
        if not self._numPolyExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numPoly
                + " attribute in table Pulsar does not exist!"
            )

        return self._numPoly

    def setNumPoly(self, numPoly):
        """
        Set numPoly with the specified int value.
        numPoly The int value to which numPoly is to be set.


        """

        self._numPoly = int(numPoly)

        self._numPolyExists = True

    def clearNumPoly(self):
        """
        Mark numPoly, which is an optional field, as non-existent.
        """
        self._numPolyExists = False

    # ===> Attribute phasePoly, which is optional
    _phasePolyExists = False

    _phasePoly = None  # this is a 1D list of float

    def isPhasePolyExists(self):
        """
        The attribute phasePoly is optional. Return True if this attribute exists.
        return True if and only if the phasePoly attribute exists.
        """
        return self._phasePolyExists

    def getPhasePoly(self):
        """
        Get phasePoly, which is optional.
        return phasePoly as float []
        raises ValueError If phasePoly does not exist.
        """
        if not self._phasePolyExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + phasePoly
                + " attribute in table Pulsar does not exist!"
            )

        return copy.deepcopy(self._phasePoly)

    def setPhasePoly(self, phasePoly):
        """
        Set phasePoly with the specified float []  value.
        phasePoly The float []  value to which phasePoly is to be set.


        """

        # value must be a list
        if not isinstance(phasePoly, list):
            raise ValueError("The value of phasePoly must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(phasePoly)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of phasePoly is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(phasePoly, float):
                raise ValueError(
                    "type of the first value in phasePoly is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phasePoly = copy.deepcopy(phasePoly)
        except Exception as exc:
            raise ValueError("Invalid phasePoly : " + str(exc))

        self._phasePolyExists = True

    def clearPhasePoly(self):
        """
        Mark phasePoly, which is an optional field, as non-existent.
        """
        self._phasePolyExists = False

    # ===> Attribute timeSpan, which is optional
    _timeSpanExists = False

    _timeSpan = Interval()

    def isTimeSpanExists(self):
        """
        The attribute timeSpan is optional. Return True if this attribute exists.
        return True if and only if the timeSpan attribute exists.
        """
        return self._timeSpanExists

    def getTimeSpan(self):
        """
        Get timeSpan, which is optional.
        return timeSpan as Interval
        raises ValueError If timeSpan does not exist.
        """
        if not self._timeSpanExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + timeSpan
                + " attribute in table Pulsar does not exist!"
            )

        # make sure it is a copy of Interval
        return Interval(self._timeSpan)

    def setTimeSpan(self, timeSpan):
        """
        Set timeSpan with the specified Interval value.
        timeSpan The Interval value to which timeSpan is to be set.
        The value of timeSpan can be anything allowed by the Interval constructor.

        """

        self._timeSpan = Interval(timeSpan)

        self._timeSpanExists = True

    def clearTimeSpan(self):
        """
        Mark timeSpan, which is an optional field, as non-existent.
        """
        self._timeSpanExists = False

    # ===> Attribute startPhaseBin, which is optional
    _startPhaseBinExists = False

    _startPhaseBin = None  # this is a 1D list of float

    def isStartPhaseBinExists(self):
        """
        The attribute startPhaseBin is optional. Return True if this attribute exists.
        return True if and only if the startPhaseBin attribute exists.
        """
        return self._startPhaseBinExists

    def getStartPhaseBin(self):
        """
        Get startPhaseBin, which is optional.
        return startPhaseBin as float []
        raises ValueError If startPhaseBin does not exist.
        """
        if not self._startPhaseBinExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + startPhaseBin
                + " attribute in table Pulsar does not exist!"
            )

        return copy.deepcopy(self._startPhaseBin)

    def setStartPhaseBin(self, startPhaseBin):
        """
        Set startPhaseBin with the specified float []  value.
        startPhaseBin The float []  value to which startPhaseBin is to be set.


        """

        # value must be a list
        if not isinstance(startPhaseBin, list):
            raise ValueError("The value of startPhaseBin must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(startPhaseBin)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of startPhaseBin is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(startPhaseBin, float):
                raise ValueError(
                    "type of the first value in startPhaseBin is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._startPhaseBin = copy.deepcopy(startPhaseBin)
        except Exception as exc:
            raise ValueError("Invalid startPhaseBin : " + str(exc))

        self._startPhaseBinExists = True

    def clearStartPhaseBin(self):
        """
        Mark startPhaseBin, which is an optional field, as non-existent.
        """
        self._startPhaseBinExists = False

    # ===> Attribute endPhaseBin, which is optional
    _endPhaseBinExists = False

    _endPhaseBin = None  # this is a 1D list of float

    def isEndPhaseBinExists(self):
        """
        The attribute endPhaseBin is optional. Return True if this attribute exists.
        return True if and only if the endPhaseBin attribute exists.
        """
        return self._endPhaseBinExists

    def getEndPhaseBin(self):
        """
        Get endPhaseBin, which is optional.
        return endPhaseBin as float []
        raises ValueError If endPhaseBin does not exist.
        """
        if not self._endPhaseBinExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + endPhaseBin
                + " attribute in table Pulsar does not exist!"
            )

        return copy.deepcopy(self._endPhaseBin)

    def setEndPhaseBin(self, endPhaseBin):
        """
        Set endPhaseBin with the specified float []  value.
        endPhaseBin The float []  value to which endPhaseBin is to be set.


        """

        # value must be a list
        if not isinstance(endPhaseBin, list):
            raise ValueError("The value of endPhaseBin must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(endPhaseBin)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of endPhaseBin is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(endPhaseBin, float):
                raise ValueError(
                    "type of the first value in endPhaseBin is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._endPhaseBin = copy.deepcopy(endPhaseBin)
        except Exception as exc:
            raise ValueError("Invalid endPhaseBin : " + str(exc))

        self._endPhaseBinExists = True

    def clearEndPhaseBin(self):
        """
        Mark endPhaseBin, which is an optional field, as non-existent.
        """
        self._endPhaseBinExists = False

    # ===> Attribute dispersionMeasure, which is optional
    _dispersionMeasureExists = False

    _dispersionMeasure = None

    def isDispersionMeasureExists(self):
        """
        The attribute dispersionMeasure is optional. Return True if this attribute exists.
        return True if and only if the dispersionMeasure attribute exists.
        """
        return self._dispersionMeasureExists

    def getDispersionMeasure(self):
        """
        Get dispersionMeasure, which is optional.
        return dispersionMeasure as float
        raises ValueError If dispersionMeasure does not exist.
        """
        if not self._dispersionMeasureExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + dispersionMeasure
                + " attribute in table Pulsar does not exist!"
            )

        return self._dispersionMeasure

    def setDispersionMeasure(self, dispersionMeasure):
        """
        Set dispersionMeasure with the specified float value.
        dispersionMeasure The float value to which dispersionMeasure is to be set.


        """

        self._dispersionMeasure = float(dispersionMeasure)

        self._dispersionMeasureExists = True

    def clearDispersionMeasure(self):
        """
        Mark dispersionMeasure, which is an optional field, as non-existent.
        """
        self._dispersionMeasureExists = False

    # ===> Attribute refFrequency, which is optional
    _refFrequencyExists = False

    _refFrequency = Frequency()

    def isRefFrequencyExists(self):
        """
        The attribute refFrequency is optional. Return True if this attribute exists.
        return True if and only if the refFrequency attribute exists.
        """
        return self._refFrequencyExists

    def getRefFrequency(self):
        """
        Get refFrequency, which is optional.
        return refFrequency as Frequency
        raises ValueError If refFrequency does not exist.
        """
        if not self._refFrequencyExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + refFrequency
                + " attribute in table Pulsar does not exist!"
            )

        # make sure it is a copy of Frequency
        return Frequency(self._refFrequency)

    def setRefFrequency(self, refFrequency):
        """
        Set refFrequency with the specified Frequency value.
        refFrequency The Frequency value to which refFrequency is to be set.
        The value of refFrequency can be anything allowed by the Frequency constructor.

        """

        self._refFrequency = Frequency(refFrequency)

        self._refFrequencyExists = True

    def clearRefFrequency(self):
        """
        Mark refFrequency, which is an optional field, as non-existent.
        """
        self._refFrequencyExists = False

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(self, refTime, refPulseFreq, refPhase, numBin):
        """
        Compare each attribute except the autoincrementable one of this PulsarRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # refTime is a ArrayTime, compare using the equals method.
        if not self._refTime.equals(refTime):
            return False

        # refPulseFreq is a Frequency, compare using the almostEquals method.
        if not self._refPulseFreq.almostEquals(
            refPulseFreq, self.getTable().getRefPulseFreqEqTolerance()
        ):
            return False

        # refPhase is a float, compare using the == operator.
        if not (self._refPhase == refPhase):
            return False

        # numBin is a int, compare using the == operator.
        if not (self._numBin == numBin):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getRefTime(),
            otherRow.getRefPulseFreq(),
            otherRow.getRefPhase(),
            otherRow.getNumBin(),
        )

    def compareRequiredValue(self, refTime, refPulseFreq, refPhase, numBin):

        # refTime is a ArrayTime, compare using the equals method.
        if not self._refTime.equals(refTime):
            return False

        # refPulseFreq is a Frequency, compare using the almostEquals method.
        if not self._refPulseFreq.almostEquals(
            refPulseFreq, self.getTable().getRefPulseFreqEqTolerance()
        ):
            return False

        # refPhase is a float, compare using the == operator.
        if not (self._refPhase == refPhase):
            return False

        # numBin is a int, compare using the == operator.
        if not (self._numBin == numBin):
            return False

        return True


# initialize the dictionary that maps fields to init methods
PulsarRow.initFromBinMethods()
