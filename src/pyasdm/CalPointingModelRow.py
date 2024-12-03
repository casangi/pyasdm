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
# File CalPointingModelRow.py
#

import pyasdm.CalPointingModelTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.AntennaMake import AntennaMake


from pyasdm.enumerations.PointingModelMode import PointingModelMode


from pyasdm.enumerations.PolarizationType import PolarizationType


from xml.dom import minidom

import copy


class CalPointingModelRow:
    """
    The CalPointingModelRow class is a row of a CalPointingModelTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalPointingModelRow.
        When row is None, create an empty row attached to table, which must be a CalPointingModelTable.
        When row is given, copy those values in to the new row. The row argument must be a CalPointingModelRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalPointingModelTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._receiverBand = ReceiverBand.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._antennaMake = AntennaMake.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._pointingModelMode = PointingModelMode.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._polarizationType = PolarizationType.from_int(0)

        if row is not None:
            if not isinstance(row, CalPointingModelRow):
                raise ValueError("row must be a MainRow")

            self._antennaName = row._antennaName

            # We force the attribute of the result to be not None
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            # We force the attribute of the result to be not None
            if row._antennaMake is None:
                self._antennaMake = AntennaMake.from_int(0)
            else:
                self._antennaMake = AntennaMake(row._antennaMake)

            # We force the attribute of the result to be not None
            if row._pointingModelMode is None:
                self._pointingModelMode = PointingModelMode.from_int(0)
            else:
                self._pointingModelMode = PointingModelMode(row._pointingModelMode)

            # We force the attribute of the result to be not None
            if row._polarizationType is None:
                self._polarizationType = PolarizationType.from_int(0)
            else:
                self._polarizationType = PolarizationType(row._polarizationType)

            self._numCoeff = row._numCoeff

            # coeffName is a  list , make a deep copy
            self._coeffName = copy.deepcopy(row._coeffName)

            # coeffVal is a  list , make a deep copy
            self._coeffVal = copy.deepcopy(row._coeffVal)

            # coeffError is a  list , make a deep copy
            self._coeffError = copy.deepcopy(row._coeffError)

            # coeffFixed is a  list , make a deep copy
            self._coeffFixed = copy.deepcopy(row._coeffFixed)

            self._azimuthRMS = Angle(row._azimuthRMS)

            self._elevationRms = Angle(row._elevationRms)

            self._skyRMS = Angle(row._skyRMS)

            self._reducedChiSquared = row._reducedChiSquared

            # by default set systematically numObs's value to something not None

            if row._numObsExists:

                self._numObs = row._numObs

                self._numObsExists = True

            # by default set systematically coeffFormula's value to something not None

            if row._coeffFormulaExists:

                # coeffFormula is a list, make a deep copy
                self.coeffFormula = copy.deepcopy(row.coeffFormula)

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

        result += Parser.valueToXML("antennaName", self._antennaName)

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.valueToXML("antennaMake", AntennaMake.name(self._antennaMake))

        result += Parser.valueToXML(
            "pointingModelMode", PointingModelMode.name(self._pointingModelMode)
        )

        result += Parser.valueToXML(
            "polarizationType", PolarizationType.name(self._polarizationType)
        )

        result += Parser.valueToXML("numCoeff", self._numCoeff)

        result += Parser.listValueToXML("coeffName", self._coeffName)

        result += Parser.listValueToXML("coeffVal", self._coeffVal)

        result += Parser.listValueToXML("coeffError", self._coeffError)

        result += Parser.listValueToXML("coeffFixed", self._coeffFixed)

        result += Parser.extendedValueToXML("azimuthRMS", self._azimuthRMS)

        result += Parser.extendedValueToXML("elevationRms", self._elevationRms)

        result += Parser.extendedValueToXML("skyRMS", self._skyRMS)

        result += Parser.valueToXML("reducedChiSquared", self._reducedChiSquared)

        if self._numObsExists:

            result += Parser.valueToXML("numObs", self._numObs)

        if self._coeffFormulaExists:

            result += Parser.listValueToXML("coeffFormula", self._coeffFormula)

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
                "xmlrow is not a string or a minidom.Element", "CalPointingModelTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException(
                "the argument is not a row", "CalPointingModelTable"
            )

        # intrinsic attribute values

        antennaNameNode = rowdom.getElementsByTagName("antennaName")[0]

        self._antennaName = str(antennaNameNode.firstChild.data)

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data
        )

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data)

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data)

        antennaMakeNode = rowdom.getElementsByTagName("antennaMake")[0]

        self._antennaMake = AntennaMake.newAntennaMake(antennaMakeNode.firstChild.data)

        pointingModelModeNode = rowdom.getElementsByTagName("pointingModelMode")[0]

        self._pointingModelMode = PointingModelMode.newPointingModelMode(
            pointingModelModeNode.firstChild.data
        )

        polarizationTypeNode = rowdom.getElementsByTagName("polarizationType")[0]

        self._polarizationType = PolarizationType.newPolarizationType(
            polarizationTypeNode.firstChild.data
        )

        numCoeffNode = rowdom.getElementsByTagName("numCoeff")[0]

        self._numCoeff = int(numCoeffNode.firstChild.data)

        coeffNameNode = rowdom.getElementsByTagName("coeffName")[0]

        coeffNameStr = coeffNameNode.firstChild.data
        self._coeffName = Parser.stringListToLists(
            coeffNameStr, str, "CalPointingModel"
        )

        coeffValNode = rowdom.getElementsByTagName("coeffVal")[0]

        coeffValStr = coeffValNode.firstChild.data
        self._coeffVal = Parser.stringListToLists(
            coeffValStr, float, "CalPointingModel"
        )

        coeffErrorNode = rowdom.getElementsByTagName("coeffError")[0]

        coeffErrorStr = coeffErrorNode.firstChild.data
        self._coeffError = Parser.stringListToLists(
            coeffErrorStr, float, "CalPointingModel"
        )

        coeffFixedNode = rowdom.getElementsByTagName("coeffFixed")[0]

        coeffFixedStr = coeffFixedNode.firstChild.data
        self._coeffFixed = Parser.stringListToLists(
            coeffFixedStr, bool, "CalPointingModel"
        )

        azimuthRMSNode = rowdom.getElementsByTagName("azimuthRMS")[0]

        self._azimuthRMS = Angle(azimuthRMSNode.firstChild.data)

        elevationRmsNode = rowdom.getElementsByTagName("elevationRms")[0]

        self._elevationRms = Angle(elevationRmsNode.firstChild.data)

        skyRMSNode = rowdom.getElementsByTagName("skyRMS")[0]

        self._skyRMS = Angle(skyRMSNode.firstChild.data)

        reducedChiSquaredNode = rowdom.getElementsByTagName("reducedChiSquared")[0]

        self._reducedChiSquared = double(reducedChiSquaredNode.firstChild.data)

        numObsNode = rowdom.getElementsByTagName("numObs")
        if len(numObsNode) > 0:

            self._numObs = int(numObsNode[0].firstChild.data)

            self._numObsExists = True

        coeffFormulaNode = rowdom.getElementsByTagName("coeffFormula")
        if len(coeffFormulaNode) > 0:

            coeffFormulaStr = coeffFormulaNode[0].firstChild.data
            self._coeffFormula = Parser.stringListToLists(
                coeffFormulaStr, str, "CalPointingModel"
            )

            self._coeffFormulaExists = True

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

    # ===> Attribute pointingModelMode

    _pointingModelMode = PointingModelMode.from_int(0)

    def getPointingModelMode(self):
        """
        Get pointingModelMode.
        return pointingModelMode as PointingModelMode
        """

        return self._pointingModelMode

    def setPointingModelMode(self, pointingModelMode):
        """
        Set pointingModelMode with the specified PointingModelMode value.
        pointingModelMode The PointingModelMode value to which pointingModelMode is to be set.


        """

        self._pointingModelMode = PointingModelMode(pointingModelMode)

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
            listDims = Parser.getListDims(coeffVal)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of coeffVal is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(coeffVal, float):
                raise ValueError(
                    "type of the first value in coeffVal is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._coeffVal = copy.deepcopy(coeffVal)
        except Exception as exc:
            raise ValueError("Invalid coeffVal : " + str(exc))

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

    # ===> Attribute azimuthRMS

    _azimuthRMS = Angle()

    def getAzimuthRMS(self):
        """
        Get azimuthRMS.
        return azimuthRMS as Angle
        """

        # make sure it is a copy of Angle
        return Angle(self._azimuthRMS)

    def setAzimuthRMS(self, azimuthRMS):
        """
        Set azimuthRMS with the specified Angle value.
        azimuthRMS The Angle value to which azimuthRMS is to be set.
        The value of azimuthRMS can be anything allowed by the Angle constructor.

        """

        self._azimuthRMS = Angle(azimuthRMS)

    # ===> Attribute elevationRms

    _elevationRms = Angle()

    def getElevationRms(self):
        """
        Get elevationRms.
        return elevationRms as Angle
        """

        # make sure it is a copy of Angle
        return Angle(self._elevationRms)

    def setElevationRms(self, elevationRms):
        """
        Set elevationRms with the specified Angle value.
        elevationRms The Angle value to which elevationRms is to be set.
        The value of elevationRms can be anything allowed by the Angle constructor.

        """

        self._elevationRms = Angle(elevationRms)

    # ===> Attribute skyRMS

    _skyRMS = Angle()

    def getSkyRMS(self):
        """
        Get skyRMS.
        return skyRMS as Angle
        """

        # make sure it is a copy of Angle
        return Angle(self._skyRMS)

    def setSkyRMS(self, skyRMS):
        """
        Set skyRMS with the specified Angle value.
        skyRMS The Angle value to which skyRMS is to be set.
        The value of skyRMS can be anything allowed by the Angle constructor.

        """

        self._skyRMS = Angle(skyRMS)

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

    # ===> Attribute numObs, which is optional
    _numObsExists = False

    _numObs = 0

    def isNumObsExists(self):
        """
        The attribute numObs is optional. Return True if this attribute exists.
        return True if and only if the numObs attribute exists.
        """
        return self._numObsExists

    def getNumObs(self):
        """
        Get numObs, which is optional.
        return numObs as int
        raises ValueError If numObs does not exist.
        """
        if not self._numObsExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numObs
                + " attribute in table CalPointingModel does not exist!"
            )

        return self._numObs

    def setNumObs(self, numObs):
        """
        Set numObs with the specified int value.
        numObs The int value to which numObs is to be set.


        """

        self._numObs = int(numObs)

        self._numObsExists = True

    def clearNumObs(self):
        """
        Mark numObs, which is an optional field, as non-existent.
        """
        self._numObsExists = False

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
                + " attribute in table CalPointingModel does not exist!"
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

        self._coeffFormulaExists = True

    def clearCoeffFormula(self):
        """
        Mark coeffFormula, which is an optional field, as non-existent.
        """
        self._coeffFormulaExists = False

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
        receiverBand,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        antennaMake,
        pointingModelMode,
        polarizationType,
        numCoeff,
        coeffName,
        coeffVal,
        coeffError,
        coeffFixed,
        azimuthRMS,
        elevationRms,
        skyRMS,
        reducedChiSquared,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalPointingModelRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaName is a str, compare using the == operator.
        if not (self._antennaName == antennaName):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
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

        # pointingModelMode is a PointingModelMode, compare using the == operator on the getValue() output
        if not (self._pointingModelMode.getValue() == pointingModelMode.getValue()):
            return False

        # polarizationType is a PolarizationType, compare using the == operator on the getValue() output
        if not (self._polarizationType.getValue() == polarizationType.getValue()):
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

        # azimuthRMS is a Angle, compare using the almostEquals method.
        if not self._azimuthRMS.almostEquals(
            azimuthRMS, self.getTable().getAzimuthRMSEqTolerance()
        ):
            return False

        # elevationRms is a Angle, compare using the almostEquals method.
        if not self._elevationRms.almostEquals(
            elevationRms, self.getTable().getElevationRmsEqTolerance()
        ):
            return False

        # skyRMS is a Angle, compare using the almostEquals method.
        if not self._skyRMS.almostEquals(
            skyRMS, self.getTable().getSkyRMSEqTolerance()
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
            otherRow.getPointingModelMode(),
            otherRow.getPolarizationType(),
            otherRow.getNumCoeff(),
            otherRow.getCoeffName(),
            otherRow.getCoeffVal(),
            otherRow.getCoeffError(),
            otherRow.getCoeffFixed(),
            otherRow.getAzimuthRMS(),
            otherRow.getElevationRms(),
            otherRow.getSkyRMS(),
            otherRow.getReducedChiSquared(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        antennaMake,
        pointingModelMode,
        polarizationType,
        numCoeff,
        coeffName,
        coeffVal,
        coeffError,
        coeffFixed,
        azimuthRMS,
        elevationRms,
        skyRMS,
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

        # pointingModelMode is a PointingModelMode, compare using the == operator on the getValue() output
        if not (self._pointingModelMode.getValue() == pointingModelMode.getValue()):
            return False

        # polarizationType is a PolarizationType, compare using the == operator on the getValue() output
        if not (self._polarizationType.getValue() == polarizationType.getValue()):
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

        # azimuthRMS is a Angle, compare using the almostEquals method.
        if not self._azimuthRMS.almostEquals(
            azimuthRMS, self.getTable().getAzimuthRMSEqTolerance()
        ):
            return False

        # elevationRms is a Angle, compare using the almostEquals method.
        if not self._elevationRms.almostEquals(
            elevationRms, self.getTable().getElevationRmsEqTolerance()
        ):
            return False

        # skyRMS is a Angle, compare using the almostEquals method.
        if not self._skyRMS.almostEquals(
            skyRMS, self.getTable().getSkyRMSEqTolerance()
        ):
            return False

        # reducedChiSquared is a double, compare using the == operator.
        if not (self._reducedChiSquared == reducedChiSquared):
            return False

        return True
