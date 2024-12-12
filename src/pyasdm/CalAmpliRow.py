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
# File CalAmpliRow.py
#

import pyasdm.CalAmpliTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.AtmPhaseCorrection import AtmPhaseCorrection


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.BasebandName import BasebandName


from pyasdm.enumerations.PolarizationType import PolarizationType


from xml.dom import minidom

import copy


class CalAmpliRow:
    """
    The CalAmpliRow class is a row of a CalAmpliTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalAmpliRow.
        When row is None, create an empty row attached to table, which must be a CalAmpliTable.
        When row is given, copy those values in to the new row. The row argument must be a CalAmpliRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalAmpliTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._antennaName = None

        self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)

        self._receiverBand = ReceiverBand.from_int(0)

        self._basebandName = BasebandName.from_int(0)

        self._numReceptor = 0

        self._polarizationTypes = []  # this is a list of PolarizationType []

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._frequencyRange = []  # this is a list of Frequency []

        self._apertureEfficiency = []  # this is a list of float []

        self._apertureEfficiencyError = []  # this is a list of float []

        self._correctionValidityExists = False

        self._correctionValidity = None

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalAmpliRow):
                raise ValueError("row must be a MainRow")

            # copy constructor

            self._antennaName = row._antennaName

            # We force the attribute of the result to be not None
            if row._atmPhaseCorrection is None:
                self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)
            else:
                self._atmPhaseCorrection = AtmPhaseCorrection(row._atmPhaseCorrection)

            # We force the attribute of the result to be not None
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            # We force the attribute of the result to be not None
            if row._basebandName is None:
                self._basebandName = BasebandName.from_int(0)
            else:
                self._basebandName = BasebandName(row._basebandName)

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._numReceptor = row._numReceptor

            # polarizationTypes is a  list , make a deep copy
            self._polarizationTypes = copy.deepcopy(row._polarizationTypes)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            # frequencyRange is a  list , make a deep copy
            self._frequencyRange = copy.deepcopy(row._frequencyRange)

            # apertureEfficiency is a  list , make a deep copy
            self._apertureEfficiency = copy.deepcopy(row._apertureEfficiency)

            # apertureEfficiencyError is a  list , make a deep copy
            self._apertureEfficiencyError = copy.deepcopy(row._apertureEfficiencyError)

            # by default set systematically correctionValidity's value to something not None

            if row._correctionValidityExists:

                self._correctionValidity = row._correctionValidity

                self._correctionValidityExists = True

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

        result += Parser.valueToXML("antennaName", self._antennaName)

        result += Parser.valueToXML(
            "atmPhaseCorrection", AtmPhaseCorrection.name(self._atmPhaseCorrection)
        )

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.valueToXML(
            "basebandName", BasebandName.name(self._basebandName)
        )

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.listExtendedValueToXML("frequencyRange", self._frequencyRange)

        result += Parser.listValueToXML("apertureEfficiency", self._apertureEfficiency)

        result += Parser.listValueToXML(
            "apertureEfficiencyError", self._apertureEfficiencyError
        )

        if self._correctionValidityExists:

            result += Parser.valueToXML("correctionValidity", self._correctionValidity)

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
                "xmlrow is not a string or a minidom.Element", "CalAmpliTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalAmpliTable")

        # intrinsic attribute values

        antennaNameNode = rowdom.getElementsByTagName("antennaName")[0]

        self._antennaName = str(antennaNameNode.firstChild.data.strip())

        atmPhaseCorrectionNode = rowdom.getElementsByTagName("atmPhaseCorrection")[0]

        self._atmPhaseCorrection = AtmPhaseCorrection.newAtmPhaseCorrection(
            atmPhaseCorrectionNode.firstChild.data.strip()
        )

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data.strip()
        )

        basebandNameNode = rowdom.getElementsByTagName("basebandName")[0]

        self._basebandName = BasebandName.newBasebandName(
            basebandNameNode.firstChild.data.strip()
        )

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data.strip()
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "CalAmpli", False
        )

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        frequencyRangeNode = rowdom.getElementsByTagName("frequencyRange")[0]

        frequencyRangeStr = frequencyRangeNode.firstChild.data.strip()

        self._frequencyRange = Parser.stringListToLists(
            frequencyRangeStr, Frequency, "CalAmpli", True
        )

        apertureEfficiencyNode = rowdom.getElementsByTagName("apertureEfficiency")[0]

        apertureEfficiencyStr = apertureEfficiencyNode.firstChild.data.strip()

        self._apertureEfficiency = Parser.stringListToLists(
            apertureEfficiencyStr, float, "CalAmpli", False
        )

        apertureEfficiencyErrorNode = rowdom.getElementsByTagName(
            "apertureEfficiencyError"
        )[0]

        apertureEfficiencyErrorStr = apertureEfficiencyErrorNode.firstChild.data.strip()

        self._apertureEfficiencyError = Parser.stringListToLists(
            apertureEfficiencyErrorStr, float, "CalAmpli", False
        )

        correctionValidityNode = rowdom.getElementsByTagName("correctionValidity")
        if len(correctionValidityNode) > 0:

            self._correctionValidity = bool(
                correctionValidityNode[0].firstChild.data.strip()
            )

            self._correctionValidityExists = True

        # extrinsic attribute values

        calDataIdNode = rowdom.getElementsByTagName("calDataId")[0]

        self._calDataId = Tag(calDataIdNode.firstChild.data.strip())

        calReductionIdNode = rowdom.getElementsByTagName("calReductionId")[0]

        self._calReductionId = Tag(calReductionIdNode.firstChild.data.strip())

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

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

    # ===> Attribute atmPhaseCorrection

    _atmPhaseCorrection = AtmPhaseCorrection.from_int(0)

    def getAtmPhaseCorrection(self):
        """
        Get atmPhaseCorrection.
        return atmPhaseCorrection as AtmPhaseCorrection
        """

        return self._atmPhaseCorrection

    def setAtmPhaseCorrection(self, atmPhaseCorrection):
        """
        Set atmPhaseCorrection with the specified AtmPhaseCorrection value.
        atmPhaseCorrection The AtmPhaseCorrection value to which atmPhaseCorrection is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the atmPhaseCorrection field, which is part of the key, after this row has been added to this table."
            )

        self._atmPhaseCorrection = AtmPhaseCorrection(atmPhaseCorrection)

    # ===> Attribute receiverBand

    _receiverBand = ReceiverBand.from_int(0)

    def getReceiverBand(self):
        """
        Get receiverBand.
        return receiverBand as ReceiverBand
        """

        return self._receiverBand

    def setReceiverBand(self, receiverBand):
        """
        Set receiverBand with the specified ReceiverBand value.
        receiverBand The ReceiverBand value to which receiverBand is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the receiverBand field, which is part of the key, after this row has been added to this table."
            )

        self._receiverBand = ReceiverBand(receiverBand)

    # ===> Attribute basebandName

    _basebandName = BasebandName.from_int(0)

    def getBasebandName(self):
        """
        Get basebandName.
        return basebandName as BasebandName
        """

        return self._basebandName

    def setBasebandName(self, basebandName):
        """
        Set basebandName with the specified BasebandName value.
        basebandName The BasebandName value to which basebandName is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the basebandName field, which is part of the key, after this row has been added to this table."
            )

        self._basebandName = BasebandName(basebandName)

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

    # ===> Attribute frequencyRange

    _frequencyRange = None  # this is a 1D list of Frequency

    def getFrequencyRange(self):
        """
        Get frequencyRange.
        return frequencyRange as Frequency []
        """

        return copy.deepcopy(self._frequencyRange)

    def setFrequencyRange(self, frequencyRange):
        """
        Set frequencyRange with the specified Frequency []  value.
        frequencyRange The Frequency []  value to which frequencyRange is to be set.
        The value of frequencyRange can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(frequencyRange, list):
            raise ValueError("The value of frequencyRange must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(frequencyRange)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of frequencyRange is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(frequencyRange, Frequency):
                raise ValueError(
                    "type of the first value in frequencyRange is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._frequencyRange = copy.deepcopy(frequencyRange)
        except Exception as exc:
            raise ValueError("Invalid frequencyRange : " + str(exc))

    # ===> Attribute apertureEfficiency

    _apertureEfficiency = None  # this is a 1D list of float

    def getApertureEfficiency(self):
        """
        Get apertureEfficiency.
        return apertureEfficiency as float []
        """

        return copy.deepcopy(self._apertureEfficiency)

    def setApertureEfficiency(self, apertureEfficiency):
        """
        Set apertureEfficiency with the specified float []  value.
        apertureEfficiency The float []  value to which apertureEfficiency is to be set.


        """

        # value must be a list
        if not isinstance(apertureEfficiency, list):
            raise ValueError("The value of apertureEfficiency must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(apertureEfficiency)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of apertureEfficiency is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(apertureEfficiency, float):
                raise ValueError(
                    "type of the first value in apertureEfficiency is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._apertureEfficiency = copy.deepcopy(apertureEfficiency)
        except Exception as exc:
            raise ValueError("Invalid apertureEfficiency : " + str(exc))

    # ===> Attribute apertureEfficiencyError

    _apertureEfficiencyError = None  # this is a 1D list of float

    def getApertureEfficiencyError(self):
        """
        Get apertureEfficiencyError.
        return apertureEfficiencyError as float []
        """

        return copy.deepcopy(self._apertureEfficiencyError)

    def setApertureEfficiencyError(self, apertureEfficiencyError):
        """
        Set apertureEfficiencyError with the specified float []  value.
        apertureEfficiencyError The float []  value to which apertureEfficiencyError is to be set.


        """

        # value must be a list
        if not isinstance(apertureEfficiencyError, list):
            raise ValueError("The value of apertureEfficiencyError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(apertureEfficiencyError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of apertureEfficiencyError is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(apertureEfficiencyError, float):
                raise ValueError(
                    "type of the first value in apertureEfficiencyError is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._apertureEfficiencyError = copy.deepcopy(apertureEfficiencyError)
        except Exception as exc:
            raise ValueError("Invalid apertureEfficiencyError : " + str(exc))

    # ===> Attribute correctionValidity, which is optional
    _correctionValidityExists = False

    _correctionValidity = None

    def isCorrectionValidityExists(self):
        """
        The attribute correctionValidity is optional. Return True if this attribute exists.
        return True if and only if the correctionValidity attribute exists.
        """
        return self._correctionValidityExists

    def getCorrectionValidity(self):
        """
        Get correctionValidity, which is optional.
        return correctionValidity as bool
        raises ValueError If correctionValidity does not exist.
        """
        if not self._correctionValidityExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + correctionValidity
                + " attribute in table CalAmpli does not exist!"
            )

        return self._correctionValidity

    def setCorrectionValidity(self, correctionValidity):
        """
        Set correctionValidity with the specified bool value.
        correctionValidity The bool value to which correctionValidity is to be set.


        """

        self._correctionValidity = bool(correctionValidity)

        self._correctionValidityExists = True

    def clearCorrectionValidity(self):
        """
        Mark correctionValidity, which is an optional field, as non-existent.
        """
        self._correctionValidityExists = False

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
        atmPhaseCorrection,
        receiverBand,
        basebandName,
        calDataId,
        calReductionId,
        numReceptor,
        polarizationTypes,
        startValidTime,
        endValidTime,
        frequencyRange,
        apertureEfficiency,
        apertureEfficiencyError,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalAmpliRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaName is a str, compare using the == operator.
        if not (self._antennaName == antennaName):
            return False

        # atmPhaseCorrection is a AtmPhaseCorrection, compare using the == operator on the getValue() output
        if not (self._atmPhaseCorrection.getValue() == atmPhaseCorrection.getValue()):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
            return False

        # basebandName is a BasebandName, compare using the == operator on the getValue() output
        if not (self._basebandName.getValue() == basebandName.getValue()):
            return False

        # calDataId is a Tag, compare using the equals method.
        if not self._calDataId.equals(calDataId):
            return False

        # calReductionId is a Tag, compare using the equals method.
        if not self._calReductionId.equals(calReductionId):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationTypes) != len(polarizationTypes):
            return False
        for indx in range(len(polarizationTypes)):

            # polarizationTypes is a list of PolarizationType, compare using == operator.
            if not (self._polarizationTypes[indx] == polarizationTypes[indx]):
                return False

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._frequencyRange) != len(frequencyRange):
            return False
        for indx in range(len(frequencyRange)):

            # frequencyRange is a list of Frequency, compare using the almostEquals method.
            if not self._frequencyRange[indx].almostEquals(
                frequencyRange[indx], self.getTable().getFrequencyRangeEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._apertureEfficiency) != len(apertureEfficiency):
            return False
        for indx in range(len(apertureEfficiency)):

            # apertureEfficiency is a list of float, compare using == operator.
            if not (self._apertureEfficiency[indx] == apertureEfficiency[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._apertureEfficiencyError) != len(apertureEfficiencyError):
            return False
        for indx in range(len(apertureEfficiencyError)):

            # apertureEfficiencyError is a list of float, compare using == operator.
            if not (
                self._apertureEfficiencyError[indx] == apertureEfficiencyError[indx]
            ):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumReceptor(),
            otherRow.getPolarizationTypes(),
            otherRow.getStartValidTime(),
            otherRow.getEndValidTime(),
            otherRow.getFrequencyRange(),
            otherRow.getApertureEfficiency(),
            otherRow.getApertureEfficiencyError(),
        )

    def compareRequiredValue(
        self,
        numReceptor,
        polarizationTypes,
        startValidTime,
        endValidTime,
        frequencyRange,
        apertureEfficiency,
        apertureEfficiencyError,
    ):

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationTypes) != len(polarizationTypes):
            return False
        for indx in range(len(polarizationTypes)):

            # polarizationTypes is a list of PolarizationType, compare using == operator.
            if not (self._polarizationTypes[indx] == polarizationTypes[indx]):
                return False

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._frequencyRange) != len(frequencyRange):
            return False
        for indx in range(len(frequencyRange)):

            # frequencyRange is a list of Frequency, compare using the almostEquals method.
            if not self._frequencyRange[indx].almostEquals(
                frequencyRange[indx], self.getTable().getFrequencyRangeEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._apertureEfficiency) != len(apertureEfficiency):
            return False
        for indx in range(len(apertureEfficiency)):

            # apertureEfficiency is a list of float, compare using == operator.
            if not (self._apertureEfficiency[indx] == apertureEfficiency[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._apertureEfficiencyError) != len(apertureEfficiencyError):
            return False
        for indx in range(len(apertureEfficiencyError)):

            # apertureEfficiencyError is a list of float, compare using == operator.
            if not (
                self._apertureEfficiencyError[indx] == apertureEfficiencyError[indx]
            ):
                return False

        return True
