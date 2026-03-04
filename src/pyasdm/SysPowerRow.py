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
# File SysPowerRow.py
#

import pyasdm.SysPowerTable

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


class SysPowerRow:
    """
    The SysPowerRow class is a row of a SysPowerTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a SysPowerRow.
        When row is None, create an empty row attached to table, which must be a SysPowerTable.
        When row is given, copy those values in to the new row. The row argument must be a SysPowerRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.SysPowerTable):
            raise ValueError("table must be a SysPowerTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._timeInterval = ArrayTimeInterval()

        self._numReceptor = 0

        self._switchedPowerDifferenceExists = False

        self._switchedPowerDifference = []  # this is a list of float []

        self._switchedPowerSumExists = False

        self._switchedPowerSum = []  # this is a list of float []

        self._requantizerGainExists = False

        self._requantizerGain = []  # this is a list of float []

        self._numChannelsExists = False

        self._numChannels = 0

        self._numPolarizationTypeExists = False

        self._numPolarizationType = 0

        self._chanFreqStartExists = False

        self._chanFreqStart = Frequency()

        self._chanFreqStepExists = False

        self._chanFreqStep = Frequency()

        self._switchedPowerDifferenceSpectrumExists = False

        self._switchedPowerDifferenceSpectrum = []  # this is a list of float []  []

        self._switchedPowerSumSpectrumExists = False

        self._switchedPowerSumSpectrum = []  # this is a list of float []  []

        self._requantizerGainSpectrumExists = False

        self._requantizerGainSpectrum = []  # this is a list of float []  []

        # extrinsic attributes

        self._antennaId = Tag()

        self._feedId = 0

        self._spectralWindowId = Tag()

        if row is not None:
            if not isinstance(row, SysPowerRow):
                raise ValueError("row must be a SysPowerRow")

            # copy constructor

            self._antennaId = Tag(row._antennaId)

            self._spectralWindowId = Tag(row._spectralWindowId)

            self._feedId = row._feedId

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._numReceptor = row._numReceptor

            # by default set systematically switchedPowerDifference's value to something not None

            if row._switchedPowerDifferenceExists:

                # switchedPowerDifference is a list, make a deep copy
                self._switchedPowerDifference = copy.deepcopy(
                    row._switchedPowerDifference
                )

                self._switchedPowerDifferenceExists = True

            # by default set systematically switchedPowerSum's value to something not None

            if row._switchedPowerSumExists:

                # switchedPowerSum is a list, make a deep copy
                self._switchedPowerSum = copy.deepcopy(row._switchedPowerSum)

                self._switchedPowerSumExists = True

            # by default set systematically requantizerGain's value to something not None

            if row._requantizerGainExists:

                # requantizerGain is a list, make a deep copy
                self._requantizerGain = copy.deepcopy(row._requantizerGain)

                self._requantizerGainExists = True

            # by default set systematically numChannels's value to something not None

            if row._numChannelsExists:

                self._numChannels = row._numChannels

                self._numChannelsExists = True

            # by default set systematically numPolarizationType's value to something not None

            if row._numPolarizationTypeExists:

                self._numPolarizationType = row._numPolarizationType

                self._numPolarizationTypeExists = True

            # by default set systematically chanFreqStart's value to something not None

            if row._chanFreqStartExists:

                self._chanFreqStart = Frequency(row._chanFreqStart)

                self._chanFreqStartExists = True

            # by default set systematically chanFreqStep's value to something not None

            if row._chanFreqStepExists:

                self._chanFreqStep = Frequency(row._chanFreqStep)

                self._chanFreqStepExists = True

            # by default set systematically switchedPowerDifferenceSpectrum's value to something not None

            if row._switchedPowerDifferenceSpectrumExists:

                # switchedPowerDifferenceSpectrum is a list, make a deep copy
                self._switchedPowerDifferenceSpectrum = copy.deepcopy(
                    row._switchedPowerDifferenceSpectrum
                )

                self._switchedPowerDifferenceSpectrumExists = True

            # by default set systematically switchedPowerSumSpectrum's value to something not None

            if row._switchedPowerSumSpectrumExists:

                # switchedPowerSumSpectrum is a list, make a deep copy
                self._switchedPowerSumSpectrum = copy.deepcopy(
                    row._switchedPowerSumSpectrum
                )

                self._switchedPowerSumSpectrumExists = True

            # by default set systematically requantizerGainSpectrum's value to something not None

            if row._requantizerGainSpectrumExists:

                # requantizerGainSpectrum is a list, make a deep copy
                self._requantizerGainSpectrum = copy.deepcopy(
                    row._requantizerGainSpectrum
                )

                self._requantizerGainSpectrumExists = True

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

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        if self._switchedPowerDifferenceExists:

            result += Parser.listValueToXML(
                "switchedPowerDifference", self._switchedPowerDifference
            )

        if self._switchedPowerSumExists:

            result += Parser.listValueToXML("switchedPowerSum", self._switchedPowerSum)

        if self._requantizerGainExists:

            result += Parser.listValueToXML("requantizerGain", self._requantizerGain)

        if self._numChannelsExists:

            result += Parser.valueToXML("numChannels", self._numChannels)

        if self._numPolarizationTypeExists:

            result += Parser.valueToXML(
                "numPolarizationType", self._numPolarizationType
            )

        if self._chanFreqStartExists:

            result += Parser.extendedValueToXML("chanFreqStart", self._chanFreqStart)

        if self._chanFreqStepExists:

            result += Parser.extendedValueToXML("chanFreqStep", self._chanFreqStep)

        if self._switchedPowerDifferenceSpectrumExists:

            result += Parser.listValueToXML(
                "switchedPowerDifferenceSpectrum", self._switchedPowerDifferenceSpectrum
            )

        if self._switchedPowerSumSpectrumExists:

            result += Parser.listValueToXML(
                "switchedPowerSumSpectrum", self._switchedPowerSumSpectrum
            )

        if self._requantizerGainSpectrumExists:

            result += Parser.listValueToXML(
                "requantizerGainSpectrum", self._requantizerGainSpectrum
            )

        # extrinsic attributes

        result += Parser.extendedValueToXML("antennaId", self._antennaId)

        result += Parser.valueToXML("feedId", self._feedId)

        result += Parser.extendedValueToXML("spectralWindowId", self._spectralWindowId)

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
                "xmlrow is not a string or a minidom.Element", "SysPowerTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "SysPowerTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        switchedPowerDifferenceNode = rowdom.getElementsByTagName(
            "switchedPowerDifference"
        )
        if len(switchedPowerDifferenceNode) > 0:

            switchedPowerDifferenceStr = switchedPowerDifferenceNode[
                0
            ].firstChild.data.strip()

            self._switchedPowerDifference = Parser.stringListToLists(
                switchedPowerDifferenceStr, float, "SysPower", False
            )

            self._switchedPowerDifferenceExists = True

        switchedPowerSumNode = rowdom.getElementsByTagName("switchedPowerSum")
        if len(switchedPowerSumNode) > 0:

            switchedPowerSumStr = switchedPowerSumNode[0].firstChild.data.strip()

            self._switchedPowerSum = Parser.stringListToLists(
                switchedPowerSumStr, float, "SysPower", False
            )

            self._switchedPowerSumExists = True

        requantizerGainNode = rowdom.getElementsByTagName("requantizerGain")
        if len(requantizerGainNode) > 0:

            requantizerGainStr = requantizerGainNode[0].firstChild.data.strip()

            self._requantizerGain = Parser.stringListToLists(
                requantizerGainStr, float, "SysPower", False
            )

            self._requantizerGainExists = True

        numChannelsNode = rowdom.getElementsByTagName("numChannels")
        if len(numChannelsNode) > 0:

            self._numChannels = int(numChannelsNode[0].firstChild.data.strip())

            self._numChannelsExists = True

        numPolarizationTypeNode = rowdom.getElementsByTagName("numPolarizationType")
        if len(numPolarizationTypeNode) > 0:

            self._numPolarizationType = int(
                numPolarizationTypeNode[0].firstChild.data.strip()
            )

            self._numPolarizationTypeExists = True

        chanFreqStartNode = rowdom.getElementsByTagName("chanFreqStart")
        if len(chanFreqStartNode) > 0:

            self._chanFreqStart = Frequency(
                chanFreqStartNode[0].firstChild.data.strip()
            )

            self._chanFreqStartExists = True

        chanFreqStepNode = rowdom.getElementsByTagName("chanFreqStep")
        if len(chanFreqStepNode) > 0:

            self._chanFreqStep = Frequency(chanFreqStepNode[0].firstChild.data.strip())

            self._chanFreqStepExists = True

        switchedPowerDifferenceSpectrumNode = rowdom.getElementsByTagName(
            "switchedPowerDifferenceSpectrum"
        )
        if len(switchedPowerDifferenceSpectrumNode) > 0:

            switchedPowerDifferenceSpectrumStr = switchedPowerDifferenceSpectrumNode[
                0
            ].firstChild.data.strip()

            self._switchedPowerDifferenceSpectrum = Parser.stringListToLists(
                switchedPowerDifferenceSpectrumStr, float, "SysPower", False
            )

            self._switchedPowerDifferenceSpectrumExists = True

        switchedPowerSumSpectrumNode = rowdom.getElementsByTagName(
            "switchedPowerSumSpectrum"
        )
        if len(switchedPowerSumSpectrumNode) > 0:

            switchedPowerSumSpectrumStr = switchedPowerSumSpectrumNode[
                0
            ].firstChild.data.strip()

            self._switchedPowerSumSpectrum = Parser.stringListToLists(
                switchedPowerSumSpectrumStr, float, "SysPower", False
            )

            self._switchedPowerSumSpectrumExists = True

        requantizerGainSpectrumNode = rowdom.getElementsByTagName(
            "requantizerGainSpectrum"
        )
        if len(requantizerGainSpectrumNode) > 0:

            requantizerGainSpectrumStr = requantizerGainSpectrumNode[
                0
            ].firstChild.data.strip()

            self._requantizerGainSpectrum = Parser.stringListToLists(
                requantizerGainSpectrumStr, float, "SysPower", False
            )

            self._requantizerGainSpectrumExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        self._antennaId = Tag(antennaIdNode.firstChild.data.strip())

        feedIdNode = rowdom.getElementsByTagName("feedId")[0]

        self._feedId = int(feedIdNode.firstChild.data.strip())

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")[0]

        self._spectralWindowId = Tag(spectralWindowIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._antennaId.toBin(eos)

        self._spectralWindowId.toBin(eos)

        eos.writeInt(self._feedId)

        self._timeInterval.toBin(eos)

        eos.writeInt(self._numReceptor)

        eos.writeBool(self._switchedPowerDifferenceExists)
        if self._switchedPowerDifferenceExists:

            eos.writeInt(len(self._switchedPowerDifference))
            for i in range(len(self._switchedPowerDifference)):

                eos.writeFloat(self._switchedPowerDifference[i])

        eos.writeBool(self._switchedPowerSumExists)
        if self._switchedPowerSumExists:

            eos.writeInt(len(self._switchedPowerSum))
            for i in range(len(self._switchedPowerSum)):

                eos.writeFloat(self._switchedPowerSum[i])

        eos.writeBool(self._requantizerGainExists)
        if self._requantizerGainExists:

            eos.writeInt(len(self._requantizerGain))
            for i in range(len(self._requantizerGain)):

                eos.writeFloat(self._requantizerGain[i])

        eos.writeBool(self._numChannelsExists)
        if self._numChannelsExists:

            eos.writeInt(self._numChannels)

        eos.writeBool(self._numPolarizationTypeExists)
        if self._numPolarizationTypeExists:

            eos.writeInt(self._numPolarizationType)

        eos.writeBool(self._chanFreqStartExists)
        if self._chanFreqStartExists:

            self._chanFreqStart.toBin(eos)

        eos.writeBool(self._chanFreqStepExists)
        if self._chanFreqStepExists:

            self._chanFreqStep.toBin(eos)

        eos.writeBool(self._switchedPowerDifferenceSpectrumExists)
        if self._switchedPowerDifferenceSpectrumExists:

            # null array case, unsure if this is possible but this should work
            if self._switchedPowerDifferenceSpectrum is None:
                eos.writeInt(0)
                eos.writeInt(0)
            else:
                switchedPowerDifferenceSpectrum_dims = pyasdm.utils.getListDims(
                    self._switchedPowerDifferenceSpectrum
                )
            # assumes it really is 2D
            eos.writeInt(switchedPowerDifferenceSpectrum_dims[0])
            eos.writeInt(switchedPowerDifferenceSpectrum_dims[1])
            for i in range(switchedPowerDifferenceSpectrum_dims[0]):
                for j in range(switchedPowerDifferenceSpectrum_dims[1]):
                    eos.writeFloat(self._switchedPowerDifferenceSpectrum[i][j])

        eos.writeBool(self._switchedPowerSumSpectrumExists)
        if self._switchedPowerSumSpectrumExists:

            # null array case, unsure if this is possible but this should work
            if self._switchedPowerSumSpectrum is None:
                eos.writeInt(0)
                eos.writeInt(0)
            else:
                switchedPowerSumSpectrum_dims = pyasdm.utils.getListDims(
                    self._switchedPowerSumSpectrum
                )
            # assumes it really is 2D
            eos.writeInt(switchedPowerSumSpectrum_dims[0])
            eos.writeInt(switchedPowerSumSpectrum_dims[1])
            for i in range(switchedPowerSumSpectrum_dims[0]):
                for j in range(switchedPowerSumSpectrum_dims[1]):
                    eos.writeFloat(self._switchedPowerSumSpectrum[i][j])

        eos.writeBool(self._requantizerGainSpectrumExists)
        if self._requantizerGainSpectrumExists:

            # null array case, unsure if this is possible but this should work
            if self._requantizerGainSpectrum is None:
                eos.writeInt(0)
                eos.writeInt(0)
            else:
                requantizerGainSpectrum_dims = pyasdm.utils.getListDims(
                    self._requantizerGainSpectrum
                )
            # assumes it really is 2D
            eos.writeInt(requantizerGainSpectrum_dims[0])
            eos.writeInt(requantizerGainSpectrum_dims[1])
            for i in range(requantizerGainSpectrum_dims[0]):
                for j in range(requantizerGainSpectrum_dims[1]):
                    eos.writeFloat(self._requantizerGainSpectrum[i][j])

    @staticmethod
    def antennaIdFromBin(row, eis):
        """
        Set the antennaId in row from the EndianInput (eis) instance.
        """

        row._antennaId = Tag.fromBin(eis)

    @staticmethod
    def spectralWindowIdFromBin(row, eis):
        """
        Set the spectralWindowId in row from the EndianInput (eis) instance.
        """

        row._spectralWindowId = Tag.fromBin(eis)

    @staticmethod
    def feedIdFromBin(row, eis):
        """
        Set the feedId in row from the EndianInput (eis) instance.
        """

        row._feedId = eis.readInt()

    @staticmethod
    def timeIntervalFromBin(row, eis):
        """
        Set the timeInterval in row from the EndianInput (eis) instance.
        """

        row._timeInterval = ArrayTimeInterval.fromBin(eis)

    @staticmethod
    def numReceptorFromBin(row, eis):
        """
        Set the numReceptor in row from the EndianInput (eis) instance.
        """

        row._numReceptor = eis.readInt()

    @staticmethod
    def switchedPowerDifferenceFromBin(row, eis):
        """
        Set the optional switchedPowerDifference in row from the EndianInput (eis) instance.
        """
        row._switchedPowerDifferenceExists = eis.readBool()
        if row._switchedPowerDifferenceExists:

            switchedPowerDifferenceDim1 = eis.readInt()
            thisList = []
            for i in range(switchedPowerDifferenceDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._switchedPowerDifference = thisList

    @staticmethod
    def switchedPowerSumFromBin(row, eis):
        """
        Set the optional switchedPowerSum in row from the EndianInput (eis) instance.
        """
        row._switchedPowerSumExists = eis.readBool()
        if row._switchedPowerSumExists:

            switchedPowerSumDim1 = eis.readInt()
            thisList = []
            for i in range(switchedPowerSumDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._switchedPowerSum = thisList

    @staticmethod
    def requantizerGainFromBin(row, eis):
        """
        Set the optional requantizerGain in row from the EndianInput (eis) instance.
        """
        row._requantizerGainExists = eis.readBool()
        if row._requantizerGainExists:

            requantizerGainDim1 = eis.readInt()
            thisList = []
            for i in range(requantizerGainDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._requantizerGain = thisList

    @staticmethod
    def numChannelsFromBin(row, eis):
        """
        Set the optional numChannels in row from the EndianInput (eis) instance.
        """
        row._numChannelsExists = eis.readBool()
        if row._numChannelsExists:

            row._numChannels = eis.readInt()

    @staticmethod
    def numPolarizationTypeFromBin(row, eis):
        """
        Set the optional numPolarizationType in row from the EndianInput (eis) instance.
        """
        row._numPolarizationTypeExists = eis.readBool()
        if row._numPolarizationTypeExists:

            row._numPolarizationType = eis.readInt()

    @staticmethod
    def chanFreqStartFromBin(row, eis):
        """
        Set the optional chanFreqStart in row from the EndianInput (eis) instance.
        """
        row._chanFreqStartExists = eis.readBool()
        if row._chanFreqStartExists:

            row._chanFreqStart = Frequency.fromBin(eis)

    @staticmethod
    def chanFreqStepFromBin(row, eis):
        """
        Set the optional chanFreqStep in row from the EndianInput (eis) instance.
        """
        row._chanFreqStepExists = eis.readBool()
        if row._chanFreqStepExists:

            row._chanFreqStep = Frequency.fromBin(eis)

    @staticmethod
    def switchedPowerDifferenceSpectrumFromBin(row, eis):
        """
        Set the optional switchedPowerDifferenceSpectrum in row from the EndianInput (eis) instance.
        """
        row._switchedPowerDifferenceSpectrumExists = eis.readBool()
        if row._switchedPowerDifferenceSpectrumExists:

            switchedPowerDifferenceSpectrumDim1 = eis.readInt()
            switchedPowerDifferenceSpectrumDim2 = eis.readInt()
            thisList = []
            for i in range(switchedPowerDifferenceSpectrumDim1):
                thisList_j = []
                for j in range(switchedPowerDifferenceSpectrumDim2):
                    thisValue = eis.readFloat()
                    thisList_j.append(thisValue)
                thisList.append(thisList_j)
            row._switchedPowerDifferenceSpectrum = thisList

    @staticmethod
    def switchedPowerSumSpectrumFromBin(row, eis):
        """
        Set the optional switchedPowerSumSpectrum in row from the EndianInput (eis) instance.
        """
        row._switchedPowerSumSpectrumExists = eis.readBool()
        if row._switchedPowerSumSpectrumExists:

            switchedPowerSumSpectrumDim1 = eis.readInt()
            switchedPowerSumSpectrumDim2 = eis.readInt()
            thisList = []
            for i in range(switchedPowerSumSpectrumDim1):
                thisList_j = []
                for j in range(switchedPowerSumSpectrumDim2):
                    thisValue = eis.readFloat()
                    thisList_j.append(thisValue)
                thisList.append(thisList_j)
            row._switchedPowerSumSpectrum = thisList

    @staticmethod
    def requantizerGainSpectrumFromBin(row, eis):
        """
        Set the optional requantizerGainSpectrum in row from the EndianInput (eis) instance.
        """
        row._requantizerGainSpectrumExists = eis.readBool()
        if row._requantizerGainSpectrumExists:

            requantizerGainSpectrumDim1 = eis.readInt()
            requantizerGainSpectrumDim2 = eis.readInt()
            thisList = []
            for i in range(requantizerGainSpectrumDim1):
                thisList_j = []
                for j in range(requantizerGainSpectrumDim2):
                    thisValue = eis.readFloat()
                    thisList_j.append(thisValue)
                thisList.append(thisList_j)
            row._requantizerGainSpectrum = thisList

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaId"] = SysPowerRow.antennaIdFromBin
        _fromBinMethods["spectralWindowId"] = SysPowerRow.spectralWindowIdFromBin
        _fromBinMethods["feedId"] = SysPowerRow.feedIdFromBin
        _fromBinMethods["timeInterval"] = SysPowerRow.timeIntervalFromBin
        _fromBinMethods["numReceptor"] = SysPowerRow.numReceptorFromBin

        _fromBinMethods["switchedPowerDifference"] = (
            SysPowerRow.switchedPowerDifferenceFromBin
        )
        _fromBinMethods["switchedPowerSum"] = SysPowerRow.switchedPowerSumFromBin
        _fromBinMethods["requantizerGain"] = SysPowerRow.requantizerGainFromBin
        _fromBinMethods["numChannels"] = SysPowerRow.numChannelsFromBin
        _fromBinMethods["numPolarizationType"] = SysPowerRow.numPolarizationTypeFromBin
        _fromBinMethods["chanFreqStart"] = SysPowerRow.chanFreqStartFromBin
        _fromBinMethods["chanFreqStep"] = SysPowerRow.chanFreqStepFromBin
        _fromBinMethods["switchedPowerDifferenceSpectrum"] = (
            SysPowerRow.switchedPowerDifferenceSpectrumFromBin
        )
        _fromBinMethods["switchedPowerSumSpectrum"] = (
            SysPowerRow.switchedPowerSumSpectrumFromBin
        )
        _fromBinMethods["requantizerGainSpectrum"] = (
            SysPowerRow.requantizerGainSpectrumFromBin
        )

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = SysPowerRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " SysPower",
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

    # ===> Attribute switchedPowerDifference, which is optional
    _switchedPowerDifferenceExists = False

    _switchedPowerDifference = None  # this is a 1D list of float

    def isSwitchedPowerDifferenceExists(self):
        """
        The attribute switchedPowerDifference is optional. Return True if this attribute exists.
        return True if and only if the switchedPowerDifference attribute exists.
        """
        return self._switchedPowerDifferenceExists

    def getSwitchedPowerDifference(self):
        """
        Get switchedPowerDifference, which is optional.
        return switchedPowerDifference as float []
        raises ValueError If switchedPowerDifference does not exist.
        """
        if not self._switchedPowerDifferenceExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + "'switchedPowerDifference' attribute in table SysPower does not exist!"
            )

        return copy.deepcopy(self._switchedPowerDifference)

    def setSwitchedPowerDifference(self, switchedPowerDifference):
        """
        Set switchedPowerDifference with the specified float []  value.
        switchedPowerDifference The float []  value to which switchedPowerDifference is to be set.


        """

        # value must be a list
        if not isinstance(switchedPowerDifference, list):
            raise ValueError("The value of switchedPowerDifference must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(switchedPowerDifference)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of switchedPowerDifference is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(switchedPowerDifference, float):
                raise ValueError(
                    "type of the first value in switchedPowerDifference is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._switchedPowerDifference = copy.deepcopy(switchedPowerDifference)
        except Exception as exc:
            raise ValueError("Invalid switchedPowerDifference : " + str(exc))

        self._switchedPowerDifferenceExists = True

    def clearSwitchedPowerDifference(self):
        """
        Mark switchedPowerDifference, which is an optional field, as non-existent.
        """
        self._switchedPowerDifferenceExists = False

    # ===> Attribute switchedPowerSum, which is optional
    _switchedPowerSumExists = False

    _switchedPowerSum = None  # this is a 1D list of float

    def isSwitchedPowerSumExists(self):
        """
        The attribute switchedPowerSum is optional. Return True if this attribute exists.
        return True if and only if the switchedPowerSum attribute exists.
        """
        return self._switchedPowerSumExists

    def getSwitchedPowerSum(self):
        """
        Get switchedPowerSum, which is optional.
        return switchedPowerSum as float []
        raises ValueError If switchedPowerSum does not exist.
        """
        if not self._switchedPowerSumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + "'switchedPowerSum' attribute in table SysPower does not exist!"
            )

        return copy.deepcopy(self._switchedPowerSum)

    def setSwitchedPowerSum(self, switchedPowerSum):
        """
        Set switchedPowerSum with the specified float []  value.
        switchedPowerSum The float []  value to which switchedPowerSum is to be set.


        """

        # value must be a list
        if not isinstance(switchedPowerSum, list):
            raise ValueError("The value of switchedPowerSum must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(switchedPowerSum)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of switchedPowerSum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(switchedPowerSum, float):
                raise ValueError(
                    "type of the first value in switchedPowerSum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._switchedPowerSum = copy.deepcopy(switchedPowerSum)
        except Exception as exc:
            raise ValueError("Invalid switchedPowerSum : " + str(exc))

        self._switchedPowerSumExists = True

    def clearSwitchedPowerSum(self):
        """
        Mark switchedPowerSum, which is an optional field, as non-existent.
        """
        self._switchedPowerSumExists = False

    # ===> Attribute requantizerGain, which is optional
    _requantizerGainExists = False

    _requantizerGain = None  # this is a 1D list of float

    def isRequantizerGainExists(self):
        """
        The attribute requantizerGain is optional. Return True if this attribute exists.
        return True if and only if the requantizerGain attribute exists.
        """
        return self._requantizerGainExists

    def getRequantizerGain(self):
        """
        Get requantizerGain, which is optional.
        return requantizerGain as float []
        raises ValueError If requantizerGain does not exist.
        """
        if not self._requantizerGainExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + "'requantizerGain' attribute in table SysPower does not exist!"
            )

        return copy.deepcopy(self._requantizerGain)

    def setRequantizerGain(self, requantizerGain):
        """
        Set requantizerGain with the specified float []  value.
        requantizerGain The float []  value to which requantizerGain is to be set.


        """

        # value must be a list
        if not isinstance(requantizerGain, list):
            raise ValueError("The value of requantizerGain must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(requantizerGain)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of requantizerGain is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(requantizerGain, float):
                raise ValueError(
                    "type of the first value in requantizerGain is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._requantizerGain = copy.deepcopy(requantizerGain)
        except Exception as exc:
            raise ValueError("Invalid requantizerGain : " + str(exc))

        self._requantizerGainExists = True

    def clearRequantizerGain(self):
        """
        Mark requantizerGain, which is an optional field, as non-existent.
        """
        self._requantizerGainExists = False

    # ===> Attribute numChannels, which is optional
    _numChannelsExists = False

    _numChannels = 0

    def isNumChannelsExists(self):
        """
        The attribute numChannels is optional. Return True if this attribute exists.
        return True if and only if the numChannels attribute exists.
        """
        return self._numChannelsExists

    def getNumChannels(self):
        """
        Get numChannels, which is optional.
        return numChannels as int
        raises ValueError If numChannels does not exist.
        """
        if not self._numChannelsExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + "'numChannels' attribute in table SysPower does not exist!"
            )

        return self._numChannels

    def setNumChannels(self, numChannels):
        """
        Set numChannels with the specified int value.
        numChannels The int value to which numChannels is to be set.


        """

        self._numChannels = int(numChannels)

        self._numChannelsExists = True

    def clearNumChannels(self):
        """
        Mark numChannels, which is an optional field, as non-existent.
        """
        self._numChannelsExists = False

    # ===> Attribute numPolarizationType, which is optional
    _numPolarizationTypeExists = False

    _numPolarizationType = 0

    def isNumPolarizationTypeExists(self):
        """
        The attribute numPolarizationType is optional. Return True if this attribute exists.
        return True if and only if the numPolarizationType attribute exists.
        """
        return self._numPolarizationTypeExists

    def getNumPolarizationType(self):
        """
        Get numPolarizationType, which is optional.
        return numPolarizationType as int
        raises ValueError If numPolarizationType does not exist.
        """
        if not self._numPolarizationTypeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + "'numPolarizationType' attribute in table SysPower does not exist!"
            )

        return self._numPolarizationType

    def setNumPolarizationType(self, numPolarizationType):
        """
        Set numPolarizationType with the specified int value.
        numPolarizationType The int value to which numPolarizationType is to be set.


        """

        self._numPolarizationType = int(numPolarizationType)

        self._numPolarizationTypeExists = True

    def clearNumPolarizationType(self):
        """
        Mark numPolarizationType, which is an optional field, as non-existent.
        """
        self._numPolarizationTypeExists = False

    # ===> Attribute chanFreqStart, which is optional
    _chanFreqStartExists = False

    _chanFreqStart = Frequency()

    def isChanFreqStartExists(self):
        """
        The attribute chanFreqStart is optional. Return True if this attribute exists.
        return True if and only if the chanFreqStart attribute exists.
        """
        return self._chanFreqStartExists

    def getChanFreqStart(self):
        """
        Get chanFreqStart, which is optional.
        return chanFreqStart as Frequency
        raises ValueError If chanFreqStart does not exist.
        """
        if not self._chanFreqStartExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + "'chanFreqStart' attribute in table SysPower does not exist!"
            )

        # make sure it is a copy of Frequency
        return Frequency(self._chanFreqStart)

    def setChanFreqStart(self, chanFreqStart):
        """
        Set chanFreqStart with the specified Frequency value.
        chanFreqStart The Frequency value to which chanFreqStart is to be set.
        The value of chanFreqStart can be anything allowed by the Frequency constructor.

        """

        self._chanFreqStart = Frequency(chanFreqStart)

        self._chanFreqStartExists = True

    def clearChanFreqStart(self):
        """
        Mark chanFreqStart, which is an optional field, as non-existent.
        """
        self._chanFreqStartExists = False

    # ===> Attribute chanFreqStep, which is optional
    _chanFreqStepExists = False

    _chanFreqStep = Frequency()

    def isChanFreqStepExists(self):
        """
        The attribute chanFreqStep is optional. Return True if this attribute exists.
        return True if and only if the chanFreqStep attribute exists.
        """
        return self._chanFreqStepExists

    def getChanFreqStep(self):
        """
        Get chanFreqStep, which is optional.
        return chanFreqStep as Frequency
        raises ValueError If chanFreqStep does not exist.
        """
        if not self._chanFreqStepExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + "'chanFreqStep' attribute in table SysPower does not exist!"
            )

        # make sure it is a copy of Frequency
        return Frequency(self._chanFreqStep)

    def setChanFreqStep(self, chanFreqStep):
        """
        Set chanFreqStep with the specified Frequency value.
        chanFreqStep The Frequency value to which chanFreqStep is to be set.
        The value of chanFreqStep can be anything allowed by the Frequency constructor.

        """

        self._chanFreqStep = Frequency(chanFreqStep)

        self._chanFreqStepExists = True

    def clearChanFreqStep(self):
        """
        Mark chanFreqStep, which is an optional field, as non-existent.
        """
        self._chanFreqStepExists = False

    # ===> Attribute switchedPowerDifferenceSpectrum, which is optional
    _switchedPowerDifferenceSpectrumExists = False

    _switchedPowerDifferenceSpectrum = None  # this is a 2D list of float

    def isSwitchedPowerDifferenceSpectrumExists(self):
        """
        The attribute switchedPowerDifferenceSpectrum is optional. Return True if this attribute exists.
        return True if and only if the switchedPowerDifferenceSpectrum attribute exists.
        """
        return self._switchedPowerDifferenceSpectrumExists

    def getSwitchedPowerDifferenceSpectrum(self):
        """
        Get switchedPowerDifferenceSpectrum, which is optional.
        return switchedPowerDifferenceSpectrum as float []  []
        raises ValueError If switchedPowerDifferenceSpectrum does not exist.
        """
        if not self._switchedPowerDifferenceSpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + "'switchedPowerDifferenceSpectrum' attribute in table SysPower does not exist!"
            )

        return copy.deepcopy(self._switchedPowerDifferenceSpectrum)

    def setSwitchedPowerDifferenceSpectrum(self, switchedPowerDifferenceSpectrum):
        """
        Set switchedPowerDifferenceSpectrum with the specified float []  []  value.
        switchedPowerDifferenceSpectrum The float []  []  value to which switchedPowerDifferenceSpectrum is to be set.


        """

        # value must be a list
        if not isinstance(switchedPowerDifferenceSpectrum, list):
            raise ValueError(
                "The value of switchedPowerDifferenceSpectrum must be a list"
            )
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(switchedPowerDifferenceSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError(
                    "shape of switchedPowerDifferenceSpectrum is not correct"
                )

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(switchedPowerDifferenceSpectrum, float):
                raise ValueError(
                    "type of the first value in switchedPowerDifferenceSpectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._switchedPowerDifferenceSpectrum = copy.deepcopy(
                switchedPowerDifferenceSpectrum
            )
        except Exception as exc:
            raise ValueError("Invalid switchedPowerDifferenceSpectrum : " + str(exc))

        self._switchedPowerDifferenceSpectrumExists = True

    def clearSwitchedPowerDifferenceSpectrum(self):
        """
        Mark switchedPowerDifferenceSpectrum, which is an optional field, as non-existent.
        """
        self._switchedPowerDifferenceSpectrumExists = False

    # ===> Attribute switchedPowerSumSpectrum, which is optional
    _switchedPowerSumSpectrumExists = False

    _switchedPowerSumSpectrum = None  # this is a 2D list of float

    def isSwitchedPowerSumSpectrumExists(self):
        """
        The attribute switchedPowerSumSpectrum is optional. Return True if this attribute exists.
        return True if and only if the switchedPowerSumSpectrum attribute exists.
        """
        return self._switchedPowerSumSpectrumExists

    def getSwitchedPowerSumSpectrum(self):
        """
        Get switchedPowerSumSpectrum, which is optional.
        return switchedPowerSumSpectrum as float []  []
        raises ValueError If switchedPowerSumSpectrum does not exist.
        """
        if not self._switchedPowerSumSpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + "'switchedPowerSumSpectrum' attribute in table SysPower does not exist!"
            )

        return copy.deepcopy(self._switchedPowerSumSpectrum)

    def setSwitchedPowerSumSpectrum(self, switchedPowerSumSpectrum):
        """
        Set switchedPowerSumSpectrum with the specified float []  []  value.
        switchedPowerSumSpectrum The float []  []  value to which switchedPowerSumSpectrum is to be set.


        """

        # value must be a list
        if not isinstance(switchedPowerSumSpectrum, list):
            raise ValueError("The value of switchedPowerSumSpectrum must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(switchedPowerSumSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of switchedPowerSumSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(switchedPowerSumSpectrum, float):
                raise ValueError(
                    "type of the first value in switchedPowerSumSpectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._switchedPowerSumSpectrum = copy.deepcopy(switchedPowerSumSpectrum)
        except Exception as exc:
            raise ValueError("Invalid switchedPowerSumSpectrum : " + str(exc))

        self._switchedPowerSumSpectrumExists = True

    def clearSwitchedPowerSumSpectrum(self):
        """
        Mark switchedPowerSumSpectrum, which is an optional field, as non-existent.
        """
        self._switchedPowerSumSpectrumExists = False

    # ===> Attribute requantizerGainSpectrum, which is optional
    _requantizerGainSpectrumExists = False

    _requantizerGainSpectrum = None  # this is a 2D list of float

    def isRequantizerGainSpectrumExists(self):
        """
        The attribute requantizerGainSpectrum is optional. Return True if this attribute exists.
        return True if and only if the requantizerGainSpectrum attribute exists.
        """
        return self._requantizerGainSpectrumExists

    def getRequantizerGainSpectrum(self):
        """
        Get requantizerGainSpectrum, which is optional.
        return requantizerGainSpectrum as float []  []
        raises ValueError If requantizerGainSpectrum does not exist.
        """
        if not self._requantizerGainSpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + "'requantizerGainSpectrum' attribute in table SysPower does not exist!"
            )

        return copy.deepcopy(self._requantizerGainSpectrum)

    def setRequantizerGainSpectrum(self, requantizerGainSpectrum):
        """
        Set requantizerGainSpectrum with the specified float []  []  value.
        requantizerGainSpectrum The float []  []  value to which requantizerGainSpectrum is to be set.


        """

        # value must be a list
        if not isinstance(requantizerGainSpectrum, list):
            raise ValueError("The value of requantizerGainSpectrum must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(requantizerGainSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of requantizerGainSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(requantizerGainSpectrum, float):
                raise ValueError(
                    "type of the first value in requantizerGainSpectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._requantizerGainSpectrum = copy.deepcopy(requantizerGainSpectrum)
        except Exception as exc:
            raise ValueError("Invalid requantizerGainSpectrum : " + str(exc))

        self._requantizerGainSpectrumExists = True

    def clearRequantizerGainSpectrum(self):
        """
        Mark requantizerGainSpectrum, which is an optional field, as non-existent.
        """
        self._requantizerGainSpectrumExists = False

    # Extrinsic Table Attributes

    # ===> Attribute antennaId

    _antennaId = Tag()

    def getAntennaId(self):
        """
        Get antennaId.
        return antennaId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._antennaId)

    def setAntennaId(self, antennaId):
        """
        Set antennaId with the specified Tag value.
        antennaId The Tag value to which antennaId is to be set.
        The value of antennaId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the antennaId field, which is part of the key, after this row has been added to this table."
            )

        self._antennaId = Tag(antennaId)

    # ===> Attribute feedId

    _feedId = 0

    def getFeedId(self):
        """
        Get feedId.
        return feedId as int
        """

        return self._feedId

    def setFeedId(self, feedId):
        """
        Set feedId with the specified int value.
        feedId The int value to which feedId is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the feedId field, which is part of the key, after this row has been added to this table."
            )

        self._feedId = int(feedId)

    # ===> Attribute spectralWindowId

    _spectralWindowId = Tag()

    def getSpectralWindowId(self):
        """
        Get spectralWindowId.
        return spectralWindowId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._spectralWindowId)

    def setSpectralWindowId(self, spectralWindowId):
        """
        Set spectralWindowId with the specified Tag value.
        spectralWindowId The Tag value to which spectralWindowId is to be set.
        The value of spectralWindowId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the spectralWindowId field, which is part of the key, after this row has been added to this table."
            )

        self._spectralWindowId = Tag(spectralWindowId)

    # Links

    def getAntennaUsingAntennaId(self):
        """
        Returns the row in the Antenna table having Antenna.antennaId == antennaId

        """

        return self._table.getContainer().getAntenna().getRowByKey(self._antennaId)

    def getSpectralWindowUsingSpectralWindowId(self):
        """
        Returns the row in the SpectralWindow table having SpectralWindow.spectralWindowId == spectralWindowId

        """

        return (
            self._table.getContainer()
            .getSpectralWindow()
            .getRowByKey(self._spectralWindowId)
        )

    # ===> Slice link from a row of SysPower table to a collection of row of Feed table.
    def getFeeds(self):
        """
        Get the collection of rows in the Feed table having feedId == this.feedId
        """

        return self._table.getContainer().getFeed().getRowByFeedId(self._feedId)

    # comparison methods

    def compareNoAutoInc(
        self, antennaId, spectralWindowId, feedId, timeInterval, numReceptor
    ):
        """
        Compare each attribute except the autoincrementable one of this SysPowerRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaId is a Tag, compare using the equals method.
        if not self._antennaId.equals(antennaId):
            return False

        # spectralWindowId is a Tag, compare using the equals method.
        if not self._spectralWindowId.equals(spectralWindowId):
            return False

        # feedId is a int, compare using the == operator.
        if not (self._feedId == feedId):
            return False

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(otherRow.getNumReceptor())

    def compareRequiredValue(self, numReceptor):

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        return True


# initialize the dictionary that maps fields to init methods
SysPowerRow.initFromBinMethods()
