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
# File SwitchCycleRow.py
#

import pyasdm.SwitchCycleTable

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


class SwitchCycleRow:
    """
    The SwitchCycleRow class is a row of a SwitchCycleTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a SwitchCycleRow.
        When row is None, create an empty row attached to table, which must be a SwitchCycleTable.
        When row is given, copy those values in to the new row. The row argument must be a SwitchCycleRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.SwitchCycleTable):
            raise ValueError("table must be a SwitchCycleTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._switchCycleId = Tag()

        self._numStep = 0

        self._weightArray = []  # this is a list of float []

        self._dirOffsetArray = []  # this is a list of Angle []  []

        self._freqOffsetArray = []  # this is a list of Frequency []

        self._stepDurationArray = []  # this is a list of Interval []

        self._directionCodeExists = False

        self._directionCode = DirectionReferenceCode.from_int(0)

        self._directionEquinoxExists = False

        self._directionEquinox = ArrayTime()

        if row is not None:
            if not isinstance(row, SwitchCycleRow):
                raise ValueError("row must be a SwitchCycleRow")

            # copy constructor

            self._switchCycleId = Tag(row._switchCycleId)

            self._numStep = row._numStep

            # weightArray is a  list , make a deep copy
            self._weightArray = copy.deepcopy(row._weightArray)

            # dirOffsetArray is a  list , make a deep copy
            self._dirOffsetArray = copy.deepcopy(row._dirOffsetArray)

            # freqOffsetArray is a  list , make a deep copy
            self._freqOffsetArray = copy.deepcopy(row._freqOffsetArray)

            # stepDurationArray is a  list , make a deep copy
            self._stepDurationArray = copy.deepcopy(row._stepDurationArray)

            # by default set systematically directionCode's value to something not None

            self._directionCode = DirectionReferenceCode.from_int(0)

            if row._directionCodeExists:

                if row._directionCode is not None:
                    self._directionCode = row._directionCode

                self._directionCodeExists = True

            # by default set systematically directionEquinox's value to something not None

            if row._directionEquinoxExists:

                self._directionEquinox = ArrayTime(row._directionEquinox)

                self._directionEquinoxExists = True

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

        result += Parser.extendedValueToXML("switchCycleId", self._switchCycleId)

        result += Parser.valueToXML("numStep", self._numStep)

        result += Parser.listValueToXML("weightArray", self._weightArray)

        result += Parser.listExtendedValueToXML("dirOffsetArray", self._dirOffsetArray)

        result += Parser.listExtendedValueToXML(
            "freqOffsetArray", self._freqOffsetArray
        )

        result += Parser.listExtendedValueToXML(
            "stepDurationArray", self._stepDurationArray
        )

        if self._directionCodeExists:

            result += Parser.valueToXML(
                "directionCode", DirectionReferenceCode.name(self._directionCode)
            )

        if self._directionEquinoxExists:

            result += Parser.extendedValueToXML(
                "directionEquinox", self._directionEquinox
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
                "xmlrow is not a string or a minidom.Element", "SwitchCycleTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "SwitchCycleTable")

        # intrinsic attribute values

        switchCycleIdNode = rowdom.getElementsByTagName("switchCycleId")[0]

        self._switchCycleId = Tag(switchCycleIdNode.firstChild.data.strip())

        numStepNode = rowdom.getElementsByTagName("numStep")[0]

        self._numStep = int(numStepNode.firstChild.data.strip())

        weightArrayNode = rowdom.getElementsByTagName("weightArray")[0]

        weightArrayStr = weightArrayNode.firstChild.data.strip()

        self._weightArray = Parser.stringListToLists(
            weightArrayStr, float, "SwitchCycle", False
        )

        dirOffsetArrayNode = rowdom.getElementsByTagName("dirOffsetArray")[0]

        dirOffsetArrayStr = dirOffsetArrayNode.firstChild.data.strip()

        self._dirOffsetArray = Parser.stringListToLists(
            dirOffsetArrayStr, Angle, "SwitchCycle", True
        )

        freqOffsetArrayNode = rowdom.getElementsByTagName("freqOffsetArray")[0]

        freqOffsetArrayStr = freqOffsetArrayNode.firstChild.data.strip()

        self._freqOffsetArray = Parser.stringListToLists(
            freqOffsetArrayStr, Frequency, "SwitchCycle", True
        )

        stepDurationArrayNode = rowdom.getElementsByTagName("stepDurationArray")[0]

        stepDurationArrayStr = stepDurationArrayNode.firstChild.data.strip()

        self._stepDurationArray = Parser.stringListToLists(
            stepDurationArrayStr, Interval, "SwitchCycle", True
        )

        directionCodeNode = rowdom.getElementsByTagName("directionCode")
        if len(directionCodeNode) > 0:

            self._directionCode = DirectionReferenceCode.newDirectionReferenceCode(
                directionCodeNode[0].firstChild.data.strip()
            )

            self._directionCodeExists = True

        directionEquinoxNode = rowdom.getElementsByTagName("directionEquinox")
        if len(directionEquinoxNode) > 0:

            self._directionEquinox = ArrayTime(
                directionEquinoxNode[0].firstChild.data.strip()
            )

            self._directionEquinoxExists = True

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._switchCycleId.toBin(eos)

        eos.writeInt(self._numStep)

        eos.writeInt(len(self._weightArray))
        for i in range(len(self._weightArray)):

            eos.writeFloat(self._weightArray[i])

        Angle.listToBin(self._dirOffsetArray, eos)

        Frequency.listToBin(self._freqOffsetArray, eos)

        Interval.listToBin(self._stepDurationArray, eos)

        eos.writeBool(self._directionCodeExists)
        if self._directionCodeExists:

            eos.writeString(str(self._directionCode))

        eos.writeBool(self._directionEquinoxExists)
        if self._directionEquinoxExists:

            self._directionEquinox.toBin(eos)

    @staticmethod
    def switchCycleIdFromBin(row, eis):
        """
        Set the switchCycleId in row from the EndianInput (eis) instance.
        """

        row._switchCycleId = Tag.fromBin(eis)

    @staticmethod
    def numStepFromBin(row, eis):
        """
        Set the numStep in row from the EndianInput (eis) instance.
        """

        row._numStep = eis.readInt()

    @staticmethod
    def weightArrayFromBin(row, eis):
        """
        Set the weightArray in row from the EndianInput (eis) instance.
        """

        weightArrayDim1 = eis.readInt()
        thisList = []
        for i in range(weightArrayDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._weightArray = thisList

    @staticmethod
    def dirOffsetArrayFromBin(row, eis):
        """
        Set the dirOffsetArray in row from the EndianInput (eis) instance.
        """

        row._dirOffsetArray = Angle.from2DBin(eis)

    @staticmethod
    def freqOffsetArrayFromBin(row, eis):
        """
        Set the freqOffsetArray in row from the EndianInput (eis) instance.
        """

        row._freqOffsetArray = Frequency.from1DBin(eis)

    @staticmethod
    def stepDurationArrayFromBin(row, eis):
        """
        Set the stepDurationArray in row from the EndianInput (eis) instance.
        """

        row._stepDurationArray = Interval.from1DBin(eis)

    @staticmethod
    def directionCodeFromBin(row, eis):
        """
        Set the optional directionCode in row from the EndianInput (eis) instance.
        """
        row._directionCodeExists = eis.readBool()
        if row._directionCodeExists:

            row._directionCode = DirectionReferenceCode.literal(eis.readString())

    @staticmethod
    def directionEquinoxFromBin(row, eis):
        """
        Set the optional directionEquinox in row from the EndianInput (eis) instance.
        """
        row._directionEquinoxExists = eis.readBool()
        if row._directionEquinoxExists:

            row._directionEquinox = ArrayTime.fromBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["switchCycleId"] = SwitchCycleRow.switchCycleIdFromBin
        _fromBinMethods["numStep"] = SwitchCycleRow.numStepFromBin
        _fromBinMethods["weightArray"] = SwitchCycleRow.weightArrayFromBin
        _fromBinMethods["dirOffsetArray"] = SwitchCycleRow.dirOffsetArrayFromBin
        _fromBinMethods["freqOffsetArray"] = SwitchCycleRow.freqOffsetArrayFromBin
        _fromBinMethods["stepDurationArray"] = SwitchCycleRow.stepDurationArrayFromBin

        _fromBinMethods["directionCode"] = SwitchCycleRow.directionCodeFromBin
        _fromBinMethods["directionEquinox"] = SwitchCycleRow.directionEquinoxFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = SwitchCycleRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " SwitchCycle",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute switchCycleId

    _switchCycleId = Tag()

    def getSwitchCycleId(self):
        """
        Get switchCycleId.
        return switchCycleId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._switchCycleId)

    def setSwitchCycleId(self, switchCycleId):
        """
        Set switchCycleId with the specified Tag value.
        switchCycleId The Tag value to which switchCycleId is to be set.
        The value of switchCycleId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the switchCycleId field, which is part of the key, after this row has been added to this table."
            )

        self._switchCycleId = Tag(switchCycleId)

    # ===> Attribute numStep

    _numStep = 0

    def getNumStep(self):
        """
        Get numStep.
        return numStep as int
        """

        return self._numStep

    def setNumStep(self, numStep):
        """
        Set numStep with the specified int value.
        numStep The int value to which numStep is to be set.


        """

        self._numStep = int(numStep)

    # ===> Attribute weightArray

    _weightArray = None  # this is a 1D list of float

    def getWeightArray(self):
        """
        Get weightArray.
        return weightArray as float []
        """

        return copy.deepcopy(self._weightArray)

    def setWeightArray(self, weightArray):
        """
        Set weightArray with the specified float []  value.
        weightArray The float []  value to which weightArray is to be set.


        """

        # value must be a list
        if not isinstance(weightArray, list):
            raise ValueError("The value of weightArray must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(weightArray)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of weightArray is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(weightArray, float):
                raise ValueError(
                    "type of the first value in weightArray is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._weightArray = copy.deepcopy(weightArray)
        except Exception as exc:
            raise ValueError("Invalid weightArray : " + str(exc))

    # ===> Attribute dirOffsetArray

    _dirOffsetArray = None  # this is a 2D list of Angle

    def getDirOffsetArray(self):
        """
        Get dirOffsetArray.
        return dirOffsetArray as Angle []  []
        """

        return copy.deepcopy(self._dirOffsetArray)

    def setDirOffsetArray(self, dirOffsetArray):
        """
        Set dirOffsetArray with the specified Angle []  []  value.
        dirOffsetArray The Angle []  []  value to which dirOffsetArray is to be set.
        The value of dirOffsetArray can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(dirOffsetArray, list):
            raise ValueError("The value of dirOffsetArray must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(dirOffsetArray)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of dirOffsetArray is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(dirOffsetArray, Angle):
                raise ValueError(
                    "type of the first value in dirOffsetArray is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._dirOffsetArray = copy.deepcopy(dirOffsetArray)
        except Exception as exc:
            raise ValueError("Invalid dirOffsetArray : " + str(exc))

    # ===> Attribute freqOffsetArray

    _freqOffsetArray = None  # this is a 1D list of Frequency

    def getFreqOffsetArray(self):
        """
        Get freqOffsetArray.
        return freqOffsetArray as Frequency []
        """

        return copy.deepcopy(self._freqOffsetArray)

    def setFreqOffsetArray(self, freqOffsetArray):
        """
        Set freqOffsetArray with the specified Frequency []  value.
        freqOffsetArray The Frequency []  value to which freqOffsetArray is to be set.
        The value of freqOffsetArray can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(freqOffsetArray, list):
            raise ValueError("The value of freqOffsetArray must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(freqOffsetArray)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of freqOffsetArray is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(freqOffsetArray, Frequency):
                raise ValueError(
                    "type of the first value in freqOffsetArray is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._freqOffsetArray = copy.deepcopy(freqOffsetArray)
        except Exception as exc:
            raise ValueError("Invalid freqOffsetArray : " + str(exc))

    # ===> Attribute stepDurationArray

    _stepDurationArray = None  # this is a 1D list of Interval

    def getStepDurationArray(self):
        """
        Get stepDurationArray.
        return stepDurationArray as Interval []
        """

        return copy.deepcopy(self._stepDurationArray)

    def setStepDurationArray(self, stepDurationArray):
        """
        Set stepDurationArray with the specified Interval []  value.
        stepDurationArray The Interval []  value to which stepDurationArray is to be set.
        The value of stepDurationArray can be anything allowed by the Interval []  constructor.

        """

        # value must be a list
        if not isinstance(stepDurationArray, list):
            raise ValueError("The value of stepDurationArray must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(stepDurationArray)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of stepDurationArray is not correct")

            # the type of the values in the list must be Interval
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(stepDurationArray, Interval):
                raise ValueError(
                    "type of the first value in stepDurationArray is not Interval as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._stepDurationArray = copy.deepcopy(stepDurationArray)
        except Exception as exc:
            raise ValueError("Invalid stepDurationArray : " + str(exc))

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
                + " attribute in table SwitchCycle does not exist!"
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

    _directionEquinox = ArrayTime()

    def isDirectionEquinoxExists(self):
        """
        The attribute directionEquinox is optional. Return True if this attribute exists.
        return True if and only if the directionEquinox attribute exists.
        """
        return self._directionEquinoxExists

    def getDirectionEquinox(self):
        """
        Get directionEquinox, which is optional.
        return directionEquinox as ArrayTime
        raises ValueError If directionEquinox does not exist.
        """
        if not self._directionEquinoxExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + directionEquinox
                + " attribute in table SwitchCycle does not exist!"
            )

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._directionEquinox)

    def setDirectionEquinox(self, directionEquinox):
        """
        Set directionEquinox with the specified ArrayTime value.
        directionEquinox The ArrayTime value to which directionEquinox is to be set.
        The value of directionEquinox can be anything allowed by the ArrayTime constructor.

        """

        self._directionEquinox = ArrayTime(directionEquinox)

        self._directionEquinoxExists = True

    def clearDirectionEquinox(self):
        """
        Mark directionEquinox, which is an optional field, as non-existent.
        """
        self._directionEquinoxExists = False

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(
        self, numStep, weightArray, dirOffsetArray, freqOffsetArray, stepDurationArray
    ):
        """
        Compare each attribute except the autoincrementable one of this SwitchCycleRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # numStep is a int, compare using the == operator.
        if not (self._numStep == numStep):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._weightArray) != len(weightArray):
            return False
        for indx in range(len(weightArray)):

            # weightArray is a list of float, compare using == operator.
            if not (self._weightArray[indx] == weightArray[indx]):
                return False

        # We compare two 2D arrays (lists).
        if dirOffsetArray is not None:
            if self._dirOffsetArray is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            dirOffsetArray_dims = pyasdm.utils.getListDims(dirOffsetArray)
            this_dirOffsetArray_dims = pyasdm.utils.getListDims(self._dirOffsetArray)
            if dirOffsetArray_dims != this_dirOffsetArray_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(dirOffsetArray_dims[0]):
                for j in range(dirOffsetArray_dims[1]):

                    # dirOffsetArray is a Angle, compare using the almostEquals method.
                    if not (
                        self._dirOffsetArray[i][j].almostEquals(
                            dirOffsetArray[i][j],
                            self.getTable().getDirOffsetArrayEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._freqOffsetArray) != len(freqOffsetArray):
            return False
        for indx in range(len(freqOffsetArray)):

            # freqOffsetArray is a list of Frequency, compare using the almostEquals method.
            if not self._freqOffsetArray[indx].almostEquals(
                freqOffsetArray[indx], self.getTable().getFreqOffsetArrayEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._stepDurationArray) != len(stepDurationArray):
            return False
        for indx in range(len(stepDurationArray)):

            # stepDurationArray is a list of Interval, compare using equals method.
            if not self._stepDurationArray[indx].equals(stepDurationArray[indx]):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumStep(),
            otherRow.getWeightArray(),
            otherRow.getDirOffsetArray(),
            otherRow.getFreqOffsetArray(),
            otherRow.getStepDurationArray(),
        )

    def compareRequiredValue(
        self, numStep, weightArray, dirOffsetArray, freqOffsetArray, stepDurationArray
    ):

        # numStep is a int, compare using the == operator.
        if not (self._numStep == numStep):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._weightArray) != len(weightArray):
            return False
        for indx in range(len(weightArray)):

            # weightArray is a list of float, compare using == operator.
            if not (self._weightArray[indx] == weightArray[indx]):
                return False

        # We compare two 2D arrays (lists).
        if dirOffsetArray is not None:
            if self._dirOffsetArray is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            dirOffsetArray_dims = pyasdm.utils.getListDims(dirOffsetArray)
            this_dirOffsetArray_dims = pyasdm.utils.getListDims(self._dirOffsetArray)
            if dirOffsetArray_dims != this_dirOffsetArray_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(dirOffsetArray_dims[0]):
                for j in range(dirOffsetArray_dims[1]):

                    # dirOffsetArray is a Angle, compare using the almostEquals method.
                    if not (
                        self._dirOffsetArray[i][j].almostEquals(
                            dirOffsetArray[i][j],
                            self.getTable().getDirOffsetArrayEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._freqOffsetArray) != len(freqOffsetArray):
            return False
        for indx in range(len(freqOffsetArray)):

            # freqOffsetArray is a list of Frequency, compare using the almostEquals method.
            if not self._freqOffsetArray[indx].almostEquals(
                freqOffsetArray[indx], self.getTable().getFreqOffsetArrayEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._stepDurationArray) != len(stepDurationArray):
            return False
        for indx in range(len(stepDurationArray)):

            # stepDurationArray is a list of Interval, compare using equals method.
            if not self._stepDurationArray[indx].equals(stepDurationArray[indx]):
                return False

        return True


# initialize the dictionary that maps fields to init methods
SwitchCycleRow.initFromBinMethods()
