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
# File CalPrimaryBeamRow.py
#

import pyasdm.CalPrimaryBeamTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.AntennaMake import AntennaMake


from pyasdm.enumerations.PolarizationType import PolarizationType


from pyasdm.enumerations.PrimaryBeamDescription import PrimaryBeamDescription


from xml.dom import minidom

import copy


class CalPrimaryBeamRow:
    """
    The CalPrimaryBeamRow class is a row of a CalPrimaryBeamTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalPrimaryBeamRow.
        When row is None, create an empty row attached to table, which must be a CalPrimaryBeamTable.
        When row is given, copy those values in to the new row. The row argument must be a CalPrimaryBeamRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalPrimaryBeamTable):
            raise ValueError("table must be a CalPrimaryBeamTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._antennaName = None

        self._receiverBand = ReceiverBand.from_int(0)

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._antennaMake = AntennaMake.from_int(0)

        self._numSubband = 0

        self._frequencyRange = []  # this is a list of Frequency []  []

        self._numReceptor = 0

        self._polarizationTypes = []  # this is a list of PolarizationType []

        self._mainBeamEfficiency = []  # this is a list of float []

        self._beamDescriptionUID = EntityRef()

        self._relativeAmplitudeRms = None

        self._direction = []  # this is a list of Angle []

        self._minValidDirection = []  # this is a list of Angle []

        self._maxValidDirection = []  # this is a list of Angle []

        self._descriptionType = PrimaryBeamDescription.from_int(0)

        self._imageChannelNumber = []  # this is a list of int []

        self._imageNominalFrequency = []  # this is a list of Frequency []

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalPrimaryBeamRow):
                raise ValueError("row must be a CalPrimaryBeamRow")

            # copy constructor

            self._antennaName = row._antennaName

            # We force the attribute of the result to be not None.
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            # We force the attribute of the result to be not None
            if row._antennaMake is None:
                self._antennaMake = AntennaMake.from_int(0)
            else:
                self._antennaMake = AntennaMake(row._antennaMake)

            self._numSubband = row._numSubband

            # frequencyRange is a  list , make a deep copy
            self._frequencyRange = copy.deepcopy(row._frequencyRange)

            self._numReceptor = row._numReceptor

            # polarizationTypes is a  list , make a deep copy
            self._polarizationTypes = copy.deepcopy(row._polarizationTypes)

            # mainBeamEfficiency is a  list , make a deep copy
            self._mainBeamEfficiency = copy.deepcopy(row._mainBeamEfficiency)

            self._beamDescriptionUID = EntityRef(row._beamDescriptionUID)

            self._relativeAmplitudeRms = row._relativeAmplitudeRms

            # direction is a  list , make a deep copy
            self._direction = copy.deepcopy(row._direction)

            # minValidDirection is a  list , make a deep copy
            self._minValidDirection = copy.deepcopy(row._minValidDirection)

            # maxValidDirection is a  list , make a deep copy
            self._maxValidDirection = copy.deepcopy(row._maxValidDirection)

            # We force the attribute of the result to be not None
            if row._descriptionType is None:
                self._descriptionType = PrimaryBeamDescription.from_int(0)
            else:
                self._descriptionType = PrimaryBeamDescription(row._descriptionType)

            # imageChannelNumber is a  list , make a deep copy
            self._imageChannelNumber = copy.deepcopy(row._imageChannelNumber)

            # imageNominalFrequency is a  list , make a deep copy
            self._imageNominalFrequency = copy.deepcopy(row._imageNominalFrequency)

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

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.valueToXML("antennaMake", AntennaMake.name(self._antennaMake))

        result += Parser.valueToXML("numSubband", self._numSubband)

        result += Parser.listExtendedValueToXML("frequencyRange", self._frequencyRange)

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.listValueToXML("mainBeamEfficiency", self._mainBeamEfficiency)

        result += Parser.extendedValueToXML(
            "beamDescriptionUID", self._beamDescriptionUID
        )

        result += Parser.valueToXML("relativeAmplitudeRms", self._relativeAmplitudeRms)

        result += Parser.listExtendedValueToXML("direction", self._direction)

        result += Parser.listExtendedValueToXML(
            "minValidDirection", self._minValidDirection
        )

        result += Parser.listExtendedValueToXML(
            "maxValidDirection", self._maxValidDirection
        )

        result += Parser.valueToXML(
            "descriptionType", PrimaryBeamDescription.name(self._descriptionType)
        )

        result += Parser.listValueToXML("imageChannelNumber", self._imageChannelNumber)

        result += Parser.listExtendedValueToXML(
            "imageNominalFrequency", self._imageNominalFrequency
        )

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
                "xmlrow is not a string or a minidom.Element", "CalPrimaryBeamTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException(
                "the argument is not a row", "CalPrimaryBeamTable"
            )

        # intrinsic attribute values

        antennaNameNode = rowdom.getElementsByTagName("antennaName")[0]

        self._antennaName = str(antennaNameNode.firstChild.data.strip())

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data.strip()
        )

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        antennaMakeNode = rowdom.getElementsByTagName("antennaMake")[0]

        self._antennaMake = AntennaMake.newAntennaMake(
            antennaMakeNode.firstChild.data.strip()
        )

        numSubbandNode = rowdom.getElementsByTagName("numSubband")[0]

        self._numSubband = int(numSubbandNode.firstChild.data.strip())

        frequencyRangeNode = rowdom.getElementsByTagName("frequencyRange")[0]

        frequencyRangeStr = frequencyRangeNode.firstChild.data.strip()

        self._frequencyRange = Parser.stringListToLists(
            frequencyRangeStr, Frequency, "CalPrimaryBeam", True
        )

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data.strip()
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "CalPrimaryBeam", False
        )

        mainBeamEfficiencyNode = rowdom.getElementsByTagName("mainBeamEfficiency")[0]

        mainBeamEfficiencyStr = mainBeamEfficiencyNode.firstChild.data.strip()

        self._mainBeamEfficiency = Parser.stringListToLists(
            mainBeamEfficiencyStr, float, "CalPrimaryBeam", False
        )

        beamDescriptionUIDNode = rowdom.getElementsByTagName("beamDescriptionUID")[0]

        self._beamDescriptionUID = EntityRef(beamDescriptionUIDNode.toxml())

        relativeAmplitudeRmsNode = rowdom.getElementsByTagName("relativeAmplitudeRms")[
            0
        ]

        self._relativeAmplitudeRms = float(
            relativeAmplitudeRmsNode.firstChild.data.strip()
        )

        directionNode = rowdom.getElementsByTagName("direction")[0]

        directionStr = directionNode.firstChild.data.strip()

        self._direction = Parser.stringListToLists(
            directionStr, Angle, "CalPrimaryBeam", True
        )

        minValidDirectionNode = rowdom.getElementsByTagName("minValidDirection")[0]

        minValidDirectionStr = minValidDirectionNode.firstChild.data.strip()

        self._minValidDirection = Parser.stringListToLists(
            minValidDirectionStr, Angle, "CalPrimaryBeam", True
        )

        maxValidDirectionNode = rowdom.getElementsByTagName("maxValidDirection")[0]

        maxValidDirectionStr = maxValidDirectionNode.firstChild.data.strip()

        self._maxValidDirection = Parser.stringListToLists(
            maxValidDirectionStr, Angle, "CalPrimaryBeam", True
        )

        descriptionTypeNode = rowdom.getElementsByTagName("descriptionType")[0]

        self._descriptionType = PrimaryBeamDescription.newPrimaryBeamDescription(
            descriptionTypeNode.firstChild.data.strip()
        )

        imageChannelNumberNode = rowdom.getElementsByTagName("imageChannelNumber")[0]

        imageChannelNumberStr = imageChannelNumberNode.firstChild.data.strip()

        self._imageChannelNumber = Parser.stringListToLists(
            imageChannelNumberStr, int, "CalPrimaryBeam", False
        )

        imageNominalFrequencyNode = rowdom.getElementsByTagName(
            "imageNominalFrequency"
        )[0]

        imageNominalFrequencyStr = imageNominalFrequencyNode.firstChild.data.strip()

        self._imageNominalFrequency = Parser.stringListToLists(
            imageNominalFrequencyStr, Frequency, "CalPrimaryBeam", True
        )

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

        eos.writeString(self._receiverBand.toString())

        self._calDataId.toBin(eos)

        self._calReductionId.toBin(eos)

        self._startValidTime.toBin(eos)

        self._endValidTime.toBin(eos)

        eos.writeString(self._antennaMake.toString())

        eos.writeInt(self._numSubband)

        Frequency.listToBin(self._frequencyRange, eos)

        eos.writeInt(self._numReceptor)

        eos.writeInt(len(self._polarizationTypes))
        for i in range(len(self._polarizationTypes)):

            eos.writeString(self._polarizationTypes[i].toString())

        eos.writeInt(len(self._mainBeamEfficiency))
        for i in range(len(self._mainBeamEfficiency)):

            eos.writeFloat(self._mainBeamEfficiency[i])

        self._beamDescriptionUID.toBin(eos)

        eos.writeFloat(self._relativeAmplitudeRms)

        Angle.listToBin(self._direction, eos)

        Angle.listToBin(self._minValidDirection, eos)

        Angle.listToBin(self._maxValidDirection, eos)

        eos.writeString(self._descriptionType.toString())

        eos.writeInt(len(self._imageChannelNumber))
        for i in range(len(self._imageChannelNumber)):

            eos.writeInt(self._imageChannelNumber[i])

        Frequency.listToBin(self._imageNominalFrequency, eos)

    @staticmethod
    def antennaNameFromBin(row, eis):
        """
        Set the antennaName in row from the EndianInput (eis) instance.
        """

        row._antennaName = eis.readStr()

    @staticmethod
    def receiverBandFromBin(row, eis):
        """
        Set the receiverBand in row from the EndianInput (eis) instance.
        """

        row._receiverBand = ReceiverBand.from_int(eis.readInt())

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
    def antennaMakeFromBin(row, eis):
        """
        Set the antennaMake in row from the EndianInput (eis) instance.
        """

        row._antennaMake = AntennaMake.from_int(eis.readInt())

    @staticmethod
    def numSubbandFromBin(row, eis):
        """
        Set the numSubband in row from the EndianInput (eis) instance.
        """

        row._numSubband = eis.readInt()

    @staticmethod
    def frequencyRangeFromBin(row, eis):
        """
        Set the frequencyRange in row from the EndianInput (eis) instance.
        """

        row._frequencyRange = Frequency.from2DBin(eis)

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
            thisValue = PolarizationType.from_int(eis.readInt())
            thisList.append(thisValue)
        row._polarizationTypes = thisList

    @staticmethod
    def mainBeamEfficiencyFromBin(row, eis):
        """
        Set the mainBeamEfficiency in row from the EndianInput (eis) instance.
        """

        mainBeamEfficiencyDim1 = eis.readInt()
        thisList = []
        for i in range(mainBeamEfficiencyDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._mainBeamEfficiency = thisList

    @staticmethod
    def beamDescriptionUIDFromBin(row, eis):
        """
        Set the beamDescriptionUID in row from the EndianInput (eis) instance.
        """

        row._beamDescriptionUID = EntityRef.fromBin(eis)

    @staticmethod
    def relativeAmplitudeRmsFromBin(row, eis):
        """
        Set the relativeAmplitudeRms in row from the EndianInput (eis) instance.
        """

        row._relativeAmplitudeRms = eis.readFloat()

    @staticmethod
    def directionFromBin(row, eis):
        """
        Set the direction in row from the EndianInput (eis) instance.
        """

        row._direction = Angle.from1DBin(eis)

    @staticmethod
    def minValidDirectionFromBin(row, eis):
        """
        Set the minValidDirection in row from the EndianInput (eis) instance.
        """

        row._minValidDirection = Angle.from1DBin(eis)

    @staticmethod
    def maxValidDirectionFromBin(row, eis):
        """
        Set the maxValidDirection in row from the EndianInput (eis) instance.
        """

        row._maxValidDirection = Angle.from1DBin(eis)

    @staticmethod
    def descriptionTypeFromBin(row, eis):
        """
        Set the descriptionType in row from the EndianInput (eis) instance.
        """

        row._descriptionType = PrimaryBeamDescription.from_int(eis.readInt())

    @staticmethod
    def imageChannelNumberFromBin(row, eis):
        """
        Set the imageChannelNumber in row from the EndianInput (eis) instance.
        """

        imageChannelNumberDim1 = eis.readInt()
        thisList = []
        for i in range(imageChannelNumberDim1):
            thisValue = eis.readInt()
            thisList.append(thisValue)
        row._imageChannelNumber = thisList

    @staticmethod
    def imageNominalFrequencyFromBin(row, eis):
        """
        Set the imageNominalFrequency in row from the EndianInput (eis) instance.
        """

        row._imageNominalFrequency = Frequency.from1DBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaName"] = CalPrimaryBeamRow.antennaNameFromBin
        _fromBinMethods["receiverBand"] = CalPrimaryBeamRow.receiverBandFromBin
        _fromBinMethods["calDataId"] = CalPrimaryBeamRow.calDataIdFromBin
        _fromBinMethods["calReductionId"] = CalPrimaryBeamRow.calReductionIdFromBin
        _fromBinMethods["startValidTime"] = CalPrimaryBeamRow.startValidTimeFromBin
        _fromBinMethods["endValidTime"] = CalPrimaryBeamRow.endValidTimeFromBin
        _fromBinMethods["antennaMake"] = CalPrimaryBeamRow.antennaMakeFromBin
        _fromBinMethods["numSubband"] = CalPrimaryBeamRow.numSubbandFromBin
        _fromBinMethods["frequencyRange"] = CalPrimaryBeamRow.frequencyRangeFromBin
        _fromBinMethods["numReceptor"] = CalPrimaryBeamRow.numReceptorFromBin
        _fromBinMethods["polarizationTypes"] = (
            CalPrimaryBeamRow.polarizationTypesFromBin
        )
        _fromBinMethods["mainBeamEfficiency"] = (
            CalPrimaryBeamRow.mainBeamEfficiencyFromBin
        )
        _fromBinMethods["beamDescriptionUID"] = (
            CalPrimaryBeamRow.beamDescriptionUIDFromBin
        )
        _fromBinMethods["relativeAmplitudeRms"] = (
            CalPrimaryBeamRow.relativeAmplitudeRmsFromBin
        )
        _fromBinMethods["direction"] = CalPrimaryBeamRow.directionFromBin
        _fromBinMethods["minValidDirection"] = (
            CalPrimaryBeamRow.minValidDirectionFromBin
        )
        _fromBinMethods["maxValidDirection"] = (
            CalPrimaryBeamRow.maxValidDirectionFromBin
        )
        _fromBinMethods["descriptionType"] = CalPrimaryBeamRow.descriptionTypeFromBin
        _fromBinMethods["imageChannelNumber"] = (
            CalPrimaryBeamRow.imageChannelNumberFromBin
        )
        _fromBinMethods["imageNominalFrequency"] = (
            CalPrimaryBeamRow.imageNominalFrequencyFromBin
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

        row = CalPrimaryBeamRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalPrimaryBeam",
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

    # ===> Attribute numSubband

    _numSubband = 0

    def getNumSubband(self):
        """
        Get numSubband.
        return numSubband as int
        """

        return self._numSubband

    def setNumSubband(self, numSubband):
        """
        Set numSubband with the specified int value.
        numSubband The int value to which numSubband is to be set.


        """

        self._numSubband = int(numSubband)

    # ===> Attribute frequencyRange

    _frequencyRange = None  # this is a 2D list of Frequency

    def getFrequencyRange(self):
        """
        Get frequencyRange.
        return frequencyRange as Frequency []  []
        """

        return copy.deepcopy(self._frequencyRange)

    def setFrequencyRange(self, frequencyRange):
        """
        Set frequencyRange with the specified Frequency []  []  value.
        frequencyRange The Frequency []  []  value to which frequencyRange is to be set.
        The value of frequencyRange can be anything allowed by the Frequency []  []  constructor.

        """

        # value must be a list
        if not isinstance(frequencyRange, list):
            raise ValueError("The value of frequencyRange must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(frequencyRange)

            shapeOK = len(listDims) == 2

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

    # ===> Attribute mainBeamEfficiency

    _mainBeamEfficiency = None  # this is a 1D list of float

    def getMainBeamEfficiency(self):
        """
        Get mainBeamEfficiency.
        return mainBeamEfficiency as float []
        """

        return copy.deepcopy(self._mainBeamEfficiency)

    def setMainBeamEfficiency(self, mainBeamEfficiency):
        """
        Set mainBeamEfficiency with the specified float []  value.
        mainBeamEfficiency The float []  value to which mainBeamEfficiency is to be set.


        """

        # value must be a list
        if not isinstance(mainBeamEfficiency, list):
            raise ValueError("The value of mainBeamEfficiency must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(mainBeamEfficiency)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of mainBeamEfficiency is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(mainBeamEfficiency, float):
                raise ValueError(
                    "type of the first value in mainBeamEfficiency is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._mainBeamEfficiency = copy.deepcopy(mainBeamEfficiency)
        except Exception as exc:
            raise ValueError("Invalid mainBeamEfficiency : " + str(exc))

    # ===> Attribute beamDescriptionUID

    _beamDescriptionUID = EntityRef()

    def getBeamDescriptionUID(self):
        """
        Get beamDescriptionUID.
        return beamDescriptionUID as EntityRef
        """

        # make sure it is a copy of EntityRef
        return EntityRef(self._beamDescriptionUID)

    def setBeamDescriptionUID(self, beamDescriptionUID):
        """
        Set beamDescriptionUID with the specified EntityRef value.
        beamDescriptionUID The EntityRef value to which beamDescriptionUID is to be set.
        The value of beamDescriptionUID can be anything allowed by the EntityRef constructor.

        """

        self._beamDescriptionUID = EntityRef(beamDescriptionUID)

    # ===> Attribute relativeAmplitudeRms

    _relativeAmplitudeRms = None

    def getRelativeAmplitudeRms(self):
        """
        Get relativeAmplitudeRms.
        return relativeAmplitudeRms as float
        """

        return self._relativeAmplitudeRms

    def setRelativeAmplitudeRms(self, relativeAmplitudeRms):
        """
        Set relativeAmplitudeRms with the specified float value.
        relativeAmplitudeRms The float value to which relativeAmplitudeRms is to be set.


        """

        self._relativeAmplitudeRms = float(relativeAmplitudeRms)

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

    # ===> Attribute minValidDirection

    _minValidDirection = None  # this is a 1D list of Angle

    def getMinValidDirection(self):
        """
        Get minValidDirection.
        return minValidDirection as Angle []
        """

        return copy.deepcopy(self._minValidDirection)

    def setMinValidDirection(self, minValidDirection):
        """
        Set minValidDirection with the specified Angle []  value.
        minValidDirection The Angle []  value to which minValidDirection is to be set.
        The value of minValidDirection can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(minValidDirection, list):
            raise ValueError("The value of minValidDirection must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(minValidDirection)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of minValidDirection is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(minValidDirection, Angle):
                raise ValueError(
                    "type of the first value in minValidDirection is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._minValidDirection = copy.deepcopy(minValidDirection)
        except Exception as exc:
            raise ValueError("Invalid minValidDirection : " + str(exc))

    # ===> Attribute maxValidDirection

    _maxValidDirection = None  # this is a 1D list of Angle

    def getMaxValidDirection(self):
        """
        Get maxValidDirection.
        return maxValidDirection as Angle []
        """

        return copy.deepcopy(self._maxValidDirection)

    def setMaxValidDirection(self, maxValidDirection):
        """
        Set maxValidDirection with the specified Angle []  value.
        maxValidDirection The Angle []  value to which maxValidDirection is to be set.
        The value of maxValidDirection can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(maxValidDirection, list):
            raise ValueError("The value of maxValidDirection must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(maxValidDirection)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of maxValidDirection is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(maxValidDirection, Angle):
                raise ValueError(
                    "type of the first value in maxValidDirection is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._maxValidDirection = copy.deepcopy(maxValidDirection)
        except Exception as exc:
            raise ValueError("Invalid maxValidDirection : " + str(exc))

    # ===> Attribute descriptionType

    _descriptionType = PrimaryBeamDescription.from_int(0)

    def getDescriptionType(self):
        """
        Get descriptionType.
        return descriptionType as PrimaryBeamDescription
        """

        return self._descriptionType

    def setDescriptionType(self, descriptionType):
        """
        Set descriptionType with the specified PrimaryBeamDescription value.
        descriptionType The PrimaryBeamDescription value to which descriptionType is to be set.


        """

        self._descriptionType = PrimaryBeamDescription(descriptionType)

    # ===> Attribute imageChannelNumber

    _imageChannelNumber = None  # this is a 1D list of int

    def getImageChannelNumber(self):
        """
        Get imageChannelNumber.
        return imageChannelNumber as int []
        """

        return copy.deepcopy(self._imageChannelNumber)

    def setImageChannelNumber(self, imageChannelNumber):
        """
        Set imageChannelNumber with the specified int []  value.
        imageChannelNumber The int []  value to which imageChannelNumber is to be set.


        """

        # value must be a list
        if not isinstance(imageChannelNumber, list):
            raise ValueError("The value of imageChannelNumber must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(imageChannelNumber)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of imageChannelNumber is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(imageChannelNumber, int):
                raise ValueError(
                    "type of the first value in imageChannelNumber is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._imageChannelNumber = copy.deepcopy(imageChannelNumber)
        except Exception as exc:
            raise ValueError("Invalid imageChannelNumber : " + str(exc))

    # ===> Attribute imageNominalFrequency

    _imageNominalFrequency = None  # this is a 1D list of Frequency

    def getImageNominalFrequency(self):
        """
        Get imageNominalFrequency.
        return imageNominalFrequency as Frequency []
        """

        return copy.deepcopy(self._imageNominalFrequency)

    def setImageNominalFrequency(self, imageNominalFrequency):
        """
        Set imageNominalFrequency with the specified Frequency []  value.
        imageNominalFrequency The Frequency []  value to which imageNominalFrequency is to be set.
        The value of imageNominalFrequency can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(imageNominalFrequency, list):
            raise ValueError("The value of imageNominalFrequency must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(imageNominalFrequency)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of imageNominalFrequency is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(imageNominalFrequency, Frequency):
                raise ValueError(
                    "type of the first value in imageNominalFrequency is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._imageNominalFrequency = copy.deepcopy(imageNominalFrequency)
        except Exception as exc:
            raise ValueError("Invalid imageNominalFrequency : " + str(exc))

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
        receiverBand,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        antennaMake,
        numSubband,
        frequencyRange,
        numReceptor,
        polarizationTypes,
        mainBeamEfficiency,
        beamDescriptionUID,
        relativeAmplitudeRms,
        direction,
        minValidDirection,
        maxValidDirection,
        descriptionType,
        imageChannelNumber,
        imageNominalFrequency,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalPrimaryBeamRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaName is a str, compare using the == operator.
        if not (self._antennaName == antennaName):
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

        # antennaMake is a AntennaMake, compare using the == operator on the getValue() output
        if not (self._antennaMake.getValue() == antennaMake.getValue()):
            return False

        # numSubband is a int, compare using the == operator.
        if not (self._numSubband == numSubband):
            return False

        # We compare two 2D arrays (lists).
        if frequencyRange is not None:
            if self._frequencyRange is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            frequencyRange_dims = pyasdm.utils.getListDims(frequencyRange)
            this_frequencyRange_dims = pyasdm.utils.getListDims(self._frequencyRange)
            if frequencyRange_dims != this_frequencyRange_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(frequencyRange_dims[0]):
                for j in range(frequencyRange_dims[1]):

                    # frequencyRange is a Frequency, compare using the almostEquals method.
                    if not (
                        self._frequencyRange[i][j].almostEquals(
                            frequencyRange[i][j],
                            self.getTable().getFrequencyRangeEqTolerance(),
                        )
                    ):
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

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._mainBeamEfficiency) != len(mainBeamEfficiency):
            return False
        for indx in range(len(mainBeamEfficiency)):

            # mainBeamEfficiency is a list of float, compare using == operator.
            if not (self._mainBeamEfficiency[indx] == mainBeamEfficiency[indx]):
                return False

        # beamDescriptionUID is a EntityRef, compare using the equals method.
        if not self._beamDescriptionUID.equals(beamDescriptionUID):
            return False

        # relativeAmplitudeRms is a float, compare using the == operator.
        if not (self._relativeAmplitudeRms == relativeAmplitudeRms):
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

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._minValidDirection) != len(minValidDirection):
            return False
        for indx in range(len(minValidDirection)):

            # minValidDirection is a list of Angle, compare using the almostEquals method.
            if not self._minValidDirection[indx].almostEquals(
                minValidDirection[indx],
                self.getTable().getMinValidDirectionEqTolerance(),
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._maxValidDirection) != len(maxValidDirection):
            return False
        for indx in range(len(maxValidDirection)):

            # maxValidDirection is a list of Angle, compare using the almostEquals method.
            if not self._maxValidDirection[indx].almostEquals(
                maxValidDirection[indx],
                self.getTable().getMaxValidDirectionEqTolerance(),
            ):
                return False

        # descriptionType is a PrimaryBeamDescription, compare using the == operator on the getValue() output
        if not (self._descriptionType.getValue() == descriptionType.getValue()):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._imageChannelNumber) != len(imageChannelNumber):
            return False
        for indx in range(len(imageChannelNumber)):

            # imageChannelNumber is a list of int, compare using == operator.
            if not (self._imageChannelNumber[indx] == imageChannelNumber[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._imageNominalFrequency) != len(imageNominalFrequency):
            return False
        for indx in range(len(imageNominalFrequency)):

            # imageNominalFrequency is a list of Frequency, compare using the almostEquals method.
            if not self._imageNominalFrequency[indx].almostEquals(
                imageNominalFrequency[indx],
                self.getTable().getImageNominalFrequencyEqTolerance(),
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
            otherRow.getAntennaMake(),
            otherRow.getNumSubband(),
            otherRow.getFrequencyRange(),
            otherRow.getNumReceptor(),
            otherRow.getPolarizationTypes(),
            otherRow.getMainBeamEfficiency(),
            otherRow.getBeamDescriptionUID(),
            otherRow.getRelativeAmplitudeRms(),
            otherRow.getDirection(),
            otherRow.getMinValidDirection(),
            otherRow.getMaxValidDirection(),
            otherRow.getDescriptionType(),
            otherRow.getImageChannelNumber(),
            otherRow.getImageNominalFrequency(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        antennaMake,
        numSubband,
        frequencyRange,
        numReceptor,
        polarizationTypes,
        mainBeamEfficiency,
        beamDescriptionUID,
        relativeAmplitudeRms,
        direction,
        minValidDirection,
        maxValidDirection,
        descriptionType,
        imageChannelNumber,
        imageNominalFrequency,
    ):

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # antennaMake is a AntennaMake, compare using the == operator on the getValue() output
        if not (self._antennaMake.getValue() == antennaMake.getValue()):
            return False

        # numSubband is a int, compare using the == operator.
        if not (self._numSubband == numSubband):
            return False

        # We compare two 2D arrays (lists).
        if frequencyRange is not None:
            if self._frequencyRange is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            frequencyRange_dims = pyasdm.utils.getListDims(frequencyRange)
            this_frequencyRange_dims = pyasdm.utils.getListDims(self._frequencyRange)
            if frequencyRange_dims != this_frequencyRange_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(frequencyRange_dims[0]):
                for j in range(frequencyRange_dims[1]):

                    # frequencyRange is a Frequency, compare using the almostEquals method.
                    if not (
                        self._frequencyRange[i][j].almostEquals(
                            frequencyRange[i][j],
                            self.getTable().getFrequencyRangeEqTolerance(),
                        )
                    ):
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

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._mainBeamEfficiency) != len(mainBeamEfficiency):
            return False
        for indx in range(len(mainBeamEfficiency)):

            # mainBeamEfficiency is a list of float, compare using == operator.
            if not (self._mainBeamEfficiency[indx] == mainBeamEfficiency[indx]):
                return False

        # beamDescriptionUID is a EntityRef, compare using the equals method.
        if not self._beamDescriptionUID.equals(beamDescriptionUID):
            return False

        # relativeAmplitudeRms is a float, compare using the == operator.
        if not (self._relativeAmplitudeRms == relativeAmplitudeRms):
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

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._minValidDirection) != len(minValidDirection):
            return False
        for indx in range(len(minValidDirection)):

            # minValidDirection is a list of Angle, compare using the almostEquals method.
            if not self._minValidDirection[indx].almostEquals(
                minValidDirection[indx],
                self.getTable().getMinValidDirectionEqTolerance(),
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._maxValidDirection) != len(maxValidDirection):
            return False
        for indx in range(len(maxValidDirection)):

            # maxValidDirection is a list of Angle, compare using the almostEquals method.
            if not self._maxValidDirection[indx].almostEquals(
                maxValidDirection[indx],
                self.getTable().getMaxValidDirectionEqTolerance(),
            ):
                return False

        # descriptionType is a PrimaryBeamDescription, compare using the == operator on the getValue() output
        if not (self._descriptionType.getValue() == descriptionType.getValue()):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._imageChannelNumber) != len(imageChannelNumber):
            return False
        for indx in range(len(imageChannelNumber)):

            # imageChannelNumber is a list of int, compare using == operator.
            if not (self._imageChannelNumber[indx] == imageChannelNumber[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._imageNominalFrequency) != len(imageNominalFrequency):
            return False
        for indx in range(len(imageNominalFrequency)):

            # imageNominalFrequency is a list of Frequency, compare using the almostEquals method.
            if not self._imageNominalFrequency[indx].almostEquals(
                imageNominalFrequency[indx],
                self.getTable().getImageNominalFrequencyEqTolerance(),
            ):
                return False

        return True


# initialize the dictionary that maps fields to init methods
CalPrimaryBeamRow.initFromBinMethods()
