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
# File CalWVRRow.py
#

import pyasdm.CalWVRTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.WVRMethod import WVRMethod


from xml.dom import minidom

import copy


class CalWVRRow:
    """
    The CalWVRRow class is a row of a CalWVRTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalWVRRow.
        When row is None, create an empty row attached to table, which must be a CalWVRTable.
        When row is given, copy those values in to the new row. The row argument must be a CalWVRRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalWVRTable):
            raise ValueError("table must be a CalWVRTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._wvrMethod = WVRMethod.from_int(0)

        self._antennaName = None

        self._numInputAntennas = 0

        self._inputAntennaNames = []  # this is a list of str []

        self._numChan = 0

        self._chanFreq = []  # this is a list of Frequency []

        self._chanWidth = []  # this is a list of Frequency []

        self._refTemp = []  # this is a list of Temperature []  []

        self._numPoly = 0

        self._pathCoeff = []  # this is a list of float []  []  []

        self._polyFreqLimits = []  # this is a list of Frequency []

        self._wetPath = []  # this is a list of float []

        self._dryPath = []  # this is a list of float []

        self._water = Length()

        self._tauBaselineExists = False

        self._tauBaseline = None

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalWVRRow):
                raise ValueError("row must be a CalWVRRow")

            # copy constructor

            self._antennaName = row._antennaName

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            # We force the attribute of the result to be not None
            if row._wvrMethod is None:
                self._wvrMethod = WVRMethod.from_int(0)
            else:
                self._wvrMethod = WVRMethod(row._wvrMethod)

            self._numInputAntennas = row._numInputAntennas

            # inputAntennaNames is a  list , make a deep copy
            self._inputAntennaNames = copy.deepcopy(row._inputAntennaNames)

            self._numChan = row._numChan

            # chanFreq is a  list , make a deep copy
            self._chanFreq = copy.deepcopy(row._chanFreq)

            # chanWidth is a  list , make a deep copy
            self._chanWidth = copy.deepcopy(row._chanWidth)

            # refTemp is a  list , make a deep copy
            self._refTemp = copy.deepcopy(row._refTemp)

            self._numPoly = row._numPoly

            # pathCoeff is a  list , make a deep copy
            self._pathCoeff = copy.deepcopy(row._pathCoeff)

            # polyFreqLimits is a  list , make a deep copy
            self._polyFreqLimits = copy.deepcopy(row._polyFreqLimits)

            # wetPath is a  list , make a deep copy
            self._wetPath = copy.deepcopy(row._wetPath)

            # dryPath is a  list , make a deep copy
            self._dryPath = copy.deepcopy(row._dryPath)

            self._water = Length(row._water)

            # by default set systematically tauBaseline's value to something not None

            if row._tauBaselineExists:

                self._tauBaseline = row._tauBaseline

                self._tauBaselineExists = True

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

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.valueToXML("wvrMethod", WVRMethod.name(self._wvrMethod))

        result += Parser.valueToXML("antennaName", self._antennaName)

        result += Parser.valueToXML("numInputAntennas", self._numInputAntennas)

        result += Parser.listValueToXML("inputAntennaNames", self._inputAntennaNames)

        result += Parser.valueToXML("numChan", self._numChan)

        result += Parser.listExtendedValueToXML("chanFreq", self._chanFreq)

        result += Parser.listExtendedValueToXML("chanWidth", self._chanWidth)

        result += Parser.listExtendedValueToXML("refTemp", self._refTemp)

        result += Parser.valueToXML("numPoly", self._numPoly)

        result += Parser.listValueToXML("pathCoeff", self._pathCoeff)

        result += Parser.listExtendedValueToXML("polyFreqLimits", self._polyFreqLimits)

        result += Parser.listValueToXML("wetPath", self._wetPath)

        result += Parser.listValueToXML("dryPath", self._dryPath)

        result += Parser.extendedValueToXML("water", self._water)

        if self._tauBaselineExists:

            result += Parser.valueToXML("tauBaseline", self._tauBaseline)

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
                "xmlrow is not a string or a minidom.Element", "CalWVRTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalWVRTable")

        # intrinsic attribute values

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        wvrMethodNode = rowdom.getElementsByTagName("wvrMethod")[0]

        self._wvrMethod = WVRMethod.newWVRMethod(wvrMethodNode.firstChild.data.strip())

        antennaNameNode = rowdom.getElementsByTagName("antennaName")[0]

        self._antennaName = str(antennaNameNode.firstChild.data.strip())

        numInputAntennasNode = rowdom.getElementsByTagName("numInputAntennas")[0]

        self._numInputAntennas = int(numInputAntennasNode.firstChild.data.strip())

        inputAntennaNamesNode = rowdom.getElementsByTagName("inputAntennaNames")[0]

        inputAntennaNamesStr = inputAntennaNamesNode.firstChild.data.strip()

        self._inputAntennaNames = Parser.stringListToLists(
            inputAntennaNamesStr, str, "CalWVR", False
        )

        numChanNode = rowdom.getElementsByTagName("numChan")[0]

        self._numChan = int(numChanNode.firstChild.data.strip())

        chanFreqNode = rowdom.getElementsByTagName("chanFreq")[0]

        chanFreqStr = chanFreqNode.firstChild.data.strip()

        self._chanFreq = Parser.stringListToLists(
            chanFreqStr, Frequency, "CalWVR", True
        )

        chanWidthNode = rowdom.getElementsByTagName("chanWidth")[0]

        chanWidthStr = chanWidthNode.firstChild.data.strip()

        self._chanWidth = Parser.stringListToLists(
            chanWidthStr, Frequency, "CalWVR", True
        )

        refTempNode = rowdom.getElementsByTagName("refTemp")[0]

        refTempStr = refTempNode.firstChild.data.strip()

        self._refTemp = Parser.stringListToLists(
            refTempStr, Temperature, "CalWVR", True
        )

        numPolyNode = rowdom.getElementsByTagName("numPoly")[0]

        self._numPoly = int(numPolyNode.firstChild.data.strip())

        pathCoeffNode = rowdom.getElementsByTagName("pathCoeff")[0]

        pathCoeffStr = pathCoeffNode.firstChild.data.strip()

        self._pathCoeff = Parser.stringListToLists(pathCoeffStr, float, "CalWVR", False)

        polyFreqLimitsNode = rowdom.getElementsByTagName("polyFreqLimits")[0]

        polyFreqLimitsStr = polyFreqLimitsNode.firstChild.data.strip()

        self._polyFreqLimits = Parser.stringListToLists(
            polyFreqLimitsStr, Frequency, "CalWVR", True
        )

        wetPathNode = rowdom.getElementsByTagName("wetPath")[0]

        wetPathStr = wetPathNode.firstChild.data.strip()

        self._wetPath = Parser.stringListToLists(wetPathStr, float, "CalWVR", False)

        dryPathNode = rowdom.getElementsByTagName("dryPath")[0]

        dryPathStr = dryPathNode.firstChild.data.strip()

        self._dryPath = Parser.stringListToLists(dryPathStr, float, "CalWVR", False)

        waterNode = rowdom.getElementsByTagName("water")[0]

        self._water = Length(waterNode.firstChild.data.strip())

        tauBaselineNode = rowdom.getElementsByTagName("tauBaseline")
        if len(tauBaselineNode) > 0:

            self._tauBaseline = float(tauBaselineNode[0].firstChild.data.strip())

            self._tauBaselineExists = True

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

        self._calDataId.toBin(eos)

        self._calReductionId.toBin(eos)

        self._startValidTime.toBin(eos)

        self._endValidTime.toBin(eos)

        eos.writeString(self._wvrMethod.toString())

        eos.writeInt(self._numInputAntennas)

        eos.writeInt(len(self._inputAntennaNames))
        for i in range(len(self._inputAntennaNames)):

            eos.writeStr(self._inputAntennaNames[i])

        eos.writeInt(self._numChan)

        Frequency.listToBin(self._chanFreq, eos)

        Frequency.listToBin(self._chanWidth, eos)

        Temperature.listToBin(self._refTemp, eos)

        eos.writeInt(self._numPoly)

        # null array case, unsure if this is possible but this should work
        if self._pathCoeff is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            pathCoeff_dims = pyasdm.utils.getListDims(self._pathCoeff)
        # assumes it really is 3D
        eos.writeInt(pathCoeff_dims[0])
        eos.writeInt(pathCoeff_dims[1])
        eos.writeInt(pathCoeff_dims[2])
        for i in range(pathCoeff_dims[0]):
            for j in range(pathCoeff_dims[1]):
                for k in range(pathCoeff_dims[2]):
                    eos.writeFloat(self._pathCoeff[i][j][k])

        Frequency.listToBin(self._polyFreqLimits, eos)

        eos.writeInt(len(self._wetPath))
        for i in range(len(self._wetPath)):

            eos.writeFloat(self._wetPath[i])

        eos.writeInt(len(self._dryPath))
        for i in range(len(self._dryPath)):

            eos.writeFloat(self._dryPath[i])

        self._water.toBin(eos)

        eos.writeBool(self._tauBaselineExists)
        if self._tauBaselineExists:

            eos.writeFloat(self._tauBaseline)

    @staticmethod
    def antennaNameFromBin(row, eis):
        """
        Set the antennaName in row from the EndianInput (eis) instance.
        """

        row._antennaName = eis.readStr()

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
    def wvrMethodFromBin(row, eis):
        """
        Set the wvrMethod in row from the EndianInput (eis) instance.
        """

        row._wvrMethod = WVRMethod.from_int(eis.readInt())

    @staticmethod
    def numInputAntennasFromBin(row, eis):
        """
        Set the numInputAntennas in row from the EndianInput (eis) instance.
        """

        row._numInputAntennas = eis.readInt()

    @staticmethod
    def inputAntennaNamesFromBin(row, eis):
        """
        Set the inputAntennaNames in row from the EndianInput (eis) instance.
        """

        inputAntennaNamesDim1 = eis.readInt()
        thisList = []
        for i in range(inputAntennaNamesDim1):
            thisValue = eis.readStr()
            thisList.append(thisValue)
        row._inputAntennaNames = thisList

    @staticmethod
    def numChanFromBin(row, eis):
        """
        Set the numChan in row from the EndianInput (eis) instance.
        """

        row._numChan = eis.readInt()

    @staticmethod
    def chanFreqFromBin(row, eis):
        """
        Set the chanFreq in row from the EndianInput (eis) instance.
        """

        row._chanFreq = Frequency.from1DBin(eis)

    @staticmethod
    def chanWidthFromBin(row, eis):
        """
        Set the chanWidth in row from the EndianInput (eis) instance.
        """

        row._chanWidth = Frequency.from1DBin(eis)

    @staticmethod
    def refTempFromBin(row, eis):
        """
        Set the refTemp in row from the EndianInput (eis) instance.
        """

        row._refTemp = Temperature.from2DBin(eis)

    @staticmethod
    def numPolyFromBin(row, eis):
        """
        Set the numPoly in row from the EndianInput (eis) instance.
        """

        row._numPoly = eis.readInt()

    @staticmethod
    def pathCoeffFromBin(row, eis):
        """
        Set the pathCoeff in row from the EndianInput (eis) instance.
        """

        pathCoeffDim1 = eis.readInt()
        pathCoeffDim2 = eis.readInt()
        pathCoeffDim3 = eis.readInt()
        thisList = []
        for i in range(pathCoeffDim1):
            thisList_j = []
            for j in range(pathCoeffDim2):
                thisList_k = []
                for k in range(pathCoeffDim3):
                    thisValue = eis.readFloat()
                    thisList_k.append(thisValue)
                thisList_j.append(thisList_k)
            thisList.append(thisList_j)
        row.pathCoeff = thisList

    @staticmethod
    def polyFreqLimitsFromBin(row, eis):
        """
        Set the polyFreqLimits in row from the EndianInput (eis) instance.
        """

        row._polyFreqLimits = Frequency.from1DBin(eis)

    @staticmethod
    def wetPathFromBin(row, eis):
        """
        Set the wetPath in row from the EndianInput (eis) instance.
        """

        wetPathDim1 = eis.readInt()
        thisList = []
        for i in range(wetPathDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._wetPath = thisList

    @staticmethod
    def dryPathFromBin(row, eis):
        """
        Set the dryPath in row from the EndianInput (eis) instance.
        """

        dryPathDim1 = eis.readInt()
        thisList = []
        for i in range(dryPathDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._dryPath = thisList

    @staticmethod
    def waterFromBin(row, eis):
        """
        Set the water in row from the EndianInput (eis) instance.
        """

        row._water = Length.fromBin(eis)

    @staticmethod
    def tauBaselineFromBin(row, eis):
        """
        Set the optional tauBaseline in row from the EndianInput (eis) instance.
        """
        row._tauBaselineExists = eis.readBool()
        if row._tauBaselineExists:

            row._tauBaseline = eis.readFloat()

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaName"] = CalWVRRow.antennaNameFromBin
        _fromBinMethods["calDataId"] = CalWVRRow.calDataIdFromBin
        _fromBinMethods["calReductionId"] = CalWVRRow.calReductionIdFromBin
        _fromBinMethods["startValidTime"] = CalWVRRow.startValidTimeFromBin
        _fromBinMethods["endValidTime"] = CalWVRRow.endValidTimeFromBin
        _fromBinMethods["wvrMethod"] = CalWVRRow.wvrMethodFromBin
        _fromBinMethods["numInputAntennas"] = CalWVRRow.numInputAntennasFromBin
        _fromBinMethods["inputAntennaNames"] = CalWVRRow.inputAntennaNamesFromBin
        _fromBinMethods["numChan"] = CalWVRRow.numChanFromBin
        _fromBinMethods["chanFreq"] = CalWVRRow.chanFreqFromBin
        _fromBinMethods["chanWidth"] = CalWVRRow.chanWidthFromBin
        _fromBinMethods["refTemp"] = CalWVRRow.refTempFromBin
        _fromBinMethods["numPoly"] = CalWVRRow.numPolyFromBin
        _fromBinMethods["pathCoeff"] = CalWVRRow.pathCoeffFromBin
        _fromBinMethods["polyFreqLimits"] = CalWVRRow.polyFreqLimitsFromBin
        _fromBinMethods["wetPath"] = CalWVRRow.wetPathFromBin
        _fromBinMethods["dryPath"] = CalWVRRow.dryPathFromBin
        _fromBinMethods["water"] = CalWVRRow.waterFromBin

        _fromBinMethods["tauBaseline"] = CalWVRRow.tauBaselineFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CalWVRRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalWVR",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

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

    # ===> Attribute wvrMethod

    _wvrMethod = WVRMethod.from_int(0)

    def getWvrMethod(self):
        """
        Get wvrMethod.
        return wvrMethod as WVRMethod
        """

        return self._wvrMethod

    def setWvrMethod(self, wvrMethod):
        """
        Set wvrMethod with the specified WVRMethod value.
        wvrMethod The WVRMethod value to which wvrMethod is to be set.


        """

        self._wvrMethod = WVRMethod(wvrMethod)

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

    # ===> Attribute numInputAntennas

    _numInputAntennas = 0

    def getNumInputAntennas(self):
        """
        Get numInputAntennas.
        return numInputAntennas as int
        """

        return self._numInputAntennas

    def setNumInputAntennas(self, numInputAntennas):
        """
        Set numInputAntennas with the specified int value.
        numInputAntennas The int value to which numInputAntennas is to be set.


        """

        self._numInputAntennas = int(numInputAntennas)

    # ===> Attribute inputAntennaNames

    _inputAntennaNames = None  # this is a 1D list of str

    def getInputAntennaNames(self):
        """
        Get inputAntennaNames.
        return inputAntennaNames as str []
        """

        return copy.deepcopy(self._inputAntennaNames)

    def setInputAntennaNames(self, inputAntennaNames):
        """
        Set inputAntennaNames with the specified str []  value.
        inputAntennaNames The str []  value to which inputAntennaNames is to be set.


        """

        # value must be a list
        if not isinstance(inputAntennaNames, list):
            raise ValueError("The value of inputAntennaNames must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(inputAntennaNames)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of inputAntennaNames is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(inputAntennaNames, str):
                raise ValueError(
                    "type of the first value in inputAntennaNames is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._inputAntennaNames = copy.deepcopy(inputAntennaNames)
        except Exception as exc:
            raise ValueError("Invalid inputAntennaNames : " + str(exc))

    # ===> Attribute numChan

    _numChan = 0

    def getNumChan(self):
        """
        Get numChan.
        return numChan as int
        """

        return self._numChan

    def setNumChan(self, numChan):
        """
        Set numChan with the specified int value.
        numChan The int value to which numChan is to be set.


        """

        self._numChan = int(numChan)

    # ===> Attribute chanFreq

    _chanFreq = None  # this is a 1D list of Frequency

    def getChanFreq(self):
        """
        Get chanFreq.
        return chanFreq as Frequency []
        """

        return copy.deepcopy(self._chanFreq)

    def setChanFreq(self, chanFreq):
        """
        Set chanFreq with the specified Frequency []  value.
        chanFreq The Frequency []  value to which chanFreq is to be set.
        The value of chanFreq can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(chanFreq, list):
            raise ValueError("The value of chanFreq must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(chanFreq)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of chanFreq is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(chanFreq, Frequency):
                raise ValueError(
                    "type of the first value in chanFreq is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._chanFreq = copy.deepcopy(chanFreq)
        except Exception as exc:
            raise ValueError("Invalid chanFreq : " + str(exc))

    # ===> Attribute chanWidth

    _chanWidth = None  # this is a 1D list of Frequency

    def getChanWidth(self):
        """
        Get chanWidth.
        return chanWidth as Frequency []
        """

        return copy.deepcopy(self._chanWidth)

    def setChanWidth(self, chanWidth):
        """
        Set chanWidth with the specified Frequency []  value.
        chanWidth The Frequency []  value to which chanWidth is to be set.
        The value of chanWidth can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(chanWidth, list):
            raise ValueError("The value of chanWidth must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(chanWidth)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of chanWidth is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(chanWidth, Frequency):
                raise ValueError(
                    "type of the first value in chanWidth is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._chanWidth = copy.deepcopy(chanWidth)
        except Exception as exc:
            raise ValueError("Invalid chanWidth : " + str(exc))

    # ===> Attribute refTemp

    _refTemp = None  # this is a 2D list of Temperature

    def getRefTemp(self):
        """
        Get refTemp.
        return refTemp as Temperature []  []
        """

        return copy.deepcopy(self._refTemp)

    def setRefTemp(self, refTemp):
        """
        Set refTemp with the specified Temperature []  []  value.
        refTemp The Temperature []  []  value to which refTemp is to be set.
        The value of refTemp can be anything allowed by the Temperature []  []  constructor.

        """

        # value must be a list
        if not isinstance(refTemp, list):
            raise ValueError("The value of refTemp must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(refTemp)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of refTemp is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(refTemp, Temperature):
                raise ValueError(
                    "type of the first value in refTemp is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._refTemp = copy.deepcopy(refTemp)
        except Exception as exc:
            raise ValueError("Invalid refTemp : " + str(exc))

    # ===> Attribute numPoly

    _numPoly = 0

    def getNumPoly(self):
        """
        Get numPoly.
        return numPoly as int
        """

        return self._numPoly

    def setNumPoly(self, numPoly):
        """
        Set numPoly with the specified int value.
        numPoly The int value to which numPoly is to be set.


        """

        self._numPoly = int(numPoly)

    # ===> Attribute pathCoeff

    _pathCoeff = None  # this is a 2D list of float

    def getPathCoeff(self):
        """
        Get pathCoeff.
        return pathCoeff as float []  []  []
        """

        return copy.deepcopy(self._pathCoeff)

    def setPathCoeff(self, pathCoeff):
        """
        Set pathCoeff with the specified float []  []  []  value.
        pathCoeff The float []  []  []  value to which pathCoeff is to be set.


        """

        # value must be a list
        if not isinstance(pathCoeff, list):
            raise ValueError("The value of pathCoeff must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(pathCoeff)

            shapeOK = len(listDims) == 3

            if not shapeOK:
                raise ValueError("shape of pathCoeff is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(pathCoeff, float):
                raise ValueError(
                    "type of the first value in pathCoeff is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._pathCoeff = copy.deepcopy(pathCoeff)
        except Exception as exc:
            raise ValueError("Invalid pathCoeff : " + str(exc))

    # ===> Attribute polyFreqLimits

    _polyFreqLimits = None  # this is a 1D list of Frequency

    def getPolyFreqLimits(self):
        """
        Get polyFreqLimits.
        return polyFreqLimits as Frequency []
        """

        return copy.deepcopy(self._polyFreqLimits)

    def setPolyFreqLimits(self, polyFreqLimits):
        """
        Set polyFreqLimits with the specified Frequency []  value.
        polyFreqLimits The Frequency []  value to which polyFreqLimits is to be set.
        The value of polyFreqLimits can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(polyFreqLimits, list):
            raise ValueError("The value of polyFreqLimits must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(polyFreqLimits)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of polyFreqLimits is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(polyFreqLimits, Frequency):
                raise ValueError(
                    "type of the first value in polyFreqLimits is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._polyFreqLimits = copy.deepcopy(polyFreqLimits)
        except Exception as exc:
            raise ValueError("Invalid polyFreqLimits : " + str(exc))

    # ===> Attribute wetPath

    _wetPath = None  # this is a 1D list of float

    def getWetPath(self):
        """
        Get wetPath.
        return wetPath as float []
        """

        return copy.deepcopy(self._wetPath)

    def setWetPath(self, wetPath):
        """
        Set wetPath with the specified float []  value.
        wetPath The float []  value to which wetPath is to be set.


        """

        # value must be a list
        if not isinstance(wetPath, list):
            raise ValueError("The value of wetPath must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(wetPath)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of wetPath is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(wetPath, float):
                raise ValueError(
                    "type of the first value in wetPath is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._wetPath = copy.deepcopy(wetPath)
        except Exception as exc:
            raise ValueError("Invalid wetPath : " + str(exc))

    # ===> Attribute dryPath

    _dryPath = None  # this is a 1D list of float

    def getDryPath(self):
        """
        Get dryPath.
        return dryPath as float []
        """

        return copy.deepcopy(self._dryPath)

    def setDryPath(self, dryPath):
        """
        Set dryPath with the specified float []  value.
        dryPath The float []  value to which dryPath is to be set.


        """

        # value must be a list
        if not isinstance(dryPath, list):
            raise ValueError("The value of dryPath must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(dryPath)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of dryPath is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(dryPath, float):
                raise ValueError(
                    "type of the first value in dryPath is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._dryPath = copy.deepcopy(dryPath)
        except Exception as exc:
            raise ValueError("Invalid dryPath : " + str(exc))

    # ===> Attribute water

    _water = Length()

    def getWater(self):
        """
        Get water.
        return water as Length
        """

        # make sure it is a copy of Length
        return Length(self._water)

    def setWater(self, water):
        """
        Set water with the specified Length value.
        water The Length value to which water is to be set.
        The value of water can be anything allowed by the Length constructor.

        """

        self._water = Length(water)

    # ===> Attribute tauBaseline, which is optional
    _tauBaselineExists = False

    _tauBaseline = None

    def isTauBaselineExists(self):
        """
        The attribute tauBaseline is optional. Return True if this attribute exists.
        return True if and only if the tauBaseline attribute exists.
        """
        return self._tauBaselineExists

    def getTauBaseline(self):
        """
        Get tauBaseline, which is optional.
        return tauBaseline as float
        raises ValueError If tauBaseline does not exist.
        """
        if not self._tauBaselineExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tauBaseline
                + " attribute in table CalWVR does not exist!"
            )

        return self._tauBaseline

    def setTauBaseline(self, tauBaseline):
        """
        Set tauBaseline with the specified float value.
        tauBaseline The float value to which tauBaseline is to be set.


        """

        self._tauBaseline = float(tauBaseline)

        self._tauBaselineExists = True

    def clearTauBaseline(self):
        """
        Mark tauBaseline, which is an optional field, as non-existent.
        """
        self._tauBaselineExists = False

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
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        wvrMethod,
        numInputAntennas,
        inputAntennaNames,
        numChan,
        chanFreq,
        chanWidth,
        refTemp,
        numPoly,
        pathCoeff,
        polyFreqLimits,
        wetPath,
        dryPath,
        water,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalWVRRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaName is a str, compare using the == operator.
        if not (self._antennaName == antennaName):
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

        # wvrMethod is a WVRMethod, compare using the == operator on the getValue() output
        if not (self._wvrMethod.getValue() == wvrMethod.getValue()):
            return False

        # numInputAntennas is a int, compare using the == operator.
        if not (self._numInputAntennas == numInputAntennas):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._inputAntennaNames) != len(inputAntennaNames):
            return False
        for indx in range(len(inputAntennaNames)):

            # inputAntennaNames is a list of str, compare using == operator.
            if not (self._inputAntennaNames[indx] == inputAntennaNames[indx]):
                return False

        # numChan is a int, compare using the == operator.
        if not (self._numChan == numChan):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._chanFreq) != len(chanFreq):
            return False
        for indx in range(len(chanFreq)):

            # chanFreq is a list of Frequency, compare using the almostEquals method.
            if not self._chanFreq[indx].almostEquals(
                chanFreq[indx], self.getTable().getChanFreqEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._chanWidth) != len(chanWidth):
            return False
        for indx in range(len(chanWidth)):

            # chanWidth is a list of Frequency, compare using the almostEquals method.
            if not self._chanWidth[indx].almostEquals(
                chanWidth[indx], self.getTable().getChanWidthEqTolerance()
            ):
                return False

        # We compare two 2D arrays (lists).
        if refTemp is not None:
            if self._refTemp is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            refTemp_dims = pyasdm.utils.getListDims(refTemp)
            this_refTemp_dims = pyasdm.utils.getListDims(self._refTemp)
            if refTemp_dims != this_refTemp_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(refTemp_dims[0]):
                for j in range(refTemp_dims[1]):

                    # refTemp is a Temperature, compare using the almostEquals method.
                    if not (
                        self._refTemp[i][j].almostEquals(
                            refTemp[i][j], self.getTable().getRefTempEqTolerance()
                        )
                    ):
                        return False

        # numPoly is a int, compare using the == operator.
        if not (self._numPoly == numPoly):
            return False

        # We compare two 3D arrays.
        # Compare firstly their dimensions and then their values.
        if pathCoeff is not None:
            if self._pathCoeff is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            pathCoeff_dims = pyasdm.utils.getListDims(pathCoeff)
            this_pathCoeff_dims = pyasdm.utils.getListDims(self._pathCoeff)
            if pathCoeff_dims != this_pathCoeff_dims:
                return False
            # assumes they are both 3D arrays, the internal one should be
            for i in range(pathCoeff_dims[0]):
                for j in range(pathCoeff_dims[1]):
                    for k in range(pathCoeff_dims[2]):

                        # pathCoeff is an array of float, compare using == operator.
                        if not (self._pathCoeff[i][j][k] == pathCoeff[i][j][k]):
                            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polyFreqLimits) != len(polyFreqLimits):
            return False
        for indx in range(len(polyFreqLimits)):

            # polyFreqLimits is a list of Frequency, compare using the almostEquals method.
            if not self._polyFreqLimits[indx].almostEquals(
                polyFreqLimits[indx], self.getTable().getPolyFreqLimitsEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._wetPath) != len(wetPath):
            return False
        for indx in range(len(wetPath)):

            # wetPath is a list of float, compare using == operator.
            if not (self._wetPath[indx] == wetPath[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._dryPath) != len(dryPath):
            return False
        for indx in range(len(dryPath)):

            # dryPath is a list of float, compare using == operator.
            if not (self._dryPath[indx] == dryPath[indx]):
                return False

        # water is a Length, compare using the almostEquals method.
        if not self._water.almostEquals(water, self.getTable().getWaterEqTolerance()):
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
            otherRow.getWvrMethod(),
            otherRow.getNumInputAntennas(),
            otherRow.getInputAntennaNames(),
            otherRow.getNumChan(),
            otherRow.getChanFreq(),
            otherRow.getChanWidth(),
            otherRow.getRefTemp(),
            otherRow.getNumPoly(),
            otherRow.getPathCoeff(),
            otherRow.getPolyFreqLimits(),
            otherRow.getWetPath(),
            otherRow.getDryPath(),
            otherRow.getWater(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        wvrMethod,
        numInputAntennas,
        inputAntennaNames,
        numChan,
        chanFreq,
        chanWidth,
        refTemp,
        numPoly,
        pathCoeff,
        polyFreqLimits,
        wetPath,
        dryPath,
        water,
    ):

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # wvrMethod is a WVRMethod, compare using the == operator on the getValue() output
        if not (self._wvrMethod.getValue() == wvrMethod.getValue()):
            return False

        # numInputAntennas is a int, compare using the == operator.
        if not (self._numInputAntennas == numInputAntennas):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._inputAntennaNames) != len(inputAntennaNames):
            return False
        for indx in range(len(inputAntennaNames)):

            # inputAntennaNames is a list of str, compare using == operator.
            if not (self._inputAntennaNames[indx] == inputAntennaNames[indx]):
                return False

        # numChan is a int, compare using the == operator.
        if not (self._numChan == numChan):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._chanFreq) != len(chanFreq):
            return False
        for indx in range(len(chanFreq)):

            # chanFreq is a list of Frequency, compare using the almostEquals method.
            if not self._chanFreq[indx].almostEquals(
                chanFreq[indx], self.getTable().getChanFreqEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._chanWidth) != len(chanWidth):
            return False
        for indx in range(len(chanWidth)):

            # chanWidth is a list of Frequency, compare using the almostEquals method.
            if not self._chanWidth[indx].almostEquals(
                chanWidth[indx], self.getTable().getChanWidthEqTolerance()
            ):
                return False

        # We compare two 2D arrays (lists).
        if refTemp is not None:
            if self._refTemp is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            refTemp_dims = pyasdm.utils.getListDims(refTemp)
            this_refTemp_dims = pyasdm.utils.getListDims(self._refTemp)
            if refTemp_dims != this_refTemp_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(refTemp_dims[0]):
                for j in range(refTemp_dims[1]):

                    # refTemp is a Temperature, compare using the almostEquals method.
                    if not (
                        self._refTemp[i][j].almostEquals(
                            refTemp[i][j], self.getTable().getRefTempEqTolerance()
                        )
                    ):
                        return False

        # numPoly is a int, compare using the == operator.
        if not (self._numPoly == numPoly):
            return False

        # We compare two 3D arrays.
        # Compare firstly their dimensions and then their values.
        if pathCoeff is not None:
            if self._pathCoeff is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            pathCoeff_dims = pyasdm.utils.getListDims(pathCoeff)
            this_pathCoeff_dims = pyasdm.utils.getListDims(self._pathCoeff)
            if pathCoeff_dims != this_pathCoeff_dims:
                return False
            # assumes they are both 3D arrays, the internal one should be
            for i in range(pathCoeff_dims[0]):
                for j in range(pathCoeff_dims[1]):
                    for k in range(pathCoeff_dims[2]):

                        # pathCoeff is an array of float, compare using == operator.
                        if not (self._pathCoeff[i][j][k] == pathCoeff[i][j][k]):
                            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polyFreqLimits) != len(polyFreqLimits):
            return False
        for indx in range(len(polyFreqLimits)):

            # polyFreqLimits is a list of Frequency, compare using the almostEquals method.
            if not self._polyFreqLimits[indx].almostEquals(
                polyFreqLimits[indx], self.getTable().getPolyFreqLimitsEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._wetPath) != len(wetPath):
            return False
        for indx in range(len(wetPath)):

            # wetPath is a list of float, compare using == operator.
            if not (self._wetPath[indx] == wetPath[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._dryPath) != len(dryPath):
            return False
        for indx in range(len(dryPath)):

            # dryPath is a list of float, compare using == operator.
            if not (self._dryPath[indx] == dryPath[indx]):
                return False

        # water is a Length, compare using the almostEquals method.
        if not self._water.almostEquals(water, self.getTable().getWaterEqTolerance()):
            return False

        return True


# initialize the dictionary that maps fields to init methods
CalWVRRow.initFromBinMethods()
