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

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


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

    # utility function to safely extract the stripped text of the first child of
    # an XML node, returns an empty string if the node doesn't have any data there
    @staticmethod
    def _getXMLNodeChildText(xmlNode):
        """Returns the stripped text of the first child of xmlNode if it exists, otherwise an empty string"""
        result = ""
        if xmlNode and xmlNode.firstChild and xmlNode.firstChild.data:
            result = xmlNode.firstChild.data.strip()
        return result

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalFocusModelRow.
        When row is None, create an empty row attached to table, which must be a CalFocusModelTable.
        When row is given, copy those values in to the new row. The row argument must be a CalFocusModelRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalFocusModelTable):
            raise ValueError("table must be a CalFocusModelTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._antennaName = None

        self._receiverBand = ReceiverBand.from_int(0)

        self._polarizationType = PolarizationType.from_int(0)

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._antennaMake = AntennaMake.from_int(0)

        self._numCoeff = 0

        self._numSourceObs = 0

        self._coeffName = []  # this is a list of str []

        self._coeffFormula = []  # this is a list of str []

        self._coeffValue = []  # this is a list of float []  saved as single precision

        self._coeffError = []  # this is a list of float []  saved as single precision

        self._coeffFixed = []  # this is a list of bool []

        self._focusModel = None

        self._focusRMS = []  # this is a list of Length []

        self._reducedChiSquared = None

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalFocusModelRow):
                raise ValueError("row must be a CalFocusModelRow")

            # copy constructor

            self._antennaName = row._antennaName

            # We force the attribute of the result to be not None.
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            # We force the attribute of the result to be not None.
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

        result += "  <row>"

        # intrinsic attributes

        result += "\n   "

        result += Parser.valueToXML("antennaName", self._antennaName)

        result += "\n   "

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += "\n   "

        result += Parser.valueToXML(
            "polarizationType", PolarizationType.name(self._polarizationType)
        )

        result += "\n   "

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += "\n   "

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += "\n   "

        result += Parser.valueToXML("antennaMake", AntennaMake.name(self._antennaMake))

        result += "\n   "

        result += Parser.valueToXML("numCoeff", self._numCoeff)

        result += "\n   "

        result += Parser.valueToXML("numSourceObs", self._numSourceObs)

        result += "\n   "

        result += Parser.listValueToXML("coeffName", self._coeffName)

        result += "\n   "

        result += Parser.listValueToXML("coeffFormula", self._coeffFormula)

        result += "\n   "

        result += Parser.floatListValueToXML("coeffValue", self._coeffValue)

        result += "\n   "

        result += Parser.floatListValueToXML("coeffError", self._coeffError)

        result += "\n   "

        result += Parser.listValueToXML("coeffFixed", self._coeffFixed)

        result += "\n   "

        result += Parser.valueToXML("focusModel", self._focusModel)

        result += "\n   "

        result += Parser.listExtendedValueToXML("focusRMS", self._focusRMS)

        result += "\n   "

        result += Parser.doubleValueToXML("reducedChiSquared", self._reducedChiSquared)

        # extrinsic attributes

        result += "\n   "

        result += Parser.extendedValueToXML("calDataId", self._calDataId)

        result += "\n   "

        result += Parser.extendedValueToXML("calReductionId", self._calReductionId)

        # links, if any

        result += "</row>"
        return result

    @staticmethod
    def _getFirstNodeByTagName(rowdom, tagname, required):
        """
        return the first node in rowdom of the elements using tagname.

        If tagname is a required field (required=True) then a
        ConversionException is raised if that tagname is not present.
        Otherwise a None is returned if the tagname is not present.
        """
        result = None
        elementNodes = rowdom.getElementsByTagName(tagname)
        if len(elementNodes) > 0:
            result = elementNodes[0]
        else:
            if required:
                raise ConversionException(
                    f"missing required field '{tagname}' in at least one row",
                    "CalFocusModelTable",
                )
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

        antennaNameNode = self._getFirstNodeByTagName(rowdom, "antennaName", True)

        self._antennaName = str(self._getXMLNodeChildText(antennaNameNode))

        receiverBandNode = self._getFirstNodeByTagName(rowdom, "receiverBand", True)

        self._receiverBand = ReceiverBand.newReceiverBand(
            self._getXMLNodeChildText(receiverBandNode)
        )

        polarizationTypeNode = self._getFirstNodeByTagName(
            rowdom, "polarizationType", True
        )

        self._polarizationType = PolarizationType.newPolarizationType(
            self._getXMLNodeChildText(polarizationTypeNode)
        )

        startValidTimeNode = self._getFirstNodeByTagName(rowdom, "startValidTime", True)

        self._startValidTime = ArrayTime(self._getXMLNodeChildText(startValidTimeNode))

        endValidTimeNode = self._getFirstNodeByTagName(rowdom, "endValidTime", True)

        self._endValidTime = ArrayTime(self._getXMLNodeChildText(endValidTimeNode))

        antennaMakeNode = self._getFirstNodeByTagName(rowdom, "antennaMake", True)

        self._antennaMake = AntennaMake.newAntennaMake(
            self._getXMLNodeChildText(antennaMakeNode)
        )

        numCoeffNode = self._getFirstNodeByTagName(rowdom, "numCoeff", True)

        self._numCoeff = int(self._getXMLNodeChildText(numCoeffNode))

        numSourceObsNode = self._getFirstNodeByTagName(rowdom, "numSourceObs", True)

        self._numSourceObs = int(self._getXMLNodeChildText(numSourceObsNode))

        coeffNameNode = self._getFirstNodeByTagName(rowdom, "coeffName", True)

        coeffNameStr = self._getXMLNodeChildText(coeffNameNode)

        self._coeffName = Parser.stringListToLists(
            coeffNameStr, str, "CalFocusModel", False
        )

        coeffFormulaNode = self._getFirstNodeByTagName(rowdom, "coeffFormula", True)

        coeffFormulaStr = self._getXMLNodeChildText(coeffFormulaNode)

        self._coeffFormula = Parser.stringListToLists(
            coeffFormulaStr, str, "CalFocusModel", False
        )

        coeffValueNode = self._getFirstNodeByTagName(rowdom, "coeffValue", True)

        coeffValueStr = self._getXMLNodeChildText(coeffValueNode)

        self._coeffValue = Parser.stringListToLists(
            coeffValueStr, float, "CalFocusModel", False
        )

        coeffErrorNode = self._getFirstNodeByTagName(rowdom, "coeffError", True)

        coeffErrorStr = self._getXMLNodeChildText(coeffErrorNode)

        self._coeffError = Parser.stringListToLists(
            coeffErrorStr, float, "CalFocusModel", False
        )

        coeffFixedNode = self._getFirstNodeByTagName(rowdom, "coeffFixed", True)

        coeffFixedStr = self._getXMLNodeChildText(coeffFixedNode)

        self._coeffFixed = Parser.stringListToLists(
            coeffFixedStr, bool, "CalFocusModel", False
        )

        focusModelNode = self._getFirstNodeByTagName(rowdom, "focusModel", True)

        self._focusModel = str(self._getXMLNodeChildText(focusModelNode))

        focusRMSNode = self._getFirstNodeByTagName(rowdom, "focusRMS", True)

        focusRMSStr = self._getXMLNodeChildText(focusRMSNode)

        self._focusRMS = Parser.stringListToLists(
            focusRMSStr, Length, "CalFocusModel", True
        )

        reducedChiSquaredNode = self._getFirstNodeByTagName(
            rowdom, "reducedChiSquared", True
        )

        self._reducedChiSquared = float(
            self._getXMLNodeChildText(reducedChiSquaredNode)
        )

        # extrinsic attribute values

        calDataIdNode = self._getFirstNodeByTagName(rowdom, "calDataId", True)

        self._calDataId = Tag(self._getXMLNodeChildText(calDataIdNode))

        calReductionIdNode = self._getFirstNodeByTagName(rowdom, "calReductionId", True)

        self._calReductionId = Tag(self._getXMLNodeChildText(calReductionIdNode))

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        eos.writeStr(self._antennaName)

        eos.writeString(str(self._receiverBand))

        eos.writeString(str(self._polarizationType))

        self._calDataId.toBin(eos)

        self._calReductionId.toBin(eos)

        self._startValidTime.toBin(eos)

        self._endValidTime.toBin(eos)

        eos.writeString(str(self._antennaMake))

        eos.writeInt(self._numCoeff)

        eos.writeInt(self._numSourceObs)

        eos.writeInt(len(self._coeffName))
        for i in range(len(self._coeffName)):

            eos.writeStr(self._coeffName[i])

        eos.writeInt(len(self._coeffFormula))
        for i in range(len(self._coeffFormula)):

            eos.writeStr(self._coeffFormula[i])

        eos.writeInt(len(self._coeffValue))
        for i in range(len(self._coeffValue)):

            eos.writeFloat(self._coeffValue[i])

        eos.writeInt(len(self._coeffError))
        for i in range(len(self._coeffError)):

            eos.writeFloat(self._coeffError[i])

        eos.writeInt(len(self._coeffFixed))
        for i in range(len(self._coeffFixed)):

            eos.writeBool(self._coeffFixed[i])

        eos.writeStr(self._focusModel)

        Length.listToBin(self._focusRMS, eos)

        eos.writeDouble(self._reducedChiSquared)

    @staticmethod
    def antennaNameFromBin(row, eis):
        """
        Set the antennaName in row from the EndianInput (eis) instance.
        """

        row._antennaName = eis.readStr()

    @staticmethod
    def receiverBandFromBin(row, eis):
        """
        Set the receiverBand in row from the EndianInput (eis) instance.
        """

        row._receiverBand = ReceiverBand.literal(eis.readString())

    @staticmethod
    def polarizationTypeFromBin(row, eis):
        """
        Set the polarizationType in row from the EndianInput (eis) instance.
        """

        row._polarizationType = PolarizationType.literal(eis.readString())

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
    def antennaMakeFromBin(row, eis):
        """
        Set the antennaMake in row from the EndianInput (eis) instance.
        """

        row._antennaMake = AntennaMake.literal(eis.readString())

    @staticmethod
    def numCoeffFromBin(row, eis):
        """
        Set the numCoeff in row from the EndianInput (eis) instance.
        """

        row._numCoeff = eis.readInt()

    @staticmethod
    def numSourceObsFromBin(row, eis):
        """
        Set the numSourceObs in row from the EndianInput (eis) instance.
        """

        row._numSourceObs = eis.readInt()

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
    def coeffFormulaFromBin(row, eis):
        """
        Set the coeffFormula in row from the EndianInput (eis) instance.
        """

        coeffFormulaDim1 = eis.readInt()
        thisList = []
        for i in range(coeffFormulaDim1):
            thisValue = eis.readStr()
            thisList.append(thisValue)
        row._coeffFormula = thisList

    @staticmethod
    def coeffValueFromBin(row, eis):
        """
        Set the coeffValue in row from the EndianInput (eis) instance.
        """

        coeffValueDim1 = eis.readInt()
        thisList = []
        for i in range(coeffValueDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._coeffValue = thisList

    @staticmethod
    def coeffErrorFromBin(row, eis):
        """
        Set the coeffError in row from the EndianInput (eis) instance.
        """

        coeffErrorDim1 = eis.readInt()
        thisList = []
        for i in range(coeffErrorDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._coeffError = thisList

    @staticmethod
    def coeffFixedFromBin(row, eis):
        """
        Set the coeffFixed in row from the EndianInput (eis) instance.
        """

        coeffFixedDim1 = eis.readInt()
        thisList = []
        for i in range(coeffFixedDim1):
            thisValue = eis.readBool()
            thisList.append(thisValue)
        row._coeffFixed = thisList

    @staticmethod
    def focusModelFromBin(row, eis):
        """
        Set the focusModel in row from the EndianInput (eis) instance.
        """

        row._focusModel = eis.readStr()

    @staticmethod
    def focusRMSFromBin(row, eis):
        """
        Set the focusRMS in row from the EndianInput (eis) instance.
        """

        row._focusRMS = Length.from1DBin(eis)

    @staticmethod
    def reducedChiSquaredFromBin(row, eis):
        """
        Set the reducedChiSquared in row from the EndianInput (eis) instance.
        """

        row._reducedChiSquared = eis.readDouble()

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaName"] = CalFocusModelRow.antennaNameFromBin
        _fromBinMethods["receiverBand"] = CalFocusModelRow.receiverBandFromBin
        _fromBinMethods["polarizationType"] = CalFocusModelRow.polarizationTypeFromBin
        _fromBinMethods["calDataId"] = CalFocusModelRow.calDataIdFromBin
        _fromBinMethods["calReductionId"] = CalFocusModelRow.calReductionIdFromBin
        _fromBinMethods["startValidTime"] = CalFocusModelRow.startValidTimeFromBin
        _fromBinMethods["endValidTime"] = CalFocusModelRow.endValidTimeFromBin
        _fromBinMethods["antennaMake"] = CalFocusModelRow.antennaMakeFromBin
        _fromBinMethods["numCoeff"] = CalFocusModelRow.numCoeffFromBin
        _fromBinMethods["numSourceObs"] = CalFocusModelRow.numSourceObsFromBin
        _fromBinMethods["coeffName"] = CalFocusModelRow.coeffNameFromBin
        _fromBinMethods["coeffFormula"] = CalFocusModelRow.coeffFormulaFromBin
        _fromBinMethods["coeffValue"] = CalFocusModelRow.coeffValueFromBin
        _fromBinMethods["coeffError"] = CalFocusModelRow.coeffErrorFromBin
        _fromBinMethods["coeffFixed"] = CalFocusModelRow.coeffFixedFromBin
        _fromBinMethods["focusModel"] = CalFocusModelRow.focusModelFromBin
        _fromBinMethods["focusRMS"] = CalFocusModelRow.focusRMSFromBin
        _fromBinMethods["reducedChiSquared"] = CalFocusModelRow.reducedChiSquaredFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CalFocusModelRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalFocusModel",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

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

        The values are saved as single precision floats.



        """

        # value must be a list
        if not isinstance(coeffValue, list):
            raise ValueError("The value of coeffValue must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(coeffValue)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of coeffValue is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(coeffValue, float):
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

        The values are saved as single precision floats.



        """

        # value must be a list
        if not isinstance(coeffError, list):
            raise ValueError("The value of coeffError must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(coeffError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of coeffError is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(coeffError, float):
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
            listDims = pyasdm.utils.getListDims(coeffFixed)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of coeffFixed is not correct")

            # the type of the values in the list must be bool
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(coeffFixed, bool):
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
            listDims = pyasdm.utils.getListDims(focusRMS)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of focusRMS is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(focusRMS, Length):
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
        return reducedChiSquared as float
        """

        return self._reducedChiSquared

    def setReducedChiSquared(self, reducedChiSquared):
        """
        Set reducedChiSquared with the specified float value.
        reducedChiSquared The float value to which reducedChiSquared is to be set.

        The values are saved as double precision floats.



        """

        self._reducedChiSquared = float(reducedChiSquared)

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

        # reducedChiSquared is a float, compare using the == operator.
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

        # reducedChiSquared is a float, compare using the == operator.
        if not (self._reducedChiSquared == reducedChiSquared):
            return False

        return True


# initialize the dictionary that maps fields to init methods
CalFocusModelRow.initFromBinMethods()
