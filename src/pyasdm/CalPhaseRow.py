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
# File CalPhaseRow.py
#

import pyasdm.CalPhaseTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.BasebandName import BasebandName


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.AtmPhaseCorrection import AtmPhaseCorrection


from pyasdm.enumerations.PolarizationType import PolarizationType


from xml.dom import minidom

import copy


class CalPhaseRow:
    """
    The CalPhaseRow class is a row of a CalPhaseTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalPhaseRow.
        When row is None, create an empty row attached to table, which must be a CalPhaseTable.
        When row is given, copy those values in to the new row. The row argument must be a CalPhaseRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalPhaseTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._basebandName = BasebandName.from_int(0)

        self._receiverBand = ReceiverBand.from_int(0)

        self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._numBaseline = 0

        self._numReceptor = 0

        self._ampli = []  # this is a list of float []  []

        self._antennaNames = []  # this is a list of str []  []

        self._baselineLengths = []  # this is a list of Length []

        self._decorrelationFactor = []  # this is a list of float []  []

        self._direction = []  # this is a list of Angle []

        self._frequencyRange = []  # this is a list of Frequency []

        self._integrationTime = Interval()

        self._phase = []  # this is a list of float []  []

        self._polarizationTypes = []  # this is a list of PolarizationType []

        self._phaseRMS = []  # this is a list of float []  []

        self._statPhaseRMS = []  # this is a list of float []  []

        self._correctionValidityExists = False

        self._correctionValidity = []  # this is a list of bool []

        self._numAntennaExists = False

        self._numAntenna = 0

        self._singleAntennaNameExists = False

        self._singleAntennaName = []  # this is a list of str []

        self._refAntennaNameExists = False

        self._refAntennaName = None

        self._phaseAntExists = False

        self._phaseAnt = []  # this is a list of float []  []

        self._phaseAntRMSExists = False

        self._phaseAntRMS = []  # this is a list of float []  []

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalPhaseRow):
                raise ValueError("row must be a MainRow")

            # copy constructor

            # We force the attribute of the result to be not None
            if row._basebandName is None:
                self._basebandName = BasebandName.from_int(0)
            else:
                self._basebandName = BasebandName(row._basebandName)

            # We force the attribute of the result to be not None
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            # We force the attribute of the result to be not None
            if row._atmPhaseCorrection is None:
                self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)
            else:
                self._atmPhaseCorrection = AtmPhaseCorrection(row._atmPhaseCorrection)

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            self._numBaseline = row._numBaseline

            self._numReceptor = row._numReceptor

            # ampli is a  list , make a deep copy
            self._ampli = copy.deepcopy(row._ampli)

            # antennaNames is a  list , make a deep copy
            self._antennaNames = copy.deepcopy(row._antennaNames)

            # baselineLengths is a  list , make a deep copy
            self._baselineLengths = copy.deepcopy(row._baselineLengths)

            # decorrelationFactor is a  list , make a deep copy
            self._decorrelationFactor = copy.deepcopy(row._decorrelationFactor)

            # direction is a  list , make a deep copy
            self._direction = copy.deepcopy(row._direction)

            # frequencyRange is a  list , make a deep copy
            self._frequencyRange = copy.deepcopy(row._frequencyRange)

            self._integrationTime = Interval(row._integrationTime)

            # phase is a  list , make a deep copy
            self._phase = copy.deepcopy(row._phase)

            # polarizationTypes is a  list , make a deep copy
            self._polarizationTypes = copy.deepcopy(row._polarizationTypes)

            # phaseRMS is a  list , make a deep copy
            self._phaseRMS = copy.deepcopy(row._phaseRMS)

            # statPhaseRMS is a  list , make a deep copy
            self._statPhaseRMS = copy.deepcopy(row._statPhaseRMS)

            # by default set systematically correctionValidity's value to something not None

            if row._correctionValidityExists:

                # correctionValidity is a list, make a deep copy
                self.correctionValidity = copy.deepcopy(row.correctionValidity)

                self._correctionValidityExists = True

            # by default set systematically numAntenna's value to something not None

            if row._numAntennaExists:

                self._numAntenna = row._numAntenna

                self._numAntennaExists = True

            # by default set systematically singleAntennaName's value to something not None

            if row._singleAntennaNameExists:

                # singleAntennaName is a list, make a deep copy
                self.singleAntennaName = copy.deepcopy(row.singleAntennaName)

                self._singleAntennaNameExists = True

            # by default set systematically refAntennaName's value to something not None

            if row._refAntennaNameExists:

                self._refAntennaName = row._refAntennaName

                self._refAntennaNameExists = True

            # by default set systematically phaseAnt's value to something not None

            if row._phaseAntExists:

                # phaseAnt is a list, make a deep copy
                self.phaseAnt = copy.deepcopy(row.phaseAnt)

                self._phaseAntExists = True

            # by default set systematically phaseAntRMS's value to something not None

            if row._phaseAntRMSExists:

                # phaseAntRMS is a list, make a deep copy
                self.phaseAntRMS = copy.deepcopy(row.phaseAntRMS)

                self._phaseAntRMSExists = True

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

        result += Parser.valueToXML(
            "basebandName", BasebandName.name(self._basebandName)
        )

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.valueToXML(
            "atmPhaseCorrection", AtmPhaseCorrection.name(self._atmPhaseCorrection)
        )

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.valueToXML("numBaseline", self._numBaseline)

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listValueToXML("ampli", self._ampli)

        result += Parser.listValueToXML("antennaNames", self._antennaNames)

        result += Parser.listExtendedValueToXML(
            "baselineLengths", self._baselineLengths
        )

        result += Parser.listValueToXML(
            "decorrelationFactor", self._decorrelationFactor
        )

        result += Parser.listExtendedValueToXML("direction", self._direction)

        result += Parser.listExtendedValueToXML("frequencyRange", self._frequencyRange)

        result += Parser.extendedValueToXML("integrationTime", self._integrationTime)

        result += Parser.listValueToXML("phase", self._phase)

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.listValueToXML("phaseRMS", self._phaseRMS)

        result += Parser.listValueToXML("statPhaseRMS", self._statPhaseRMS)

        if self._correctionValidityExists:

            result += Parser.listValueToXML(
                "correctionValidity", self._correctionValidity
            )

        if self._numAntennaExists:

            result += Parser.valueToXML("numAntenna", self._numAntenna)

        if self._singleAntennaNameExists:

            result += Parser.listValueToXML(
                "singleAntennaName", self._singleAntennaName
            )

        if self._refAntennaNameExists:

            result += Parser.valueToXML("refAntennaName", self._refAntennaName)

        if self._phaseAntExists:

            result += Parser.listValueToXML("phaseAnt", self._phaseAnt)

        if self._phaseAntRMSExists:

            result += Parser.listValueToXML("phaseAntRMS", self._phaseAntRMS)

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
                "xmlrow is not a string or a minidom.Element", "CalPhaseTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalPhaseTable")

        # intrinsic attribute values

        basebandNameNode = rowdom.getElementsByTagName("basebandName")[0]

        self._basebandName = BasebandName.newBasebandName(
            basebandNameNode.firstChild.data.strip()
        )

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data.strip()
        )

        atmPhaseCorrectionNode = rowdom.getElementsByTagName("atmPhaseCorrection")[0]

        self._atmPhaseCorrection = AtmPhaseCorrection.newAtmPhaseCorrection(
            atmPhaseCorrectionNode.firstChild.data.strip()
        )

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        numBaselineNode = rowdom.getElementsByTagName("numBaseline")[0]

        self._numBaseline = int(numBaselineNode.firstChild.data.strip())

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        ampliNode = rowdom.getElementsByTagName("ampli")[0]

        ampliStr = ampliNode.firstChild.data.strip()

        self._ampli = Parser.stringListToLists(ampliStr, float, "CalPhase", False)

        antennaNamesNode = rowdom.getElementsByTagName("antennaNames")[0]

        antennaNamesStr = antennaNamesNode.firstChild.data.strip()

        self._antennaNames = Parser.stringListToLists(
            antennaNamesStr, str, "CalPhase", False
        )

        baselineLengthsNode = rowdom.getElementsByTagName("baselineLengths")[0]

        baselineLengthsStr = baselineLengthsNode.firstChild.data.strip()

        self._baselineLengths = Parser.stringListToLists(
            baselineLengthsStr, Length, "CalPhase", True
        )

        decorrelationFactorNode = rowdom.getElementsByTagName("decorrelationFactor")[0]

        decorrelationFactorStr = decorrelationFactorNode.firstChild.data.strip()

        self._decorrelationFactor = Parser.stringListToLists(
            decorrelationFactorStr, float, "CalPhase", False
        )

        directionNode = rowdom.getElementsByTagName("direction")[0]

        directionStr = directionNode.firstChild.data.strip()

        self._direction = Parser.stringListToLists(
            directionStr, Angle, "CalPhase", True
        )

        frequencyRangeNode = rowdom.getElementsByTagName("frequencyRange")[0]

        frequencyRangeStr = frequencyRangeNode.firstChild.data.strip()

        self._frequencyRange = Parser.stringListToLists(
            frequencyRangeStr, Frequency, "CalPhase", True
        )

        integrationTimeNode = rowdom.getElementsByTagName("integrationTime")[0]

        self._integrationTime = Interval(integrationTimeNode.firstChild.data.strip())

        phaseNode = rowdom.getElementsByTagName("phase")[0]

        phaseStr = phaseNode.firstChild.data.strip()

        self._phase = Parser.stringListToLists(phaseStr, float, "CalPhase", False)

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data.strip()
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "CalPhase", False
        )

        phaseRMSNode = rowdom.getElementsByTagName("phaseRMS")[0]

        phaseRMSStr = phaseRMSNode.firstChild.data.strip()

        self._phaseRMS = Parser.stringListToLists(phaseRMSStr, float, "CalPhase", False)

        statPhaseRMSNode = rowdom.getElementsByTagName("statPhaseRMS")[0]

        statPhaseRMSStr = statPhaseRMSNode.firstChild.data.strip()

        self._statPhaseRMS = Parser.stringListToLists(
            statPhaseRMSStr, float, "CalPhase", False
        )

        correctionValidityNode = rowdom.getElementsByTagName("correctionValidity")
        if len(correctionValidityNode) > 0:

            correctionValidityStr = correctionValidityNode[0].firstChild.data.strip()

            self._correctionValidity = Parser.stringListToLists(
                correctionValidityStr, bool, "CalPhase", False
            )

            self._correctionValidityExists = True

        numAntennaNode = rowdom.getElementsByTagName("numAntenna")
        if len(numAntennaNode) > 0:

            self._numAntenna = int(numAntennaNode[0].firstChild.data.strip())

            self._numAntennaExists = True

        singleAntennaNameNode = rowdom.getElementsByTagName("singleAntennaName")
        if len(singleAntennaNameNode) > 0:

            singleAntennaNameStr = singleAntennaNameNode[0].firstChild.data.strip()

            self._singleAntennaName = Parser.stringListToLists(
                singleAntennaNameStr, str, "CalPhase", False
            )

            self._singleAntennaNameExists = True

        refAntennaNameNode = rowdom.getElementsByTagName("refAntennaName")
        if len(refAntennaNameNode) > 0:

            self._refAntennaName = str(refAntennaNameNode[0].firstChild.data.strip())

            self._refAntennaNameExists = True

        phaseAntNode = rowdom.getElementsByTagName("phaseAnt")
        if len(phaseAntNode) > 0:

            phaseAntStr = phaseAntNode[0].firstChild.data.strip()

            self._phaseAnt = Parser.stringListToLists(
                phaseAntStr, float, "CalPhase", False
            )

            self._phaseAntExists = True

        phaseAntRMSNode = rowdom.getElementsByTagName("phaseAntRMS")
        if len(phaseAntRMSNode) > 0:

            phaseAntRMSStr = phaseAntRMSNode[0].firstChild.data.strip()

            self._phaseAntRMS = Parser.stringListToLists(
                phaseAntRMSStr, float, "CalPhase", False
            )

            self._phaseAntRMSExists = True

        # extrinsic attribute values

        calDataIdNode = rowdom.getElementsByTagName("calDataId")[0]

        self._calDataId = Tag(calDataIdNode.firstChild.data.strip())

        calReductionIdNode = rowdom.getElementsByTagName("calReductionId")[0]

        self._calReductionId = Tag(calReductionIdNode.firstChild.data.strip())

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

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

    # ===> Attribute numBaseline

    _numBaseline = 0

    def getNumBaseline(self):
        """
        Get numBaseline.
        return numBaseline as int
        """

        return self._numBaseline

    def setNumBaseline(self, numBaseline):
        """
        Set numBaseline with the specified int value.
        numBaseline The int value to which numBaseline is to be set.


        """

        self._numBaseline = int(numBaseline)

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

    # ===> Attribute ampli

    _ampli = None  # this is a 2D list of float

    def getAmpli(self):
        """
        Get ampli.
        return ampli as float []  []
        """

        return copy.deepcopy(self._ampli)

    def setAmpli(self, ampli):
        """
        Set ampli with the specified float []  []  value.
        ampli The float []  []  value to which ampli is to be set.


        """

        # value must be a list
        if not isinstance(ampli, list):
            raise ValueError("The value of ampli must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(ampli)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of ampli is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(ampli, float):
                raise ValueError(
                    "type of the first value in ampli is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._ampli = copy.deepcopy(ampli)
        except Exception as exc:
            raise ValueError("Invalid ampli : " + str(exc))

    # ===> Attribute antennaNames

    _antennaNames = None  # this is a 2D list of str

    def getAntennaNames(self):
        """
        Get antennaNames.
        return antennaNames as str []  []
        """

        return copy.deepcopy(self._antennaNames)

    def setAntennaNames(self, antennaNames):
        """
        Set antennaNames with the specified str []  []  value.
        antennaNames The str []  []  value to which antennaNames is to be set.


        """

        # value must be a list
        if not isinstance(antennaNames, list):
            raise ValueError("The value of antennaNames must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(antennaNames)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of antennaNames is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not Parser.checkListType(antennaNames, str):
                raise ValueError(
                    "type of the first value in antennaNames is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._antennaNames = copy.deepcopy(antennaNames)
        except Exception as exc:
            raise ValueError("Invalid antennaNames : " + str(exc))

    # ===> Attribute baselineLengths

    _baselineLengths = None  # this is a 1D list of Length

    def getBaselineLengths(self):
        """
        Get baselineLengths.
        return baselineLengths as Length []
        """

        return copy.deepcopy(self._baselineLengths)

    def setBaselineLengths(self, baselineLengths):
        """
        Set baselineLengths with the specified Length []  value.
        baselineLengths The Length []  value to which baselineLengths is to be set.
        The value of baselineLengths can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(baselineLengths, list):
            raise ValueError("The value of baselineLengths must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(baselineLengths)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of baselineLengths is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(baselineLengths, Length):
                raise ValueError(
                    "type of the first value in baselineLengths is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._baselineLengths = copy.deepcopy(baselineLengths)
        except Exception as exc:
            raise ValueError("Invalid baselineLengths : " + str(exc))

    # ===> Attribute decorrelationFactor

    _decorrelationFactor = None  # this is a 2D list of float

    def getDecorrelationFactor(self):
        """
        Get decorrelationFactor.
        return decorrelationFactor as float []  []
        """

        return copy.deepcopy(self._decorrelationFactor)

    def setDecorrelationFactor(self, decorrelationFactor):
        """
        Set decorrelationFactor with the specified float []  []  value.
        decorrelationFactor The float []  []  value to which decorrelationFactor is to be set.


        """

        # value must be a list
        if not isinstance(decorrelationFactor, list):
            raise ValueError("The value of decorrelationFactor must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(decorrelationFactor)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of decorrelationFactor is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(decorrelationFactor, float):
                raise ValueError(
                    "type of the first value in decorrelationFactor is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._decorrelationFactor = copy.deepcopy(decorrelationFactor)
        except Exception as exc:
            raise ValueError("Invalid decorrelationFactor : " + str(exc))

    # ===> Attribute direction

    _direction = None  # this is a 1D list of Angle

    def getDirection(self):
        """
        Get direction.
        return direction as Angle []
        """

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

    # ===> Attribute integrationTime

    _integrationTime = Interval()

    def getIntegrationTime(self):
        """
        Get integrationTime.
        return integrationTime as Interval
        """

        # make sure it is a copy of Interval
        return Interval(self._integrationTime)

    def setIntegrationTime(self, integrationTime):
        """
        Set integrationTime with the specified Interval value.
        integrationTime The Interval value to which integrationTime is to be set.
        The value of integrationTime can be anything allowed by the Interval constructor.

        """

        self._integrationTime = Interval(integrationTime)

    # ===> Attribute phase

    _phase = None  # this is a 2D list of float

    def getPhase(self):
        """
        Get phase.
        return phase as float []  []
        """

        return copy.deepcopy(self._phase)

    def setPhase(self, phase):
        """
        Set phase with the specified float []  []  value.
        phase The float []  []  value to which phase is to be set.


        """

        # value must be a list
        if not isinstance(phase, list):
            raise ValueError("The value of phase must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(phase)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of phase is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(phase, float):
                raise ValueError(
                    "type of the first value in phase is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phase = copy.deepcopy(phase)
        except Exception as exc:
            raise ValueError("Invalid phase : " + str(exc))

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

    # ===> Attribute phaseRMS

    _phaseRMS = None  # this is a 2D list of float

    def getPhaseRMS(self):
        """
        Get phaseRMS.
        return phaseRMS as float []  []
        """

        return copy.deepcopy(self._phaseRMS)

    def setPhaseRMS(self, phaseRMS):
        """
        Set phaseRMS with the specified float []  []  value.
        phaseRMS The float []  []  value to which phaseRMS is to be set.


        """

        # value must be a list
        if not isinstance(phaseRMS, list):
            raise ValueError("The value of phaseRMS must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(phaseRMS)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of phaseRMS is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(phaseRMS, float):
                raise ValueError(
                    "type of the first value in phaseRMS is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phaseRMS = copy.deepcopy(phaseRMS)
        except Exception as exc:
            raise ValueError("Invalid phaseRMS : " + str(exc))

    # ===> Attribute statPhaseRMS

    _statPhaseRMS = None  # this is a 2D list of float

    def getStatPhaseRMS(self):
        """
        Get statPhaseRMS.
        return statPhaseRMS as float []  []
        """

        return copy.deepcopy(self._statPhaseRMS)

    def setStatPhaseRMS(self, statPhaseRMS):
        """
        Set statPhaseRMS with the specified float []  []  value.
        statPhaseRMS The float []  []  value to which statPhaseRMS is to be set.


        """

        # value must be a list
        if not isinstance(statPhaseRMS, list):
            raise ValueError("The value of statPhaseRMS must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(statPhaseRMS)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of statPhaseRMS is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(statPhaseRMS, float):
                raise ValueError(
                    "type of the first value in statPhaseRMS is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._statPhaseRMS = copy.deepcopy(statPhaseRMS)
        except Exception as exc:
            raise ValueError("Invalid statPhaseRMS : " + str(exc))

    # ===> Attribute correctionValidity, which is optional
    _correctionValidityExists = False

    _correctionValidity = None  # this is a 1D list of bool

    def isCorrectionValidityExists(self):
        """
        The attribute correctionValidity is optional. Return True if this attribute exists.
        return True if and only if the correctionValidity attribute exists.
        """
        return self._correctionValidityExists

    def getCorrectionValidity(self):
        """
        Get correctionValidity, which is optional.
        return correctionValidity as bool []
        raises ValueError If correctionValidity does not exist.
        """
        if not self._correctionValidityExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + correctionValidity
                + " attribute in table CalPhase does not exist!"
            )

        return copy.deepcopy(self._correctionValidity)

    def setCorrectionValidity(self, correctionValidity):
        """
        Set correctionValidity with the specified bool []  value.
        correctionValidity The bool []  value to which correctionValidity is to be set.


        """

        # value must be a list
        if not isinstance(correctionValidity, list):
            raise ValueError("The value of correctionValidity must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(correctionValidity)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of correctionValidity is not correct")

            # the type of the values in the list must be bool
            # note : this only checks the first value found
            if not Parser.checkListType(correctionValidity, bool):
                raise ValueError(
                    "type of the first value in correctionValidity is not bool as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._correctionValidity = copy.deepcopy(correctionValidity)
        except Exception as exc:
            raise ValueError("Invalid correctionValidity : " + str(exc))

        self._correctionValidityExists = True

    def clearCorrectionValidity(self):
        """
        Mark correctionValidity, which is an optional field, as non-existent.
        """
        self._correctionValidityExists = False

    # ===> Attribute numAntenna, which is optional
    _numAntennaExists = False

    _numAntenna = 0

    def isNumAntennaExists(self):
        """
        The attribute numAntenna is optional. Return True if this attribute exists.
        return True if and only if the numAntenna attribute exists.
        """
        return self._numAntennaExists

    def getNumAntenna(self):
        """
        Get numAntenna, which is optional.
        return numAntenna as int
        raises ValueError If numAntenna does not exist.
        """
        if not self._numAntennaExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numAntenna
                + " attribute in table CalPhase does not exist!"
            )

        return self._numAntenna

    def setNumAntenna(self, numAntenna):
        """
        Set numAntenna with the specified int value.
        numAntenna The int value to which numAntenna is to be set.


        """

        self._numAntenna = int(numAntenna)

        self._numAntennaExists = True

    def clearNumAntenna(self):
        """
        Mark numAntenna, which is an optional field, as non-existent.
        """
        self._numAntennaExists = False

    # ===> Attribute singleAntennaName, which is optional
    _singleAntennaNameExists = False

    _singleAntennaName = None  # this is a 1D list of str

    def isSingleAntennaNameExists(self):
        """
        The attribute singleAntennaName is optional. Return True if this attribute exists.
        return True if and only if the singleAntennaName attribute exists.
        """
        return self._singleAntennaNameExists

    def getSingleAntennaName(self):
        """
        Get singleAntennaName, which is optional.
        return singleAntennaName as str []
        raises ValueError If singleAntennaName does not exist.
        """
        if not self._singleAntennaNameExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + singleAntennaName
                + " attribute in table CalPhase does not exist!"
            )

        return copy.deepcopy(self._singleAntennaName)

    def setSingleAntennaName(self, singleAntennaName):
        """
        Set singleAntennaName with the specified str []  value.
        singleAntennaName The str []  value to which singleAntennaName is to be set.


        """

        # value must be a list
        if not isinstance(singleAntennaName, list):
            raise ValueError("The value of singleAntennaName must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(singleAntennaName)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of singleAntennaName is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not Parser.checkListType(singleAntennaName, str):
                raise ValueError(
                    "type of the first value in singleAntennaName is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._singleAntennaName = copy.deepcopy(singleAntennaName)
        except Exception as exc:
            raise ValueError("Invalid singleAntennaName : " + str(exc))

        self._singleAntennaNameExists = True

    def clearSingleAntennaName(self):
        """
        Mark singleAntennaName, which is an optional field, as non-existent.
        """
        self._singleAntennaNameExists = False

    # ===> Attribute refAntennaName, which is optional
    _refAntennaNameExists = False

    _refAntennaName = None

    def isRefAntennaNameExists(self):
        """
        The attribute refAntennaName is optional. Return True if this attribute exists.
        return True if and only if the refAntennaName attribute exists.
        """
        return self._refAntennaNameExists

    def getRefAntennaName(self):
        """
        Get refAntennaName, which is optional.
        return refAntennaName as str
        raises ValueError If refAntennaName does not exist.
        """
        if not self._refAntennaNameExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + refAntennaName
                + " attribute in table CalPhase does not exist!"
            )

        return self._refAntennaName

    def setRefAntennaName(self, refAntennaName):
        """
        Set refAntennaName with the specified str value.
        refAntennaName The str value to which refAntennaName is to be set.


        """

        self._refAntennaName = str(refAntennaName)

        self._refAntennaNameExists = True

    def clearRefAntennaName(self):
        """
        Mark refAntennaName, which is an optional field, as non-existent.
        """
        self._refAntennaNameExists = False

    # ===> Attribute phaseAnt, which is optional
    _phaseAntExists = False

    _phaseAnt = None  # this is a 2D list of float

    def isPhaseAntExists(self):
        """
        The attribute phaseAnt is optional. Return True if this attribute exists.
        return True if and only if the phaseAnt attribute exists.
        """
        return self._phaseAntExists

    def getPhaseAnt(self):
        """
        Get phaseAnt, which is optional.
        return phaseAnt as float []  []
        raises ValueError If phaseAnt does not exist.
        """
        if not self._phaseAntExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + phaseAnt
                + " attribute in table CalPhase does not exist!"
            )

        return copy.deepcopy(self._phaseAnt)

    def setPhaseAnt(self, phaseAnt):
        """
        Set phaseAnt with the specified float []  []  value.
        phaseAnt The float []  []  value to which phaseAnt is to be set.


        """

        # value must be a list
        if not isinstance(phaseAnt, list):
            raise ValueError("The value of phaseAnt must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(phaseAnt)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of phaseAnt is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(phaseAnt, float):
                raise ValueError(
                    "type of the first value in phaseAnt is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phaseAnt = copy.deepcopy(phaseAnt)
        except Exception as exc:
            raise ValueError("Invalid phaseAnt : " + str(exc))

        self._phaseAntExists = True

    def clearPhaseAnt(self):
        """
        Mark phaseAnt, which is an optional field, as non-existent.
        """
        self._phaseAntExists = False

    # ===> Attribute phaseAntRMS, which is optional
    _phaseAntRMSExists = False

    _phaseAntRMS = None  # this is a 2D list of float

    def isPhaseAntRMSExists(self):
        """
        The attribute phaseAntRMS is optional. Return True if this attribute exists.
        return True if and only if the phaseAntRMS attribute exists.
        """
        return self._phaseAntRMSExists

    def getPhaseAntRMS(self):
        """
        Get phaseAntRMS, which is optional.
        return phaseAntRMS as float []  []
        raises ValueError If phaseAntRMS does not exist.
        """
        if not self._phaseAntRMSExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + phaseAntRMS
                + " attribute in table CalPhase does not exist!"
            )

        return copy.deepcopy(self._phaseAntRMS)

    def setPhaseAntRMS(self, phaseAntRMS):
        """
        Set phaseAntRMS with the specified float []  []  value.
        phaseAntRMS The float []  []  value to which phaseAntRMS is to be set.


        """

        # value must be a list
        if not isinstance(phaseAntRMS, list):
            raise ValueError("The value of phaseAntRMS must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(phaseAntRMS)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of phaseAntRMS is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(phaseAntRMS, float):
                raise ValueError(
                    "type of the first value in phaseAntRMS is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phaseAntRMS = copy.deepcopy(phaseAntRMS)
        except Exception as exc:
            raise ValueError("Invalid phaseAntRMS : " + str(exc))

        self._phaseAntRMSExists = True

    def clearPhaseAntRMS(self):
        """
        Mark phaseAntRMS, which is an optional field, as non-existent.
        """
        self._phaseAntRMSExists = False

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
        basebandName,
        receiverBand,
        atmPhaseCorrection,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numBaseline,
        numReceptor,
        ampli,
        antennaNames,
        baselineLengths,
        decorrelationFactor,
        direction,
        frequencyRange,
        integrationTime,
        phase,
        polarizationTypes,
        phaseRMS,
        statPhaseRMS,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalPhaseRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # basebandName is a BasebandName, compare using the == operator on the getValue() output
        if not (self._basebandName.getValue() == basebandName.getValue()):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
            return False

        # atmPhaseCorrection is a AtmPhaseCorrection, compare using the == operator on the getValue() output
        if not (self._atmPhaseCorrection.getValue() == atmPhaseCorrection.getValue()):
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

        # numBaseline is a int, compare using the == operator.
        if not (self._numBaseline == numBaseline):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 2D arrays (lists)
        if ampli is not None:
            if self._ampli is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            ampli_dims = Parser.getListDims(ampli)
            this_ampli_dims = Parser.getListDims(self._ampli)
            if ampli_dims != this_ampli_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(ampli_dims[0]):
                for j in range(ampli_dims[0]):

                    # ampli is an array of float, compare using == operator.
                    if not (self._ampli[i][j] == ampli[i][j]):
                        return False

        # We compare two 2D arrays (lists)
        if antennaNames is not None:
            if self._antennaNames is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            antennaNames_dims = Parser.getListDims(antennaNames)
            this_antennaNames_dims = Parser.getListDims(self._antennaNames)
            if antennaNames_dims != this_antennaNames_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(antennaNames_dims[0]):
                for j in range(antennaNames_dims[0]):

                    # antennaNames is an array of str, compare using == operator.
                    if not (self._antennaNames[i][j] == antennaNames[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._baselineLengths) != len(baselineLengths):
            return False
        for indx in range(len(baselineLengths)):

            # baselineLengths is a list of Length, compare using the almostEquals method.
            if not self._baselineLengths[indx].almostEquals(
                baselineLengths[indx], self.getTable().getBaselineLengthsEqTolerance()
            ):
                return False

        # We compare two 2D arrays (lists)
        if decorrelationFactor is not None:
            if self._decorrelationFactor is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            decorrelationFactor_dims = Parser.getListDims(decorrelationFactor)
            this_decorrelationFactor_dims = Parser.getListDims(
                self._decorrelationFactor
            )
            if decorrelationFactor_dims != this_decorrelationFactor_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(decorrelationFactor_dims[0]):
                for j in range(decorrelationFactor_dims[0]):

                    # decorrelationFactor is an array of float, compare using == operator.
                    if not (
                        self._decorrelationFactor[i][j] == decorrelationFactor[i][j]
                    ):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._direction) != len(direction):
            return False
        for indx in range(len(direction)):

            # direction is a list of Angle, compare using the almostEquals method.
            if not self._direction[indx].almostEquals(
                direction[indx], self.getTable().getDirectionEqTolerance()
            ):
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

        # integrationTime is a Interval, compare using the equals method.
        if not self._integrationTime.equals(integrationTime):
            return False

        # We compare two 2D arrays (lists)
        if phase is not None:
            if self._phase is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            phase_dims = Parser.getListDims(phase)
            this_phase_dims = Parser.getListDims(self._phase)
            if phase_dims != this_phase_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(phase_dims[0]):
                for j in range(phase_dims[0]):

                    # phase is an array of float, compare using == operator.
                    if not (self._phase[i][j] == phase[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationTypes) != len(polarizationTypes):
            return False
        for indx in range(len(polarizationTypes)):

            # polarizationTypes is a list of PolarizationType, compare using == operator.
            if not (self._polarizationTypes[indx] == polarizationTypes[indx]):
                return False

        # We compare two 2D arrays (lists)
        if phaseRMS is not None:
            if self._phaseRMS is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            phaseRMS_dims = Parser.getListDims(phaseRMS)
            this_phaseRMS_dims = Parser.getListDims(self._phaseRMS)
            if phaseRMS_dims != this_phaseRMS_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(phaseRMS_dims[0]):
                for j in range(phaseRMS_dims[0]):

                    # phaseRMS is an array of float, compare using == operator.
                    if not (self._phaseRMS[i][j] == phaseRMS[i][j]):
                        return False

        # We compare two 2D arrays (lists)
        if statPhaseRMS is not None:
            if self._statPhaseRMS is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            statPhaseRMS_dims = Parser.getListDims(statPhaseRMS)
            this_statPhaseRMS_dims = Parser.getListDims(self._statPhaseRMS)
            if statPhaseRMS_dims != this_statPhaseRMS_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(statPhaseRMS_dims[0]):
                for j in range(statPhaseRMS_dims[0]):

                    # statPhaseRMS is an array of float, compare using == operator.
                    if not (self._statPhaseRMS[i][j] == statPhaseRMS[i][j]):
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
            otherRow.getNumBaseline(),
            otherRow.getNumReceptor(),
            otherRow.getAmpli(),
            otherRow.getAntennaNames(),
            otherRow.getBaselineLengths(),
            otherRow.getDecorrelationFactor(),
            otherRow.getDirection(),
            otherRow.getFrequencyRange(),
            otherRow.getIntegrationTime(),
            otherRow.getPhase(),
            otherRow.getPolarizationTypes(),
            otherRow.getPhaseRMS(),
            otherRow.getStatPhaseRMS(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        numBaseline,
        numReceptor,
        ampli,
        antennaNames,
        baselineLengths,
        decorrelationFactor,
        direction,
        frequencyRange,
        integrationTime,
        phase,
        polarizationTypes,
        phaseRMS,
        statPhaseRMS,
    ):

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # numBaseline is a int, compare using the == operator.
        if not (self._numBaseline == numBaseline):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 2D arrays (lists)
        if ampli is not None:
            if self._ampli is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            ampli_dims = Parser.getListDims(ampli)
            this_ampli_dims = Parser.getListDims(self._ampli)
            if ampli_dims != this_ampli_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(ampli_dims[0]):
                for j in range(ampli_dims[0]):

                    # ampli is an array of float, compare using == operator.
                    if not (self._ampli[i][j] == ampli[i][j]):
                        return False

        # We compare two 2D arrays (lists)
        if antennaNames is not None:
            if self._antennaNames is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            antennaNames_dims = Parser.getListDims(antennaNames)
            this_antennaNames_dims = Parser.getListDims(self._antennaNames)
            if antennaNames_dims != this_antennaNames_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(antennaNames_dims[0]):
                for j in range(antennaNames_dims[0]):

                    # antennaNames is an array of str, compare using == operator.
                    if not (self._antennaNames[i][j] == antennaNames[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._baselineLengths) != len(baselineLengths):
            return False
        for indx in range(len(baselineLengths)):

            # baselineLengths is a list of Length, compare using the almostEquals method.
            if not self._baselineLengths[indx].almostEquals(
                baselineLengths[indx], self.getTable().getBaselineLengthsEqTolerance()
            ):
                return False

        # We compare two 2D arrays (lists)
        if decorrelationFactor is not None:
            if self._decorrelationFactor is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            decorrelationFactor_dims = Parser.getListDims(decorrelationFactor)
            this_decorrelationFactor_dims = Parser.getListDims(
                self._decorrelationFactor
            )
            if decorrelationFactor_dims != this_decorrelationFactor_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(decorrelationFactor_dims[0]):
                for j in range(decorrelationFactor_dims[0]):

                    # decorrelationFactor is an array of float, compare using == operator.
                    if not (
                        self._decorrelationFactor[i][j] == decorrelationFactor[i][j]
                    ):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._direction) != len(direction):
            return False
        for indx in range(len(direction)):

            # direction is a list of Angle, compare using the almostEquals method.
            if not self._direction[indx].almostEquals(
                direction[indx], self.getTable().getDirectionEqTolerance()
            ):
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

        # integrationTime is a Interval, compare using the equals method.
        if not self._integrationTime.equals(integrationTime):
            return False

        # We compare two 2D arrays (lists)
        if phase is not None:
            if self._phase is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            phase_dims = Parser.getListDims(phase)
            this_phase_dims = Parser.getListDims(self._phase)
            if phase_dims != this_phase_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(phase_dims[0]):
                for j in range(phase_dims[0]):

                    # phase is an array of float, compare using == operator.
                    if not (self._phase[i][j] == phase[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationTypes) != len(polarizationTypes):
            return False
        for indx in range(len(polarizationTypes)):

            # polarizationTypes is a list of PolarizationType, compare using == operator.
            if not (self._polarizationTypes[indx] == polarizationTypes[indx]):
                return False

        # We compare two 2D arrays (lists)
        if phaseRMS is not None:
            if self._phaseRMS is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            phaseRMS_dims = Parser.getListDims(phaseRMS)
            this_phaseRMS_dims = Parser.getListDims(self._phaseRMS)
            if phaseRMS_dims != this_phaseRMS_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(phaseRMS_dims[0]):
                for j in range(phaseRMS_dims[0]):

                    # phaseRMS is an array of float, compare using == operator.
                    if not (self._phaseRMS[i][j] == phaseRMS[i][j]):
                        return False

        # We compare two 2D arrays (lists)
        if statPhaseRMS is not None:
            if self._statPhaseRMS is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            statPhaseRMS_dims = Parser.getListDims(statPhaseRMS)
            this_statPhaseRMS_dims = Parser.getListDims(self._statPhaseRMS)
            if statPhaseRMS_dims != this_statPhaseRMS_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(statPhaseRMS_dims[0]):
                for j in range(statPhaseRMS_dims[0]):

                    # statPhaseRMS is an array of float, compare using == operator.
                    if not (self._statPhaseRMS[i][j] == statPhaseRMS[i][j]):
                        return False

        return True
