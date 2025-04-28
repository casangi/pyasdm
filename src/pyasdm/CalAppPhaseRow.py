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
# File CalAppPhaseRow.py
#

import pyasdm.CalAppPhaseTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.BasebandName import BasebandName


from xml.dom import minidom

import copy


class CalAppPhaseRow:
    """
    The CalAppPhaseRow class is a row of a CalAppPhaseTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalAppPhaseRow.
        When row is None, create an empty row attached to table, which must be a CalAppPhaseTable.
        When row is given, copy those values in to the new row. The row argument must be a CalAppPhaseRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalAppPhaseTable):
            raise ValueError("table must be a CalAppPhaseTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._basebandName = BasebandName.from_int(0)

        self._scanNumber = 0

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._adjustTime = ArrayTime()

        self._adjustToken = None

        self._phasingMode = None

        self._numPhasedAntennas = 0

        self._phasedAntennas = []  # this is a list of str []

        self._refAntennaIndex = 0

        self._candRefAntennaIndex = 0

        self._phasePacking = None

        self._numReceptors = 0

        self._numChannels = 0

        self._numPhaseValues = 0

        self._phaseValues = []  # this is a list of float []

        self._numCompare = 0

        self._numEfficiencies = 0

        self._compareArray = []  # this is a list of str []

        self._efficiencyIndices = []  # this is a list of int []

        self._efficiencies = []  # this is a list of float []  []

        self._quality = []  # this is a list of float []

        self._phasedSumAntenna = None

        self._typeSupportsExists = False

        self._typeSupports = None

        self._numSupportsExists = False

        self._numSupports = 0

        self._phaseSupportsExists = False

        self._phaseSupports = []  # this is a list of float []

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalAppPhaseRow):
                raise ValueError("row must be a CalAppPhaseRow")

            # copy constructor

            # We force the attribute of the result to be not None.
            if row._basebandName is None:
                self._basebandName = BasebandName.from_int(0)
            else:
                self._basebandName = BasebandName(row._basebandName)

            self._scanNumber = row._scanNumber

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            self._adjustTime = ArrayTime(row._adjustTime)

            self._adjustToken = row._adjustToken

            self._phasingMode = row._phasingMode

            self._numPhasedAntennas = row._numPhasedAntennas

            # phasedAntennas is a  list , make a deep copy
            self._phasedAntennas = copy.deepcopy(row._phasedAntennas)

            self._refAntennaIndex = row._refAntennaIndex

            self._candRefAntennaIndex = row._candRefAntennaIndex

            self._phasePacking = row._phasePacking

            self._numReceptors = row._numReceptors

            self._numChannels = row._numChannels

            self._numPhaseValues = row._numPhaseValues

            # phaseValues is a  list , make a deep copy
            self._phaseValues = copy.deepcopy(row._phaseValues)

            self._numCompare = row._numCompare

            self._numEfficiencies = row._numEfficiencies

            # compareArray is a  list , make a deep copy
            self._compareArray = copy.deepcopy(row._compareArray)

            # efficiencyIndices is a  list , make a deep copy
            self._efficiencyIndices = copy.deepcopy(row._efficiencyIndices)

            # efficiencies is a  list , make a deep copy
            self._efficiencies = copy.deepcopy(row._efficiencies)

            # quality is a  list , make a deep copy
            self._quality = copy.deepcopy(row._quality)

            self._phasedSumAntenna = row._phasedSumAntenna

            # by default set systematically typeSupports's value to something not None

            if row._typeSupportsExists:

                self._typeSupports = row._typeSupports

                self._typeSupportsExists = True

            # by default set systematically numSupports's value to something not None

            if row._numSupportsExists:

                self._numSupports = row._numSupports

                self._numSupportsExists = True

            # by default set systematically phaseSupports's value to something not None

            if row._phaseSupportsExists:

                # phaseSupports is a list, make a deep copy
                self._phaseSupports = copy.deepcopy(row._phaseSupports)

                self._phaseSupportsExists = True

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

        result += Parser.valueToXML("scanNumber", self._scanNumber)

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.extendedValueToXML("adjustTime", self._adjustTime)

        result += Parser.valueToXML("adjustToken", self._adjustToken)

        result += Parser.valueToXML("phasingMode", self._phasingMode)

        result += Parser.valueToXML("numPhasedAntennas", self._numPhasedAntennas)

        result += Parser.listValueToXML("phasedAntennas", self._phasedAntennas)

        result += Parser.valueToXML("refAntennaIndex", self._refAntennaIndex)

        result += Parser.valueToXML("candRefAntennaIndex", self._candRefAntennaIndex)

        result += Parser.valueToXML("phasePacking", self._phasePacking)

        result += Parser.valueToXML("numReceptors", self._numReceptors)

        result += Parser.valueToXML("numChannels", self._numChannels)

        result += Parser.valueToXML("numPhaseValues", self._numPhaseValues)

        result += Parser.listValueToXML("phaseValues", self._phaseValues)

        result += Parser.valueToXML("numCompare", self._numCompare)

        result += Parser.valueToXML("numEfficiencies", self._numEfficiencies)

        result += Parser.listValueToXML("compareArray", self._compareArray)

        result += Parser.listValueToXML("efficiencyIndices", self._efficiencyIndices)

        result += Parser.listValueToXML("efficiencies", self._efficiencies)

        result += Parser.listValueToXML("quality", self._quality)

        result += Parser.valueToXML("phasedSumAntenna", self._phasedSumAntenna)

        if self._typeSupportsExists:

            result += Parser.valueToXML("typeSupports", self._typeSupports)

        if self._numSupportsExists:

            result += Parser.valueToXML("numSupports", self._numSupports)

        if self._phaseSupportsExists:

            result += Parser.listValueToXML("phaseSupports", self._phaseSupports)

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
                "xmlrow is not a string or a minidom.Element", "CalAppPhaseTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalAppPhaseTable")

        # intrinsic attribute values

        basebandNameNode = rowdom.getElementsByTagName("basebandName")[0]

        self._basebandName = BasebandName.newBasebandName(
            basebandNameNode.firstChild.data.strip()
        )

        scanNumberNode = rowdom.getElementsByTagName("scanNumber")[0]

        self._scanNumber = int(scanNumberNode.firstChild.data.strip())

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        adjustTimeNode = rowdom.getElementsByTagName("adjustTime")[0]

        self._adjustTime = ArrayTime(adjustTimeNode.firstChild.data.strip())

        adjustTokenNode = rowdom.getElementsByTagName("adjustToken")[0]

        self._adjustToken = str(adjustTokenNode.firstChild.data.strip())

        phasingModeNode = rowdom.getElementsByTagName("phasingMode")[0]

        self._phasingMode = str(phasingModeNode.firstChild.data.strip())

        numPhasedAntennasNode = rowdom.getElementsByTagName("numPhasedAntennas")[0]

        self._numPhasedAntennas = int(numPhasedAntennasNode.firstChild.data.strip())

        phasedAntennasNode = rowdom.getElementsByTagName("phasedAntennas")[0]

        phasedAntennasStr = phasedAntennasNode.firstChild.data.strip()

        self._phasedAntennas = Parser.stringListToLists(
            phasedAntennasStr, str, "CalAppPhase", False
        )

        refAntennaIndexNode = rowdom.getElementsByTagName("refAntennaIndex")[0]

        self._refAntennaIndex = int(refAntennaIndexNode.firstChild.data.strip())

        candRefAntennaIndexNode = rowdom.getElementsByTagName("candRefAntennaIndex")[0]

        self._candRefAntennaIndex = int(candRefAntennaIndexNode.firstChild.data.strip())

        phasePackingNode = rowdom.getElementsByTagName("phasePacking")[0]

        self._phasePacking = str(phasePackingNode.firstChild.data.strip())

        numReceptorsNode = rowdom.getElementsByTagName("numReceptors")[0]

        self._numReceptors = int(numReceptorsNode.firstChild.data.strip())

        numChannelsNode = rowdom.getElementsByTagName("numChannels")[0]

        self._numChannels = int(numChannelsNode.firstChild.data.strip())

        numPhaseValuesNode = rowdom.getElementsByTagName("numPhaseValues")[0]

        self._numPhaseValues = int(numPhaseValuesNode.firstChild.data.strip())

        phaseValuesNode = rowdom.getElementsByTagName("phaseValues")[0]

        phaseValuesStr = phaseValuesNode.firstChild.data.strip()

        self._phaseValues = Parser.stringListToLists(
            phaseValuesStr, float, "CalAppPhase", False
        )

        numCompareNode = rowdom.getElementsByTagName("numCompare")[0]

        self._numCompare = int(numCompareNode.firstChild.data.strip())

        numEfficienciesNode = rowdom.getElementsByTagName("numEfficiencies")[0]

        self._numEfficiencies = int(numEfficienciesNode.firstChild.data.strip())

        compareArrayNode = rowdom.getElementsByTagName("compareArray")[0]

        compareArrayStr = compareArrayNode.firstChild.data.strip()

        self._compareArray = Parser.stringListToLists(
            compareArrayStr, str, "CalAppPhase", False
        )

        efficiencyIndicesNode = rowdom.getElementsByTagName("efficiencyIndices")[0]

        efficiencyIndicesStr = efficiencyIndicesNode.firstChild.data.strip()

        self._efficiencyIndices = Parser.stringListToLists(
            efficiencyIndicesStr, int, "CalAppPhase", False
        )

        efficienciesNode = rowdom.getElementsByTagName("efficiencies")[0]

        efficienciesStr = efficienciesNode.firstChild.data.strip()

        self._efficiencies = Parser.stringListToLists(
            efficienciesStr, float, "CalAppPhase", False
        )

        qualityNode = rowdom.getElementsByTagName("quality")[0]

        qualityStr = qualityNode.firstChild.data.strip()

        self._quality = Parser.stringListToLists(
            qualityStr, float, "CalAppPhase", False
        )

        phasedSumAntennaNode = rowdom.getElementsByTagName("phasedSumAntenna")[0]

        self._phasedSumAntenna = str(phasedSumAntennaNode.firstChild.data.strip())

        typeSupportsNode = rowdom.getElementsByTagName("typeSupports")
        if len(typeSupportsNode) > 0:

            self._typeSupports = str(typeSupportsNode[0].firstChild.data.strip())

            self._typeSupportsExists = True

        numSupportsNode = rowdom.getElementsByTagName("numSupports")
        if len(numSupportsNode) > 0:

            self._numSupports = int(numSupportsNode[0].firstChild.data.strip())

            self._numSupportsExists = True

        phaseSupportsNode = rowdom.getElementsByTagName("phaseSupports")
        if len(phaseSupportsNode) > 0:

            phaseSupportsStr = phaseSupportsNode[0].firstChild.data.strip()

            self._phaseSupports = Parser.stringListToLists(
                phaseSupportsStr, float, "CalAppPhase", False
            )

            self._phaseSupportsExists = True

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

        eos.writeInt(self._scanNumber)

        self._calDataId.toBin(eos)

        self._calReductionId.toBin(eos)

        self._startValidTime.toBin(eos)

        self._endValidTime.toBin(eos)

        self._adjustTime.toBin(eos)

        eos.writeStr(self._adjustToken)

        eos.writeStr(self._phasingMode)

        eos.writeInt(self._numPhasedAntennas)

        eos.writeInt(len(self._phasedAntennas))
        for i in range(len(self._phasedAntennas)):

            eos.writeStr(self._phasedAntennas[i])

        eos.writeInt(self._refAntennaIndex)

        eos.writeInt(self._candRefAntennaIndex)

        eos.writeStr(self._phasePacking)

        eos.writeInt(self._numReceptors)

        eos.writeInt(self._numChannels)

        eos.writeInt(self._numPhaseValues)

        eos.writeInt(len(self._phaseValues))
        for i in range(len(self._phaseValues)):

            eos.writeFloat(self._phaseValues[i])

        eos.writeInt(self._numCompare)

        eos.writeInt(self._numEfficiencies)

        eos.writeInt(len(self._compareArray))
        for i in range(len(self._compareArray)):

            eos.writeStr(self._compareArray[i])

        eos.writeInt(len(self._efficiencyIndices))
        for i in range(len(self._efficiencyIndices)):

            eos.writeInt(self._efficiencyIndices[i])

        # null array case, unsure if this is possible but this should work
        if self._efficiencies is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            efficiencies_dims = pyasdm.utils.getListDims(self._efficiencies)
        # assumes it really is 2D
        eos.writeInt(efficiencies_dims[0])
        eos.writeInt(efficiencies_dims[1])
        for i in range(efficiencies_dims[0]):
            for j in range(efficiencies_dims[1]):
                eos.writeFloat(self._efficiencies[i][j])

        eos.writeInt(len(self._quality))
        for i in range(len(self._quality)):

            eos.writeFloat(self._quality[i])

        eos.writeStr(self._phasedSumAntenna)

        eos.writeBool(self._typeSupportsExists)
        if self._typeSupportsExists:

            eos.writeStr(self._typeSupports)

        eos.writeBool(self._numSupportsExists)
        if self._numSupportsExists:

            eos.writeInt(self._numSupports)

        eos.writeBool(self._phaseSupportsExists)
        if self._phaseSupportsExists:

            eos.writeInt(len(self._phaseSupports))
            for i in range(len(self._phaseSupports)):

                eos.writeFloat(self._phaseSupports[i])

    @staticmethod
    def basebandNameFromBin(row, eis):
        """
        Set the basebandName in row from the EndianInput (eis) instance.
        """

        row._basebandName = BasebandName.literal(eis.readString())

    @staticmethod
    def scanNumberFromBin(row, eis):
        """
        Set the scanNumber in row from the EndianInput (eis) instance.
        """

        row._scanNumber = eis.readInt()

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
    def adjustTimeFromBin(row, eis):
        """
        Set the adjustTime in row from the EndianInput (eis) instance.
        """

        row._adjustTime = ArrayTime.fromBin(eis)

    @staticmethod
    def adjustTokenFromBin(row, eis):
        """
        Set the adjustToken in row from the EndianInput (eis) instance.
        """

        row._adjustToken = eis.readStr()

    @staticmethod
    def phasingModeFromBin(row, eis):
        """
        Set the phasingMode in row from the EndianInput (eis) instance.
        """

        row._phasingMode = eis.readStr()

    @staticmethod
    def numPhasedAntennasFromBin(row, eis):
        """
        Set the numPhasedAntennas in row from the EndianInput (eis) instance.
        """

        row._numPhasedAntennas = eis.readInt()

    @staticmethod
    def phasedAntennasFromBin(row, eis):
        """
        Set the phasedAntennas in row from the EndianInput (eis) instance.
        """

        phasedAntennasDim1 = eis.readInt()
        thisList = []
        for i in range(phasedAntennasDim1):
            thisValue = eis.readStr()
            thisList.append(thisValue)
        row._phasedAntennas = thisList

    @staticmethod
    def refAntennaIndexFromBin(row, eis):
        """
        Set the refAntennaIndex in row from the EndianInput (eis) instance.
        """

        row._refAntennaIndex = eis.readInt()

    @staticmethod
    def candRefAntennaIndexFromBin(row, eis):
        """
        Set the candRefAntennaIndex in row from the EndianInput (eis) instance.
        """

        row._candRefAntennaIndex = eis.readInt()

    @staticmethod
    def phasePackingFromBin(row, eis):
        """
        Set the phasePacking in row from the EndianInput (eis) instance.
        """

        row._phasePacking = eis.readStr()

    @staticmethod
    def numReceptorsFromBin(row, eis):
        """
        Set the numReceptors in row from the EndianInput (eis) instance.
        """

        row._numReceptors = eis.readInt()

    @staticmethod
    def numChannelsFromBin(row, eis):
        """
        Set the numChannels in row from the EndianInput (eis) instance.
        """

        row._numChannels = eis.readInt()

    @staticmethod
    def numPhaseValuesFromBin(row, eis):
        """
        Set the numPhaseValues in row from the EndianInput (eis) instance.
        """

        row._numPhaseValues = eis.readInt()

    @staticmethod
    def phaseValuesFromBin(row, eis):
        """
        Set the phaseValues in row from the EndianInput (eis) instance.
        """

        phaseValuesDim1 = eis.readInt()
        thisList = []
        for i in range(phaseValuesDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._phaseValues = thisList

    @staticmethod
    def numCompareFromBin(row, eis):
        """
        Set the numCompare in row from the EndianInput (eis) instance.
        """

        row._numCompare = eis.readInt()

    @staticmethod
    def numEfficienciesFromBin(row, eis):
        """
        Set the numEfficiencies in row from the EndianInput (eis) instance.
        """

        row._numEfficiencies = eis.readInt()

    @staticmethod
    def compareArrayFromBin(row, eis):
        """
        Set the compareArray in row from the EndianInput (eis) instance.
        """

        compareArrayDim1 = eis.readInt()
        thisList = []
        for i in range(compareArrayDim1):
            thisValue = eis.readStr()
            thisList.append(thisValue)
        row._compareArray = thisList

    @staticmethod
    def efficiencyIndicesFromBin(row, eis):
        """
        Set the efficiencyIndices in row from the EndianInput (eis) instance.
        """

        efficiencyIndicesDim1 = eis.readInt()
        thisList = []
        for i in range(efficiencyIndicesDim1):
            thisValue = eis.readInt()
            thisList.append(thisValue)
        row._efficiencyIndices = thisList

    @staticmethod
    def efficienciesFromBin(row, eis):
        """
        Set the efficiencies in row from the EndianInput (eis) instance.
        """

        efficienciesDim1 = eis.readInt()
        efficienciesDim2 = eis.readInt()
        thisList = []
        for i in range(efficienciesDim1):
            thisList_j = []
            for j in range(efficienciesDim2):
                thisValue = eis.readFloat()
                thisList_j.append(thisValue)
            thisList.append(thisList_j)
        row._efficiencies = thisList

    @staticmethod
    def qualityFromBin(row, eis):
        """
        Set the quality in row from the EndianInput (eis) instance.
        """

        qualityDim1 = eis.readInt()
        thisList = []
        for i in range(qualityDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._quality = thisList

    @staticmethod
    def phasedSumAntennaFromBin(row, eis):
        """
        Set the phasedSumAntenna in row from the EndianInput (eis) instance.
        """

        row._phasedSumAntenna = eis.readStr()

    @staticmethod
    def typeSupportsFromBin(row, eis):
        """
        Set the optional typeSupports in row from the EndianInput (eis) instance.
        """
        row._typeSupportsExists = eis.readBool()
        if row._typeSupportsExists:

            row._typeSupports = eis.readStr()

    @staticmethod
    def numSupportsFromBin(row, eis):
        """
        Set the optional numSupports in row from the EndianInput (eis) instance.
        """
        row._numSupportsExists = eis.readBool()
        if row._numSupportsExists:

            row._numSupports = eis.readInt()

    @staticmethod
    def phaseSupportsFromBin(row, eis):
        """
        Set the optional phaseSupports in row from the EndianInput (eis) instance.
        """
        row._phaseSupportsExists = eis.readBool()
        if row._phaseSupportsExists:

            phaseSupportsDim1 = eis.readInt()
            thisList = []
            for i in range(phaseSupportsDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._phaseSupports = thisList

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["basebandName"] = CalAppPhaseRow.basebandNameFromBin
        _fromBinMethods["scanNumber"] = CalAppPhaseRow.scanNumberFromBin
        _fromBinMethods["calDataId"] = CalAppPhaseRow.calDataIdFromBin
        _fromBinMethods["calReductionId"] = CalAppPhaseRow.calReductionIdFromBin
        _fromBinMethods["startValidTime"] = CalAppPhaseRow.startValidTimeFromBin
        _fromBinMethods["endValidTime"] = CalAppPhaseRow.endValidTimeFromBin
        _fromBinMethods["adjustTime"] = CalAppPhaseRow.adjustTimeFromBin
        _fromBinMethods["adjustToken"] = CalAppPhaseRow.adjustTokenFromBin
        _fromBinMethods["phasingMode"] = CalAppPhaseRow.phasingModeFromBin
        _fromBinMethods["numPhasedAntennas"] = CalAppPhaseRow.numPhasedAntennasFromBin
        _fromBinMethods["phasedAntennas"] = CalAppPhaseRow.phasedAntennasFromBin
        _fromBinMethods["refAntennaIndex"] = CalAppPhaseRow.refAntennaIndexFromBin
        _fromBinMethods["candRefAntennaIndex"] = (
            CalAppPhaseRow.candRefAntennaIndexFromBin
        )
        _fromBinMethods["phasePacking"] = CalAppPhaseRow.phasePackingFromBin
        _fromBinMethods["numReceptors"] = CalAppPhaseRow.numReceptorsFromBin
        _fromBinMethods["numChannels"] = CalAppPhaseRow.numChannelsFromBin
        _fromBinMethods["numPhaseValues"] = CalAppPhaseRow.numPhaseValuesFromBin
        _fromBinMethods["phaseValues"] = CalAppPhaseRow.phaseValuesFromBin
        _fromBinMethods["numCompare"] = CalAppPhaseRow.numCompareFromBin
        _fromBinMethods["numEfficiencies"] = CalAppPhaseRow.numEfficienciesFromBin
        _fromBinMethods["compareArray"] = CalAppPhaseRow.compareArrayFromBin
        _fromBinMethods["efficiencyIndices"] = CalAppPhaseRow.efficiencyIndicesFromBin
        _fromBinMethods["efficiencies"] = CalAppPhaseRow.efficienciesFromBin
        _fromBinMethods["quality"] = CalAppPhaseRow.qualityFromBin
        _fromBinMethods["phasedSumAntenna"] = CalAppPhaseRow.phasedSumAntennaFromBin

        _fromBinMethods["typeSupports"] = CalAppPhaseRow.typeSupportsFromBin
        _fromBinMethods["numSupports"] = CalAppPhaseRow.numSupportsFromBin
        _fromBinMethods["phaseSupports"] = CalAppPhaseRow.phaseSupportsFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CalAppPhaseRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalAppPhase",
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

    # ===> Attribute scanNumber

    _scanNumber = 0

    def getScanNumber(self):
        """
        Get scanNumber.
        return scanNumber as int
        """

        return self._scanNumber

    def setScanNumber(self, scanNumber):
        """
        Set scanNumber with the specified int value.
        scanNumber The int value to which scanNumber is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the scanNumber field, which is part of the key, after this row has been added to this table."
            )

        self._scanNumber = int(scanNumber)

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

    # ===> Attribute adjustTime

    _adjustTime = ArrayTime()

    def getAdjustTime(self):
        """
        Get adjustTime.
        return adjustTime as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._adjustTime)

    def setAdjustTime(self, adjustTime):
        """
        Set adjustTime with the specified ArrayTime value.
        adjustTime The ArrayTime value to which adjustTime is to be set.
        The value of adjustTime can be anything allowed by the ArrayTime constructor.

        """

        self._adjustTime = ArrayTime(adjustTime)

    # ===> Attribute adjustToken

    _adjustToken = None

    def getAdjustToken(self):
        """
        Get adjustToken.
        return adjustToken as str
        """

        return self._adjustToken

    def setAdjustToken(self, adjustToken):
        """
        Set adjustToken with the specified str value.
        adjustToken The str value to which adjustToken is to be set.


        """

        self._adjustToken = str(adjustToken)

    # ===> Attribute phasingMode

    _phasingMode = None

    def getPhasingMode(self):
        """
        Get phasingMode.
        return phasingMode as str
        """

        return self._phasingMode

    def setPhasingMode(self, phasingMode):
        """
        Set phasingMode with the specified str value.
        phasingMode The str value to which phasingMode is to be set.


        """

        self._phasingMode = str(phasingMode)

    # ===> Attribute numPhasedAntennas

    _numPhasedAntennas = 0

    def getNumPhasedAntennas(self):
        """
        Get numPhasedAntennas.
        return numPhasedAntennas as int
        """

        return self._numPhasedAntennas

    def setNumPhasedAntennas(self, numPhasedAntennas):
        """
        Set numPhasedAntennas with the specified int value.
        numPhasedAntennas The int value to which numPhasedAntennas is to be set.


        """

        self._numPhasedAntennas = int(numPhasedAntennas)

    # ===> Attribute phasedAntennas

    _phasedAntennas = None  # this is a 1D list of str

    def getPhasedAntennas(self):
        """
        Get phasedAntennas.
        return phasedAntennas as str []
        """

        return copy.deepcopy(self._phasedAntennas)

    def setPhasedAntennas(self, phasedAntennas):
        """
        Set phasedAntennas with the specified str []  value.
        phasedAntennas The str []  value to which phasedAntennas is to be set.


        """

        # value must be a list
        if not isinstance(phasedAntennas, list):
            raise ValueError("The value of phasedAntennas must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(phasedAntennas)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of phasedAntennas is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(phasedAntennas, str):
                raise ValueError(
                    "type of the first value in phasedAntennas is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phasedAntennas = copy.deepcopy(phasedAntennas)
        except Exception as exc:
            raise ValueError("Invalid phasedAntennas : " + str(exc))

    # ===> Attribute refAntennaIndex

    _refAntennaIndex = 0

    def getRefAntennaIndex(self):
        """
        Get refAntennaIndex.
        return refAntennaIndex as int
        """

        return self._refAntennaIndex

    def setRefAntennaIndex(self, refAntennaIndex):
        """
        Set refAntennaIndex with the specified int value.
        refAntennaIndex The int value to which refAntennaIndex is to be set.


        """

        self._refAntennaIndex = int(refAntennaIndex)

    # ===> Attribute candRefAntennaIndex

    _candRefAntennaIndex = 0

    def getCandRefAntennaIndex(self):
        """
        Get candRefAntennaIndex.
        return candRefAntennaIndex as int
        """

        return self._candRefAntennaIndex

    def setCandRefAntennaIndex(self, candRefAntennaIndex):
        """
        Set candRefAntennaIndex with the specified int value.
        candRefAntennaIndex The int value to which candRefAntennaIndex is to be set.


        """

        self._candRefAntennaIndex = int(candRefAntennaIndex)

    # ===> Attribute phasePacking

    _phasePacking = None

    def getPhasePacking(self):
        """
        Get phasePacking.
        return phasePacking as str
        """

        return self._phasePacking

    def setPhasePacking(self, phasePacking):
        """
        Set phasePacking with the specified str value.
        phasePacking The str value to which phasePacking is to be set.


        """

        self._phasePacking = str(phasePacking)

    # ===> Attribute numReceptors

    _numReceptors = 0

    def getNumReceptors(self):
        """
        Get numReceptors.
        return numReceptors as int
        """

        return self._numReceptors

    def setNumReceptors(self, numReceptors):
        """
        Set numReceptors with the specified int value.
        numReceptors The int value to which numReceptors is to be set.


        """

        self._numReceptors = int(numReceptors)

    # ===> Attribute numChannels

    _numChannels = 0

    def getNumChannels(self):
        """
        Get numChannels.
        return numChannels as int
        """

        return self._numChannels

    def setNumChannels(self, numChannels):
        """
        Set numChannels with the specified int value.
        numChannels The int value to which numChannels is to be set.


        """

        self._numChannels = int(numChannels)

    # ===> Attribute numPhaseValues

    _numPhaseValues = 0

    def getNumPhaseValues(self):
        """
        Get numPhaseValues.
        return numPhaseValues as int
        """

        return self._numPhaseValues

    def setNumPhaseValues(self, numPhaseValues):
        """
        Set numPhaseValues with the specified int value.
        numPhaseValues The int value to which numPhaseValues is to be set.


        """

        self._numPhaseValues = int(numPhaseValues)

    # ===> Attribute phaseValues

    _phaseValues = None  # this is a 1D list of float

    def getPhaseValues(self):
        """
        Get phaseValues.
        return phaseValues as float []
        """

        return copy.deepcopy(self._phaseValues)

    def setPhaseValues(self, phaseValues):
        """
        Set phaseValues with the specified float []  value.
        phaseValues The float []  value to which phaseValues is to be set.


        """

        # value must be a list
        if not isinstance(phaseValues, list):
            raise ValueError("The value of phaseValues must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(phaseValues)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of phaseValues is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(phaseValues, float):
                raise ValueError(
                    "type of the first value in phaseValues is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phaseValues = copy.deepcopy(phaseValues)
        except Exception as exc:
            raise ValueError("Invalid phaseValues : " + str(exc))

    # ===> Attribute numCompare

    _numCompare = 0

    def getNumCompare(self):
        """
        Get numCompare.
        return numCompare as int
        """

        return self._numCompare

    def setNumCompare(self, numCompare):
        """
        Set numCompare with the specified int value.
        numCompare The int value to which numCompare is to be set.


        """

        self._numCompare = int(numCompare)

    # ===> Attribute numEfficiencies

    _numEfficiencies = 0

    def getNumEfficiencies(self):
        """
        Get numEfficiencies.
        return numEfficiencies as int
        """

        return self._numEfficiencies

    def setNumEfficiencies(self, numEfficiencies):
        """
        Set numEfficiencies with the specified int value.
        numEfficiencies The int value to which numEfficiencies is to be set.


        """

        self._numEfficiencies = int(numEfficiencies)

    # ===> Attribute compareArray

    _compareArray = None  # this is a 1D list of str

    def getCompareArray(self):
        """
        Get compareArray.
        return compareArray as str []
        """

        return copy.deepcopy(self._compareArray)

    def setCompareArray(self, compareArray):
        """
        Set compareArray with the specified str []  value.
        compareArray The str []  value to which compareArray is to be set.


        """

        # value must be a list
        if not isinstance(compareArray, list):
            raise ValueError("The value of compareArray must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(compareArray)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of compareArray is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(compareArray, str):
                raise ValueError(
                    "type of the first value in compareArray is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._compareArray = copy.deepcopy(compareArray)
        except Exception as exc:
            raise ValueError("Invalid compareArray : " + str(exc))

    # ===> Attribute efficiencyIndices

    _efficiencyIndices = None  # this is a 1D list of int

    def getEfficiencyIndices(self):
        """
        Get efficiencyIndices.
        return efficiencyIndices as int []
        """

        return copy.deepcopy(self._efficiencyIndices)

    def setEfficiencyIndices(self, efficiencyIndices):
        """
        Set efficiencyIndices with the specified int []  value.
        efficiencyIndices The int []  value to which efficiencyIndices is to be set.


        """

        # value must be a list
        if not isinstance(efficiencyIndices, list):
            raise ValueError("The value of efficiencyIndices must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(efficiencyIndices)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of efficiencyIndices is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(efficiencyIndices, int):
                raise ValueError(
                    "type of the first value in efficiencyIndices is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._efficiencyIndices = copy.deepcopy(efficiencyIndices)
        except Exception as exc:
            raise ValueError("Invalid efficiencyIndices : " + str(exc))

    # ===> Attribute efficiencies

    _efficiencies = None  # this is a 2D list of float

    def getEfficiencies(self):
        """
        Get efficiencies.
        return efficiencies as float []  []
        """

        return copy.deepcopy(self._efficiencies)

    def setEfficiencies(self, efficiencies):
        """
        Set efficiencies with the specified float []  []  value.
        efficiencies The float []  []  value to which efficiencies is to be set.


        """

        # value must be a list
        if not isinstance(efficiencies, list):
            raise ValueError("The value of efficiencies must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(efficiencies)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of efficiencies is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(efficiencies, float):
                raise ValueError(
                    "type of the first value in efficiencies is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._efficiencies = copy.deepcopy(efficiencies)
        except Exception as exc:
            raise ValueError("Invalid efficiencies : " + str(exc))

    # ===> Attribute quality

    _quality = None  # this is a 1D list of float

    def getQuality(self):
        """
        Get quality.
        return quality as float []
        """

        return copy.deepcopy(self._quality)

    def setQuality(self, quality):
        """
        Set quality with the specified float []  value.
        quality The float []  value to which quality is to be set.


        """

        # value must be a list
        if not isinstance(quality, list):
            raise ValueError("The value of quality must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(quality)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of quality is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(quality, float):
                raise ValueError(
                    "type of the first value in quality is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._quality = copy.deepcopy(quality)
        except Exception as exc:
            raise ValueError("Invalid quality : " + str(exc))

    # ===> Attribute phasedSumAntenna

    _phasedSumAntenna = None

    def getPhasedSumAntenna(self):
        """
        Get phasedSumAntenna.
        return phasedSumAntenna as str
        """

        return self._phasedSumAntenna

    def setPhasedSumAntenna(self, phasedSumAntenna):
        """
        Set phasedSumAntenna with the specified str value.
        phasedSumAntenna The str value to which phasedSumAntenna is to be set.


        """

        self._phasedSumAntenna = str(phasedSumAntenna)

    # ===> Attribute typeSupports, which is optional
    _typeSupportsExists = False

    _typeSupports = None

    def isTypeSupportsExists(self):
        """
        The attribute typeSupports is optional. Return True if this attribute exists.
        return True if and only if the typeSupports attribute exists.
        """
        return self._typeSupportsExists

    def getTypeSupports(self):
        """
        Get typeSupports, which is optional.
        return typeSupports as str
        raises ValueError If typeSupports does not exist.
        """
        if not self._typeSupportsExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + typeSupports
                + " attribute in table CalAppPhase does not exist!"
            )

        return self._typeSupports

    def setTypeSupports(self, typeSupports):
        """
        Set typeSupports with the specified str value.
        typeSupports The str value to which typeSupports is to be set.


        """

        self._typeSupports = str(typeSupports)

        self._typeSupportsExists = True

    def clearTypeSupports(self):
        """
        Mark typeSupports, which is an optional field, as non-existent.
        """
        self._typeSupportsExists = False

    # ===> Attribute numSupports, which is optional
    _numSupportsExists = False

    _numSupports = 0

    def isNumSupportsExists(self):
        """
        The attribute numSupports is optional. Return True if this attribute exists.
        return True if and only if the numSupports attribute exists.
        """
        return self._numSupportsExists

    def getNumSupports(self):
        """
        Get numSupports, which is optional.
        return numSupports as int
        raises ValueError If numSupports does not exist.
        """
        if not self._numSupportsExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numSupports
                + " attribute in table CalAppPhase does not exist!"
            )

        return self._numSupports

    def setNumSupports(self, numSupports):
        """
        Set numSupports with the specified int value.
        numSupports The int value to which numSupports is to be set.


        """

        self._numSupports = int(numSupports)

        self._numSupportsExists = True

    def clearNumSupports(self):
        """
        Mark numSupports, which is an optional field, as non-existent.
        """
        self._numSupportsExists = False

    # ===> Attribute phaseSupports, which is optional
    _phaseSupportsExists = False

    _phaseSupports = None  # this is a 1D list of float

    def isPhaseSupportsExists(self):
        """
        The attribute phaseSupports is optional. Return True if this attribute exists.
        return True if and only if the phaseSupports attribute exists.
        """
        return self._phaseSupportsExists

    def getPhaseSupports(self):
        """
        Get phaseSupports, which is optional.
        return phaseSupports as float []
        raises ValueError If phaseSupports does not exist.
        """
        if not self._phaseSupportsExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + phaseSupports
                + " attribute in table CalAppPhase does not exist!"
            )

        return copy.deepcopy(self._phaseSupports)

    def setPhaseSupports(self, phaseSupports):
        """
        Set phaseSupports with the specified float []  value.
        phaseSupports The float []  value to which phaseSupports is to be set.


        """

        # value must be a list
        if not isinstance(phaseSupports, list):
            raise ValueError("The value of phaseSupports must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(phaseSupports)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of phaseSupports is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(phaseSupports, float):
                raise ValueError(
                    "type of the first value in phaseSupports is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phaseSupports = copy.deepcopy(phaseSupports)
        except Exception as exc:
            raise ValueError("Invalid phaseSupports : " + str(exc))

        self._phaseSupportsExists = True

    def clearPhaseSupports(self):
        """
        Mark phaseSupports, which is an optional field, as non-existent.
        """
        self._phaseSupportsExists = False

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
        basebandName,
        scanNumber,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        adjustTime,
        adjustToken,
        phasingMode,
        numPhasedAntennas,
        phasedAntennas,
        refAntennaIndex,
        candRefAntennaIndex,
        phasePacking,
        numReceptors,
        numChannels,
        numPhaseValues,
        phaseValues,
        numCompare,
        numEfficiencies,
        compareArray,
        efficiencyIndices,
        efficiencies,
        quality,
        phasedSumAntenna,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalAppPhaseRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # basebandName is a BasebandName, compare using the == operator on the getValue() output
        if not (self._basebandName.getValue() == basebandName.getValue()):
            return False

        # scanNumber is a int, compare using the == operator.
        if not (self._scanNumber == scanNumber):
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

        # adjustTime is a ArrayTime, compare using the equals method.
        if not self._adjustTime.equals(adjustTime):
            return False

        # adjustToken is a str, compare using the == operator.
        if not (self._adjustToken == adjustToken):
            return False

        # phasingMode is a str, compare using the == operator.
        if not (self._phasingMode == phasingMode):
            return False

        # numPhasedAntennas is a int, compare using the == operator.
        if not (self._numPhasedAntennas == numPhasedAntennas):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phasedAntennas) != len(phasedAntennas):
            return False
        for indx in range(len(phasedAntennas)):

            # phasedAntennas is a list of str, compare using == operator.
            if not (self._phasedAntennas[indx] == phasedAntennas[indx]):
                return False

        # refAntennaIndex is a int, compare using the == operator.
        if not (self._refAntennaIndex == refAntennaIndex):
            return False

        # candRefAntennaIndex is a int, compare using the == operator.
        if not (self._candRefAntennaIndex == candRefAntennaIndex):
            return False

        # phasePacking is a str, compare using the == operator.
        if not (self._phasePacking == phasePacking):
            return False

        # numReceptors is a int, compare using the == operator.
        if not (self._numReceptors == numReceptors):
            return False

        # numChannels is a int, compare using the == operator.
        if not (self._numChannels == numChannels):
            return False

        # numPhaseValues is a int, compare using the == operator.
        if not (self._numPhaseValues == numPhaseValues):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseValues) != len(phaseValues):
            return False
        for indx in range(len(phaseValues)):

            # phaseValues is a list of float, compare using == operator.
            if not (self._phaseValues[indx] == phaseValues[indx]):
                return False

        # numCompare is a int, compare using the == operator.
        if not (self._numCompare == numCompare):
            return False

        # numEfficiencies is a int, compare using the == operator.
        if not (self._numEfficiencies == numEfficiencies):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._compareArray) != len(compareArray):
            return False
        for indx in range(len(compareArray)):

            # compareArray is a list of str, compare using == operator.
            if not (self._compareArray[indx] == compareArray[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._efficiencyIndices) != len(efficiencyIndices):
            return False
        for indx in range(len(efficiencyIndices)):

            # efficiencyIndices is a list of int, compare using == operator.
            if not (self._efficiencyIndices[indx] == efficiencyIndices[indx]):
                return False

        # We compare two 2D arrays (lists).
        if efficiencies is not None:
            if self._efficiencies is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            efficiencies_dims = pyasdm.utils.getListDims(efficiencies)
            this_efficiencies_dims = pyasdm.utils.getListDims(self._efficiencies)
            if efficiencies_dims != this_efficiencies_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(efficiencies_dims[0]):
                for j in range(efficiencies_dims[1]):

                    # efficiencies is an array of float, compare using == operator.
                    if not (self._efficiencies[i][j] == efficiencies[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._quality) != len(quality):
            return False
        for indx in range(len(quality)):

            # quality is a list of float, compare using == operator.
            if not (self._quality[indx] == quality[indx]):
                return False

        # phasedSumAntenna is a str, compare using the == operator.
        if not (self._phasedSumAntenna == phasedSumAntenna):
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
            otherRow.getAdjustTime(),
            otherRow.getAdjustToken(),
            otherRow.getPhasingMode(),
            otherRow.getNumPhasedAntennas(),
            otherRow.getPhasedAntennas(),
            otherRow.getRefAntennaIndex(),
            otherRow.getCandRefAntennaIndex(),
            otherRow.getPhasePacking(),
            otherRow.getNumReceptors(),
            otherRow.getNumChannels(),
            otherRow.getNumPhaseValues(),
            otherRow.getPhaseValues(),
            otherRow.getNumCompare(),
            otherRow.getNumEfficiencies(),
            otherRow.getCompareArray(),
            otherRow.getEfficiencyIndices(),
            otherRow.getEfficiencies(),
            otherRow.getQuality(),
            otherRow.getPhasedSumAntenna(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        adjustTime,
        adjustToken,
        phasingMode,
        numPhasedAntennas,
        phasedAntennas,
        refAntennaIndex,
        candRefAntennaIndex,
        phasePacking,
        numReceptors,
        numChannels,
        numPhaseValues,
        phaseValues,
        numCompare,
        numEfficiencies,
        compareArray,
        efficiencyIndices,
        efficiencies,
        quality,
        phasedSumAntenna,
    ):

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # adjustTime is a ArrayTime, compare using the equals method.
        if not self._adjustTime.equals(adjustTime):
            return False

        # adjustToken is a str, compare using the == operator.
        if not (self._adjustToken == adjustToken):
            return False

        # phasingMode is a str, compare using the == operator.
        if not (self._phasingMode == phasingMode):
            return False

        # numPhasedAntennas is a int, compare using the == operator.
        if not (self._numPhasedAntennas == numPhasedAntennas):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phasedAntennas) != len(phasedAntennas):
            return False
        for indx in range(len(phasedAntennas)):

            # phasedAntennas is a list of str, compare using == operator.
            if not (self._phasedAntennas[indx] == phasedAntennas[indx]):
                return False

        # refAntennaIndex is a int, compare using the == operator.
        if not (self._refAntennaIndex == refAntennaIndex):
            return False

        # candRefAntennaIndex is a int, compare using the == operator.
        if not (self._candRefAntennaIndex == candRefAntennaIndex):
            return False

        # phasePacking is a str, compare using the == operator.
        if not (self._phasePacking == phasePacking):
            return False

        # numReceptors is a int, compare using the == operator.
        if not (self._numReceptors == numReceptors):
            return False

        # numChannels is a int, compare using the == operator.
        if not (self._numChannels == numChannels):
            return False

        # numPhaseValues is a int, compare using the == operator.
        if not (self._numPhaseValues == numPhaseValues):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseValues) != len(phaseValues):
            return False
        for indx in range(len(phaseValues)):

            # phaseValues is a list of float, compare using == operator.
            if not (self._phaseValues[indx] == phaseValues[indx]):
                return False

        # numCompare is a int, compare using the == operator.
        if not (self._numCompare == numCompare):
            return False

        # numEfficiencies is a int, compare using the == operator.
        if not (self._numEfficiencies == numEfficiencies):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._compareArray) != len(compareArray):
            return False
        for indx in range(len(compareArray)):

            # compareArray is a list of str, compare using == operator.
            if not (self._compareArray[indx] == compareArray[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._efficiencyIndices) != len(efficiencyIndices):
            return False
        for indx in range(len(efficiencyIndices)):

            # efficiencyIndices is a list of int, compare using == operator.
            if not (self._efficiencyIndices[indx] == efficiencyIndices[indx]):
                return False

        # We compare two 2D arrays (lists).
        if efficiencies is not None:
            if self._efficiencies is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            efficiencies_dims = pyasdm.utils.getListDims(efficiencies)
            this_efficiencies_dims = pyasdm.utils.getListDims(self._efficiencies)
            if efficiencies_dims != this_efficiencies_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(efficiencies_dims[0]):
                for j in range(efficiencies_dims[1]):

                    # efficiencies is an array of float, compare using == operator.
                    if not (self._efficiencies[i][j] == efficiencies[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._quality) != len(quality):
            return False
        for indx in range(len(quality)):

            # quality is a list of float, compare using == operator.
            if not (self._quality[indx] == quality[indx]):
                return False

        # phasedSumAntenna is a str, compare using the == operator.
        if not (self._phasedSumAntenna == phasedSumAntenna):
            return False

        return True


# initialize the dictionary that maps fields to init methods
CalAppPhaseRow.initFromBinMethods()
