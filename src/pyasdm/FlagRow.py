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
# File FlagRow.py
#

import pyasdm.FlagTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.PolarizationType import PolarizationType


from xml.dom import minidom

import copy


class FlagRow:
    """
    The FlagRow class is a row of a FlagTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a FlagRow.
        When row is None, create an empty row attached to table, which must be a FlagTable.
        When row is given, copy those values in to the new row. The row argument must be a FlagRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.FlagTable):
            raise ValueError("table must be a FlagTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._flagId = Tag()

        self._startTime = ArrayTime()

        self._endTime = ArrayTime()

        self._reason = None

        self._numAntenna = 0

        self._numPolarizationTypeExists = False

        self._numPolarizationType = 0

        self._numSpectralWindowExists = False

        self._numSpectralWindow = 0

        self._numPairedAntennaExists = False

        self._numPairedAntenna = 0

        self._numChanExists = False

        self._numChan = 0

        self._polarizationTypeExists = False

        self._polarizationType = []  # this is a list of PolarizationType []

        self._channelExists = False

        self._channel = []  # this is a list of int []  []

        # extrinsic attributes

        self._antennaId = []  # this is a list of Tag []

        self._pairedAntennaIdExists = False

        self._pairedAntennaId = []  # this is a list of Tag []

        self._spectralWindowIdExists = False

        self._spectralWindowId = []  # this is a list of Tag []

        if row is not None:
            if not isinstance(row, FlagRow):
                raise ValueError("row must be a FlagRow")

            # copy constructor

            self._flagId = Tag(row._flagId)

            self._startTime = ArrayTime(row._startTime)

            self._endTime = ArrayTime(row._endTime)

            self._reason = row._reason

            self._numAntenna = row._numAntenna

            # antennaId is a list, let's populate self._antennaId element by element.
            if self._antennaId is None:
                self._antennaId = []

            for i in range(len(row._antennaId)):

                self._antennaId.append(Tag(row._antennaId[i]))

            # by default set systematically numPolarizationType's value to something not None

            if row._numPolarizationTypeExists:

                self._numPolarizationType = row._numPolarizationType

                self._numPolarizationTypeExists = True

            # by default set systematically numSpectralWindow's value to something not None

            if row._numSpectralWindowExists:

                self._numSpectralWindow = row._numSpectralWindow

                self._numSpectralWindowExists = True

            # by default set systematically numPairedAntenna's value to something not None

            if row._numPairedAntennaExists:

                self._numPairedAntenna = row._numPairedAntenna

                self._numPairedAntennaExists = True

            # by default set systematically numChan's value to something not None

            if row._numChanExists:

                self._numChan = row._numChan

                self._numChanExists = True

            # by default set systematically polarizationType's value to something not None

            if row._polarizationTypeExists:

                # polarizationType is a list, make a deep copy
                self.polarizationType = copy.deepcopy(row.polarizationType)

                self._polarizationTypeExists = True

            # by default set systematically channel's value to something not None

            if row._channelExists:

                # channel is a list, make a deep copy
                self.channel = copy.deepcopy(row.channel)

                self._channelExists = True

            # by default set systematically pairedAntennaId's value to something not None

            if row._pairedAntennaIdExists:

                # pairedAntennaId is a list, let's populate self._pairedAntennaId element by element.
                if self._pairedAntennaId is None:
                    self._pairedAntennaId = []
                for i in range(len(row._pairedAntennaId)):

                    self._pairedAntennaId.append(Tag(row._pairedAntennaId[i]))

                self._pairedAntennaIdExists = True

            # by default set systematically spectralWindowId's value to something not None

            if row._spectralWindowIdExists:

                # spectralWindowId is a list, let's populate self._spectralWindowId element by element.
                if self._spectralWindowId is None:
                    self._spectralWindowId = []
                for i in range(len(row._spectralWindowId)):

                    self._spectralWindowId.append(Tag(row._spectralWindowId[i]))

                self._spectralWindowIdExists = True

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

        result += Parser.extendedValueToXML("flagId", self._flagId)

        result += Parser.extendedValueToXML("startTime", self._startTime)

        result += Parser.extendedValueToXML("endTime", self._endTime)

        result += Parser.valueToXML("reason", self._reason)

        result += Parser.valueToXML("numAntenna", self._numAntenna)

        if self._numPolarizationTypeExists:

            result += Parser.valueToXML(
                "numPolarizationType", self._numPolarizationType
            )

        if self._numSpectralWindowExists:

            result += Parser.valueToXML("numSpectralWindow", self._numSpectralWindow)

        if self._numPairedAntennaExists:

            result += Parser.valueToXML("numPairedAntenna", self._numPairedAntenna)

        if self._numChanExists:

            result += Parser.valueToXML("numChan", self._numChan)

        if self._polarizationTypeExists:

            result += Parser.listEnumValueToXML(
                "polarizationType", self._polarizationType
            )

        if self._channelExists:

            result += Parser.listValueToXML("channel", self._channel)

        # extrinsic attributes

        result += Parser.listExtendedValueToXML("antennaId", self._antennaId)

        if self._pairedAntennaIdExists:

            result += Parser.listExtendedValueToXML(
                "pairedAntennaId", self._pairedAntennaId
            )

        if self._spectralWindowIdExists:

            result += Parser.listExtendedValueToXML(
                "spectralWindowId", self._spectralWindowId
            )

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
                "xmlrow is not a string or a minidom.Element", "FlagTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "FlagTable")

        # intrinsic attribute values

        flagIdNode = rowdom.getElementsByTagName("flagId")[0]

        self._flagId = Tag(flagIdNode.firstChild.data.strip())

        startTimeNode = rowdom.getElementsByTagName("startTime")[0]

        self._startTime = ArrayTime(startTimeNode.firstChild.data.strip())

        endTimeNode = rowdom.getElementsByTagName("endTime")[0]

        self._endTime = ArrayTime(endTimeNode.firstChild.data.strip())

        reasonNode = rowdom.getElementsByTagName("reason")[0]

        self._reason = str(reasonNode.firstChild.data.strip())

        numAntennaNode = rowdom.getElementsByTagName("numAntenna")[0]

        self._numAntenna = int(numAntennaNode.firstChild.data.strip())

        numPolarizationTypeNode = rowdom.getElementsByTagName("numPolarizationType")
        if len(numPolarizationTypeNode) > 0:

            self._numPolarizationType = int(
                numPolarizationTypeNode[0].firstChild.data.strip()
            )

            self._numPolarizationTypeExists = True

        numSpectralWindowNode = rowdom.getElementsByTagName("numSpectralWindow")
        if len(numSpectralWindowNode) > 0:

            self._numSpectralWindow = int(
                numSpectralWindowNode[0].firstChild.data.strip()
            )

            self._numSpectralWindowExists = True

        numPairedAntennaNode = rowdom.getElementsByTagName("numPairedAntenna")
        if len(numPairedAntennaNode) > 0:

            self._numPairedAntenna = int(
                numPairedAntennaNode[0].firstChild.data.strip()
            )

            self._numPairedAntennaExists = True

        numChanNode = rowdom.getElementsByTagName("numChan")
        if len(numChanNode) > 0:

            self._numChan = int(numChanNode[0].firstChild.data.strip())

            self._numChanExists = True

        polarizationTypeNode = rowdom.getElementsByTagName("polarizationType")
        if len(polarizationTypeNode) > 0:

            polarizationTypeStr = polarizationTypeNode[0].firstChild.data.strip()
            self._polarizationType = Parser.stringListToLists(
                polarizationTypeStr, PolarizationType, "Flag", False
            )

            self._polarizationTypeExists = True

        channelNode = rowdom.getElementsByTagName("channel")
        if len(channelNode) > 0:

            channelStr = channelNode[0].firstChild.data.strip()

            self._channel = Parser.stringListToLists(channelStr, int, "Flag", False)

            self._channelExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        antennaIdStr = antennaIdNode.firstChild.data.strip()

        self._antennaId = Parser.stringListToLists(antennaIdStr, Tag, "Flag", True)

        pairedAntennaIdNode = rowdom.getElementsByTagName("pairedAntennaId")
        if len(pairedAntennaIdNode) > 0:

            pairedAntennaIdStr = pairedAntennaIdNode[0].firstChild.data.strip()

            self._pairedAntennaId = Parser.stringListToLists(
                pairedAntennaIdStr, Tag, "Flag", True
            )

            self._pairedAntennaIdExists = True

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")
        if len(spectralWindowIdNode) > 0:

            spectralWindowIdStr = spectralWindowIdNode[0].firstChild.data.strip()

            self._spectralWindowId = Parser.stringListToLists(
                spectralWindowIdStr, Tag, "Flag", True
            )

            self._spectralWindowIdExists = True

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._flagId.toBin(eos)

        self._startTime.toBin(eos)

        self._endTime.toBin(eos)

        eos.writeStr(self._reason)

        eos.writeInt(self._numAntenna)

        Tag.listToBin(self._antennaId, eos)

        eos.writeBool(self._numPolarizationTypeExists)
        if self._numPolarizationTypeExists:

            eos.writeInt(self._numPolarizationType)

        eos.writeBool(self._numSpectralWindowExists)
        if self._numSpectralWindowExists:

            eos.writeInt(self._numSpectralWindow)

        eos.writeBool(self._numPairedAntennaExists)
        if self._numPairedAntennaExists:

            eos.writeInt(self._numPairedAntenna)

        eos.writeBool(self._numChanExists)
        if self._numChanExists:

            eos.writeInt(self._numChan)

        eos.writeBool(self._polarizationTypeExists)
        if self._polarizationTypeExists:

            eos.writeInt(len(self._polarizationType))
            for i in range(len(self._polarizationType)):

                eos.writeString(self._polarizationType[i].toString())

        eos.writeBool(self._channelExists)
        if self._channelExists:

            # null array case, unsure if this is possible but this should work
            if self._channel is None:
                eos.writeInt(0)
                eos.writeInt(0)
            else:
                channel_dims = Parser.getListDims(self._channel)
            # assumes it really is 2D
            eos.writeInt(channel_dims[0])
            eos.writeInt(channel_dims[1])
            for i in range(channel_dims[0]):
                for j in range(channel_dims[1]):
                    eos.writeInt(self._channel[i][j])

        eos.writeBool(self._pairedAntennaIdExists)
        if self._pairedAntennaIdExists:

            Tag.listToBin(self._pairedAntennaId, eos)

        eos.writeBool(self._spectralWindowIdExists)
        if self._spectralWindowIdExists:

            Tag.listToBin(self._spectralWindowId, eos)

    @staticmethod
    def flagIdFromBin(row, eis):
        """
        Set the flagId in row from the EndianInput (eis) instance.
        """

        row._flagId = Tag.fromBin(eis)

    @staticmethod
    def startTimeFromBin(row, eis):
        """
        Set the startTime in row from the EndianInput (eis) instance.
        """

        row._startTime = ArrayTime.fromBin(eis)

    @staticmethod
    def endTimeFromBin(row, eis):
        """
        Set the endTime in row from the EndianInput (eis) instance.
        """

        row._endTime = ArrayTime.fromBin(eis)

    @staticmethod
    def reasonFromBin(row, eis):
        """
        Set the reason in row from the EndianInput (eis) instance.
        """

        row._reason = eis.readStr()

    @staticmethod
    def numAntennaFromBin(row, eis):
        """
        Set the numAntenna in row from the EndianInput (eis) instance.
        """

        row._numAntenna = eis.readInt()

    @staticmethod
    def antennaIdFromBin(row, eis):
        """
        Set the antennaId in row from the EndianInput (eis) instance.
        """

        row._antennaId = Tag.from1DBin(eis)

    @staticmethod
    def numPolarizationTypeFromBin(row, eis):
        """
        Set the optional numPolarizationType in row from the EndianInput (eis) instance.
        """
        row._numPolarizationTypeExists = eis.readBool()
        if row._numPolarizationTypeExists:

            row._numPolarizationType = eis.readInt()

    @staticmethod
    def numSpectralWindowFromBin(row, eis):
        """
        Set the optional numSpectralWindow in row from the EndianInput (eis) instance.
        """
        row._numSpectralWindowExists = eis.readBool()
        if row._numSpectralWindowExists:

            row._numSpectralWindow = eis.readInt()

    @staticmethod
    def numPairedAntennaFromBin(row, eis):
        """
        Set the optional numPairedAntenna in row from the EndianInput (eis) instance.
        """
        row._numPairedAntennaExists = eis.readBool()
        if row._numPairedAntennaExists:

            row._numPairedAntenna = eis.readInt()

    @staticmethod
    def numChanFromBin(row, eis):
        """
        Set the optional numChan in row from the EndianInput (eis) instance.
        """
        row._numChanExists = eis.readBool()
        if row._numChanExists:

            row._numChan = eis.readInt()

    @staticmethod
    def polarizationTypeFromBin(row, eis):
        """
        Set the optional polarizationType in row from the EndianInput (eis) instance.
        """
        row._polarizationTypeExists = eis.readBool()
        if row._polarizationTypeExists:

            polarizationTypeDim1 = eis.readInt()
            thisList = []
            for i in range(polarizationTypeDim1):
                thisValue = PolarizationType.from_int(eis.readInt())
                thisList.append(thisValue)
            row._polarizationType = thisList

    @staticmethod
    def channelFromBin(row, eis):
        """
        Set the optional channel in row from the EndianInput (eis) instance.
        """
        row._channelExists = eis.readBool()
        if row._channelExists:

            channelDim1 = eis.readInt()
            channelDim2 = eis.readInt()
            thisList = []
            for i in range(channelDim1):
                thisList_j = []
                for j in range(channelDim2):
                    thisValue = eis.readInt()
                    thisList_j.append(thisValue)
                thisList.append(thisList_j)
            row.channel = thisList

    @staticmethod
    def pairedAntennaIdFromBin(row, eis):
        """
        Set the optional pairedAntennaId in row from the EndianInput (eis) instance.
        """
        row._pairedAntennaIdExists = eis.readBool()
        if row._pairedAntennaIdExists:

            row._pairedAntennaId = Tag.from1DBin(eis)

    @staticmethod
    def spectralWindowIdFromBin(row, eis):
        """
        Set the optional spectralWindowId in row from the EndianInput (eis) instance.
        """
        row._spectralWindowIdExists = eis.readBool()
        if row._spectralWindowIdExists:

            row._spectralWindowId = Tag.from1DBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["flagId"] = FlagRow.flagIdFromBin
        _fromBinMethods["startTime"] = FlagRow.startTimeFromBin
        _fromBinMethods["endTime"] = FlagRow.endTimeFromBin
        _fromBinMethods["reason"] = FlagRow.reasonFromBin
        _fromBinMethods["numAntenna"] = FlagRow.numAntennaFromBin
        _fromBinMethods["antennaId"] = FlagRow.antennaIdFromBin

        _fromBinMethods["numPolarizationType"] = FlagRow.numPolarizationTypeFromBin
        _fromBinMethods["numSpectralWindow"] = FlagRow.numSpectralWindowFromBin
        _fromBinMethods["numPairedAntenna"] = FlagRow.numPairedAntennaFromBin
        _fromBinMethods["numChan"] = FlagRow.numChanFromBin
        _fromBinMethods["polarizationType"] = FlagRow.polarizationTypeFromBin
        _fromBinMethods["channel"] = FlagRow.channelFromBin
        _fromBinMethods["pairedAntennaId"] = FlagRow.pairedAntennaIdFromBin
        _fromBinMethods["spectralWindowId"] = FlagRow.spectralWindowIdFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = FlagRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Flag",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute flagId

    _flagId = Tag()

    def getFlagId(self):
        """
        Get flagId.
        return flagId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._flagId)

    def setFlagId(self, flagId):
        """
        Set flagId with the specified Tag value.
        flagId The Tag value to which flagId is to be set.
        The value of flagId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the flagId field, which is part of the key, after this row has been added to this table."
            )

        self._flagId = Tag(flagId)

    # ===> Attribute startTime

    _startTime = ArrayTime()

    def getStartTime(self):
        """
        Get startTime.
        return startTime as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._startTime)

    def setStartTime(self, startTime):
        """
        Set startTime with the specified ArrayTime value.
        startTime The ArrayTime value to which startTime is to be set.
        The value of startTime can be anything allowed by the ArrayTime constructor.

        """

        self._startTime = ArrayTime(startTime)

    # ===> Attribute endTime

    _endTime = ArrayTime()

    def getEndTime(self):
        """
        Get endTime.
        return endTime as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._endTime)

    def setEndTime(self, endTime):
        """
        Set endTime with the specified ArrayTime value.
        endTime The ArrayTime value to which endTime is to be set.
        The value of endTime can be anything allowed by the ArrayTime constructor.

        """

        self._endTime = ArrayTime(endTime)

    # ===> Attribute reason

    _reason = None

    def getReason(self):
        """
        Get reason.
        return reason as str
        """

        return self._reason

    def setReason(self, reason):
        """
        Set reason with the specified str value.
        reason The str value to which reason is to be set.


        """

        self._reason = str(reason)

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
                + numPolarizationType
                + " attribute in table Flag does not exist!"
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
                + " attribute in table Flag does not exist!"
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

    # ===> Attribute numPairedAntenna, which is optional
    _numPairedAntennaExists = False

    _numPairedAntenna = 0

    def isNumPairedAntennaExists(self):
        """
        The attribute numPairedAntenna is optional. Return True if this attribute exists.
        return True if and only if the numPairedAntenna attribute exists.
        """
        return self._numPairedAntennaExists

    def getNumPairedAntenna(self):
        """
        Get numPairedAntenna, which is optional.
        return numPairedAntenna as int
        raises ValueError If numPairedAntenna does not exist.
        """
        if not self._numPairedAntennaExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numPairedAntenna
                + " attribute in table Flag does not exist!"
            )

        return self._numPairedAntenna

    def setNumPairedAntenna(self, numPairedAntenna):
        """
        Set numPairedAntenna with the specified int value.
        numPairedAntenna The int value to which numPairedAntenna is to be set.


        """

        self._numPairedAntenna = int(numPairedAntenna)

        self._numPairedAntennaExists = True

    def clearNumPairedAntenna(self):
        """
        Mark numPairedAntenna, which is an optional field, as non-existent.
        """
        self._numPairedAntennaExists = False

    # ===> Attribute numChan, which is optional
    _numChanExists = False

    _numChan = 0

    def isNumChanExists(self):
        """
        The attribute numChan is optional. Return True if this attribute exists.
        return True if and only if the numChan attribute exists.
        """
        return self._numChanExists

    def getNumChan(self):
        """
        Get numChan, which is optional.
        return numChan as int
        raises ValueError If numChan does not exist.
        """
        if not self._numChanExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numChan
                + " attribute in table Flag does not exist!"
            )

        return self._numChan

    def setNumChan(self, numChan):
        """
        Set numChan with the specified int value.
        numChan The int value to which numChan is to be set.


        """

        self._numChan = int(numChan)

        self._numChanExists = True

    def clearNumChan(self):
        """
        Mark numChan, which is an optional field, as non-existent.
        """
        self._numChanExists = False

    # ===> Attribute polarizationType, which is optional
    _polarizationTypeExists = False

    _polarizationType = None  # this is a 1D list of PolarizationType

    def isPolarizationTypeExists(self):
        """
        The attribute polarizationType is optional. Return True if this attribute exists.
        return True if and only if the polarizationType attribute exists.
        """
        return self._polarizationTypeExists

    def getPolarizationType(self):
        """
        Get polarizationType, which is optional.
        return polarizationType as PolarizationType []
        raises ValueError If polarizationType does not exist.
        """
        if not self._polarizationTypeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + polarizationType
                + " attribute in table Flag does not exist!"
            )

        return copy.deepcopy(self._polarizationType)

    def setPolarizationType(self, polarizationType):
        """
        Set polarizationType with the specified PolarizationType []  value.
        polarizationType The PolarizationType []  value to which polarizationType is to be set.


        """

        # value must be a list
        if not isinstance(polarizationType, list):
            raise ValueError("The value of polarizationType must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(polarizationType)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of polarizationType is not correct")

            # the type of the values in the list must be PolarizationType
            # note : this only checks the first value found
            if not Parser.checkListType(polarizationType, PolarizationType):
                raise ValueError(
                    "type of the first value in polarizationType is not PolarizationType as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._polarizationType = copy.deepcopy(polarizationType)
        except Exception as exc:
            raise ValueError("Invalid polarizationType : " + str(exc))

        self._polarizationTypeExists = True

    def clearPolarizationType(self):
        """
        Mark polarizationType, which is an optional field, as non-existent.
        """
        self._polarizationTypeExists = False

    # ===> Attribute channel, which is optional
    _channelExists = False

    _channel = None  # this is a 2D list of int

    def isChannelExists(self):
        """
        The attribute channel is optional. Return True if this attribute exists.
        return True if and only if the channel attribute exists.
        """
        return self._channelExists

    def getChannel(self):
        """
        Get channel, which is optional.
        return channel as int []  []
        raises ValueError If channel does not exist.
        """
        if not self._channelExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + channel
                + " attribute in table Flag does not exist!"
            )

        return copy.deepcopy(self._channel)

    def setChannel(self, channel):
        """
        Set channel with the specified int []  []  value.
        channel The int []  []  value to which channel is to be set.


        """

        # value must be a list
        if not isinstance(channel, list):
            raise ValueError("The value of channel must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(channel)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of channel is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not Parser.checkListType(channel, int):
                raise ValueError(
                    "type of the first value in channel is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._channel = copy.deepcopy(channel)
        except Exception as exc:
            raise ValueError("Invalid channel : " + str(exc))

        self._channelExists = True

    def clearChannel(self):
        """
        Mark channel, which is an optional field, as non-existent.
        """
        self._channelExists = False

    # Extrinsic Table Attributes

    # ===> Attribute antennaId

    _antennaId = []  # this is a list of Tag []

    def getAntennaId(self):
        """
        Get antennaId.
        return antennaId as Tag []
        """

        return copy.deepcopy(self._antennaId)

    def setAntennaId(self, antennaId):
        """
        Set antennaId with the specified Tag []  value.
        antennaId The Tag []  value to which antennaId is to be set.
        The value of antennaId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(antennaId, list):
            raise ValueError("The value of antennaId must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(antennaId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of antennaId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not Parser.checkListType(antennaId, Tag):
                raise ValueError(
                    "type of the first value in antennaId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._antennaId = copy.deepcopy(antennaId)
        except Exception as exc:
            raise ValueError("Invalid antennaId : " + str(exc))

    # ===> Attribute pairedAntennaId, which is optional
    _pairedAntennaIdExists = False

    _pairedAntennaId = []  # this is a list of Tag []

    def isPairedAntennaIdExists(self):
        """
        The attribute pairedAntennaId is optional. Return True if this attribute exists.
        return True if and only if the pairedAntennaId attribute exists.
        """
        return self._pairedAntennaIdExists

    def getPairedAntennaId(self):
        """
        Get pairedAntennaId, which is optional.
        return pairedAntennaId as Tag []
        raises ValueError If pairedAntennaId does not exist.
        """
        if not self._pairedAntennaIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + pairedAntennaId
                + " attribute in table Flag does not exist!"
            )

        return copy.deepcopy(self._pairedAntennaId)

    def setPairedAntennaId(self, pairedAntennaId):
        """
        Set pairedAntennaId with the specified Tag []  value.
        pairedAntennaId The Tag []  value to which pairedAntennaId is to be set.
        The value of pairedAntennaId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(pairedAntennaId, list):
            raise ValueError("The value of pairedAntennaId must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(pairedAntennaId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of pairedAntennaId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not Parser.checkListType(pairedAntennaId, Tag):
                raise ValueError(
                    "type of the first value in pairedAntennaId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._pairedAntennaId = copy.deepcopy(pairedAntennaId)
        except Exception as exc:
            raise ValueError("Invalid pairedAntennaId : " + str(exc))

        self._pairedAntennaIdExists = True

    def clearPairedAntennaId(self):
        """
        Mark pairedAntennaId, which is an optional field, as non-existent.
        """
        self._pairedAntennaIdExists = False

    # ===> Attribute spectralWindowId, which is optional
    _spectralWindowIdExists = False

    _spectralWindowId = []  # this is a list of Tag []

    def isSpectralWindowIdExists(self):
        """
        The attribute spectralWindowId is optional. Return True if this attribute exists.
        return True if and only if the spectralWindowId attribute exists.
        """
        return self._spectralWindowIdExists

    def getSpectralWindowId(self):
        """
        Get spectralWindowId, which is optional.
        return spectralWindowId as Tag []
        raises ValueError If spectralWindowId does not exist.
        """
        if not self._spectralWindowIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + spectralWindowId
                + " attribute in table Flag does not exist!"
            )

        return copy.deepcopy(self._spectralWindowId)

    def setSpectralWindowId(self, spectralWindowId):
        """
        Set spectralWindowId with the specified Tag []  value.
        spectralWindowId The Tag []  value to which spectralWindowId is to be set.
        The value of spectralWindowId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(spectralWindowId, list):
            raise ValueError("The value of spectralWindowId must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(spectralWindowId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of spectralWindowId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not Parser.checkListType(spectralWindowId, Tag):
                raise ValueError(
                    "type of the first value in spectralWindowId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._spectralWindowId = copy.deepcopy(spectralWindowId)
        except Exception as exc:
            raise ValueError("Invalid spectralWindowId : " + str(exc))

        self._spectralWindowIdExists = True

    def clearSpectralWindowId(self):
        """
        Mark spectralWindowId, which is an optional field, as non-existent.
        """
        self._spectralWindowIdExists = False

    # Links

    def setOneAntennaId(self, index, antennaId):
        """
        Set antennaId[index] with the specified Tag value.
        index The index in antennaId where to set the Tag value.
        antennaId The Tag value to which antennaId[index] is to be set.

        """

        self._antennaId[index] = Tag(antennaId)

    # ===> hasmany link from a row of Flag table to many rows of Antenna table.

    def addAntennaId(self, id):
        """
        Append a Tag to antennaId
        id the Tag to be appended to antennaId
        """
        if isinstance(id, list):
            for thisValue in id:
                self._antennaId.append(Tag(thisValue))
        else:
            self._antennaId.append(Tag(id))

    def getOneAntennaId(self, i):
        """
        Returns the Tag stored in antennaId at position i.
        """
        return self._antennaId[i]

    def getAntennaUsingAntennaId(self, i):
        """
        Returns the AntennaRow linked to this row via the Tag stored in antennaId
        at position i.
        """

        return self._table.getContainer().getAntenna().getRowByKey(self._antennaId[i])

    def getAntennasUsingAntennaId(self):
        """
        Returns the array of AntennaRow linked to this row via the Tags stored in antennaId
        """
        result = []
        for thisItem in self._antennaId:
            result.append(self._table.getContainer().getAntenna().getRowByKey(thisItem))

        return result

    def setOnePairedAntennaId(self, index, pairedAntennaId):
        """
        Set pairedAntennaId[index] with the specified Tag value.
        index The index in pairedAntennaId where to set the Tag value.
        pairedAntennaId The Tag value to which pairedAntennaId[index] is to be set.
        Raises an exception if that value does not already exist in this row
        """
        if not self._pairedAntennaIdExists():
            raise ValueError(
                "The optional attribute, pairedAntennaId, does not exist in this row. This value can not be set using this method."
            )
        self._pairedAntennaId[index] = Tag(pairedAntennaId)

    # ===> hasmany link from a row of Flag table to many rows of Antenna table.

    def addPairedAntennaId(self, id):
        """
        Append a Tag to pairedAntennaId
        id the Tag to be appended to pairedAntennaId
        """
        if isinstance(id, list):
            for thisValue in id:
                self._pairedAntennaId.append(Tag(thisValue))
        else:
            self._pairedAntennaId.append(Tag(id))

        if not self._pairedAntennaIdExists:
            self._pairedAntennaIdExists = True

    def getOnePairedAntennaId(self, i):
        """
        Returns the Tag stored in pairedAntennaId at position i.
        """
        return self._pairedAntennaId[i]

    def getAntennaUsingPairedAntennaId(self, i):
        """
        Returns the AntennaRow linked to this row via the Tag stored in pairedAntennaId
        at position i.
        """

        return (
            self._table.getContainer()
            .getAntenna()
            .getRowByKey(self._pairedAntennaId[i])
        )

    def getAntennasUsingPairedAntennaId(self):
        """
        Returns the array of AntennaRow linked to this row via the Tags stored in pairedAntennaId
        """
        result = []
        for thisItem in self._pairedAntennaId:
            result.append(self._table.getContainer().getAntenna().getRowByKey(thisItem))

        return result

    def setOneSpectralWindowId(self, index, spectralWindowId):
        """
        Set spectralWindowId[index] with the specified Tag value.
        index The index in spectralWindowId where to set the Tag value.
        spectralWindowId The Tag value to which spectralWindowId[index] is to be set.
        Raises an exception if that value does not already exist in this row
        """
        if not self._spectralWindowIdExists():
            raise ValueError(
                "The optional attribute, spectralWindowId, does not exist in this row. This value can not be set using this method."
            )
        self._spectralWindowId[index] = Tag(spectralWindowId)

    # ===> hasmany link from a row of Flag table to many rows of SpectralWindow table.

    def addSpectralWindowId(self, id):
        """
        Append a Tag to spectralWindowId
        id the Tag to be appended to spectralWindowId
        """
        if isinstance(id, list):
            for thisValue in id:
                self._spectralWindowId.append(Tag(thisValue))
        else:
            self._spectralWindowId.append(Tag(id))

        if not self._spectralWindowIdExists:
            self._spectralWindowIdExists = True

    def getOneSpectralWindowId(self, i):
        """
        Returns the Tag stored in spectralWindowId at position i.
        """
        return self._spectralWindowId[i]

    def getSpectralWindowUsingSpectralWindowId(self, i):
        """
        Returns the SpectralWindowRow linked to this row via the Tag stored in spectralWindowId
        at position i.
        """

        return (
            self._table.getContainer()
            .getSpectralWindow()
            .getRowByKey(self._spectralWindowId[i])
        )

    def getSpectralWindowsUsingSpectralWindowId(self):
        """
        Returns the array of SpectralWindowRow linked to this row via the Tags stored in spectralWindowId
        """
        result = []
        for thisItem in self._spectralWindowId:
            result.append(
                self._table.getContainer().getSpectralWindow().getRowByKey(thisItem)
            )

        return result

    # comparison methods

    def compareNoAutoInc(self, startTime, endTime, reason, numAntenna, antennaId):
        """
        Compare each attribute except the autoincrementable one of this FlagRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # startTime is a ArrayTime, compare using the equals method.
        if not self._startTime.equals(startTime):
            return False

        # endTime is a ArrayTime, compare using the equals method.
        if not self._endTime.equals(endTime):
            return False

        # reason is a str, compare using the == operator.
        if not (self._reason == reason):
            return False

        # numAntenna is a int, compare using the == operator.
        if not (self._numAntenna == numAntenna):
            return False

        # antennaId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._antennaId) != len(antennaId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._antennaId)):
            if not (self._antennaId[indx].equals(antennaId[indx])):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getStartTime(),
            otherRow.getEndTime(),
            otherRow.getReason(),
            otherRow.getNumAntenna(),
            otherRow.getAntennaId(),
        )

    def compareRequiredValue(self, startTime, endTime, reason, numAntenna, antennaId):

        # startTime is a ArrayTime, compare using the equals method.
        if not self._startTime.equals(startTime):
            return False

        # endTime is a ArrayTime, compare using the equals method.
        if not self._endTime.equals(endTime):
            return False

        # reason is a str, compare using the == operator.
        if not (self._reason == reason):
            return False

        # numAntenna is a int, compare using the == operator.
        if not (self._numAntenna == numAntenna):
            return False

        # antennaId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._antennaId) != len(antennaId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._antennaId)):
            if not (self._antennaId[indx].equals(antennaId[indx])):
                return False

        return True


# initialize the dictionary that maps fields to init methods
FlagRow.initFromBinMethods()
