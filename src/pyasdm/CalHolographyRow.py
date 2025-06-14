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
# File CalHolographyRow.py
#

import pyasdm.CalHolographyTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.AntennaMake import AntennaMake


from pyasdm.enumerations.PolarizationType import PolarizationType


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from xml.dom import minidom

import copy


class CalHolographyRow:
    """
    The CalHolographyRow class is a row of a CalHolographyTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalHolographyRow.
        When row is None, create an empty row attached to table, which must be a CalHolographyTable.
        When row is given, copy those values in to the new row. The row argument must be a CalHolographyRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalHolographyTable):
            raise ValueError("table must be a CalHolographyTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._antennaName = None

        self._antennaMake = AntennaMake.from_int(0)

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._ambientTemperature = Temperature()

        self._focusPosition = []  # this is a list of Length []

        self._frequencyRange = []  # this is a list of Frequency []

        self._illuminationTaper = None

        self._numReceptor = 0

        self._polarizationTypes = []  # this is a list of PolarizationType []

        self._numPanelModes = 0

        self._receiverBand = ReceiverBand.from_int(0)

        self._beamMapUID = EntityRef()

        self._rawRMS = Length()

        self._weightedRMS = Length()

        self._surfaceMapUID = EntityRef()

        self._direction = []  # this is a list of Angle []

        self._numScrewExists = False

        self._numScrew = 0

        self._screwNameExists = False

        self._screwName = []  # this is a list of str []

        self._screwMotionExists = False

        self._screwMotion = []  # this is a list of Length []

        self._screwMotionErrorExists = False

        self._screwMotionError = []  # this is a list of Length []

        self._gravCorrectionExists = False

        self._gravCorrection = None

        self._gravOptRangeExists = False

        self._gravOptRange = []  # this is a list of Angle []

        self._tempCorrectionExists = False

        self._tempCorrection = None

        self._tempOptRangeExists = False

        self._tempOptRange = []  # this is a list of Temperature []

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalHolographyRow):
                raise ValueError("row must be a CalHolographyRow")

            # copy constructor

            self._antennaName = row._antennaName

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            # We force the attribute of the result to be not None
            if row._antennaMake is None:
                self._antennaMake = AntennaMake.from_int(0)
            else:
                self._antennaMake = AntennaMake(row._antennaMake)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            self._ambientTemperature = Temperature(row._ambientTemperature)

            # focusPosition is a  list , make a deep copy
            self._focusPosition = copy.deepcopy(row._focusPosition)

            # frequencyRange is a  list , make a deep copy
            self._frequencyRange = copy.deepcopy(row._frequencyRange)

            self._illuminationTaper = row._illuminationTaper

            self._numReceptor = row._numReceptor

            # polarizationTypes is a  list , make a deep copy
            self._polarizationTypes = copy.deepcopy(row._polarizationTypes)

            self._numPanelModes = row._numPanelModes

            # We force the attribute of the result to be not None
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            self._beamMapUID = EntityRef(row._beamMapUID)

            self._rawRMS = Length(row._rawRMS)

            self._weightedRMS = Length(row._weightedRMS)

            self._surfaceMapUID = EntityRef(row._surfaceMapUID)

            # direction is a  list , make a deep copy
            self._direction = copy.deepcopy(row._direction)

            # by default set systematically numScrew's value to something not None

            if row._numScrewExists:

                self._numScrew = row._numScrew

                self._numScrewExists = True

            # by default set systematically screwName's value to something not None

            if row._screwNameExists:

                # screwName is a list, make a deep copy
                self._screwName = copy.deepcopy(row._screwName)

                self._screwNameExists = True

            # by default set systematically screwMotion's value to something not None

            if row._screwMotionExists:

                # screwMotion is a list, make a deep copy
                self._screwMotion = copy.deepcopy(row._screwMotion)

                self._screwMotionExists = True

            # by default set systematically screwMotionError's value to something not None

            if row._screwMotionErrorExists:

                # screwMotionError is a list, make a deep copy
                self._screwMotionError = copy.deepcopy(row._screwMotionError)

                self._screwMotionErrorExists = True

            # by default set systematically gravCorrection's value to something not None

            if row._gravCorrectionExists:

                self._gravCorrection = row._gravCorrection

                self._gravCorrectionExists = True

            # by default set systematically gravOptRange's value to something not None

            if row._gravOptRangeExists:

                # gravOptRange is a list, make a deep copy
                self._gravOptRange = copy.deepcopy(row._gravOptRange)

                self._gravOptRangeExists = True

            # by default set systematically tempCorrection's value to something not None

            if row._tempCorrectionExists:

                self._tempCorrection = row._tempCorrection

                self._tempCorrectionExists = True

            # by default set systematically tempOptRange's value to something not None

            if row._tempOptRangeExists:

                # tempOptRange is a list, make a deep copy
                self._tempOptRange = copy.deepcopy(row._tempOptRange)

                self._tempOptRangeExists = True

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

        result += Parser.valueToXML("antennaName", self._antennaName)

        result += Parser.valueToXML("antennaMake", AntennaMake.name(self._antennaMake))

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.extendedValueToXML(
            "ambientTemperature", self._ambientTemperature
        )

        result += Parser.listExtendedValueToXML("focusPosition", self._focusPosition)

        result += Parser.listExtendedValueToXML("frequencyRange", self._frequencyRange)

        result += Parser.valueToXML("illuminationTaper", self._illuminationTaper)

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.valueToXML("numPanelModes", self._numPanelModes)

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.extendedValueToXML("beamMapUID", self._beamMapUID)

        result += Parser.extendedValueToXML("rawRMS", self._rawRMS)

        result += Parser.extendedValueToXML("weightedRMS", self._weightedRMS)

        result += Parser.extendedValueToXML("surfaceMapUID", self._surfaceMapUID)

        result += Parser.listExtendedValueToXML("direction", self._direction)

        if self._numScrewExists:

            result += Parser.valueToXML("numScrew", self._numScrew)

        if self._screwNameExists:

            result += Parser.listValueToXML("screwName", self._screwName)

        if self._screwMotionExists:

            result += Parser.listExtendedValueToXML("screwMotion", self._screwMotion)

        if self._screwMotionErrorExists:

            result += Parser.listExtendedValueToXML(
                "screwMotionError", self._screwMotionError
            )

        if self._gravCorrectionExists:

            result += Parser.valueToXML("gravCorrection", self._gravCorrection)

        if self._gravOptRangeExists:

            result += Parser.listExtendedValueToXML("gravOptRange", self._gravOptRange)

        if self._tempCorrectionExists:

            result += Parser.valueToXML("tempCorrection", self._tempCorrection)

        if self._tempOptRangeExists:

            result += Parser.listExtendedValueToXML("tempOptRange", self._tempOptRange)

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
                "xmlrow is not a string or a minidom.Element", "CalHolographyTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalHolographyTable")

        # intrinsic attribute values

        antennaNameNode = rowdom.getElementsByTagName("antennaName")[0]

        self._antennaName = str(antennaNameNode.firstChild.data.strip())

        antennaMakeNode = rowdom.getElementsByTagName("antennaMake")[0]

        self._antennaMake = AntennaMake.newAntennaMake(
            antennaMakeNode.firstChild.data.strip()
        )

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        ambientTemperatureNode = rowdom.getElementsByTagName("ambientTemperature")[0]

        self._ambientTemperature = Temperature(
            ambientTemperatureNode.firstChild.data.strip()
        )

        focusPositionNode = rowdom.getElementsByTagName("focusPosition")[0]

        focusPositionStr = focusPositionNode.firstChild.data.strip()

        self._focusPosition = Parser.stringListToLists(
            focusPositionStr, Length, "CalHolography", True
        )

        frequencyRangeNode = rowdom.getElementsByTagName("frequencyRange")[0]

        frequencyRangeStr = frequencyRangeNode.firstChild.data.strip()

        self._frequencyRange = Parser.stringListToLists(
            frequencyRangeStr, Frequency, "CalHolography", True
        )

        illuminationTaperNode = rowdom.getElementsByTagName("illuminationTaper")[0]

        self._illuminationTaper = float(illuminationTaperNode.firstChild.data.strip())

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data.strip()
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "CalHolography", False
        )

        numPanelModesNode = rowdom.getElementsByTagName("numPanelModes")[0]

        self._numPanelModes = int(numPanelModesNode.firstChild.data.strip())

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data.strip()
        )

        beamMapUIDNode = rowdom.getElementsByTagName("beamMapUID")[0]

        self._beamMapUID = EntityRef(beamMapUIDNode.toxml())

        rawRMSNode = rowdom.getElementsByTagName("rawRMS")[0]

        self._rawRMS = Length(rawRMSNode.firstChild.data.strip())

        weightedRMSNode = rowdom.getElementsByTagName("weightedRMS")[0]

        self._weightedRMS = Length(weightedRMSNode.firstChild.data.strip())

        surfaceMapUIDNode = rowdom.getElementsByTagName("surfaceMapUID")[0]

        self._surfaceMapUID = EntityRef(surfaceMapUIDNode.toxml())

        directionNode = rowdom.getElementsByTagName("direction")[0]

        directionStr = directionNode.firstChild.data.strip()

        self._direction = Parser.stringListToLists(
            directionStr, Angle, "CalHolography", True
        )

        numScrewNode = rowdom.getElementsByTagName("numScrew")
        if len(numScrewNode) > 0:

            self._numScrew = int(numScrewNode[0].firstChild.data.strip())

            self._numScrewExists = True

        screwNameNode = rowdom.getElementsByTagName("screwName")
        if len(screwNameNode) > 0:

            screwNameStr = screwNameNode[0].firstChild.data.strip()

            self._screwName = Parser.stringListToLists(
                screwNameStr, str, "CalHolography", False
            )

            self._screwNameExists = True

        screwMotionNode = rowdom.getElementsByTagName("screwMotion")
        if len(screwMotionNode) > 0:

            screwMotionStr = screwMotionNode[0].firstChild.data.strip()

            self._screwMotion = Parser.stringListToLists(
                screwMotionStr, Length, "CalHolography", True
            )

            self._screwMotionExists = True

        screwMotionErrorNode = rowdom.getElementsByTagName("screwMotionError")
        if len(screwMotionErrorNode) > 0:

            screwMotionErrorStr = screwMotionErrorNode[0].firstChild.data.strip()

            self._screwMotionError = Parser.stringListToLists(
                screwMotionErrorStr, Length, "CalHolography", True
            )

            self._screwMotionErrorExists = True

        gravCorrectionNode = rowdom.getElementsByTagName("gravCorrection")
        if len(gravCorrectionNode) > 0:

            self._gravCorrection = bool(gravCorrectionNode[0].firstChild.data.strip())

            self._gravCorrectionExists = True

        gravOptRangeNode = rowdom.getElementsByTagName("gravOptRange")
        if len(gravOptRangeNode) > 0:

            gravOptRangeStr = gravOptRangeNode[0].firstChild.data.strip()

            self._gravOptRange = Parser.stringListToLists(
                gravOptRangeStr, Angle, "CalHolography", True
            )

            self._gravOptRangeExists = True

        tempCorrectionNode = rowdom.getElementsByTagName("tempCorrection")
        if len(tempCorrectionNode) > 0:

            self._tempCorrection = bool(tempCorrectionNode[0].firstChild.data.strip())

            self._tempCorrectionExists = True

        tempOptRangeNode = rowdom.getElementsByTagName("tempOptRange")
        if len(tempOptRangeNode) > 0:

            tempOptRangeStr = tempOptRangeNode[0].firstChild.data.strip()

            self._tempOptRange = Parser.stringListToLists(
                tempOptRangeStr, Temperature, "CalHolography", True
            )

            self._tempOptRangeExists = True

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

        eos.writeStr(self._antennaName)

        self._calDataId.toBin(eos)

        self._calReductionId.toBin(eos)

        eos.writeString(str(self._antennaMake))

        self._startValidTime.toBin(eos)

        self._endValidTime.toBin(eos)

        self._ambientTemperature.toBin(eos)

        Length.listToBin(self._focusPosition, eos)

        Frequency.listToBin(self._frequencyRange, eos)

        eos.writeFloat(self._illuminationTaper)

        eos.writeInt(self._numReceptor)

        eos.writeInt(len(self._polarizationTypes))
        for i in range(len(self._polarizationTypes)):

            eos.writeString(str(self._polarizationTypes[i]))

        eos.writeInt(self._numPanelModes)

        eos.writeString(str(self._receiverBand))

        self._beamMapUID.toBin(eos)

        self._rawRMS.toBin(eos)

        self._weightedRMS.toBin(eos)

        self._surfaceMapUID.toBin(eos)

        Angle.listToBin(self._direction, eos)

        eos.writeBool(self._numScrewExists)
        if self._numScrewExists:

            eos.writeInt(self._numScrew)

        eos.writeBool(self._screwNameExists)
        if self._screwNameExists:

            eos.writeInt(len(self._screwName))
            for i in range(len(self._screwName)):

                eos.writeStr(self._screwName[i])

        eos.writeBool(self._screwMotionExists)
        if self._screwMotionExists:

            Length.listToBin(self._screwMotion, eos)

        eos.writeBool(self._screwMotionErrorExists)
        if self._screwMotionErrorExists:

            Length.listToBin(self._screwMotionError, eos)

        eos.writeBool(self._gravCorrectionExists)
        if self._gravCorrectionExists:

            eos.writeBool(self._gravCorrection)

        eos.writeBool(self._gravOptRangeExists)
        if self._gravOptRangeExists:

            Angle.listToBin(self._gravOptRange, eos)

        eos.writeBool(self._tempCorrectionExists)
        if self._tempCorrectionExists:

            eos.writeBool(self._tempCorrection)

        eos.writeBool(self._tempOptRangeExists)
        if self._tempOptRangeExists:

            Temperature.listToBin(self._tempOptRange, eos)

    @staticmethod
    def antennaNameFromBin(row, eis):
        """
        Set the antennaName in row from the EndianInput (eis) instance.
        """

        row._antennaName = eis.readStr()

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
    def antennaMakeFromBin(row, eis):
        """
        Set the antennaMake in row from the EndianInput (eis) instance.
        """

        row._antennaMake = AntennaMake.literal(eis.readString())

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
    def ambientTemperatureFromBin(row, eis):
        """
        Set the ambientTemperature in row from the EndianInput (eis) instance.
        """

        row._ambientTemperature = Temperature.fromBin(eis)

    @staticmethod
    def focusPositionFromBin(row, eis):
        """
        Set the focusPosition in row from the EndianInput (eis) instance.
        """

        row._focusPosition = Length.from1DBin(eis)

    @staticmethod
    def frequencyRangeFromBin(row, eis):
        """
        Set the frequencyRange in row from the EndianInput (eis) instance.
        """

        row._frequencyRange = Frequency.from1DBin(eis)

    @staticmethod
    def illuminationTaperFromBin(row, eis):
        """
        Set the illuminationTaper in row from the EndianInput (eis) instance.
        """

        row._illuminationTaper = eis.readFloat()

    @staticmethod
    def numReceptorFromBin(row, eis):
        """
        Set the numReceptor in row from the EndianInput (eis) instance.
        """

        row._numReceptor = eis.readInt()

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
    def numPanelModesFromBin(row, eis):
        """
        Set the numPanelModes in row from the EndianInput (eis) instance.
        """

        row._numPanelModes = eis.readInt()

    @staticmethod
    def receiverBandFromBin(row, eis):
        """
        Set the receiverBand in row from the EndianInput (eis) instance.
        """

        row._receiverBand = ReceiverBand.literal(eis.readString())

    @staticmethod
    def beamMapUIDFromBin(row, eis):
        """
        Set the beamMapUID in row from the EndianInput (eis) instance.
        """

        row._beamMapUID = EntityRef.fromBin(eis)

    @staticmethod
    def rawRMSFromBin(row, eis):
        """
        Set the rawRMS in row from the EndianInput (eis) instance.
        """

        row._rawRMS = Length.fromBin(eis)

    @staticmethod
    def weightedRMSFromBin(row, eis):
        """
        Set the weightedRMS in row from the EndianInput (eis) instance.
        """

        row._weightedRMS = Length.fromBin(eis)

    @staticmethod
    def surfaceMapUIDFromBin(row, eis):
        """
        Set the surfaceMapUID in row from the EndianInput (eis) instance.
        """

        row._surfaceMapUID = EntityRef.fromBin(eis)

    @staticmethod
    def directionFromBin(row, eis):
        """
        Set the direction in row from the EndianInput (eis) instance.
        """

        row._direction = Angle.from1DBin(eis)

    @staticmethod
    def numScrewFromBin(row, eis):
        """
        Set the optional numScrew in row from the EndianInput (eis) instance.
        """
        row._numScrewExists = eis.readBool()
        if row._numScrewExists:

            row._numScrew = eis.readInt()

    @staticmethod
    def screwNameFromBin(row, eis):
        """
        Set the optional screwName in row from the EndianInput (eis) instance.
        """
        row._screwNameExists = eis.readBool()
        if row._screwNameExists:

            screwNameDim1 = eis.readInt()
            thisList = []
            for i in range(screwNameDim1):
                thisValue = eis.readStr()
                thisList.append(thisValue)
            row._screwName = thisList

    @staticmethod
    def screwMotionFromBin(row, eis):
        """
        Set the optional screwMotion in row from the EndianInput (eis) instance.
        """
        row._screwMotionExists = eis.readBool()
        if row._screwMotionExists:

            row._screwMotion = Length.from1DBin(eis)

    @staticmethod
    def screwMotionErrorFromBin(row, eis):
        """
        Set the optional screwMotionError in row from the EndianInput (eis) instance.
        """
        row._screwMotionErrorExists = eis.readBool()
        if row._screwMotionErrorExists:

            row._screwMotionError = Length.from1DBin(eis)

    @staticmethod
    def gravCorrectionFromBin(row, eis):
        """
        Set the optional gravCorrection in row from the EndianInput (eis) instance.
        """
        row._gravCorrectionExists = eis.readBool()
        if row._gravCorrectionExists:

            row._gravCorrection = eis.readBool()

    @staticmethod
    def gravOptRangeFromBin(row, eis):
        """
        Set the optional gravOptRange in row from the EndianInput (eis) instance.
        """
        row._gravOptRangeExists = eis.readBool()
        if row._gravOptRangeExists:

            row._gravOptRange = Angle.from1DBin(eis)

    @staticmethod
    def tempCorrectionFromBin(row, eis):
        """
        Set the optional tempCorrection in row from the EndianInput (eis) instance.
        """
        row._tempCorrectionExists = eis.readBool()
        if row._tempCorrectionExists:

            row._tempCorrection = eis.readBool()

    @staticmethod
    def tempOptRangeFromBin(row, eis):
        """
        Set the optional tempOptRange in row from the EndianInput (eis) instance.
        """
        row._tempOptRangeExists = eis.readBool()
        if row._tempOptRangeExists:

            row._tempOptRange = Temperature.from1DBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaName"] = CalHolographyRow.antennaNameFromBin
        _fromBinMethods["calDataId"] = CalHolographyRow.calDataIdFromBin
        _fromBinMethods["calReductionId"] = CalHolographyRow.calReductionIdFromBin
        _fromBinMethods["antennaMake"] = CalHolographyRow.antennaMakeFromBin
        _fromBinMethods["startValidTime"] = CalHolographyRow.startValidTimeFromBin
        _fromBinMethods["endValidTime"] = CalHolographyRow.endValidTimeFromBin
        _fromBinMethods["ambientTemperature"] = (
            CalHolographyRow.ambientTemperatureFromBin
        )
        _fromBinMethods["focusPosition"] = CalHolographyRow.focusPositionFromBin
        _fromBinMethods["frequencyRange"] = CalHolographyRow.frequencyRangeFromBin
        _fromBinMethods["illuminationTaper"] = CalHolographyRow.illuminationTaperFromBin
        _fromBinMethods["numReceptor"] = CalHolographyRow.numReceptorFromBin
        _fromBinMethods["polarizationTypes"] = CalHolographyRow.polarizationTypesFromBin
        _fromBinMethods["numPanelModes"] = CalHolographyRow.numPanelModesFromBin
        _fromBinMethods["receiverBand"] = CalHolographyRow.receiverBandFromBin
        _fromBinMethods["beamMapUID"] = CalHolographyRow.beamMapUIDFromBin
        _fromBinMethods["rawRMS"] = CalHolographyRow.rawRMSFromBin
        _fromBinMethods["weightedRMS"] = CalHolographyRow.weightedRMSFromBin
        _fromBinMethods["surfaceMapUID"] = CalHolographyRow.surfaceMapUIDFromBin
        _fromBinMethods["direction"] = CalHolographyRow.directionFromBin

        _fromBinMethods["numScrew"] = CalHolographyRow.numScrewFromBin
        _fromBinMethods["screwName"] = CalHolographyRow.screwNameFromBin
        _fromBinMethods["screwMotion"] = CalHolographyRow.screwMotionFromBin
        _fromBinMethods["screwMotionError"] = CalHolographyRow.screwMotionErrorFromBin
        _fromBinMethods["gravCorrection"] = CalHolographyRow.gravCorrectionFromBin
        _fromBinMethods["gravOptRange"] = CalHolographyRow.gravOptRangeFromBin
        _fromBinMethods["tempCorrection"] = CalHolographyRow.tempCorrectionFromBin
        _fromBinMethods["tempOptRange"] = CalHolographyRow.tempOptRangeFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CalHolographyRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalHolography",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute antennaName

    _antennaName = None

    def getAntennaName(self):
        """
        Get antennaName.
        return antennaName as str
        """

        return self._antennaName

    def setAntennaName(self, antennaName):
        """
        Set antennaName with the specified str value.
        antennaName The str value to which antennaName is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the antennaName field, which is part of the key, after this row has been added to this table."
            )

        self._antennaName = str(antennaName)

    # ===> Attribute antennaMake

    _antennaMake = AntennaMake.from_int(0)

    def getAntennaMake(self):
        """
        Get antennaMake.
        return antennaMake as AntennaMake
        """

        return self._antennaMake

    def setAntennaMake(self, antennaMake):
        """
        Set antennaMake with the specified AntennaMake value.
        antennaMake The AntennaMake value to which antennaMake is to be set.


        """

        self._antennaMake = AntennaMake(antennaMake)

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

    # ===> Attribute ambientTemperature

    _ambientTemperature = Temperature()

    def getAmbientTemperature(self):
        """
        Get ambientTemperature.
        return ambientTemperature as Temperature
        """

        # make sure it is a copy of Temperature
        return Temperature(self._ambientTemperature)

    def setAmbientTemperature(self, ambientTemperature):
        """
        Set ambientTemperature with the specified Temperature value.
        ambientTemperature The Temperature value to which ambientTemperature is to be set.
        The value of ambientTemperature can be anything allowed by the Temperature constructor.

        """

        self._ambientTemperature = Temperature(ambientTemperature)

    # ===> Attribute focusPosition

    _focusPosition = None  # this is a 1D list of Length

    def getFocusPosition(self):
        """
        Get focusPosition.
        return focusPosition as Length []
        """

        return copy.deepcopy(self._focusPosition)

    def setFocusPosition(self, focusPosition):
        """
        Set focusPosition with the specified Length []  value.
        focusPosition The Length []  value to which focusPosition is to be set.
        The value of focusPosition can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(focusPosition, list):
            raise ValueError("The value of focusPosition must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(focusPosition)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of focusPosition is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(focusPosition, Length):
                raise ValueError(
                    "type of the first value in focusPosition is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._focusPosition = copy.deepcopy(focusPosition)
        except Exception as exc:
            raise ValueError("Invalid focusPosition : " + str(exc))

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

    # ===> Attribute illuminationTaper

    _illuminationTaper = None

    def getIlluminationTaper(self):
        """
        Get illuminationTaper.
        return illuminationTaper as float
        """

        return self._illuminationTaper

    def setIlluminationTaper(self, illuminationTaper):
        """
        Set illuminationTaper with the specified float value.
        illuminationTaper The float value to which illuminationTaper is to be set.


        """

        self._illuminationTaper = float(illuminationTaper)

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

    # ===> Attribute numPanelModes

    _numPanelModes = 0

    def getNumPanelModes(self):
        """
        Get numPanelModes.
        return numPanelModes as int
        """

        return self._numPanelModes

    def setNumPanelModes(self, numPanelModes):
        """
        Set numPanelModes with the specified int value.
        numPanelModes The int value to which numPanelModes is to be set.


        """

        self._numPanelModes = int(numPanelModes)

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


        """

        self._receiverBand = ReceiverBand(receiverBand)

    # ===> Attribute beamMapUID

    _beamMapUID = EntityRef()

    def getBeamMapUID(self):
        """
        Get beamMapUID.
        return beamMapUID as EntityRef
        """

        # make sure it is a copy of EntityRef
        return EntityRef(self._beamMapUID)

    def setBeamMapUID(self, beamMapUID):
        """
        Set beamMapUID with the specified EntityRef value.
        beamMapUID The EntityRef value to which beamMapUID is to be set.
        The value of beamMapUID can be anything allowed by the EntityRef constructor.

        """

        self._beamMapUID = EntityRef(beamMapUID)

    # ===> Attribute rawRMS

    _rawRMS = Length()

    def getRawRMS(self):
        """
        Get rawRMS.
        return rawRMS as Length
        """

        # make sure it is a copy of Length
        return Length(self._rawRMS)

    def setRawRMS(self, rawRMS):
        """
        Set rawRMS with the specified Length value.
        rawRMS The Length value to which rawRMS is to be set.
        The value of rawRMS can be anything allowed by the Length constructor.

        """

        self._rawRMS = Length(rawRMS)

    # ===> Attribute weightedRMS

    _weightedRMS = Length()

    def getWeightedRMS(self):
        """
        Get weightedRMS.
        return weightedRMS as Length
        """

        # make sure it is a copy of Length
        return Length(self._weightedRMS)

    def setWeightedRMS(self, weightedRMS):
        """
        Set weightedRMS with the specified Length value.
        weightedRMS The Length value to which weightedRMS is to be set.
        The value of weightedRMS can be anything allowed by the Length constructor.

        """

        self._weightedRMS = Length(weightedRMS)

    # ===> Attribute surfaceMapUID

    _surfaceMapUID = EntityRef()

    def getSurfaceMapUID(self):
        """
        Get surfaceMapUID.
        return surfaceMapUID as EntityRef
        """

        # make sure it is a copy of EntityRef
        return EntityRef(self._surfaceMapUID)

    def setSurfaceMapUID(self, surfaceMapUID):
        """
        Set surfaceMapUID with the specified EntityRef value.
        surfaceMapUID The EntityRef value to which surfaceMapUID is to be set.
        The value of surfaceMapUID can be anything allowed by the EntityRef constructor.

        """

        self._surfaceMapUID = EntityRef(surfaceMapUID)

    # ===> Attribute direction

    _direction = None  # this is a 1D list of Angle

    def getDirection(self):
        """
        Get direction.
        return direction as Angle []
        """

        return copy.deepcopy(self._direction)

    def setDirection(self, direction):
        """
        Set direction with the specified Angle []  value.
        direction The Angle []  value to which direction is to be set.
        The value of direction can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(direction, list):
            raise ValueError("The value of direction must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(direction)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of direction is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(direction, Angle):
                raise ValueError(
                    "type of the first value in direction is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._direction = copy.deepcopy(direction)
        except Exception as exc:
            raise ValueError("Invalid direction : " + str(exc))

    # ===> Attribute numScrew, which is optional
    _numScrewExists = False

    _numScrew = 0

    def isNumScrewExists(self):
        """
        The attribute numScrew is optional. Return True if this attribute exists.
        return True if and only if the numScrew attribute exists.
        """
        return self._numScrewExists

    def getNumScrew(self):
        """
        Get numScrew, which is optional.
        return numScrew as int
        raises ValueError If numScrew does not exist.
        """
        if not self._numScrewExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numScrew
                + " attribute in table CalHolography does not exist!"
            )

        return self._numScrew

    def setNumScrew(self, numScrew):
        """
        Set numScrew with the specified int value.
        numScrew The int value to which numScrew is to be set.


        """

        self._numScrew = int(numScrew)

        self._numScrewExists = True

    def clearNumScrew(self):
        """
        Mark numScrew, which is an optional field, as non-existent.
        """
        self._numScrewExists = False

    # ===> Attribute screwName, which is optional
    _screwNameExists = False

    _screwName = None  # this is a 1D list of str

    def isScrewNameExists(self):
        """
        The attribute screwName is optional. Return True if this attribute exists.
        return True if and only if the screwName attribute exists.
        """
        return self._screwNameExists

    def getScrewName(self):
        """
        Get screwName, which is optional.
        return screwName as str []
        raises ValueError If screwName does not exist.
        """
        if not self._screwNameExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + screwName
                + " attribute in table CalHolography does not exist!"
            )

        return copy.deepcopy(self._screwName)

    def setScrewName(self, screwName):
        """
        Set screwName with the specified str []  value.
        screwName The str []  value to which screwName is to be set.


        """

        # value must be a list
        if not isinstance(screwName, list):
            raise ValueError("The value of screwName must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(screwName)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of screwName is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(screwName, str):
                raise ValueError(
                    "type of the first value in screwName is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._screwName = copy.deepcopy(screwName)
        except Exception as exc:
            raise ValueError("Invalid screwName : " + str(exc))

        self._screwNameExists = True

    def clearScrewName(self):
        """
        Mark screwName, which is an optional field, as non-existent.
        """
        self._screwNameExists = False

    # ===> Attribute screwMotion, which is optional
    _screwMotionExists = False

    _screwMotion = None  # this is a 1D list of Length

    def isScrewMotionExists(self):
        """
        The attribute screwMotion is optional. Return True if this attribute exists.
        return True if and only if the screwMotion attribute exists.
        """
        return self._screwMotionExists

    def getScrewMotion(self):
        """
        Get screwMotion, which is optional.
        return screwMotion as Length []
        raises ValueError If screwMotion does not exist.
        """
        if not self._screwMotionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + screwMotion
                + " attribute in table CalHolography does not exist!"
            )

        return copy.deepcopy(self._screwMotion)

    def setScrewMotion(self, screwMotion):
        """
        Set screwMotion with the specified Length []  value.
        screwMotion The Length []  value to which screwMotion is to be set.
        The value of screwMotion can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(screwMotion, list):
            raise ValueError("The value of screwMotion must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(screwMotion)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of screwMotion is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(screwMotion, Length):
                raise ValueError(
                    "type of the first value in screwMotion is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._screwMotion = copy.deepcopy(screwMotion)
        except Exception as exc:
            raise ValueError("Invalid screwMotion : " + str(exc))

        self._screwMotionExists = True

    def clearScrewMotion(self):
        """
        Mark screwMotion, which is an optional field, as non-existent.
        """
        self._screwMotionExists = False

    # ===> Attribute screwMotionError, which is optional
    _screwMotionErrorExists = False

    _screwMotionError = None  # this is a 1D list of Length

    def isScrewMotionErrorExists(self):
        """
        The attribute screwMotionError is optional. Return True if this attribute exists.
        return True if and only if the screwMotionError attribute exists.
        """
        return self._screwMotionErrorExists

    def getScrewMotionError(self):
        """
        Get screwMotionError, which is optional.
        return screwMotionError as Length []
        raises ValueError If screwMotionError does not exist.
        """
        if not self._screwMotionErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + screwMotionError
                + " attribute in table CalHolography does not exist!"
            )

        return copy.deepcopy(self._screwMotionError)

    def setScrewMotionError(self, screwMotionError):
        """
        Set screwMotionError with the specified Length []  value.
        screwMotionError The Length []  value to which screwMotionError is to be set.
        The value of screwMotionError can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(screwMotionError, list):
            raise ValueError("The value of screwMotionError must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(screwMotionError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of screwMotionError is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(screwMotionError, Length):
                raise ValueError(
                    "type of the first value in screwMotionError is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._screwMotionError = copy.deepcopy(screwMotionError)
        except Exception as exc:
            raise ValueError("Invalid screwMotionError : " + str(exc))

        self._screwMotionErrorExists = True

    def clearScrewMotionError(self):
        """
        Mark screwMotionError, which is an optional field, as non-existent.
        """
        self._screwMotionErrorExists = False

    # ===> Attribute gravCorrection, which is optional
    _gravCorrectionExists = False

    _gravCorrection = None

    def isGravCorrectionExists(self):
        """
        The attribute gravCorrection is optional. Return True if this attribute exists.
        return True if and only if the gravCorrection attribute exists.
        """
        return self._gravCorrectionExists

    def getGravCorrection(self):
        """
        Get gravCorrection, which is optional.
        return gravCorrection as bool
        raises ValueError If gravCorrection does not exist.
        """
        if not self._gravCorrectionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + gravCorrection
                + " attribute in table CalHolography does not exist!"
            )

        return self._gravCorrection

    def setGravCorrection(self, gravCorrection):
        """
        Set gravCorrection with the specified bool value.
        gravCorrection The bool value to which gravCorrection is to be set.


        """

        self._gravCorrection = bool(gravCorrection)

        self._gravCorrectionExists = True

    def clearGravCorrection(self):
        """
        Mark gravCorrection, which is an optional field, as non-existent.
        """
        self._gravCorrectionExists = False

    # ===> Attribute gravOptRange, which is optional
    _gravOptRangeExists = False

    _gravOptRange = None  # this is a 1D list of Angle

    def isGravOptRangeExists(self):
        """
        The attribute gravOptRange is optional. Return True if this attribute exists.
        return True if and only if the gravOptRange attribute exists.
        """
        return self._gravOptRangeExists

    def getGravOptRange(self):
        """
        Get gravOptRange, which is optional.
        return gravOptRange as Angle []
        raises ValueError If gravOptRange does not exist.
        """
        if not self._gravOptRangeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + gravOptRange
                + " attribute in table CalHolography does not exist!"
            )

        return copy.deepcopy(self._gravOptRange)

    def setGravOptRange(self, gravOptRange):
        """
        Set gravOptRange with the specified Angle []  value.
        gravOptRange The Angle []  value to which gravOptRange is to be set.
        The value of gravOptRange can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(gravOptRange, list):
            raise ValueError("The value of gravOptRange must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(gravOptRange)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of gravOptRange is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(gravOptRange, Angle):
                raise ValueError(
                    "type of the first value in gravOptRange is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._gravOptRange = copy.deepcopy(gravOptRange)
        except Exception as exc:
            raise ValueError("Invalid gravOptRange : " + str(exc))

        self._gravOptRangeExists = True

    def clearGravOptRange(self):
        """
        Mark gravOptRange, which is an optional field, as non-existent.
        """
        self._gravOptRangeExists = False

    # ===> Attribute tempCorrection, which is optional
    _tempCorrectionExists = False

    _tempCorrection = None

    def isTempCorrectionExists(self):
        """
        The attribute tempCorrection is optional. Return True if this attribute exists.
        return True if and only if the tempCorrection attribute exists.
        """
        return self._tempCorrectionExists

    def getTempCorrection(self):
        """
        Get tempCorrection, which is optional.
        return tempCorrection as bool
        raises ValueError If tempCorrection does not exist.
        """
        if not self._tempCorrectionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tempCorrection
                + " attribute in table CalHolography does not exist!"
            )

        return self._tempCorrection

    def setTempCorrection(self, tempCorrection):
        """
        Set tempCorrection with the specified bool value.
        tempCorrection The bool value to which tempCorrection is to be set.


        """

        self._tempCorrection = bool(tempCorrection)

        self._tempCorrectionExists = True

    def clearTempCorrection(self):
        """
        Mark tempCorrection, which is an optional field, as non-existent.
        """
        self._tempCorrectionExists = False

    # ===> Attribute tempOptRange, which is optional
    _tempOptRangeExists = False

    _tempOptRange = None  # this is a 1D list of Temperature

    def isTempOptRangeExists(self):
        """
        The attribute tempOptRange is optional. Return True if this attribute exists.
        return True if and only if the tempOptRange attribute exists.
        """
        return self._tempOptRangeExists

    def getTempOptRange(self):
        """
        Get tempOptRange, which is optional.
        return tempOptRange as Temperature []
        raises ValueError If tempOptRange does not exist.
        """
        if not self._tempOptRangeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tempOptRange
                + " attribute in table CalHolography does not exist!"
            )

        return copy.deepcopy(self._tempOptRange)

    def setTempOptRange(self, tempOptRange):
        """
        Set tempOptRange with the specified Temperature []  value.
        tempOptRange The Temperature []  value to which tempOptRange is to be set.
        The value of tempOptRange can be anything allowed by the Temperature []  constructor.

        """

        # value must be a list
        if not isinstance(tempOptRange, list):
            raise ValueError("The value of tempOptRange must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(tempOptRange)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of tempOptRange is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(tempOptRange, Temperature):
                raise ValueError(
                    "type of the first value in tempOptRange is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tempOptRange = copy.deepcopy(tempOptRange)
        except Exception as exc:
            raise ValueError("Invalid tempOptRange : " + str(exc))

        self._tempOptRangeExists = True

    def clearTempOptRange(self):
        """
        Mark tempOptRange, which is an optional field, as non-existent.
        """
        self._tempOptRangeExists = False

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
        antennaName,
        calDataId,
        calReductionId,
        antennaMake,
        startValidTime,
        endValidTime,
        ambientTemperature,
        focusPosition,
        frequencyRange,
        illuminationTaper,
        numReceptor,
        polarizationTypes,
        numPanelModes,
        receiverBand,
        beamMapUID,
        rawRMS,
        weightedRMS,
        surfaceMapUID,
        direction,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalHolographyRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaName is a str, compare using the == operator.
        if not (self._antennaName == antennaName):
            return False

        # calDataId is a Tag, compare using the equals method.
        if not self._calDataId.equals(calDataId):
            return False

        # calReductionId is a Tag, compare using the equals method.
        if not self._calReductionId.equals(calReductionId):
            return False

        # antennaMake is a AntennaMake, compare using the == operator on the getValue() output
        if not (self._antennaMake.getValue() == antennaMake.getValue()):
            return False

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # ambientTemperature is a Temperature, compare using the almostEquals method.
        if not self._ambientTemperature.almostEquals(
            ambientTemperature, self.getTable().getAmbientTemperatureEqTolerance()
        ):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._focusPosition) != len(focusPosition):
            return False
        for indx in range(len(focusPosition)):

            # focusPosition is a list of Length, compare using the almostEquals method.
            if not self._focusPosition[indx].almostEquals(
                focusPosition[indx], self.getTable().getFocusPositionEqTolerance()
            ):
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

        # illuminationTaper is a float, compare using the == operator.
        if not (self._illuminationTaper == illuminationTaper):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationTypes) != len(polarizationTypes):
            return False
        for indx in range(len(polarizationTypes)):

            # polarizationTypes is a list of PolarizationType, compare using == operator.
            if not (self._polarizationTypes[indx] == polarizationTypes[indx]):
                return False

        # numPanelModes is a int, compare using the == operator.
        if not (self._numPanelModes == numPanelModes):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
            return False

        # beamMapUID is a EntityRef, compare using the equals method.
        if not self._beamMapUID.equals(beamMapUID):
            return False

        # rawRMS is a Length, compare using the almostEquals method.
        if not self._rawRMS.almostEquals(
            rawRMS, self.getTable().getRawRMSEqTolerance()
        ):
            return False

        # weightedRMS is a Length, compare using the almostEquals method.
        if not self._weightedRMS.almostEquals(
            weightedRMS, self.getTable().getWeightedRMSEqTolerance()
        ):
            return False

        # surfaceMapUID is a EntityRef, compare using the equals method.
        if not self._surfaceMapUID.equals(surfaceMapUID):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._direction) != len(direction):
            return False
        for indx in range(len(direction)):

            # direction is a list of Angle, compare using the almostEquals method.
            if not self._direction[indx].almostEquals(
                direction[indx], self.getTable().getDirectionEqTolerance()
            ):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getAntennaMake(),
            otherRow.getStartValidTime(),
            otherRow.getEndValidTime(),
            otherRow.getAmbientTemperature(),
            otherRow.getFocusPosition(),
            otherRow.getFrequencyRange(),
            otherRow.getIlluminationTaper(),
            otherRow.getNumReceptor(),
            otherRow.getPolarizationTypes(),
            otherRow.getNumPanelModes(),
            otherRow.getReceiverBand(),
            otherRow.getBeamMapUID(),
            otherRow.getRawRMS(),
            otherRow.getWeightedRMS(),
            otherRow.getSurfaceMapUID(),
            otherRow.getDirection(),
        )

    def compareRequiredValue(
        self,
        antennaMake,
        startValidTime,
        endValidTime,
        ambientTemperature,
        focusPosition,
        frequencyRange,
        illuminationTaper,
        numReceptor,
        polarizationTypes,
        numPanelModes,
        receiverBand,
        beamMapUID,
        rawRMS,
        weightedRMS,
        surfaceMapUID,
        direction,
    ):

        # antennaMake is a AntennaMake, compare using the == operator on the getValue() output
        if not (self._antennaMake.getValue() == antennaMake.getValue()):
            return False

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # ambientTemperature is a Temperature, compare using the almostEquals method.
        if not self._ambientTemperature.almostEquals(
            ambientTemperature, self.getTable().getAmbientTemperatureEqTolerance()
        ):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._focusPosition) != len(focusPosition):
            return False
        for indx in range(len(focusPosition)):

            # focusPosition is a list of Length, compare using the almostEquals method.
            if not self._focusPosition[indx].almostEquals(
                focusPosition[indx], self.getTable().getFocusPositionEqTolerance()
            ):
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

        # illuminationTaper is a float, compare using the == operator.
        if not (self._illuminationTaper == illuminationTaper):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationTypes) != len(polarizationTypes):
            return False
        for indx in range(len(polarizationTypes)):

            # polarizationTypes is a list of PolarizationType, compare using == operator.
            if not (self._polarizationTypes[indx] == polarizationTypes[indx]):
                return False

        # numPanelModes is a int, compare using the == operator.
        if not (self._numPanelModes == numPanelModes):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
            return False

        # beamMapUID is a EntityRef, compare using the equals method.
        if not self._beamMapUID.equals(beamMapUID):
            return False

        # rawRMS is a Length, compare using the almostEquals method.
        if not self._rawRMS.almostEquals(
            rawRMS, self.getTable().getRawRMSEqTolerance()
        ):
            return False

        # weightedRMS is a Length, compare using the almostEquals method.
        if not self._weightedRMS.almostEquals(
            weightedRMS, self.getTable().getWeightedRMSEqTolerance()
        ):
            return False

        # surfaceMapUID is a EntityRef, compare using the equals method.
        if not self._surfaceMapUID.equals(surfaceMapUID):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._direction) != len(direction):
            return False
        for indx in range(len(direction)):

            # direction is a list of Angle, compare using the almostEquals method.
            if not self._direction[indx].almostEquals(
                direction[indx], self.getTable().getDirectionEqTolerance()
            ):
                return False

        return True


# initialize the dictionary that maps fields to init methods
CalHolographyRow.initFromBinMethods()
