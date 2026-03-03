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
# File ModulationRow.py
#

import pyasdm.ModulationTable

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


class ModulationRow:
    """
    The ModulationRow class is a row of a ModulationTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a ModulationRow.
        When row is None, create an empty row attached to table, which must be a ModulationTable.
        When row is given, copy those values in to the new row. The row argument must be a ModulationRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.ModulationTable):
            raise ValueError("table must be a ModulationTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._receiverId = 0

        self._timeInterval = ArrayTimeInterval()

        self._localOscillatorOffset = Frequency()

        self._walsh180enabled = None

        self._walsh90enabled = None

        self._walsh180indexExists = False

        self._walsh180index = 0

        self._walsh90indexExists = False

        self._walsh90index = 0

        # extrinsic attributes

        self._antennaId = Tag()

        self._spectralWindowId = Tag()

        if row is not None:
            if not isinstance(row, ModulationRow):
                raise ValueError("row must be a ModulationRow")

            # copy constructor

            self._antennaId = Tag(row._antennaId)

            self._receiverId = row._receiverId

            self._spectralWindowId = Tag(row._spectralWindowId)

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._localOscillatorOffset = Frequency(row._localOscillatorOffset)

            self._walsh180enabled = row._walsh180enabled

            self._walsh90enabled = row._walsh90enabled

            # by default set systematically walsh180index's value to something not None

            if row._walsh180indexExists:

                self._walsh180index = row._walsh180index

                self._walsh180indexExists = True

            # by default set systematically walsh90index's value to something not None

            if row._walsh90indexExists:

                self._walsh90index = row._walsh90index

                self._walsh90indexExists = True

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

        result += Parser.extendedValueToXML(
            "localOscillatorOffset", self._localOscillatorOffset
        )

        result += Parser.valueToXML("walsh180enabled", self._walsh180enabled)

        result += Parser.valueToXML("walsh90enabled", self._walsh90enabled)

        if self._walsh180indexExists:

            result += Parser.valueToXML("walsh180index", self._walsh180index)

        if self._walsh90indexExists:

            result += Parser.valueToXML("walsh90index", self._walsh90index)

        # extrinsic attributes

        result += Parser.extendedValueToXML("antennaId", self._antennaId)

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
                "xmlrow is not a string or a minidom.Element", "ModulationTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "ModulationTable")

        # intrinsic attribute values

        receiverIdNode = rowdom.getElementsByTagName("receiverId")[0]

        self._receiverId = int(receiverIdNode.firstChild.data.strip())

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        localOscillatorOffsetNode = rowdom.getElementsByTagName(
            "localOscillatorOffset"
        )[0]

        self._localOscillatorOffset = Frequency(
            localOscillatorOffsetNode.firstChild.data.strip()
        )

        walsh180enabledNode = rowdom.getElementsByTagName("walsh180enabled")[0]

        self._walsh180enabled = bool(walsh180enabledNode.firstChild.data.strip())

        walsh90enabledNode = rowdom.getElementsByTagName("walsh90enabled")[0]

        self._walsh90enabled = bool(walsh90enabledNode.firstChild.data.strip())

        walsh180indexNode = rowdom.getElementsByTagName("walsh180index")
        if len(walsh180indexNode) > 0:

            self._walsh180index = int(walsh180indexNode[0].firstChild.data.strip())

            self._walsh180indexExists = True

        walsh90indexNode = rowdom.getElementsByTagName("walsh90index")
        if len(walsh90indexNode) > 0:

            self._walsh90index = int(walsh90indexNode[0].firstChild.data.strip())

            self._walsh90indexExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        self._antennaId = Tag(antennaIdNode.firstChild.data.strip())

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")[0]

        self._spectralWindowId = Tag(spectralWindowIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._antennaId.toBin(eos)

        eos.writeInt(self._receiverId)

        self._spectralWindowId.toBin(eos)

        self._timeInterval.toBin(eos)

        self._localOscillatorOffset.toBin(eos)

        eos.writeBool(self._walsh180enabled)

        eos.writeBool(self._walsh90enabled)

        eos.writeBool(self._walsh180indexExists)
        if self._walsh180indexExists:

            eos.writeInt(self._walsh180index)

        eos.writeBool(self._walsh90indexExists)
        if self._walsh90indexExists:

            eos.writeInt(self._walsh90index)

    @staticmethod
    def antennaIdFromBin(row, eis):
        """
        Set the antennaId in row from the EndianInput (eis) instance.
        """

        row._antennaId = Tag.fromBin(eis)

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
    def localOscillatorOffsetFromBin(row, eis):
        """
        Set the localOscillatorOffset in row from the EndianInput (eis) instance.
        """

        row._localOscillatorOffset = Frequency.fromBin(eis)

    @staticmethod
    def walsh180enabledFromBin(row, eis):
        """
        Set the walsh180enabled in row from the EndianInput (eis) instance.
        """

        row._walsh180enabled = eis.readBool()

    @staticmethod
    def walsh90enabledFromBin(row, eis):
        """
        Set the walsh90enabled in row from the EndianInput (eis) instance.
        """

        row._walsh90enabled = eis.readBool()

    @staticmethod
    def walsh180indexFromBin(row, eis):
        """
        Set the optional walsh180index in row from the EndianInput (eis) instance.
        """
        row._walsh180indexExists = eis.readBool()
        if row._walsh180indexExists:

            row._walsh180index = eis.readInt()

    @staticmethod
    def walsh90indexFromBin(row, eis):
        """
        Set the optional walsh90index in row from the EndianInput (eis) instance.
        """
        row._walsh90indexExists = eis.readBool()
        if row._walsh90indexExists:

            row._walsh90index = eis.readInt()

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaId"] = ModulationRow.antennaIdFromBin
        _fromBinMethods["receiverId"] = ModulationRow.receiverIdFromBin
        _fromBinMethods["spectralWindowId"] = ModulationRow.spectralWindowIdFromBin
        _fromBinMethods["timeInterval"] = ModulationRow.timeIntervalFromBin
        _fromBinMethods["localOscillatorOffset"] = (
            ModulationRow.localOscillatorOffsetFromBin
        )
        _fromBinMethods["walsh180enabled"] = ModulationRow.walsh180enabledFromBin
        _fromBinMethods["walsh90enabled"] = ModulationRow.walsh90enabledFromBin

        _fromBinMethods["walsh180index"] = ModulationRow.walsh180indexFromBin
        _fromBinMethods["walsh90index"] = ModulationRow.walsh90indexFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = ModulationRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Modulation",
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

    # ===> Attribute localOscillatorOffset

    _localOscillatorOffset = Frequency()

    def getLocalOscillatorOffset(self):
        """
        Get localOscillatorOffset.
        return localOscillatorOffset as Frequency
        """

        # make sure it is a copy of Frequency
        return Frequency(self._localOscillatorOffset)

    def setLocalOscillatorOffset(self, localOscillatorOffset):
        """
        Set localOscillatorOffset with the specified Frequency value.
        localOscillatorOffset The Frequency value to which localOscillatorOffset is to be set.
        The value of localOscillatorOffset can be anything allowed by the Frequency constructor.

        """

        self._localOscillatorOffset = Frequency(localOscillatorOffset)

    # ===> Attribute walsh180enabled

    _walsh180enabled = None

    def getWalsh180enabled(self):
        """
        Get walsh180enabled.
        return walsh180enabled as bool
        """

        return self._walsh180enabled

    def setWalsh180enabled(self, walsh180enabled):
        """
        Set walsh180enabled with the specified bool value.
        walsh180enabled The bool value to which walsh180enabled is to be set.


        """

        self._walsh180enabled = bool(walsh180enabled)

    # ===> Attribute walsh90enabled

    _walsh90enabled = None

    def getWalsh90enabled(self):
        """
        Get walsh90enabled.
        return walsh90enabled as bool
        """

        return self._walsh90enabled

    def setWalsh90enabled(self, walsh90enabled):
        """
        Set walsh90enabled with the specified bool value.
        walsh90enabled The bool value to which walsh90enabled is to be set.


        """

        self._walsh90enabled = bool(walsh90enabled)

    # ===> Attribute walsh180index, which is optional
    _walsh180indexExists = False

    _walsh180index = 0

    def isWalsh180indexExists(self):
        """
        The attribute walsh180index is optional. Return True if this attribute exists.
        return True if and only if the walsh180index attribute exists.
        """
        return self._walsh180indexExists

    def getWalsh180index(self):
        """
        Get walsh180index, which is optional.
        return walsh180index as int
        raises ValueError If walsh180index does not exist.
        """
        if not self._walsh180indexExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + "'walsh180index' attribute in table Modulation does not exist!"
            )

        return self._walsh180index

    def setWalsh180index(self, walsh180index):
        """
        Set walsh180index with the specified int value.
        walsh180index The int value to which walsh180index is to be set.


        """

        self._walsh180index = int(walsh180index)

        self._walsh180indexExists = True

    def clearWalsh180index(self):
        """
        Mark walsh180index, which is an optional field, as non-existent.
        """
        self._walsh180indexExists = False

    # ===> Attribute walsh90index, which is optional
    _walsh90indexExists = False

    _walsh90index = 0

    def isWalsh90indexExists(self):
        """
        The attribute walsh90index is optional. Return True if this attribute exists.
        return True if and only if the walsh90index attribute exists.
        """
        return self._walsh90indexExists

    def getWalsh90index(self):
        """
        Get walsh90index, which is optional.
        return walsh90index as int
        raises ValueError If walsh90index does not exist.
        """
        if not self._walsh90indexExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + "'walsh90index' attribute in table Modulation does not exist!"
            )

        return self._walsh90index

    def setWalsh90index(self, walsh90index):
        """
        Set walsh90index with the specified int value.
        walsh90index The int value to which walsh90index is to be set.


        """

        self._walsh90index = int(walsh90index)

        self._walsh90indexExists = True

    def clearWalsh90index(self):
        """
        Mark walsh90index, which is an optional field, as non-existent.
        """
        self._walsh90indexExists = False

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

    # comparison methods

    def compareNoAutoInc(
        self,
        antennaId,
        receiverId,
        spectralWindowId,
        timeInterval,
        localOscillatorOffset,
        walsh180enabled,
        walsh90enabled,
    ):
        """
        Compare each attribute except the autoincrementable one of this ModulationRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaId is a Tag, compare using the equals method.
        if not self._antennaId.equals(antennaId):
            return False

        # receiverId is a int, compare using the == operator.
        if not (self._receiverId == receiverId):
            return False

        # spectralWindowId is a Tag, compare using the equals method.
        if not self._spectralWindowId.equals(spectralWindowId):
            return False

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # localOscillatorOffset is a Frequency, compare using the almostEquals method.
        if not self._localOscillatorOffset.almostEquals(
            localOscillatorOffset, self.getTable().getLocalOscillatorOffsetEqTolerance()
        ):
            return False

        # walsh180enabled is a bool, compare using the == operator.
        if not (self._walsh180enabled == walsh180enabled):
            return False

        # walsh90enabled is a bool, compare using the == operator.
        if not (self._walsh90enabled == walsh90enabled):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getLocalOscillatorOffset(),
            otherRow.getWalsh180enabled(),
            otherRow.getWalsh90enabled(),
        )

    def compareRequiredValue(
        self, localOscillatorOffset, walsh180enabled, walsh90enabled
    ):

        # localOscillatorOffset is a Frequency, compare using the almostEquals method.
        if not self._localOscillatorOffset.almostEquals(
            localOscillatorOffset, self.getTable().getLocalOscillatorOffsetEqTolerance()
        ):
            return False

        # walsh180enabled is a bool, compare using the == operator.
        if not (self._walsh180enabled == walsh180enabled):
            return False

        # walsh90enabled is a bool, compare using the == operator.
        if not (self._walsh90enabled == walsh90enabled):
            return False

        return True


# initialize the dictionary that maps fields to init methods
ModulationRow.initFromBinMethods()
