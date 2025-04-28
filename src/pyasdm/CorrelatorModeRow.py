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
# File CorrelatorModeRow.py
#

import pyasdm.CorrelatorModeTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.BasebandName import BasebandName


from pyasdm.enumerations.AccumMode import AccumMode


from pyasdm.enumerations.AxisName import AxisName


from pyasdm.enumerations.FilterMode import FilterMode


from pyasdm.enumerations.CorrelatorName import CorrelatorName


from xml.dom import minidom

import copy


class CorrelatorModeRow:
    """
    The CorrelatorModeRow class is a row of a CorrelatorModeTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CorrelatorModeRow.
        When row is None, create an empty row attached to table, which must be a CorrelatorModeTable.
        When row is given, copy those values in to the new row. The row argument must be a CorrelatorModeRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CorrelatorModeTable):
            raise ValueError("table must be a CorrelatorModeTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._correlatorModeId = Tag()

        self._numBaseband = 0

        self._basebandNames = []  # this is a list of BasebandName []

        self._basebandConfig = []  # this is a list of int []

        self._accumMode = AccumMode.from_int(0)

        self._binMode = 0

        self._numAxes = 0

        self._axesOrderArray = []  # this is a list of AxisName []

        self._filterMode = []  # this is a list of FilterMode []

        self._correlatorName = CorrelatorName.from_int(0)

        if row is not None:
            if not isinstance(row, CorrelatorModeRow):
                raise ValueError("row must be a CorrelatorModeRow")

            # copy constructor

            self._correlatorModeId = Tag(row._correlatorModeId)

            self._numBaseband = row._numBaseband

            # basebandNames is a  list , make a deep copy
            self._basebandNames = copy.deepcopy(row._basebandNames)

            # basebandConfig is a  list , make a deep copy
            self._basebandConfig = copy.deepcopy(row._basebandConfig)

            # We force the attribute of the result to be not None
            if row._accumMode is None:
                self._accumMode = AccumMode.from_int(0)
            else:
                self._accumMode = AccumMode(row._accumMode)

            self._binMode = row._binMode

            self._numAxes = row._numAxes

            # axesOrderArray is a  list , make a deep copy
            self._axesOrderArray = copy.deepcopy(row._axesOrderArray)

            # filterMode is a  list , make a deep copy
            self._filterMode = copy.deepcopy(row._filterMode)

            # We force the attribute of the result to be not None
            if row._correlatorName is None:
                self._correlatorName = CorrelatorName.from_int(0)
            else:
                self._correlatorName = CorrelatorName(row._correlatorName)

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

        result += Parser.extendedValueToXML("correlatorModeId", self._correlatorModeId)

        result += Parser.valueToXML("numBaseband", self._numBaseband)

        result += Parser.listEnumValueToXML("basebandNames", self._basebandNames)

        result += Parser.listValueToXML("basebandConfig", self._basebandConfig)

        result += Parser.valueToXML("accumMode", AccumMode.name(self._accumMode))

        result += Parser.valueToXML("binMode", self._binMode)

        result += Parser.valueToXML("numAxes", self._numAxes)

        result += Parser.listEnumValueToXML("axesOrderArray", self._axesOrderArray)

        result += Parser.listEnumValueToXML("filterMode", self._filterMode)

        result += Parser.valueToXML(
            "correlatorName", CorrelatorName.name(self._correlatorName)
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
                "xmlrow is not a string or a minidom.Element", "CorrelatorModeTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException(
                "the argument is not a row", "CorrelatorModeTable"
            )

        # intrinsic attribute values

        correlatorModeIdNode = rowdom.getElementsByTagName("correlatorModeId")[0]

        self._correlatorModeId = Tag(correlatorModeIdNode.firstChild.data.strip())

        numBasebandNode = rowdom.getElementsByTagName("numBaseband")[0]

        self._numBaseband = int(numBasebandNode.firstChild.data.strip())

        basebandNamesNode = rowdom.getElementsByTagName("basebandNames")[0]

        basebandNamesStr = basebandNamesNode.firstChild.data.strip()
        self._basebandNames = Parser.stringListToLists(
            basebandNamesStr, BasebandName, "CorrelatorMode", False
        )

        basebandConfigNode = rowdom.getElementsByTagName("basebandConfig")[0]

        basebandConfigStr = basebandConfigNode.firstChild.data.strip()

        self._basebandConfig = Parser.stringListToLists(
            basebandConfigStr, int, "CorrelatorMode", False
        )

        accumModeNode = rowdom.getElementsByTagName("accumMode")[0]

        self._accumMode = AccumMode.newAccumMode(accumModeNode.firstChild.data.strip())

        binModeNode = rowdom.getElementsByTagName("binMode")[0]

        self._binMode = int(binModeNode.firstChild.data.strip())

        numAxesNode = rowdom.getElementsByTagName("numAxes")[0]

        self._numAxes = int(numAxesNode.firstChild.data.strip())

        axesOrderArrayNode = rowdom.getElementsByTagName("axesOrderArray")[0]

        axesOrderArrayStr = axesOrderArrayNode.firstChild.data.strip()
        self._axesOrderArray = Parser.stringListToLists(
            axesOrderArrayStr, AxisName, "CorrelatorMode", False
        )

        filterModeNode = rowdom.getElementsByTagName("filterMode")[0]

        filterModeStr = filterModeNode.firstChild.data.strip()
        self._filterMode = Parser.stringListToLists(
            filterModeStr, FilterMode, "CorrelatorMode", False
        )

        correlatorNameNode = rowdom.getElementsByTagName("correlatorName")[0]

        self._correlatorName = CorrelatorName.newCorrelatorName(
            correlatorNameNode.firstChild.data.strip()
        )

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._correlatorModeId.toBin(eos)

        eos.writeInt(self._numBaseband)

        eos.writeInt(len(self._basebandNames))
        for i in range(len(self._basebandNames)):

            eos.writeString(str(self._basebandNames[i]))

        eos.writeInt(len(self._basebandConfig))
        for i in range(len(self._basebandConfig)):

            eos.writeInt(self._basebandConfig[i])

        eos.writeString(str(self._accumMode))

        eos.writeInt(self._binMode)

        eos.writeInt(self._numAxes)

        eos.writeInt(len(self._axesOrderArray))
        for i in range(len(self._axesOrderArray)):

            eos.writeString(str(self._axesOrderArray[i]))

        eos.writeInt(len(self._filterMode))
        for i in range(len(self._filterMode)):

            eos.writeString(str(self._filterMode[i]))

        eos.writeString(str(self._correlatorName))

    @staticmethod
    def correlatorModeIdFromBin(row, eis):
        """
        Set the correlatorModeId in row from the EndianInput (eis) instance.
        """

        row._correlatorModeId = Tag.fromBin(eis)

    @staticmethod
    def numBasebandFromBin(row, eis):
        """
        Set the numBaseband in row from the EndianInput (eis) instance.
        """

        row._numBaseband = eis.readInt()

    @staticmethod
    def basebandNamesFromBin(row, eis):
        """
        Set the basebandNames in row from the EndianInput (eis) instance.
        """

        basebandNamesDim1 = eis.readInt()
        thisList = []
        for i in range(basebandNamesDim1):
            thisValue = BasebandName.literal(eis.readString())
            thisList.append(thisValue)
        row._basebandNames = thisList

    @staticmethod
    def basebandConfigFromBin(row, eis):
        """
        Set the basebandConfig in row from the EndianInput (eis) instance.
        """

        basebandConfigDim1 = eis.readInt()
        thisList = []
        for i in range(basebandConfigDim1):
            thisValue = eis.readInt()
            thisList.append(thisValue)
        row._basebandConfig = thisList

    @staticmethod
    def accumModeFromBin(row, eis):
        """
        Set the accumMode in row from the EndianInput (eis) instance.
        """

        row._accumMode = AccumMode.literal(eis.readString())

    @staticmethod
    def binModeFromBin(row, eis):
        """
        Set the binMode in row from the EndianInput (eis) instance.
        """

        row._binMode = eis.readInt()

    @staticmethod
    def numAxesFromBin(row, eis):
        """
        Set the numAxes in row from the EndianInput (eis) instance.
        """

        row._numAxes = eis.readInt()

    @staticmethod
    def axesOrderArrayFromBin(row, eis):
        """
        Set the axesOrderArray in row from the EndianInput (eis) instance.
        """

        axesOrderArrayDim1 = eis.readInt()
        thisList = []
        for i in range(axesOrderArrayDim1):
            thisValue = AxisName.literal(eis.readString())
            thisList.append(thisValue)
        row._axesOrderArray = thisList

    @staticmethod
    def filterModeFromBin(row, eis):
        """
        Set the filterMode in row from the EndianInput (eis) instance.
        """

        filterModeDim1 = eis.readInt()
        thisList = []
        for i in range(filterModeDim1):
            thisValue = FilterMode.literal(eis.readString())
            thisList.append(thisValue)
        row._filterMode = thisList

    @staticmethod
    def correlatorNameFromBin(row, eis):
        """
        Set the correlatorName in row from the EndianInput (eis) instance.
        """

        row._correlatorName = CorrelatorName.literal(eis.readString())

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["correlatorModeId"] = CorrelatorModeRow.correlatorModeIdFromBin
        _fromBinMethods["numBaseband"] = CorrelatorModeRow.numBasebandFromBin
        _fromBinMethods["basebandNames"] = CorrelatorModeRow.basebandNamesFromBin
        _fromBinMethods["basebandConfig"] = CorrelatorModeRow.basebandConfigFromBin
        _fromBinMethods["accumMode"] = CorrelatorModeRow.accumModeFromBin
        _fromBinMethods["binMode"] = CorrelatorModeRow.binModeFromBin
        _fromBinMethods["numAxes"] = CorrelatorModeRow.numAxesFromBin
        _fromBinMethods["axesOrderArray"] = CorrelatorModeRow.axesOrderArrayFromBin
        _fromBinMethods["filterMode"] = CorrelatorModeRow.filterModeFromBin
        _fromBinMethods["correlatorName"] = CorrelatorModeRow.correlatorNameFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CorrelatorModeRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CorrelatorMode",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute correlatorModeId

    _correlatorModeId = Tag()

    def getCorrelatorModeId(self):
        """
        Get correlatorModeId.
        return correlatorModeId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._correlatorModeId)

    def setCorrelatorModeId(self, correlatorModeId):
        """
        Set correlatorModeId with the specified Tag value.
        correlatorModeId The Tag value to which correlatorModeId is to be set.
        The value of correlatorModeId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the correlatorModeId field, which is part of the key, after this row has been added to this table."
            )

        self._correlatorModeId = Tag(correlatorModeId)

    # ===> Attribute numBaseband

    _numBaseband = 0

    def getNumBaseband(self):
        """
        Get numBaseband.
        return numBaseband as int
        """

        return self._numBaseband

    def setNumBaseband(self, numBaseband):
        """
        Set numBaseband with the specified int value.
        numBaseband The int value to which numBaseband is to be set.


        """

        self._numBaseband = int(numBaseband)

    # ===> Attribute basebandNames

    _basebandNames = None  # this is a 1D list of BasebandName

    def getBasebandNames(self):
        """
        Get basebandNames.
        return basebandNames as BasebandName []
        """

        return copy.deepcopy(self._basebandNames)

    def setBasebandNames(self, basebandNames):
        """
        Set basebandNames with the specified BasebandName []  value.
        basebandNames The BasebandName []  value to which basebandNames is to be set.


        """

        # value must be a list
        if not isinstance(basebandNames, list):
            raise ValueError("The value of basebandNames must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(basebandNames)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of basebandNames is not correct")

            # the type of the values in the list must be BasebandName
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(basebandNames, BasebandName):
                raise ValueError(
                    "type of the first value in basebandNames is not BasebandName as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._basebandNames = copy.deepcopy(basebandNames)
        except Exception as exc:
            raise ValueError("Invalid basebandNames : " + str(exc))

    # ===> Attribute basebandConfig

    _basebandConfig = None  # this is a 1D list of int

    def getBasebandConfig(self):
        """
        Get basebandConfig.
        return basebandConfig as int []
        """

        return copy.deepcopy(self._basebandConfig)

    def setBasebandConfig(self, basebandConfig):
        """
        Set basebandConfig with the specified int []  value.
        basebandConfig The int []  value to which basebandConfig is to be set.


        """

        # value must be a list
        if not isinstance(basebandConfig, list):
            raise ValueError("The value of basebandConfig must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(basebandConfig)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of basebandConfig is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(basebandConfig, int):
                raise ValueError(
                    "type of the first value in basebandConfig is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._basebandConfig = copy.deepcopy(basebandConfig)
        except Exception as exc:
            raise ValueError("Invalid basebandConfig : " + str(exc))

    # ===> Attribute accumMode

    _accumMode = AccumMode.from_int(0)

    def getAccumMode(self):
        """
        Get accumMode.
        return accumMode as AccumMode
        """

        return self._accumMode

    def setAccumMode(self, accumMode):
        """
        Set accumMode with the specified AccumMode value.
        accumMode The AccumMode value to which accumMode is to be set.


        """

        self._accumMode = AccumMode(accumMode)

    # ===> Attribute binMode

    _binMode = 0

    def getBinMode(self):
        """
        Get binMode.
        return binMode as int
        """

        return self._binMode

    def setBinMode(self, binMode):
        """
        Set binMode with the specified int value.
        binMode The int value to which binMode is to be set.


        """

        self._binMode = int(binMode)

    # ===> Attribute numAxes

    _numAxes = 0

    def getNumAxes(self):
        """
        Get numAxes.
        return numAxes as int
        """

        return self._numAxes

    def setNumAxes(self, numAxes):
        """
        Set numAxes with the specified int value.
        numAxes The int value to which numAxes is to be set.


        """

        self._numAxes = int(numAxes)

    # ===> Attribute axesOrderArray

    _axesOrderArray = None  # this is a 1D list of AxisName

    def getAxesOrderArray(self):
        """
        Get axesOrderArray.
        return axesOrderArray as AxisName []
        """

        return copy.deepcopy(self._axesOrderArray)

    def setAxesOrderArray(self, axesOrderArray):
        """
        Set axesOrderArray with the specified AxisName []  value.
        axesOrderArray The AxisName []  value to which axesOrderArray is to be set.


        """

        # value must be a list
        if not isinstance(axesOrderArray, list):
            raise ValueError("The value of axesOrderArray must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(axesOrderArray)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of axesOrderArray is not correct")

            # the type of the values in the list must be AxisName
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(axesOrderArray, AxisName):
                raise ValueError(
                    "type of the first value in axesOrderArray is not AxisName as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._axesOrderArray = copy.deepcopy(axesOrderArray)
        except Exception as exc:
            raise ValueError("Invalid axesOrderArray : " + str(exc))

    # ===> Attribute filterMode

    _filterMode = None  # this is a 1D list of FilterMode

    def getFilterMode(self):
        """
        Get filterMode.
        return filterMode as FilterMode []
        """

        return copy.deepcopy(self._filterMode)

    def setFilterMode(self, filterMode):
        """
        Set filterMode with the specified FilterMode []  value.
        filterMode The FilterMode []  value to which filterMode is to be set.


        """

        # value must be a list
        if not isinstance(filterMode, list):
            raise ValueError("The value of filterMode must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(filterMode)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of filterMode is not correct")

            # the type of the values in the list must be FilterMode
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(filterMode, FilterMode):
                raise ValueError(
                    "type of the first value in filterMode is not FilterMode as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._filterMode = copy.deepcopy(filterMode)
        except Exception as exc:
            raise ValueError("Invalid filterMode : " + str(exc))

    # ===> Attribute correlatorName

    _correlatorName = CorrelatorName.from_int(0)

    def getCorrelatorName(self):
        """
        Get correlatorName.
        return correlatorName as CorrelatorName
        """

        return self._correlatorName

    def setCorrelatorName(self, correlatorName):
        """
        Set correlatorName with the specified CorrelatorName value.
        correlatorName The CorrelatorName value to which correlatorName is to be set.


        """

        self._correlatorName = CorrelatorName(correlatorName)

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(
        self,
        numBaseband,
        basebandNames,
        basebandConfig,
        accumMode,
        binMode,
        numAxes,
        axesOrderArray,
        filterMode,
        correlatorName,
    ):
        """
        Compare each attribute except the autoincrementable one of this CorrelatorModeRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # numBaseband is a int, compare using the == operator.
        if not (self._numBaseband == numBaseband):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._basebandNames) != len(basebandNames):
            return False
        for indx in range(len(basebandNames)):

            # basebandNames is a list of BasebandName, compare using == operator.
            if not (self._basebandNames[indx] == basebandNames[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._basebandConfig) != len(basebandConfig):
            return False
        for indx in range(len(basebandConfig)):

            # basebandConfig is a list of int, compare using == operator.
            if not (self._basebandConfig[indx] == basebandConfig[indx]):
                return False

        # accumMode is a AccumMode, compare using the == operator on the getValue() output
        if not (self._accumMode.getValue() == accumMode.getValue()):
            return False

        # binMode is a int, compare using the == operator.
        if not (self._binMode == binMode):
            return False

        # numAxes is a int, compare using the == operator.
        if not (self._numAxes == numAxes):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._axesOrderArray) != len(axesOrderArray):
            return False
        for indx in range(len(axesOrderArray)):

            # axesOrderArray is a list of AxisName, compare using == operator.
            if not (self._axesOrderArray[indx] == axesOrderArray[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._filterMode) != len(filterMode):
            return False
        for indx in range(len(filterMode)):

            # filterMode is a list of FilterMode, compare using == operator.
            if not (self._filterMode[indx] == filterMode[indx]):
                return False

        # correlatorName is a CorrelatorName, compare using the == operator on the getValue() output
        if not (self._correlatorName.getValue() == correlatorName.getValue()):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumBaseband(),
            otherRow.getBasebandNames(),
            otherRow.getBasebandConfig(),
            otherRow.getAccumMode(),
            otherRow.getBinMode(),
            otherRow.getNumAxes(),
            otherRow.getAxesOrderArray(),
            otherRow.getFilterMode(),
            otherRow.getCorrelatorName(),
        )

    def compareRequiredValue(
        self,
        numBaseband,
        basebandNames,
        basebandConfig,
        accumMode,
        binMode,
        numAxes,
        axesOrderArray,
        filterMode,
        correlatorName,
    ):

        # numBaseband is a int, compare using the == operator.
        if not (self._numBaseband == numBaseband):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._basebandNames) != len(basebandNames):
            return False
        for indx in range(len(basebandNames)):

            # basebandNames is a list of BasebandName, compare using == operator.
            if not (self._basebandNames[indx] == basebandNames[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._basebandConfig) != len(basebandConfig):
            return False
        for indx in range(len(basebandConfig)):

            # basebandConfig is a list of int, compare using == operator.
            if not (self._basebandConfig[indx] == basebandConfig[indx]):
                return False

        # accumMode is a AccumMode, compare using the == operator on the getValue() output
        if not (self._accumMode.getValue() == accumMode.getValue()):
            return False

        # binMode is a int, compare using the == operator.
        if not (self._binMode == binMode):
            return False

        # numAxes is a int, compare using the == operator.
        if not (self._numAxes == numAxes):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._axesOrderArray) != len(axesOrderArray):
            return False
        for indx in range(len(axesOrderArray)):

            # axesOrderArray is a list of AxisName, compare using == operator.
            if not (self._axesOrderArray[indx] == axesOrderArray[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._filterMode) != len(filterMode):
            return False
        for indx in range(len(filterMode)):

            # filterMode is a list of FilterMode, compare using == operator.
            if not (self._filterMode[indx] == filterMode[indx]):
                return False

        # correlatorName is a CorrelatorName, compare using the == operator on the getValue() output
        if not (self._correlatorName.getValue() == correlatorName.getValue()):
            return False

        return True


# initialize the dictionary that maps fields to init methods
CorrelatorModeRow.initFromBinMethods()
