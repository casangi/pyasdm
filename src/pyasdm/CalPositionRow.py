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
# File CalPositionRow.py
#

import pyasdm.CalPositionTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.AtmPhaseCorrection import AtmPhaseCorrection


from pyasdm.enumerations.PositionMethod import PositionMethod


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from xml.dom import minidom

import copy


class CalPositionRow:
    """
    The CalPositionRow class is a row of a CalPositionTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalPositionRow.
        When row is None, create an empty row attached to table, which must be a CalPositionTable.
        When row is given, copy those values in to the new row. The row argument must be a CalPositionRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalPositionTable):
            raise ValueError("table must be a CalPositionTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._antennaName = None

        self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._antennaPosition = []  # this is a list of Length []

        self._stationName = None

        self._stationPosition = []  # this is a list of Length []

        self._positionMethod = PositionMethod.from_int(0)

        self._receiverBand = ReceiverBand.from_int(0)

        self._numAntenna = 0

        self._refAntennaNames = []  # this is a list of str []

        self._axesOffset = Length()

        self._axesOffsetErr = Length()

        self._axesOffsetFixed = None

        self._positionOffset = []  # this is a list of Length []

        self._positionErr = []  # this is a list of Length []

        self._reducedChiSquared = None

        self._delayRmsExists = False

        self._delayRms = None

        self._phaseRmsExists = False

        self._phaseRms = Angle()

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalPositionRow):
                raise ValueError("row must be a CalPositionRow")

            # copy constructor

            self._antennaName = row._antennaName

            # We force the attribute of the result to be not None.
            if row._atmPhaseCorrection is None:
                self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)
            else:
                self._atmPhaseCorrection = AtmPhaseCorrection(row._atmPhaseCorrection)

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            # antennaPosition is a  list , make a deep copy
            self._antennaPosition = copy.deepcopy(row._antennaPosition)

            self._stationName = row._stationName

            # stationPosition is a  list , make a deep copy
            self._stationPosition = copy.deepcopy(row._stationPosition)

            # We force the attribute of the result to be not None
            if row._positionMethod is None:
                self._positionMethod = PositionMethod.from_int(0)
            else:
                self._positionMethod = PositionMethod(row._positionMethod)

            # We force the attribute of the result to be not None
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            self._numAntenna = row._numAntenna

            # refAntennaNames is a  list , make a deep copy
            self._refAntennaNames = copy.deepcopy(row._refAntennaNames)

            self._axesOffset = Length(row._axesOffset)

            self._axesOffsetErr = Length(row._axesOffsetErr)

            self._axesOffsetFixed = row._axesOffsetFixed

            # positionOffset is a  list , make a deep copy
            self._positionOffset = copy.deepcopy(row._positionOffset)

            # positionErr is a  list , make a deep copy
            self._positionErr = copy.deepcopy(row._positionErr)

            self._reducedChiSquared = row._reducedChiSquared

            # by default set systematically delayRms's value to something not None

            if row._delayRmsExists:

                self._delayRms = row._delayRms

                self._delayRmsExists = True

            # by default set systematically phaseRms's value to something not None

            if row._phaseRmsExists:

                self._phaseRms = Angle(row._phaseRms)

                self._phaseRmsExists = True

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

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.listExtendedValueToXML(
            "antennaPosition", self._antennaPosition
        )

        result += Parser.valueToXML("stationName", self._stationName)

        result += Parser.listExtendedValueToXML(
            "stationPosition", self._stationPosition
        )

        result += Parser.valueToXML(
            "positionMethod", PositionMethod.name(self._positionMethod)
        )

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.valueToXML("numAntenna", self._numAntenna)

        result += Parser.listValueToXML("refAntennaNames", self._refAntennaNames)

        result += Parser.extendedValueToXML("axesOffset", self._axesOffset)

        result += Parser.extendedValueToXML("axesOffsetErr", self._axesOffsetErr)

        result += Parser.valueToXML("axesOffsetFixed", self._axesOffsetFixed)

        result += Parser.listExtendedValueToXML("positionOffset", self._positionOffset)

        result += Parser.listExtendedValueToXML("positionErr", self._positionErr)

        result += Parser.valueToXML("reducedChiSquared", self._reducedChiSquared)

        if self._delayRmsExists:

            result += Parser.valueToXML("delayRms", self._delayRms)

        if self._phaseRmsExists:

            result += Parser.extendedValueToXML("phaseRms", self._phaseRms)

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
                "xmlrow is not a string or a minidom.Element", "CalPositionTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalPositionTable")

        # intrinsic attribute values

        antennaNameNode = rowdom.getElementsByTagName("antennaName")[0]

        self._antennaName = str(antennaNameNode.firstChild.data.strip())

        atmPhaseCorrectionNode = rowdom.getElementsByTagName("atmPhaseCorrection")[0]

        self._atmPhaseCorrection = AtmPhaseCorrection.newAtmPhaseCorrection(
            atmPhaseCorrectionNode.firstChild.data.strip()
        )

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        antennaPositionNode = rowdom.getElementsByTagName("antennaPosition")[0]

        antennaPositionStr = antennaPositionNode.firstChild.data.strip()

        self._antennaPosition = Parser.stringListToLists(
            antennaPositionStr, Length, "CalPosition", True
        )

        stationNameNode = rowdom.getElementsByTagName("stationName")[0]

        self._stationName = str(stationNameNode.firstChild.data.strip())

        stationPositionNode = rowdom.getElementsByTagName("stationPosition")[0]

        stationPositionStr = stationPositionNode.firstChild.data.strip()

        self._stationPosition = Parser.stringListToLists(
            stationPositionStr, Length, "CalPosition", True
        )

        positionMethodNode = rowdom.getElementsByTagName("positionMethod")[0]

        self._positionMethod = PositionMethod.newPositionMethod(
            positionMethodNode.firstChild.data.strip()
        )

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data.strip()
        )

        numAntennaNode = rowdom.getElementsByTagName("numAntenna")[0]

        self._numAntenna = int(numAntennaNode.firstChild.data.strip())

        refAntennaNamesNode = rowdom.getElementsByTagName("refAntennaNames")[0]

        refAntennaNamesStr = refAntennaNamesNode.firstChild.data.strip()

        self._refAntennaNames = Parser.stringListToLists(
            refAntennaNamesStr, str, "CalPosition", False
        )

        axesOffsetNode = rowdom.getElementsByTagName("axesOffset")[0]

        self._axesOffset = Length(axesOffsetNode.firstChild.data.strip())

        axesOffsetErrNode = rowdom.getElementsByTagName("axesOffsetErr")[0]

        self._axesOffsetErr = Length(axesOffsetErrNode.firstChild.data.strip())

        axesOffsetFixedNode = rowdom.getElementsByTagName("axesOffsetFixed")[0]

        self._axesOffsetFixed = bool(axesOffsetFixedNode.firstChild.data.strip())

        positionOffsetNode = rowdom.getElementsByTagName("positionOffset")[0]

        positionOffsetStr = positionOffsetNode.firstChild.data.strip()

        self._positionOffset = Parser.stringListToLists(
            positionOffsetStr, Length, "CalPosition", True
        )

        positionErrNode = rowdom.getElementsByTagName("positionErr")[0]

        positionErrStr = positionErrNode.firstChild.data.strip()

        self._positionErr = Parser.stringListToLists(
            positionErrStr, Length, "CalPosition", True
        )

        reducedChiSquaredNode = rowdom.getElementsByTagName("reducedChiSquared")[0]

        self._reducedChiSquared = float(reducedChiSquaredNode.firstChild.data.strip())

        delayRmsNode = rowdom.getElementsByTagName("delayRms")
        if len(delayRmsNode) > 0:

            self._delayRms = float(delayRmsNode[0].firstChild.data.strip())

            self._delayRmsExists = True

        phaseRmsNode = rowdom.getElementsByTagName("phaseRms")
        if len(phaseRmsNode) > 0:

            self._phaseRms = Angle(phaseRmsNode[0].firstChild.data.strip())

            self._phaseRmsExists = True

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

        eos.writeString(self._atmPhaseCorrection.toString())

        self._calDataId.toBin(eos)

        self._calReductionId.toBin(eos)

        self._startValidTime.toBin(eos)

        self._endValidTime.toBin(eos)

        Length.listToBin(self._antennaPosition, eos)

        eos.writeStr(self._stationName)

        Length.listToBin(self._stationPosition, eos)

        eos.writeString(self._positionMethod.toString())

        eos.writeString(self._receiverBand.toString())

        eos.writeInt(self._numAntenna)

        eos.writeInt(len(self._refAntennaNames))
        for i in range(len(self._refAntennaNames)):

            eos.writeStr(self._refAntennaNames[i])

        self._axesOffset.toBin(eos)

        self._axesOffsetErr.toBin(eos)

        eos.writeBool(self._axesOffsetFixed)

        Length.listToBin(self._positionOffset, eos)

        Length.listToBin(self._positionErr, eos)

        eos.writeFloat(self._reducedChiSquared)

        eos.writeBool(self._delayRmsExists)
        if self._delayRmsExists:

            eos.writeFloat(self._delayRms)

        eos.writeBool(self._phaseRmsExists)
        if self._phaseRmsExists:

            self._phaseRms.toBin(eos)

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
    def antennaPositionFromBin(row, eis):
        """
        Set the antennaPosition in row from the EndianInput (eis) instance.
        """

        row._antennaPosition = Length.from1DBin(eis)

    @staticmethod
    def stationNameFromBin(row, eis):
        """
        Set the stationName in row from the EndianInput (eis) instance.
        """

        row._stationName = eis.readStr()

    @staticmethod
    def stationPositionFromBin(row, eis):
        """
        Set the stationPosition in row from the EndianInput (eis) instance.
        """

        row._stationPosition = Length.from1DBin(eis)

    @staticmethod
    def positionMethodFromBin(row, eis):
        """
        Set the positionMethod in row from the EndianInput (eis) instance.
        """

        row._positionMethod = PositionMethod.from_int(eis.readInt())

    @staticmethod
    def receiverBandFromBin(row, eis):
        """
        Set the receiverBand in row from the EndianInput (eis) instance.
        """

        row._receiverBand = ReceiverBand.from_int(eis.readInt())

    @staticmethod
    def numAntennaFromBin(row, eis):
        """
        Set the numAntenna in row from the EndianInput (eis) instance.
        """

        row._numAntenna = eis.readInt()

    @staticmethod
    def refAntennaNamesFromBin(row, eis):
        """
        Set the refAntennaNames in row from the EndianInput (eis) instance.
        """

        refAntennaNamesDim1 = eis.readInt()
        thisList = []
        for i in range(refAntennaNamesDim1):
            thisValue = eis.readStr()
            thisList.append(thisValue)
        row._refAntennaNames = thisList

    @staticmethod
    def axesOffsetFromBin(row, eis):
        """
        Set the axesOffset in row from the EndianInput (eis) instance.
        """

        row._axesOffset = Length.fromBin(eis)

    @staticmethod
    def axesOffsetErrFromBin(row, eis):
        """
        Set the axesOffsetErr in row from the EndianInput (eis) instance.
        """

        row._axesOffsetErr = Length.fromBin(eis)

    @staticmethod
    def axesOffsetFixedFromBin(row, eis):
        """
        Set the axesOffsetFixed in row from the EndianInput (eis) instance.
        """

        row._axesOffsetFixed = eis.readBool()

    @staticmethod
    def positionOffsetFromBin(row, eis):
        """
        Set the positionOffset in row from the EndianInput (eis) instance.
        """

        row._positionOffset = Length.from1DBin(eis)

    @staticmethod
    def positionErrFromBin(row, eis):
        """
        Set the positionErr in row from the EndianInput (eis) instance.
        """

        row._positionErr = Length.from1DBin(eis)

    @staticmethod
    def reducedChiSquaredFromBin(row, eis):
        """
        Set the reducedChiSquared in row from the EndianInput (eis) instance.
        """

        row._reducedChiSquared = eis.readFloat()

    @staticmethod
    def delayRmsFromBin(row, eis):
        """
        Set the optional delayRms in row from the EndianInput (eis) instance.
        """
        row._delayRmsExists = eis.readBool()
        if row._delayRmsExists:

            row._delayRms = eis.readFloat()

    @staticmethod
    def phaseRmsFromBin(row, eis):
        """
        Set the optional phaseRms in row from the EndianInput (eis) instance.
        """
        row._phaseRmsExists = eis.readBool()
        if row._phaseRmsExists:

            row._phaseRms = Angle.fromBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaName"] = CalPositionRow.antennaNameFromBin
        _fromBinMethods["atmPhaseCorrection"] = CalPositionRow.atmPhaseCorrectionFromBin
        _fromBinMethods["calDataId"] = CalPositionRow.calDataIdFromBin
        _fromBinMethods["calReductionId"] = CalPositionRow.calReductionIdFromBin
        _fromBinMethods["startValidTime"] = CalPositionRow.startValidTimeFromBin
        _fromBinMethods["endValidTime"] = CalPositionRow.endValidTimeFromBin
        _fromBinMethods["antennaPosition"] = CalPositionRow.antennaPositionFromBin
        _fromBinMethods["stationName"] = CalPositionRow.stationNameFromBin
        _fromBinMethods["stationPosition"] = CalPositionRow.stationPositionFromBin
        _fromBinMethods["positionMethod"] = CalPositionRow.positionMethodFromBin
        _fromBinMethods["receiverBand"] = CalPositionRow.receiverBandFromBin
        _fromBinMethods["numAntenna"] = CalPositionRow.numAntennaFromBin
        _fromBinMethods["refAntennaNames"] = CalPositionRow.refAntennaNamesFromBin
        _fromBinMethods["axesOffset"] = CalPositionRow.axesOffsetFromBin
        _fromBinMethods["axesOffsetErr"] = CalPositionRow.axesOffsetErrFromBin
        _fromBinMethods["axesOffsetFixed"] = CalPositionRow.axesOffsetFixedFromBin
        _fromBinMethods["positionOffset"] = CalPositionRow.positionOffsetFromBin
        _fromBinMethods["positionErr"] = CalPositionRow.positionErrFromBin
        _fromBinMethods["reducedChiSquared"] = CalPositionRow.reducedChiSquaredFromBin

        _fromBinMethods["delayRms"] = CalPositionRow.delayRmsFromBin
        _fromBinMethods["phaseRms"] = CalPositionRow.phaseRmsFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CalPositionRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalPosition",
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

    # ===> Attribute antennaPosition

    _antennaPosition = None  # this is a 1D list of Length

    def getAntennaPosition(self):
        """
        Get antennaPosition.
        return antennaPosition as Length []
        """

        return copy.deepcopy(self._antennaPosition)

    def setAntennaPosition(self, antennaPosition):
        """
        Set antennaPosition with the specified Length []  value.
        antennaPosition The Length []  value to which antennaPosition is to be set.
        The value of antennaPosition can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(antennaPosition, list):
            raise ValueError("The value of antennaPosition must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(antennaPosition)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of antennaPosition is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(antennaPosition, Length):
                raise ValueError(
                    "type of the first value in antennaPosition is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._antennaPosition = copy.deepcopy(antennaPosition)
        except Exception as exc:
            raise ValueError("Invalid antennaPosition : " + str(exc))

    # ===> Attribute stationName

    _stationName = None

    def getStationName(self):
        """
        Get stationName.
        return stationName as str
        """

        return self._stationName

    def setStationName(self, stationName):
        """
        Set stationName with the specified str value.
        stationName The str value to which stationName is to be set.


        """

        self._stationName = str(stationName)

    # ===> Attribute stationPosition

    _stationPosition = None  # this is a 1D list of Length

    def getStationPosition(self):
        """
        Get stationPosition.
        return stationPosition as Length []
        """

        return copy.deepcopy(self._stationPosition)

    def setStationPosition(self, stationPosition):
        """
        Set stationPosition with the specified Length []  value.
        stationPosition The Length []  value to which stationPosition is to be set.
        The value of stationPosition can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(stationPosition, list):
            raise ValueError("The value of stationPosition must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(stationPosition)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of stationPosition is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(stationPosition, Length):
                raise ValueError(
                    "type of the first value in stationPosition is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._stationPosition = copy.deepcopy(stationPosition)
        except Exception as exc:
            raise ValueError("Invalid stationPosition : " + str(exc))

    # ===> Attribute positionMethod

    _positionMethod = PositionMethod.from_int(0)

    def getPositionMethod(self):
        """
        Get positionMethod.
        return positionMethod as PositionMethod
        """

        return self._positionMethod

    def setPositionMethod(self, positionMethod):
        """
        Set positionMethod with the specified PositionMethod value.
        positionMethod The PositionMethod value to which positionMethod is to be set.


        """

        self._positionMethod = PositionMethod(positionMethod)

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

    # ===> Attribute refAntennaNames

    _refAntennaNames = None  # this is a 1D list of str

    def getRefAntennaNames(self):
        """
        Get refAntennaNames.
        return refAntennaNames as str []
        """

        return copy.deepcopy(self._refAntennaNames)

    def setRefAntennaNames(self, refAntennaNames):
        """
        Set refAntennaNames with the specified str []  value.
        refAntennaNames The str []  value to which refAntennaNames is to be set.


        """

        # value must be a list
        if not isinstance(refAntennaNames, list):
            raise ValueError("The value of refAntennaNames must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(refAntennaNames)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of refAntennaNames is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not Parser.checkListType(refAntennaNames, str):
                raise ValueError(
                    "type of the first value in refAntennaNames is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._refAntennaNames = copy.deepcopy(refAntennaNames)
        except Exception as exc:
            raise ValueError("Invalid refAntennaNames : " + str(exc))

    # ===> Attribute axesOffset

    _axesOffset = Length()

    def getAxesOffset(self):
        """
        Get axesOffset.
        return axesOffset as Length
        """

        # make sure it is a copy of Length
        return Length(self._axesOffset)

    def setAxesOffset(self, axesOffset):
        """
        Set axesOffset with the specified Length value.
        axesOffset The Length value to which axesOffset is to be set.
        The value of axesOffset can be anything allowed by the Length constructor.

        """

        self._axesOffset = Length(axesOffset)

    # ===> Attribute axesOffsetErr

    _axesOffsetErr = Length()

    def getAxesOffsetErr(self):
        """
        Get axesOffsetErr.
        return axesOffsetErr as Length
        """

        # make sure it is a copy of Length
        return Length(self._axesOffsetErr)

    def setAxesOffsetErr(self, axesOffsetErr):
        """
        Set axesOffsetErr with the specified Length value.
        axesOffsetErr The Length value to which axesOffsetErr is to be set.
        The value of axesOffsetErr can be anything allowed by the Length constructor.

        """

        self._axesOffsetErr = Length(axesOffsetErr)

    # ===> Attribute axesOffsetFixed

    _axesOffsetFixed = None

    def getAxesOffsetFixed(self):
        """
        Get axesOffsetFixed.
        return axesOffsetFixed as bool
        """

        return self._axesOffsetFixed

    def setAxesOffsetFixed(self, axesOffsetFixed):
        """
        Set axesOffsetFixed with the specified bool value.
        axesOffsetFixed The bool value to which axesOffsetFixed is to be set.


        """

        self._axesOffsetFixed = bool(axesOffsetFixed)

    # ===> Attribute positionOffset

    _positionOffset = None  # this is a 1D list of Length

    def getPositionOffset(self):
        """
        Get positionOffset.
        return positionOffset as Length []
        """

        return copy.deepcopy(self._positionOffset)

    def setPositionOffset(self, positionOffset):
        """
        Set positionOffset with the specified Length []  value.
        positionOffset The Length []  value to which positionOffset is to be set.
        The value of positionOffset can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(positionOffset, list):
            raise ValueError("The value of positionOffset must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(positionOffset)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of positionOffset is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(positionOffset, Length):
                raise ValueError(
                    "type of the first value in positionOffset is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._positionOffset = copy.deepcopy(positionOffset)
        except Exception as exc:
            raise ValueError("Invalid positionOffset : " + str(exc))

    # ===> Attribute positionErr

    _positionErr = None  # this is a 1D list of Length

    def getPositionErr(self):
        """
        Get positionErr.
        return positionErr as Length []
        """

        return copy.deepcopy(self._positionErr)

    def setPositionErr(self, positionErr):
        """
        Set positionErr with the specified Length []  value.
        positionErr The Length []  value to which positionErr is to be set.
        The value of positionErr can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(positionErr, list):
            raise ValueError("The value of positionErr must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(positionErr)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of positionErr is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(positionErr, Length):
                raise ValueError(
                    "type of the first value in positionErr is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._positionErr = copy.deepcopy(positionErr)
        except Exception as exc:
            raise ValueError("Invalid positionErr : " + str(exc))

    # ===> Attribute reducedChiSquared

    _reducedChiSquared = None

    def getReducedChiSquared(self):
        """
        Get reducedChiSquared.
        return reducedChiSquared as float
        """

        return self._reducedChiSquared

    def setReducedChiSquared(self, reducedChiSquared):
        """
        Set reducedChiSquared with the specified float value.
        reducedChiSquared The float value to which reducedChiSquared is to be set.


        """

        self._reducedChiSquared = float(reducedChiSquared)

    # ===> Attribute delayRms, which is optional
    _delayRmsExists = False

    _delayRms = None

    def isDelayRmsExists(self):
        """
        The attribute delayRms is optional. Return True if this attribute exists.
        return True if and only if the delayRms attribute exists.
        """
        return self._delayRmsExists

    def getDelayRms(self):
        """
        Get delayRms, which is optional.
        return delayRms as float
        raises ValueError If delayRms does not exist.
        """
        if not self._delayRmsExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + delayRms
                + " attribute in table CalPosition does not exist!"
            )

        return self._delayRms

    def setDelayRms(self, delayRms):
        """
        Set delayRms with the specified float value.
        delayRms The float value to which delayRms is to be set.


        """

        self._delayRms = float(delayRms)

        self._delayRmsExists = True

    def clearDelayRms(self):
        """
        Mark delayRms, which is an optional field, as non-existent.
        """
        self._delayRmsExists = False

    # ===> Attribute phaseRms, which is optional
    _phaseRmsExists = False

    _phaseRms = Angle()

    def isPhaseRmsExists(self):
        """
        The attribute phaseRms is optional. Return True if this attribute exists.
        return True if and only if the phaseRms attribute exists.
        """
        return self._phaseRmsExists

    def getPhaseRms(self):
        """
        Get phaseRms, which is optional.
        return phaseRms as Angle
        raises ValueError If phaseRms does not exist.
        """
        if not self._phaseRmsExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + phaseRms
                + " attribute in table CalPosition does not exist!"
            )

        # make sure it is a copy of Angle
        return Angle(self._phaseRms)

    def setPhaseRms(self, phaseRms):
        """
        Set phaseRms with the specified Angle value.
        phaseRms The Angle value to which phaseRms is to be set.
        The value of phaseRms can be anything allowed by the Angle constructor.

        """

        self._phaseRms = Angle(phaseRms)

        self._phaseRmsExists = True

    def clearPhaseRms(self):
        """
        Mark phaseRms, which is an optional field, as non-existent.
        """
        self._phaseRmsExists = False

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
        antennaName,
        atmPhaseCorrection,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        antennaPosition,
        stationName,
        stationPosition,
        positionMethod,
        receiverBand,
        numAntenna,
        refAntennaNames,
        axesOffset,
        axesOffsetErr,
        axesOffsetFixed,
        positionOffset,
        positionErr,
        reducedChiSquared,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalPositionRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaName is a str, compare using the == operator.
        if not (self._antennaName == antennaName):
            return False

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
        if len(self._antennaPosition) != len(antennaPosition):
            return False
        for indx in range(len(antennaPosition)):

            # antennaPosition is a list of Length, compare using the almostEquals method.
            if not self._antennaPosition[indx].almostEquals(
                antennaPosition[indx], self.getTable().getAntennaPositionEqTolerance()
            ):
                return False

        # stationName is a str, compare using the == operator.
        if not (self._stationName == stationName):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._stationPosition) != len(stationPosition):
            return False
        for indx in range(len(stationPosition)):

            # stationPosition is a list of Length, compare using the almostEquals method.
            if not self._stationPosition[indx].almostEquals(
                stationPosition[indx], self.getTable().getStationPositionEqTolerance()
            ):
                return False

        # positionMethod is a PositionMethod, compare using the == operator on the getValue() output
        if not (self._positionMethod.getValue() == positionMethod.getValue()):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
            return False

        # numAntenna is a int, compare using the == operator.
        if not (self._numAntenna == numAntenna):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._refAntennaNames) != len(refAntennaNames):
            return False
        for indx in range(len(refAntennaNames)):

            # refAntennaNames is a list of str, compare using == operator.
            if not (self._refAntennaNames[indx] == refAntennaNames[indx]):
                return False

        # axesOffset is a Length, compare using the almostEquals method.
        if not self._axesOffset.almostEquals(
            axesOffset, self.getTable().getAxesOffsetEqTolerance()
        ):
            return False

        # axesOffsetErr is a Length, compare using the almostEquals method.
        if not self._axesOffsetErr.almostEquals(
            axesOffsetErr, self.getTable().getAxesOffsetErrEqTolerance()
        ):
            return False

        # axesOffsetFixed is a bool, compare using the == operator.
        if not (self._axesOffsetFixed == axesOffsetFixed):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._positionOffset) != len(positionOffset):
            return False
        for indx in range(len(positionOffset)):

            # positionOffset is a list of Length, compare using the almostEquals method.
            if not self._positionOffset[indx].almostEquals(
                positionOffset[indx], self.getTable().getPositionOffsetEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._positionErr) != len(positionErr):
            return False
        for indx in range(len(positionErr)):

            # positionErr is a list of Length, compare using the almostEquals method.
            if not self._positionErr[indx].almostEquals(
                positionErr[indx], self.getTable().getPositionErrEqTolerance()
            ):
                return False

        # reducedChiSquared is a float, compare using the == operator.
        if not (self._reducedChiSquared == reducedChiSquared):
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
            otherRow.getAntennaPosition(),
            otherRow.getStationName(),
            otherRow.getStationPosition(),
            otherRow.getPositionMethod(),
            otherRow.getReceiverBand(),
            otherRow.getNumAntenna(),
            otherRow.getRefAntennaNames(),
            otherRow.getAxesOffset(),
            otherRow.getAxesOffsetErr(),
            otherRow.getAxesOffsetFixed(),
            otherRow.getPositionOffset(),
            otherRow.getPositionErr(),
            otherRow.getReducedChiSquared(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        antennaPosition,
        stationName,
        stationPosition,
        positionMethod,
        receiverBand,
        numAntenna,
        refAntennaNames,
        axesOffset,
        axesOffsetErr,
        axesOffsetFixed,
        positionOffset,
        positionErr,
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
        if len(self._antennaPosition) != len(antennaPosition):
            return False
        for indx in range(len(antennaPosition)):

            # antennaPosition is a list of Length, compare using the almostEquals method.
            if not self._antennaPosition[indx].almostEquals(
                antennaPosition[indx], self.getTable().getAntennaPositionEqTolerance()
            ):
                return False

        # stationName is a str, compare using the == operator.
        if not (self._stationName == stationName):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._stationPosition) != len(stationPosition):
            return False
        for indx in range(len(stationPosition)):

            # stationPosition is a list of Length, compare using the almostEquals method.
            if not self._stationPosition[indx].almostEquals(
                stationPosition[indx], self.getTable().getStationPositionEqTolerance()
            ):
                return False

        # positionMethod is a PositionMethod, compare using the == operator on the getValue() output
        if not (self._positionMethod.getValue() == positionMethod.getValue()):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
            return False

        # numAntenna is a int, compare using the == operator.
        if not (self._numAntenna == numAntenna):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._refAntennaNames) != len(refAntennaNames):
            return False
        for indx in range(len(refAntennaNames)):

            # refAntennaNames is a list of str, compare using == operator.
            if not (self._refAntennaNames[indx] == refAntennaNames[indx]):
                return False

        # axesOffset is a Length, compare using the almostEquals method.
        if not self._axesOffset.almostEquals(
            axesOffset, self.getTable().getAxesOffsetEqTolerance()
        ):
            return False

        # axesOffsetErr is a Length, compare using the almostEquals method.
        if not self._axesOffsetErr.almostEquals(
            axesOffsetErr, self.getTable().getAxesOffsetErrEqTolerance()
        ):
            return False

        # axesOffsetFixed is a bool, compare using the == operator.
        if not (self._axesOffsetFixed == axesOffsetFixed):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._positionOffset) != len(positionOffset):
            return False
        for indx in range(len(positionOffset)):

            # positionOffset is a list of Length, compare using the almostEquals method.
            if not self._positionOffset[indx].almostEquals(
                positionOffset[indx], self.getTable().getPositionOffsetEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._positionErr) != len(positionErr):
            return False
        for indx in range(len(positionErr)):

            # positionErr is a list of Length, compare using the almostEquals method.
            if not self._positionErr[indx].almostEquals(
                positionErr[indx], self.getTable().getPositionErrEqTolerance()
            ):
                return False

        # reducedChiSquared is a float, compare using the == operator.
        if not (self._reducedChiSquared == reducedChiSquared):
            return False

        return True


# initialize the dictionary that maps fields to init methods
CalPositionRow.initFromBinMethods()
