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
# File CalBandpassRow.py
#

import pyasdm.CalBandpassTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.BasebandName import BasebandName


from pyasdm.enumerations.NetSideband import NetSideband


from pyasdm.enumerations.AtmPhaseCorrection import AtmPhaseCorrection


from pyasdm.enumerations.CalCurveType import CalCurveType


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.PolarizationType import PolarizationType


from xml.dom import minidom

import copy


class CalBandpassRow:
    """
    The CalBandpassRow class is a row of a CalBandpassTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalBandpassRow.
        When row is None, create an empty row attached to table, which must be a CalBandpassTable.
        When row is given, copy those values in to the new row. The row argument must be a CalBandpassRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalBandpassTable):
            raise ValueError("table must be a CalBandpassTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._basebandName = BasebandName.from_int(0)

        self._sideband = NetSideband.from_int(0)

        self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)

        self._typeCurve = CalCurveType.from_int(0)

        self._receiverBand = ReceiverBand.from_int(0)

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._numAntenna = 0

        self._numPoly = 0

        self._numReceptor = 0

        self._antennaNames = []  # this is a list of str []

        self._refAntennaName = None

        self._freqLimits = []  # this is a list of Frequency []

        self._polarizationTypes = []  # this is a list of PolarizationType []

        self._curve = []  # this is a list of float []  []  []

        self._reducedChiSquared = []  # this is a list of float []

        self._numBaselineExists = False

        self._numBaseline = 0

        self._numFreqExists = False

        self._numFreq = 0

        self._rmsExists = False

        self._rms = []  # this is a list of float []  []

        self._frequencyRangeExists = False

        self._frequencyRange = []  # this is a list of Frequency []

        self._numSpectralWindowExists = False

        self._numSpectralWindow = 0

        self._chanFreqStartExists = False

        self._chanFreqStart = []  # this is a list of Frequency []

        self._chanFreqStepExists = False

        self._chanFreqStep = []  # this is a list of Frequency []

        self._numSpectralWindowChanExists = False

        self._numSpectralWindowChan = []  # this is a list of int []

        self._spectrumExists = False

        self._spectrum = []  # this is a list of float []  []  []

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalBandpassRow):
                raise ValueError("row must be a CalBandpassRow")

            # copy constructor

            # We force the attribute of the result to be not None.
            if row._basebandName is None:
                self._basebandName = BasebandName.from_int(0)
            else:
                self._basebandName = BasebandName(row._basebandName)

            # We force the attribute of the result to be not None.
            if row._sideband is None:
                self._sideband = NetSideband.from_int(0)
            else:
                self._sideband = NetSideband(row._sideband)

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

            self._numAntenna = row._numAntenna

            self._numPoly = row._numPoly

            self._numReceptor = row._numReceptor

            # antennaNames is a  list , make a deep copy
            self._antennaNames = copy.deepcopy(row._antennaNames)

            self._refAntennaName = row._refAntennaName

            # freqLimits is a  list , make a deep copy
            self._freqLimits = copy.deepcopy(row._freqLimits)

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

            # by default set systematically numFreq's value to something not None

            if row._numFreqExists:

                self._numFreq = row._numFreq

                self._numFreqExists = True

            # by default set systematically rms's value to something not None

            if row._rmsExists:

                # rms is a list, make a deep copy
                self._rms = copy.deepcopy(row._rms)

                self._rmsExists = True

            # by default set systematically frequencyRange's value to something not None

            if row._frequencyRangeExists:

                # frequencyRange is a list, make a deep copy
                self._frequencyRange = copy.deepcopy(row._frequencyRange)

                self._frequencyRangeExists = True

            # by default set systematically numSpectralWindow's value to something not None

            if row._numSpectralWindowExists:

                self._numSpectralWindow = row._numSpectralWindow

                self._numSpectralWindowExists = True

            # by default set systematically chanFreqStart's value to something not None

            if row._chanFreqStartExists:

                # chanFreqStart is a list, make a deep copy
                self._chanFreqStart = copy.deepcopy(row._chanFreqStart)

                self._chanFreqStartExists = True

            # by default set systematically chanFreqStep's value to something not None

            if row._chanFreqStepExists:

                # chanFreqStep is a list, make a deep copy
                self._chanFreqStep = copy.deepcopy(row._chanFreqStep)

                self._chanFreqStepExists = True

            # by default set systematically numSpectralWindowChan's value to something not None

            if row._numSpectralWindowChanExists:

                # numSpectralWindowChan is a list, make a deep copy
                self._numSpectralWindowChan = copy.deepcopy(row._numSpectralWindowChan)

                self._numSpectralWindowChanExists = True

            # by default set systematically spectrum's value to something not None

            if row._spectrumExists:

                # spectrum is a list, make a deep copy
                self._spectrum = copy.deepcopy(row._spectrum)

                self._spectrumExists = True

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
            "basebandName", BasebandName.name(self._basebandName)
        )

        result += Parser.valueToXML("sideband", NetSideband.name(self._sideband))

        result += Parser.valueToXML(
            "atmPhaseCorrection", AtmPhaseCorrection.name(self._atmPhaseCorrection)
        )

        result += Parser.valueToXML("typeCurve", CalCurveType.name(self._typeCurve))

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.valueToXML("numAntenna", self._numAntenna)

        result += Parser.valueToXML("numPoly", self._numPoly)

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listValueToXML("antennaNames", self._antennaNames)

        result += Parser.valueToXML("refAntennaName", self._refAntennaName)

        result += Parser.listExtendedValueToXML("freqLimits", self._freqLimits)

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.listValueToXML("curve", self._curve)

        result += Parser.listValueToXML("reducedChiSquared", self._reducedChiSquared)

        if self._numBaselineExists:

            result += Parser.valueToXML("numBaseline", self._numBaseline)

        if self._numFreqExists:

            result += Parser.valueToXML("numFreq", self._numFreq)

        if self._rmsExists:

            result += Parser.listValueToXML("rms", self._rms)

        if self._frequencyRangeExists:

            result += Parser.listExtendedValueToXML(
                "frequencyRange", self._frequencyRange
            )

        if self._numSpectralWindowExists:

            result += Parser.valueToXML("numSpectralWindow", self._numSpectralWindow)

        if self._chanFreqStartExists:

            result += Parser.listExtendedValueToXML(
                "chanFreqStart", self._chanFreqStart
            )

        if self._chanFreqStepExists:

            result += Parser.listExtendedValueToXML("chanFreqStep", self._chanFreqStep)

        if self._numSpectralWindowChanExists:

            result += Parser.listValueToXML(
                "numSpectralWindowChan", self._numSpectralWindowChan
            )

        if self._spectrumExists:

            result += Parser.listValueToXML("spectrum", self._spectrum)

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
                "xmlrow is not a string or a minidom.Element", "CalBandpassTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalBandpassTable")

        # intrinsic attribute values

        basebandNameNode = rowdom.getElementsByTagName("basebandName")[0]

        self._basebandName = BasebandName.newBasebandName(
            basebandNameNode.firstChild.data.strip()
        )

        sidebandNode = rowdom.getElementsByTagName("sideband")[0]

        self._sideband = NetSideband.newNetSideband(
            sidebandNode.firstChild.data.strip()
        )

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

        numAntennaNode = rowdom.getElementsByTagName("numAntenna")[0]

        self._numAntenna = int(numAntennaNode.firstChild.data.strip())

        numPolyNode = rowdom.getElementsByTagName("numPoly")[0]

        self._numPoly = int(numPolyNode.firstChild.data.strip())

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        antennaNamesNode = rowdom.getElementsByTagName("antennaNames")[0]

        antennaNamesStr = antennaNamesNode.firstChild.data.strip()

        self._antennaNames = Parser.stringListToLists(
            antennaNamesStr, str, "CalBandpass", False
        )

        refAntennaNameNode = rowdom.getElementsByTagName("refAntennaName")[0]

        self._refAntennaName = str(refAntennaNameNode.firstChild.data.strip())

        freqLimitsNode = rowdom.getElementsByTagName("freqLimits")[0]

        freqLimitsStr = freqLimitsNode.firstChild.data.strip()

        self._freqLimits = Parser.stringListToLists(
            freqLimitsStr, Frequency, "CalBandpass", True
        )

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data.strip()
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "CalBandpass", False
        )

        curveNode = rowdom.getElementsByTagName("curve")[0]

        curveStr = curveNode.firstChild.data.strip()

        self._curve = Parser.stringListToLists(curveStr, float, "CalBandpass", False)

        reducedChiSquaredNode = rowdom.getElementsByTagName("reducedChiSquared")[0]

        reducedChiSquaredStr = reducedChiSquaredNode.firstChild.data.strip()

        self._reducedChiSquared = Parser.stringListToLists(
            reducedChiSquaredStr, float, "CalBandpass", False
        )

        numBaselineNode = rowdom.getElementsByTagName("numBaseline")
        if len(numBaselineNode) > 0:

            self._numBaseline = int(numBaselineNode[0].firstChild.data.strip())

            self._numBaselineExists = True

        numFreqNode = rowdom.getElementsByTagName("numFreq")
        if len(numFreqNode) > 0:

            self._numFreq = int(numFreqNode[0].firstChild.data.strip())

            self._numFreqExists = True

        rmsNode = rowdom.getElementsByTagName("rms")
        if len(rmsNode) > 0:

            rmsStr = rmsNode[0].firstChild.data.strip()

            self._rms = Parser.stringListToLists(rmsStr, float, "CalBandpass", False)

            self._rmsExists = True

        frequencyRangeNode = rowdom.getElementsByTagName("frequencyRange")
        if len(frequencyRangeNode) > 0:

            frequencyRangeStr = frequencyRangeNode[0].firstChild.data.strip()

            self._frequencyRange = Parser.stringListToLists(
                frequencyRangeStr, Frequency, "CalBandpass", True
            )

            self._frequencyRangeExists = True

        numSpectralWindowNode = rowdom.getElementsByTagName("numSpectralWindow")
        if len(numSpectralWindowNode) > 0:

            self._numSpectralWindow = int(
                numSpectralWindowNode[0].firstChild.data.strip()
            )

            self._numSpectralWindowExists = True

        chanFreqStartNode = rowdom.getElementsByTagName("chanFreqStart")
        if len(chanFreqStartNode) > 0:

            chanFreqStartStr = chanFreqStartNode[0].firstChild.data.strip()

            self._chanFreqStart = Parser.stringListToLists(
                chanFreqStartStr, Frequency, "CalBandpass", True
            )

            self._chanFreqStartExists = True

        chanFreqStepNode = rowdom.getElementsByTagName("chanFreqStep")
        if len(chanFreqStepNode) > 0:

            chanFreqStepStr = chanFreqStepNode[0].firstChild.data.strip()

            self._chanFreqStep = Parser.stringListToLists(
                chanFreqStepStr, Frequency, "CalBandpass", True
            )

            self._chanFreqStepExists = True

        numSpectralWindowChanNode = rowdom.getElementsByTagName("numSpectralWindowChan")
        if len(numSpectralWindowChanNode) > 0:

            numSpectralWindowChanStr = numSpectralWindowChanNode[
                0
            ].firstChild.data.strip()

            self._numSpectralWindowChan = Parser.stringListToLists(
                numSpectralWindowChanStr, int, "CalBandpass", False
            )

            self._numSpectralWindowChanExists = True

        spectrumNode = rowdom.getElementsByTagName("spectrum")
        if len(spectrumNode) > 0:

            spectrumStr = spectrumNode[0].firstChild.data.strip()

            self._spectrum = Parser.stringListToLists(
                spectrumStr, float, "CalBandpass", False
            )

            self._spectrumExists = True

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

        eos.writeString(str(self._basebandName))

        eos.writeString(str(self._sideband))

        eos.writeString(str(self._atmPhaseCorrection))

        eos.writeString(str(self._typeCurve))

        eos.writeString(str(self._receiverBand))

        self._calDataId.toBin(eos)

        self._calReductionId.toBin(eos)

        self._startValidTime.toBin(eos)

        self._endValidTime.toBin(eos)

        eos.writeInt(self._numAntenna)

        eos.writeInt(self._numPoly)

        eos.writeInt(self._numReceptor)

        eos.writeInt(len(self._antennaNames))
        for i in range(len(self._antennaNames)):

            eos.writeStr(self._antennaNames[i])

        eos.writeStr(self._refAntennaName)

        Frequency.listToBin(self._freqLimits, eos)

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

        eos.writeBool(self._numFreqExists)
        if self._numFreqExists:

            eos.writeInt(self._numFreq)

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

        eos.writeBool(self._frequencyRangeExists)
        if self._frequencyRangeExists:

            Frequency.listToBin(self._frequencyRange, eos)

        eos.writeBool(self._numSpectralWindowExists)
        if self._numSpectralWindowExists:

            eos.writeInt(self._numSpectralWindow)

        eos.writeBool(self._chanFreqStartExists)
        if self._chanFreqStartExists:

            Frequency.listToBin(self._chanFreqStart, eos)

        eos.writeBool(self._chanFreqStepExists)
        if self._chanFreqStepExists:

            Frequency.listToBin(self._chanFreqStep, eos)

        eos.writeBool(self._numSpectralWindowChanExists)
        if self._numSpectralWindowChanExists:

            eos.writeInt(len(self._numSpectralWindowChan))
            for i in range(len(self._numSpectralWindowChan)):

                eos.writeInt(self._numSpectralWindowChan[i])

        eos.writeBool(self._spectrumExists)
        if self._spectrumExists:

            # null array case, unsure if this is possible but this should work
            if self._spectrum is None:
                eos.writeInt(0)
                eos.writeInt(0)
            else:
                spectrum_dims = pyasdm.utils.getListDims(self._spectrum)
            # assumes it really is 3D
            eos.writeInt(spectrum_dims[0])
            eos.writeInt(spectrum_dims[1])
            eos.writeInt(spectrum_dims[2])
            for i in range(spectrum_dims[0]):
                for j in range(spectrum_dims[1]):
                    for k in range(spectrum_dims[2]):
                        eos.writeFloat(self._spectrum[i][j][k])

    @staticmethod
    def basebandNameFromBin(row, eis):
        """
        Set the basebandName in row from the EndianInput (eis) instance.
        """

        row._basebandName = BasebandName.literal(eis.readString())

    @staticmethod
    def sidebandFromBin(row, eis):
        """
        Set the sideband in row from the EndianInput (eis) instance.
        """

        row._sideband = NetSideband.literal(eis.readString())

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
    def freqLimitsFromBin(row, eis):
        """
        Set the freqLimits in row from the EndianInput (eis) instance.
        """

        row._freqLimits = Frequency.from1DBin(eis)

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
    def numFreqFromBin(row, eis):
        """
        Set the optional numFreq in row from the EndianInput (eis) instance.
        """
        row._numFreqExists = eis.readBool()
        if row._numFreqExists:

            row._numFreq = eis.readInt()

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
    def frequencyRangeFromBin(row, eis):
        """
        Set the optional frequencyRange in row from the EndianInput (eis) instance.
        """
        row._frequencyRangeExists = eis.readBool()
        if row._frequencyRangeExists:

            row._frequencyRange = Frequency.from1DBin(eis)

    @staticmethod
    def numSpectralWindowFromBin(row, eis):
        """
        Set the optional numSpectralWindow in row from the EndianInput (eis) instance.
        """
        row._numSpectralWindowExists = eis.readBool()
        if row._numSpectralWindowExists:

            row._numSpectralWindow = eis.readInt()

    @staticmethod
    def chanFreqStartFromBin(row, eis):
        """
        Set the optional chanFreqStart in row from the EndianInput (eis) instance.
        """
        row._chanFreqStartExists = eis.readBool()
        if row._chanFreqStartExists:

            row._chanFreqStart = Frequency.from1DBin(eis)

    @staticmethod
    def chanFreqStepFromBin(row, eis):
        """
        Set the optional chanFreqStep in row from the EndianInput (eis) instance.
        """
        row._chanFreqStepExists = eis.readBool()
        if row._chanFreqStepExists:

            row._chanFreqStep = Frequency.from1DBin(eis)

    @staticmethod
    def numSpectralWindowChanFromBin(row, eis):
        """
        Set the optional numSpectralWindowChan in row from the EndianInput (eis) instance.
        """
        row._numSpectralWindowChanExists = eis.readBool()
        if row._numSpectralWindowChanExists:

            numSpectralWindowChanDim1 = eis.readInt()
            thisList = []
            for i in range(numSpectralWindowChanDim1):
                thisValue = eis.readInt()
                thisList.append(thisValue)
            row._numSpectralWindowChan = thisList

    @staticmethod
    def spectrumFromBin(row, eis):
        """
        Set the optional spectrum in row from the EndianInput (eis) instance.
        """
        row._spectrumExists = eis.readBool()
        if row._spectrumExists:

            spectrumDim1 = eis.readInt()
            spectrumDim2 = eis.readInt()
            spectrumDim3 = eis.readInt()
            thisList = []
            for i in range(spectrumDim1):
                thisList_j = []
                for j in range(spectrumDim2):
                    thisList_k = []
                    for k in range(spectrumDim3):
                        thisValue = eis.readFloat()
                        thisList_k.append(thisValue)
                    thisList_j.append(thisList_k)
                thisList.append(thisList_j)
            row._spectrum = thisList

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["basebandName"] = CalBandpassRow.basebandNameFromBin
        _fromBinMethods["sideband"] = CalBandpassRow.sidebandFromBin
        _fromBinMethods["atmPhaseCorrection"] = CalBandpassRow.atmPhaseCorrectionFromBin
        _fromBinMethods["typeCurve"] = CalBandpassRow.typeCurveFromBin
        _fromBinMethods["receiverBand"] = CalBandpassRow.receiverBandFromBin
        _fromBinMethods["calDataId"] = CalBandpassRow.calDataIdFromBin
        _fromBinMethods["calReductionId"] = CalBandpassRow.calReductionIdFromBin
        _fromBinMethods["startValidTime"] = CalBandpassRow.startValidTimeFromBin
        _fromBinMethods["endValidTime"] = CalBandpassRow.endValidTimeFromBin
        _fromBinMethods["numAntenna"] = CalBandpassRow.numAntennaFromBin
        _fromBinMethods["numPoly"] = CalBandpassRow.numPolyFromBin
        _fromBinMethods["numReceptor"] = CalBandpassRow.numReceptorFromBin
        _fromBinMethods["antennaNames"] = CalBandpassRow.antennaNamesFromBin
        _fromBinMethods["refAntennaName"] = CalBandpassRow.refAntennaNameFromBin
        _fromBinMethods["freqLimits"] = CalBandpassRow.freqLimitsFromBin
        _fromBinMethods["polarizationTypes"] = CalBandpassRow.polarizationTypesFromBin
        _fromBinMethods["curve"] = CalBandpassRow.curveFromBin
        _fromBinMethods["reducedChiSquared"] = CalBandpassRow.reducedChiSquaredFromBin

        _fromBinMethods["numBaseline"] = CalBandpassRow.numBaselineFromBin
        _fromBinMethods["numFreq"] = CalBandpassRow.numFreqFromBin
        _fromBinMethods["rms"] = CalBandpassRow.rmsFromBin
        _fromBinMethods["frequencyRange"] = CalBandpassRow.frequencyRangeFromBin
        _fromBinMethods["numSpectralWindow"] = CalBandpassRow.numSpectralWindowFromBin
        _fromBinMethods["chanFreqStart"] = CalBandpassRow.chanFreqStartFromBin
        _fromBinMethods["chanFreqStep"] = CalBandpassRow.chanFreqStepFromBin
        _fromBinMethods["numSpectralWindowChan"] = (
            CalBandpassRow.numSpectralWindowChanFromBin
        )
        _fromBinMethods["spectrum"] = CalBandpassRow.spectrumFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CalBandpassRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalBandpass",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute basebandName

    _basebandName = BasebandName.from_int(0)

    def getBasebandName(self):
        """
        Get basebandName.
        return basebandName as BasebandName
        """

        return self._basebandName

    def setBasebandName(self, basebandName):
        """
        Set basebandName with the specified BasebandName value.
        basebandName The BasebandName value to which basebandName is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the basebandName field, which is part of the key, after this row has been added to this table."
            )

        self._basebandName = BasebandName(basebandName)

    # ===> Attribute sideband

    _sideband = NetSideband.from_int(0)

    def getSideband(self):
        """
        Get sideband.
        return sideband as NetSideband
        """

        return self._sideband

    def setSideband(self, sideband):
        """
        Set sideband with the specified NetSideband value.
        sideband The NetSideband value to which sideband is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the sideband field, which is part of the key, after this row has been added to this table."
            )

        self._sideband = NetSideband(sideband)

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

    # ===> Attribute freqLimits

    _freqLimits = None  # this is a 1D list of Frequency

    def getFreqLimits(self):
        """
        Get freqLimits.
        return freqLimits as Frequency []
        """

        return copy.deepcopy(self._freqLimits)

    def setFreqLimits(self, freqLimits):
        """
        Set freqLimits with the specified Frequency []  value.
        freqLimits The Frequency []  value to which freqLimits is to be set.
        The value of freqLimits can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(freqLimits, list):
            raise ValueError("The value of freqLimits must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(freqLimits)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of freqLimits is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(freqLimits, Frequency):
                raise ValueError(
                    "type of the first value in freqLimits is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._freqLimits = copy.deepcopy(freqLimits)
        except Exception as exc:
            raise ValueError("Invalid freqLimits : " + str(exc))

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
                + " attribute in table CalBandpass does not exist!"
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

    # ===> Attribute numFreq, which is optional
    _numFreqExists = False

    _numFreq = 0

    def isNumFreqExists(self):
        """
        The attribute numFreq is optional. Return True if this attribute exists.
        return True if and only if the numFreq attribute exists.
        """
        return self._numFreqExists

    def getNumFreq(self):
        """
        Get numFreq, which is optional.
        return numFreq as int
        raises ValueError If numFreq does not exist.
        """
        if not self._numFreqExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numFreq
                + " attribute in table CalBandpass does not exist!"
            )

        return self._numFreq

    def setNumFreq(self, numFreq):
        """
        Set numFreq with the specified int value.
        numFreq The int value to which numFreq is to be set.


        """

        self._numFreq = int(numFreq)

        self._numFreqExists = True

    def clearNumFreq(self):
        """
        Mark numFreq, which is an optional field, as non-existent.
        """
        self._numFreqExists = False

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
                + " attribute in table CalBandpass does not exist!"
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

    # ===> Attribute frequencyRange, which is optional
    _frequencyRangeExists = False

    _frequencyRange = None  # this is a 1D list of Frequency

    def isFrequencyRangeExists(self):
        """
        The attribute frequencyRange is optional. Return True if this attribute exists.
        return True if and only if the frequencyRange attribute exists.
        """
        return self._frequencyRangeExists

    def getFrequencyRange(self):
        """
        Get frequencyRange, which is optional.
        return frequencyRange as Frequency []
        raises ValueError If frequencyRange does not exist.
        """
        if not self._frequencyRangeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + frequencyRange
                + " attribute in table CalBandpass does not exist!"
            )

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

        self._frequencyRangeExists = True

    def clearFrequencyRange(self):
        """
        Mark frequencyRange, which is an optional field, as non-existent.
        """
        self._frequencyRangeExists = False

    # ===> Attribute numSpectralWindow, which is optional
    _numSpectralWindowExists = False

    _numSpectralWindow = 0

    def isNumSpectralWindowExists(self):
        """
        The attribute numSpectralWindow is optional. Return True if this attribute exists.
        return True if and only if the numSpectralWindow attribute exists.
        """
        return self._numSpectralWindowExists

    def getNumSpectralWindow(self):
        """
        Get numSpectralWindow, which is optional.
        return numSpectralWindow as int
        raises ValueError If numSpectralWindow does not exist.
        """
        if not self._numSpectralWindowExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numSpectralWindow
                + " attribute in table CalBandpass does not exist!"
            )

        return self._numSpectralWindow

    def setNumSpectralWindow(self, numSpectralWindow):
        """
        Set numSpectralWindow with the specified int value.
        numSpectralWindow The int value to which numSpectralWindow is to be set.


        """

        self._numSpectralWindow = int(numSpectralWindow)

        self._numSpectralWindowExists = True

    def clearNumSpectralWindow(self):
        """
        Mark numSpectralWindow, which is an optional field, as non-existent.
        """
        self._numSpectralWindowExists = False

    # ===> Attribute chanFreqStart, which is optional
    _chanFreqStartExists = False

    _chanFreqStart = None  # this is a 1D list of Frequency

    def isChanFreqStartExists(self):
        """
        The attribute chanFreqStart is optional. Return True if this attribute exists.
        return True if and only if the chanFreqStart attribute exists.
        """
        return self._chanFreqStartExists

    def getChanFreqStart(self):
        """
        Get chanFreqStart, which is optional.
        return chanFreqStart as Frequency []
        raises ValueError If chanFreqStart does not exist.
        """
        if not self._chanFreqStartExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + chanFreqStart
                + " attribute in table CalBandpass does not exist!"
            )

        return copy.deepcopy(self._chanFreqStart)

    def setChanFreqStart(self, chanFreqStart):
        """
        Set chanFreqStart with the specified Frequency []  value.
        chanFreqStart The Frequency []  value to which chanFreqStart is to be set.
        The value of chanFreqStart can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(chanFreqStart, list):
            raise ValueError("The value of chanFreqStart must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(chanFreqStart)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of chanFreqStart is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(chanFreqStart, Frequency):
                raise ValueError(
                    "type of the first value in chanFreqStart is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._chanFreqStart = copy.deepcopy(chanFreqStart)
        except Exception as exc:
            raise ValueError("Invalid chanFreqStart : " + str(exc))

        self._chanFreqStartExists = True

    def clearChanFreqStart(self):
        """
        Mark chanFreqStart, which is an optional field, as non-existent.
        """
        self._chanFreqStartExists = False

    # ===> Attribute chanFreqStep, which is optional
    _chanFreqStepExists = False

    _chanFreqStep = None  # this is a 1D list of Frequency

    def isChanFreqStepExists(self):
        """
        The attribute chanFreqStep is optional. Return True if this attribute exists.
        return True if and only if the chanFreqStep attribute exists.
        """
        return self._chanFreqStepExists

    def getChanFreqStep(self):
        """
        Get chanFreqStep, which is optional.
        return chanFreqStep as Frequency []
        raises ValueError If chanFreqStep does not exist.
        """
        if not self._chanFreqStepExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + chanFreqStep
                + " attribute in table CalBandpass does not exist!"
            )

        return copy.deepcopy(self._chanFreqStep)

    def setChanFreqStep(self, chanFreqStep):
        """
        Set chanFreqStep with the specified Frequency []  value.
        chanFreqStep The Frequency []  value to which chanFreqStep is to be set.
        The value of chanFreqStep can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(chanFreqStep, list):
            raise ValueError("The value of chanFreqStep must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(chanFreqStep)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of chanFreqStep is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(chanFreqStep, Frequency):
                raise ValueError(
                    "type of the first value in chanFreqStep is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._chanFreqStep = copy.deepcopy(chanFreqStep)
        except Exception as exc:
            raise ValueError("Invalid chanFreqStep : " + str(exc))

        self._chanFreqStepExists = True

    def clearChanFreqStep(self):
        """
        Mark chanFreqStep, which is an optional field, as non-existent.
        """
        self._chanFreqStepExists = False

    # ===> Attribute numSpectralWindowChan, which is optional
    _numSpectralWindowChanExists = False

    _numSpectralWindowChan = None  # this is a 1D list of int

    def isNumSpectralWindowChanExists(self):
        """
        The attribute numSpectralWindowChan is optional. Return True if this attribute exists.
        return True if and only if the numSpectralWindowChan attribute exists.
        """
        return self._numSpectralWindowChanExists

    def getNumSpectralWindowChan(self):
        """
        Get numSpectralWindowChan, which is optional.
        return numSpectralWindowChan as int []
        raises ValueError If numSpectralWindowChan does not exist.
        """
        if not self._numSpectralWindowChanExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numSpectralWindowChan
                + " attribute in table CalBandpass does not exist!"
            )

        return copy.deepcopy(self._numSpectralWindowChan)

    def setNumSpectralWindowChan(self, numSpectralWindowChan):
        """
        Set numSpectralWindowChan with the specified int []  value.
        numSpectralWindowChan The int []  value to which numSpectralWindowChan is to be set.


        """

        # value must be a list
        if not isinstance(numSpectralWindowChan, list):
            raise ValueError("The value of numSpectralWindowChan must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(numSpectralWindowChan)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of numSpectralWindowChan is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(numSpectralWindowChan, int):
                raise ValueError(
                    "type of the first value in numSpectralWindowChan is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._numSpectralWindowChan = copy.deepcopy(numSpectralWindowChan)
        except Exception as exc:
            raise ValueError("Invalid numSpectralWindowChan : " + str(exc))

        self._numSpectralWindowChanExists = True

    def clearNumSpectralWindowChan(self):
        """
        Mark numSpectralWindowChan, which is an optional field, as non-existent.
        """
        self._numSpectralWindowChanExists = False

    # ===> Attribute spectrum, which is optional
    _spectrumExists = False

    _spectrum = None  # this is a 2D list of float

    def isSpectrumExists(self):
        """
        The attribute spectrum is optional. Return True if this attribute exists.
        return True if and only if the spectrum attribute exists.
        """
        return self._spectrumExists

    def getSpectrum(self):
        """
        Get spectrum, which is optional.
        return spectrum as float []  []  []
        raises ValueError If spectrum does not exist.
        """
        if not self._spectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + spectrum
                + " attribute in table CalBandpass does not exist!"
            )

        return copy.deepcopy(self._spectrum)

    def setSpectrum(self, spectrum):
        """
        Set spectrum with the specified float []  []  []  value.
        spectrum The float []  []  []  value to which spectrum is to be set.


        """

        # value must be a list
        if not isinstance(spectrum, list):
            raise ValueError("The value of spectrum must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(spectrum)

            shapeOK = len(listDims) == 3

            if not shapeOK:
                raise ValueError("shape of spectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(spectrum, float):
                raise ValueError(
                    "type of the first value in spectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._spectrum = copy.deepcopy(spectrum)
        except Exception as exc:
            raise ValueError("Invalid spectrum : " + str(exc))

        self._spectrumExists = True

    def clearSpectrum(self):
        """
        Mark spectrum, which is an optional field, as non-existent.
        """
        self._spectrumExists = False

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
        basebandName,
        sideband,
        atmPhaseCorrection,
        typeCurve,
        receiverBand,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numAntenna,
        numPoly,
        numReceptor,
        antennaNames,
        refAntennaName,
        freqLimits,
        polarizationTypes,
        curve,
        reducedChiSquared,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalBandpassRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # basebandName is a BasebandName, compare using the == operator on the getValue() output
        if not (self._basebandName.getValue() == basebandName.getValue()):
            return False

        # sideband is a NetSideband, compare using the == operator on the getValue() output
        if not (self._sideband.getValue() == sideband.getValue()):
            return False

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
        if len(self._freqLimits) != len(freqLimits):
            return False
        for indx in range(len(freqLimits)):

            # freqLimits is a list of Frequency, compare using the almostEquals method.
            if not self._freqLimits[indx].almostEquals(
                freqLimits[indx], self.getTable().getFreqLimitsEqTolerance()
            ):
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
            otherRow.getNumAntenna(),
            otherRow.getNumPoly(),
            otherRow.getNumReceptor(),
            otherRow.getAntennaNames(),
            otherRow.getRefAntennaName(),
            otherRow.getFreqLimits(),
            otherRow.getPolarizationTypes(),
            otherRow.getCurve(),
            otherRow.getReducedChiSquared(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        numAntenna,
        numPoly,
        numReceptor,
        antennaNames,
        refAntennaName,
        freqLimits,
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
        if len(self._freqLimits) != len(freqLimits):
            return False
        for indx in range(len(freqLimits)):

            # freqLimits is a list of Frequency, compare using the almostEquals method.
            if not self._freqLimits[indx].almostEquals(
                freqLimits[indx], self.getTable().getFreqLimitsEqTolerance()
            ):
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
CalBandpassRow.initFromBinMethods()
