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
# File PointingModelRow.py
#

import pyasdm.PointingModelTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.PolarizationType import PolarizationType


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from xml.dom import minidom

import copy


class PointingModelRow:
    """
    The PointingModelRow class is a row of a PointingModelTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a PointingModelRow.
        When row is None, create an empty row attached to table, which must be a PointingModelTable.
        When row is given, copy those values in to the new row. The row argument must be a PointingModelRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.PointingModelTable):
            raise ValueError("table must be a PointingModelTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._pointingModelId = 0

        self._numCoeff = 0

        self._coeffName = []  # this is a list of str []

        self._coeffVal = []  # this is a list of float []

        self._polarizationType = PolarizationType.from_int(0)

        self._receiverBand = ReceiverBand.from_int(0)

        self._assocNature = None

        self._coeffFormulaExists = False

        self._coeffFormula = []  # this is a list of str []

        # extrinsic attributes

        self._antennaId = Tag()

        self._assocPointingModelId = 0

        if row is not None:
            if not isinstance(row, PointingModelRow):
                raise ValueError("row must be a PointingModelRow")

            # copy constructor

            self._antennaId = Tag(row._antennaId)

            self._pointingModelId = row._pointingModelId

            self._numCoeff = row._numCoeff

            # coeffName is a  list , make a deep copy
            self._coeffName = copy.deepcopy(row._coeffName)

            # coeffVal is a  list , make a deep copy
            self._coeffVal = copy.deepcopy(row._coeffVal)

            # We force the attribute of the result to be not None
            if row._polarizationType is None:
                self._polarizationType = PolarizationType.from_int(0)
            else:
                self._polarizationType = PolarizationType(row._polarizationType)

            # We force the attribute of the result to be not None
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            self._assocNature = row._assocNature

            self._assocPointingModelId = row._assocPointingModelId

            # by default set systematically coeffFormula's value to something not None

            if row._coeffFormulaExists:

                # coeffFormula is a list, make a deep copy
                self._coeffFormula = copy.deepcopy(row._coeffFormula)

                self._coeffFormulaExists = True

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

        result += Parser.valueToXML("pointingModelId", self._pointingModelId)

        result += Parser.valueToXML("numCoeff", self._numCoeff)

        result += Parser.listValueToXML("coeffName", self._coeffName)

        result += Parser.listValueToXML("coeffVal", self._coeffVal)

        result += Parser.valueToXML(
            "polarizationType", PolarizationType.name(self._polarizationType)
        )

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.valueToXML("assocNature", self._assocNature)

        if self._coeffFormulaExists:

            result += Parser.listValueToXML("coeffFormula", self._coeffFormula)

        # extrinsic attributes

        result += Parser.extendedValueToXML("antennaId", self._antennaId)

        result += Parser.valueToXML("assocPointingModelId", self._assocPointingModelId)

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
                "xmlrow is not a string or a minidom.Element", "PointingModelTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "PointingModelTable")

        # intrinsic attribute values

        pointingModelIdNode = rowdom.getElementsByTagName("pointingModelId")[0]

        self._pointingModelId = int(pointingModelIdNode.firstChild.data.strip())

        numCoeffNode = rowdom.getElementsByTagName("numCoeff")[0]

        self._numCoeff = int(numCoeffNode.firstChild.data.strip())

        coeffNameNode = rowdom.getElementsByTagName("coeffName")[0]

        coeffNameStr = coeffNameNode.firstChild.data.strip()

        self._coeffName = Parser.stringListToLists(
            coeffNameStr, str, "PointingModel", False
        )

        coeffValNode = rowdom.getElementsByTagName("coeffVal")[0]

        coeffValStr = coeffValNode.firstChild.data.strip()

        self._coeffVal = Parser.stringListToLists(
            coeffValStr, float, "PointingModel", False
        )

        polarizationTypeNode = rowdom.getElementsByTagName("polarizationType")[0]

        self._polarizationType = PolarizationType.newPolarizationType(
            polarizationTypeNode.firstChild.data.strip()
        )

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data.strip()
        )

        assocNatureNode = rowdom.getElementsByTagName("assocNature")[0]

        self._assocNature = str(assocNatureNode.firstChild.data.strip())

        coeffFormulaNode = rowdom.getElementsByTagName("coeffFormula")
        if len(coeffFormulaNode) > 0:

            coeffFormulaStr = coeffFormulaNode[0].firstChild.data.strip()

            self._coeffFormula = Parser.stringListToLists(
                coeffFormulaStr, str, "PointingModel", False
            )

            self._coeffFormulaExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        self._antennaId = Tag(antennaIdNode.firstChild.data.strip())

        assocPointingModelIdNode = rowdom.getElementsByTagName("assocPointingModelId")[
            0
        ]

        self._assocPointingModelId = int(
            assocPointingModelIdNode.firstChild.data.strip()
        )

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._antennaId.toBin(eos)

        eos.writeInt(self._pointingModelId)

        eos.writeInt(self._numCoeff)

        eos.writeInt(len(self._coeffName))
        for i in range(len(self._coeffName)):

            eos.writeStr(self._coeffName[i])

        eos.writeInt(len(self._coeffVal))
        for i in range(len(self._coeffVal)):

            eos.writeFloat(self._coeffVal[i])

        eos.writeString(str(self._polarizationType))

        eos.writeString(str(self._receiverBand))

        eos.writeStr(self._assocNature)

        eos.writeInt(self._assocPointingModelId)

        eos.writeBool(self._coeffFormulaExists)
        if self._coeffFormulaExists:

            eos.writeInt(len(self._coeffFormula))
            for i in range(len(self._coeffFormula)):

                eos.writeStr(self._coeffFormula[i])

    @staticmethod
    def antennaIdFromBin(row, eis):
        """
        Set the antennaId in row from the EndianInput (eis) instance.
        """

        row._antennaId = Tag.fromBin(eis)

    @staticmethod
    def pointingModelIdFromBin(row, eis):
        """
        Set the pointingModelId in row from the EndianInput (eis) instance.
        """

        row._pointingModelId = eis.readInt()

    @staticmethod
    def numCoeffFromBin(row, eis):
        """
        Set the numCoeff in row from the EndianInput (eis) instance.
        """

        row._numCoeff = eis.readInt()

    @staticmethod
    def coeffNameFromBin(row, eis):
        """
        Set the coeffName in row from the EndianInput (eis) instance.
        """

        coeffNameDim1 = eis.readInt()
        thisList = []
        for i in range(coeffNameDim1):
            thisValue = eis.readStr()
            thisList.append(thisValue)
        row._coeffName = thisList

    @staticmethod
    def coeffValFromBin(row, eis):
        """
        Set the coeffVal in row from the EndianInput (eis) instance.
        """

        coeffValDim1 = eis.readInt()
        thisList = []
        for i in range(coeffValDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._coeffVal = thisList

    @staticmethod
    def polarizationTypeFromBin(row, eis):
        """
        Set the polarizationType in row from the EndianInput (eis) instance.
        """

        row._polarizationType = PolarizationType.literal(eis.readString())

    @staticmethod
    def receiverBandFromBin(row, eis):
        """
        Set the receiverBand in row from the EndianInput (eis) instance.
        """

        row._receiverBand = ReceiverBand.literal(eis.readString())

    @staticmethod
    def assocNatureFromBin(row, eis):
        """
        Set the assocNature in row from the EndianInput (eis) instance.
        """

        row._assocNature = eis.readStr()

    @staticmethod
    def assocPointingModelIdFromBin(row, eis):
        """
        Set the assocPointingModelId in row from the EndianInput (eis) instance.
        """

        row._assocPointingModelId = eis.readInt()

    @staticmethod
    def coeffFormulaFromBin(row, eis):
        """
        Set the optional coeffFormula in row from the EndianInput (eis) instance.
        """
        row._coeffFormulaExists = eis.readBool()
        if row._coeffFormulaExists:

            coeffFormulaDim1 = eis.readInt()
            thisList = []
            for i in range(coeffFormulaDim1):
                thisValue = eis.readStr()
                thisList.append(thisValue)
            row._coeffFormula = thisList

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaId"] = PointingModelRow.antennaIdFromBin
        _fromBinMethods["pointingModelId"] = PointingModelRow.pointingModelIdFromBin
        _fromBinMethods["numCoeff"] = PointingModelRow.numCoeffFromBin
        _fromBinMethods["coeffName"] = PointingModelRow.coeffNameFromBin
        _fromBinMethods["coeffVal"] = PointingModelRow.coeffValFromBin
        _fromBinMethods["polarizationType"] = PointingModelRow.polarizationTypeFromBin
        _fromBinMethods["receiverBand"] = PointingModelRow.receiverBandFromBin
        _fromBinMethods["assocNature"] = PointingModelRow.assocNatureFromBin
        _fromBinMethods["assocPointingModelId"] = (
            PointingModelRow.assocPointingModelIdFromBin
        )

        _fromBinMethods["coeffFormula"] = PointingModelRow.coeffFormulaFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = PointingModelRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " PointingModel",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

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


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the pointingModelId field, which is part of the key, after this row has been added to this table."
            )

        self._pointingModelId = int(pointingModelId)

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
            listDims = pyasdm.utils.getListDims(coeffName)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of coeffName is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(coeffName, str):
                raise ValueError(
                    "type of the first value in coeffName is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._coeffName = copy.deepcopy(coeffName)
        except Exception as exc:
            raise ValueError("Invalid coeffName : " + str(exc))

    # ===> Attribute coeffVal

    _coeffVal = None  # this is a 1D list of float

    def getCoeffVal(self):
        """
        Get coeffVal.
        return coeffVal as float []
        """

        return copy.deepcopy(self._coeffVal)

    def setCoeffVal(self, coeffVal):
        """
        Set coeffVal with the specified float []  value.
        coeffVal The float []  value to which coeffVal is to be set.


        """

        # value must be a list
        if not isinstance(coeffVal, list):
            raise ValueError("The value of coeffVal must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(coeffVal)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of coeffVal is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(coeffVal, float):
                raise ValueError(
                    "type of the first value in coeffVal is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._coeffVal = copy.deepcopy(coeffVal)
        except Exception as exc:
            raise ValueError("Invalid coeffVal : " + str(exc))

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


        """

        self._polarizationType = PolarizationType(polarizationType)

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


        """

        self._receiverBand = ReceiverBand(receiverBand)

    # ===> Attribute assocNature

    _assocNature = None

    def getAssocNature(self):
        """
        Get assocNature.
        return assocNature as str
        """

        return self._assocNature

    def setAssocNature(self, assocNature):
        """
        Set assocNature with the specified str value.
        assocNature The str value to which assocNature is to be set.


        """

        self._assocNature = str(assocNature)

    # ===> Attribute coeffFormula, which is optional
    _coeffFormulaExists = False

    _coeffFormula = None  # this is a 1D list of str

    def isCoeffFormulaExists(self):
        """
        The attribute coeffFormula is optional. Return True if this attribute exists.
        return True if and only if the coeffFormula attribute exists.
        """
        return self._coeffFormulaExists

    def getCoeffFormula(self):
        """
        Get coeffFormula, which is optional.
        return coeffFormula as str []
        raises ValueError If coeffFormula does not exist.
        """
        if not self._coeffFormulaExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + coeffFormula
                + " attribute in table PointingModel does not exist!"
            )

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
            listDims = pyasdm.utils.getListDims(coeffFormula)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of coeffFormula is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(coeffFormula, str):
                raise ValueError(
                    "type of the first value in coeffFormula is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._coeffFormula = copy.deepcopy(coeffFormula)
        except Exception as exc:
            raise ValueError("Invalid coeffFormula : " + str(exc))

        self._coeffFormulaExists = True

    def clearCoeffFormula(self):
        """
        Mark coeffFormula, which is an optional field, as non-existent.
        """
        self._coeffFormulaExists = False

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

    # ===> Attribute assocPointingModelId

    _assocPointingModelId = 0

    def getAssocPointingModelId(self):
        """
        Get assocPointingModelId.
        return assocPointingModelId as int
        """

        return self._assocPointingModelId

    def setAssocPointingModelId(self, assocPointingModelId):
        """
        Set assocPointingModelId with the specified int value.
        assocPointingModelId The int value to which assocPointingModelId is to be set.


        """

        self._assocPointingModelId = int(assocPointingModelId)

    # Links

    # ===> Slice link from a row of PointingModel table to a collection of row of PointingModel table.
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
        numCoeff,
        coeffName,
        coeffVal,
        polarizationType,
        receiverBand,
        assocNature,
        assocPointingModelId,
    ):
        """
        Compare each attribute except the autoincrementable one of this PointingModelRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaId is a Tag, compare using the equals method.
        if not self._antennaId.equals(antennaId):
            return False

        # numCoeff is a int, compare using the == operator.
        if not (self._numCoeff == numCoeff):
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
        if len(self._coeffVal) != len(coeffVal):
            return False
        for indx in range(len(coeffVal)):

            # coeffVal is a list of float, compare using == operator.
            if not (self._coeffVal[indx] == coeffVal[indx]):
                return False

        # polarizationType is a PolarizationType, compare using the == operator on the getValue() output
        if not (self._polarizationType.getValue() == polarizationType.getValue()):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
            return False

        # assocNature is a str, compare using the == operator.
        if not (self._assocNature == assocNature):
            return False

        # assocPointingModelId is a int, compare using the == operator.
        if not (self._assocPointingModelId == assocPointingModelId):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumCoeff(),
            otherRow.getCoeffName(),
            otherRow.getCoeffVal(),
            otherRow.getPolarizationType(),
            otherRow.getReceiverBand(),
            otherRow.getAssocNature(),
            otherRow.getAssocPointingModelId(),
        )

    def compareRequiredValue(
        self,
        numCoeff,
        coeffName,
        coeffVal,
        polarizationType,
        receiverBand,
        assocNature,
        assocPointingModelId,
    ):

        # numCoeff is a int, compare using the == operator.
        if not (self._numCoeff == numCoeff):
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
        if len(self._coeffVal) != len(coeffVal):
            return False
        for indx in range(len(coeffVal)):

            # coeffVal is a list of float, compare using == operator.
            if not (self._coeffVal[indx] == coeffVal[indx]):
                return False

        # polarizationType is a PolarizationType, compare using the == operator on the getValue() output
        if not (self._polarizationType.getValue() == polarizationType.getValue()):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
            return False

        # assocNature is a str, compare using the == operator.
        if not (self._assocNature == assocNature):
            return False

        # assocPointingModelId is a int, compare using the == operator.
        if not (self._assocPointingModelId == assocPointingModelId):
            return False

        return True


# initialize the dictionary that maps fields to init methods
PointingModelRow.initFromBinMethods()
