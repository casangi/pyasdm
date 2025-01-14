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
# File CalAntennaSolutionsRow.py
#

import pyasdm.CalAntennaSolutionsTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.AtmPhaseCorrection import AtmPhaseCorrection


from pyasdm.enumerations.BasebandName import BasebandName


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.PolarizationType import PolarizationType


from xml.dom import minidom

import copy


class CalAntennaSolutionsRow:
    """
    The CalAntennaSolutionsRow class is a row of a CalAntennaSolutionsTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalAntennaSolutionsRow.
        When row is None, create an empty row attached to table, which must be a CalAntennaSolutionsTable.
        When row is given, copy those values in to the new row. The row argument must be a CalAntennaSolutionsRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalAntennaSolutionsTable):
            raise ValueError("table must be a CalAntennaSolutionsTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._antennaName = None

        self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)

        self._basebandName = BasebandName.from_int(0)

        self._receiverBand = ReceiverBand.from_int(0)

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._numReceptor = 0

        self._refAntennaName = None

        self._direction = []  # this is a list of Angle []

        self._frequencyRange = []  # this is a list of Frequency []

        self._integrationTime = Interval()

        self._polarizationTypes = []  # this is a list of PolarizationType []

        self._correctionValidity = None

        self._phaseAnt = []  # this is a list of float []

        self._phaseAntRMS = []  # this is a list of float []

        self._amplitudeAnt = []  # this is a list of float []

        self._amplitudeAntRMS = []  # this is a list of float []

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        self._spectralWindowId = Tag()

        if row is not None:
            if not isinstance(row, CalAntennaSolutionsRow):
                raise ValueError("row must be a CalAntennaSolutionsRow")

            # copy constructor

            self._antennaName = row._antennaName

            # We force the attribute of the result to be not None.
            if row._atmPhaseCorrection is None:
                self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)
            else:
                self._atmPhaseCorrection = AtmPhaseCorrection(row._atmPhaseCorrection)

            # We force the attribute of the result to be not None.
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            # We force the attribute of the result to be not None.
            if row._basebandName is None:
                self._basebandName = BasebandName.from_int(0)
            else:
                self._basebandName = BasebandName(row._basebandName)

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._spectralWindowId = Tag(row._spectralWindowId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            self._numReceptor = row._numReceptor

            self._refAntennaName = row._refAntennaName

            # direction is a  list , make a deep copy
            self._direction = copy.deepcopy(row._direction)

            # frequencyRange is a  list , make a deep copy
            self._frequencyRange = copy.deepcopy(row._frequencyRange)

            self._integrationTime = Interval(row._integrationTime)

            # polarizationTypes is a  list , make a deep copy
            self._polarizationTypes = copy.deepcopy(row._polarizationTypes)

            self._correctionValidity = row._correctionValidity

            # phaseAnt is a  list , make a deep copy
            self._phaseAnt = copy.deepcopy(row._phaseAnt)

            # phaseAntRMS is a  list , make a deep copy
            self._phaseAntRMS = copy.deepcopy(row._phaseAntRMS)

            # amplitudeAnt is a  list , make a deep copy
            self._amplitudeAnt = copy.deepcopy(row._amplitudeAnt)

            # amplitudeAntRMS is a  list , make a deep copy
            self._amplitudeAntRMS = copy.deepcopy(row._amplitudeAntRMS)

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
            "atmPhaseCorrection", AtmPhaseCorrection.name(self._atmPhaseCorrection)
        )

        result += Parser.valueToXML(
            "basebandName", BasebandName.name(self._basebandName)
        )

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.valueToXML("refAntennaName", self._refAntennaName)

        result += Parser.listExtendedValueToXML("direction", self._direction)

        result += Parser.listExtendedValueToXML("frequencyRange", self._frequencyRange)

        result += Parser.extendedValueToXML("integrationTime", self._integrationTime)

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.valueToXML("correctionValidity", self._correctionValidity)

        result += Parser.listValueToXML("phaseAnt", self._phaseAnt)

        result += Parser.listValueToXML("phaseAntRMS", self._phaseAntRMS)

        result += Parser.listValueToXML("amplitudeAnt", self._amplitudeAnt)

        result += Parser.listValueToXML("amplitudeAntRMS", self._amplitudeAntRMS)

        # extrinsic attributes

        result += Parser.extendedValueToXML("calDataId", self._calDataId)

        result += Parser.extendedValueToXML("calReductionId", self._calReductionId)

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
                "xmlrow is not a string or a minidom.Element",
                "CalAntennaSolutionsTable",
            )

        if rowdom.nodeName != "row":
            raise ConversionException(
                "the argument is not a row", "CalAntennaSolutionsTable"
            )

        # intrinsic attribute values

        antennaNameNode = rowdom.getElementsByTagName("antennaName")[0]

        self._antennaName = str(antennaNameNode.firstChild.data.strip())

        atmPhaseCorrectionNode = rowdom.getElementsByTagName("atmPhaseCorrection")[0]

        self._atmPhaseCorrection = AtmPhaseCorrection.newAtmPhaseCorrection(
            atmPhaseCorrectionNode.firstChild.data.strip()
        )

        basebandNameNode = rowdom.getElementsByTagName("basebandName")[0]

        self._basebandName = BasebandName.newBasebandName(
            basebandNameNode.firstChild.data.strip()
        )

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data.strip()
        )

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        refAntennaNameNode = rowdom.getElementsByTagName("refAntennaName")[0]

        self._refAntennaName = str(refAntennaNameNode.firstChild.data.strip())

        directionNode = rowdom.getElementsByTagName("direction")[0]

        directionStr = directionNode.firstChild.data.strip()

        self._direction = Parser.stringListToLists(
            directionStr, Angle, "CalAntennaSolutions", True
        )

        frequencyRangeNode = rowdom.getElementsByTagName("frequencyRange")[0]

        frequencyRangeStr = frequencyRangeNode.firstChild.data.strip()

        self._frequencyRange = Parser.stringListToLists(
            frequencyRangeStr, Frequency, "CalAntennaSolutions", True
        )

        integrationTimeNode = rowdom.getElementsByTagName("integrationTime")[0]

        self._integrationTime = Interval(integrationTimeNode.firstChild.data.strip())

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data.strip()
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "CalAntennaSolutions", False
        )

        correctionValidityNode = rowdom.getElementsByTagName("correctionValidity")[0]

        self._correctionValidity = bool(correctionValidityNode.firstChild.data.strip())

        phaseAntNode = rowdom.getElementsByTagName("phaseAnt")[0]

        phaseAntStr = phaseAntNode.firstChild.data.strip()

        self._phaseAnt = Parser.stringListToLists(
            phaseAntStr, float, "CalAntennaSolutions", False
        )

        phaseAntRMSNode = rowdom.getElementsByTagName("phaseAntRMS")[0]

        phaseAntRMSStr = phaseAntRMSNode.firstChild.data.strip()

        self._phaseAntRMS = Parser.stringListToLists(
            phaseAntRMSStr, float, "CalAntennaSolutions", False
        )

        amplitudeAntNode = rowdom.getElementsByTagName("amplitudeAnt")[0]

        amplitudeAntStr = amplitudeAntNode.firstChild.data.strip()

        self._amplitudeAnt = Parser.stringListToLists(
            amplitudeAntStr, float, "CalAntennaSolutions", False
        )

        amplitudeAntRMSNode = rowdom.getElementsByTagName("amplitudeAntRMS")[0]

        amplitudeAntRMSStr = amplitudeAntRMSNode.firstChild.data.strip()

        self._amplitudeAntRMS = Parser.stringListToLists(
            amplitudeAntRMSStr, float, "CalAntennaSolutions", False
        )

        # extrinsic attribute values

        calDataIdNode = rowdom.getElementsByTagName("calDataId")[0]

        self._calDataId = Tag(calDataIdNode.firstChild.data.strip())

        calReductionIdNode = rowdom.getElementsByTagName("calReductionId")[0]

        self._calReductionId = Tag(calReductionIdNode.firstChild.data.strip())

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")[0]

        self._spectralWindowId = Tag(spectralWindowIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        eos.writeStr(self._antennaName)

        eos.writeString(self._atmPhaseCorrection.toString())

        eos.writeString(self._receiverBand.toString())

        eos.writeString(self._basebandName.toString())

        self._calDataId.toBin(eos)

        self._calReductionId.toBin(eos)

        self._spectralWindowId.toBin(eos)

        self._startValidTime.toBin(eos)

        self._endValidTime.toBin(eos)

        eos.writeInt(self._numReceptor)

        eos.writeStr(self._refAntennaName)

        Angle.listToBin(self._direction, eos)

        Frequency.listToBin(self._frequencyRange, eos)

        self._integrationTime.toBin(eos)

        eos.writeInt(len(self._polarizationTypes))
        for i in range(len(self._polarizationTypes)):

            eos.writeString(self._polarizationTypes[i].toString())

        eos.writeBool(self._correctionValidity)

        eos.writeInt(len(self._phaseAnt))
        for i in range(len(self._phaseAnt)):

            eos.writeFloat(self._phaseAnt[i])

        eos.writeInt(len(self._phaseAntRMS))
        for i in range(len(self._phaseAntRMS)):

            eos.writeFloat(self._phaseAntRMS[i])

        eos.writeInt(len(self._amplitudeAnt))
        for i in range(len(self._amplitudeAnt)):

            eos.writeFloat(self._amplitudeAnt[i])

        eos.writeInt(len(self._amplitudeAntRMS))
        for i in range(len(self._amplitudeAntRMS)):

            eos.writeFloat(self._amplitudeAntRMS[i])

    @staticmethod
    def antennaNameFromBin(row, eis):
        """
        Set the antennaName in row from the EndianInput (eis) instance.
        """

        row._antennaName = eis.readStr()

    @staticmethod
    def atmPhaseCorrectionFromBin(row, eis):
        """
        Set the atmPhaseCorrection in row from the EndianInput (eis) instance.
        """

        row._atmPhaseCorrection = AtmPhaseCorrection.from_int(eis.readInt())

    @staticmethod
    def receiverBandFromBin(row, eis):
        """
        Set the receiverBand in row from the EndianInput (eis) instance.
        """

        row._receiverBand = ReceiverBand.from_int(eis.readInt())

    @staticmethod
    def basebandNameFromBin(row, eis):
        """
        Set the basebandName in row from the EndianInput (eis) instance.
        """

        row._basebandName = BasebandName.from_int(eis.readInt())

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
    def spectralWindowIdFromBin(row, eis):
        """
        Set the spectralWindowId in row from the EndianInput (eis) instance.
        """

        row._spectralWindowId = Tag.fromBin(eis)

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
    def numReceptorFromBin(row, eis):
        """
        Set the numReceptor in row from the EndianInput (eis) instance.
        """

        row._numReceptor = eis.readInt()

    @staticmethod
    def refAntennaNameFromBin(row, eis):
        """
        Set the refAntennaName in row from the EndianInput (eis) instance.
        """

        row._refAntennaName = eis.readStr()

    @staticmethod
    def directionFromBin(row, eis):
        """
        Set the direction in row from the EndianInput (eis) instance.
        """

        row._direction = Angle.from1DBin(eis)

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
    def correctionValidityFromBin(row, eis):
        """
        Set the correctionValidity in row from the EndianInput (eis) instance.
        """

        row._correctionValidity = eis.readBool()

    @staticmethod
    def phaseAntFromBin(row, eis):
        """
        Set the phaseAnt in row from the EndianInput (eis) instance.
        """

        phaseAntDim1 = eis.readInt()
        thisList = []
        for i in range(phaseAntDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._phaseAnt = thisList

    @staticmethod
    def phaseAntRMSFromBin(row, eis):
        """
        Set the phaseAntRMS in row from the EndianInput (eis) instance.
        """

        phaseAntRMSDim1 = eis.readInt()
        thisList = []
        for i in range(phaseAntRMSDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._phaseAntRMS = thisList

    @staticmethod
    def amplitudeAntFromBin(row, eis):
        """
        Set the amplitudeAnt in row from the EndianInput (eis) instance.
        """

        amplitudeAntDim1 = eis.readInt()
        thisList = []
        for i in range(amplitudeAntDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._amplitudeAnt = thisList

    @staticmethod
    def amplitudeAntRMSFromBin(row, eis):
        """
        Set the amplitudeAntRMS in row from the EndianInput (eis) instance.
        """

        amplitudeAntRMSDim1 = eis.readInt()
        thisList = []
        for i in range(amplitudeAntRMSDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._amplitudeAntRMS = thisList

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaName"] = CalAntennaSolutionsRow.antennaNameFromBin
        _fromBinMethods["atmPhaseCorrection"] = (
            CalAntennaSolutionsRow.atmPhaseCorrectionFromBin
        )
        _fromBinMethods["receiverBand"] = CalAntennaSolutionsRow.receiverBandFromBin
        _fromBinMethods["basebandName"] = CalAntennaSolutionsRow.basebandNameFromBin
        _fromBinMethods["calDataId"] = CalAntennaSolutionsRow.calDataIdFromBin
        _fromBinMethods["calReductionId"] = CalAntennaSolutionsRow.calReductionIdFromBin
        _fromBinMethods["spectralWindowId"] = (
            CalAntennaSolutionsRow.spectralWindowIdFromBin
        )
        _fromBinMethods["startValidTime"] = CalAntennaSolutionsRow.startValidTimeFromBin
        _fromBinMethods["endValidTime"] = CalAntennaSolutionsRow.endValidTimeFromBin
        _fromBinMethods["numReceptor"] = CalAntennaSolutionsRow.numReceptorFromBin
        _fromBinMethods["refAntennaName"] = CalAntennaSolutionsRow.refAntennaNameFromBin
        _fromBinMethods["direction"] = CalAntennaSolutionsRow.directionFromBin
        _fromBinMethods["frequencyRange"] = CalAntennaSolutionsRow.frequencyRangeFromBin
        _fromBinMethods["integrationTime"] = (
            CalAntennaSolutionsRow.integrationTimeFromBin
        )
        _fromBinMethods["polarizationTypes"] = (
            CalAntennaSolutionsRow.polarizationTypesFromBin
        )
        _fromBinMethods["correctionValidity"] = (
            CalAntennaSolutionsRow.correctionValidityFromBin
        )
        _fromBinMethods["phaseAnt"] = CalAntennaSolutionsRow.phaseAntFromBin
        _fromBinMethods["phaseAntRMS"] = CalAntennaSolutionsRow.phaseAntRMSFromBin
        _fromBinMethods["amplitudeAnt"] = CalAntennaSolutionsRow.amplitudeAntFromBin
        _fromBinMethods["amplitudeAntRMS"] = (
            CalAntennaSolutionsRow.amplitudeAntRMSFromBin
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

        row = CalAntennaSolutionsRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalAntennaSolutions",
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
            listDims = Parser.getListDims(direction)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of direction is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(direction, Angle):
                raise ValueError(
                    "type of the first value in direction is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._direction = copy.deepcopy(direction)
        except Exception as exc:
            raise ValueError("Invalid direction : " + str(exc))

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
            listDims = Parser.getListDims(frequencyRange)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of frequencyRange is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(frequencyRange, Frequency):
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
            listDims = Parser.getListDims(polarizationTypes)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of polarizationTypes is not correct")

            # the type of the values in the list must be PolarizationType
            # note : this only checks the first value found
            if not Parser.checkListType(polarizationTypes, PolarizationType):
                raise ValueError(
                    "type of the first value in polarizationTypes is not PolarizationType as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._polarizationTypes = copy.deepcopy(polarizationTypes)
        except Exception as exc:
            raise ValueError("Invalid polarizationTypes : " + str(exc))

    # ===> Attribute correctionValidity

    _correctionValidity = None

    def getCorrectionValidity(self):
        """
        Get correctionValidity.
        return correctionValidity as bool
        """

        return self._correctionValidity

    def setCorrectionValidity(self, correctionValidity):
        """
        Set correctionValidity with the specified bool value.
        correctionValidity The bool value to which correctionValidity is to be set.


        """

        self._correctionValidity = bool(correctionValidity)

    # ===> Attribute phaseAnt

    _phaseAnt = None  # this is a 1D list of float

    def getPhaseAnt(self):
        """
        Get phaseAnt.
        return phaseAnt as float []
        """

        return copy.deepcopy(self._phaseAnt)

    def setPhaseAnt(self, phaseAnt):
        """
        Set phaseAnt with the specified float []  value.
        phaseAnt The float []  value to which phaseAnt is to be set.


        """

        # value must be a list
        if not isinstance(phaseAnt, list):
            raise ValueError("The value of phaseAnt must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(phaseAnt)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of phaseAnt is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(phaseAnt, float):
                raise ValueError(
                    "type of the first value in phaseAnt is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phaseAnt = copy.deepcopy(phaseAnt)
        except Exception as exc:
            raise ValueError("Invalid phaseAnt : " + str(exc))

    # ===> Attribute phaseAntRMS

    _phaseAntRMS = None  # this is a 1D list of float

    def getPhaseAntRMS(self):
        """
        Get phaseAntRMS.
        return phaseAntRMS as float []
        """

        return copy.deepcopy(self._phaseAntRMS)

    def setPhaseAntRMS(self, phaseAntRMS):
        """
        Set phaseAntRMS with the specified float []  value.
        phaseAntRMS The float []  value to which phaseAntRMS is to be set.


        """

        # value must be a list
        if not isinstance(phaseAntRMS, list):
            raise ValueError("The value of phaseAntRMS must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(phaseAntRMS)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of phaseAntRMS is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(phaseAntRMS, float):
                raise ValueError(
                    "type of the first value in phaseAntRMS is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phaseAntRMS = copy.deepcopy(phaseAntRMS)
        except Exception as exc:
            raise ValueError("Invalid phaseAntRMS : " + str(exc))

    # ===> Attribute amplitudeAnt

    _amplitudeAnt = None  # this is a 1D list of float

    def getAmplitudeAnt(self):
        """
        Get amplitudeAnt.
        return amplitudeAnt as float []
        """

        return copy.deepcopy(self._amplitudeAnt)

    def setAmplitudeAnt(self, amplitudeAnt):
        """
        Set amplitudeAnt with the specified float []  value.
        amplitudeAnt The float []  value to which amplitudeAnt is to be set.


        """

        # value must be a list
        if not isinstance(amplitudeAnt, list):
            raise ValueError("The value of amplitudeAnt must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(amplitudeAnt)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of amplitudeAnt is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(amplitudeAnt, float):
                raise ValueError(
                    "type of the first value in amplitudeAnt is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._amplitudeAnt = copy.deepcopy(amplitudeAnt)
        except Exception as exc:
            raise ValueError("Invalid amplitudeAnt : " + str(exc))

    # ===> Attribute amplitudeAntRMS

    _amplitudeAntRMS = None  # this is a 1D list of float

    def getAmplitudeAntRMS(self):
        """
        Get amplitudeAntRMS.
        return amplitudeAntRMS as float []
        """

        return copy.deepcopy(self._amplitudeAntRMS)

    def setAmplitudeAntRMS(self, amplitudeAntRMS):
        """
        Set amplitudeAntRMS with the specified float []  value.
        amplitudeAntRMS The float []  value to which amplitudeAntRMS is to be set.


        """

        # value must be a list
        if not isinstance(amplitudeAntRMS, list):
            raise ValueError("The value of amplitudeAntRMS must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(amplitudeAntRMS)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of amplitudeAntRMS is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(amplitudeAntRMS, float):
                raise ValueError(
                    "type of the first value in amplitudeAntRMS is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._amplitudeAntRMS = copy.deepcopy(amplitudeAntRMS)
        except Exception as exc:
            raise ValueError("Invalid amplitudeAntRMS : " + str(exc))

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

    def getSpectralWindowUsingSpectralWindowId(self):
        """
        Returns the row in the SpectralWindow table having SpectralWindow.spectralWindowId == spectralWindowId

        """

        return (
            self._table.getContainer()
            .getSpectralWindow()
            .getRowByKey(self._spectralWindowId)
        )

    # comparison methods

    def compareNoAutoInc(
        self,
        antennaName,
        atmPhaseCorrection,
        receiverBand,
        basebandName,
        calDataId,
        calReductionId,
        spectralWindowId,
        startValidTime,
        endValidTime,
        numReceptor,
        refAntennaName,
        direction,
        frequencyRange,
        integrationTime,
        polarizationTypes,
        correctionValidity,
        phaseAnt,
        phaseAntRMS,
        amplitudeAnt,
        amplitudeAntRMS,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalAntennaSolutionsRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaName is a str, compare using the == operator.
        if not (self._antennaName == antennaName):
            return False

        # atmPhaseCorrection is a AtmPhaseCorrection, compare using the == operator on the getValue() output
        if not (self._atmPhaseCorrection.getValue() == atmPhaseCorrection.getValue()):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
            return False

        # basebandName is a BasebandName, compare using the == operator on the getValue() output
        if not (self._basebandName.getValue() == basebandName.getValue()):
            return False

        # calDataId is a Tag, compare using the equals method.
        if not self._calDataId.equals(calDataId):
            return False

        # calReductionId is a Tag, compare using the equals method.
        if not self._calReductionId.equals(calReductionId):
            return False

        # spectralWindowId is a Tag, compare using the equals method.
        if not self._spectralWindowId.equals(spectralWindowId):
            return False

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # refAntennaName is a str, compare using the == operator.
        if not (self._refAntennaName == refAntennaName):
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

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationTypes) != len(polarizationTypes):
            return False
        for indx in range(len(polarizationTypes)):

            # polarizationTypes is a list of PolarizationType, compare using == operator.
            if not (self._polarizationTypes[indx] == polarizationTypes[indx]):
                return False

        # correctionValidity is a bool, compare using the == operator.
        if not (self._correctionValidity == correctionValidity):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseAnt) != len(phaseAnt):
            return False
        for indx in range(len(phaseAnt)):

            # phaseAnt is a list of float, compare using == operator.
            if not (self._phaseAnt[indx] == phaseAnt[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseAntRMS) != len(phaseAntRMS):
            return False
        for indx in range(len(phaseAntRMS)):

            # phaseAntRMS is a list of float, compare using == operator.
            if not (self._phaseAntRMS[indx] == phaseAntRMS[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._amplitudeAnt) != len(amplitudeAnt):
            return False
        for indx in range(len(amplitudeAnt)):

            # amplitudeAnt is a list of float, compare using == operator.
            if not (self._amplitudeAnt[indx] == amplitudeAnt[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._amplitudeAntRMS) != len(amplitudeAntRMS):
            return False
        for indx in range(len(amplitudeAntRMS)):

            # amplitudeAntRMS is a list of float, compare using == operator.
            if not (self._amplitudeAntRMS[indx] == amplitudeAntRMS[indx]):
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
            otherRow.getNumReceptor(),
            otherRow.getRefAntennaName(),
            otherRow.getDirection(),
            otherRow.getFrequencyRange(),
            otherRow.getIntegrationTime(),
            otherRow.getPolarizationTypes(),
            otherRow.getCorrectionValidity(),
            otherRow.getPhaseAnt(),
            otherRow.getPhaseAntRMS(),
            otherRow.getAmplitudeAnt(),
            otherRow.getAmplitudeAntRMS(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        numReceptor,
        refAntennaName,
        direction,
        frequencyRange,
        integrationTime,
        polarizationTypes,
        correctionValidity,
        phaseAnt,
        phaseAntRMS,
        amplitudeAnt,
        amplitudeAntRMS,
    ):

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # refAntennaName is a str, compare using the == operator.
        if not (self._refAntennaName == refAntennaName):
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

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationTypes) != len(polarizationTypes):
            return False
        for indx in range(len(polarizationTypes)):

            # polarizationTypes is a list of PolarizationType, compare using == operator.
            if not (self._polarizationTypes[indx] == polarizationTypes[indx]):
                return False

        # correctionValidity is a bool, compare using the == operator.
        if not (self._correctionValidity == correctionValidity):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseAnt) != len(phaseAnt):
            return False
        for indx in range(len(phaseAnt)):

            # phaseAnt is a list of float, compare using == operator.
            if not (self._phaseAnt[indx] == phaseAnt[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseAntRMS) != len(phaseAntRMS):
            return False
        for indx in range(len(phaseAntRMS)):

            # phaseAntRMS is a list of float, compare using == operator.
            if not (self._phaseAntRMS[indx] == phaseAntRMS[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._amplitudeAnt) != len(amplitudeAnt):
            return False
        for indx in range(len(amplitudeAnt)):

            # amplitudeAnt is a list of float, compare using == operator.
            if not (self._amplitudeAnt[indx] == amplitudeAnt[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._amplitudeAntRMS) != len(amplitudeAntRMS):
            return False
        for indx in range(len(amplitudeAntRMS)):

            # amplitudeAntRMS is a list of float, compare using == operator.
            if not (self._amplitudeAntRMS[indx] == amplitudeAntRMS[indx]):
                return False

        return True


# initialize the dictionary that maps fields to init methods
CalAntennaSolutionsRow.initFromBinMethods()
