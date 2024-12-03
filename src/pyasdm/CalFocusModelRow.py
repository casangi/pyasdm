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
# File CalFocusModelRow.py
#

import pyasdm.CalFocusModelTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.PolarizationType import PolarizationType


from pyasdm.enumerations.AntennaMake import AntennaMake


from xml.dom import minidom

import copy


class CalFocusModelRow:
    """
    The CalFocusModelRow class is a row of a CalFocusModelTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalFocusModelRow.
        When row is None, create an empty row attached to table, which must be a CalFocusModelTable.
        When row is given, copy those values in to the new row. The row argument must be a CalFocusModelRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalFocusModelTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._receiverBand = ReceiverBand.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._polarizationType = PolarizationType.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._antennaMake = AntennaMake.from_int(0)

        if row is not None:
            if not isinstance(row, CalFocusModelRow):
                raise ValueError("row must be a MainRow")

            self._antennaName = row._antennaName

            # We force the attribute of the result to be not None
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            # We force the attribute of the result to be not None
            if row._polarizationType is None:
                self._polarizationType = PolarizationType.from_int(0)
            else:
                self._polarizationType = PolarizationType(row._polarizationType)

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            # We force the attribute of the result to be not None
            if row._antennaMake is None:
                self._antennaMake = AntennaMake.from_int(0)
            else:
                self._antennaMake = AntennaMake(row._antennaMake)

            self._numCoeff = row._numCoeff

            self._numSourceObs = row._numSourceObs

            # coeffName is a  list , make a deep copy
            self._coeffName = copy.deepcopy(row._coeffName)

            # coeffFormula is a  list , make a deep copy
            self._coeffFormula = copy.deepcopy(row._coeffFormula)

            # coeffValue is a  list , make a deep copy
            self._coeffValue = copy.deepcopy(row._coeffValue)

            # coeffError is a  list , make a deep copy
            self._coeffError = copy.deepcopy(row._coeffError)

            # coeffFixed is a  list , make a deep copy
            self._coeffFixed = copy.deepcopy(row._coeffFixed)

            self._focusModel = row._focusModel

            # focusRMS is a  list , make a deep copy
            self._focusRMS = copy.deepcopy(row._focusRMS)

            self._reducedChiSquared = row._reducedChiSquared

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
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.valueToXML(
            "polarizationType", PolarizationType.name(self._polarizationType)
        )

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.valueToXML("antennaMake", AntennaMake.name(self._antennaMake))

        result += Parser.valueToXML("numCoeff", self._numCoeff)

        result += Parser.valueToXML("numSourceObs", self._numSourceObs)

        result += Parser.listValueToXML("coeffName", self._coeffName)

        result += Parser.listValueToXML("coeffFormula", self._coeffFormula)

        result += Parser.listValueToXML("coeffValue", self._coeffValue)

        result += Parser.listValueToXML("coeffError", self._coeffError)

        result += Parser.listValueToXML("coeffFixed", self._coeffFixed)

        result += Parser.valueToXML("focusModel", self._focusModel)

        result += Parser.listExtendedValueToXML("focusRMS", self._focusRMS)

        result += Parser.valueToXML("reducedChiSquared", self._reducedChiSquared)

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
                "xmlrow is not a string or a minidom.Element", "CalFocusModelTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalFocusModelTable")

        # intrinsic attribute values

        antennaNameNode = rowdom.getElementsByTagName("antennaName")[0]

        self._antennaName = str(antennaNameNode.firstChild.data)

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data
        )

        polarizationTypeNode = rowdom.getElementsByTagName("polarizationType")[0]

        self._polarizationType = PolarizationType.newPolarizationType(
            polarizationTypeNode.firstChild.data
        )

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data)

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data)

        antennaMakeNode = rowdom.getElementsByTagName("antennaMake")[0]

        self._antennaMake = AntennaMake.newAntennaMake(antennaMakeNode.firstChild.data)

        numCoeffNode = rowdom.getElementsByTagName("numCoeff")[0]

        self._numCoeff = int(numCoeffNode.firstChild.data)

        numSourceObsNode = rowdom.getElementsByTagName("numSourceObs")[0]

        self._numSourceObs = int(numSourceObsNode.firstChild.data)

        coeffNameNode = rowdom.getElementsByTagName("coeffName")[0]

        coeffNameStr = coeffNameNode.firstChild.data
        self._coeffName = Parser.stringListToLists(coeffNameStr, str, "CalFocusModel")

        coeffFormulaNode = rowdom.getElementsByTagName("coeffFormula")[0]

        coeffFormulaStr = coeffFormulaNode.firstChild.data
        self._coeffFormula = Parser.stringListToLists(
            coeffFormulaStr, str, "CalFocusModel"
        )

        coeffValueNode = rowdom.getElementsByTagName("coeffValue")[0]

        coeffValueStr = coeffValueNode.firstChild.data
        self._coeffValue = Parser.stringListToLists(
            coeffValueStr, float, "CalFocusModel"
        )

        coeffErrorNode = rowdom.getElementsByTagName("coeffError")[0]

        coeffErrorStr = coeffErrorNode.firstChild.data
        self._coeffError = Parser.stringListToLists(
            coeffErrorStr, float, "CalFocusModel"
        )

        coeffFixedNode = rowdom.getElementsByTagName("coeffFixed")[0]

        coeffFixedStr = coeffFixedNode.firstChild.data
        self._coeffFixed = Parser.stringListToLists(
            coeffFixedStr, bool, "CalFocusModel"
        )

        focusModelNode = rowdom.getElementsByTagName("focusModel")[0]

        self._focusModel = str(focusModelNode.firstChild.data)

        focusRMSNode = rowdom.getElementsByTagName("focusRMS")[0]

        focusRMSStr = focusRMSNode.firstChild.data
        self._focusRMS = Parser.stringListToLists(focusRMSStr, Length, "CalFocusModel")

        reducedChiSquaredNode = rowdom.getElementsByTagName("reducedChiSquared")[0]

        self._reducedChiSquared = double(reducedChiSquaredNode.firstChild.data)

        # extrinsic attribute values

        calDataIdNode = rowdom.getElementsByTagName("calDataId")[0]

        self._calDataId = Tag(calDataIdNode.firstChild.data)

        calReductionIdNode = rowdom.getElementsByTagName("calReductionId")[0]

        self._calReductionId = Tag(calReductionIdNode.firstChild.data)

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

    # ===> Attribute polarizationType

    _polarizationType = PolarizationType.from_int(0)

    def getPolarizationType(self):
        """
        Get polarizationType.
        return polarizationType as PolarizationType
        """

        return self._polarizationType

    def setPolarizationType(self, polarizationType):
        """
        Set polarizationType with the specified PolarizationType value.
        polarizationType The PolarizationType value to which polarizationType is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the polarizationType field, which is part of the key, after this row has been added to this table."
            )

        self._polarizationType = PolarizationType(polarizationType)

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

    # ===> Attribute antennaMake

    _antennaMake = AntennaMake.from_int(0)

    def getAntennaMake(self):
        """
        Get antennaMake.
        return antennaMake as AntennaMake
        """

        return self._antennaMake

    def setAntennaMake(self, antennaMake):
        """
        Set antennaMake with the specified AntennaMake value.
        antennaMake The AntennaMake value to which antennaMake is to be set.


        """

        self._antennaMake = AntennaMake(antennaMake)

    # ===> Attribute numCoeff

    _numCoeff = 0

    def getNumCoeff(self):
        """
        Get numCoeff.
        return numCoeff as int
        """

        return self._numCoeff

    def setNumCoeff(self, numCoeff):
        """
        Set numCoeff with the specified int value.
        numCoeff The int value to which numCoeff is to be set.


        """

        self._numCoeff = int(numCoeff)

    # ===> Attribute numSourceObs

    _numSourceObs = 0

    def getNumSourceObs(self):
        """
        Get numSourceObs.
        return numSourceObs as int
        """

        return self._numSourceObs

    def setNumSourceObs(self, numSourceObs):
        """
        Set numSourceObs with the specified int value.
        numSourceObs The int value to which numSourceObs is to be set.


        """

        self._numSourceObs = int(numSourceObs)

    # ===> Attribute coeffName

    _coeffName = None  # this is a 1D list of str

    def getCoeffName(self):
        """
        Get coeffName.
        return coeffName as str []
        """

        return copy.deepcopy(self._coeffName)

    def setCoeffName(self, coeffName):
        """
        Set coeffName with the specified str []  value.
        coeffName The str []  value to which coeffName is to be set.


        """

        # value must be a list
        if not isinstance(coeffName, list):
            raise ValueError("The value of coeffName must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(coeffName)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of coeffName is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not Parser.checkListType(coeffName, str):
                raise ValueError(
                    "type of the first value in coeffName is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._coeffName = copy.deepcopy(coeffName)
        except Exception as exc:
            raise ValueError("Invalid coeffName : " + str(exc))

    # ===> Attribute coeffFormula

    _coeffFormula = None  # this is a 1D list of str

    def getCoeffFormula(self):
        """
        Get coeffFormula.
        return coeffFormula as str []
        """

        return copy.deepcopy(self._coeffFormula)

    def setCoeffFormula(self, coeffFormula):
        """
        Set coeffFormula with the specified str []  value.
        coeffFormula The str []  value to which coeffFormula is to be set.


        """

        # value must be a list
        if not isinstance(coeffFormula, list):
            raise ValueError("The value of coeffFormula must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(coeffFormula)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of coeffFormula is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not Parser.checkListType(coeffFormula, str):
                raise ValueError(
                    "type of the first value in coeffFormula is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._coeffFormula = copy.deepcopy(coeffFormula)
        except Exception as exc:
            raise ValueError("Invalid coeffFormula : " + str(exc))

    # ===> Attribute coeffValue

    _coeffValue = None  # this is a 1D list of float

    def getCoeffValue(self):
        """
        Get coeffValue.
        return coeffValue as float []
        """

        return copy.deepcopy(self._coeffValue)

    def setCoeffValue(self, coeffValue):
        """
        Set coeffValue with the specified float []  value.
        coeffValue The float []  value to which coeffValue is to be set.


        """

        # value must be a list
        if not isinstance(coeffValue, list):
            raise ValueError("The value of coeffValue must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(coeffValue)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of coeffValue is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(coeffValue, float):
                raise ValueError(
                    "type of the first value in coeffValue is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._coeffValue = copy.deepcopy(coeffValue)
        except Exception as exc:
            raise ValueError("Invalid coeffValue : " + str(exc))

    # ===> Attribute coeffError

    _coeffError = None  # this is a 1D list of float

    def getCoeffError(self):
        """
        Get coeffError.
        return coeffError as float []
        """

        return copy.deepcopy(self._coeffError)

    def setCoeffError(self, coeffError):
        """
        Set coeffError with the specified float []  value.
        coeffError The float []  value to which coeffError is to be set.


        """

        # value must be a list
        if not isinstance(coeffError, list):
            raise ValueError("The value of coeffError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(coeffError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of coeffError is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(coeffError, float):
                raise ValueError(
                    "type of the first value in coeffError is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._coeffError = copy.deepcopy(coeffError)
        except Exception as exc:
            raise ValueError("Invalid coeffError : " + str(exc))

    # ===> Attribute coeffFixed

    _coeffFixed = None  # this is a 1D list of bool

    def getCoeffFixed(self):
        """
        Get coeffFixed.
        return coeffFixed as bool []
        """

        return copy.deepcopy(self._coeffFixed)

    def setCoeffFixed(self, coeffFixed):
        """
        Set coeffFixed with the specified bool []  value.
        coeffFixed The bool []  value to which coeffFixed is to be set.


        """

        # value must be a list
        if not isinstance(coeffFixed, list):
            raise ValueError("The value of coeffFixed must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(coeffFixed)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of coeffFixed is not correct")

            # the type of the values in the list must be bool
            # note : this only checks the first value found
            if not Parser.checkListType(coeffFixed, bool):
                raise ValueError(
                    "type of the first value in coeffFixed is not bool as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._coeffFixed = copy.deepcopy(coeffFixed)
        except Exception as exc:
            raise ValueError("Invalid coeffFixed : " + str(exc))

    # ===> Attribute focusModel

    _focusModel = None

    def getFocusModel(self):
        """
        Get focusModel.
        return focusModel as str
        """

        return self._focusModel

    def setFocusModel(self, focusModel):
        """
        Set focusModel with the specified str value.
        focusModel The str value to which focusModel is to be set.


        """

        self._focusModel = str(focusModel)

    # ===> Attribute focusRMS

    _focusRMS = None  # this is a 1D list of Length

    def getFocusRMS(self):
        """
        Get focusRMS.
        return focusRMS as Length []
        """

        return copy.deepcopy(self._focusRMS)

    def setFocusRMS(self, focusRMS):
        """
        Set focusRMS with the specified Length []  value.
        focusRMS The Length []  value to which focusRMS is to be set.
        The value of focusRMS can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(focusRMS, list):
            raise ValueError("The value of focusRMS must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(focusRMS)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of focusRMS is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(focusRMS, Length):
                raise ValueError(
                    "type of the first value in focusRMS is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._focusRMS = copy.deepcopy(focusRMS)
        except Exception as exc:
            raise ValueError("Invalid focusRMS : " + str(exc))

    # ===> Attribute reducedChiSquared

    _reducedChiSquared = None

    def getReducedChiSquared(self):
        """
        Get reducedChiSquared.
        return reducedChiSquared as double
        """

        return self._reducedChiSquared

    def setReducedChiSquared(self, reducedChiSquared):
        """
        Set reducedChiSquared with the specified double value.
        reducedChiSquared The double value to which reducedChiSquared is to be set.


        """

        self._reducedChiSquared = double(reducedChiSquared)

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

    def getCalReductionUsingCalReductionId(self):
        """
        Returns the row in the CalReduction table having CalReduction.calReductionId == calReductionId

        """

        return (
            self._table.getContainer()
            .getCalReduction()
            .getRowByKey(self._calReductionId)
        )

    def getCalDataUsingCalDataId(self):
        """
        Returns the row in the CalData table having CalData.calDataId == calDataId

        """

        return self._table.getContainer().getCalData().getRowByKey(self._calDataId)

    # comparison methods

    def compareNoAutoInc(
        self,
        antennaName,
        receiverBand,
        polarizationType,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        antennaMake,
        numCoeff,
        numSourceObs,
        coeffName,
        coeffFormula,
        coeffValue,
        coeffError,
        coeffFixed,
        focusModel,
        focusRMS,
        reducedChiSquared,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalFocusModelRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaName is a str, compare using the == operator.
        if not (self._antennaName == antennaName):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
            return False

        # polarizationType is a PolarizationType, compare using the == operator on the getValue() output
        if not (self._polarizationType.getValue() == polarizationType.getValue()):
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

        # antennaMake is a AntennaMake, compare using the == operator on the getValue() output
        if not (self._antennaMake.getValue() == antennaMake.getValue()):
            return False

        # numCoeff is a int, compare using the == operator.
        if not (self._numCoeff == numCoeff):
            return False

        # numSourceObs is a int, compare using the == operator.
        if not (self._numSourceObs == numSourceObs):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._coeffName) != len(coeffName):
            return False
        for indx in range(len(coeffName)):

            # coeffName is a list of str, compare using == operator.
            if not (self._coeffName[indx] == coeffName[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._coeffFormula) != len(coeffFormula):
            return False
        for indx in range(len(coeffFormula)):

            # coeffFormula is a list of str, compare using == operator.
            if not (self._coeffFormula[indx] == coeffFormula[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._coeffValue) != len(coeffValue):
            return False
        for indx in range(len(coeffValue)):

            # coeffValue is a list of float, compare using == operator.
            if not (self._coeffValue[indx] == coeffValue[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._coeffError) != len(coeffError):
            return False
        for indx in range(len(coeffError)):

            # coeffError is a list of float, compare using == operator.
            if not (self._coeffError[indx] == coeffError[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._coeffFixed) != len(coeffFixed):
            return False
        for indx in range(len(coeffFixed)):

            # coeffFixed is a list of bool, compare using == operator.
            if not (self._coeffFixed[indx] == coeffFixed[indx]):
                return False

        # focusModel is a str, compare using the == operator.
        if not (self._focusModel == focusModel):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._focusRMS) != len(focusRMS):
            return False
        for indx in range(len(focusRMS)):

            # focusRMS is a list of Length, compare using the almostEquals method.
            if not self._focusRMS[indx].almostEquals(
                focusRMS[indx], self.getTable().getFocusRMSEqTolerance()
            ):
                return False

        # reducedChiSquared is a double, compare using the == operator.
        if not (self._reducedChiSquared == reducedChiSquared):
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
            otherRow.getAntennaMake(),
            otherRow.getNumCoeff(),
            otherRow.getNumSourceObs(),
            otherRow.getCoeffName(),
            otherRow.getCoeffFormula(),
            otherRow.getCoeffValue(),
            otherRow.getCoeffError(),
            otherRow.getCoeffFixed(),
            otherRow.getFocusModel(),
            otherRow.getFocusRMS(),
            otherRow.getReducedChiSquared(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        antennaMake,
        numCoeff,
        numSourceObs,
        coeffName,
        coeffFormula,
        coeffValue,
        coeffError,
        coeffFixed,
        focusModel,
        focusRMS,
        reducedChiSquared,
    ):

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # antennaMake is a AntennaMake, compare using the == operator on the getValue() output
        if not (self._antennaMake.getValue() == antennaMake.getValue()):
            return False

        # numCoeff is a int, compare using the == operator.
        if not (self._numCoeff == numCoeff):
            return False

        # numSourceObs is a int, compare using the == operator.
        if not (self._numSourceObs == numSourceObs):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._coeffName) != len(coeffName):
            return False
        for indx in range(len(coeffName)):

            # coeffName is a list of str, compare using == operator.
            if not (self._coeffName[indx] == coeffName[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._coeffFormula) != len(coeffFormula):
            return False
        for indx in range(len(coeffFormula)):

            # coeffFormula is a list of str, compare using == operator.
            if not (self._coeffFormula[indx] == coeffFormula[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._coeffValue) != len(coeffValue):
            return False
        for indx in range(len(coeffValue)):

            # coeffValue is a list of float, compare using == operator.
            if not (self._coeffValue[indx] == coeffValue[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._coeffError) != len(coeffError):
            return False
        for indx in range(len(coeffError)):

            # coeffError is a list of float, compare using == operator.
            if not (self._coeffError[indx] == coeffError[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._coeffFixed) != len(coeffFixed):
            return False
        for indx in range(len(coeffFixed)):

            # coeffFixed is a list of bool, compare using == operator.
            if not (self._coeffFixed[indx] == coeffFixed[indx]):
                return False

        # focusModel is a str, compare using the == operator.
        if not (self._focusModel == focusModel):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._focusRMS) != len(focusRMS):
            return False
        for indx in range(len(focusRMS)):

            # focusRMS is a list of Length, compare using the almostEquals method.
            if not self._focusRMS[indx].almostEquals(
                focusRMS[indx], self.getTable().getFocusRMSEqTolerance()
            ):
                return False

        # reducedChiSquared is a double, compare using the == operator.
        if not (self._reducedChiSquared == reducedChiSquared):
            return False

        return True
