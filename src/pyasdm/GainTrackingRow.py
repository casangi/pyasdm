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
# File GainTrackingRow.py
#

import pyasdm.GainTrackingTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.PolarizationType import PolarizationType


from xml.dom import minidom

import copy


class GainTrackingRow:
    """
    The GainTrackingRow class is a row of a GainTrackingTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a GainTrackingRow.
        When row is None, create an empty row attached to table, which must be a GainTrackingTable.
        When row is given, copy those values in to the new row. The row argument must be a GainTrackingRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.GainTrackingTable):
            raise ValueError("table must be a GainTrackingTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._timeInterval = ArrayTimeInterval()

        self._numReceptor = 0

        self._attenuator = []  # this is a list of float []

        self._polarizationType = []  # this is a list of PolarizationType []

        self._samplingLevelExists = False

        self._samplingLevel = None

        self._numAttFreqExists = False

        self._numAttFreq = 0

        self._attFreqExists = False

        self._attFreq = []  # this is a list of float []

        self._attSpectrumExists = False

        self._attSpectrum = []  # this is a list of Complex []

        # extrinsic attributes

        self._antennaId = Tag()

        self._feedId = 0

        self._spectralWindowId = Tag()

        if row is not None:
            if not isinstance(row, GainTrackingRow):
                raise ValueError("row must be a GainTrackingRow")

            # copy constructor

            self._antennaId = Tag(row._antennaId)

            self._spectralWindowId = Tag(row._spectralWindowId)

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._feedId = row._feedId

            self._numReceptor = row._numReceptor

            # attenuator is a  list , make a deep copy
            self._attenuator = copy.deepcopy(row._attenuator)

            # polarizationType is a  list , make a deep copy
            self._polarizationType = copy.deepcopy(row._polarizationType)

            # by default set systematically samplingLevel's value to something not None

            if row._samplingLevelExists:

                self._samplingLevel = row._samplingLevel

                self._samplingLevelExists = True

            # by default set systematically numAttFreq's value to something not None

            if row._numAttFreqExists:

                self._numAttFreq = row._numAttFreq

                self._numAttFreqExists = True

            # by default set systematically attFreq's value to something not None

            if row._attFreqExists:

                # attFreq is a list, make a deep copy
                self.attFreq = copy.deepcopy(row.attFreq)

                self._attFreqExists = True

            # by default set systematically attSpectrum's value to something not None

            if row._attSpectrumExists:

                # attSpectrum is a list, make a deep copy
                self.attSpectrum = copy.deepcopy(row.attSpectrum)

                self._attSpectrumExists = True

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

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listValueToXML("attenuator", self._attenuator)

        result += Parser.listEnumValueToXML("polarizationType", self._polarizationType)

        if self._samplingLevelExists:

            result += Parser.valueToXML("samplingLevel", self._samplingLevel)

        if self._numAttFreqExists:

            result += Parser.valueToXML("numAttFreq", self._numAttFreq)

        if self._attFreqExists:

            result += Parser.listValueToXML("attFreq", self._attFreq)

        if self._attSpectrumExists:

            result += Parser.listExtendedValueToXML("attSpectrum", self._attSpectrum)

        # extrinsic attributes

        result += Parser.extendedValueToXML("antennaId", self._antennaId)

        result += Parser.valueToXML("feedId", self._feedId)

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
                "xmlrow is not a string or a minidom.Element", "GainTrackingTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "GainTrackingTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        attenuatorNode = rowdom.getElementsByTagName("attenuator")[0]

        attenuatorStr = attenuatorNode.firstChild.data.strip()

        self._attenuator = Parser.stringListToLists(
            attenuatorStr, float, "GainTracking", False
        )

        polarizationTypeNode = rowdom.getElementsByTagName("polarizationType")[0]

        polarizationTypeStr = polarizationTypeNode.firstChild.data.strip()
        self._polarizationType = Parser.stringListToLists(
            polarizationTypeStr, PolarizationType, "GainTracking", False
        )

        samplingLevelNode = rowdom.getElementsByTagName("samplingLevel")
        if len(samplingLevelNode) > 0:

            self._samplingLevel = float(samplingLevelNode[0].firstChild.data.strip())

            self._samplingLevelExists = True

        numAttFreqNode = rowdom.getElementsByTagName("numAttFreq")
        if len(numAttFreqNode) > 0:

            self._numAttFreq = int(numAttFreqNode[0].firstChild.data.strip())

            self._numAttFreqExists = True

        attFreqNode = rowdom.getElementsByTagName("attFreq")
        if len(attFreqNode) > 0:

            attFreqStr = attFreqNode[0].firstChild.data.strip()

            self._attFreq = Parser.stringListToLists(
                attFreqStr, float, "GainTracking", False
            )

            self._attFreqExists = True

        attSpectrumNode = rowdom.getElementsByTagName("attSpectrum")
        if len(attSpectrumNode) > 0:

            attSpectrumStr = attSpectrumNode[0].firstChild.data.strip()

            self._attSpectrum = Parser.stringListToLists(
                attSpectrumStr, Complex, "GainTracking", True
            )

            self._attSpectrumExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        self._antennaId = Tag(antennaIdNode.firstChild.data.strip())

        feedIdNode = rowdom.getElementsByTagName("feedId")[0]

        self._feedId = int(feedIdNode.firstChild.data.strip())

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

        eos.writeInt(len(self._attenuator))
        for i in range(len(self._attenuator)):

            eos.writeFloat(self._attenuator[i])

        eos.writeInt(len(self._polarizationType))
        for i in range(len(self._polarizationType)):

            eos.writeString(self._polarizationType[i].toString())

        eos.writeBool(self._samplingLevelExists)
        if self._samplingLevelExists:

            eos.writeFloat(self._samplingLevel)

        eos.writeBool(self._numAttFreqExists)
        if self._numAttFreqExists:

            eos.writeInt(self._numAttFreq)

        eos.writeBool(self._attFreqExists)
        if self._attFreqExists:

            eos.writeInt(len(self._attFreq))
            for i in range(len(self._attFreq)):

                eos.writeFloat(self._attFreq[i])

        eos.writeBool(self._attSpectrumExists)
        if self._attSpectrumExists:

            Complex.listToBin(self._attSpectrum, eos)

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
    def attenuatorFromBin(row, eis):
        """
        Set the attenuator in row from the EndianInput (eis) instance.
        """

        attenuatorDim1 = eis.readInt()
        thisList = []
        for i in range(attenuatorDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._attenuator = thisList

    @staticmethod
    def polarizationTypeFromBin(row, eis):
        """
        Set the polarizationType in row from the EndianInput (eis) instance.
        """

        polarizationTypeDim1 = eis.readInt()
        thisList = []
        for i in range(polarizationTypeDim1):
            thisValue = PolarizationType.from_int(eis.readInt())
            thisList.append(thisValue)
        row._polarizationType = thisList

    @staticmethod
    def samplingLevelFromBin(row, eis):
        """
        Set the optional samplingLevel in row from the EndianInput (eis) instance.
        """
        row._samplingLevelExists = eis.readBool()
        if row._samplingLevelExists:

            row._samplingLevel = eis.readFloat()

    @staticmethod
    def numAttFreqFromBin(row, eis):
        """
        Set the optional numAttFreq in row from the EndianInput (eis) instance.
        """
        row._numAttFreqExists = eis.readBool()
        if row._numAttFreqExists:

            row._numAttFreq = eis.readInt()

    @staticmethod
    def attFreqFromBin(row, eis):
        """
        Set the optional attFreq in row from the EndianInput (eis) instance.
        """
        row._attFreqExists = eis.readBool()
        if row._attFreqExists:

            attFreqDim1 = eis.readInt()
            thisList = []
            for i in range(attFreqDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._attFreq = thisList

    @staticmethod
    def attSpectrumFromBin(row, eis):
        """
        Set the optional attSpectrum in row from the EndianInput (eis) instance.
        """
        row._attSpectrumExists = eis.readBool()
        if row._attSpectrumExists:

            row._attSpectrum = Complex.from1DBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaId"] = GainTrackingRow.antennaIdFromBin
        _fromBinMethods["spectralWindowId"] = GainTrackingRow.spectralWindowIdFromBin
        _fromBinMethods["timeInterval"] = GainTrackingRow.timeIntervalFromBin
        _fromBinMethods["feedId"] = GainTrackingRow.feedIdFromBin
        _fromBinMethods["numReceptor"] = GainTrackingRow.numReceptorFromBin
        _fromBinMethods["attenuator"] = GainTrackingRow.attenuatorFromBin
        _fromBinMethods["polarizationType"] = GainTrackingRow.polarizationTypeFromBin

        _fromBinMethods["samplingLevel"] = GainTrackingRow.samplingLevelFromBin
        _fromBinMethods["numAttFreq"] = GainTrackingRow.numAttFreqFromBin
        _fromBinMethods["attFreq"] = GainTrackingRow.attFreqFromBin
        _fromBinMethods["attSpectrum"] = GainTrackingRow.attSpectrumFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = GainTrackingRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " GainTracking",
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

    # ===> Attribute attenuator

    _attenuator = None  # this is a 1D list of float

    def getAttenuator(self):
        """
        Get attenuator.
        return attenuator as float []
        """

        return copy.deepcopy(self._attenuator)

    def setAttenuator(self, attenuator):
        """
        Set attenuator with the specified float []  value.
        attenuator The float []  value to which attenuator is to be set.


        """

        # value must be a list
        if not isinstance(attenuator, list):
            raise ValueError("The value of attenuator must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(attenuator)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of attenuator is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(attenuator, float):
                raise ValueError(
                    "type of the first value in attenuator is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._attenuator = copy.deepcopy(attenuator)
        except Exception as exc:
            raise ValueError("Invalid attenuator : " + str(exc))

    # ===> Attribute polarizationType

    _polarizationType = None  # this is a 1D list of PolarizationType

    def getPolarizationType(self):
        """
        Get polarizationType.
        return polarizationType as PolarizationType []
        """

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
            listDims = pyasdm.utils.getListDims(polarizationType)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of polarizationType is not correct")

            # the type of the values in the list must be PolarizationType
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(polarizationType, PolarizationType):
                raise ValueError(
                    "type of the first value in polarizationType is not PolarizationType as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._polarizationType = copy.deepcopy(polarizationType)
        except Exception as exc:
            raise ValueError("Invalid polarizationType : " + str(exc))

    # ===> Attribute samplingLevel, which is optional
    _samplingLevelExists = False

    _samplingLevel = None

    def isSamplingLevelExists(self):
        """
        The attribute samplingLevel is optional. Return True if this attribute exists.
        return True if and only if the samplingLevel attribute exists.
        """
        return self._samplingLevelExists

    def getSamplingLevel(self):
        """
        Get samplingLevel, which is optional.
        return samplingLevel as float
        raises ValueError If samplingLevel does not exist.
        """
        if not self._samplingLevelExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + samplingLevel
                + " attribute in table GainTracking does not exist!"
            )

        return self._samplingLevel

    def setSamplingLevel(self, samplingLevel):
        """
        Set samplingLevel with the specified float value.
        samplingLevel The float value to which samplingLevel is to be set.


        """

        self._samplingLevel = float(samplingLevel)

        self._samplingLevelExists = True

    def clearSamplingLevel(self):
        """
        Mark samplingLevel, which is an optional field, as non-existent.
        """
        self._samplingLevelExists = False

    # ===> Attribute numAttFreq, which is optional
    _numAttFreqExists = False

    _numAttFreq = 0

    def isNumAttFreqExists(self):
        """
        The attribute numAttFreq is optional. Return True if this attribute exists.
        return True if and only if the numAttFreq attribute exists.
        """
        return self._numAttFreqExists

    def getNumAttFreq(self):
        """
        Get numAttFreq, which is optional.
        return numAttFreq as int
        raises ValueError If numAttFreq does not exist.
        """
        if not self._numAttFreqExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numAttFreq
                + " attribute in table GainTracking does not exist!"
            )

        return self._numAttFreq

    def setNumAttFreq(self, numAttFreq):
        """
        Set numAttFreq with the specified int value.
        numAttFreq The int value to which numAttFreq is to be set.


        """

        self._numAttFreq = int(numAttFreq)

        self._numAttFreqExists = True

    def clearNumAttFreq(self):
        """
        Mark numAttFreq, which is an optional field, as non-existent.
        """
        self._numAttFreqExists = False

    # ===> Attribute attFreq, which is optional
    _attFreqExists = False

    _attFreq = None  # this is a 1D list of float

    def isAttFreqExists(self):
        """
        The attribute attFreq is optional. Return True if this attribute exists.
        return True if and only if the attFreq attribute exists.
        """
        return self._attFreqExists

    def getAttFreq(self):
        """
        Get attFreq, which is optional.
        return attFreq as float []
        raises ValueError If attFreq does not exist.
        """
        if not self._attFreqExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + attFreq
                + " attribute in table GainTracking does not exist!"
            )

        return copy.deepcopy(self._attFreq)

    def setAttFreq(self, attFreq):
        """
        Set attFreq with the specified float []  value.
        attFreq The float []  value to which attFreq is to be set.


        """

        # value must be a list
        if not isinstance(attFreq, list):
            raise ValueError("The value of attFreq must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(attFreq)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of attFreq is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(attFreq, float):
                raise ValueError(
                    "type of the first value in attFreq is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._attFreq = copy.deepcopy(attFreq)
        except Exception as exc:
            raise ValueError("Invalid attFreq : " + str(exc))

        self._attFreqExists = True

    def clearAttFreq(self):
        """
        Mark attFreq, which is an optional field, as non-existent.
        """
        self._attFreqExists = False

    # ===> Attribute attSpectrum, which is optional
    _attSpectrumExists = False

    _attSpectrum = None  # this is a 1D list of Complex

    def isAttSpectrumExists(self):
        """
        The attribute attSpectrum is optional. Return True if this attribute exists.
        return True if and only if the attSpectrum attribute exists.
        """
        return self._attSpectrumExists

    def getAttSpectrum(self):
        """
        Get attSpectrum, which is optional.
        return attSpectrum as Complex []
        raises ValueError If attSpectrum does not exist.
        """
        if not self._attSpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + attSpectrum
                + " attribute in table GainTracking does not exist!"
            )

        return copy.deepcopy(self._attSpectrum)

    def setAttSpectrum(self, attSpectrum):
        """
        Set attSpectrum with the specified Complex []  value.
        attSpectrum The Complex []  value to which attSpectrum is to be set.
        The value of attSpectrum can be anything allowed by the Complex []  constructor.

        """

        # value must be a list
        if not isinstance(attSpectrum, list):
            raise ValueError("The value of attSpectrum must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(attSpectrum)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of attSpectrum is not correct")

            # the type of the values in the list must be Complex
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(attSpectrum, Complex):
                raise ValueError(
                    "type of the first value in attSpectrum is not Complex as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._attSpectrum = copy.deepcopy(attSpectrum)
        except Exception as exc:
            raise ValueError("Invalid attSpectrum : " + str(exc))

        self._attSpectrumExists = True

    def clearAttSpectrum(self):
        """
        Mark attSpectrum, which is an optional field, as non-existent.
        """
        self._attSpectrumExists = False

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

    # ===> Slice link from a row of GainTracking table to a collection of row of Feed table.
    def getFeeds(self):
        """
        Get the collection of rows in the Feed table having feedId == this.feedId
        """

        return self._table.getContainer().getFeed().getRowByFeedId(self._feedId)

    # comparison methods

    def compareNoAutoInc(
        self,
        antennaId,
        spectralWindowId,
        timeInterval,
        feedId,
        numReceptor,
        attenuator,
        polarizationType,
    ):
        """
        Compare each attribute except the autoincrementable one of this GainTrackingRow with
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

        # feedId is a int, compare using the == operator.
        if not (self._feedId == feedId):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._attenuator) != len(attenuator):
            return False
        for indx in range(len(attenuator)):

            # attenuator is a list of float, compare using == operator.
            if not (self._attenuator[indx] == attenuator[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationType) != len(polarizationType):
            return False
        for indx in range(len(polarizationType)):

            # polarizationType is a list of PolarizationType, compare using == operator.
            if not (self._polarizationType[indx] == polarizationType[indx]):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumReceptor(),
            otherRow.getAttenuator(),
            otherRow.getPolarizationType(),
        )

    def compareRequiredValue(self, numReceptor, attenuator, polarizationType):

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._attenuator) != len(attenuator):
            return False
        for indx in range(len(attenuator)):

            # attenuator is a list of float, compare using == operator.
            if not (self._attenuator[indx] == attenuator[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationType) != len(polarizationType):
            return False
        for indx in range(len(polarizationType)):

            # polarizationType is a list of PolarizationType, compare using == operator.
            if not (self._polarizationType[indx] == polarizationType[indx]):
                return False

        return True


# initialize the dictionary that maps fields to init methods
GainTrackingRow.initFromBinMethods()
