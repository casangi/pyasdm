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
# File PointingRow.py
#

import pyasdm.PointingTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.DirectionReferenceCode import DirectionReferenceCode


from xml.dom import minidom

import copy


class PointingRow:
    """
    The PointingRow class is a row of a PointingTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a PointingRow.
        When row is None, create an empty row attached to table, which must be a PointingTable.
        When row is given, copy those values in to the new row. The row argument must be a PointingRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.PointingTable):
            raise ValueError("table must be a PointingTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._timeInterval = ArrayTimeInterval()

        self._numSample = 0

        self._encoder = []  # this is a list of Angle []  []

        self._pointingTracking = None

        self._usePolynomials = None

        self._timeOrigin = ArrayTime()

        self._numTerm = 0

        self._pointingDirection = []  # this is a list of Angle []  []

        self._target = []  # this is a list of Angle []  []

        self._offset = []  # this is a list of Angle []  []

        self._overTheTopExists = False

        self._overTheTop = None

        self._sourceOffsetExists = False

        self._sourceOffset = []  # this is a list of Angle []  []

        self._sourceOffsetReferenceCodeExists = False

        self._sourceOffsetReferenceCode = DirectionReferenceCode.from_int(0)

        self._sourceOffsetEquinoxExists = False

        self._sourceOffsetEquinox = ArrayTime()

        self._sampledTimeIntervalExists = False

        self._sampledTimeInterval = []  # this is a list of ArrayTimeInterval []

        self._atmosphericCorrectionExists = False

        self._atmosphericCorrection = []  # this is a list of Angle []  []

        # extrinsic attributes

        self._antennaId = Tag()

        self._pointingModelId = 0

        if row is not None:
            if not isinstance(row, PointingRow):
                raise ValueError("row must be a PointingRow")

            # copy constructor

            self._antennaId = Tag(row._antennaId)

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._numSample = row._numSample

            # encoder is a  list , make a deep copy
            self._encoder = copy.deepcopy(row._encoder)

            self._pointingTracking = row._pointingTracking

            self._usePolynomials = row._usePolynomials

            self._timeOrigin = ArrayTime(row._timeOrigin)

            self._numTerm = row._numTerm

            # pointingDirection is a  list , make a deep copy
            self._pointingDirection = copy.deepcopy(row._pointingDirection)

            # target is a  list , make a deep copy
            self._target = copy.deepcopy(row._target)

            # offset is a  list , make a deep copy
            self._offset = copy.deepcopy(row._offset)

            self._pointingModelId = row._pointingModelId

            # by default set systematically overTheTop's value to something not None

            if row._overTheTopExists:

                self._overTheTop = row._overTheTop

                self._overTheTopExists = True

            # by default set systematically sourceOffset's value to something not None

            if row._sourceOffsetExists:

                # sourceOffset is a list, make a deep copy
                self.sourceOffset = copy.deepcopy(row.sourceOffset)

                self._sourceOffsetExists = True

            # by default set systematically sourceOffsetReferenceCode's value to something not None

            self._sourceOffsetReferenceCode = DirectionReferenceCode.from_int(0)

            if row._sourceOffsetReferenceCodeExists:

                if row._sourceOffsetReferenceCode is not None:
                    self._sourceOffsetReferenceCode = row._sourceOffsetReferenceCode

                self._sourceOffsetReferenceCodeExists = True

            # by default set systematically sourceOffsetEquinox's value to something not None

            if row._sourceOffsetEquinoxExists:

                self._sourceOffsetEquinox = ArrayTime(row._sourceOffsetEquinox)

                self._sourceOffsetEquinoxExists = True

            # by default set systematically sampledTimeInterval's value to something not None

            if row._sampledTimeIntervalExists:

                # sampledTimeInterval is a list, make a deep copy
                self.sampledTimeInterval = copy.deepcopy(row.sampledTimeInterval)

                self._sampledTimeIntervalExists = True

            # by default set systematically atmosphericCorrection's value to something not None

            if row._atmosphericCorrectionExists:

                # atmosphericCorrection is a list, make a deep copy
                self.atmosphericCorrection = copy.deepcopy(row.atmosphericCorrection)

                self._atmosphericCorrectionExists = True

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

        result += Parser.valueToXML("numSample", self._numSample)

        result += Parser.listExtendedValueToXML("encoder", self._encoder)

        result += Parser.valueToXML("pointingTracking", self._pointingTracking)

        result += Parser.valueToXML("usePolynomials", self._usePolynomials)

        result += Parser.extendedValueToXML("timeOrigin", self._timeOrigin)

        result += Parser.valueToXML("numTerm", self._numTerm)

        result += Parser.listExtendedValueToXML(
            "pointingDirection", self._pointingDirection
        )

        result += Parser.listExtendedValueToXML("target", self._target)

        result += Parser.listExtendedValueToXML("offset", self._offset)

        if self._overTheTopExists:

            result += Parser.valueToXML("overTheTop", self._overTheTop)

        if self._sourceOffsetExists:

            result += Parser.listExtendedValueToXML("sourceOffset", self._sourceOffset)

        if self._sourceOffsetReferenceCodeExists:

            result += Parser.valueToXML(
                "sourceOffsetReferenceCode",
                DirectionReferenceCode.name(self._sourceOffsetReferenceCode),
            )

        if self._sourceOffsetEquinoxExists:

            result += Parser.extendedValueToXML(
                "sourceOffsetEquinox", self._sourceOffsetEquinox
            )

        if self._sampledTimeIntervalExists:

            result += Parser.listExtendedValueToXML(
                "sampledTimeInterval", self._sampledTimeInterval
            )

        if self._atmosphericCorrectionExists:

            result += Parser.listExtendedValueToXML(
                "atmosphericCorrection", self._atmosphericCorrection
            )

        # extrinsic attributes

        result += Parser.extendedValueToXML("antennaId", self._antennaId)

        result += Parser.valueToXML("pointingModelId", self._pointingModelId)

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
                "xmlrow is not a string or a minidom.Element", "PointingTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "PointingTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        numSampleNode = rowdom.getElementsByTagName("numSample")[0]

        self._numSample = int(numSampleNode.firstChild.data.strip())

        encoderNode = rowdom.getElementsByTagName("encoder")[0]

        encoderStr = encoderNode.firstChild.data.strip()

        self._encoder = Parser.stringListToLists(encoderStr, Angle, "Pointing", True)

        pointingTrackingNode = rowdom.getElementsByTagName("pointingTracking")[0]

        self._pointingTracking = bool(pointingTrackingNode.firstChild.data.strip())

        usePolynomialsNode = rowdom.getElementsByTagName("usePolynomials")[0]

        self._usePolynomials = bool(usePolynomialsNode.firstChild.data.strip())

        timeOriginNode = rowdom.getElementsByTagName("timeOrigin")[0]

        self._timeOrigin = ArrayTime(timeOriginNode.firstChild.data.strip())

        numTermNode = rowdom.getElementsByTagName("numTerm")[0]

        self._numTerm = int(numTermNode.firstChild.data.strip())

        pointingDirectionNode = rowdom.getElementsByTagName("pointingDirection")[0]

        pointingDirectionStr = pointingDirectionNode.firstChild.data.strip()

        self._pointingDirection = Parser.stringListToLists(
            pointingDirectionStr, Angle, "Pointing", True
        )

        targetNode = rowdom.getElementsByTagName("target")[0]

        targetStr = targetNode.firstChild.data.strip()

        self._target = Parser.stringListToLists(targetStr, Angle, "Pointing", True)

        offsetNode = rowdom.getElementsByTagName("offset")[0]

        offsetStr = offsetNode.firstChild.data.strip()

        self._offset = Parser.stringListToLists(offsetStr, Angle, "Pointing", True)

        overTheTopNode = rowdom.getElementsByTagName("overTheTop")
        if len(overTheTopNode) > 0:

            self._overTheTop = bool(overTheTopNode[0].firstChild.data.strip())

            self._overTheTopExists = True

        sourceOffsetNode = rowdom.getElementsByTagName("sourceOffset")
        if len(sourceOffsetNode) > 0:

            sourceOffsetStr = sourceOffsetNode[0].firstChild.data.strip()

            self._sourceOffset = Parser.stringListToLists(
                sourceOffsetStr, Angle, "Pointing", True
            )

            self._sourceOffsetExists = True

        sourceOffsetReferenceCodeNode = rowdom.getElementsByTagName(
            "sourceOffsetReferenceCode"
        )
        if len(sourceOffsetReferenceCodeNode) > 0:

            self._sourceOffsetReferenceCode = (
                DirectionReferenceCode.newDirectionReferenceCode(
                    sourceOffsetReferenceCodeNode[0].firstChild.data.strip()
                )
            )

            self._sourceOffsetReferenceCodeExists = True

        sourceOffsetEquinoxNode = rowdom.getElementsByTagName("sourceOffsetEquinox")
        if len(sourceOffsetEquinoxNode) > 0:

            self._sourceOffsetEquinox = ArrayTime(
                sourceOffsetEquinoxNode[0].firstChild.data.strip()
            )

            self._sourceOffsetEquinoxExists = True

        sampledTimeIntervalNode = rowdom.getElementsByTagName("sampledTimeInterval")
        if len(sampledTimeIntervalNode) > 0:

            sampledTimeIntervalStr = sampledTimeIntervalNode[0].firstChild.data.strip()

            self._sampledTimeInterval = Parser.stringListToLists(
                sampledTimeIntervalStr, ArrayTimeInterval, "Pointing", True
            )

            self._sampledTimeIntervalExists = True

        atmosphericCorrectionNode = rowdom.getElementsByTagName("atmosphericCorrection")
        if len(atmosphericCorrectionNode) > 0:

            atmosphericCorrectionStr = atmosphericCorrectionNode[
                0
            ].firstChild.data.strip()

            self._atmosphericCorrection = Parser.stringListToLists(
                atmosphericCorrectionStr, Angle, "Pointing", True
            )

            self._atmosphericCorrectionExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        self._antennaId = Tag(antennaIdNode.firstChild.data.strip())

        pointingModelIdNode = rowdom.getElementsByTagName("pointingModelId")[0]

        self._pointingModelId = int(pointingModelIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._antennaId.toBin(eos)

        self._timeInterval.toBin(eos)

        eos.writeInt(self._numSample)

        Angle.listToBin(self._encoder, eos)

        eos.writeBool(self._pointingTracking)

        eos.writeBool(self._usePolynomials)

        self._timeOrigin.toBin(eos)

        eos.writeInt(self._numTerm)

        Angle.listToBin(self._pointingDirection, eos)

        Angle.listToBin(self._target, eos)

        Angle.listToBin(self._offset, eos)

        eos.writeInt(self._pointingModelId)

        eos.writeBool(self._overTheTopExists)
        if self._overTheTopExists:

            eos.writeBool(self._overTheTop)

        eos.writeBool(self._sourceOffsetExists)
        if self._sourceOffsetExists:

            Angle.listToBin(self._sourceOffset, eos)

        eos.writeBool(self._sourceOffsetReferenceCodeExists)
        if self._sourceOffsetReferenceCodeExists:

            eos.writeString(self._sourceOffsetReferenceCode.toString())

        eos.writeBool(self._sourceOffsetEquinoxExists)
        if self._sourceOffsetEquinoxExists:

            self._sourceOffsetEquinox.toBin(eos)

        eos.writeBool(self._sampledTimeIntervalExists)
        if self._sampledTimeIntervalExists:

            ArrayTimeInterval.listToBin(self._sampledTimeInterval, eos)

        eos.writeBool(self._atmosphericCorrectionExists)
        if self._atmosphericCorrectionExists:

            Angle.listToBin(self._atmosphericCorrection, eos)

    @staticmethod
    def antennaIdFromBin(row, eis):
        """
        Set the antennaId in row from the EndianInput (eis) instance.
        """

        row._antennaId = Tag.fromBin(eis)

    @staticmethod
    def timeIntervalFromBin(row, eis):
        """
        Set the timeInterval in row from the EndianInput (eis) instance.
        """

        row._timeInterval = ArrayTimeInterval.fromBin(eis)

    @staticmethod
    def numSampleFromBin(row, eis):
        """
        Set the numSample in row from the EndianInput (eis) instance.
        """

        row._numSample = eis.readInt()

    @staticmethod
    def encoderFromBin(row, eis):
        """
        Set the encoder in row from the EndianInput (eis) instance.
        """

        row._encoder = Angle.from2DBin(eis)

    @staticmethod
    def pointingTrackingFromBin(row, eis):
        """
        Set the pointingTracking in row from the EndianInput (eis) instance.
        """

        row._pointingTracking = eis.readBool()

    @staticmethod
    def usePolynomialsFromBin(row, eis):
        """
        Set the usePolynomials in row from the EndianInput (eis) instance.
        """

        row._usePolynomials = eis.readBool()

    @staticmethod
    def timeOriginFromBin(row, eis):
        """
        Set the timeOrigin in row from the EndianInput (eis) instance.
        """

        row._timeOrigin = ArrayTime.fromBin(eis)

    @staticmethod
    def numTermFromBin(row, eis):
        """
        Set the numTerm in row from the EndianInput (eis) instance.
        """

        row._numTerm = eis.readInt()

    @staticmethod
    def pointingDirectionFromBin(row, eis):
        """
        Set the pointingDirection in row from the EndianInput (eis) instance.
        """

        row._pointingDirection = Angle.from2DBin(eis)

    @staticmethod
    def targetFromBin(row, eis):
        """
        Set the target in row from the EndianInput (eis) instance.
        """

        row._target = Angle.from2DBin(eis)

    @staticmethod
    def offsetFromBin(row, eis):
        """
        Set the offset in row from the EndianInput (eis) instance.
        """

        row._offset = Angle.from2DBin(eis)

    @staticmethod
    def pointingModelIdFromBin(row, eis):
        """
        Set the pointingModelId in row from the EndianInput (eis) instance.
        """

        row._pointingModelId = eis.readInt()

    @staticmethod
    def overTheTopFromBin(row, eis):
        """
        Set the optional overTheTop in row from the EndianInput (eis) instance.
        """
        row._overTheTopExists = eis.readBool()
        if row._overTheTopExists:

            row._overTheTop = eis.readBool()

    @staticmethod
    def sourceOffsetFromBin(row, eis):
        """
        Set the optional sourceOffset in row from the EndianInput (eis) instance.
        """
        row._sourceOffsetExists = eis.readBool()
        if row._sourceOffsetExists:

            row._sourceOffset = Angle.from2DBin(eis)

    @staticmethod
    def sourceOffsetReferenceCodeFromBin(row, eis):
        """
        Set the optional sourceOffsetReferenceCode in row from the EndianInput (eis) instance.
        """
        row._sourceOffsetReferenceCodeExists = eis.readBool()
        if row._sourceOffsetReferenceCodeExists:

            row._sourceOffsetReferenceCode = DirectionReferenceCode.from_int(
                eis.readInt()
            )

    @staticmethod
    def sourceOffsetEquinoxFromBin(row, eis):
        """
        Set the optional sourceOffsetEquinox in row from the EndianInput (eis) instance.
        """
        row._sourceOffsetEquinoxExists = eis.readBool()
        if row._sourceOffsetEquinoxExists:

            row._sourceOffsetEquinox = ArrayTime.fromBin(eis)

    @staticmethod
    def sampledTimeIntervalFromBin(row, eis):
        """
        Set the optional sampledTimeInterval in row from the EndianInput (eis) instance.
        """
        row._sampledTimeIntervalExists = eis.readBool()
        if row._sampledTimeIntervalExists:

            row._sampledTimeInterval = ArrayTimeInterval.from1DBin(eis)

    @staticmethod
    def atmosphericCorrectionFromBin(row, eis):
        """
        Set the optional atmosphericCorrection in row from the EndianInput (eis) instance.
        """
        row._atmosphericCorrectionExists = eis.readBool()
        if row._atmosphericCorrectionExists:

            row._atmosphericCorrection = Angle.from2DBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaId"] = PointingRow.antennaIdFromBin
        _fromBinMethods["timeInterval"] = PointingRow.timeIntervalFromBin
        _fromBinMethods["numSample"] = PointingRow.numSampleFromBin
        _fromBinMethods["encoder"] = PointingRow.encoderFromBin
        _fromBinMethods["pointingTracking"] = PointingRow.pointingTrackingFromBin
        _fromBinMethods["usePolynomials"] = PointingRow.usePolynomialsFromBin
        _fromBinMethods["timeOrigin"] = PointingRow.timeOriginFromBin
        _fromBinMethods["numTerm"] = PointingRow.numTermFromBin
        _fromBinMethods["pointingDirection"] = PointingRow.pointingDirectionFromBin
        _fromBinMethods["target"] = PointingRow.targetFromBin
        _fromBinMethods["offset"] = PointingRow.offsetFromBin
        _fromBinMethods["pointingModelId"] = PointingRow.pointingModelIdFromBin

        _fromBinMethods["overTheTop"] = PointingRow.overTheTopFromBin
        _fromBinMethods["sourceOffset"] = PointingRow.sourceOffsetFromBin
        _fromBinMethods["sourceOffsetReferenceCode"] = (
            PointingRow.sourceOffsetReferenceCodeFromBin
        )
        _fromBinMethods["sourceOffsetEquinox"] = PointingRow.sourceOffsetEquinoxFromBin
        _fromBinMethods["sampledTimeInterval"] = PointingRow.sampledTimeIntervalFromBin
        _fromBinMethods["atmosphericCorrection"] = (
            PointingRow.atmosphericCorrectionFromBin
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

        row = PointingRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Pointing",
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

    # ===> Attribute numSample

    _numSample = 0

    def getNumSample(self):
        """
        Get numSample.
        return numSample as int
        """

        return self._numSample

    def setNumSample(self, numSample):
        """
        Set numSample with the specified int value.
        numSample The int value to which numSample is to be set.


        """

        self._numSample = int(numSample)

    # ===> Attribute encoder

    _encoder = None  # this is a 2D list of Angle

    def getEncoder(self):
        """
        Get encoder.
        return encoder as Angle []  []
        """

        return copy.deepcopy(self._encoder)

    def setEncoder(self, encoder):
        """
        Set encoder with the specified Angle []  []  value.
        encoder The Angle []  []  value to which encoder is to be set.
        The value of encoder can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(encoder, list):
            raise ValueError("The value of encoder must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(encoder)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of encoder is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(encoder, Angle):
                raise ValueError(
                    "type of the first value in encoder is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._encoder = copy.deepcopy(encoder)
        except Exception as exc:
            raise ValueError("Invalid encoder : " + str(exc))

    # ===> Attribute pointingTracking

    _pointingTracking = None

    def getPointingTracking(self):
        """
        Get pointingTracking.
        return pointingTracking as bool
        """

        return self._pointingTracking

    def setPointingTracking(self, pointingTracking):
        """
        Set pointingTracking with the specified bool value.
        pointingTracking The bool value to which pointingTracking is to be set.


        """

        self._pointingTracking = bool(pointingTracking)

    # ===> Attribute usePolynomials

    _usePolynomials = None

    def getUsePolynomials(self):
        """
        Get usePolynomials.
        return usePolynomials as bool
        """

        return self._usePolynomials

    def setUsePolynomials(self, usePolynomials):
        """
        Set usePolynomials with the specified bool value.
        usePolynomials The bool value to which usePolynomials is to be set.


        """

        self._usePolynomials = bool(usePolynomials)

    # ===> Attribute timeOrigin

    _timeOrigin = ArrayTime()

    def getTimeOrigin(self):
        """
        Get timeOrigin.
        return timeOrigin as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._timeOrigin)

    def setTimeOrigin(self, timeOrigin):
        """
        Set timeOrigin with the specified ArrayTime value.
        timeOrigin The ArrayTime value to which timeOrigin is to be set.
        The value of timeOrigin can be anything allowed by the ArrayTime constructor.

        """

        self._timeOrigin = ArrayTime(timeOrigin)

    # ===> Attribute numTerm

    _numTerm = 0

    def getNumTerm(self):
        """
        Get numTerm.
        return numTerm as int
        """

        return self._numTerm

    def setNumTerm(self, numTerm):
        """
        Set numTerm with the specified int value.
        numTerm The int value to which numTerm is to be set.


        """

        self._numTerm = int(numTerm)

    # ===> Attribute pointingDirection

    _pointingDirection = None  # this is a 2D list of Angle

    def getPointingDirection(self):
        """
        Get pointingDirection.
        return pointingDirection as Angle []  []
        """

        return copy.deepcopy(self._pointingDirection)

    def setPointingDirection(self, pointingDirection):
        """
        Set pointingDirection with the specified Angle []  []  value.
        pointingDirection The Angle []  []  value to which pointingDirection is to be set.
        The value of pointingDirection can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(pointingDirection, list):
            raise ValueError("The value of pointingDirection must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(pointingDirection)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of pointingDirection is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(pointingDirection, Angle):
                raise ValueError(
                    "type of the first value in pointingDirection is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._pointingDirection = copy.deepcopy(pointingDirection)
        except Exception as exc:
            raise ValueError("Invalid pointingDirection : " + str(exc))

    # ===> Attribute target

    _target = None  # this is a 2D list of Angle

    def getTarget(self):
        """
        Get target.
        return target as Angle []  []
        """

        return copy.deepcopy(self._target)

    def setTarget(self, target):
        """
        Set target with the specified Angle []  []  value.
        target The Angle []  []  value to which target is to be set.
        The value of target can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(target, list):
            raise ValueError("The value of target must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(target)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of target is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(target, Angle):
                raise ValueError(
                    "type of the first value in target is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._target = copy.deepcopy(target)
        except Exception as exc:
            raise ValueError("Invalid target : " + str(exc))

    # ===> Attribute offset

    _offset = None  # this is a 2D list of Angle

    def getOffset(self):
        """
        Get offset.
        return offset as Angle []  []
        """

        return copy.deepcopy(self._offset)

    def setOffset(self, offset):
        """
        Set offset with the specified Angle []  []  value.
        offset The Angle []  []  value to which offset is to be set.
        The value of offset can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(offset, list):
            raise ValueError("The value of offset must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(offset)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of offset is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(offset, Angle):
                raise ValueError(
                    "type of the first value in offset is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._offset = copy.deepcopy(offset)
        except Exception as exc:
            raise ValueError("Invalid offset : " + str(exc))

    # ===> Attribute overTheTop, which is optional
    _overTheTopExists = False

    _overTheTop = None

    def isOverTheTopExists(self):
        """
        The attribute overTheTop is optional. Return True if this attribute exists.
        return True if and only if the overTheTop attribute exists.
        """
        return self._overTheTopExists

    def getOverTheTop(self):
        """
        Get overTheTop, which is optional.
        return overTheTop as bool
        raises ValueError If overTheTop does not exist.
        """
        if not self._overTheTopExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + overTheTop
                + " attribute in table Pointing does not exist!"
            )

        return self._overTheTop

    def setOverTheTop(self, overTheTop):
        """
        Set overTheTop with the specified bool value.
        overTheTop The bool value to which overTheTop is to be set.


        """

        self._overTheTop = bool(overTheTop)

        self._overTheTopExists = True

    def clearOverTheTop(self):
        """
        Mark overTheTop, which is an optional field, as non-existent.
        """
        self._overTheTopExists = False

    # ===> Attribute sourceOffset, which is optional
    _sourceOffsetExists = False

    _sourceOffset = None  # this is a 2D list of Angle

    def isSourceOffsetExists(self):
        """
        The attribute sourceOffset is optional. Return True if this attribute exists.
        return True if and only if the sourceOffset attribute exists.
        """
        return self._sourceOffsetExists

    def getSourceOffset(self):
        """
        Get sourceOffset, which is optional.
        return sourceOffset as Angle []  []
        raises ValueError If sourceOffset does not exist.
        """
        if not self._sourceOffsetExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sourceOffset
                + " attribute in table Pointing does not exist!"
            )

        return copy.deepcopy(self._sourceOffset)

    def setSourceOffset(self, sourceOffset):
        """
        Set sourceOffset with the specified Angle []  []  value.
        sourceOffset The Angle []  []  value to which sourceOffset is to be set.
        The value of sourceOffset can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(sourceOffset, list):
            raise ValueError("The value of sourceOffset must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(sourceOffset)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of sourceOffset is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(sourceOffset, Angle):
                raise ValueError(
                    "type of the first value in sourceOffset is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._sourceOffset = copy.deepcopy(sourceOffset)
        except Exception as exc:
            raise ValueError("Invalid sourceOffset : " + str(exc))

        self._sourceOffsetExists = True

    def clearSourceOffset(self):
        """
        Mark sourceOffset, which is an optional field, as non-existent.
        """
        self._sourceOffsetExists = False

    # ===> Attribute sourceOffsetReferenceCode, which is optional
    _sourceOffsetReferenceCodeExists = False

    _sourceOffsetReferenceCode = DirectionReferenceCode.from_int(0)

    def isSourceOffsetReferenceCodeExists(self):
        """
        The attribute sourceOffsetReferenceCode is optional. Return True if this attribute exists.
        return True if and only if the sourceOffsetReferenceCode attribute exists.
        """
        return self._sourceOffsetReferenceCodeExists

    def getSourceOffsetReferenceCode(self):
        """
        Get sourceOffsetReferenceCode, which is optional.
        return sourceOffsetReferenceCode as DirectionReferenceCode
        raises ValueError If sourceOffsetReferenceCode does not exist.
        """
        if not self._sourceOffsetReferenceCodeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sourceOffsetReferenceCode
                + " attribute in table Pointing does not exist!"
            )

        return self._sourceOffsetReferenceCode

    def setSourceOffsetReferenceCode(self, sourceOffsetReferenceCode):
        """
        Set sourceOffsetReferenceCode with the specified DirectionReferenceCode value.
        sourceOffsetReferenceCode The DirectionReferenceCode value to which sourceOffsetReferenceCode is to be set.


        """

        self._sourceOffsetReferenceCode = DirectionReferenceCode(
            sourceOffsetReferenceCode
        )

        self._sourceOffsetReferenceCodeExists = True

    def clearSourceOffsetReferenceCode(self):
        """
        Mark sourceOffsetReferenceCode, which is an optional field, as non-existent.
        """
        self._sourceOffsetReferenceCodeExists = False

    # ===> Attribute sourceOffsetEquinox, which is optional
    _sourceOffsetEquinoxExists = False

    _sourceOffsetEquinox = ArrayTime()

    def isSourceOffsetEquinoxExists(self):
        """
        The attribute sourceOffsetEquinox is optional. Return True if this attribute exists.
        return True if and only if the sourceOffsetEquinox attribute exists.
        """
        return self._sourceOffsetEquinoxExists

    def getSourceOffsetEquinox(self):
        """
        Get sourceOffsetEquinox, which is optional.
        return sourceOffsetEquinox as ArrayTime
        raises ValueError If sourceOffsetEquinox does not exist.
        """
        if not self._sourceOffsetEquinoxExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sourceOffsetEquinox
                + " attribute in table Pointing does not exist!"
            )

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._sourceOffsetEquinox)

    def setSourceOffsetEquinox(self, sourceOffsetEquinox):
        """
        Set sourceOffsetEquinox with the specified ArrayTime value.
        sourceOffsetEquinox The ArrayTime value to which sourceOffsetEquinox is to be set.
        The value of sourceOffsetEquinox can be anything allowed by the ArrayTime constructor.

        """

        self._sourceOffsetEquinox = ArrayTime(sourceOffsetEquinox)

        self._sourceOffsetEquinoxExists = True

    def clearSourceOffsetEquinox(self):
        """
        Mark sourceOffsetEquinox, which is an optional field, as non-existent.
        """
        self._sourceOffsetEquinoxExists = False

    # ===> Attribute sampledTimeInterval, which is optional
    _sampledTimeIntervalExists = False

    _sampledTimeInterval = None  # this is a 1D list of ArrayTimeInterval

    def isSampledTimeIntervalExists(self):
        """
        The attribute sampledTimeInterval is optional. Return True if this attribute exists.
        return True if and only if the sampledTimeInterval attribute exists.
        """
        return self._sampledTimeIntervalExists

    def getSampledTimeInterval(self):
        """
        Get sampledTimeInterval, which is optional.
        return sampledTimeInterval as ArrayTimeInterval []
        raises ValueError If sampledTimeInterval does not exist.
        """
        if not self._sampledTimeIntervalExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sampledTimeInterval
                + " attribute in table Pointing does not exist!"
            )

        return copy.deepcopy(self._sampledTimeInterval)

    def setSampledTimeInterval(self, sampledTimeInterval):
        """
        Set sampledTimeInterval with the specified ArrayTimeInterval []  value.
        sampledTimeInterval The ArrayTimeInterval []  value to which sampledTimeInterval is to be set.
        The value of sampledTimeInterval can be anything allowed by the ArrayTimeInterval []  constructor.

        """

        # value must be a list
        if not isinstance(sampledTimeInterval, list):
            raise ValueError("The value of sampledTimeInterval must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(sampledTimeInterval)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of sampledTimeInterval is not correct")

            # the type of the values in the list must be ArrayTimeInterval
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(sampledTimeInterval, ArrayTimeInterval):
                raise ValueError(
                    "type of the first value in sampledTimeInterval is not ArrayTimeInterval as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._sampledTimeInterval = copy.deepcopy(sampledTimeInterval)
        except Exception as exc:
            raise ValueError("Invalid sampledTimeInterval : " + str(exc))

        self._sampledTimeIntervalExists = True

    def clearSampledTimeInterval(self):
        """
        Mark sampledTimeInterval, which is an optional field, as non-existent.
        """
        self._sampledTimeIntervalExists = False

    # ===> Attribute atmosphericCorrection, which is optional
    _atmosphericCorrectionExists = False

    _atmosphericCorrection = None  # this is a 2D list of Angle

    def isAtmosphericCorrectionExists(self):
        """
        The attribute atmosphericCorrection is optional. Return True if this attribute exists.
        return True if and only if the atmosphericCorrection attribute exists.
        """
        return self._atmosphericCorrectionExists

    def getAtmosphericCorrection(self):
        """
        Get atmosphericCorrection, which is optional.
        return atmosphericCorrection as Angle []  []
        raises ValueError If atmosphericCorrection does not exist.
        """
        if not self._atmosphericCorrectionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + atmosphericCorrection
                + " attribute in table Pointing does not exist!"
            )

        return copy.deepcopy(self._atmosphericCorrection)

    def setAtmosphericCorrection(self, atmosphericCorrection):
        """
        Set atmosphericCorrection with the specified Angle []  []  value.
        atmosphericCorrection The Angle []  []  value to which atmosphericCorrection is to be set.
        The value of atmosphericCorrection can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(atmosphericCorrection, list):
            raise ValueError("The value of atmosphericCorrection must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(atmosphericCorrection)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of atmosphericCorrection is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(atmosphericCorrection, Angle):
                raise ValueError(
                    "type of the first value in atmosphericCorrection is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._atmosphericCorrection = copy.deepcopy(atmosphericCorrection)
        except Exception as exc:
            raise ValueError("Invalid atmosphericCorrection : " + str(exc))

        self._atmosphericCorrectionExists = True

    def clearAtmosphericCorrection(self):
        """
        Mark atmosphericCorrection, which is an optional field, as non-existent.
        """
        self._atmosphericCorrectionExists = False

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

    # ===> Attribute pointingModelId

    _pointingModelId = 0

    def getPointingModelId(self):
        """
        Get pointingModelId.
        return pointingModelId as int
        """

        return self._pointingModelId

    def setPointingModelId(self, pointingModelId):
        """
        Set pointingModelId with the specified int value.
        pointingModelId The int value to which pointingModelId is to be set.


        """

        self._pointingModelId = int(pointingModelId)

    # Links

    # ===> Slice link from a row of Pointing table to a collection of row of PointingModel table.
    def getPointingModels(self):
        """
        Get the collection of rows in the PointingModel table having pointingModelId == this.pointingModelId
        """

        return (
            self._table.getContainer()
            .getPointingModel()
            .getRowByPointingModelId(self._pointingModelId)
        )

    def getAntennaUsingAntennaId(self):
        """
        Returns the row in the Antenna table having Antenna.antennaId == antennaId

        """

        return self._table.getContainer().getAntenna().getRowByKey(self._antennaId)

    # comparison methods

    def compareNoAutoInc(
        self,
        antennaId,
        timeInterval,
        numSample,
        encoder,
        pointingTracking,
        usePolynomials,
        timeOrigin,
        numTerm,
        pointingDirection,
        target,
        offset,
        pointingModelId,
    ):
        """
        Compare each attribute except the autoincrementable one of this PointingRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaId is a Tag, compare using the equals method.
        if not self._antennaId.equals(antennaId):
            return False

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # numSample is a int, compare using the == operator.
        if not (self._numSample == numSample):
            return False

        # We compare two 2D arrays (lists).
        if encoder is not None:
            if self._encoder is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            encoder_dims = pyasdm.utils.getListDims(encoder)
            this_encoder_dims = pyasdm.utils.getListDims(self._encoder)
            if encoder_dims != this_encoder_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(encoder_dims[0]):
                for j in range(encoder_dims[1]):

                    # encoder is a Angle, compare using the almostEquals method.
                    if not (
                        self._encoder[i][j].almostEquals(
                            encoder[i][j], self.getTable().getEncoderEqTolerance()
                        )
                    ):
                        return False

        # pointingTracking is a bool, compare using the == operator.
        if not (self._pointingTracking == pointingTracking):
            return False

        # usePolynomials is a bool, compare using the == operator.
        if not (self._usePolynomials == usePolynomials):
            return False

        # timeOrigin is a ArrayTime, compare using the equals method.
        if not self._timeOrigin.equals(timeOrigin):
            return False

        # numTerm is a int, compare using the == operator.
        if not (self._numTerm == numTerm):
            return False

        # We compare two 2D arrays (lists).
        if pointingDirection is not None:
            if self._pointingDirection is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            pointingDirection_dims = pyasdm.utils.getListDims(pointingDirection)
            this_pointingDirection_dims = pyasdm.utils.getListDims(
                self._pointingDirection
            )
            if pointingDirection_dims != this_pointingDirection_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(pointingDirection_dims[0]):
                for j in range(pointingDirection_dims[1]):

                    # pointingDirection is a Angle, compare using the almostEquals method.
                    if not (
                        self._pointingDirection[i][j].almostEquals(
                            pointingDirection[i][j],
                            self.getTable().getPointingDirectionEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if target is not None:
            if self._target is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            target_dims = pyasdm.utils.getListDims(target)
            this_target_dims = pyasdm.utils.getListDims(self._target)
            if target_dims != this_target_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(target_dims[0]):
                for j in range(target_dims[1]):

                    # target is a Angle, compare using the almostEquals method.
                    if not (
                        self._target[i][j].almostEquals(
                            target[i][j], self.getTable().getTargetEqTolerance()
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if offset is not None:
            if self._offset is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            offset_dims = pyasdm.utils.getListDims(offset)
            this_offset_dims = pyasdm.utils.getListDims(self._offset)
            if offset_dims != this_offset_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(offset_dims[0]):
                for j in range(offset_dims[1]):

                    # offset is a Angle, compare using the almostEquals method.
                    if not (
                        self._offset[i][j].almostEquals(
                            offset[i][j], self.getTable().getOffsetEqTolerance()
                        )
                    ):
                        return False

        # pointingModelId is a int, compare using the == operator.
        if not (self._pointingModelId == pointingModelId):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumSample(),
            otherRow.getEncoder(),
            otherRow.getPointingTracking(),
            otherRow.getUsePolynomials(),
            otherRow.getTimeOrigin(),
            otherRow.getNumTerm(),
            otherRow.getPointingDirection(),
            otherRow.getTarget(),
            otherRow.getOffset(),
            otherRow.getPointingModelId(),
        )

    def compareRequiredValue(
        self,
        numSample,
        encoder,
        pointingTracking,
        usePolynomials,
        timeOrigin,
        numTerm,
        pointingDirection,
        target,
        offset,
        pointingModelId,
    ):

        # numSample is a int, compare using the == operator.
        if not (self._numSample == numSample):
            return False

        # We compare two 2D arrays (lists).
        if encoder is not None:
            if self._encoder is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            encoder_dims = pyasdm.utils.getListDims(encoder)
            this_encoder_dims = pyasdm.utils.getListDims(self._encoder)
            if encoder_dims != this_encoder_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(encoder_dims[0]):
                for j in range(encoder_dims[1]):

                    # encoder is a Angle, compare using the almostEquals method.
                    if not (
                        self._encoder[i][j].almostEquals(
                            encoder[i][j], self.getTable().getEncoderEqTolerance()
                        )
                    ):
                        return False

        # pointingTracking is a bool, compare using the == operator.
        if not (self._pointingTracking == pointingTracking):
            return False

        # usePolynomials is a bool, compare using the == operator.
        if not (self._usePolynomials == usePolynomials):
            return False

        # timeOrigin is a ArrayTime, compare using the equals method.
        if not self._timeOrigin.equals(timeOrigin):
            return False

        # numTerm is a int, compare using the == operator.
        if not (self._numTerm == numTerm):
            return False

        # We compare two 2D arrays (lists).
        if pointingDirection is not None:
            if self._pointingDirection is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            pointingDirection_dims = pyasdm.utils.getListDims(pointingDirection)
            this_pointingDirection_dims = pyasdm.utils.getListDims(
                self._pointingDirection
            )
            if pointingDirection_dims != this_pointingDirection_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(pointingDirection_dims[0]):
                for j in range(pointingDirection_dims[1]):

                    # pointingDirection is a Angle, compare using the almostEquals method.
                    if not (
                        self._pointingDirection[i][j].almostEquals(
                            pointingDirection[i][j],
                            self.getTable().getPointingDirectionEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if target is not None:
            if self._target is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            target_dims = pyasdm.utils.getListDims(target)
            this_target_dims = pyasdm.utils.getListDims(self._target)
            if target_dims != this_target_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(target_dims[0]):
                for j in range(target_dims[1]):

                    # target is a Angle, compare using the almostEquals method.
                    if not (
                        self._target[i][j].almostEquals(
                            target[i][j], self.getTable().getTargetEqTolerance()
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if offset is not None:
            if self._offset is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            offset_dims = pyasdm.utils.getListDims(offset)
            this_offset_dims = pyasdm.utils.getListDims(self._offset)
            if offset_dims != this_offset_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(offset_dims[0]):
                for j in range(offset_dims[1]):

                    # offset is a Angle, compare using the almostEquals method.
                    if not (
                        self._offset[i][j].almostEquals(
                            offset[i][j], self.getTable().getOffsetEqTolerance()
                        )
                    ):
                        return False

        # pointingModelId is a int, compare using the == operator.
        if not (self._pointingModelId == pointingModelId):
            return False

        return True


# initialize the dictionary that maps fields to init methods
PointingRow.initFromBinMethods()
