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
# File CalCurveRow.py
#

import pyasdm.CalCurveTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.AtmPhaseCorrection import AtmPhaseCorrection


from pyasdm.enumerations.CalCurveType import CalCurveType


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.PolarizationType import PolarizationType


from xml.dom import minidom

import copy


class CalCurveRow:
    """
    The CalCurveRow class is a row of a CalCurveTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalCurveRow.
        When row is None, create an empty row attached to table, which must be a CalCurveTable.
        When row is given, copy those values in to the new row. The row argument must be a CalCurveRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalCurveTable):
            raise ValueError("table must be a CalCurveTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)

        self._typeCurve = CalCurveType.from_int(0)

        self._receiverBand = ReceiverBand.from_int(0)

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._frequencyRange = []  # this is a list of Frequency []

        self._numAntenna = 0

        self._numPoly = 0

        self._numReceptor = 0

        self._antennaNames = []  # this is a list of str []

        self._refAntennaName = None

        self._polarizationTypes = []  # this is a list of PolarizationType []

        self._curve = []  # this is a list of float []  []  []

        self._reducedChiSquared = []  # this is a list of float []

        self._numBaselineExists = False

        self._numBaseline = 0

        self._rmsExists = False

        self._rms = []  # this is a list of float []  []

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalCurveRow):
                raise ValueError("row must be a CalCurveRow")

            # copy constructor

            # We force the attribute of the result to be not None.
            if row._atmPhaseCorrection is None:
                self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)
            else:
                self._atmPhaseCorrection = AtmPhaseCorrection(row._atmPhaseCorrection)

            # We force the attribute of the result to be not None.
            if row._typeCurve is None:
                self._typeCurve = CalCurveType.from_int(0)
            else:
                self._typeCurve = CalCurveType(row._typeCurve)

            # We force the attribute of the result to be not None.
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            # frequencyRange is a  list , make a deep copy
            self._frequencyRange = copy.deepcopy(row._frequencyRange)

            self._numAntenna = row._numAntenna

            self._numPoly = row._numPoly

            self._numReceptor = row._numReceptor

            # antennaNames is a  list , make a deep copy
            self._antennaNames = copy.deepcopy(row._antennaNames)

            self._refAntennaName = row._refAntennaName

            # polarizationTypes is a  list , make a deep copy
            self._polarizationTypes = copy.deepcopy(row._polarizationTypes)

            # curve is a  list , make a deep copy
            self._curve = copy.deepcopy(row._curve)

            # reducedChiSquared is a  list , make a deep copy
            self._reducedChiSquared = copy.deepcopy(row._reducedChiSquared)

            # by default set systematically numBaseline's value to something not None

            if row._numBaselineExists:

                self._numBaseline = row._numBaseline

                self._numBaselineExists = True

            # by default set systematically rms's value to something not None

            if row._rmsExists:

                # rms is a list, make a deep copy
                self._rms = copy.deepcopy(row._rms)

                self._rmsExists = True

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

        result += Parser.valueToXML("typeCurve", CalCurveType.name(self._typeCurve))

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.listExtendedValueToXML("frequencyRange", self._frequencyRange)

        result += Parser.valueToXML("numAntenna", self._numAntenna)

        result += Parser.valueToXML("numPoly", self._numPoly)

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listValueToXML("antennaNames", self._antennaNames)

        result += Parser.valueToXML("refAntennaName", self._refAntennaName)

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.listValueToXML("curve", self._curve)

        result += Parser.listValueToXML("reducedChiSquared", self._reducedChiSquared)

        if self._numBaselineExists:

            result += Parser.valueToXML("numBaseline", self._numBaseline)

        if self._rmsExists:

            result += Parser.listValueToXML("rms", self._rms)

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
                "xmlrow is not a string or a minidom.Element", "CalCurveTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalCurveTable")

        # intrinsic attribute values

        atmPhaseCorrectionNode = rowdom.getElementsByTagName("atmPhaseCorrection")[0]

        self._atmPhaseCorrection = AtmPhaseCorrection.newAtmPhaseCorrection(
            atmPhaseCorrectionNode.firstChild.data.strip()
        )

        typeCurveNode = rowdom.getElementsByTagName("typeCurve")[0]

        self._typeCurve = CalCurveType.newCalCurveType(
            typeCurveNode.firstChild.data.strip()
        )

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data.strip()
        )

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        frequencyRangeNode = rowdom.getElementsByTagName("frequencyRange")[0]

        frequencyRangeStr = frequencyRangeNode.firstChild.data.strip()

        self._frequencyRange = Parser.stringListToLists(
            frequencyRangeStr, Frequency, "CalCurve", True
        )

        numAntennaNode = rowdom.getElementsByTagName("numAntenna")[0]

        self._numAntenna = int(numAntennaNode.firstChild.data.strip())

        numPolyNode = rowdom.getElementsByTagName("numPoly")[0]

        self._numPoly = int(numPolyNode.firstChild.data.strip())

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        antennaNamesNode = rowdom.getElementsByTagName("antennaNames")[0]

        antennaNamesStr = antennaNamesNode.firstChild.data.strip()

        self._antennaNames = Parser.stringListToLists(
            antennaNamesStr, str, "CalCurve", False
        )

        refAntennaNameNode = rowdom.getElementsByTagName("refAntennaName")[0]

        self._refAntennaName = str(refAntennaNameNode.firstChild.data.strip())

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data.strip()
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "CalCurve", False
        )

        curveNode = rowdom.getElementsByTagName("curve")[0]

        curveStr = curveNode.firstChild.data.strip()

        self._curve = Parser.stringListToLists(curveStr, float, "CalCurve", False)

        reducedChiSquaredNode = rowdom.getElementsByTagName("reducedChiSquared")[0]

        reducedChiSquaredStr = reducedChiSquaredNode.firstChild.data.strip()

        self._reducedChiSquared = Parser.stringListToLists(
            reducedChiSquaredStr, float, "CalCurve", False
        )

        numBaselineNode = rowdom.getElementsByTagName("numBaseline")
        if len(numBaselineNode) > 0:

            self._numBaseline = int(numBaselineNode[0].firstChild.data.strip())

            self._numBaselineExists = True

        rmsNode = rowdom.getElementsByTagName("rms")
        if len(rmsNode) > 0:

            rmsStr = rmsNode[0].firstChild.data.strip()

            self._rms = Parser.stringListToLists(rmsStr, float, "CalCurve", False)

            self._rmsExists = True

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

        eos.writeString(str(self._typeCurve))

        eos.writeString(str(self._receiverBand))

        self._calDataId.toBin(eos)

        self._calReductionId.toBin(eos)

        self._startValidTime.toBin(eos)

        self._endValidTime.toBin(eos)

        Frequency.listToBin(self._frequencyRange, eos)

        eos.writeInt(self._numAntenna)

        eos.writeInt(self._numPoly)

        eos.writeInt(self._numReceptor)

        eos.writeInt(len(self._antennaNames))
        for i in range(len(self._antennaNames)):

            eos.writeStr(self._antennaNames[i])

        eos.writeStr(self._refAntennaName)

        eos.writeInt(len(self._polarizationTypes))
        for i in range(len(self._polarizationTypes)):

            eos.writeString(str(self._polarizationTypes[i]))

        # null array case, unsure if this is possible but this should work
        if self._curve is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            curve_dims = pyasdm.utils.getListDims(self._curve)
        # assumes it really is 3D
        eos.writeInt(curve_dims[0])
        eos.writeInt(curve_dims[1])
        eos.writeInt(curve_dims[2])
        for i in range(curve_dims[0]):
            for j in range(curve_dims[1]):
                for k in range(curve_dims[2]):
                    eos.writeFloat(self._curve[i][j][k])

        eos.writeInt(len(self._reducedChiSquared))
        for i in range(len(self._reducedChiSquared)):

            eos.writeFloat(self._reducedChiSquared[i])

        eos.writeBool(self._numBaselineExists)
        if self._numBaselineExists:

            eos.writeInt(self._numBaseline)

        eos.writeBool(self._rmsExists)
        if self._rmsExists:

            # null array case, unsure if this is possible but this should work
            if self._rms is None:
                eos.writeInt(0)
                eos.writeInt(0)
            else:
                rms_dims = pyasdm.utils.getListDims(self._rms)
            # assumes it really is 2D
            eos.writeInt(rms_dims[0])
            eos.writeInt(rms_dims[1])
            for i in range(rms_dims[0]):
                for j in range(rms_dims[1]):
                    eos.writeFloat(self._rms[i][j])

    @staticmethod
    def atmPhaseCorrectionFromBin(row, eis):
        """
        Set the atmPhaseCorrection in row from the EndianInput (eis) instance.
        """

        row._atmPhaseCorrection = AtmPhaseCorrection.literal(eis.readString())

    @staticmethod
    def typeCurveFromBin(row, eis):
        """
        Set the typeCurve in row from the EndianInput (eis) instance.
        """

        row._typeCurve = CalCurveType.literal(eis.readString())

    @staticmethod
    def receiverBandFromBin(row, eis):
        """
        Set the receiverBand in row from the EndianInput (eis) instance.
        """

        row._receiverBand = ReceiverBand.literal(eis.readString())

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
    def numAntennaFromBin(row, eis):
        """
        Set the numAntenna in row from the EndianInput (eis) instance.
        """

        row._numAntenna = eis.readInt()

    @staticmethod
    def numPolyFromBin(row, eis):
        """
        Set the numPoly in row from the EndianInput (eis) instance.
        """

        row._numPoly = eis.readInt()

    @staticmethod
    def numReceptorFromBin(row, eis):
        """
        Set the numReceptor in row from the EndianInput (eis) instance.
        """

        row._numReceptor = eis.readInt()

    @staticmethod
    def antennaNamesFromBin(row, eis):
        """
        Set the antennaNames in row from the EndianInput (eis) instance.
        """

        antennaNamesDim1 = eis.readInt()
        thisList = []
        for i in range(antennaNamesDim1):
            thisValue = eis.readStr()
            thisList.append(thisValue)
        row._antennaNames = thisList

    @staticmethod
    def refAntennaNameFromBin(row, eis):
        """
        Set the refAntennaName in row from the EndianInput (eis) instance.
        """

        row._refAntennaName = eis.readStr()

    @staticmethod
    def polarizationTypesFromBin(row, eis):
        """
        Set the polarizationTypes in row from the EndianInput (eis) instance.
        """

        polarizationTypesDim1 = eis.readInt()
        thisList = []
        for i in range(polarizationTypesDim1):
            thisValue = PolarizationType.literal(eis.readString())
            thisList.append(thisValue)
        row._polarizationTypes = thisList

    @staticmethod
    def curveFromBin(row, eis):
        """
        Set the curve in row from the EndianInput (eis) instance.
        """

        curveDim1 = eis.readInt()
        curveDim2 = eis.readInt()
        curveDim3 = eis.readInt()
        thisList = []
        for i in range(curveDim1):
            thisList_j = []
            for j in range(curveDim2):
                thisList_k = []
                for k in range(curveDim3):
                    thisValue = eis.readFloat()
                    thisList_k.append(thisValue)
                thisList_j.append(thisList_k)
            thisList.append(thisList_j)
        row._curve = thisList

    @staticmethod
    def reducedChiSquaredFromBin(row, eis):
        """
        Set the reducedChiSquared in row from the EndianInput (eis) instance.
        """

        reducedChiSquaredDim1 = eis.readInt()
        thisList = []
        for i in range(reducedChiSquaredDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._reducedChiSquared = thisList

    @staticmethod
    def numBaselineFromBin(row, eis):
        """
        Set the optional numBaseline in row from the EndianInput (eis) instance.
        """
        row._numBaselineExists = eis.readBool()
        if row._numBaselineExists:

            row._numBaseline = eis.readInt()

    @staticmethod
    def rmsFromBin(row, eis):
        """
        Set the optional rms in row from the EndianInput (eis) instance.
        """
        row._rmsExists = eis.readBool()
        if row._rmsExists:

            rmsDim1 = eis.readInt()
            rmsDim2 = eis.readInt()
            thisList = []
            for i in range(rmsDim1):
                thisList_j = []
                for j in range(rmsDim2):
                    thisValue = eis.readFloat()
                    thisList_j.append(thisValue)
                thisList.append(thisList_j)
            row._rms = thisList

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["atmPhaseCorrection"] = CalCurveRow.atmPhaseCorrectionFromBin
        _fromBinMethods["typeCurve"] = CalCurveRow.typeCurveFromBin
        _fromBinMethods["receiverBand"] = CalCurveRow.receiverBandFromBin
        _fromBinMethods["calDataId"] = CalCurveRow.calDataIdFromBin
        _fromBinMethods["calReductionId"] = CalCurveRow.calReductionIdFromBin
        _fromBinMethods["startValidTime"] = CalCurveRow.startValidTimeFromBin
        _fromBinMethods["endValidTime"] = CalCurveRow.endValidTimeFromBin
        _fromBinMethods["frequencyRange"] = CalCurveRow.frequencyRangeFromBin
        _fromBinMethods["numAntenna"] = CalCurveRow.numAntennaFromBin
        _fromBinMethods["numPoly"] = CalCurveRow.numPolyFromBin
        _fromBinMethods["numReceptor"] = CalCurveRow.numReceptorFromBin
        _fromBinMethods["antennaNames"] = CalCurveRow.antennaNamesFromBin
        _fromBinMethods["refAntennaName"] = CalCurveRow.refAntennaNameFromBin
        _fromBinMethods["polarizationTypes"] = CalCurveRow.polarizationTypesFromBin
        _fromBinMethods["curve"] = CalCurveRow.curveFromBin
        _fromBinMethods["reducedChiSquared"] = CalCurveRow.reducedChiSquaredFromBin

        _fromBinMethods["numBaseline"] = CalCurveRow.numBaselineFromBin
        _fromBinMethods["rms"] = CalCurveRow.rmsFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CalCurveRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalCurve",
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

    # ===> Attribute typeCurve

    _typeCurve = CalCurveType.from_int(0)

    def getTypeCurve(self):
        """
        Get typeCurve.
        return typeCurve as CalCurveType
        """

        return self._typeCurve

    def setTypeCurve(self, typeCurve):
        """
        Set typeCurve with the specified CalCurveType value.
        typeCurve The CalCurveType value to which typeCurve is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the typeCurve field, which is part of the key, after this row has been added to this table."
            )

        self._typeCurve = CalCurveType(typeCurve)

    # ===> Attribute receiverBand

    _receiverBand = ReceiverBand.from_int(0)

    def getReceiverBand(self):
        """
        Get receiverBand.
        return receiverBand as ReceiverBand
        """

        return self._receiverBand

    def setReceiverBand(self, receiverBand):
        """
        Set receiverBand with the specified ReceiverBand value.
        receiverBand The ReceiverBand value to which receiverBand is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the receiverBand field, which is part of the key, after this row has been added to this table."
            )

        self._receiverBand = ReceiverBand(receiverBand)

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

    # ===> Attribute numAntenna

    _numAntenna = 0

    def getNumAntenna(self):
        """
        Get numAntenna.
        return numAntenna as int
        """

        return self._numAntenna

    def setNumAntenna(self, numAntenna):
        """
        Set numAntenna with the specified int value.
        numAntenna The int value to which numAntenna is to be set.


        """

        self._numAntenna = int(numAntenna)

    # ===> Attribute numPoly

    _numPoly = 0

    def getNumPoly(self):
        """
        Get numPoly.
        return numPoly as int
        """

        return self._numPoly

    def setNumPoly(self, numPoly):
        """
        Set numPoly with the specified int value.
        numPoly The int value to which numPoly is to be set.


        """

        self._numPoly = int(numPoly)

    # ===> Attribute numReceptor

    _numReceptor = 0

    def getNumReceptor(self):
        """
        Get numReceptor.
        return numReceptor as int
        """

        return self._numReceptor

    def setNumReceptor(self, numReceptor):
        """
        Set numReceptor with the specified int value.
        numReceptor The int value to which numReceptor is to be set.


        """

        self._numReceptor = int(numReceptor)

    # ===> Attribute antennaNames

    _antennaNames = None  # this is a 1D list of str

    def getAntennaNames(self):
        """
        Get antennaNames.
        return antennaNames as str []
        """

        return copy.deepcopy(self._antennaNames)

    def setAntennaNames(self, antennaNames):
        """
        Set antennaNames with the specified str []  value.
        antennaNames The str []  value to which antennaNames is to be set.


        """

        # value must be a list
        if not isinstance(antennaNames, list):
            raise ValueError("The value of antennaNames must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(antennaNames)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of antennaNames is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(antennaNames, str):
                raise ValueError(
                    "type of the first value in antennaNames is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._antennaNames = copy.deepcopy(antennaNames)
        except Exception as exc:
            raise ValueError("Invalid antennaNames : " + str(exc))

    # ===> Attribute refAntennaName

    _refAntennaName = None

    def getRefAntennaName(self):
        """
        Get refAntennaName.
        return refAntennaName as str
        """

        return self._refAntennaName

    def setRefAntennaName(self, refAntennaName):
        """
        Set refAntennaName with the specified str value.
        refAntennaName The str value to which refAntennaName is to be set.


        """

        self._refAntennaName = str(refAntennaName)

    # ===> Attribute polarizationTypes

    _polarizationTypes = None  # this is a 1D list of PolarizationType

    def getPolarizationTypes(self):
        """
        Get polarizationTypes.
        return polarizationTypes as PolarizationType []
        """

        return copy.deepcopy(self._polarizationTypes)

    def setPolarizationTypes(self, polarizationTypes):
        """
        Set polarizationTypes with the specified PolarizationType []  value.
        polarizationTypes The PolarizationType []  value to which polarizationTypes is to be set.


        """

        # value must be a list
        if not isinstance(polarizationTypes, list):
            raise ValueError("The value of polarizationTypes must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(polarizationTypes)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of polarizationTypes is not correct")

            # the type of the values in the list must be PolarizationType
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(polarizationTypes, PolarizationType):
                raise ValueError(
                    "type of the first value in polarizationTypes is not PolarizationType as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._polarizationTypes = copy.deepcopy(polarizationTypes)
        except Exception as exc:
            raise ValueError("Invalid polarizationTypes : " + str(exc))

    # ===> Attribute curve

    _curve = None  # this is a 2D list of float

    def getCurve(self):
        """
        Get curve.
        return curve as float []  []  []
        """

        return copy.deepcopy(self._curve)

    def setCurve(self, curve):
        """
        Set curve with the specified float []  []  []  value.
        curve The float []  []  []  value to which curve is to be set.


        """

        # value must be a list
        if not isinstance(curve, list):
            raise ValueError("The value of curve must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(curve)

            shapeOK = len(listDims) == 3

            if not shapeOK:
                raise ValueError("shape of curve is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(curve, float):
                raise ValueError(
                    "type of the first value in curve is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._curve = copy.deepcopy(curve)
        except Exception as exc:
            raise ValueError("Invalid curve : " + str(exc))

    # ===> Attribute reducedChiSquared

    _reducedChiSquared = None  # this is a 1D list of float

    def getReducedChiSquared(self):
        """
        Get reducedChiSquared.
        return reducedChiSquared as float []
        """

        return copy.deepcopy(self._reducedChiSquared)

    def setReducedChiSquared(self, reducedChiSquared):
        """
        Set reducedChiSquared with the specified float []  value.
        reducedChiSquared The float []  value to which reducedChiSquared is to be set.


        """

        # value must be a list
        if not isinstance(reducedChiSquared, list):
            raise ValueError("The value of reducedChiSquared must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(reducedChiSquared)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of reducedChiSquared is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(reducedChiSquared, float):
                raise ValueError(
                    "type of the first value in reducedChiSquared is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._reducedChiSquared = copy.deepcopy(reducedChiSquared)
        except Exception as exc:
            raise ValueError("Invalid reducedChiSquared : " + str(exc))

    # ===> Attribute numBaseline, which is optional
    _numBaselineExists = False

    _numBaseline = 0

    def isNumBaselineExists(self):
        """
        The attribute numBaseline is optional. Return True if this attribute exists.
        return True if and only if the numBaseline attribute exists.
        """
        return self._numBaselineExists

    def getNumBaseline(self):
        """
        Get numBaseline, which is optional.
        return numBaseline as int
        raises ValueError If numBaseline does not exist.
        """
        if not self._numBaselineExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numBaseline
                + " attribute in table CalCurve does not exist!"
            )

        return self._numBaseline

    def setNumBaseline(self, numBaseline):
        """
        Set numBaseline with the specified int value.
        numBaseline The int value to which numBaseline is to be set.


        """

        self._numBaseline = int(numBaseline)

        self._numBaselineExists = True

    def clearNumBaseline(self):
        """
        Mark numBaseline, which is an optional field, as non-existent.
        """
        self._numBaselineExists = False

    # ===> Attribute rms, which is optional
    _rmsExists = False

    _rms = None  # this is a 2D list of float

    def isRmsExists(self):
        """
        The attribute rms is optional. Return True if this attribute exists.
        return True if and only if the rms attribute exists.
        """
        return self._rmsExists

    def getRms(self):
        """
        Get rms, which is optional.
        return rms as float []  []
        raises ValueError If rms does not exist.
        """
        if not self._rmsExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + rms
                + " attribute in table CalCurve does not exist!"
            )

        return copy.deepcopy(self._rms)

    def setRms(self, rms):
        """
        Set rms with the specified float []  []  value.
        rms The float []  []  value to which rms is to be set.


        """

        # value must be a list
        if not isinstance(rms, list):
            raise ValueError("The value of rms must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(rms)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of rms is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(rms, float):
                raise ValueError(
                    "type of the first value in rms is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._rms = copy.deepcopy(rms)
        except Exception as exc:
            raise ValueError("Invalid rms : " + str(exc))

        self._rmsExists = True

    def clearRms(self):
        """
        Mark rms, which is an optional field, as non-existent.
        """
        self._rmsExists = False

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
        typeCurve,
        receiverBand,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        frequencyRange,
        numAntenna,
        numPoly,
        numReceptor,
        antennaNames,
        refAntennaName,
        polarizationTypes,
        curve,
        reducedChiSquared,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalCurveRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # atmPhaseCorrection is a AtmPhaseCorrection, compare using the == operator on the getValue() output
        if not (self._atmPhaseCorrection.getValue() == atmPhaseCorrection.getValue()):
            return False

        # typeCurve is a CalCurveType, compare using the == operator on the getValue() output
        if not (self._typeCurve.getValue() == typeCurve.getValue()):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
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

        # numAntenna is a int, compare using the == operator.
        if not (self._numAntenna == numAntenna):
            return False

        # numPoly is a int, compare using the == operator.
        if not (self._numPoly == numPoly):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._antennaNames) != len(antennaNames):
            return False
        for indx in range(len(antennaNames)):

            # antennaNames is a list of str, compare using == operator.
            if not (self._antennaNames[indx] == antennaNames[indx]):
                return False

        # refAntennaName is a str, compare using the == operator.
        if not (self._refAntennaName == refAntennaName):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationTypes) != len(polarizationTypes):
            return False
        for indx in range(len(polarizationTypes)):

            # polarizationTypes is a list of PolarizationType, compare using == operator.
            if not (self._polarizationTypes[indx] == polarizationTypes[indx]):
                return False

        # We compare two 3D arrays.
        # Compare firstly their dimensions and then their values.
        if curve is not None:
            if self._curve is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            curve_dims = pyasdm.utils.getListDims(curve)
            this_curve_dims = pyasdm.utils.getListDims(self._curve)
            if curve_dims != this_curve_dims:
                return False
            # assumes they are both 3D arrays, the internal one should be
            for i in range(curve_dims[0]):
                for j in range(curve_dims[1]):
                    for k in range(curve_dims[2]):

                        # curve is an array of float, compare using == operator.
                        if not (self._curve[i][j][k] == curve[i][j][k]):
                            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._reducedChiSquared) != len(reducedChiSquared):
            return False
        for indx in range(len(reducedChiSquared)):

            # reducedChiSquared is a list of float, compare using == operator.
            if not (self._reducedChiSquared[indx] == reducedChiSquared[indx]):
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
            otherRow.getNumAntenna(),
            otherRow.getNumPoly(),
            otherRow.getNumReceptor(),
            otherRow.getAntennaNames(),
            otherRow.getRefAntennaName(),
            otherRow.getPolarizationTypes(),
            otherRow.getCurve(),
            otherRow.getReducedChiSquared(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        frequencyRange,
        numAntenna,
        numPoly,
        numReceptor,
        antennaNames,
        refAntennaName,
        polarizationTypes,
        curve,
        reducedChiSquared,
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

        # numAntenna is a int, compare using the == operator.
        if not (self._numAntenna == numAntenna):
            return False

        # numPoly is a int, compare using the == operator.
        if not (self._numPoly == numPoly):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._antennaNames) != len(antennaNames):
            return False
        for indx in range(len(antennaNames)):

            # antennaNames is a list of str, compare using == operator.
            if not (self._antennaNames[indx] == antennaNames[indx]):
                return False

        # refAntennaName is a str, compare using the == operator.
        if not (self._refAntennaName == refAntennaName):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationTypes) != len(polarizationTypes):
            return False
        for indx in range(len(polarizationTypes)):

            # polarizationTypes is a list of PolarizationType, compare using == operator.
            if not (self._polarizationTypes[indx] == polarizationTypes[indx]):
                return False

        # We compare two 3D arrays.
        # Compare firstly their dimensions and then their values.
        if curve is not None:
            if self._curve is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            curve_dims = pyasdm.utils.getListDims(curve)
            this_curve_dims = pyasdm.utils.getListDims(self._curve)
            if curve_dims != this_curve_dims:
                return False
            # assumes they are both 3D arrays, the internal one should be
            for i in range(curve_dims[0]):
                for j in range(curve_dims[1]):
                    for k in range(curve_dims[2]):

                        # curve is an array of float, compare using == operator.
                        if not (self._curve[i][j][k] == curve[i][j][k]):
                            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._reducedChiSquared) != len(reducedChiSquared):
            return False
        for indx in range(len(reducedChiSquared)):

            # reducedChiSquared is a list of float, compare using == operator.
            if not (self._reducedChiSquared[indx] == reducedChiSquared[indx]):
                return False

        return True


# initialize the dictionary that maps fields to init methods
CalCurveRow.initFromBinMethods()
