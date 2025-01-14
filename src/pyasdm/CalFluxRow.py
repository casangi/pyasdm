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
# File CalFluxRow.py
#

import pyasdm.CalFluxTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.FluxCalibrationMethod import FluxCalibrationMethod


from pyasdm.enumerations.StokesParameter import StokesParameter


from pyasdm.enumerations.DirectionReferenceCode import DirectionReferenceCode


from pyasdm.enumerations.SourceModel import SourceModel


from xml.dom import minidom

import copy


class CalFluxRow:
    """
    The CalFluxRow class is a row of a CalFluxTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalFluxRow.
        When row is None, create an empty row attached to table, which must be a CalFluxTable.
        When row is given, copy those values in to the new row. The row argument must be a CalFluxRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalFluxTable):
            raise ValueError("table must be a CalFluxTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._sourceName = None

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._numFrequencyRanges = 0

        self._numStokes = 0

        self._frequencyRanges = []  # this is a list of Frequency []  []

        self._fluxMethod = FluxCalibrationMethod.from_int(0)

        self._flux = []  # this is a list of float []  []

        self._fluxError = []  # this is a list of float []  []

        self._stokes = []  # this is a list of StokesParameter []

        self._directionExists = False

        self._direction = []  # this is a list of Angle []

        self._directionCodeExists = False

        self._directionCode = DirectionReferenceCode.from_int(0)

        self._directionEquinoxExists = False

        self._directionEquinox = Angle()

        self._PAExists = False

        self._PA = []  # this is a list of Angle []  []

        self._PAErrorExists = False

        self._PAError = []  # this is a list of Angle []  []

        self._sizeExists = False

        self._size = []  # this is a list of Angle []  []  []

        self._sizeErrorExists = False

        self._sizeError = []  # this is a list of Angle []  []  []

        self._sourceModelExists = False

        self._sourceModel = SourceModel.from_int(0)

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalFluxRow):
                raise ValueError("row must be a CalFluxRow")

            # copy constructor

            self._sourceName = row._sourceName

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            self._numFrequencyRanges = row._numFrequencyRanges

            self._numStokes = row._numStokes

            # frequencyRanges is a  list , make a deep copy
            self._frequencyRanges = copy.deepcopy(row._frequencyRanges)

            # We force the attribute of the result to be not None
            if row._fluxMethod is None:
                self._fluxMethod = FluxCalibrationMethod.from_int(0)
            else:
                self._fluxMethod = FluxCalibrationMethod(row._fluxMethod)

            # flux is a  list , make a deep copy
            self._flux = copy.deepcopy(row._flux)

            # fluxError is a  list , make a deep copy
            self._fluxError = copy.deepcopy(row._fluxError)

            # stokes is a  list , make a deep copy
            self._stokes = copy.deepcopy(row._stokes)

            # by default set systematically direction's value to something not None

            if row._directionExists:

                # direction is a list, make a deep copy
                self.direction = copy.deepcopy(row.direction)

                self._directionExists = True

            # by default set systematically directionCode's value to something not None

            self._directionCode = DirectionReferenceCode.from_int(0)

            if row._directionCodeExists:

                if row._directionCode is not None:
                    self._directionCode = row._directionCode

                self._directionCodeExists = True

            # by default set systematically directionEquinox's value to something not None

            if row._directionEquinoxExists:

                self._directionEquinox = Angle(row._directionEquinox)

                self._directionEquinoxExists = True

            # by default set systematically PA's value to something not None

            if row._PAExists:

                # PA is a list, make a deep copy
                self.PA = copy.deepcopy(row.PA)

                self._PAExists = True

            # by default set systematically PAError's value to something not None

            if row._PAErrorExists:

                # PAError is a list, make a deep copy
                self.PAError = copy.deepcopy(row.PAError)

                self._PAErrorExists = True

            # by default set systematically size's value to something not None

            if row._sizeExists:

                # size is a list, make a deep copy
                self.size = copy.deepcopy(row.size)

                self._sizeExists = True

            # by default set systematically sizeError's value to something not None

            if row._sizeErrorExists:

                # sizeError is a list, make a deep copy
                self.sizeError = copy.deepcopy(row.sizeError)

                self._sizeErrorExists = True

            # by default set systematically sourceModel's value to something not None

            self._sourceModel = SourceModel.from_int(0)

            if row._sourceModelExists:

                if row._sourceModel is not None:
                    self._sourceModel = row._sourceModel

                self._sourceModelExists = True

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

        result += Parser.valueToXML("sourceName", self._sourceName)

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.valueToXML("numFrequencyRanges", self._numFrequencyRanges)

        result += Parser.valueToXML("numStokes", self._numStokes)

        result += Parser.listExtendedValueToXML(
            "frequencyRanges", self._frequencyRanges
        )

        result += Parser.valueToXML(
            "fluxMethod", FluxCalibrationMethod.name(self._fluxMethod)
        )

        result += Parser.listValueToXML("flux", self._flux)

        result += Parser.listValueToXML("fluxError", self._fluxError)

        result += Parser.listEnumValueToXML("stokes", self._stokes)

        if self._directionExists:

            result += Parser.listExtendedValueToXML("direction", self._direction)

        if self._directionCodeExists:

            result += Parser.valueToXML(
                "directionCode", DirectionReferenceCode.name(self._directionCode)
            )

        if self._directionEquinoxExists:

            result += Parser.extendedValueToXML(
                "directionEquinox", self._directionEquinox
            )

        if self._PAExists:

            result += Parser.listExtendedValueToXML("PA", self._PA)

        if self._PAErrorExists:

            result += Parser.listExtendedValueToXML("PAError", self._PAError)

        if self._sizeExists:

            result += Parser.listExtendedValueToXML("size", self._size)

        if self._sizeErrorExists:

            result += Parser.listExtendedValueToXML("sizeError", self._sizeError)

        if self._sourceModelExists:

            result += Parser.valueToXML(
                "sourceModel", SourceModel.name(self._sourceModel)
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
                "xmlrow is not a string or a minidom.Element", "CalFluxTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalFluxTable")

        # intrinsic attribute values

        sourceNameNode = rowdom.getElementsByTagName("sourceName")[0]

        self._sourceName = str(sourceNameNode.firstChild.data.strip())

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        numFrequencyRangesNode = rowdom.getElementsByTagName("numFrequencyRanges")[0]

        self._numFrequencyRanges = int(numFrequencyRangesNode.firstChild.data.strip())

        numStokesNode = rowdom.getElementsByTagName("numStokes")[0]

        self._numStokes = int(numStokesNode.firstChild.data.strip())

        frequencyRangesNode = rowdom.getElementsByTagName("frequencyRanges")[0]

        frequencyRangesStr = frequencyRangesNode.firstChild.data.strip()

        self._frequencyRanges = Parser.stringListToLists(
            frequencyRangesStr, Frequency, "CalFlux", True
        )

        fluxMethodNode = rowdom.getElementsByTagName("fluxMethod")[0]

        self._fluxMethod = FluxCalibrationMethod.newFluxCalibrationMethod(
            fluxMethodNode.firstChild.data.strip()
        )

        fluxNode = rowdom.getElementsByTagName("flux")[0]

        fluxStr = fluxNode.firstChild.data.strip()

        self._flux = Parser.stringListToLists(fluxStr, float, "CalFlux", False)

        fluxErrorNode = rowdom.getElementsByTagName("fluxError")[0]

        fluxErrorStr = fluxErrorNode.firstChild.data.strip()

        self._fluxError = Parser.stringListToLists(
            fluxErrorStr, float, "CalFlux", False
        )

        stokesNode = rowdom.getElementsByTagName("stokes")[0]

        stokesStr = stokesNode.firstChild.data.strip()
        self._stokes = Parser.stringListToLists(
            stokesStr, StokesParameter, "CalFlux", False
        )

        directionNode = rowdom.getElementsByTagName("direction")
        if len(directionNode) > 0:

            directionStr = directionNode[0].firstChild.data.strip()

            self._direction = Parser.stringListToLists(
                directionStr, Angle, "CalFlux", True
            )

            self._directionExists = True

        directionCodeNode = rowdom.getElementsByTagName("directionCode")
        if len(directionCodeNode) > 0:

            self._directionCode = DirectionReferenceCode.newDirectionReferenceCode(
                directionCodeNode[0].firstChild.data.strip()
            )

            self._directionCodeExists = True

        directionEquinoxNode = rowdom.getElementsByTagName("directionEquinox")
        if len(directionEquinoxNode) > 0:

            self._directionEquinox = Angle(
                directionEquinoxNode[0].firstChild.data.strip()
            )

            self._directionEquinoxExists = True

        PANode = rowdom.getElementsByTagName("PA")
        if len(PANode) > 0:

            PAStr = PANode[0].firstChild.data.strip()

            self._PA = Parser.stringListToLists(PAStr, Angle, "CalFlux", True)

            self._PAExists = True

        PAErrorNode = rowdom.getElementsByTagName("PAError")
        if len(PAErrorNode) > 0:

            PAErrorStr = PAErrorNode[0].firstChild.data.strip()

            self._PAError = Parser.stringListToLists(PAErrorStr, Angle, "CalFlux", True)

            self._PAErrorExists = True

        sizeNode = rowdom.getElementsByTagName("size")
        if len(sizeNode) > 0:

            sizeStr = sizeNode[0].firstChild.data.strip()

            self._size = Parser.stringListToLists(sizeStr, Angle, "CalFlux", True)

            self._sizeExists = True

        sizeErrorNode = rowdom.getElementsByTagName("sizeError")
        if len(sizeErrorNode) > 0:

            sizeErrorStr = sizeErrorNode[0].firstChild.data.strip()

            self._sizeError = Parser.stringListToLists(
                sizeErrorStr, Angle, "CalFlux", True
            )

            self._sizeErrorExists = True

        sourceModelNode = rowdom.getElementsByTagName("sourceModel")
        if len(sourceModelNode) > 0:

            self._sourceModel = SourceModel.newSourceModel(
                sourceModelNode[0].firstChild.data.strip()
            )

            self._sourceModelExists = True

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

        eos.writeStr(self._sourceName)

        self._calDataId.toBin(eos)

        self._calReductionId.toBin(eos)

        self._startValidTime.toBin(eos)

        self._endValidTime.toBin(eos)

        eos.writeInt(self._numFrequencyRanges)

        eos.writeInt(self._numStokes)

        Frequency.listToBin(self._frequencyRanges, eos)

        eos.writeString(self._fluxMethod.toString())

        # null array case, unsure if this is possible but this should work
        if self._flux is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            flux_dims = Parser.getListDims(self._flux)
        # assumes it really is 2D
        eos.writeInt(flux_dims[0])
        eos.writeInt(flux_dims[1])
        for i in range(flux_dims[0]):
            for j in range(flux_dims[1]):
                eos.writeFloat(self._flux[i][j])

        # null array case, unsure if this is possible but this should work
        if self._fluxError is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            fluxError_dims = Parser.getListDims(self._fluxError)
        # assumes it really is 2D
        eos.writeInt(fluxError_dims[0])
        eos.writeInt(fluxError_dims[1])
        for i in range(fluxError_dims[0]):
            for j in range(fluxError_dims[1]):
                eos.writeFloat(self._fluxError[i][j])

        eos.writeInt(len(self._stokes))
        for i in range(len(self._stokes)):

            eos.writeString(self._stokes[i].toString())

        eos.writeBool(self._directionExists)
        if self._directionExists:

            Angle.listToBin(self._direction, eos)

        eos.writeBool(self._directionCodeExists)
        if self._directionCodeExists:

            eos.writeString(self._directionCode.toString())

        eos.writeBool(self._directionEquinoxExists)
        if self._directionEquinoxExists:

            self._directionEquinox.toBin(eos)

        eos.writeBool(self._PAExists)
        if self._PAExists:

            Angle.listToBin(self._PA, eos)

        eos.writeBool(self._PAErrorExists)
        if self._PAErrorExists:

            Angle.listToBin(self._PAError, eos)

        eos.writeBool(self._sizeExists)
        if self._sizeExists:

            Angle.listToBin(self._size, eos)

        eos.writeBool(self._sizeErrorExists)
        if self._sizeErrorExists:

            Angle.listToBin(self._sizeError, eos)

        eos.writeBool(self._sourceModelExists)
        if self._sourceModelExists:

            eos.writeString(self._sourceModel.toString())

    @staticmethod
    def sourceNameFromBin(row, eis):
        """
        Set the sourceName in row from the EndianInput (eis) instance.
        """

        row._sourceName = eis.readStr()

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
    def numFrequencyRangesFromBin(row, eis):
        """
        Set the numFrequencyRanges in row from the EndianInput (eis) instance.
        """

        row._numFrequencyRanges = eis.readInt()

    @staticmethod
    def numStokesFromBin(row, eis):
        """
        Set the numStokes in row from the EndianInput (eis) instance.
        """

        row._numStokes = eis.readInt()

    @staticmethod
    def frequencyRangesFromBin(row, eis):
        """
        Set the frequencyRanges in row from the EndianInput (eis) instance.
        """

        row._frequencyRanges = Frequency.from2DBin(eis)

    @staticmethod
    def fluxMethodFromBin(row, eis):
        """
        Set the fluxMethod in row from the EndianInput (eis) instance.
        """

        row._fluxMethod = FluxCalibrationMethod.from_int(eis.readInt())

    @staticmethod
    def fluxFromBin(row, eis):
        """
        Set the flux in row from the EndianInput (eis) instance.
        """

        fluxDim1 = eis.readInt()
        fluxDim2 = eis.readInt()
        thisList = []
        for i in range(fluxDim1):
            thisList_j = []
            for j in range(fluxDim2):
                thisValue = eis.readFloat()
                thisList_j.append(thisValue)
            thisList.append(thisList_j)
        row.flux = thisList

    @staticmethod
    def fluxErrorFromBin(row, eis):
        """
        Set the fluxError in row from the EndianInput (eis) instance.
        """

        fluxErrorDim1 = eis.readInt()
        fluxErrorDim2 = eis.readInt()
        thisList = []
        for i in range(fluxErrorDim1):
            thisList_j = []
            for j in range(fluxErrorDim2):
                thisValue = eis.readFloat()
                thisList_j.append(thisValue)
            thisList.append(thisList_j)
        row.fluxError = thisList

    @staticmethod
    def stokesFromBin(row, eis):
        """
        Set the stokes in row from the EndianInput (eis) instance.
        """

        stokesDim1 = eis.readInt()
        thisList = []
        for i in range(stokesDim1):
            thisValue = StokesParameter.from_int(eis.readInt())
            thisList.append(thisValue)
        row._stokes = thisList

    @staticmethod
    def directionFromBin(row, eis):
        """
        Set the optional direction in row from the EndianInput (eis) instance.
        """
        row._directionExists = eis.readBool()
        if row._directionExists:

            row._direction = Angle.from1DBin(eis)

    @staticmethod
    def directionCodeFromBin(row, eis):
        """
        Set the optional directionCode in row from the EndianInput (eis) instance.
        """
        row._directionCodeExists = eis.readBool()
        if row._directionCodeExists:

            row._directionCode = DirectionReferenceCode.from_int(eis.readInt())

    @staticmethod
    def directionEquinoxFromBin(row, eis):
        """
        Set the optional directionEquinox in row from the EndianInput (eis) instance.
        """
        row._directionEquinoxExists = eis.readBool()
        if row._directionEquinoxExists:

            row._directionEquinox = Angle.fromBin(eis)

    @staticmethod
    def PAFromBin(row, eis):
        """
        Set the optional PA in row from the EndianInput (eis) instance.
        """
        row._PAExists = eis.readBool()
        if row._PAExists:

            row._PA = Angle.from2DBin(eis)

    @staticmethod
    def PAErrorFromBin(row, eis):
        """
        Set the optional PAError in row from the EndianInput (eis) instance.
        """
        row._PAErrorExists = eis.readBool()
        if row._PAErrorExists:

            row._PAError = Angle.from2DBin(eis)

    @staticmethod
    def sizeFromBin(row, eis):
        """
        Set the optional size in row from the EndianInput (eis) instance.
        """
        row._sizeExists = eis.readBool()
        if row._sizeExists:

            row._size = Angle.from3DBin(eis)

    @staticmethod
    def sizeErrorFromBin(row, eis):
        """
        Set the optional sizeError in row from the EndianInput (eis) instance.
        """
        row._sizeErrorExists = eis.readBool()
        if row._sizeErrorExists:

            row._sizeError = Angle.from3DBin(eis)

    @staticmethod
    def sourceModelFromBin(row, eis):
        """
        Set the optional sourceModel in row from the EndianInput (eis) instance.
        """
        row._sourceModelExists = eis.readBool()
        if row._sourceModelExists:

            row._sourceModel = SourceModel.from_int(eis.readInt())

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["sourceName"] = CalFluxRow.sourceNameFromBin
        _fromBinMethods["calDataId"] = CalFluxRow.calDataIdFromBin
        _fromBinMethods["calReductionId"] = CalFluxRow.calReductionIdFromBin
        _fromBinMethods["startValidTime"] = CalFluxRow.startValidTimeFromBin
        _fromBinMethods["endValidTime"] = CalFluxRow.endValidTimeFromBin
        _fromBinMethods["numFrequencyRanges"] = CalFluxRow.numFrequencyRangesFromBin
        _fromBinMethods["numStokes"] = CalFluxRow.numStokesFromBin
        _fromBinMethods["frequencyRanges"] = CalFluxRow.frequencyRangesFromBin
        _fromBinMethods["fluxMethod"] = CalFluxRow.fluxMethodFromBin
        _fromBinMethods["flux"] = CalFluxRow.fluxFromBin
        _fromBinMethods["fluxError"] = CalFluxRow.fluxErrorFromBin
        _fromBinMethods["stokes"] = CalFluxRow.stokesFromBin

        _fromBinMethods["direction"] = CalFluxRow.directionFromBin
        _fromBinMethods["directionCode"] = CalFluxRow.directionCodeFromBin
        _fromBinMethods["directionEquinox"] = CalFluxRow.directionEquinoxFromBin
        _fromBinMethods["PA"] = CalFluxRow.PAFromBin
        _fromBinMethods["PAError"] = CalFluxRow.PAErrorFromBin
        _fromBinMethods["size"] = CalFluxRow.sizeFromBin
        _fromBinMethods["sizeError"] = CalFluxRow.sizeErrorFromBin
        _fromBinMethods["sourceModel"] = CalFluxRow.sourceModelFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CalFluxRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalFlux",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute sourceName

    _sourceName = None

    def getSourceName(self):
        """
        Get sourceName.
        return sourceName as str
        """

        return self._sourceName

    def setSourceName(self, sourceName):
        """
        Set sourceName with the specified str value.
        sourceName The str value to which sourceName is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the sourceName field, which is part of the key, after this row has been added to this table."
            )

        self._sourceName = str(sourceName)

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

    # ===> Attribute numFrequencyRanges

    _numFrequencyRanges = 0

    def getNumFrequencyRanges(self):
        """
        Get numFrequencyRanges.
        return numFrequencyRanges as int
        """

        return self._numFrequencyRanges

    def setNumFrequencyRanges(self, numFrequencyRanges):
        """
        Set numFrequencyRanges with the specified int value.
        numFrequencyRanges The int value to which numFrequencyRanges is to be set.


        """

        self._numFrequencyRanges = int(numFrequencyRanges)

    # ===> Attribute numStokes

    _numStokes = 0

    def getNumStokes(self):
        """
        Get numStokes.
        return numStokes as int
        """

        return self._numStokes

    def setNumStokes(self, numStokes):
        """
        Set numStokes with the specified int value.
        numStokes The int value to which numStokes is to be set.


        """

        self._numStokes = int(numStokes)

    # ===> Attribute frequencyRanges

    _frequencyRanges = None  # this is a 2D list of Frequency

    def getFrequencyRanges(self):
        """
        Get frequencyRanges.
        return frequencyRanges as Frequency []  []
        """

        return copy.deepcopy(self._frequencyRanges)

    def setFrequencyRanges(self, frequencyRanges):
        """
        Set frequencyRanges with the specified Frequency []  []  value.
        frequencyRanges The Frequency []  []  value to which frequencyRanges is to be set.
        The value of frequencyRanges can be anything allowed by the Frequency []  []  constructor.

        """

        # value must be a list
        if not isinstance(frequencyRanges, list):
            raise ValueError("The value of frequencyRanges must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(frequencyRanges)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of frequencyRanges is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(frequencyRanges, Frequency):
                raise ValueError(
                    "type of the first value in frequencyRanges is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._frequencyRanges = copy.deepcopy(frequencyRanges)
        except Exception as exc:
            raise ValueError("Invalid frequencyRanges : " + str(exc))

    # ===> Attribute fluxMethod

    _fluxMethod = FluxCalibrationMethod.from_int(0)

    def getFluxMethod(self):
        """
        Get fluxMethod.
        return fluxMethod as FluxCalibrationMethod
        """

        return self._fluxMethod

    def setFluxMethod(self, fluxMethod):
        """
        Set fluxMethod with the specified FluxCalibrationMethod value.
        fluxMethod The FluxCalibrationMethod value to which fluxMethod is to be set.


        """

        self._fluxMethod = FluxCalibrationMethod(fluxMethod)

    # ===> Attribute flux

    _flux = None  # this is a 2D list of float

    def getFlux(self):
        """
        Get flux.
        return flux as float []  []
        """

        return copy.deepcopy(self._flux)

    def setFlux(self, flux):
        """
        Set flux with the specified float []  []  value.
        flux The float []  []  value to which flux is to be set.


        """

        # value must be a list
        if not isinstance(flux, list):
            raise ValueError("The value of flux must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(flux)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of flux is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(flux, float):
                raise ValueError(
                    "type of the first value in flux is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._flux = copy.deepcopy(flux)
        except Exception as exc:
            raise ValueError("Invalid flux : " + str(exc))

    # ===> Attribute fluxError

    _fluxError = None  # this is a 2D list of float

    def getFluxError(self):
        """
        Get fluxError.
        return fluxError as float []  []
        """

        return copy.deepcopy(self._fluxError)

    def setFluxError(self, fluxError):
        """
        Set fluxError with the specified float []  []  value.
        fluxError The float []  []  value to which fluxError is to be set.


        """

        # value must be a list
        if not isinstance(fluxError, list):
            raise ValueError("The value of fluxError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(fluxError)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of fluxError is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(fluxError, float):
                raise ValueError(
                    "type of the first value in fluxError is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._fluxError = copy.deepcopy(fluxError)
        except Exception as exc:
            raise ValueError("Invalid fluxError : " + str(exc))

    # ===> Attribute stokes

    _stokes = None  # this is a 1D list of StokesParameter

    def getStokes(self):
        """
        Get stokes.
        return stokes as StokesParameter []
        """

        return copy.deepcopy(self._stokes)

    def setStokes(self, stokes):
        """
        Set stokes with the specified StokesParameter []  value.
        stokes The StokesParameter []  value to which stokes is to be set.


        """

        # value must be a list
        if not isinstance(stokes, list):
            raise ValueError("The value of stokes must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(stokes)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of stokes is not correct")

            # the type of the values in the list must be StokesParameter
            # note : this only checks the first value found
            if not Parser.checkListType(stokes, StokesParameter):
                raise ValueError(
                    "type of the first value in stokes is not StokesParameter as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._stokes = copy.deepcopy(stokes)
        except Exception as exc:
            raise ValueError("Invalid stokes : " + str(exc))

    # ===> Attribute direction, which is optional
    _directionExists = False

    _direction = None  # this is a 1D list of Angle

    def isDirectionExists(self):
        """
        The attribute direction is optional. Return True if this attribute exists.
        return True if and only if the direction attribute exists.
        """
        return self._directionExists

    def getDirection(self):
        """
        Get direction, which is optional.
        return direction as Angle []
        raises ValueError If direction does not exist.
        """
        if not self._directionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + direction
                + " attribute in table CalFlux does not exist!"
            )

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

        self._directionExists = True

    def clearDirection(self):
        """
        Mark direction, which is an optional field, as non-existent.
        """
        self._directionExists = False

    # ===> Attribute directionCode, which is optional
    _directionCodeExists = False

    _directionCode = DirectionReferenceCode.from_int(0)

    def isDirectionCodeExists(self):
        """
        The attribute directionCode is optional. Return True if this attribute exists.
        return True if and only if the directionCode attribute exists.
        """
        return self._directionCodeExists

    def getDirectionCode(self):
        """
        Get directionCode, which is optional.
        return directionCode as DirectionReferenceCode
        raises ValueError If directionCode does not exist.
        """
        if not self._directionCodeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + directionCode
                + " attribute in table CalFlux does not exist!"
            )

        return self._directionCode

    def setDirectionCode(self, directionCode):
        """
        Set directionCode with the specified DirectionReferenceCode value.
        directionCode The DirectionReferenceCode value to which directionCode is to be set.


        """

        self._directionCode = DirectionReferenceCode(directionCode)

        self._directionCodeExists = True

    def clearDirectionCode(self):
        """
        Mark directionCode, which is an optional field, as non-existent.
        """
        self._directionCodeExists = False

    # ===> Attribute directionEquinox, which is optional
    _directionEquinoxExists = False

    _directionEquinox = Angle()

    def isDirectionEquinoxExists(self):
        """
        The attribute directionEquinox is optional. Return True if this attribute exists.
        return True if and only if the directionEquinox attribute exists.
        """
        return self._directionEquinoxExists

    def getDirectionEquinox(self):
        """
        Get directionEquinox, which is optional.
        return directionEquinox as Angle
        raises ValueError If directionEquinox does not exist.
        """
        if not self._directionEquinoxExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + directionEquinox
                + " attribute in table CalFlux does not exist!"
            )

        # make sure it is a copy of Angle
        return Angle(self._directionEquinox)

    def setDirectionEquinox(self, directionEquinox):
        """
        Set directionEquinox with the specified Angle value.
        directionEquinox The Angle value to which directionEquinox is to be set.
        The value of directionEquinox can be anything allowed by the Angle constructor.

        """

        self._directionEquinox = Angle(directionEquinox)

        self._directionEquinoxExists = True

    def clearDirectionEquinox(self):
        """
        Mark directionEquinox, which is an optional field, as non-existent.
        """
        self._directionEquinoxExists = False

    # ===> Attribute PA, which is optional
    _PAExists = False

    _PA = None  # this is a 2D list of Angle

    def isPAExists(self):
        """
        The attribute PA is optional. Return True if this attribute exists.
        return True if and only if the PA attribute exists.
        """
        return self._PAExists

    def getPA(self):
        """
        Get PA, which is optional.
        return PA as Angle []  []
        raises ValueError If PA does not exist.
        """
        if not self._PAExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + PA
                + " attribute in table CalFlux does not exist!"
            )

        return copy.deepcopy(self._PA)

    def setPA(self, PA):
        """
        Set PA with the specified Angle []  []  value.
        PA The Angle []  []  value to which PA is to be set.
        The value of PA can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(PA, list):
            raise ValueError("The value of PA must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(PA)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of PA is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(PA, Angle):
                raise ValueError(
                    "type of the first value in PA is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._PA = copy.deepcopy(PA)
        except Exception as exc:
            raise ValueError("Invalid PA : " + str(exc))

        self._PAExists = True

    def clearPA(self):
        """
        Mark PA, which is an optional field, as non-existent.
        """
        self._PAExists = False

    # ===> Attribute PAError, which is optional
    _PAErrorExists = False

    _PAError = None  # this is a 2D list of Angle

    def isPAErrorExists(self):
        """
        The attribute PAError is optional. Return True if this attribute exists.
        return True if and only if the PAError attribute exists.
        """
        return self._PAErrorExists

    def getPAError(self):
        """
        Get PAError, which is optional.
        return PAError as Angle []  []
        raises ValueError If PAError does not exist.
        """
        if not self._PAErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + PAError
                + " attribute in table CalFlux does not exist!"
            )

        return copy.deepcopy(self._PAError)

    def setPAError(self, PAError):
        """
        Set PAError with the specified Angle []  []  value.
        PAError The Angle []  []  value to which PAError is to be set.
        The value of PAError can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(PAError, list):
            raise ValueError("The value of PAError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(PAError)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of PAError is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(PAError, Angle):
                raise ValueError(
                    "type of the first value in PAError is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._PAError = copy.deepcopy(PAError)
        except Exception as exc:
            raise ValueError("Invalid PAError : " + str(exc))

        self._PAErrorExists = True

    def clearPAError(self):
        """
        Mark PAError, which is an optional field, as non-existent.
        """
        self._PAErrorExists = False

    # ===> Attribute size, which is optional
    _sizeExists = False

    _size = None  # this is a 2D list of Angle

    def isSizeExists(self):
        """
        The attribute size is optional. Return True if this attribute exists.
        return True if and only if the size attribute exists.
        """
        return self._sizeExists

    def getSize(self):
        """
        Get size, which is optional.
        return size as Angle []  []  []
        raises ValueError If size does not exist.
        """
        if not self._sizeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + size
                + " attribute in table CalFlux does not exist!"
            )

        return copy.deepcopy(self._size)

    def setSize(self, size):
        """
        Set size with the specified Angle []  []  []  value.
        size The Angle []  []  []  value to which size is to be set.
        The value of size can be anything allowed by the Angle []  []  []  constructor.

        """

        # value must be a list
        if not isinstance(size, list):
            raise ValueError("The value of size must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(size)

            shapeOK = len(listDims) == 3

            if not shapeOK:
                raise ValueError("shape of size is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(size, Angle):
                raise ValueError(
                    "type of the first value in size is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._size = copy.deepcopy(size)
        except Exception as exc:
            raise ValueError("Invalid size : " + str(exc))

        self._sizeExists = True

    def clearSize(self):
        """
        Mark size, which is an optional field, as non-existent.
        """
        self._sizeExists = False

    # ===> Attribute sizeError, which is optional
    _sizeErrorExists = False

    _sizeError = None  # this is a 2D list of Angle

    def isSizeErrorExists(self):
        """
        The attribute sizeError is optional. Return True if this attribute exists.
        return True if and only if the sizeError attribute exists.
        """
        return self._sizeErrorExists

    def getSizeError(self):
        """
        Get sizeError, which is optional.
        return sizeError as Angle []  []  []
        raises ValueError If sizeError does not exist.
        """
        if not self._sizeErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sizeError
                + " attribute in table CalFlux does not exist!"
            )

        return copy.deepcopy(self._sizeError)

    def setSizeError(self, sizeError):
        """
        Set sizeError with the specified Angle []  []  []  value.
        sizeError The Angle []  []  []  value to which sizeError is to be set.
        The value of sizeError can be anything allowed by the Angle []  []  []  constructor.

        """

        # value must be a list
        if not isinstance(sizeError, list):
            raise ValueError("The value of sizeError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(sizeError)

            shapeOK = len(listDims) == 3

            if not shapeOK:
                raise ValueError("shape of sizeError is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(sizeError, Angle):
                raise ValueError(
                    "type of the first value in sizeError is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._sizeError = copy.deepcopy(sizeError)
        except Exception as exc:
            raise ValueError("Invalid sizeError : " + str(exc))

        self._sizeErrorExists = True

    def clearSizeError(self):
        """
        Mark sizeError, which is an optional field, as non-existent.
        """
        self._sizeErrorExists = False

    # ===> Attribute sourceModel, which is optional
    _sourceModelExists = False

    _sourceModel = SourceModel.from_int(0)

    def isSourceModelExists(self):
        """
        The attribute sourceModel is optional. Return True if this attribute exists.
        return True if and only if the sourceModel attribute exists.
        """
        return self._sourceModelExists

    def getSourceModel(self):
        """
        Get sourceModel, which is optional.
        return sourceModel as SourceModel
        raises ValueError If sourceModel does not exist.
        """
        if not self._sourceModelExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sourceModel
                + " attribute in table CalFlux does not exist!"
            )

        return self._sourceModel

    def setSourceModel(self, sourceModel):
        """
        Set sourceModel with the specified SourceModel value.
        sourceModel The SourceModel value to which sourceModel is to be set.


        """

        self._sourceModel = SourceModel(sourceModel)

        self._sourceModelExists = True

    def clearSourceModel(self):
        """
        Mark sourceModel, which is an optional field, as non-existent.
        """
        self._sourceModelExists = False

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
        sourceName,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numFrequencyRanges,
        numStokes,
        frequencyRanges,
        fluxMethod,
        flux,
        fluxError,
        stokes,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalFluxRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # sourceName is a str, compare using the == operator.
        if not (self._sourceName == sourceName):
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

        # numFrequencyRanges is a int, compare using the == operator.
        if not (self._numFrequencyRanges == numFrequencyRanges):
            return False

        # numStokes is a int, compare using the == operator.
        if not (self._numStokes == numStokes):
            return False

        # We compare two 2D arrays (lists).
        if frequencyRanges is not None:
            if self._frequencyRanges is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            frequencyRanges_dims = Parser.getListDims(frequencyRanges)
            this_frequencyRanges_dims = Parser.getListDims(self._frequencyRanges)
            if frequencyRanges_dims != this_frequencyRanges_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(frequencyRanges_dims[0]):
                for j in range(frequencyRanges_dims[1]):

                    # frequencyRanges is a Frequency, compare using the almostEquals method.
                    if not (
                        self._frequencyRanges[i][j].almostEquals(
                            frequencyRanges[i][j],
                            self.getTable().getFrequencyRangesEqTolerance(),
                        )
                    ):
                        return False

        # fluxMethod is a FluxCalibrationMethod, compare using the == operator on the getValue() output
        if not (self._fluxMethod.getValue() == fluxMethod.getValue()):
            return False

        # We compare two 2D arrays (lists).
        if flux is not None:
            if self._flux is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            flux_dims = Parser.getListDims(flux)
            this_flux_dims = Parser.getListDims(self._flux)
            if flux_dims != this_flux_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(flux_dims[0]):
                for j in range(flux_dims[1]):

                    # flux is an array of float, compare using == operator.
                    if not (self._flux[i][j] == flux[i][j]):
                        return False

        # We compare two 2D arrays (lists).
        if fluxError is not None:
            if self._fluxError is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            fluxError_dims = Parser.getListDims(fluxError)
            this_fluxError_dims = Parser.getListDims(self._fluxError)
            if fluxError_dims != this_fluxError_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(fluxError_dims[0]):
                for j in range(fluxError_dims[1]):

                    # fluxError is an array of float, compare using == operator.
                    if not (self._fluxError[i][j] == fluxError[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._stokes) != len(stokes):
            return False
        for indx in range(len(stokes)):

            # stokes is a list of StokesParameter, compare using == operator.
            if not (self._stokes[indx] == stokes[indx]):
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
            otherRow.getNumFrequencyRanges(),
            otherRow.getNumStokes(),
            otherRow.getFrequencyRanges(),
            otherRow.getFluxMethod(),
            otherRow.getFlux(),
            otherRow.getFluxError(),
            otherRow.getStokes(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        numFrequencyRanges,
        numStokes,
        frequencyRanges,
        fluxMethod,
        flux,
        fluxError,
        stokes,
    ):

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # numFrequencyRanges is a int, compare using the == operator.
        if not (self._numFrequencyRanges == numFrequencyRanges):
            return False

        # numStokes is a int, compare using the == operator.
        if not (self._numStokes == numStokes):
            return False

        # We compare two 2D arrays (lists).
        if frequencyRanges is not None:
            if self._frequencyRanges is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            frequencyRanges_dims = Parser.getListDims(frequencyRanges)
            this_frequencyRanges_dims = Parser.getListDims(self._frequencyRanges)
            if frequencyRanges_dims != this_frequencyRanges_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(frequencyRanges_dims[0]):
                for j in range(frequencyRanges_dims[1]):

                    # frequencyRanges is a Frequency, compare using the almostEquals method.
                    if not (
                        self._frequencyRanges[i][j].almostEquals(
                            frequencyRanges[i][j],
                            self.getTable().getFrequencyRangesEqTolerance(),
                        )
                    ):
                        return False

        # fluxMethod is a FluxCalibrationMethod, compare using the == operator on the getValue() output
        if not (self._fluxMethod.getValue() == fluxMethod.getValue()):
            return False

        # We compare two 2D arrays (lists).
        if flux is not None:
            if self._flux is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            flux_dims = Parser.getListDims(flux)
            this_flux_dims = Parser.getListDims(self._flux)
            if flux_dims != this_flux_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(flux_dims[0]):
                for j in range(flux_dims[1]):

                    # flux is an array of float, compare using == operator.
                    if not (self._flux[i][j] == flux[i][j]):
                        return False

        # We compare two 2D arrays (lists).
        if fluxError is not None:
            if self._fluxError is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            fluxError_dims = Parser.getListDims(fluxError)
            this_fluxError_dims = Parser.getListDims(self._fluxError)
            if fluxError_dims != this_fluxError_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(fluxError_dims[0]):
                for j in range(fluxError_dims[1]):

                    # fluxError is an array of float, compare using == operator.
                    if not (self._fluxError[i][j] == fluxError[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._stokes) != len(stokes):
            return False
        for indx in range(len(stokes)):

            # stokes is a list of StokesParameter, compare using == operator.
            if not (self._stokes[indx] == stokes[indx]):
                return False

        return True


# initialize the dictionary that maps fields to init methods
CalFluxRow.initFromBinMethods()
