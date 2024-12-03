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

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


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
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        if row is not None:
            if not isinstance(row, PulsarRow):
                raise ValueError("row must be a MainRow")

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

        self._pulsarId = Tag(pulsarIdNode.firstChild.data)

        refTimeNode = rowdom.getElementsByTagName("refTime")[0]

        self._refTime = ArrayTime(refTimeNode.firstChild.data)

        refPulseFreqNode = rowdom.getElementsByTagName("refPulseFreq")[0]

        self._refPulseFreq = Frequency(refPulseFreqNode.firstChild.data)

        refPhaseNode = rowdom.getElementsByTagName("refPhase")[0]

        self._refPhase = double(refPhaseNode.firstChild.data)

        numBinNode = rowdom.getElementsByTagName("numBin")[0]

        self._numBin = int(numBinNode.firstChild.data)

        numPolyNode = rowdom.getElementsByTagName("numPoly")
        if len(numPolyNode) > 0:

            self._numPoly = int(numPolyNode[0].firstChild.data)

            self._numPolyExists = True

        phasePolyNode = rowdom.getElementsByTagName("phasePoly")
        if len(phasePolyNode) > 0:

            phasePolyStr = phasePolyNode[0].firstChild.data
            self._phasePoly = Parser.stringListToLists(phasePolyStr, double, "Pulsar")

            self._phasePolyExists = True

        timeSpanNode = rowdom.getElementsByTagName("timeSpan")
        if len(timeSpanNode) > 0:

            self._timeSpan = Interval(timeSpanNode[0].firstChild.data)

            self._timeSpanExists = True

        startPhaseBinNode = rowdom.getElementsByTagName("startPhaseBin")
        if len(startPhaseBinNode) > 0:

            startPhaseBinStr = startPhaseBinNode[0].firstChild.data
            self._startPhaseBin = Parser.stringListToLists(
                startPhaseBinStr, float, "Pulsar"
            )

            self._startPhaseBinExists = True

        endPhaseBinNode = rowdom.getElementsByTagName("endPhaseBin")
        if len(endPhaseBinNode) > 0:

            endPhaseBinStr = endPhaseBinNode[0].firstChild.data
            self._endPhaseBin = Parser.stringListToLists(
                endPhaseBinStr, float, "Pulsar"
            )

            self._endPhaseBinExists = True

        dispersionMeasureNode = rowdom.getElementsByTagName("dispersionMeasure")
        if len(dispersionMeasureNode) > 0:

            self._dispersionMeasure = double(dispersionMeasureNode[0].firstChild.data)

            self._dispersionMeasureExists = True

        refFrequencyNode = rowdom.getElementsByTagName("refFrequency")
        if len(refFrequencyNode) > 0:

            self._refFrequency = Frequency(refFrequencyNode[0].firstChild.data)

            self._refFrequencyExists = True

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

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
        return refPhase as double
        """

        return self._refPhase

    def setRefPhase(self, refPhase):
        """
        Set refPhase with the specified double value.
        refPhase The double value to which refPhase is to be set.


        """

        self._refPhase = double(refPhase)

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

    _phasePoly = None  # this is a 1D list of double

    def isPhasePolyExists(self):
        """
        The attribute phasePoly is optional. Return True if this attribute exists.
        return True if and only if the phasePoly attribute exists.
        """
        return self._phasePolyExists

    def getPhasePoly(self):
        """
        Get phasePoly, which is optional.
        return phasePoly as double []
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
        Set phasePoly with the specified double []  value.
        phasePoly The double []  value to which phasePoly is to be set.


        """

        # value must be a list
        if not isinstance(phasePoly, list):
            raise ValueError("The value of phasePoly must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(phasePoly)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of phasePoly is not correct")

            # the type of the values in the list must be double
            # note : this only checks the first value found
            if not Parser.checkListType(phasePoly, double):
                raise ValueError(
                    "type of the first value in phasePoly is not double as expected"
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
            listDims = Parser.getListDims(startPhaseBin)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of startPhaseBin is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(startPhaseBin, float):
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
            listDims = Parser.getListDims(endPhaseBin)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of endPhaseBin is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(endPhaseBin, float):
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
        return dispersionMeasure as double
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
        Set dispersionMeasure with the specified double value.
        dispersionMeasure The double value to which dispersionMeasure is to be set.


        """

        self._dispersionMeasure = double(dispersionMeasure)

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

        # refPhase is a double, compare using the == operator.
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

        # refPhase is a double, compare using the == operator.
        if not (self._refPhase == refPhase):
            return False

        # numBin is a int, compare using the == operator.
        if not (self._numBin == numBin):
            return False

        return True
