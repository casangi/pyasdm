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
# File FeedRow.py
#

import pyasdm.FeedTable

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


class FeedRow:
    """
    The FeedRow class is a row of a FeedTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a FeedRow.
        When row is None, create an empty row attached to table, which must be a FeedTable.
        When row is given, copy those values in to the new row. The row argument must be a FeedRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.FeedTable):
            raise ValueError("table must be a FeedTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._feedId = 0

        self._timeInterval = ArrayTimeInterval()

        self._numReceptor = 0

        self._beamOffset = []  # this is a list of float []  []

        self._focusReference = []  # this is a list of Length []  []

        self._polarizationTypes = []  # this is a list of PolarizationType []

        self._polResponse = []  # this is a list of Complex []  []

        self._receptorAngle = []  # this is a list of Angle []

        self._feedNumExists = False

        self._feedNum = 0

        self._illumOffsetExists = False

        self._illumOffset = []  # this is a list of Length []

        self._positionExists = False

        self._position = []  # this is a list of Length []

        self._skyCouplingExists = False

        self._skyCoupling = None

        self._numChanExists = False

        self._numChan = 0

        self._skyCouplingSpectrumExists = False

        self._skyCouplingSpectrum = []  # this is a list of float []

        # extrinsic attributes

        self._antennaId = Tag()

        self._receiverId = []  # this is a list of int []

        self._spectralWindowId = Tag()

        if row is not None:
            if not isinstance(row, FeedRow):
                raise ValueError("row must be a FeedRow")

            # copy constructor

            self._antennaId = Tag(row._antennaId)

            self._spectralWindowId = Tag(row._spectralWindowId)

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._feedId = row._feedId

            self._numReceptor = row._numReceptor

            # beamOffset is a  list , make a deep copy
            self._beamOffset = copy.deepcopy(row._beamOffset)

            # focusReference is a  list , make a deep copy
            self._focusReference = copy.deepcopy(row._focusReference)

            # polarizationTypes is a  list , make a deep copy
            self._polarizationTypes = copy.deepcopy(row._polarizationTypes)

            # polResponse is a  list , make a deep copy
            self._polResponse = copy.deepcopy(row._polResponse)

            # receptorAngle is a  list , make a deep copy
            self._receptorAngle = copy.deepcopy(row._receptorAngle)

            # receiverId is a list, let's populate self._receiverId element by element.
            if self._receiverId is None:
                self._receiverId = []

            for i in range(len(row._receiverId)):

                self._receiverId.append(row._receiverId[i])

            # by default set systematically feedNum's value to something not None

            if row._feedNumExists:

                self._feedNum = row._feedNum

                self._feedNumExists = True

            # by default set systematically illumOffset's value to something not None

            if row._illumOffsetExists:

                # illumOffset is a list, make a deep copy
                self.illumOffset = copy.deepcopy(row.illumOffset)

                self._illumOffsetExists = True

            # by default set systematically position's value to something not None

            if row._positionExists:

                # position is a list, make a deep copy
                self.position = copy.deepcopy(row.position)

                self._positionExists = True

            # by default set systematically skyCoupling's value to something not None

            if row._skyCouplingExists:

                self._skyCoupling = row._skyCoupling

                self._skyCouplingExists = True

            # by default set systematically numChan's value to something not None

            if row._numChanExists:

                self._numChan = row._numChan

                self._numChanExists = True

            # by default set systematically skyCouplingSpectrum's value to something not None

            if row._skyCouplingSpectrumExists:

                # skyCouplingSpectrum is a list, make a deep copy
                self.skyCouplingSpectrum = copy.deepcopy(row.skyCouplingSpectrum)

                self._skyCouplingSpectrumExists = True

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

        result += Parser.valueToXML("feedId", self._feedId)

        result += Parser.extendedValueToXML("timeInterval", self._timeInterval)

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listValueToXML("beamOffset", self._beamOffset)

        result += Parser.listExtendedValueToXML("focusReference", self._focusReference)

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.listExtendedValueToXML("polResponse", self._polResponse)

        result += Parser.listExtendedValueToXML("receptorAngle", self._receptorAngle)

        if self._feedNumExists:

            result += Parser.valueToXML("feedNum", self._feedNum)

        if self._illumOffsetExists:

            result += Parser.listExtendedValueToXML("illumOffset", self._illumOffset)

        if self._positionExists:

            result += Parser.listExtendedValueToXML("position", self._position)

        if self._skyCouplingExists:

            result += Parser.valueToXML("skyCoupling", self._skyCoupling)

        if self._numChanExists:

            result += Parser.valueToXML("numChan", self._numChan)

        if self._skyCouplingSpectrumExists:

            result += Parser.listValueToXML(
                "skyCouplingSpectrum", self._skyCouplingSpectrum
            )

        # extrinsic attributes

        result += Parser.extendedValueToXML("antennaId", self._antennaId)

        result += Parser.listValueToXML("receiverId", self._receiverId)

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
                "xmlrow is not a string or a minidom.Element", "FeedTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "FeedTable")

        # intrinsic attribute values

        feedIdNode = rowdom.getElementsByTagName("feedId")[0]

        self._feedId = int(feedIdNode.firstChild.data.strip())

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        beamOffsetNode = rowdom.getElementsByTagName("beamOffset")[0]

        beamOffsetStr = beamOffsetNode.firstChild.data.strip()

        self._beamOffset = Parser.stringListToLists(beamOffsetStr, float, "Feed", False)

        focusReferenceNode = rowdom.getElementsByTagName("focusReference")[0]

        focusReferenceStr = focusReferenceNode.firstChild.data.strip()

        self._focusReference = Parser.stringListToLists(
            focusReferenceStr, Length, "Feed", True
        )

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data.strip()
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "Feed", False
        )

        polResponseNode = rowdom.getElementsByTagName("polResponse")[0]

        polResponseStr = polResponseNode.firstChild.data.strip()

        self._polResponse = Parser.stringListToLists(
            polResponseStr, Complex, "Feed", True
        )

        receptorAngleNode = rowdom.getElementsByTagName("receptorAngle")[0]

        receptorAngleStr = receptorAngleNode.firstChild.data.strip()

        self._receptorAngle = Parser.stringListToLists(
            receptorAngleStr, Angle, "Feed", True
        )

        feedNumNode = rowdom.getElementsByTagName("feedNum")
        if len(feedNumNode) > 0:

            self._feedNum = int(feedNumNode[0].firstChild.data.strip())

            self._feedNumExists = True

        illumOffsetNode = rowdom.getElementsByTagName("illumOffset")
        if len(illumOffsetNode) > 0:

            illumOffsetStr = illumOffsetNode[0].firstChild.data.strip()

            self._illumOffset = Parser.stringListToLists(
                illumOffsetStr, Length, "Feed", True
            )

            self._illumOffsetExists = True

        positionNode = rowdom.getElementsByTagName("position")
        if len(positionNode) > 0:

            positionStr = positionNode[0].firstChild.data.strip()

            self._position = Parser.stringListToLists(positionStr, Length, "Feed", True)

            self._positionExists = True

        skyCouplingNode = rowdom.getElementsByTagName("skyCoupling")
        if len(skyCouplingNode) > 0:

            self._skyCoupling = float(skyCouplingNode[0].firstChild.data.strip())

            self._skyCouplingExists = True

        numChanNode = rowdom.getElementsByTagName("numChan")
        if len(numChanNode) > 0:

            self._numChan = int(numChanNode[0].firstChild.data.strip())

            self._numChanExists = True

        skyCouplingSpectrumNode = rowdom.getElementsByTagName("skyCouplingSpectrum")
        if len(skyCouplingSpectrumNode) > 0:

            skyCouplingSpectrumStr = skyCouplingSpectrumNode[0].firstChild.data.strip()

            self._skyCouplingSpectrum = Parser.stringListToLists(
                skyCouplingSpectrumStr, float, "Feed", False
            )

            self._skyCouplingSpectrumExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        self._antennaId = Tag(antennaIdNode.firstChild.data.strip())

        receiverIdNode = rowdom.getElementsByTagName("receiverId")[0]

        receiverIdStr = receiverIdNode.firstChild.data.strip()

        self._receiverId = Parser.stringListToLists(receiverIdStr, int, "Feed", False)

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")[0]

        self._spectralWindowId = Tag(spectralWindowIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._antennaId.toBin(eos)

        self._spectralWindowId.toBin(eos)

        self._timeInterval.toBin(eos)

        eos.writeInt(self._feedId)

        eos.writeInt(self._numReceptor)

        # null array case, unsure if this is possible but this should work
        if self._beamOffset is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            beamOffset_dims = Parser.getListDims(self._beamOffset)
        # assumes it really is 2D
        eos.writeInt(beamOffset_dims[0])
        eos.writeInt(beamOffset_dims[1])
        for i in range(beamOffset_dims[0]):
            for j in range(beamOffset_dims[1]):
                eos.writeFloat(self._beamOffset[i][j])

        Length.listToBin(self._focusReference, eos)

        eos.writeInt(len(self._polarizationTypes))
        for i in range(len(self._polarizationTypes)):

            eos.writeString(self._polarizationTypes[i].toString())

        Complex.listToBin(self._polResponse, eos)

        Angle.listToBin(self._receptorAngle, eos)

        eos.writeInt(len(self._receiverId))
        for i in range(len(self._receiverId)):

            eos.writeInt(int(self._receiverId[i].getValue()))

        eos.writeBool(self._feedNumExists)
        if self._feedNumExists:

            eos.writeInt(self._feedNum)

        eos.writeBool(self._illumOffsetExists)
        if self._illumOffsetExists:

            Length.listToBin(self._illumOffset, eos)

        eos.writeBool(self._positionExists)
        if self._positionExists:

            Length.listToBin(self._position, eos)

        eos.writeBool(self._skyCouplingExists)
        if self._skyCouplingExists:

            eos.writeFloat(self._skyCoupling)

        eos.writeBool(self._numChanExists)
        if self._numChanExists:

            eos.writeInt(self._numChan)

        eos.writeBool(self._skyCouplingSpectrumExists)
        if self._skyCouplingSpectrumExists:

            eos.writeInt(len(self._skyCouplingSpectrum))
            for i in range(len(self._skyCouplingSpectrum)):

                eos.writeFloat(self._skyCouplingSpectrum[i])

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
    def timeIntervalFromBin(row, eis):
        """
        Set the timeInterval in row from the EndianInput (eis) instance.
        """

        row._timeInterval = ArrayTimeInterval.fromBin(eis)

    @staticmethod
    def feedIdFromBin(row, eis):
        """
        Set the feedId in row from the EndianInput (eis) instance.
        """

        row._feedId = eis.readInt()

    @staticmethod
    def numReceptorFromBin(row, eis):
        """
        Set the numReceptor in row from the EndianInput (eis) instance.
        """

        row._numReceptor = eis.readInt()

    @staticmethod
    def beamOffsetFromBin(row, eis):
        """
        Set the beamOffset in row from the EndianInput (eis) instance.
        """

        beamOffsetDim1 = eis.readInt()
        beamOffsetDim2 = eis.readInt()
        thisList = []
        for i in range(beamOffsetDim1):
            thisList_j = []
            for j in range(beamOffsetDim2):
                thisValue = eis.readFloat()
                thisList_j.append(thisValue)
            thisList.append(thisList_j)
        row.beamOffset = thisList

    @staticmethod
    def focusReferenceFromBin(row, eis):
        """
        Set the focusReference in row from the EndianInput (eis) instance.
        """

        row._focusReference = Length.from2DBin(eis)

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
    def polResponseFromBin(row, eis):
        """
        Set the polResponse in row from the EndianInput (eis) instance.
        """

        row._polResponse = Complex.from2DBin(eis)

    @staticmethod
    def receptorAngleFromBin(row, eis):
        """
        Set the receptorAngle in row from the EndianInput (eis) instance.
        """

        row._receptorAngle = Angle.from1DBin(eis)

    @staticmethod
    def receiverIdFromBin(row, eis):
        """
        Set the receiverId in row from the EndianInput (eis) instance.
        """

        thisList = []
        unusedLength = eis.readInt()
        for i in range(unusedLength):
            thisList.append(eis.readInt())
        row._receiverId = thisList

    @staticmethod
    def feedNumFromBin(row, eis):
        """
        Set the optional feedNum in row from the EndianInput (eis) instance.
        """
        row._feedNumExists = eis.readBool()
        if row._feedNumExists:

            row._feedNum = eis.readInt()

    @staticmethod
    def illumOffsetFromBin(row, eis):
        """
        Set the optional illumOffset in row from the EndianInput (eis) instance.
        """
        row._illumOffsetExists = eis.readBool()
        if row._illumOffsetExists:

            row._illumOffset = Length.from1DBin(eis)

    @staticmethod
    def positionFromBin(row, eis):
        """
        Set the optional position in row from the EndianInput (eis) instance.
        """
        row._positionExists = eis.readBool()
        if row._positionExists:

            row._position = Length.from1DBin(eis)

    @staticmethod
    def skyCouplingFromBin(row, eis):
        """
        Set the optional skyCoupling in row from the EndianInput (eis) instance.
        """
        row._skyCouplingExists = eis.readBool()
        if row._skyCouplingExists:

            row._skyCoupling = eis.readFloat()

    @staticmethod
    def numChanFromBin(row, eis):
        """
        Set the optional numChan in row from the EndianInput (eis) instance.
        """
        row._numChanExists = eis.readBool()
        if row._numChanExists:

            row._numChan = eis.readInt()

    @staticmethod
    def skyCouplingSpectrumFromBin(row, eis):
        """
        Set the optional skyCouplingSpectrum in row from the EndianInput (eis) instance.
        """
        row._skyCouplingSpectrumExists = eis.readBool()
        if row._skyCouplingSpectrumExists:

            skyCouplingSpectrumDim1 = eis.readInt()
            thisList = []
            for i in range(skyCouplingSpectrumDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._skyCouplingSpectrum = thisList

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaId"] = FeedRow.antennaIdFromBin
        _fromBinMethods["spectralWindowId"] = FeedRow.spectralWindowIdFromBin
        _fromBinMethods["timeInterval"] = FeedRow.timeIntervalFromBin
        _fromBinMethods["feedId"] = FeedRow.feedIdFromBin
        _fromBinMethods["numReceptor"] = FeedRow.numReceptorFromBin
        _fromBinMethods["beamOffset"] = FeedRow.beamOffsetFromBin
        _fromBinMethods["focusReference"] = FeedRow.focusReferenceFromBin
        _fromBinMethods["polarizationTypes"] = FeedRow.polarizationTypesFromBin
        _fromBinMethods["polResponse"] = FeedRow.polResponseFromBin
        _fromBinMethods["receptorAngle"] = FeedRow.receptorAngleFromBin
        _fromBinMethods["receiverId"] = FeedRow.receiverIdFromBin

        _fromBinMethods["feedNum"] = FeedRow.feedNumFromBin
        _fromBinMethods["illumOffset"] = FeedRow.illumOffsetFromBin
        _fromBinMethods["position"] = FeedRow.positionFromBin
        _fromBinMethods["skyCoupling"] = FeedRow.skyCouplingFromBin
        _fromBinMethods["numChan"] = FeedRow.numChanFromBin
        _fromBinMethods["skyCouplingSpectrum"] = FeedRow.skyCouplingSpectrumFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = FeedRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Feed",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

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

    # ===> Attribute beamOffset

    _beamOffset = None  # this is a 2D list of float

    def getBeamOffset(self):
        """
        Get beamOffset.
        return beamOffset as float []  []
        """

        return copy.deepcopy(self._beamOffset)

    def setBeamOffset(self, beamOffset):
        """
        Set beamOffset with the specified float []  []  value.
        beamOffset The float []  []  value to which beamOffset is to be set.


        """

        # value must be a list
        if not isinstance(beamOffset, list):
            raise ValueError("The value of beamOffset must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(beamOffset)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of beamOffset is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(beamOffset, float):
                raise ValueError(
                    "type of the first value in beamOffset is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._beamOffset = copy.deepcopy(beamOffset)
        except Exception as exc:
            raise ValueError("Invalid beamOffset : " + str(exc))

    # ===> Attribute focusReference

    _focusReference = None  # this is a 2D list of Length

    def getFocusReference(self):
        """
        Get focusReference.
        return focusReference as Length []  []
        """

        return copy.deepcopy(self._focusReference)

    def setFocusReference(self, focusReference):
        """
        Set focusReference with the specified Length []  []  value.
        focusReference The Length []  []  value to which focusReference is to be set.
        The value of focusReference can be anything allowed by the Length []  []  constructor.

        """

        # value must be a list
        if not isinstance(focusReference, list):
            raise ValueError("The value of focusReference must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(focusReference)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of focusReference is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(focusReference, Length):
                raise ValueError(
                    "type of the first value in focusReference is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._focusReference = copy.deepcopy(focusReference)
        except Exception as exc:
            raise ValueError("Invalid focusReference : " + str(exc))

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

    # ===> Attribute polResponse

    _polResponse = None  # this is a 2D list of Complex

    def getPolResponse(self):
        """
        Get polResponse.
        return polResponse as Complex []  []
        """

        return copy.deepcopy(self._polResponse)

    def setPolResponse(self, polResponse):
        """
        Set polResponse with the specified Complex []  []  value.
        polResponse The Complex []  []  value to which polResponse is to be set.
        The value of polResponse can be anything allowed by the Complex []  []  constructor.

        """

        # value must be a list
        if not isinstance(polResponse, list):
            raise ValueError("The value of polResponse must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(polResponse)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of polResponse is not correct")

            # the type of the values in the list must be Complex
            # note : this only checks the first value found
            if not Parser.checkListType(polResponse, Complex):
                raise ValueError(
                    "type of the first value in polResponse is not Complex as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._polResponse = copy.deepcopy(polResponse)
        except Exception as exc:
            raise ValueError("Invalid polResponse : " + str(exc))

    # ===> Attribute receptorAngle

    _receptorAngle = None  # this is a 1D list of Angle

    def getReceptorAngle(self):
        """
        Get receptorAngle.
        return receptorAngle as Angle []
        """

        return copy.deepcopy(self._receptorAngle)

    def setReceptorAngle(self, receptorAngle):
        """
        Set receptorAngle with the specified Angle []  value.
        receptorAngle The Angle []  value to which receptorAngle is to be set.
        The value of receptorAngle can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(receptorAngle, list):
            raise ValueError("The value of receptorAngle must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(receptorAngle)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of receptorAngle is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(receptorAngle, Angle):
                raise ValueError(
                    "type of the first value in receptorAngle is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._receptorAngle = copy.deepcopy(receptorAngle)
        except Exception as exc:
            raise ValueError("Invalid receptorAngle : " + str(exc))

    # ===> Attribute feedNum, which is optional
    _feedNumExists = False

    _feedNum = 0

    def isFeedNumExists(self):
        """
        The attribute feedNum is optional. Return True if this attribute exists.
        return True if and only if the feedNum attribute exists.
        """
        return self._feedNumExists

    def getFeedNum(self):
        """
        Get feedNum, which is optional.
        return feedNum as int
        raises ValueError If feedNum does not exist.
        """
        if not self._feedNumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + feedNum
                + " attribute in table Feed does not exist!"
            )

        return self._feedNum

    def setFeedNum(self, feedNum):
        """
        Set feedNum with the specified int value.
        feedNum The int value to which feedNum is to be set.


        """

        self._feedNum = int(feedNum)

        self._feedNumExists = True

    def clearFeedNum(self):
        """
        Mark feedNum, which is an optional field, as non-existent.
        """
        self._feedNumExists = False

    # ===> Attribute illumOffset, which is optional
    _illumOffsetExists = False

    _illumOffset = None  # this is a 1D list of Length

    def isIllumOffsetExists(self):
        """
        The attribute illumOffset is optional. Return True if this attribute exists.
        return True if and only if the illumOffset attribute exists.
        """
        return self._illumOffsetExists

    def getIllumOffset(self):
        """
        Get illumOffset, which is optional.
        return illumOffset as Length []
        raises ValueError If illumOffset does not exist.
        """
        if not self._illumOffsetExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + illumOffset
                + " attribute in table Feed does not exist!"
            )

        return copy.deepcopy(self._illumOffset)

    def setIllumOffset(self, illumOffset):
        """
        Set illumOffset with the specified Length []  value.
        illumOffset The Length []  value to which illumOffset is to be set.
        The value of illumOffset can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(illumOffset, list):
            raise ValueError("The value of illumOffset must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(illumOffset)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of illumOffset is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(illumOffset, Length):
                raise ValueError(
                    "type of the first value in illumOffset is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._illumOffset = copy.deepcopy(illumOffset)
        except Exception as exc:
            raise ValueError("Invalid illumOffset : " + str(exc))

        self._illumOffsetExists = True

    def clearIllumOffset(self):
        """
        Mark illumOffset, which is an optional field, as non-existent.
        """
        self._illumOffsetExists = False

    # ===> Attribute position, which is optional
    _positionExists = False

    _position = None  # this is a 1D list of Length

    def isPositionExists(self):
        """
        The attribute position is optional. Return True if this attribute exists.
        return True if and only if the position attribute exists.
        """
        return self._positionExists

    def getPosition(self):
        """
        Get position, which is optional.
        return position as Length []
        raises ValueError If position does not exist.
        """
        if not self._positionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + position
                + " attribute in table Feed does not exist!"
            )

        return copy.deepcopy(self._position)

    def setPosition(self, position):
        """
        Set position with the specified Length []  value.
        position The Length []  value to which position is to be set.
        The value of position can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(position, list):
            raise ValueError("The value of position must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(position)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of position is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(position, Length):
                raise ValueError(
                    "type of the first value in position is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._position = copy.deepcopy(position)
        except Exception as exc:
            raise ValueError("Invalid position : " + str(exc))

        self._positionExists = True

    def clearPosition(self):
        """
        Mark position, which is an optional field, as non-existent.
        """
        self._positionExists = False

    # ===> Attribute skyCoupling, which is optional
    _skyCouplingExists = False

    _skyCoupling = None

    def isSkyCouplingExists(self):
        """
        The attribute skyCoupling is optional. Return True if this attribute exists.
        return True if and only if the skyCoupling attribute exists.
        """
        return self._skyCouplingExists

    def getSkyCoupling(self):
        """
        Get skyCoupling, which is optional.
        return skyCoupling as float
        raises ValueError If skyCoupling does not exist.
        """
        if not self._skyCouplingExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + skyCoupling
                + " attribute in table Feed does not exist!"
            )

        return self._skyCoupling

    def setSkyCoupling(self, skyCoupling):
        """
        Set skyCoupling with the specified float value.
        skyCoupling The float value to which skyCoupling is to be set.


        """

        self._skyCoupling = float(skyCoupling)

        self._skyCouplingExists = True

    def clearSkyCoupling(self):
        """
        Mark skyCoupling, which is an optional field, as non-existent.
        """
        self._skyCouplingExists = False

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
                + " attribute in table Feed does not exist!"
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

    # ===> Attribute skyCouplingSpectrum, which is optional
    _skyCouplingSpectrumExists = False

    _skyCouplingSpectrum = None  # this is a 1D list of float

    def isSkyCouplingSpectrumExists(self):
        """
        The attribute skyCouplingSpectrum is optional. Return True if this attribute exists.
        return True if and only if the skyCouplingSpectrum attribute exists.
        """
        return self._skyCouplingSpectrumExists

    def getSkyCouplingSpectrum(self):
        """
        Get skyCouplingSpectrum, which is optional.
        return skyCouplingSpectrum as float []
        raises ValueError If skyCouplingSpectrum does not exist.
        """
        if not self._skyCouplingSpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + skyCouplingSpectrum
                + " attribute in table Feed does not exist!"
            )

        return copy.deepcopy(self._skyCouplingSpectrum)

    def setSkyCouplingSpectrum(self, skyCouplingSpectrum):
        """
        Set skyCouplingSpectrum with the specified float []  value.
        skyCouplingSpectrum The float []  value to which skyCouplingSpectrum is to be set.


        """

        # value must be a list
        if not isinstance(skyCouplingSpectrum, list):
            raise ValueError("The value of skyCouplingSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(skyCouplingSpectrum)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of skyCouplingSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(skyCouplingSpectrum, float):
                raise ValueError(
                    "type of the first value in skyCouplingSpectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._skyCouplingSpectrum = copy.deepcopy(skyCouplingSpectrum)
        except Exception as exc:
            raise ValueError("Invalid skyCouplingSpectrum : " + str(exc))

        self._skyCouplingSpectrumExists = True

    def clearSkyCouplingSpectrum(self):
        """
        Mark skyCouplingSpectrum, which is an optional field, as non-existent.
        """
        self._skyCouplingSpectrumExists = False

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

    # ===> Attribute receiverId

    _receiverId = []  # this is a list of int []

    def getReceiverId(self):
        """
        Get receiverId.
        return receiverId as int []
        """

        return copy.deepcopy(self._receiverId)

    def setReceiverId(self, receiverId):
        """
        Set receiverId with the specified int []  value.
        receiverId The int []  value to which receiverId is to be set.


        """

        # value must be a list
        if not isinstance(receiverId, list):
            raise ValueError("The value of receiverId must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(receiverId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of receiverId is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not Parser.checkListType(receiverId, int):
                raise ValueError(
                    "type of the first value in receiverId is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._receiverId = copy.deepcopy(receiverId)
        except Exception as exc:
            raise ValueError("Invalid receiverId : " + str(exc))

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

    def setOneReceiverId(self, index, receiverId):
        """
        Set receiverId[index] with the specified int value.
        index The index in receiverId where to set the int value.
        receiverId The int value to which receiverId[index] is to be set.

        """

        self._receiverId[index] = int(receiverId)

    # ===> Slices link from a row of Feed table to a collection of row of Receiver table.
    def addReceiverId(self, id):
        """
        Append a new id or list of ids to receiverId
        """
        if isinstance(id, list):
            for thisId in id:
                receiverId.append(SimplePythonType(id))
        else:
            receiverId.append(SimplePythonType(id))

    def getOneReceiver(self, i):
        """
        Using the receiverId at location i in this row, return the corresponding row from ReceiverTable
        """

        j = self._receiverId[i]
        return self._table.getContainer().getReceiver().getRowByReceiverId(j)

    def getReceivers(self):
        """
        Get all of the rows at ReceiverTable corresponding to each of the values of receiverId from this row.
        returns a list of ReceiverRow
        """
        result = []

        for thisValue in self._receiverId:
            tr = self._table.getContainer().getReceiver().getRowByReceiverId(thisValue)
            # this may return more than one row
            if isinstance(tr, list):
                for thisRow in tr:
                    result.append(thisRow)
            else:
                result.append(tr)
        return copy.deepcopy(result)

    # comparison methods

    def compareNoAutoInc(
        self,
        antennaId,
        spectralWindowId,
        timeInterval,
        numReceptor,
        beamOffset,
        focusReference,
        polarizationTypes,
        polResponse,
        receptorAngle,
        receiverId,
    ):
        """
        Compare each attribute except the autoincrementable one of this FeedRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaId is a Tag, compare using the equals method.
        if not self._antennaId.equals(antennaId):
            return False

        # spectralWindowId is a Tag, compare using the equals method.
        if not self._spectralWindowId.equals(spectralWindowId):
            return False

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 2D arrays (lists).
        if beamOffset is not None:
            if self._beamOffset is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            beamOffset_dims = Parser.getListDims(beamOffset)
            this_beamOffset_dims = Parser.getListDims(self._beamOffset)
            if beamOffset_dims != this_beamOffset_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(beamOffset_dims[0]):
                for j in range(beamOffset_dims[1]):

                    # beamOffset is an array of float, compare using == operator.
                    if not (self._beamOffset[i][j] == beamOffset[i][j]):
                        return False

        # We compare two 2D arrays (lists).
        if focusReference is not None:
            if self._focusReference is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            focusReference_dims = Parser.getListDims(focusReference)
            this_focusReference_dims = Parser.getListDims(self._focusReference)
            if focusReference_dims != this_focusReference_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(focusReference_dims[0]):
                for j in range(focusReference_dims[1]):

                    # focusReference is a Length, compare using the almostEquals method.
                    if not (
                        self._focusReference[i][j].almostEquals(
                            focusReference[i][j],
                            self.getTable().getFocusReferenceEqTolerance(),
                        )
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

        # We compare two 2D arrays (lists).
        if polResponse is not None:
            if self._polResponse is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            polResponse_dims = Parser.getListDims(polResponse)
            this_polResponse_dims = Parser.getListDims(self._polResponse)
            if polResponse_dims != this_polResponse_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(polResponse_dims[0]):
                for j in range(polResponse_dims[1]):

                    # polResponse is an array of Complex, compare using equals method.
                    if not (self._polResponse[i][j].equals(polResponse[i][j])):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._receptorAngle) != len(receptorAngle):
            return False
        for indx in range(len(receptorAngle)):

            # receptorAngle is a list of Angle, compare using the almostEquals method.
            if not self._receptorAngle[indx].almostEquals(
                receptorAngle[indx], self.getTable().getReceptorAngleEqTolerance()
            ):
                return False

        # receiverId is an extrinsic attribute which is a list of int.
        # the lists must have the same length
        if len(self._receiverId) != len(receiverId):
            return False

        # receiverId is a list of int, compare using the != operator.
        for indx in range(len(receiverId)):
            if self._receiverId[indx] != receiverId[indx]:
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumReceptor(),
            otherRow.getBeamOffset(),
            otherRow.getFocusReference(),
            otherRow.getPolarizationTypes(),
            otherRow.getPolResponse(),
            otherRow.getReceptorAngle(),
            otherRow.getReceiverId(),
        )

    def compareRequiredValue(
        self,
        numReceptor,
        beamOffset,
        focusReference,
        polarizationTypes,
        polResponse,
        receptorAngle,
        receiverId,
    ):

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 2D arrays (lists).
        if beamOffset is not None:
            if self._beamOffset is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            beamOffset_dims = Parser.getListDims(beamOffset)
            this_beamOffset_dims = Parser.getListDims(self._beamOffset)
            if beamOffset_dims != this_beamOffset_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(beamOffset_dims[0]):
                for j in range(beamOffset_dims[1]):

                    # beamOffset is an array of float, compare using == operator.
                    if not (self._beamOffset[i][j] == beamOffset[i][j]):
                        return False

        # We compare two 2D arrays (lists).
        if focusReference is not None:
            if self._focusReference is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            focusReference_dims = Parser.getListDims(focusReference)
            this_focusReference_dims = Parser.getListDims(self._focusReference)
            if focusReference_dims != this_focusReference_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(focusReference_dims[0]):
                for j in range(focusReference_dims[1]):

                    # focusReference is a Length, compare using the almostEquals method.
                    if not (
                        self._focusReference[i][j].almostEquals(
                            focusReference[i][j],
                            self.getTable().getFocusReferenceEqTolerance(),
                        )
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

        # We compare two 2D arrays (lists).
        if polResponse is not None:
            if self._polResponse is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            polResponse_dims = Parser.getListDims(polResponse)
            this_polResponse_dims = Parser.getListDims(self._polResponse)
            if polResponse_dims != this_polResponse_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(polResponse_dims[0]):
                for j in range(polResponse_dims[1]):

                    # polResponse is an array of Complex, compare using equals method.
                    if not (self._polResponse[i][j].equals(polResponse[i][j])):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._receptorAngle) != len(receptorAngle):
            return False
        for indx in range(len(receptorAngle)):

            # receptorAngle is a list of Angle, compare using the almostEquals method.
            if not self._receptorAngle[indx].almostEquals(
                receptorAngle[indx], self.getTable().getReceptorAngleEqTolerance()
            ):
                return False

        # receiverId is an extrinsic attribute which is a list of int.
        # the lists must have the same length
        if len(self._receiverId) != len(receiverId):
            return False

        # receiverId is a list of int, compare using the != operator.
        for indx in range(len(receiverId)):
            if self._receiverId[indx] != receiverId[indx]:
                return False

        return True


# initialize the dictionary that maps fields to init methods
FeedRow.initFromBinMethods()
