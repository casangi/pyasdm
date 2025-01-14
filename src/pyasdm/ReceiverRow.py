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
# File ReceiverRow.py
#

import pyasdm.ReceiverTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.ReceiverSideband import ReceiverSideband


from pyasdm.enumerations.NetSideband import NetSideband


from xml.dom import minidom

import copy


class ReceiverRow:
    """
    The ReceiverRow class is a row of a ReceiverTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a ReceiverRow.
        When row is None, create an empty row attached to table, which must be a ReceiverTable.
        When row is given, copy those values in to the new row. The row argument must be a ReceiverRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.ReceiverTable):
            raise ValueError("table must be a ReceiverTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._receiverId = 0

        self._timeInterval = ArrayTimeInterval()

        self._name = None

        self._numLO = 0

        self._frequencyBand = ReceiverBand.from_int(0)

        self._freqLO = []  # this is a list of Frequency []

        self._receiverSideband = ReceiverSideband.from_int(0)

        self._sidebandLO = []  # this is a list of NetSideband []

        # extrinsic attributes

        self._spectralWindowId = Tag()

        if row is not None:
            if not isinstance(row, ReceiverRow):
                raise ValueError("row must be a ReceiverRow")

            # copy constructor

            self._receiverId = row._receiverId

            self._spectralWindowId = Tag(row._spectralWindowId)

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._name = row._name

            self._numLO = row._numLO

            # We force the attribute of the result to be not None
            if row._frequencyBand is None:
                self._frequencyBand = ReceiverBand.from_int(0)
            else:
                self._frequencyBand = ReceiverBand(row._frequencyBand)

            # freqLO is a  list , make a deep copy
            self._freqLO = copy.deepcopy(row._freqLO)

            # We force the attribute of the result to be not None
            if row._receiverSideband is None:
                self._receiverSideband = ReceiverSideband.from_int(0)
            else:
                self._receiverSideband = ReceiverSideband(row._receiverSideband)

            # sidebandLO is a  list , make a deep copy
            self._sidebandLO = copy.deepcopy(row._sidebandLO)

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

        result += Parser.valueToXML("receiverId", self._receiverId)

        result += Parser.extendedValueToXML("timeInterval", self._timeInterval)

        result += Parser.valueToXML("name", self._name)

        result += Parser.valueToXML("numLO", self._numLO)

        result += Parser.valueToXML(
            "frequencyBand", ReceiverBand.name(self._frequencyBand)
        )

        result += Parser.listExtendedValueToXML("freqLO", self._freqLO)

        result += Parser.valueToXML(
            "receiverSideband", ReceiverSideband.name(self._receiverSideband)
        )

        result += Parser.listEnumValueToXML("sidebandLO", self._sidebandLO)

        # extrinsic attributes

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
                "xmlrow is not a string or a minidom.Element", "ReceiverTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "ReceiverTable")

        # intrinsic attribute values

        receiverIdNode = rowdom.getElementsByTagName("receiverId")[0]

        self._receiverId = int(receiverIdNode.firstChild.data.strip())

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        nameNode = rowdom.getElementsByTagName("name")[0]

        self._name = str(nameNode.firstChild.data.strip())

        numLONode = rowdom.getElementsByTagName("numLO")[0]

        self._numLO = int(numLONode.firstChild.data.strip())

        frequencyBandNode = rowdom.getElementsByTagName("frequencyBand")[0]

        self._frequencyBand = ReceiverBand.newReceiverBand(
            frequencyBandNode.firstChild.data.strip()
        )

        freqLONode = rowdom.getElementsByTagName("freqLO")[0]

        freqLOStr = freqLONode.firstChild.data.strip()

        self._freqLO = Parser.stringListToLists(freqLOStr, Frequency, "Receiver", True)

        receiverSidebandNode = rowdom.getElementsByTagName("receiverSideband")[0]

        self._receiverSideband = ReceiverSideband.newReceiverSideband(
            receiverSidebandNode.firstChild.data.strip()
        )

        sidebandLONode = rowdom.getElementsByTagName("sidebandLO")[0]

        sidebandLOStr = sidebandLONode.firstChild.data.strip()
        self._sidebandLO = Parser.stringListToLists(
            sidebandLOStr, NetSideband, "Receiver", False
        )

        # extrinsic attribute values

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")[0]

        self._spectralWindowId = Tag(spectralWindowIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        eos.writeInt(self._receiverId)

        self._spectralWindowId.toBin(eos)

        self._timeInterval.toBin(eos)

        eos.writeStr(self._name)

        eos.writeInt(self._numLO)

        eos.writeString(self._frequencyBand.toString())

        Frequency.listToBin(self._freqLO, eos)

        eos.writeString(self._receiverSideband.toString())

        eos.writeInt(len(self._sidebandLO))
        for i in range(len(self._sidebandLO)):

            eos.writeString(self._sidebandLO[i].toString())

    @staticmethod
    def receiverIdFromBin(row, eis):
        """
        Set the receiverId in row from the EndianInput (eis) instance.
        """

        row._receiverId = eis.readInt()

    @staticmethod
    def spectralWindowIdFromBin(row, eis):
        """
        Set the spectralWindowId in row from the EndianInput (eis) instance.
        """

        row._spectralWindowId = Tag.fromBin(eis)

    @staticmethod
    def timeIntervalFromBin(row, eis):
        """
        Set the timeInterval in row from the EndianInput (eis) instance.
        """

        row._timeInterval = ArrayTimeInterval.fromBin(eis)

    @staticmethod
    def nameFromBin(row, eis):
        """
        Set the name in row from the EndianInput (eis) instance.
        """

        row._name = eis.readStr()

    @staticmethod
    def numLOFromBin(row, eis):
        """
        Set the numLO in row from the EndianInput (eis) instance.
        """

        row._numLO = eis.readInt()

    @staticmethod
    def frequencyBandFromBin(row, eis):
        """
        Set the frequencyBand in row from the EndianInput (eis) instance.
        """

        row._frequencyBand = ReceiverBand.from_int(eis.readInt())

    @staticmethod
    def freqLOFromBin(row, eis):
        """
        Set the freqLO in row from the EndianInput (eis) instance.
        """

        row._freqLO = Frequency.from1DBin(eis)

    @staticmethod
    def receiverSidebandFromBin(row, eis):
        """
        Set the receiverSideband in row from the EndianInput (eis) instance.
        """

        row._receiverSideband = ReceiverSideband.from_int(eis.readInt())

    @staticmethod
    def sidebandLOFromBin(row, eis):
        """
        Set the sidebandLO in row from the EndianInput (eis) instance.
        """

        sidebandLODim1 = eis.readInt()
        thisList = []
        for i in range(sidebandLODim1):
            thisValue = NetSideband.from_int(eis.readInt())
            thisList.append(thisValue)
        row._sidebandLO = thisList

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["receiverId"] = ReceiverRow.receiverIdFromBin
        _fromBinMethods["spectralWindowId"] = ReceiverRow.spectralWindowIdFromBin
        _fromBinMethods["timeInterval"] = ReceiverRow.timeIntervalFromBin
        _fromBinMethods["name"] = ReceiverRow.nameFromBin
        _fromBinMethods["numLO"] = ReceiverRow.numLOFromBin
        _fromBinMethods["frequencyBand"] = ReceiverRow.frequencyBandFromBin
        _fromBinMethods["freqLO"] = ReceiverRow.freqLOFromBin
        _fromBinMethods["receiverSideband"] = ReceiverRow.receiverSidebandFromBin
        _fromBinMethods["sidebandLO"] = ReceiverRow.sidebandLOFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = ReceiverRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Receiver",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute receiverId

    _receiverId = 0

    def getReceiverId(self):
        """
        Get receiverId.
        return receiverId as int
        """

        return self._receiverId

    def setReceiverId(self, receiverId):
        """
        Set receiverId with the specified int value.
        receiverId The int value to which receiverId is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the receiverId field, which is part of the key, after this row has been added to this table."
            )

        self._receiverId = int(receiverId)

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

    # ===> Attribute name

    _name = None

    def getName(self):
        """
        Get name.
        return name as str
        """

        return self._name

    def setName(self, name):
        """
        Set name with the specified str value.
        name The str value to which name is to be set.


        """

        self._name = str(name)

    # ===> Attribute numLO

    _numLO = 0

    def getNumLO(self):
        """
        Get numLO.
        return numLO as int
        """

        return self._numLO

    def setNumLO(self, numLO):
        """
        Set numLO with the specified int value.
        numLO The int value to which numLO is to be set.


        """

        self._numLO = int(numLO)

    # ===> Attribute frequencyBand

    _frequencyBand = ReceiverBand.from_int(0)

    def getFrequencyBand(self):
        """
        Get frequencyBand.
        return frequencyBand as ReceiverBand
        """

        return self._frequencyBand

    def setFrequencyBand(self, frequencyBand):
        """
        Set frequencyBand with the specified ReceiverBand value.
        frequencyBand The ReceiverBand value to which frequencyBand is to be set.


        """

        self._frequencyBand = ReceiverBand(frequencyBand)

    # ===> Attribute freqLO

    _freqLO = None  # this is a 1D list of Frequency

    def getFreqLO(self):
        """
        Get freqLO.
        return freqLO as Frequency []
        """

        return copy.deepcopy(self._freqLO)

    def setFreqLO(self, freqLO):
        """
        Set freqLO with the specified Frequency []  value.
        freqLO The Frequency []  value to which freqLO is to be set.
        The value of freqLO can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(freqLO, list):
            raise ValueError("The value of freqLO must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(freqLO)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of freqLO is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(freqLO, Frequency):
                raise ValueError(
                    "type of the first value in freqLO is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._freqLO = copy.deepcopy(freqLO)
        except Exception as exc:
            raise ValueError("Invalid freqLO : " + str(exc))

    # ===> Attribute receiverSideband

    _receiverSideband = ReceiverSideband.from_int(0)

    def getReceiverSideband(self):
        """
        Get receiverSideband.
        return receiverSideband as ReceiverSideband
        """

        return self._receiverSideband

    def setReceiverSideband(self, receiverSideband):
        """
        Set receiverSideband with the specified ReceiverSideband value.
        receiverSideband The ReceiverSideband value to which receiverSideband is to be set.


        """

        self._receiverSideband = ReceiverSideband(receiverSideband)

    # ===> Attribute sidebandLO

    _sidebandLO = None  # this is a 1D list of NetSideband

    def getSidebandLO(self):
        """
        Get sidebandLO.
        return sidebandLO as NetSideband []
        """

        return copy.deepcopy(self._sidebandLO)

    def setSidebandLO(self, sidebandLO):
        """
        Set sidebandLO with the specified NetSideband []  value.
        sidebandLO The NetSideband []  value to which sidebandLO is to be set.


        """

        # value must be a list
        if not isinstance(sidebandLO, list):
            raise ValueError("The value of sidebandLO must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(sidebandLO)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of sidebandLO is not correct")

            # the type of the values in the list must be NetSideband
            # note : this only checks the first value found
            if not Parser.checkListType(sidebandLO, NetSideband):
                raise ValueError(
                    "type of the first value in sidebandLO is not NetSideband as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._sidebandLO = copy.deepcopy(sidebandLO)
        except Exception as exc:
            raise ValueError("Invalid sidebandLO : " + str(exc))

    # Extrinsic Table Attributes

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
        spectralWindowId,
        timeInterval,
        name,
        numLO,
        frequencyBand,
        freqLO,
        receiverSideband,
        sidebandLO,
    ):
        """
        Compare each attribute except the autoincrementable one of this ReceiverRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # spectralWindowId is a Tag, compare using the equals method.
        if not self._spectralWindowId.equals(spectralWindowId):
            return False

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # name is a str, compare using the == operator.
        if not (self._name == name):
            return False

        # numLO is a int, compare using the == operator.
        if not (self._numLO == numLO):
            return False

        # frequencyBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._frequencyBand.getValue() == frequencyBand.getValue()):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._freqLO) != len(freqLO):
            return False
        for indx in range(len(freqLO)):

            # freqLO is a list of Frequency, compare using the almostEquals method.
            if not self._freqLO[indx].almostEquals(
                freqLO[indx], self.getTable().getFreqLOEqTolerance()
            ):
                return False

        # receiverSideband is a ReceiverSideband, compare using the == operator on the getValue() output
        if not (self._receiverSideband.getValue() == receiverSideband.getValue()):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._sidebandLO) != len(sidebandLO):
            return False
        for indx in range(len(sidebandLO)):

            # sidebandLO is a list of NetSideband, compare using == operator.
            if not (self._sidebandLO[indx] == sidebandLO[indx]):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getName(),
            otherRow.getNumLO(),
            otherRow.getFrequencyBand(),
            otherRow.getFreqLO(),
            otherRow.getReceiverSideband(),
            otherRow.getSidebandLO(),
        )

    def compareRequiredValue(
        self, name, numLO, frequencyBand, freqLO, receiverSideband, sidebandLO
    ):

        # name is a str, compare using the == operator.
        if not (self._name == name):
            return False

        # numLO is a int, compare using the == operator.
        if not (self._numLO == numLO):
            return False

        # frequencyBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._frequencyBand.getValue() == frequencyBand.getValue()):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._freqLO) != len(freqLO):
            return False
        for indx in range(len(freqLO)):

            # freqLO is a list of Frequency, compare using the almostEquals method.
            if not self._freqLO[indx].almostEquals(
                freqLO[indx], self.getTable().getFreqLOEqTolerance()
            ):
                return False

        # receiverSideband is a ReceiverSideband, compare using the == operator on the getValue() output
        if not (self._receiverSideband.getValue() == receiverSideband.getValue()):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._sidebandLO) != len(sidebandLO):
            return False
        for indx in range(len(sidebandLO)):

            # sidebandLO is a list of NetSideband, compare using == operator.
            if not (self._sidebandLO[indx] == sidebandLO[indx]):
                return False

        return True


# initialize the dictionary that maps fields to init methods
ReceiverRow.initFromBinMethods()
