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
# File CalFocusRow.py
#

import pyasdm.CalFocusTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.AtmPhaseCorrection import AtmPhaseCorrection


from pyasdm.enumerations.FocusMethod import FocusMethod


from pyasdm.enumerations.PolarizationType import PolarizationType


from xml.dom import minidom

import copy


class CalFocusRow:
    """
    The CalFocusRow class is a row of a CalFocusTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalFocusRow.
        When row is None, create an empty row attached to table, which must be a CalFocusTable.
        When row is given, copy those values in to the new row. The row argument must be a CalFocusRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalFocusTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._receiverBand = ReceiverBand.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._focusMethod = FocusMethod.from_int(0)

        # this is a list of PolarizationType Enumeration, start off with it being empty
        self._polarizationTypes = []

        if row is not None:
            if not isinstance(row, CalFocusRow):
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

            self._ambientTemperature = Temperature(row._ambientTemperature)

            # We force the attribute of the result to be not None
            if row._atmPhaseCorrection is None:
                self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)
            else:
                self._atmPhaseCorrection = AtmPhaseCorrection(row._atmPhaseCorrection)

            # We force the attribute of the result to be not None
            if row._focusMethod is None:
                self._focusMethod = FocusMethod.from_int(0)
            else:
                self._focusMethod = FocusMethod(row._focusMethod)

            # frequencyRange is a  list , make a deep copy
            self._frequencyRange = copy.deepcopy(row._frequencyRange)

            # pointingDirection is a  list , make a deep copy
            self._pointingDirection = copy.deepcopy(row._pointingDirection)

            self._numReceptor = row._numReceptor

            # polarizationTypes is a  list , make a deep copy
            self._polarizationTypes = copy.deepcopy(row._polarizationTypes)

            # wereFixed is a  list , make a deep copy
            self._wereFixed = copy.deepcopy(row._wereFixed)

            # offset is a  list , make a deep copy
            self._offset = copy.deepcopy(row._offset)

            # offsetError is a  list , make a deep copy
            self._offsetError = copy.deepcopy(row._offsetError)

            # offsetWasTied is a  list , make a deep copy
            self._offsetWasTied = copy.deepcopy(row._offsetWasTied)

            # reducedChiSquared is a  list , make a deep copy
            self._reducedChiSquared = copy.deepcopy(row._reducedChiSquared)

            # position is a  list , make a deep copy
            self._position = copy.deepcopy(row._position)

            # by default set systematically polarizationsAveraged's value to something not None

            if row._polarizationsAveragedExists:

                self._polarizationsAveraged = row._polarizationsAveraged

                self._polarizationsAveragedExists = True

            # by default set systematically focusCurveWidth's value to something not None

            if row._focusCurveWidthExists:

                # focusCurveWidth is a list, make a deep copy
                self.focusCurveWidth = copy.deepcopy(row.focusCurveWidth)

                self._focusCurveWidthExists = True

            # by default set systematically focusCurveWidthError's value to something not None

            if row._focusCurveWidthErrorExists:

                # focusCurveWidthError is a list, make a deep copy
                self.focusCurveWidthError = copy.deepcopy(row.focusCurveWidthError)

                self._focusCurveWidthErrorExists = True

            # by default set systematically focusCurveWasFixed's value to something not None

            if row._focusCurveWasFixedExists:

                # focusCurveWasFixed is a list, make a deep copy
                self.focusCurveWasFixed = copy.deepcopy(row.focusCurveWasFixed)

                self._focusCurveWasFixedExists = True

            # by default set systematically offIntensity's value to something not None

            if row._offIntensityExists:

                # offIntensity is a list, make a deep copy
                self.offIntensity = copy.deepcopy(row.offIntensity)

                self._offIntensityExists = True

            # by default set systematically offIntensityError's value to something not None

            if row._offIntensityErrorExists:

                # offIntensityError is a list, make a deep copy
                self.offIntensityError = copy.deepcopy(row.offIntensityError)

                self._offIntensityErrorExists = True

            # by default set systematically offIntensityWasFixed's value to something not None

            if row._offIntensityWasFixedExists:

                self._offIntensityWasFixed = row._offIntensityWasFixed

                self._offIntensityWasFixedExists = True

            # by default set systematically peakIntensity's value to something not None

            if row._peakIntensityExists:

                # peakIntensity is a list, make a deep copy
                self.peakIntensity = copy.deepcopy(row.peakIntensity)

                self._peakIntensityExists = True

            # by default set systematically peakIntensityError's value to something not None

            if row._peakIntensityErrorExists:

                # peakIntensityError is a list, make a deep copy
                self.peakIntensityError = copy.deepcopy(row.peakIntensityError)

                self._peakIntensityErrorExists = True

            # by default set systematically peakIntensityWasFixed's value to something not None

            if row._peakIntensityWasFixedExists:

                self._peakIntensityWasFixed = row._peakIntensityWasFixed

                self._peakIntensityWasFixedExists = True

            # by default set systematically astigmPlus's value to something not None

            if row._astigmPlusExists:

                # astigmPlus is a list, make a deep copy
                self.astigmPlus = copy.deepcopy(row.astigmPlus)

                self._astigmPlusExists = True

            # by default set systematically astigmPlusError's value to something not None

            if row._astigmPlusErrorExists:

                # astigmPlusError is a list, make a deep copy
                self.astigmPlusError = copy.deepcopy(row.astigmPlusError)

                self._astigmPlusErrorExists = True

            # by default set systematically astigmMult's value to something not None

            if row._astigmMultExists:

                # astigmMult is a list, make a deep copy
                self.astigmMult = copy.deepcopy(row.astigmMult)

                self._astigmMultExists = True

            # by default set systematically astigmMultError's value to something not None

            if row._astigmMultErrorExists:

                # astigmMultError is a list, make a deep copy
                self.astigmMultError = copy.deepcopy(row.astigmMultError)

                self._astigmMultErrorExists = True

            # by default set systematically illumOffset's value to something not None

            if row._illumOffsetExists:

                # illumOffset is a list, make a deep copy
                self.illumOffset = copy.deepcopy(row.illumOffset)

                self._illumOffsetExists = True

            # by default set systematically illumOffsetError's value to something not None

            if row._illumOffsetErrorExists:

                # illumOffsetError is a list, make a deep copy
                self.illumOffsetError = copy.deepcopy(row.illumOffsetError)

                self._illumOffsetErrorExists = True

            # by default set systematically fitRMS's value to something not None

            if row._fitRMSExists:

                # fitRMS is a list, make a deep copy
                self.fitRMS = copy.deepcopy(row.fitRMS)

                self._fitRMSExists = True

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

        result += Parser.valueToXML("antennaName", self._antennaName)

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.extendedValueToXML(
            "ambientTemperature", self._ambientTemperature
        )

        result += Parser.valueToXML(
            "atmPhaseCorrection", AtmPhaseCorrection.name(self._atmPhaseCorrection)
        )

        result += Parser.valueToXML("focusMethod", FocusMethod.name(self._focusMethod))

        result += Parser.listExtendedValueToXML("frequencyRange", self._frequencyRange)

        result += Parser.listExtendedValueToXML(
            "pointingDirection", self._pointingDirection
        )

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.listValueToXML("wereFixed", self._wereFixed)

        result += Parser.listExtendedValueToXML("offset", self._offset)

        result += Parser.listExtendedValueToXML("offsetError", self._offsetError)

        result += Parser.listValueToXML("offsetWasTied", self._offsetWasTied)

        result += Parser.listValueToXML("reducedChiSquared", self._reducedChiSquared)

        result += Parser.listExtendedValueToXML("position", self._position)

        if self._polarizationsAveragedExists:

            result += Parser.valueToXML(
                "polarizationsAveraged", self._polarizationsAveraged
            )

        if self._focusCurveWidthExists:

            result += Parser.listExtendedValueToXML(
                "focusCurveWidth", self._focusCurveWidth
            )

        if self._focusCurveWidthErrorExists:

            result += Parser.listExtendedValueToXML(
                "focusCurveWidthError", self._focusCurveWidthError
            )

        if self._focusCurveWasFixedExists:

            result += Parser.listValueToXML(
                "focusCurveWasFixed", self._focusCurveWasFixed
            )

        if self._offIntensityExists:

            result += Parser.listExtendedValueToXML("offIntensity", self._offIntensity)

        if self._offIntensityErrorExists:

            result += Parser.listExtendedValueToXML(
                "offIntensityError", self._offIntensityError
            )

        if self._offIntensityWasFixedExists:

            result += Parser.valueToXML(
                "offIntensityWasFixed", self._offIntensityWasFixed
            )

        if self._peakIntensityExists:

            result += Parser.listExtendedValueToXML(
                "peakIntensity", self._peakIntensity
            )

        if self._peakIntensityErrorExists:

            result += Parser.listExtendedValueToXML(
                "peakIntensityError", self._peakIntensityError
            )

        if self._peakIntensityWasFixedExists:

            result += Parser.valueToXML(
                "peakIntensityWasFixed", self._peakIntensityWasFixed
            )

        if self._astigmPlusExists:

            result += Parser.listExtendedValueToXML("astigmPlus", self._astigmPlus)

        if self._astigmPlusErrorExists:

            result += Parser.listExtendedValueToXML(
                "astigmPlusError", self._astigmPlusError
            )

        if self._astigmMultExists:

            result += Parser.listExtendedValueToXML("astigmMult", self._astigmMult)

        if self._astigmMultErrorExists:

            result += Parser.listExtendedValueToXML(
                "astigmMultError", self._astigmMultError
            )

        if self._illumOffsetExists:

            result += Parser.listExtendedValueToXML("illumOffset", self._illumOffset)

        if self._illumOffsetErrorExists:

            result += Parser.listExtendedValueToXML(
                "illumOffsetError", self._illumOffsetError
            )

        if self._fitRMSExists:

            result += Parser.listExtendedValueToXML("fitRMS", self._fitRMS)

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
                "xmlrow is not a string or a minidom.Element", "CalFocusTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalFocusTable")

        # intrinsic attribute values

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data)

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data)

        antennaNameNode = rowdom.getElementsByTagName("antennaName")[0]

        self._antennaName = str(antennaNameNode.firstChild.data)

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data
        )

        ambientTemperatureNode = rowdom.getElementsByTagName("ambientTemperature")[0]

        self._ambientTemperature = Temperature(ambientTemperatureNode.firstChild.data)

        atmPhaseCorrectionNode = rowdom.getElementsByTagName("atmPhaseCorrection")[0]

        self._atmPhaseCorrection = AtmPhaseCorrection.newAtmPhaseCorrection(
            atmPhaseCorrectionNode.firstChild.data
        )

        focusMethodNode = rowdom.getElementsByTagName("focusMethod")[0]

        self._focusMethod = FocusMethod.newFocusMethod(focusMethodNode.firstChild.data)

        frequencyRangeNode = rowdom.getElementsByTagName("frequencyRange")[0]

        frequencyRangeStr = frequencyRangeNode.firstChild.data
        self._frequencyRange = Parser.stringListToLists(
            frequencyRangeStr, Frequency, "CalFocus"
        )

        pointingDirectionNode = rowdom.getElementsByTagName("pointingDirection")[0]

        pointingDirectionStr = pointingDirectionNode.firstChild.data
        self._pointingDirection = Parser.stringListToLists(
            pointingDirectionStr, Angle, "CalFocus"
        )

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data)

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "CalFocus"
        )

        wereFixedNode = rowdom.getElementsByTagName("wereFixed")[0]

        wereFixedStr = wereFixedNode.firstChild.data
        self._wereFixed = Parser.stringListToLists(wereFixedStr, bool, "CalFocus")

        offsetNode = rowdom.getElementsByTagName("offset")[0]

        offsetStr = offsetNode.firstChild.data
        self._offset = Parser.stringListToLists(offsetStr, Length, "CalFocus")

        offsetErrorNode = rowdom.getElementsByTagName("offsetError")[0]

        offsetErrorStr = offsetErrorNode.firstChild.data
        self._offsetError = Parser.stringListToLists(offsetErrorStr, Length, "CalFocus")

        offsetWasTiedNode = rowdom.getElementsByTagName("offsetWasTied")[0]

        offsetWasTiedStr = offsetWasTiedNode.firstChild.data
        self._offsetWasTied = Parser.stringListToLists(
            offsetWasTiedStr, bool, "CalFocus"
        )

        reducedChiSquaredNode = rowdom.getElementsByTagName("reducedChiSquared")[0]

        reducedChiSquaredStr = reducedChiSquaredNode.firstChild.data
        self._reducedChiSquared = Parser.stringListToLists(
            reducedChiSquaredStr, double, "CalFocus"
        )

        positionNode = rowdom.getElementsByTagName("position")[0]

        positionStr = positionNode.firstChild.data
        self._position = Parser.stringListToLists(positionStr, Length, "CalFocus")

        polarizationsAveragedNode = rowdom.getElementsByTagName("polarizationsAveraged")
        if len(polarizationsAveragedNode) > 0:

            self._polarizationsAveraged = bool(
                polarizationsAveragedNode[0].firstChild.data
            )

            self._polarizationsAveragedExists = True

        focusCurveWidthNode = rowdom.getElementsByTagName("focusCurveWidth")
        if len(focusCurveWidthNode) > 0:

            focusCurveWidthStr = focusCurveWidthNode[0].firstChild.data
            self._focusCurveWidth = Parser.stringListToLists(
                focusCurveWidthStr, Length, "CalFocus"
            )

            self._focusCurveWidthExists = True

        focusCurveWidthErrorNode = rowdom.getElementsByTagName("focusCurveWidthError")
        if len(focusCurveWidthErrorNode) > 0:

            focusCurveWidthErrorStr = focusCurveWidthErrorNode[0].firstChild.data
            self._focusCurveWidthError = Parser.stringListToLists(
                focusCurveWidthErrorStr, Length, "CalFocus"
            )

            self._focusCurveWidthErrorExists = True

        focusCurveWasFixedNode = rowdom.getElementsByTagName("focusCurveWasFixed")
        if len(focusCurveWasFixedNode) > 0:

            focusCurveWasFixedStr = focusCurveWasFixedNode[0].firstChild.data
            self._focusCurveWasFixed = Parser.stringListToLists(
                focusCurveWasFixedStr, bool, "CalFocus"
            )

            self._focusCurveWasFixedExists = True

        offIntensityNode = rowdom.getElementsByTagName("offIntensity")
        if len(offIntensityNode) > 0:

            offIntensityStr = offIntensityNode[0].firstChild.data
            self._offIntensity = Parser.stringListToLists(
                offIntensityStr, Temperature, "CalFocus"
            )

            self._offIntensityExists = True

        offIntensityErrorNode = rowdom.getElementsByTagName("offIntensityError")
        if len(offIntensityErrorNode) > 0:

            offIntensityErrorStr = offIntensityErrorNode[0].firstChild.data
            self._offIntensityError = Parser.stringListToLists(
                offIntensityErrorStr, Temperature, "CalFocus"
            )

            self._offIntensityErrorExists = True

        offIntensityWasFixedNode = rowdom.getElementsByTagName("offIntensityWasFixed")
        if len(offIntensityWasFixedNode) > 0:

            self._offIntensityWasFixed = bool(
                offIntensityWasFixedNode[0].firstChild.data
            )

            self._offIntensityWasFixedExists = True

        peakIntensityNode = rowdom.getElementsByTagName("peakIntensity")
        if len(peakIntensityNode) > 0:

            peakIntensityStr = peakIntensityNode[0].firstChild.data
            self._peakIntensity = Parser.stringListToLists(
                peakIntensityStr, Temperature, "CalFocus"
            )

            self._peakIntensityExists = True

        peakIntensityErrorNode = rowdom.getElementsByTagName("peakIntensityError")
        if len(peakIntensityErrorNode) > 0:

            peakIntensityErrorStr = peakIntensityErrorNode[0].firstChild.data
            self._peakIntensityError = Parser.stringListToLists(
                peakIntensityErrorStr, Temperature, "CalFocus"
            )

            self._peakIntensityErrorExists = True

        peakIntensityWasFixedNode = rowdom.getElementsByTagName("peakIntensityWasFixed")
        if len(peakIntensityWasFixedNode) > 0:

            self._peakIntensityWasFixed = bool(
                peakIntensityWasFixedNode[0].firstChild.data
            )

            self._peakIntensityWasFixedExists = True

        astigmPlusNode = rowdom.getElementsByTagName("astigmPlus")
        if len(astigmPlusNode) > 0:

            astigmPlusStr = astigmPlusNode[0].firstChild.data
            self._astigmPlus = Parser.stringListToLists(
                astigmPlusStr, Length, "CalFocus"
            )

            self._astigmPlusExists = True

        astigmPlusErrorNode = rowdom.getElementsByTagName("astigmPlusError")
        if len(astigmPlusErrorNode) > 0:

            astigmPlusErrorStr = astigmPlusErrorNode[0].firstChild.data
            self._astigmPlusError = Parser.stringListToLists(
                astigmPlusErrorStr, Length, "CalFocus"
            )

            self._astigmPlusErrorExists = True

        astigmMultNode = rowdom.getElementsByTagName("astigmMult")
        if len(astigmMultNode) > 0:

            astigmMultStr = astigmMultNode[0].firstChild.data
            self._astigmMult = Parser.stringListToLists(
                astigmMultStr, Length, "CalFocus"
            )

            self._astigmMultExists = True

        astigmMultErrorNode = rowdom.getElementsByTagName("astigmMultError")
        if len(astigmMultErrorNode) > 0:

            astigmMultErrorStr = astigmMultErrorNode[0].firstChild.data
            self._astigmMultError = Parser.stringListToLists(
                astigmMultErrorStr, Length, "CalFocus"
            )

            self._astigmMultErrorExists = True

        illumOffsetNode = rowdom.getElementsByTagName("illumOffset")
        if len(illumOffsetNode) > 0:

            illumOffsetStr = illumOffsetNode[0].firstChild.data
            self._illumOffset = Parser.stringListToLists(
                illumOffsetStr, Length, "CalFocus"
            )

            self._illumOffsetExists = True

        illumOffsetErrorNode = rowdom.getElementsByTagName("illumOffsetError")
        if len(illumOffsetErrorNode) > 0:

            illumOffsetErrorStr = illumOffsetErrorNode[0].firstChild.data
            self._illumOffsetError = Parser.stringListToLists(
                illumOffsetErrorStr, Length, "CalFocus"
            )

            self._illumOffsetErrorExists = True

        fitRMSNode = rowdom.getElementsByTagName("fitRMS")
        if len(fitRMSNode) > 0:

            fitRMSStr = fitRMSNode[0].firstChild.data
            self._fitRMS = Parser.stringListToLists(fitRMSStr, Length, "CalFocus")

            self._fitRMSExists = True

        # extrinsic attribute values

        calDataIdNode = rowdom.getElementsByTagName("calDataId")[0]

        self._calDataId = Tag(calDataIdNode.firstChild.data)

        calReductionIdNode = rowdom.getElementsByTagName("calReductionId")[0]

        self._calReductionId = Tag(calReductionIdNode.firstChild.data)

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

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

    # ===> Attribute ambientTemperature

    _ambientTemperature = Temperature()

    def getAmbientTemperature(self):
        """
        Get ambientTemperature.
        return ambientTemperature as Temperature
        """

        # make sure it is a copy of Temperature
        return Temperature(self._ambientTemperature)

    def setAmbientTemperature(self, ambientTemperature):
        """
        Set ambientTemperature with the specified Temperature value.
        ambientTemperature The Temperature value to which ambientTemperature is to be set.
        The value of ambientTemperature can be anything allowed by the Temperature constructor.

        """

        self._ambientTemperature = Temperature(ambientTemperature)

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


        """

        self._atmPhaseCorrection = AtmPhaseCorrection(atmPhaseCorrection)

    # ===> Attribute focusMethod

    _focusMethod = FocusMethod.from_int(0)

    def getFocusMethod(self):
        """
        Get focusMethod.
        return focusMethod as FocusMethod
        """

        return self._focusMethod

    def setFocusMethod(self, focusMethod):
        """
        Set focusMethod with the specified FocusMethod value.
        focusMethod The FocusMethod value to which focusMethod is to be set.


        """

        self._focusMethod = FocusMethod(focusMethod)

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

    # ===> Attribute pointingDirection

    _pointingDirection = None  # this is a 1D list of Angle

    def getPointingDirection(self):
        """
        Get pointingDirection.
        return pointingDirection as Angle []
        """

        return copy.deepcopy(self._pointingDirection)

    def setPointingDirection(self, pointingDirection):
        """
        Set pointingDirection with the specified Angle []  value.
        pointingDirection The Angle []  value to which pointingDirection is to be set.
        The value of pointingDirection can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(pointingDirection, list):
            raise ValueError("The value of pointingDirection must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(pointingDirection)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of pointingDirection is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(pointingDirection, Angle):
                raise ValueError(
                    "type of the first value in pointingDirection is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._pointingDirection = copy.deepcopy(pointingDirection)
        except Exception as exc:
            raise ValueError("Invalid pointingDirection : " + str(exc))

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

    # ===> Attribute wereFixed

    _wereFixed = None  # this is a 1D list of bool

    def getWereFixed(self):
        """
        Get wereFixed.
        return wereFixed as bool []
        """

        return copy.deepcopy(self._wereFixed)

    def setWereFixed(self, wereFixed):
        """
        Set wereFixed with the specified bool []  value.
        wereFixed The bool []  value to which wereFixed is to be set.


        """

        # value must be a list
        if not isinstance(wereFixed, list):
            raise ValueError("The value of wereFixed must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(wereFixed)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of wereFixed is not correct")

            # the type of the values in the list must be bool
            # note : this only checks the first value found
            if not Parser.checkListType(wereFixed, bool):
                raise ValueError(
                    "type of the first value in wereFixed is not bool as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._wereFixed = copy.deepcopy(wereFixed)
        except Exception as exc:
            raise ValueError("Invalid wereFixed : " + str(exc))

    # ===> Attribute offset

    _offset = None  # this is a 2D list of Length

    def getOffset(self):
        """
        Get offset.
        return offset as Length []  []
        """

        return copy.deepcopy(self._offset)

    def setOffset(self, offset):
        """
        Set offset with the specified Length []  []  value.
        offset The Length []  []  value to which offset is to be set.
        The value of offset can be anything allowed by the Length []  []  constructor.

        """

        # value must be a list
        if not isinstance(offset, list):
            raise ValueError("The value of offset must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(offset)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of offset is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(offset, Length):
                raise ValueError(
                    "type of the first value in offset is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._offset = copy.deepcopy(offset)
        except Exception as exc:
            raise ValueError("Invalid offset : " + str(exc))

    # ===> Attribute offsetError

    _offsetError = None  # this is a 2D list of Length

    def getOffsetError(self):
        """
        Get offsetError.
        return offsetError as Length []  []
        """

        return copy.deepcopy(self._offsetError)

    def setOffsetError(self, offsetError):
        """
        Set offsetError with the specified Length []  []  value.
        offsetError The Length []  []  value to which offsetError is to be set.
        The value of offsetError can be anything allowed by the Length []  []  constructor.

        """

        # value must be a list
        if not isinstance(offsetError, list):
            raise ValueError("The value of offsetError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(offsetError)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of offsetError is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(offsetError, Length):
                raise ValueError(
                    "type of the first value in offsetError is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._offsetError = copy.deepcopy(offsetError)
        except Exception as exc:
            raise ValueError("Invalid offsetError : " + str(exc))

    # ===> Attribute offsetWasTied

    _offsetWasTied = None  # this is a 2D list of bool

    def getOffsetWasTied(self):
        """
        Get offsetWasTied.
        return offsetWasTied as bool []  []
        """

        return copy.deepcopy(self._offsetWasTied)

    def setOffsetWasTied(self, offsetWasTied):
        """
        Set offsetWasTied with the specified bool []  []  value.
        offsetWasTied The bool []  []  value to which offsetWasTied is to be set.


        """

        # value must be a list
        if not isinstance(offsetWasTied, list):
            raise ValueError("The value of offsetWasTied must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(offsetWasTied)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of offsetWasTied is not correct")

            # the type of the values in the list must be bool
            # note : this only checks the first value found
            if not Parser.checkListType(offsetWasTied, bool):
                raise ValueError(
                    "type of the first value in offsetWasTied is not bool as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._offsetWasTied = copy.deepcopy(offsetWasTied)
        except Exception as exc:
            raise ValueError("Invalid offsetWasTied : " + str(exc))

    # ===> Attribute reducedChiSquared

    _reducedChiSquared = None  # this is a 2D list of double

    def getReducedChiSquared(self):
        """
        Get reducedChiSquared.
        return reducedChiSquared as double []  []
        """

        return copy.deepcopy(self._reducedChiSquared)

    def setReducedChiSquared(self, reducedChiSquared):
        """
        Set reducedChiSquared with the specified double []  []  value.
        reducedChiSquared The double []  []  value to which reducedChiSquared is to be set.


        """

        # value must be a list
        if not isinstance(reducedChiSquared, list):
            raise ValueError("The value of reducedChiSquared must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(reducedChiSquared)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of reducedChiSquared is not correct")

            # the type of the values in the list must be double
            # note : this only checks the first value found
            if not Parser.checkListType(reducedChiSquared, double):
                raise ValueError(
                    "type of the first value in reducedChiSquared is not double as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._reducedChiSquared = copy.deepcopy(reducedChiSquared)
        except Exception as exc:
            raise ValueError("Invalid reducedChiSquared : " + str(exc))

    # ===> Attribute position

    _position = None  # this is a 2D list of Length

    def getPosition(self):
        """
        Get position.
        return position as Length []  []
        """

        return copy.deepcopy(self._position)

    def setPosition(self, position):
        """
        Set position with the specified Length []  []  value.
        position The Length []  []  value to which position is to be set.
        The value of position can be anything allowed by the Length []  []  constructor.

        """

        # value must be a list
        if not isinstance(position, list):
            raise ValueError("The value of position must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(position)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of position is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(position, Length):
                raise ValueError(
                    "type of the first value in position is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._position = copy.deepcopy(position)
        except Exception as exc:
            raise ValueError("Invalid position : " + str(exc))

    # ===> Attribute polarizationsAveraged, which is optional
    _polarizationsAveragedExists = False

    _polarizationsAveraged = None

    def isPolarizationsAveragedExists(self):
        """
        The attribute polarizationsAveraged is optional. Return True if this attribute exists.
        return True if and only if the polarizationsAveraged attribute exists.
        """
        return self._polarizationsAveragedExists

    def getPolarizationsAveraged(self):
        """
        Get polarizationsAveraged, which is optional.
        return polarizationsAveraged as bool
        raises ValueError If polarizationsAveraged does not exist.
        """
        if not self._polarizationsAveragedExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + polarizationsAveraged
                + " attribute in table CalFocus does not exist!"
            )

        return self._polarizationsAveraged

    def setPolarizationsAveraged(self, polarizationsAveraged):
        """
        Set polarizationsAveraged with the specified bool value.
        polarizationsAveraged The bool value to which polarizationsAveraged is to be set.


        """

        self._polarizationsAveraged = bool(polarizationsAveraged)

        self._polarizationsAveragedExists = True

    def clearPolarizationsAveraged(self):
        """
        Mark polarizationsAveraged, which is an optional field, as non-existent.
        """
        self._polarizationsAveragedExists = False

    # ===> Attribute focusCurveWidth, which is optional
    _focusCurveWidthExists = False

    _focusCurveWidth = None  # this is a 2D list of Length

    def isFocusCurveWidthExists(self):
        """
        The attribute focusCurveWidth is optional. Return True if this attribute exists.
        return True if and only if the focusCurveWidth attribute exists.
        """
        return self._focusCurveWidthExists

    def getFocusCurveWidth(self):
        """
        Get focusCurveWidth, which is optional.
        return focusCurveWidth as Length []  []
        raises ValueError If focusCurveWidth does not exist.
        """
        if not self._focusCurveWidthExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + focusCurveWidth
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._focusCurveWidth)

    def setFocusCurveWidth(self, focusCurveWidth):
        """
        Set focusCurveWidth with the specified Length []  []  value.
        focusCurveWidth The Length []  []  value to which focusCurveWidth is to be set.
        The value of focusCurveWidth can be anything allowed by the Length []  []  constructor.

        """

        # value must be a list
        if not isinstance(focusCurveWidth, list):
            raise ValueError("The value of focusCurveWidth must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(focusCurveWidth)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of focusCurveWidth is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(focusCurveWidth, Length):
                raise ValueError(
                    "type of the first value in focusCurveWidth is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._focusCurveWidth = copy.deepcopy(focusCurveWidth)
        except Exception as exc:
            raise ValueError("Invalid focusCurveWidth : " + str(exc))

        self._focusCurveWidthExists = True

    def clearFocusCurveWidth(self):
        """
        Mark focusCurveWidth, which is an optional field, as non-existent.
        """
        self._focusCurveWidthExists = False

    # ===> Attribute focusCurveWidthError, which is optional
    _focusCurveWidthErrorExists = False

    _focusCurveWidthError = None  # this is a 2D list of Length

    def isFocusCurveWidthErrorExists(self):
        """
        The attribute focusCurveWidthError is optional. Return True if this attribute exists.
        return True if and only if the focusCurveWidthError attribute exists.
        """
        return self._focusCurveWidthErrorExists

    def getFocusCurveWidthError(self):
        """
        Get focusCurveWidthError, which is optional.
        return focusCurveWidthError as Length []  []
        raises ValueError If focusCurveWidthError does not exist.
        """
        if not self._focusCurveWidthErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + focusCurveWidthError
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._focusCurveWidthError)

    def setFocusCurveWidthError(self, focusCurveWidthError):
        """
        Set focusCurveWidthError with the specified Length []  []  value.
        focusCurveWidthError The Length []  []  value to which focusCurveWidthError is to be set.
        The value of focusCurveWidthError can be anything allowed by the Length []  []  constructor.

        """

        # value must be a list
        if not isinstance(focusCurveWidthError, list):
            raise ValueError("The value of focusCurveWidthError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(focusCurveWidthError)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of focusCurveWidthError is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(focusCurveWidthError, Length):
                raise ValueError(
                    "type of the first value in focusCurveWidthError is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._focusCurveWidthError = copy.deepcopy(focusCurveWidthError)
        except Exception as exc:
            raise ValueError("Invalid focusCurveWidthError : " + str(exc))

        self._focusCurveWidthErrorExists = True

    def clearFocusCurveWidthError(self):
        """
        Mark focusCurveWidthError, which is an optional field, as non-existent.
        """
        self._focusCurveWidthErrorExists = False

    # ===> Attribute focusCurveWasFixed, which is optional
    _focusCurveWasFixedExists = False

    _focusCurveWasFixed = None  # this is a 1D list of bool

    def isFocusCurveWasFixedExists(self):
        """
        The attribute focusCurveWasFixed is optional. Return True if this attribute exists.
        return True if and only if the focusCurveWasFixed attribute exists.
        """
        return self._focusCurveWasFixedExists

    def getFocusCurveWasFixed(self):
        """
        Get focusCurveWasFixed, which is optional.
        return focusCurveWasFixed as bool []
        raises ValueError If focusCurveWasFixed does not exist.
        """
        if not self._focusCurveWasFixedExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + focusCurveWasFixed
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._focusCurveWasFixed)

    def setFocusCurveWasFixed(self, focusCurveWasFixed):
        """
        Set focusCurveWasFixed with the specified bool []  value.
        focusCurveWasFixed The bool []  value to which focusCurveWasFixed is to be set.


        """

        # value must be a list
        if not isinstance(focusCurveWasFixed, list):
            raise ValueError("The value of focusCurveWasFixed must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(focusCurveWasFixed)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of focusCurveWasFixed is not correct")

            # the type of the values in the list must be bool
            # note : this only checks the first value found
            if not Parser.checkListType(focusCurveWasFixed, bool):
                raise ValueError(
                    "type of the first value in focusCurveWasFixed is not bool as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._focusCurveWasFixed = copy.deepcopy(focusCurveWasFixed)
        except Exception as exc:
            raise ValueError("Invalid focusCurveWasFixed : " + str(exc))

        self._focusCurveWasFixedExists = True

    def clearFocusCurveWasFixed(self):
        """
        Mark focusCurveWasFixed, which is an optional field, as non-existent.
        """
        self._focusCurveWasFixedExists = False

    # ===> Attribute offIntensity, which is optional
    _offIntensityExists = False

    _offIntensity = None  # this is a 1D list of Temperature

    def isOffIntensityExists(self):
        """
        The attribute offIntensity is optional. Return True if this attribute exists.
        return True if and only if the offIntensity attribute exists.
        """
        return self._offIntensityExists

    def getOffIntensity(self):
        """
        Get offIntensity, which is optional.
        return offIntensity as Temperature []
        raises ValueError If offIntensity does not exist.
        """
        if not self._offIntensityExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + offIntensity
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._offIntensity)

    def setOffIntensity(self, offIntensity):
        """
        Set offIntensity with the specified Temperature []  value.
        offIntensity The Temperature []  value to which offIntensity is to be set.
        The value of offIntensity can be anything allowed by the Temperature []  constructor.

        """

        # value must be a list
        if not isinstance(offIntensity, list):
            raise ValueError("The value of offIntensity must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(offIntensity)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of offIntensity is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(offIntensity, Temperature):
                raise ValueError(
                    "type of the first value in offIntensity is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._offIntensity = copy.deepcopy(offIntensity)
        except Exception as exc:
            raise ValueError("Invalid offIntensity : " + str(exc))

        self._offIntensityExists = True

    def clearOffIntensity(self):
        """
        Mark offIntensity, which is an optional field, as non-existent.
        """
        self._offIntensityExists = False

    # ===> Attribute offIntensityError, which is optional
    _offIntensityErrorExists = False

    _offIntensityError = None  # this is a 1D list of Temperature

    def isOffIntensityErrorExists(self):
        """
        The attribute offIntensityError is optional. Return True if this attribute exists.
        return True if and only if the offIntensityError attribute exists.
        """
        return self._offIntensityErrorExists

    def getOffIntensityError(self):
        """
        Get offIntensityError, which is optional.
        return offIntensityError as Temperature []
        raises ValueError If offIntensityError does not exist.
        """
        if not self._offIntensityErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + offIntensityError
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._offIntensityError)

    def setOffIntensityError(self, offIntensityError):
        """
        Set offIntensityError with the specified Temperature []  value.
        offIntensityError The Temperature []  value to which offIntensityError is to be set.
        The value of offIntensityError can be anything allowed by the Temperature []  constructor.

        """

        # value must be a list
        if not isinstance(offIntensityError, list):
            raise ValueError("The value of offIntensityError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(offIntensityError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of offIntensityError is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(offIntensityError, Temperature):
                raise ValueError(
                    "type of the first value in offIntensityError is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._offIntensityError = copy.deepcopy(offIntensityError)
        except Exception as exc:
            raise ValueError("Invalid offIntensityError : " + str(exc))

        self._offIntensityErrorExists = True

    def clearOffIntensityError(self):
        """
        Mark offIntensityError, which is an optional field, as non-existent.
        """
        self._offIntensityErrorExists = False

    # ===> Attribute offIntensityWasFixed, which is optional
    _offIntensityWasFixedExists = False

    _offIntensityWasFixed = None

    def isOffIntensityWasFixedExists(self):
        """
        The attribute offIntensityWasFixed is optional. Return True if this attribute exists.
        return True if and only if the offIntensityWasFixed attribute exists.
        """
        return self._offIntensityWasFixedExists

    def getOffIntensityWasFixed(self):
        """
        Get offIntensityWasFixed, which is optional.
        return offIntensityWasFixed as bool
        raises ValueError If offIntensityWasFixed does not exist.
        """
        if not self._offIntensityWasFixedExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + offIntensityWasFixed
                + " attribute in table CalFocus does not exist!"
            )

        return self._offIntensityWasFixed

    def setOffIntensityWasFixed(self, offIntensityWasFixed):
        """
        Set offIntensityWasFixed with the specified bool value.
        offIntensityWasFixed The bool value to which offIntensityWasFixed is to be set.


        """

        self._offIntensityWasFixed = bool(offIntensityWasFixed)

        self._offIntensityWasFixedExists = True

    def clearOffIntensityWasFixed(self):
        """
        Mark offIntensityWasFixed, which is an optional field, as non-existent.
        """
        self._offIntensityWasFixedExists = False

    # ===> Attribute peakIntensity, which is optional
    _peakIntensityExists = False

    _peakIntensity = None  # this is a 1D list of Temperature

    def isPeakIntensityExists(self):
        """
        The attribute peakIntensity is optional. Return True if this attribute exists.
        return True if and only if the peakIntensity attribute exists.
        """
        return self._peakIntensityExists

    def getPeakIntensity(self):
        """
        Get peakIntensity, which is optional.
        return peakIntensity as Temperature []
        raises ValueError If peakIntensity does not exist.
        """
        if not self._peakIntensityExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + peakIntensity
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._peakIntensity)

    def setPeakIntensity(self, peakIntensity):
        """
        Set peakIntensity with the specified Temperature []  value.
        peakIntensity The Temperature []  value to which peakIntensity is to be set.
        The value of peakIntensity can be anything allowed by the Temperature []  constructor.

        """

        # value must be a list
        if not isinstance(peakIntensity, list):
            raise ValueError("The value of peakIntensity must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(peakIntensity)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of peakIntensity is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(peakIntensity, Temperature):
                raise ValueError(
                    "type of the first value in peakIntensity is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._peakIntensity = copy.deepcopy(peakIntensity)
        except Exception as exc:
            raise ValueError("Invalid peakIntensity : " + str(exc))

        self._peakIntensityExists = True

    def clearPeakIntensity(self):
        """
        Mark peakIntensity, which is an optional field, as non-existent.
        """
        self._peakIntensityExists = False

    # ===> Attribute peakIntensityError, which is optional
    _peakIntensityErrorExists = False

    _peakIntensityError = None  # this is a 1D list of Temperature

    def isPeakIntensityErrorExists(self):
        """
        The attribute peakIntensityError is optional. Return True if this attribute exists.
        return True if and only if the peakIntensityError attribute exists.
        """
        return self._peakIntensityErrorExists

    def getPeakIntensityError(self):
        """
        Get peakIntensityError, which is optional.
        return peakIntensityError as Temperature []
        raises ValueError If peakIntensityError does not exist.
        """
        if not self._peakIntensityErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + peakIntensityError
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._peakIntensityError)

    def setPeakIntensityError(self, peakIntensityError):
        """
        Set peakIntensityError with the specified Temperature []  value.
        peakIntensityError The Temperature []  value to which peakIntensityError is to be set.
        The value of peakIntensityError can be anything allowed by the Temperature []  constructor.

        """

        # value must be a list
        if not isinstance(peakIntensityError, list):
            raise ValueError("The value of peakIntensityError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(peakIntensityError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of peakIntensityError is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(peakIntensityError, Temperature):
                raise ValueError(
                    "type of the first value in peakIntensityError is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._peakIntensityError = copy.deepcopy(peakIntensityError)
        except Exception as exc:
            raise ValueError("Invalid peakIntensityError : " + str(exc))

        self._peakIntensityErrorExists = True

    def clearPeakIntensityError(self):
        """
        Mark peakIntensityError, which is an optional field, as non-existent.
        """
        self._peakIntensityErrorExists = False

    # ===> Attribute peakIntensityWasFixed, which is optional
    _peakIntensityWasFixedExists = False

    _peakIntensityWasFixed = None

    def isPeakIntensityWasFixedExists(self):
        """
        The attribute peakIntensityWasFixed is optional. Return True if this attribute exists.
        return True if and only if the peakIntensityWasFixed attribute exists.
        """
        return self._peakIntensityWasFixedExists

    def getPeakIntensityWasFixed(self):
        """
        Get peakIntensityWasFixed, which is optional.
        return peakIntensityWasFixed as bool
        raises ValueError If peakIntensityWasFixed does not exist.
        """
        if not self._peakIntensityWasFixedExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + peakIntensityWasFixed
                + " attribute in table CalFocus does not exist!"
            )

        return self._peakIntensityWasFixed

    def setPeakIntensityWasFixed(self, peakIntensityWasFixed):
        """
        Set peakIntensityWasFixed with the specified bool value.
        peakIntensityWasFixed The bool value to which peakIntensityWasFixed is to be set.


        """

        self._peakIntensityWasFixed = bool(peakIntensityWasFixed)

        self._peakIntensityWasFixedExists = True

    def clearPeakIntensityWasFixed(self):
        """
        Mark peakIntensityWasFixed, which is an optional field, as non-existent.
        """
        self._peakIntensityWasFixedExists = False

    # ===> Attribute astigmPlus, which is optional
    _astigmPlusExists = False

    _astigmPlus = None  # this is a 1D list of Length

    def isAstigmPlusExists(self):
        """
        The attribute astigmPlus is optional. Return True if this attribute exists.
        return True if and only if the astigmPlus attribute exists.
        """
        return self._astigmPlusExists

    def getAstigmPlus(self):
        """
        Get astigmPlus, which is optional.
        return astigmPlus as Length []
        raises ValueError If astigmPlus does not exist.
        """
        if not self._astigmPlusExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + astigmPlus
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._astigmPlus)

    def setAstigmPlus(self, astigmPlus):
        """
        Set astigmPlus with the specified Length []  value.
        astigmPlus The Length []  value to which astigmPlus is to be set.
        The value of astigmPlus can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(astigmPlus, list):
            raise ValueError("The value of astigmPlus must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(astigmPlus)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of astigmPlus is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(astigmPlus, Length):
                raise ValueError(
                    "type of the first value in astigmPlus is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._astigmPlus = copy.deepcopy(astigmPlus)
        except Exception as exc:
            raise ValueError("Invalid astigmPlus : " + str(exc))

        self._astigmPlusExists = True

    def clearAstigmPlus(self):
        """
        Mark astigmPlus, which is an optional field, as non-existent.
        """
        self._astigmPlusExists = False

    # ===> Attribute astigmPlusError, which is optional
    _astigmPlusErrorExists = False

    _astigmPlusError = None  # this is a 1D list of Length

    def isAstigmPlusErrorExists(self):
        """
        The attribute astigmPlusError is optional. Return True if this attribute exists.
        return True if and only if the astigmPlusError attribute exists.
        """
        return self._astigmPlusErrorExists

    def getAstigmPlusError(self):
        """
        Get astigmPlusError, which is optional.
        return astigmPlusError as Length []
        raises ValueError If astigmPlusError does not exist.
        """
        if not self._astigmPlusErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + astigmPlusError
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._astigmPlusError)

    def setAstigmPlusError(self, astigmPlusError):
        """
        Set astigmPlusError with the specified Length []  value.
        astigmPlusError The Length []  value to which astigmPlusError is to be set.
        The value of astigmPlusError can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(astigmPlusError, list):
            raise ValueError("The value of astigmPlusError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(astigmPlusError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of astigmPlusError is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(astigmPlusError, Length):
                raise ValueError(
                    "type of the first value in astigmPlusError is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._astigmPlusError = copy.deepcopy(astigmPlusError)
        except Exception as exc:
            raise ValueError("Invalid astigmPlusError : " + str(exc))

        self._astigmPlusErrorExists = True

    def clearAstigmPlusError(self):
        """
        Mark astigmPlusError, which is an optional field, as non-existent.
        """
        self._astigmPlusErrorExists = False

    # ===> Attribute astigmMult, which is optional
    _astigmMultExists = False

    _astigmMult = None  # this is a 1D list of Length

    def isAstigmMultExists(self):
        """
        The attribute astigmMult is optional. Return True if this attribute exists.
        return True if and only if the astigmMult attribute exists.
        """
        return self._astigmMultExists

    def getAstigmMult(self):
        """
        Get astigmMult, which is optional.
        return astigmMult as Length []
        raises ValueError If astigmMult does not exist.
        """
        if not self._astigmMultExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + astigmMult
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._astigmMult)

    def setAstigmMult(self, astigmMult):
        """
        Set astigmMult with the specified Length []  value.
        astigmMult The Length []  value to which astigmMult is to be set.
        The value of astigmMult can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(astigmMult, list):
            raise ValueError("The value of astigmMult must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(astigmMult)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of astigmMult is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(astigmMult, Length):
                raise ValueError(
                    "type of the first value in astigmMult is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._astigmMult = copy.deepcopy(astigmMult)
        except Exception as exc:
            raise ValueError("Invalid astigmMult : " + str(exc))

        self._astigmMultExists = True

    def clearAstigmMult(self):
        """
        Mark astigmMult, which is an optional field, as non-existent.
        """
        self._astigmMultExists = False

    # ===> Attribute astigmMultError, which is optional
    _astigmMultErrorExists = False

    _astigmMultError = None  # this is a 1D list of Length

    def isAstigmMultErrorExists(self):
        """
        The attribute astigmMultError is optional. Return True if this attribute exists.
        return True if and only if the astigmMultError attribute exists.
        """
        return self._astigmMultErrorExists

    def getAstigmMultError(self):
        """
        Get astigmMultError, which is optional.
        return astigmMultError as Length []
        raises ValueError If astigmMultError does not exist.
        """
        if not self._astigmMultErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + astigmMultError
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._astigmMultError)

    def setAstigmMultError(self, astigmMultError):
        """
        Set astigmMultError with the specified Length []  value.
        astigmMultError The Length []  value to which astigmMultError is to be set.
        The value of astigmMultError can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(astigmMultError, list):
            raise ValueError("The value of astigmMultError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(astigmMultError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of astigmMultError is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(astigmMultError, Length):
                raise ValueError(
                    "type of the first value in astigmMultError is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._astigmMultError = copy.deepcopy(astigmMultError)
        except Exception as exc:
            raise ValueError("Invalid astigmMultError : " + str(exc))

        self._astigmMultErrorExists = True

    def clearAstigmMultError(self):
        """
        Mark astigmMultError, which is an optional field, as non-existent.
        """
        self._astigmMultErrorExists = False

    # ===> Attribute illumOffset, which is optional
    _illumOffsetExists = False

    _illumOffset = None  # this is a 2D list of Length

    def isIllumOffsetExists(self):
        """
        The attribute illumOffset is optional. Return True if this attribute exists.
        return True if and only if the illumOffset attribute exists.
        """
        return self._illumOffsetExists

    def getIllumOffset(self):
        """
        Get illumOffset, which is optional.
        return illumOffset as Length []  []
        raises ValueError If illumOffset does not exist.
        """
        if not self._illumOffsetExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + illumOffset
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._illumOffset)

    def setIllumOffset(self, illumOffset):
        """
        Set illumOffset with the specified Length []  []  value.
        illumOffset The Length []  []  value to which illumOffset is to be set.
        The value of illumOffset can be anything allowed by the Length []  []  constructor.

        """

        # value must be a list
        if not isinstance(illumOffset, list):
            raise ValueError("The value of illumOffset must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(illumOffset)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of illumOffset is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(illumOffset, Length):
                raise ValueError(
                    "type of the first value in illumOffset is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._illumOffset = copy.deepcopy(illumOffset)
        except Exception as exc:
            raise ValueError("Invalid illumOffset : " + str(exc))

        self._illumOffsetExists = True

    def clearIllumOffset(self):
        """
        Mark illumOffset, which is an optional field, as non-existent.
        """
        self._illumOffsetExists = False

    # ===> Attribute illumOffsetError, which is optional
    _illumOffsetErrorExists = False

    _illumOffsetError = None  # this is a 2D list of Length

    def isIllumOffsetErrorExists(self):
        """
        The attribute illumOffsetError is optional. Return True if this attribute exists.
        return True if and only if the illumOffsetError attribute exists.
        """
        return self._illumOffsetErrorExists

    def getIllumOffsetError(self):
        """
        Get illumOffsetError, which is optional.
        return illumOffsetError as Length []  []
        raises ValueError If illumOffsetError does not exist.
        """
        if not self._illumOffsetErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + illumOffsetError
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._illumOffsetError)

    def setIllumOffsetError(self, illumOffsetError):
        """
        Set illumOffsetError with the specified Length []  []  value.
        illumOffsetError The Length []  []  value to which illumOffsetError is to be set.
        The value of illumOffsetError can be anything allowed by the Length []  []  constructor.

        """

        # value must be a list
        if not isinstance(illumOffsetError, list):
            raise ValueError("The value of illumOffsetError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(illumOffsetError)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of illumOffsetError is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(illumOffsetError, Length):
                raise ValueError(
                    "type of the first value in illumOffsetError is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._illumOffsetError = copy.deepcopy(illumOffsetError)
        except Exception as exc:
            raise ValueError("Invalid illumOffsetError : " + str(exc))

        self._illumOffsetErrorExists = True

    def clearIllumOffsetError(self):
        """
        Mark illumOffsetError, which is an optional field, as non-existent.
        """
        self._illumOffsetErrorExists = False

    # ===> Attribute fitRMS, which is optional
    _fitRMSExists = False

    _fitRMS = None  # this is a 1D list of Length

    def isFitRMSExists(self):
        """
        The attribute fitRMS is optional. Return True if this attribute exists.
        return True if and only if the fitRMS attribute exists.
        """
        return self._fitRMSExists

    def getFitRMS(self):
        """
        Get fitRMS, which is optional.
        return fitRMS as Length []
        raises ValueError If fitRMS does not exist.
        """
        if not self._fitRMSExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + fitRMS
                + " attribute in table CalFocus does not exist!"
            )

        return copy.deepcopy(self._fitRMS)

    def setFitRMS(self, fitRMS):
        """
        Set fitRMS with the specified Length []  value.
        fitRMS The Length []  value to which fitRMS is to be set.
        The value of fitRMS can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(fitRMS, list):
            raise ValueError("The value of fitRMS must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(fitRMS)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of fitRMS is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(fitRMS, Length):
                raise ValueError(
                    "type of the first value in fitRMS is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._fitRMS = copy.deepcopy(fitRMS)
        except Exception as exc:
            raise ValueError("Invalid fitRMS : " + str(exc))

        self._fitRMSExists = True

    def clearFitRMS(self):
        """
        Mark fitRMS, which is an optional field, as non-existent.
        """
        self._fitRMSExists = False

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
        ambientTemperature,
        atmPhaseCorrection,
        focusMethod,
        frequencyRange,
        pointingDirection,
        numReceptor,
        polarizationTypes,
        wereFixed,
        offset,
        offsetError,
        offsetWasTied,
        reducedChiSquared,
        position,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalFocusRow with
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

        # ambientTemperature is a Temperature, compare using the almostEquals method.
        if not self._ambientTemperature.almostEquals(
            ambientTemperature, self.getTable().getAmbientTemperatureEqTolerance()
        ):
            return False

        # atmPhaseCorrection is a AtmPhaseCorrection, compare using the == operator on the getValue() output
        if not (self._atmPhaseCorrection.getValue() == atmPhaseCorrection.getValue()):
            return False

        # focusMethod is a FocusMethod, compare using the == operator on the getValue() output
        if not (self._focusMethod.getValue() == focusMethod.getValue()):
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
        if len(self._pointingDirection) != len(pointingDirection):
            return False
        for indx in range(len(pointingDirection)):

            # pointingDirection is a list of Angle, compare using the almostEquals method.
            if not self._pointingDirection[indx].almostEquals(
                pointingDirection[indx],
                self.getTable().getPointingDirectionEqTolerance(),
            ):
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

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._wereFixed) != len(wereFixed):
            return False
        for indx in range(len(wereFixed)):

            # wereFixed is a list of bool, compare using == operator.
            if not (self._wereFixed[indx] == wereFixed[indx]):
                return False

        # We compare two 2D arrays (lists)
        if offset is not None:
            if self._offset is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            offset_dims = Parser.getListDims(offset)
            this_offset_dims = Parser.getListDims(self._offset)
            if offset_dims != this_offset_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(offset_dims[0]):
                for j in range(offset_dims[0]):

                    # offset is a Length, compare using the almostEquals method.
                    if not (
                        self._offset[i][j].almostEquals(
                            offset[i][j], this.getTable().getOffsetEqTolerance()
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists)
        if offsetError is not None:
            if self._offsetError is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            offsetError_dims = Parser.getListDims(offsetError)
            this_offsetError_dims = Parser.getListDims(self._offsetError)
            if offsetError_dims != this_offsetError_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(offsetError_dims[0]):
                for j in range(offsetError_dims[0]):

                    # offsetError is a Length, compare using the almostEquals method.
                    if not (
                        self._offsetError[i][j].almostEquals(
                            offsetError[i][j],
                            this.getTable().getOffsetErrorEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists)
        if offsetWasTied is not None:
            if self._offsetWasTied is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            offsetWasTied_dims = Parser.getListDims(offsetWasTied)
            this_offsetWasTied_dims = Parser.getListDims(self._offsetWasTied)
            if offsetWasTied_dims != this_offsetWasTied_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(offsetWasTied_dims[0]):
                for j in range(offsetWasTied_dims[0]):

                    # offsetWasTied is an array of bool, compare using == operator.
                    if not (self._offsetWasTied[i][j] == offsetWasTied[i][j]):
                        return False

        # We compare two 2D arrays (lists)
        if reducedChiSquared is not None:
            if self._reducedChiSquared is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            reducedChiSquared_dims = Parser.getListDims(reducedChiSquared)
            this_reducedChiSquared_dims = Parser.getListDims(self._reducedChiSquared)
            if reducedChiSquared_dims != this_reducedChiSquared_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(reducedChiSquared_dims[0]):
                for j in range(reducedChiSquared_dims[0]):

                    # reducedChiSquared is an array of double, compare using == operator.
                    if not (self._reducedChiSquared[i][j] == reducedChiSquared[i][j]):
                        return False

        # We compare two 2D arrays (lists)
        if position is not None:
            if self._position is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            position_dims = Parser.getListDims(position)
            this_position_dims = Parser.getListDims(self._position)
            if position_dims != this_position_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(position_dims[0]):
                for j in range(position_dims[0]):

                    # position is a Length, compare using the almostEquals method.
                    if not (
                        self._position[i][j].almostEquals(
                            position[i][j], this.getTable().getPositionEqTolerance()
                        )
                    ):
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
            otherRow.getAmbientTemperature(),
            otherRow.getAtmPhaseCorrection(),
            otherRow.getFocusMethod(),
            otherRow.getFrequencyRange(),
            otherRow.getPointingDirection(),
            otherRow.getNumReceptor(),
            otherRow.getPolarizationTypes(),
            otherRow.getWereFixed(),
            otherRow.getOffset(),
            otherRow.getOffsetError(),
            otherRow.getOffsetWasTied(),
            otherRow.getReducedChiSquared(),
            otherRow.getPosition(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        ambientTemperature,
        atmPhaseCorrection,
        focusMethod,
        frequencyRange,
        pointingDirection,
        numReceptor,
        polarizationTypes,
        wereFixed,
        offset,
        offsetError,
        offsetWasTied,
        reducedChiSquared,
        position,
    ):

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # ambientTemperature is a Temperature, compare using the almostEquals method.
        if not self._ambientTemperature.almostEquals(
            ambientTemperature, self.getTable().getAmbientTemperatureEqTolerance()
        ):
            return False

        # atmPhaseCorrection is a AtmPhaseCorrection, compare using the == operator on the getValue() output
        if not (self._atmPhaseCorrection.getValue() == atmPhaseCorrection.getValue()):
            return False

        # focusMethod is a FocusMethod, compare using the == operator on the getValue() output
        if not (self._focusMethod.getValue() == focusMethod.getValue()):
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
        if len(self._pointingDirection) != len(pointingDirection):
            return False
        for indx in range(len(pointingDirection)):

            # pointingDirection is a list of Angle, compare using the almostEquals method.
            if not self._pointingDirection[indx].almostEquals(
                pointingDirection[indx],
                self.getTable().getPointingDirectionEqTolerance(),
            ):
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

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._wereFixed) != len(wereFixed):
            return False
        for indx in range(len(wereFixed)):

            # wereFixed is a list of bool, compare using == operator.
            if not (self._wereFixed[indx] == wereFixed[indx]):
                return False

        # We compare two 2D arrays (lists)
        if offset is not None:
            if self._offset is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            offset_dims = Parser.getListDims(offset)
            this_offset_dims = Parser.getListDims(self._offset)
            if offset_dims != this_offset_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(offset_dims[0]):
                for j in range(offset_dims[0]):

                    # offset is a Length, compare using the almostEquals method.
                    if not (
                        self._offset[i][j].almostEquals(
                            offset[i][j], this.getTable().getOffsetEqTolerance()
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists)
        if offsetError is not None:
            if self._offsetError is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            offsetError_dims = Parser.getListDims(offsetError)
            this_offsetError_dims = Parser.getListDims(self._offsetError)
            if offsetError_dims != this_offsetError_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(offsetError_dims[0]):
                for j in range(offsetError_dims[0]):

                    # offsetError is a Length, compare using the almostEquals method.
                    if not (
                        self._offsetError[i][j].almostEquals(
                            offsetError[i][j],
                            this.getTable().getOffsetErrorEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists)
        if offsetWasTied is not None:
            if self._offsetWasTied is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            offsetWasTied_dims = Parser.getListDims(offsetWasTied)
            this_offsetWasTied_dims = Parser.getListDims(self._offsetWasTied)
            if offsetWasTied_dims != this_offsetWasTied_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(offsetWasTied_dims[0]):
                for j in range(offsetWasTied_dims[0]):

                    # offsetWasTied is an array of bool, compare using == operator.
                    if not (self._offsetWasTied[i][j] == offsetWasTied[i][j]):
                        return False

        # We compare two 2D arrays (lists)
        if reducedChiSquared is not None:
            if self._reducedChiSquared is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            reducedChiSquared_dims = Parser.getListDims(reducedChiSquared)
            this_reducedChiSquared_dims = Parser.getListDims(self._reducedChiSquared)
            if reducedChiSquared_dims != this_reducedChiSquared_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(reducedChiSquared_dims[0]):
                for j in range(reducedChiSquared_dims[0]):

                    # reducedChiSquared is an array of double, compare using == operator.
                    if not (self._reducedChiSquared[i][j] == reducedChiSquared[i][j]):
                        return False

        # We compare two 2D arrays (lists)
        if position is not None:
            if self._position is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            position_dims = Parser.getListDims(position)
            this_position_dims = Parser.getListDims(self._position)
            if position_dims != this_position_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(position_dims[0]):
                for j in range(position_dims[0]):

                    # position is a Length, compare using the almostEquals method.
                    if not (
                        self._position[i][j].almostEquals(
                            position[i][j], this.getTable().getPositionEqTolerance()
                        )
                    ):
                        return False

        return True
