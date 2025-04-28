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
# File WVMCalRow.py
#

import pyasdm.WVMCalTable

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


class WVMCalRow:
    """
    The WVMCalRow class is a row of a WVMCalTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a WVMCalRow.
        When row is None, create an empty row attached to table, which must be a WVMCalTable.
        When row is given, copy those values in to the new row. The row argument must be a WVMCalRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.WVMCalTable):
            raise ValueError("table must be a WVMCalTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._timeInterval = ArrayTimeInterval()

        self._wvrMethod = WVRMethod.from_int(0)

        self._polyFreqLimits = []  # this is a list of Frequency []

        self._numInputAntenna = 0

        self._numChan = 0

        self._numPoly = 0

        self._pathCoeff = []  # this is a list of float []  []  []

        self._refTemp = []  # this is a list of Temperature []  []

        # extrinsic attributes

        self._antennaId = Tag()

        self._inputAntennaId = []  # this is a list of Tag []

        self._spectralWindowId = Tag()

        if row is not None:
            if not isinstance(row, WVMCalRow):
                raise ValueError("row must be a WVMCalRow")

            # copy constructor

            self._antennaId = Tag(row._antennaId)

            self._spectralWindowId = Tag(row._spectralWindowId)

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            # We force the attribute of the result to be not None
            if row._wvrMethod is None:
                self._wvrMethod = WVRMethod.from_int(0)
            else:
                self._wvrMethod = WVRMethod(row._wvrMethod)

            # polyFreqLimits is a  list , make a deep copy
            self._polyFreqLimits = copy.deepcopy(row._polyFreqLimits)

            self._numInputAntenna = row._numInputAntenna

            self._numChan = row._numChan

            self._numPoly = row._numPoly

            # pathCoeff is a  list , make a deep copy
            self._pathCoeff = copy.deepcopy(row._pathCoeff)

            # refTemp is a  list , make a deep copy
            self._refTemp = copy.deepcopy(row._refTemp)

            # inputAntennaId is a list, let's populate self._inputAntennaId element by element.
            if self._inputAntennaId is None:
                self._inputAntennaId = []

            for i in range(len(row._inputAntennaId)):

                self._inputAntennaId.append(Tag(row._inputAntennaId[i]))

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

        result += Parser.valueToXML("wvrMethod", WVRMethod.name(self._wvrMethod))

        result += Parser.listExtendedValueToXML("polyFreqLimits", self._polyFreqLimits)

        result += Parser.valueToXML("numInputAntenna", self._numInputAntenna)

        result += Parser.valueToXML("numChan", self._numChan)

        result += Parser.valueToXML("numPoly", self._numPoly)

        result += Parser.listValueToXML("pathCoeff", self._pathCoeff)

        result += Parser.listExtendedValueToXML("refTemp", self._refTemp)

        # extrinsic attributes

        result += Parser.extendedValueToXML("antennaId", self._antennaId)

        result += Parser.listExtendedValueToXML("inputAntennaId", self._inputAntennaId)

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
                "xmlrow is not a string or a minidom.Element", "WVMCalTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "WVMCalTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        wvrMethodNode = rowdom.getElementsByTagName("wvrMethod")[0]

        self._wvrMethod = WVRMethod.newWVRMethod(wvrMethodNode.firstChild.data.strip())

        polyFreqLimitsNode = rowdom.getElementsByTagName("polyFreqLimits")[0]

        polyFreqLimitsStr = polyFreqLimitsNode.firstChild.data.strip()

        self._polyFreqLimits = Parser.stringListToLists(
            polyFreqLimitsStr, Frequency, "WVMCal", True
        )

        numInputAntennaNode = rowdom.getElementsByTagName("numInputAntenna")[0]

        self._numInputAntenna = int(numInputAntennaNode.firstChild.data.strip())

        numChanNode = rowdom.getElementsByTagName("numChan")[0]

        self._numChan = int(numChanNode.firstChild.data.strip())

        numPolyNode = rowdom.getElementsByTagName("numPoly")[0]

        self._numPoly = int(numPolyNode.firstChild.data.strip())

        pathCoeffNode = rowdom.getElementsByTagName("pathCoeff")[0]

        pathCoeffStr = pathCoeffNode.firstChild.data.strip()

        self._pathCoeff = Parser.stringListToLists(pathCoeffStr, float, "WVMCal", False)

        refTempNode = rowdom.getElementsByTagName("refTemp")[0]

        refTempStr = refTempNode.firstChild.data.strip()

        self._refTemp = Parser.stringListToLists(
            refTempStr, Temperature, "WVMCal", True
        )

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        self._antennaId = Tag(antennaIdNode.firstChild.data.strip())

        inputAntennaIdNode = rowdom.getElementsByTagName("inputAntennaId")[0]

        inputAntennaIdStr = inputAntennaIdNode.firstChild.data.strip()

        self._inputAntennaId = Parser.stringListToLists(
            inputAntennaIdStr, Tag, "WVMCal", True
        )

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

        eos.writeString(str(self._wvrMethod))

        Frequency.listToBin(self._polyFreqLimits, eos)

        eos.writeInt(self._numInputAntenna)

        eos.writeInt(self._numChan)

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

        Temperature.listToBin(self._refTemp, eos)

        Tag.listToBin(self._inputAntennaId, eos)

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
    def wvrMethodFromBin(row, eis):
        """
        Set the wvrMethod in row from the EndianInput (eis) instance.
        """

        row._wvrMethod = WVRMethod.literal(eis.readString())

    @staticmethod
    def polyFreqLimitsFromBin(row, eis):
        """
        Set the polyFreqLimits in row from the EndianInput (eis) instance.
        """

        row._polyFreqLimits = Frequency.from1DBin(eis)

    @staticmethod
    def numInputAntennaFromBin(row, eis):
        """
        Set the numInputAntenna in row from the EndianInput (eis) instance.
        """

        row._numInputAntenna = eis.readInt()

    @staticmethod
    def numChanFromBin(row, eis):
        """
        Set the numChan in row from the EndianInput (eis) instance.
        """

        row._numChan = eis.readInt()

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
        row._pathCoeff = thisList

    @staticmethod
    def refTempFromBin(row, eis):
        """
        Set the refTemp in row from the EndianInput (eis) instance.
        """

        row._refTemp = Temperature.from2DBin(eis)

    @staticmethod
    def inputAntennaIdFromBin(row, eis):
        """
        Set the inputAntennaId in row from the EndianInput (eis) instance.
        """

        row._inputAntennaId = Tag.from1DBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaId"] = WVMCalRow.antennaIdFromBin
        _fromBinMethods["spectralWindowId"] = WVMCalRow.spectralWindowIdFromBin
        _fromBinMethods["timeInterval"] = WVMCalRow.timeIntervalFromBin
        _fromBinMethods["wvrMethod"] = WVMCalRow.wvrMethodFromBin
        _fromBinMethods["polyFreqLimits"] = WVMCalRow.polyFreqLimitsFromBin
        _fromBinMethods["numInputAntenna"] = WVMCalRow.numInputAntennaFromBin
        _fromBinMethods["numChan"] = WVMCalRow.numChanFromBin
        _fromBinMethods["numPoly"] = WVMCalRow.numPolyFromBin
        _fromBinMethods["pathCoeff"] = WVMCalRow.pathCoeffFromBin
        _fromBinMethods["refTemp"] = WVMCalRow.refTempFromBin
        _fromBinMethods["inputAntennaId"] = WVMCalRow.inputAntennaIdFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = WVMCalRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " WVMCal",
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

    # ===> Attribute numInputAntenna

    _numInputAntenna = 0

    def getNumInputAntenna(self):
        """
        Get numInputAntenna.
        return numInputAntenna as int
        """

        return self._numInputAntenna

    def setNumInputAntenna(self, numInputAntenna):
        """
        Set numInputAntenna with the specified int value.
        numInputAntenna The int value to which numInputAntenna is to be set.


        """

        self._numInputAntenna = int(numInputAntenna)

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

    # ===> Attribute inputAntennaId

    _inputAntennaId = []  # this is a list of Tag []

    def getInputAntennaId(self):
        """
        Get inputAntennaId.
        return inputAntennaId as Tag []
        """

        return copy.deepcopy(self._inputAntennaId)

    def setInputAntennaId(self, inputAntennaId):
        """
        Set inputAntennaId with the specified Tag []  value.
        inputAntennaId The Tag []  value to which inputAntennaId is to be set.
        The value of inputAntennaId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(inputAntennaId, list):
            raise ValueError("The value of inputAntennaId must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(inputAntennaId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of inputAntennaId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(inputAntennaId, Tag):
                raise ValueError(
                    "type of the first value in inputAntennaId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._inputAntennaId = copy.deepcopy(inputAntennaId)
        except Exception as exc:
            raise ValueError("Invalid inputAntennaId : " + str(exc))

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

    def getAntennaUsingAntennaId(self):
        """
        Returns the row in the Antenna table having Antenna.antennaId == antennaId

        """

        return self._table.getContainer().getAntenna().getRowByKey(self._antennaId)

    def setOneInputAntennaId(self, index, inputAntennaId):
        """
        Set inputAntennaId[index] with the specified Tag value.
        index The index in inputAntennaId where to set the Tag value.
        inputAntennaId The Tag value to which inputAntennaId[index] is to be set.

        """

        self._inputAntennaId[index] = Tag(inputAntennaId)

    # ===> hasmany link from a row of WVMCal table to many rows of Antenna table.

    def addInputAntennaId(self, id):
        """
        Append a Tag to inputAntennaId
        id the Tag to be appended to inputAntennaId
        """
        if isinstance(id, list):
            for thisValue in id:
                self._inputAntennaId.append(Tag(thisValue))
        else:
            self._inputAntennaId.append(Tag(id))

    def getOneInputAntennaId(self, i):
        """
        Returns the Tag stored in inputAntennaId at position i.
        """
        return self._inputAntennaId[i]

    def getAntennaUsingInputAntennaId(self, i):
        """
        Returns the AntennaRow linked to this row via the Tag stored in inputAntennaId
        at position i.
        """

        return (
            self._table.getContainer().getAntenna().getRowByKey(self._inputAntennaId[i])
        )

    def getAntennasUsingInputAntennaId(self):
        """
        Returns the array of AntennaRow linked to this row via the Tags stored in inputAntennaId
        """
        result = []
        for thisItem in self._inputAntennaId:
            result.append(self._table.getContainer().getAntenna().getRowByKey(thisItem))

        return result

    # comparison methods

    def compareNoAutoInc(
        self,
        antennaId,
        spectralWindowId,
        timeInterval,
        wvrMethod,
        polyFreqLimits,
        numInputAntenna,
        numChan,
        numPoly,
        pathCoeff,
        refTemp,
        inputAntennaId,
    ):
        """
        Compare each attribute except the autoincrementable one of this WVMCalRow with
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

        # wvrMethod is a WVRMethod, compare using the == operator on the getValue() output
        if not (self._wvrMethod.getValue() == wvrMethod.getValue()):
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

        # numInputAntenna is a int, compare using the == operator.
        if not (self._numInputAntenna == numInputAntenna):
            return False

        # numChan is a int, compare using the == operator.
        if not (self._numChan == numChan):
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

        # inputAntennaId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._inputAntennaId) != len(inputAntennaId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._inputAntennaId)):
            if not (self._inputAntennaId[indx].equals(inputAntennaId[indx])):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getWvrMethod(),
            otherRow.getPolyFreqLimits(),
            otherRow.getNumInputAntenna(),
            otherRow.getNumChan(),
            otherRow.getNumPoly(),
            otherRow.getPathCoeff(),
            otherRow.getRefTemp(),
            otherRow.getInputAntennaId(),
        )

    def compareRequiredValue(
        self,
        wvrMethod,
        polyFreqLimits,
        numInputAntenna,
        numChan,
        numPoly,
        pathCoeff,
        refTemp,
        inputAntennaId,
    ):

        # wvrMethod is a WVRMethod, compare using the == operator on the getValue() output
        if not (self._wvrMethod.getValue() == wvrMethod.getValue()):
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

        # numInputAntenna is a int, compare using the == operator.
        if not (self._numInputAntenna == numInputAntenna):
            return False

        # numChan is a int, compare using the == operator.
        if not (self._numChan == numChan):
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

        # inputAntennaId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._inputAntennaId) != len(inputAntennaId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._inputAntennaId)):
            if not (self._inputAntennaId[indx].equals(inputAntennaId[indx])):
                return False

        return True


# initialize the dictionary that maps fields to init methods
WVMCalRow.initFromBinMethods()
