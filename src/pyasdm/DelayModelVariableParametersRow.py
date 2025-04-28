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
# File DelayModelVariableParametersRow.py
#

import pyasdm.DelayModelVariableParametersTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.DifferenceType import DifferenceType


from pyasdm.enumerations.DifferenceType import DifferenceType


from xml.dom import minidom

import copy


class DelayModelVariableParametersRow:
    """
    The DelayModelVariableParametersRow class is a row of a DelayModelVariableParametersTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a DelayModelVariableParametersRow.
        When row is None, create an empty row attached to table, which must be a DelayModelVariableParametersTable.
        When row is given, copy those values in to the new row. The row argument must be a DelayModelVariableParametersRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.DelayModelVariableParametersTable):
            raise ValueError("table must be a DelayModelVariableParametersTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._delayModelVariableParametersId = Tag()

        self._time = ArrayTime()

        self._ut1_utc = None

        self._iat_utc = None

        self._timeType = DifferenceType.from_int(0)

        self._gstAtUt0 = Angle()

        self._earthRotationRate = AngularRate()

        self._polarOffsets = []  # this is a list of float []

        self._polarOffsetsType = DifferenceType.from_int(0)

        self._nutationInLongitudeExists = False

        self._nutationInLongitude = Angle()

        self._nutationInLongitudeRateExists = False

        self._nutationInLongitudeRate = AngularRate()

        self._nutationInObliquityExists = False

        self._nutationInObliquity = Angle()

        self._nutationInObliquityRateExists = False

        self._nutationInObliquityRate = AngularRate()

        # extrinsic attributes

        self._delayModelFixedParametersId = Tag()

        if row is not None:
            if not isinstance(row, DelayModelVariableParametersRow):
                raise ValueError("row must be a DelayModelVariableParametersRow")

            # copy constructor

            self._delayModelVariableParametersId = Tag(
                row._delayModelVariableParametersId
            )

            self._time = ArrayTime(row._time)

            self._ut1_utc = row._ut1_utc

            self._iat_utc = row._iat_utc

            # We force the attribute of the result to be not None
            if row._timeType is None:
                self._timeType = DifferenceType.from_int(0)
            else:
                self._timeType = DifferenceType(row._timeType)

            self._gstAtUt0 = Angle(row._gstAtUt0)

            self._earthRotationRate = AngularRate(row._earthRotationRate)

            # polarOffsets is a  list , make a deep copy
            self._polarOffsets = copy.deepcopy(row._polarOffsets)

            # We force the attribute of the result to be not None
            if row._polarOffsetsType is None:
                self._polarOffsetsType = DifferenceType.from_int(0)
            else:
                self._polarOffsetsType = DifferenceType(row._polarOffsetsType)

            self._delayModelFixedParametersId = Tag(row._delayModelFixedParametersId)

            # by default set systematically nutationInLongitude's value to something not None

            if row._nutationInLongitudeExists:

                self._nutationInLongitude = Angle(row._nutationInLongitude)

                self._nutationInLongitudeExists = True

            # by default set systematically nutationInLongitudeRate's value to something not None

            if row._nutationInLongitudeRateExists:

                self._nutationInLongitudeRate = AngularRate(
                    row._nutationInLongitudeRate
                )

                self._nutationInLongitudeRateExists = True

            # by default set systematically nutationInObliquity's value to something not None

            if row._nutationInObliquityExists:

                self._nutationInObliquity = Angle(row._nutationInObliquity)

                self._nutationInObliquityExists = True

            # by default set systematically nutationInObliquityRate's value to something not None

            if row._nutationInObliquityRateExists:

                self._nutationInObliquityRate = AngularRate(
                    row._nutationInObliquityRate
                )

                self._nutationInObliquityRateExists = True

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

        result += Parser.extendedValueToXML(
            "delayModelVariableParametersId", self._delayModelVariableParametersId
        )

        result += Parser.extendedValueToXML("time", self._time)

        result += Parser.valueToXML("ut1_utc", self._ut1_utc)

        result += Parser.valueToXML("iat_utc", self._iat_utc)

        result += Parser.valueToXML("timeType", DifferenceType.name(self._timeType))

        result += Parser.extendedValueToXML("gstAtUt0", self._gstAtUt0)

        result += Parser.extendedValueToXML(
            "earthRotationRate", self._earthRotationRate
        )

        result += Parser.listValueToXML("polarOffsets", self._polarOffsets)

        result += Parser.valueToXML(
            "polarOffsetsType", DifferenceType.name(self._polarOffsetsType)
        )

        if self._nutationInLongitudeExists:

            result += Parser.extendedValueToXML(
                "nutationInLongitude", self._nutationInLongitude
            )

        if self._nutationInLongitudeRateExists:

            result += Parser.extendedValueToXML(
                "nutationInLongitudeRate", self._nutationInLongitudeRate
            )

        if self._nutationInObliquityExists:

            result += Parser.extendedValueToXML(
                "nutationInObliquity", self._nutationInObliquity
            )

        if self._nutationInObliquityRateExists:

            result += Parser.extendedValueToXML(
                "nutationInObliquityRate", self._nutationInObliquityRate
            )

        # extrinsic attributes

        result += Parser.extendedValueToXML(
            "delayModelFixedParametersId", self._delayModelFixedParametersId
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
                "xmlrow is not a string or a minidom.Element",
                "DelayModelVariableParametersTable",
            )

        if rowdom.nodeName != "row":
            raise ConversionException(
                "the argument is not a row", "DelayModelVariableParametersTable"
            )

        # intrinsic attribute values

        delayModelVariableParametersIdNode = rowdom.getElementsByTagName(
            "delayModelVariableParametersId"
        )[0]

        self._delayModelVariableParametersId = Tag(
            delayModelVariableParametersIdNode.firstChild.data.strip()
        )

        timeNode = rowdom.getElementsByTagName("time")[0]

        self._time = ArrayTime(timeNode.firstChild.data.strip())

        ut1_utcNode = rowdom.getElementsByTagName("ut1_utc")[0]

        self._ut1_utc = float(ut1_utcNode.firstChild.data.strip())

        iat_utcNode = rowdom.getElementsByTagName("iat_utc")[0]

        self._iat_utc = float(iat_utcNode.firstChild.data.strip())

        timeTypeNode = rowdom.getElementsByTagName("timeType")[0]

        self._timeType = DifferenceType.newDifferenceType(
            timeTypeNode.firstChild.data.strip()
        )

        gstAtUt0Node = rowdom.getElementsByTagName("gstAtUt0")[0]

        self._gstAtUt0 = Angle(gstAtUt0Node.firstChild.data.strip())

        earthRotationRateNode = rowdom.getElementsByTagName("earthRotationRate")[0]

        self._earthRotationRate = AngularRate(
            earthRotationRateNode.firstChild.data.strip()
        )

        polarOffsetsNode = rowdom.getElementsByTagName("polarOffsets")[0]

        polarOffsetsStr = polarOffsetsNode.firstChild.data.strip()

        self._polarOffsets = Parser.stringListToLists(
            polarOffsetsStr, float, "DelayModelVariableParameters", False
        )

        polarOffsetsTypeNode = rowdom.getElementsByTagName("polarOffsetsType")[0]

        self._polarOffsetsType = DifferenceType.newDifferenceType(
            polarOffsetsTypeNode.firstChild.data.strip()
        )

        nutationInLongitudeNode = rowdom.getElementsByTagName("nutationInLongitude")
        if len(nutationInLongitudeNode) > 0:

            self._nutationInLongitude = Angle(
                nutationInLongitudeNode[0].firstChild.data.strip()
            )

            self._nutationInLongitudeExists = True

        nutationInLongitudeRateNode = rowdom.getElementsByTagName(
            "nutationInLongitudeRate"
        )
        if len(nutationInLongitudeRateNode) > 0:

            self._nutationInLongitudeRate = AngularRate(
                nutationInLongitudeRateNode[0].firstChild.data.strip()
            )

            self._nutationInLongitudeRateExists = True

        nutationInObliquityNode = rowdom.getElementsByTagName("nutationInObliquity")
        if len(nutationInObliquityNode) > 0:

            self._nutationInObliquity = Angle(
                nutationInObliquityNode[0].firstChild.data.strip()
            )

            self._nutationInObliquityExists = True

        nutationInObliquityRateNode = rowdom.getElementsByTagName(
            "nutationInObliquityRate"
        )
        if len(nutationInObliquityRateNode) > 0:

            self._nutationInObliquityRate = AngularRate(
                nutationInObliquityRateNode[0].firstChild.data.strip()
            )

            self._nutationInObliquityRateExists = True

        # extrinsic attribute values

        delayModelFixedParametersIdNode = rowdom.getElementsByTagName(
            "delayModelFixedParametersId"
        )[0]

        self._delayModelFixedParametersId = Tag(
            delayModelFixedParametersIdNode.firstChild.data.strip()
        )

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._delayModelVariableParametersId.toBin(eos)

        self._time.toBin(eos)

        eos.writeFloat(self._ut1_utc)

        eos.writeFloat(self._iat_utc)

        eos.writeString(str(self._timeType))

        self._gstAtUt0.toBin(eos)

        self._earthRotationRate.toBin(eos)

        eos.writeInt(len(self._polarOffsets))
        for i in range(len(self._polarOffsets)):

            eos.writeFloat(self._polarOffsets[i])

        eos.writeString(str(self._polarOffsetsType))

        self._delayModelFixedParametersId.toBin(eos)

        eos.writeBool(self._nutationInLongitudeExists)
        if self._nutationInLongitudeExists:

            self._nutationInLongitude.toBin(eos)

        eos.writeBool(self._nutationInLongitudeRateExists)
        if self._nutationInLongitudeRateExists:

            self._nutationInLongitudeRate.toBin(eos)

        eos.writeBool(self._nutationInObliquityExists)
        if self._nutationInObliquityExists:

            self._nutationInObliquity.toBin(eos)

        eos.writeBool(self._nutationInObliquityRateExists)
        if self._nutationInObliquityRateExists:

            self._nutationInObliquityRate.toBin(eos)

    @staticmethod
    def delayModelVariableParametersIdFromBin(row, eis):
        """
        Set the delayModelVariableParametersId in row from the EndianInput (eis) instance.
        """

        row._delayModelVariableParametersId = Tag.fromBin(eis)

    @staticmethod
    def timeFromBin(row, eis):
        """
        Set the time in row from the EndianInput (eis) instance.
        """

        row._time = ArrayTime.fromBin(eis)

    @staticmethod
    def ut1_utcFromBin(row, eis):
        """
        Set the ut1_utc in row from the EndianInput (eis) instance.
        """

        row._ut1_utc = eis.readFloat()

    @staticmethod
    def iat_utcFromBin(row, eis):
        """
        Set the iat_utc in row from the EndianInput (eis) instance.
        """

        row._iat_utc = eis.readFloat()

    @staticmethod
    def timeTypeFromBin(row, eis):
        """
        Set the timeType in row from the EndianInput (eis) instance.
        """

        row._timeType = DifferenceType.literal(eis.readString())

    @staticmethod
    def gstAtUt0FromBin(row, eis):
        """
        Set the gstAtUt0 in row from the EndianInput (eis) instance.
        """

        row._gstAtUt0 = Angle.fromBin(eis)

    @staticmethod
    def earthRotationRateFromBin(row, eis):
        """
        Set the earthRotationRate in row from the EndianInput (eis) instance.
        """

        row._earthRotationRate = AngularRate.fromBin(eis)

    @staticmethod
    def polarOffsetsFromBin(row, eis):
        """
        Set the polarOffsets in row from the EndianInput (eis) instance.
        """

        polarOffsetsDim1 = eis.readInt()
        thisList = []
        for i in range(polarOffsetsDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._polarOffsets = thisList

    @staticmethod
    def polarOffsetsTypeFromBin(row, eis):
        """
        Set the polarOffsetsType in row from the EndianInput (eis) instance.
        """

        row._polarOffsetsType = DifferenceType.literal(eis.readString())

    @staticmethod
    def delayModelFixedParametersIdFromBin(row, eis):
        """
        Set the delayModelFixedParametersId in row from the EndianInput (eis) instance.
        """

        row._delayModelFixedParametersId = Tag.fromBin(eis)

    @staticmethod
    def nutationInLongitudeFromBin(row, eis):
        """
        Set the optional nutationInLongitude in row from the EndianInput (eis) instance.
        """
        row._nutationInLongitudeExists = eis.readBool()
        if row._nutationInLongitudeExists:

            row._nutationInLongitude = Angle.fromBin(eis)

    @staticmethod
    def nutationInLongitudeRateFromBin(row, eis):
        """
        Set the optional nutationInLongitudeRate in row from the EndianInput (eis) instance.
        """
        row._nutationInLongitudeRateExists = eis.readBool()
        if row._nutationInLongitudeRateExists:

            row._nutationInLongitudeRate = AngularRate.fromBin(eis)

    @staticmethod
    def nutationInObliquityFromBin(row, eis):
        """
        Set the optional nutationInObliquity in row from the EndianInput (eis) instance.
        """
        row._nutationInObliquityExists = eis.readBool()
        if row._nutationInObliquityExists:

            row._nutationInObliquity = Angle.fromBin(eis)

    @staticmethod
    def nutationInObliquityRateFromBin(row, eis):
        """
        Set the optional nutationInObliquityRate in row from the EndianInput (eis) instance.
        """
        row._nutationInObliquityRateExists = eis.readBool()
        if row._nutationInObliquityRateExists:

            row._nutationInObliquityRate = AngularRate.fromBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["delayModelVariableParametersId"] = (
            DelayModelVariableParametersRow.delayModelVariableParametersIdFromBin
        )
        _fromBinMethods["time"] = DelayModelVariableParametersRow.timeFromBin
        _fromBinMethods["ut1_utc"] = DelayModelVariableParametersRow.ut1_utcFromBin
        _fromBinMethods["iat_utc"] = DelayModelVariableParametersRow.iat_utcFromBin
        _fromBinMethods["timeType"] = DelayModelVariableParametersRow.timeTypeFromBin
        _fromBinMethods["gstAtUt0"] = DelayModelVariableParametersRow.gstAtUt0FromBin
        _fromBinMethods["earthRotationRate"] = (
            DelayModelVariableParametersRow.earthRotationRateFromBin
        )
        _fromBinMethods["polarOffsets"] = (
            DelayModelVariableParametersRow.polarOffsetsFromBin
        )
        _fromBinMethods["polarOffsetsType"] = (
            DelayModelVariableParametersRow.polarOffsetsTypeFromBin
        )
        _fromBinMethods["delayModelFixedParametersId"] = (
            DelayModelVariableParametersRow.delayModelFixedParametersIdFromBin
        )

        _fromBinMethods["nutationInLongitude"] = (
            DelayModelVariableParametersRow.nutationInLongitudeFromBin
        )
        _fromBinMethods["nutationInLongitudeRate"] = (
            DelayModelVariableParametersRow.nutationInLongitudeRateFromBin
        )
        _fromBinMethods["nutationInObliquity"] = (
            DelayModelVariableParametersRow.nutationInObliquityFromBin
        )
        _fromBinMethods["nutationInObliquityRate"] = (
            DelayModelVariableParametersRow.nutationInObliquityRateFromBin
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

        row = DelayModelVariableParametersRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " DelayModelVariableParameters",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute delayModelVariableParametersId

    _delayModelVariableParametersId = Tag()

    def getDelayModelVariableParametersId(self):
        """
        Get delayModelVariableParametersId.
        return delayModelVariableParametersId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._delayModelVariableParametersId)

    def setDelayModelVariableParametersId(self, delayModelVariableParametersId):
        """
        Set delayModelVariableParametersId with the specified Tag value.
        delayModelVariableParametersId The Tag value to which delayModelVariableParametersId is to be set.
        The value of delayModelVariableParametersId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the delayModelVariableParametersId field, which is part of the key, after this row has been added to this table."
            )

        self._delayModelVariableParametersId = Tag(delayModelVariableParametersId)

    # ===> Attribute time

    _time = ArrayTime()

    def getTime(self):
        """
        Get time.
        return time as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._time)

    def setTime(self, time):
        """
        Set time with the specified ArrayTime value.
        time The ArrayTime value to which time is to be set.
        The value of time can be anything allowed by the ArrayTime constructor.

        """

        self._time = ArrayTime(time)

    # ===> Attribute ut1_utc

    _ut1_utc = None

    def getUt1_utc(self):
        """
        Get ut1_utc.
        return ut1_utc as float
        """

        return self._ut1_utc

    def setUt1_utc(self, ut1_utc):
        """
        Set ut1_utc with the specified float value.
        ut1_utc The float value to which ut1_utc is to be set.


        """

        self._ut1_utc = float(ut1_utc)

    # ===> Attribute iat_utc

    _iat_utc = None

    def getIat_utc(self):
        """
        Get iat_utc.
        return iat_utc as float
        """

        return self._iat_utc

    def setIat_utc(self, iat_utc):
        """
        Set iat_utc with the specified float value.
        iat_utc The float value to which iat_utc is to be set.


        """

        self._iat_utc = float(iat_utc)

    # ===> Attribute timeType

    _timeType = DifferenceType.from_int(0)

    def getTimeType(self):
        """
        Get timeType.
        return timeType as DifferenceType
        """

        return self._timeType

    def setTimeType(self, timeType):
        """
        Set timeType with the specified DifferenceType value.
        timeType The DifferenceType value to which timeType is to be set.


        """

        self._timeType = DifferenceType(timeType)

    # ===> Attribute gstAtUt0

    _gstAtUt0 = Angle()

    def getGstAtUt0(self):
        """
        Get gstAtUt0.
        return gstAtUt0 as Angle
        """

        # make sure it is a copy of Angle
        return Angle(self._gstAtUt0)

    def setGstAtUt0(self, gstAtUt0):
        """
        Set gstAtUt0 with the specified Angle value.
        gstAtUt0 The Angle value to which gstAtUt0 is to be set.
        The value of gstAtUt0 can be anything allowed by the Angle constructor.

        """

        self._gstAtUt0 = Angle(gstAtUt0)

    # ===> Attribute earthRotationRate

    _earthRotationRate = AngularRate()

    def getEarthRotationRate(self):
        """
        Get earthRotationRate.
        return earthRotationRate as AngularRate
        """

        # make sure it is a copy of AngularRate
        return AngularRate(self._earthRotationRate)

    def setEarthRotationRate(self, earthRotationRate):
        """
        Set earthRotationRate with the specified AngularRate value.
        earthRotationRate The AngularRate value to which earthRotationRate is to be set.
        The value of earthRotationRate can be anything allowed by the AngularRate constructor.

        """

        self._earthRotationRate = AngularRate(earthRotationRate)

    # ===> Attribute polarOffsets

    _polarOffsets = None  # this is a 1D list of float

    def getPolarOffsets(self):
        """
        Get polarOffsets.
        return polarOffsets as float []
        """

        return copy.deepcopy(self._polarOffsets)

    def setPolarOffsets(self, polarOffsets):
        """
        Set polarOffsets with the specified float []  value.
        polarOffsets The float []  value to which polarOffsets is to be set.


        """

        # value must be a list
        if not isinstance(polarOffsets, list):
            raise ValueError("The value of polarOffsets must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(polarOffsets)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of polarOffsets is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(polarOffsets, float):
                raise ValueError(
                    "type of the first value in polarOffsets is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._polarOffsets = copy.deepcopy(polarOffsets)
        except Exception as exc:
            raise ValueError("Invalid polarOffsets : " + str(exc))

    # ===> Attribute polarOffsetsType

    _polarOffsetsType = DifferenceType.from_int(0)

    def getPolarOffsetsType(self):
        """
        Get polarOffsetsType.
        return polarOffsetsType as DifferenceType
        """

        return self._polarOffsetsType

    def setPolarOffsetsType(self, polarOffsetsType):
        """
        Set polarOffsetsType with the specified DifferenceType value.
        polarOffsetsType The DifferenceType value to which polarOffsetsType is to be set.


        """

        self._polarOffsetsType = DifferenceType(polarOffsetsType)

    # ===> Attribute nutationInLongitude, which is optional
    _nutationInLongitudeExists = False

    _nutationInLongitude = Angle()

    def isNutationInLongitudeExists(self):
        """
        The attribute nutationInLongitude is optional. Return True if this attribute exists.
        return True if and only if the nutationInLongitude attribute exists.
        """
        return self._nutationInLongitudeExists

    def getNutationInLongitude(self):
        """
        Get nutationInLongitude, which is optional.
        return nutationInLongitude as Angle
        raises ValueError If nutationInLongitude does not exist.
        """
        if not self._nutationInLongitudeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + nutationInLongitude
                + " attribute in table DelayModelVariableParameters does not exist!"
            )

        # make sure it is a copy of Angle
        return Angle(self._nutationInLongitude)

    def setNutationInLongitude(self, nutationInLongitude):
        """
        Set nutationInLongitude with the specified Angle value.
        nutationInLongitude The Angle value to which nutationInLongitude is to be set.
        The value of nutationInLongitude can be anything allowed by the Angle constructor.

        """

        self._nutationInLongitude = Angle(nutationInLongitude)

        self._nutationInLongitudeExists = True

    def clearNutationInLongitude(self):
        """
        Mark nutationInLongitude, which is an optional field, as non-existent.
        """
        self._nutationInLongitudeExists = False

    # ===> Attribute nutationInLongitudeRate, which is optional
    _nutationInLongitudeRateExists = False

    _nutationInLongitudeRate = AngularRate()

    def isNutationInLongitudeRateExists(self):
        """
        The attribute nutationInLongitudeRate is optional. Return True if this attribute exists.
        return True if and only if the nutationInLongitudeRate attribute exists.
        """
        return self._nutationInLongitudeRateExists

    def getNutationInLongitudeRate(self):
        """
        Get nutationInLongitudeRate, which is optional.
        return nutationInLongitudeRate as AngularRate
        raises ValueError If nutationInLongitudeRate does not exist.
        """
        if not self._nutationInLongitudeRateExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + nutationInLongitudeRate
                + " attribute in table DelayModelVariableParameters does not exist!"
            )

        # make sure it is a copy of AngularRate
        return AngularRate(self._nutationInLongitudeRate)

    def setNutationInLongitudeRate(self, nutationInLongitudeRate):
        """
        Set nutationInLongitudeRate with the specified AngularRate value.
        nutationInLongitudeRate The AngularRate value to which nutationInLongitudeRate is to be set.
        The value of nutationInLongitudeRate can be anything allowed by the AngularRate constructor.

        """

        self._nutationInLongitudeRate = AngularRate(nutationInLongitudeRate)

        self._nutationInLongitudeRateExists = True

    def clearNutationInLongitudeRate(self):
        """
        Mark nutationInLongitudeRate, which is an optional field, as non-existent.
        """
        self._nutationInLongitudeRateExists = False

    # ===> Attribute nutationInObliquity, which is optional
    _nutationInObliquityExists = False

    _nutationInObliquity = Angle()

    def isNutationInObliquityExists(self):
        """
        The attribute nutationInObliquity is optional. Return True if this attribute exists.
        return True if and only if the nutationInObliquity attribute exists.
        """
        return self._nutationInObliquityExists

    def getNutationInObliquity(self):
        """
        Get nutationInObliquity, which is optional.
        return nutationInObliquity as Angle
        raises ValueError If nutationInObliquity does not exist.
        """
        if not self._nutationInObliquityExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + nutationInObliquity
                + " attribute in table DelayModelVariableParameters does not exist!"
            )

        # make sure it is a copy of Angle
        return Angle(self._nutationInObliquity)

    def setNutationInObliquity(self, nutationInObliquity):
        """
        Set nutationInObliquity with the specified Angle value.
        nutationInObliquity The Angle value to which nutationInObliquity is to be set.
        The value of nutationInObliquity can be anything allowed by the Angle constructor.

        """

        self._nutationInObliquity = Angle(nutationInObliquity)

        self._nutationInObliquityExists = True

    def clearNutationInObliquity(self):
        """
        Mark nutationInObliquity, which is an optional field, as non-existent.
        """
        self._nutationInObliquityExists = False

    # ===> Attribute nutationInObliquityRate, which is optional
    _nutationInObliquityRateExists = False

    _nutationInObliquityRate = AngularRate()

    def isNutationInObliquityRateExists(self):
        """
        The attribute nutationInObliquityRate is optional. Return True if this attribute exists.
        return True if and only if the nutationInObliquityRate attribute exists.
        """
        return self._nutationInObliquityRateExists

    def getNutationInObliquityRate(self):
        """
        Get nutationInObliquityRate, which is optional.
        return nutationInObliquityRate as AngularRate
        raises ValueError If nutationInObliquityRate does not exist.
        """
        if not self._nutationInObliquityRateExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + nutationInObliquityRate
                + " attribute in table DelayModelVariableParameters does not exist!"
            )

        # make sure it is a copy of AngularRate
        return AngularRate(self._nutationInObliquityRate)

    def setNutationInObliquityRate(self, nutationInObliquityRate):
        """
        Set nutationInObliquityRate with the specified AngularRate value.
        nutationInObliquityRate The AngularRate value to which nutationInObliquityRate is to be set.
        The value of nutationInObliquityRate can be anything allowed by the AngularRate constructor.

        """

        self._nutationInObliquityRate = AngularRate(nutationInObliquityRate)

        self._nutationInObliquityRateExists = True

    def clearNutationInObliquityRate(self):
        """
        Mark nutationInObliquityRate, which is an optional field, as non-existent.
        """
        self._nutationInObliquityRateExists = False

    # Extrinsic Table Attributes

    # ===> Attribute delayModelFixedParametersId

    _delayModelFixedParametersId = Tag()

    def getDelayModelFixedParametersId(self):
        """
        Get delayModelFixedParametersId.
        return delayModelFixedParametersId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._delayModelFixedParametersId)

    def setDelayModelFixedParametersId(self, delayModelFixedParametersId):
        """
        Set delayModelFixedParametersId with the specified Tag value.
        delayModelFixedParametersId The Tag value to which delayModelFixedParametersId is to be set.
        The value of delayModelFixedParametersId can be anything allowed by the Tag constructor.

        """

        self._delayModelFixedParametersId = Tag(delayModelFixedParametersId)

    # Links

    def getDelayModelFixedParametersUsingDelayModelFixedParametersId(self):
        """
        Returns the row in the DelayModelFixedParameters table having DelayModelFixedParameters.delayModelFixedParametersId == delayModelFixedParametersId

        """

        return (
            self._table.getContainer()
            .getDelayModelFixedParameters()
            .getRowByKey(self._delayModelFixedParametersId)
        )

    # comparison methods

    def compareNoAutoInc(
        self,
        time,
        ut1_utc,
        iat_utc,
        timeType,
        gstAtUt0,
        earthRotationRate,
        polarOffsets,
        polarOffsetsType,
        delayModelFixedParametersId,
    ):
        """
        Compare each attribute except the autoincrementable one of this DelayModelVariableParametersRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # time is a ArrayTime, compare using the equals method.
        if not self._time.equals(time):
            return False

        # ut1_utc is a float, compare using the == operator.
        if not (self._ut1_utc == ut1_utc):
            return False

        # iat_utc is a float, compare using the == operator.
        if not (self._iat_utc == iat_utc):
            return False

        # timeType is a DifferenceType, compare using the == operator on the getValue() output
        if not (self._timeType.getValue() == timeType.getValue()):
            return False

        # gstAtUt0 is a Angle, compare using the almostEquals method.
        if not self._gstAtUt0.almostEquals(
            gstAtUt0, self.getTable().getGstAtUt0EqTolerance()
        ):
            return False

        # earthRotationRate is a AngularRate, compare using the almostEquals method.
        if not self._earthRotationRate.almostEquals(
            earthRotationRate, self.getTable().getEarthRotationRateEqTolerance()
        ):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarOffsets) != len(polarOffsets):
            return False
        for indx in range(len(polarOffsets)):

            # polarOffsets is a list of float, compare using == operator.
            if not (self._polarOffsets[indx] == polarOffsets[indx]):
                return False

        # polarOffsetsType is a DifferenceType, compare using the == operator on the getValue() output
        if not (self._polarOffsetsType.getValue() == polarOffsetsType.getValue()):
            return False

        # delayModelFixedParametersId is a Tag, compare using the equals method.
        if not self._delayModelFixedParametersId.equals(delayModelFixedParametersId):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getTime(),
            otherRow.getUt1_utc(),
            otherRow.getIat_utc(),
            otherRow.getTimeType(),
            otherRow.getGstAtUt0(),
            otherRow.getEarthRotationRate(),
            otherRow.getPolarOffsets(),
            otherRow.getPolarOffsetsType(),
            otherRow.getDelayModelFixedParametersId(),
        )

    def compareRequiredValue(
        self,
        time,
        ut1_utc,
        iat_utc,
        timeType,
        gstAtUt0,
        earthRotationRate,
        polarOffsets,
        polarOffsetsType,
        delayModelFixedParametersId,
    ):

        # time is a ArrayTime, compare using the equals method.
        if not self._time.equals(time):
            return False

        # ut1_utc is a float, compare using the == operator.
        if not (self._ut1_utc == ut1_utc):
            return False

        # iat_utc is a float, compare using the == operator.
        if not (self._iat_utc == iat_utc):
            return False

        # timeType is a DifferenceType, compare using the == operator on the getValue() output
        if not (self._timeType.getValue() == timeType.getValue()):
            return False

        # gstAtUt0 is a Angle, compare using the almostEquals method.
        if not self._gstAtUt0.almostEquals(
            gstAtUt0, self.getTable().getGstAtUt0EqTolerance()
        ):
            return False

        # earthRotationRate is a AngularRate, compare using the almostEquals method.
        if not self._earthRotationRate.almostEquals(
            earthRotationRate, self.getTable().getEarthRotationRateEqTolerance()
        ):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarOffsets) != len(polarOffsets):
            return False
        for indx in range(len(polarOffsets)):

            # polarOffsets is a list of float, compare using == operator.
            if not (self._polarOffsets[indx] == polarOffsets[indx]):
                return False

        # polarOffsetsType is a DifferenceType, compare using the == operator on the getValue() output
        if not (self._polarOffsetsType.getValue() == polarOffsetsType.getValue()):
            return False

        # delayModelFixedParametersId is a Tag, compare using the equals method.
        if not self._delayModelFixedParametersId.equals(delayModelFixedParametersId):
            return False

        return True


# initialize the dictionary that maps fields to init methods
DelayModelVariableParametersRow.initFromBinMethods()
