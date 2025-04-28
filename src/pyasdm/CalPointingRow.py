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
# File CalPointingRow.py
#

import pyasdm.CalPointingTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.AntennaMake import AntennaMake


from pyasdm.enumerations.AtmPhaseCorrection import AtmPhaseCorrection


from pyasdm.enumerations.PointingModelMode import PointingModelMode


from pyasdm.enumerations.PointingMethod import PointingMethod


from pyasdm.enumerations.PolarizationType import PolarizationType


from xml.dom import minidom

import copy


class CalPointingRow:
    """
    The CalPointingRow class is a row of a CalPointingTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalPointingRow.
        When row is None, create an empty row attached to table, which must be a CalPointingTable.
        When row is given, copy those values in to the new row. The row argument must be a CalPointingRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalPointingTable):
            raise ValueError("table must be a CalPointingTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._antennaName = None

        self._receiverBand = ReceiverBand.from_int(0)

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._ambientTemperature = Temperature()

        self._antennaMake = AntennaMake.from_int(0)

        self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)

        self._direction = []  # this is a list of Angle []

        self._frequencyRange = []  # this is a list of Frequency []

        self._pointingModelMode = PointingModelMode.from_int(0)

        self._pointingMethod = PointingMethod.from_int(0)

        self._numReceptor = 0

        self._polarizationTypes = []  # this is a list of PolarizationType []

        self._collOffsetRelative = []  # this is a list of Angle []  []

        self._collOffsetAbsolute = []  # this is a list of Angle []  []

        self._collError = []  # this is a list of Angle []  []

        self._collOffsetTied = []  # this is a list of bool []  []

        self._reducedChiSquared = []  # this is a list of float []

        self._averagedPolarizationsExists = False

        self._averagedPolarizations = None

        self._beamPAExists = False

        self._beamPA = []  # this is a list of Angle []

        self._beamPAErrorExists = False

        self._beamPAError = []  # this is a list of Angle []

        self._beamPAWasFixedExists = False

        self._beamPAWasFixed = None

        self._beamWidthExists = False

        self._beamWidth = []  # this is a list of Angle []  []

        self._beamWidthErrorExists = False

        self._beamWidthError = []  # this is a list of Angle []  []

        self._beamWidthWasFixedExists = False

        self._beamWidthWasFixed = []  # this is a list of bool []

        self._offIntensityExists = False

        self._offIntensity = []  # this is a list of Temperature []

        self._offIntensityErrorExists = False

        self._offIntensityError = []  # this is a list of Temperature []

        self._offIntensityWasFixedExists = False

        self._offIntensityWasFixed = None

        self._peakIntensityExists = False

        self._peakIntensity = []  # this is a list of Temperature []

        self._peakIntensityErrorExists = False

        self._peakIntensityError = []  # this is a list of Temperature []

        self._peakIntensityWasFixedExists = False

        self._peakIntensityWasFixed = None

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalPointingRow):
                raise ValueError("row must be a CalPointingRow")

            # copy constructor

            self._antennaName = row._antennaName

            # We force the attribute of the result to be not None.
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
            if row._antennaMake is None:
                self._antennaMake = AntennaMake.from_int(0)
            else:
                self._antennaMake = AntennaMake(row._antennaMake)

            # We force the attribute of the result to be not None
            if row._atmPhaseCorrection is None:
                self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)
            else:
                self._atmPhaseCorrection = AtmPhaseCorrection(row._atmPhaseCorrection)

            # direction is a  list , make a deep copy
            self._direction = copy.deepcopy(row._direction)

            # frequencyRange is a  list , make a deep copy
            self._frequencyRange = copy.deepcopy(row._frequencyRange)

            # We force the attribute of the result to be not None
            if row._pointingModelMode is None:
                self._pointingModelMode = PointingModelMode.from_int(0)
            else:
                self._pointingModelMode = PointingModelMode(row._pointingModelMode)

            # We force the attribute of the result to be not None
            if row._pointingMethod is None:
                self._pointingMethod = PointingMethod.from_int(0)
            else:
                self._pointingMethod = PointingMethod(row._pointingMethod)

            self._numReceptor = row._numReceptor

            # polarizationTypes is a  list , make a deep copy
            self._polarizationTypes = copy.deepcopy(row._polarizationTypes)

            # collOffsetRelative is a  list , make a deep copy
            self._collOffsetRelative = copy.deepcopy(row._collOffsetRelative)

            # collOffsetAbsolute is a  list , make a deep copy
            self._collOffsetAbsolute = copy.deepcopy(row._collOffsetAbsolute)

            # collError is a  list , make a deep copy
            self._collError = copy.deepcopy(row._collError)

            # collOffsetTied is a  list , make a deep copy
            self._collOffsetTied = copy.deepcopy(row._collOffsetTied)

            # reducedChiSquared is a  list , make a deep copy
            self._reducedChiSquared = copy.deepcopy(row._reducedChiSquared)

            # by default set systematically averagedPolarizations's value to something not None

            if row._averagedPolarizationsExists:

                self._averagedPolarizations = row._averagedPolarizations

                self._averagedPolarizationsExists = True

            # by default set systematically beamPA's value to something not None

            if row._beamPAExists:

                # beamPA is a list, make a deep copy
                self._beamPA = copy.deepcopy(row._beamPA)

                self._beamPAExists = True

            # by default set systematically beamPAError's value to something not None

            if row._beamPAErrorExists:

                # beamPAError is a list, make a deep copy
                self._beamPAError = copy.deepcopy(row._beamPAError)

                self._beamPAErrorExists = True

            # by default set systematically beamPAWasFixed's value to something not None

            if row._beamPAWasFixedExists:

                self._beamPAWasFixed = row._beamPAWasFixed

                self._beamPAWasFixedExists = True

            # by default set systematically beamWidth's value to something not None

            if row._beamWidthExists:

                # beamWidth is a list, make a deep copy
                self._beamWidth = copy.deepcopy(row._beamWidth)

                self._beamWidthExists = True

            # by default set systematically beamWidthError's value to something not None

            if row._beamWidthErrorExists:

                # beamWidthError is a list, make a deep copy
                self._beamWidthError = copy.deepcopy(row._beamWidthError)

                self._beamWidthErrorExists = True

            # by default set systematically beamWidthWasFixed's value to something not None

            if row._beamWidthWasFixedExists:

                # beamWidthWasFixed is a list, make a deep copy
                self._beamWidthWasFixed = copy.deepcopy(row._beamWidthWasFixed)

                self._beamWidthWasFixedExists = True

            # by default set systematically offIntensity's value to something not None

            if row._offIntensityExists:

                # offIntensity is a list, make a deep copy
                self._offIntensity = copy.deepcopy(row._offIntensity)

                self._offIntensityExists = True

            # by default set systematically offIntensityError's value to something not None

            if row._offIntensityErrorExists:

                # offIntensityError is a list, make a deep copy
                self._offIntensityError = copy.deepcopy(row._offIntensityError)

                self._offIntensityErrorExists = True

            # by default set systematically offIntensityWasFixed's value to something not None

            if row._offIntensityWasFixedExists:

                self._offIntensityWasFixed = row._offIntensityWasFixed

                self._offIntensityWasFixedExists = True

            # by default set systematically peakIntensity's value to something not None

            if row._peakIntensityExists:

                # peakIntensity is a list, make a deep copy
                self._peakIntensity = copy.deepcopy(row._peakIntensity)

                self._peakIntensityExists = True

            # by default set systematically peakIntensityError's value to something not None

            if row._peakIntensityErrorExists:

                # peakIntensityError is a list, make a deep copy
                self._peakIntensityError = copy.deepcopy(row._peakIntensityError)

                self._peakIntensityErrorExists = True

            # by default set systematically peakIntensityWasFixed's value to something not None

            if row._peakIntensityWasFixedExists:

                self._peakIntensityWasFixed = row._peakIntensityWasFixed

                self._peakIntensityWasFixedExists = True

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

        result += Parser.extendedValueToXML(
            "ambientTemperature", self._ambientTemperature
        )

        result += Parser.valueToXML("antennaMake", AntennaMake.name(self._antennaMake))

        result += Parser.valueToXML(
            "atmPhaseCorrection", AtmPhaseCorrection.name(self._atmPhaseCorrection)
        )

        result += Parser.listExtendedValueToXML("direction", self._direction)

        result += Parser.listExtendedValueToXML("frequencyRange", self._frequencyRange)

        result += Parser.valueToXML(
            "pointingModelMode", PointingModelMode.name(self._pointingModelMode)
        )

        result += Parser.valueToXML(
            "pointingMethod", PointingMethod.name(self._pointingMethod)
        )

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.listExtendedValueToXML(
            "collOffsetRelative", self._collOffsetRelative
        )

        result += Parser.listExtendedValueToXML(
            "collOffsetAbsolute", self._collOffsetAbsolute
        )

        result += Parser.listExtendedValueToXML("collError", self._collError)

        result += Parser.listValueToXML("collOffsetTied", self._collOffsetTied)

        result += Parser.listValueToXML("reducedChiSquared", self._reducedChiSquared)

        if self._averagedPolarizationsExists:

            result += Parser.valueToXML(
                "averagedPolarizations", self._averagedPolarizations
            )

        if self._beamPAExists:

            result += Parser.listExtendedValueToXML("beamPA", self._beamPA)

        if self._beamPAErrorExists:

            result += Parser.listExtendedValueToXML("beamPAError", self._beamPAError)

        if self._beamPAWasFixedExists:

            result += Parser.valueToXML("beamPAWasFixed", self._beamPAWasFixed)

        if self._beamWidthExists:

            result += Parser.listExtendedValueToXML("beamWidth", self._beamWidth)

        if self._beamWidthErrorExists:

            result += Parser.listExtendedValueToXML(
                "beamWidthError", self._beamWidthError
            )

        if self._beamWidthWasFixedExists:

            result += Parser.listValueToXML(
                "beamWidthWasFixed", self._beamWidthWasFixed
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
                "xmlrow is not a string or a minidom.Element", "CalPointingTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalPointingTable")

        # intrinsic attribute values

        antennaNameNode = rowdom.getElementsByTagName("antennaName")[0]

        self._antennaName = str(antennaNameNode.firstChild.data.strip())

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data.strip()
        )

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        ambientTemperatureNode = rowdom.getElementsByTagName("ambientTemperature")[0]

        self._ambientTemperature = Temperature(
            ambientTemperatureNode.firstChild.data.strip()
        )

        antennaMakeNode = rowdom.getElementsByTagName("antennaMake")[0]

        self._antennaMake = AntennaMake.newAntennaMake(
            antennaMakeNode.firstChild.data.strip()
        )

        atmPhaseCorrectionNode = rowdom.getElementsByTagName("atmPhaseCorrection")[0]

        self._atmPhaseCorrection = AtmPhaseCorrection.newAtmPhaseCorrection(
            atmPhaseCorrectionNode.firstChild.data.strip()
        )

        directionNode = rowdom.getElementsByTagName("direction")[0]

        directionStr = directionNode.firstChild.data.strip()

        self._direction = Parser.stringListToLists(
            directionStr, Angle, "CalPointing", True
        )

        frequencyRangeNode = rowdom.getElementsByTagName("frequencyRange")[0]

        frequencyRangeStr = frequencyRangeNode.firstChild.data.strip()

        self._frequencyRange = Parser.stringListToLists(
            frequencyRangeStr, Frequency, "CalPointing", True
        )

        pointingModelModeNode = rowdom.getElementsByTagName("pointingModelMode")[0]

        self._pointingModelMode = PointingModelMode.newPointingModelMode(
            pointingModelModeNode.firstChild.data.strip()
        )

        pointingMethodNode = rowdom.getElementsByTagName("pointingMethod")[0]

        self._pointingMethod = PointingMethod.newPointingMethod(
            pointingMethodNode.firstChild.data.strip()
        )

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data.strip()
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "CalPointing", False
        )

        collOffsetRelativeNode = rowdom.getElementsByTagName("collOffsetRelative")[0]

        collOffsetRelativeStr = collOffsetRelativeNode.firstChild.data.strip()

        self._collOffsetRelative = Parser.stringListToLists(
            collOffsetRelativeStr, Angle, "CalPointing", True
        )

        collOffsetAbsoluteNode = rowdom.getElementsByTagName("collOffsetAbsolute")[0]

        collOffsetAbsoluteStr = collOffsetAbsoluteNode.firstChild.data.strip()

        self._collOffsetAbsolute = Parser.stringListToLists(
            collOffsetAbsoluteStr, Angle, "CalPointing", True
        )

        collErrorNode = rowdom.getElementsByTagName("collError")[0]

        collErrorStr = collErrorNode.firstChild.data.strip()

        self._collError = Parser.stringListToLists(
            collErrorStr, Angle, "CalPointing", True
        )

        collOffsetTiedNode = rowdom.getElementsByTagName("collOffsetTied")[0]

        collOffsetTiedStr = collOffsetTiedNode.firstChild.data.strip()

        self._collOffsetTied = Parser.stringListToLists(
            collOffsetTiedStr, bool, "CalPointing", False
        )

        reducedChiSquaredNode = rowdom.getElementsByTagName("reducedChiSquared")[0]

        reducedChiSquaredStr = reducedChiSquaredNode.firstChild.data.strip()

        self._reducedChiSquared = Parser.stringListToLists(
            reducedChiSquaredStr, float, "CalPointing", False
        )

        averagedPolarizationsNode = rowdom.getElementsByTagName("averagedPolarizations")
        if len(averagedPolarizationsNode) > 0:

            self._averagedPolarizations = bool(
                averagedPolarizationsNode[0].firstChild.data.strip()
            )

            self._averagedPolarizationsExists = True

        beamPANode = rowdom.getElementsByTagName("beamPA")
        if len(beamPANode) > 0:

            beamPAStr = beamPANode[0].firstChild.data.strip()

            self._beamPA = Parser.stringListToLists(
                beamPAStr, Angle, "CalPointing", True
            )

            self._beamPAExists = True

        beamPAErrorNode = rowdom.getElementsByTagName("beamPAError")
        if len(beamPAErrorNode) > 0:

            beamPAErrorStr = beamPAErrorNode[0].firstChild.data.strip()

            self._beamPAError = Parser.stringListToLists(
                beamPAErrorStr, Angle, "CalPointing", True
            )

            self._beamPAErrorExists = True

        beamPAWasFixedNode = rowdom.getElementsByTagName("beamPAWasFixed")
        if len(beamPAWasFixedNode) > 0:

            self._beamPAWasFixed = bool(beamPAWasFixedNode[0].firstChild.data.strip())

            self._beamPAWasFixedExists = True

        beamWidthNode = rowdom.getElementsByTagName("beamWidth")
        if len(beamWidthNode) > 0:

            beamWidthStr = beamWidthNode[0].firstChild.data.strip()

            self._beamWidth = Parser.stringListToLists(
                beamWidthStr, Angle, "CalPointing", True
            )

            self._beamWidthExists = True

        beamWidthErrorNode = rowdom.getElementsByTagName("beamWidthError")
        if len(beamWidthErrorNode) > 0:

            beamWidthErrorStr = beamWidthErrorNode[0].firstChild.data.strip()

            self._beamWidthError = Parser.stringListToLists(
                beamWidthErrorStr, Angle, "CalPointing", True
            )

            self._beamWidthErrorExists = True

        beamWidthWasFixedNode = rowdom.getElementsByTagName("beamWidthWasFixed")
        if len(beamWidthWasFixedNode) > 0:

            beamWidthWasFixedStr = beamWidthWasFixedNode[0].firstChild.data.strip()

            self._beamWidthWasFixed = Parser.stringListToLists(
                beamWidthWasFixedStr, bool, "CalPointing", False
            )

            self._beamWidthWasFixedExists = True

        offIntensityNode = rowdom.getElementsByTagName("offIntensity")
        if len(offIntensityNode) > 0:

            offIntensityStr = offIntensityNode[0].firstChild.data.strip()

            self._offIntensity = Parser.stringListToLists(
                offIntensityStr, Temperature, "CalPointing", True
            )

            self._offIntensityExists = True

        offIntensityErrorNode = rowdom.getElementsByTagName("offIntensityError")
        if len(offIntensityErrorNode) > 0:

            offIntensityErrorStr = offIntensityErrorNode[0].firstChild.data.strip()

            self._offIntensityError = Parser.stringListToLists(
                offIntensityErrorStr, Temperature, "CalPointing", True
            )

            self._offIntensityErrorExists = True

        offIntensityWasFixedNode = rowdom.getElementsByTagName("offIntensityWasFixed")
        if len(offIntensityWasFixedNode) > 0:

            self._offIntensityWasFixed = bool(
                offIntensityWasFixedNode[0].firstChild.data.strip()
            )

            self._offIntensityWasFixedExists = True

        peakIntensityNode = rowdom.getElementsByTagName("peakIntensity")
        if len(peakIntensityNode) > 0:

            peakIntensityStr = peakIntensityNode[0].firstChild.data.strip()

            self._peakIntensity = Parser.stringListToLists(
                peakIntensityStr, Temperature, "CalPointing", True
            )

            self._peakIntensityExists = True

        peakIntensityErrorNode = rowdom.getElementsByTagName("peakIntensityError")
        if len(peakIntensityErrorNode) > 0:

            peakIntensityErrorStr = peakIntensityErrorNode[0].firstChild.data.strip()

            self._peakIntensityError = Parser.stringListToLists(
                peakIntensityErrorStr, Temperature, "CalPointing", True
            )

            self._peakIntensityErrorExists = True

        peakIntensityWasFixedNode = rowdom.getElementsByTagName("peakIntensityWasFixed")
        if len(peakIntensityWasFixedNode) > 0:

            self._peakIntensityWasFixed = bool(
                peakIntensityWasFixedNode[0].firstChild.data.strip()
            )

            self._peakIntensityWasFixedExists = True

        # extrinsic attribute values

        calDataIdNode = rowdom.getElementsByTagName("calDataId")[0]

        self._calDataId = Tag(calDataIdNode.firstChild.data.strip())

        calReductionIdNode = rowdom.getElementsByTagName("calReductionId")[0]

        self._calReductionId = Tag(calReductionIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        eos.writeStr(self._antennaName)

        eos.writeString(str(self._receiverBand))

        self._calDataId.toBin(eos)

        self._calReductionId.toBin(eos)

        self._startValidTime.toBin(eos)

        self._endValidTime.toBin(eos)

        self._ambientTemperature.toBin(eos)

        eos.writeString(str(self._antennaMake))

        eos.writeString(str(self._atmPhaseCorrection))

        Angle.listToBin(self._direction, eos)

        Frequency.listToBin(self._frequencyRange, eos)

        eos.writeString(str(self._pointingModelMode))

        eos.writeString(str(self._pointingMethod))

        eos.writeInt(self._numReceptor)

        eos.writeInt(len(self._polarizationTypes))
        for i in range(len(self._polarizationTypes)):

            eos.writeString(str(self._polarizationTypes[i]))

        Angle.listToBin(self._collOffsetRelative, eos)

        Angle.listToBin(self._collOffsetAbsolute, eos)

        Angle.listToBin(self._collError, eos)

        # null array case, unsure if this is possible but this should work
        if self._collOffsetTied is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            collOffsetTied_dims = pyasdm.utils.getListDims(self._collOffsetTied)
        # assumes it really is 2D
        eos.writeInt(collOffsetTied_dims[0])
        eos.writeInt(collOffsetTied_dims[1])
        for i in range(collOffsetTied_dims[0]):
            for j in range(collOffsetTied_dims[1]):
                eos.writeBool(self._collOffsetTied[i][j])

        eos.writeInt(len(self._reducedChiSquared))
        for i in range(len(self._reducedChiSquared)):

            eos.writeFloat(self._reducedChiSquared[i])

        eos.writeBool(self._averagedPolarizationsExists)
        if self._averagedPolarizationsExists:

            eos.writeBool(self._averagedPolarizations)

        eos.writeBool(self._beamPAExists)
        if self._beamPAExists:

            Angle.listToBin(self._beamPA, eos)

        eos.writeBool(self._beamPAErrorExists)
        if self._beamPAErrorExists:

            Angle.listToBin(self._beamPAError, eos)

        eos.writeBool(self._beamPAWasFixedExists)
        if self._beamPAWasFixedExists:

            eos.writeBool(self._beamPAWasFixed)

        eos.writeBool(self._beamWidthExists)
        if self._beamWidthExists:

            Angle.listToBin(self._beamWidth, eos)

        eos.writeBool(self._beamWidthErrorExists)
        if self._beamWidthErrorExists:

            Angle.listToBin(self._beamWidthError, eos)

        eos.writeBool(self._beamWidthWasFixedExists)
        if self._beamWidthWasFixedExists:

            eos.writeInt(len(self._beamWidthWasFixed))
            for i in range(len(self._beamWidthWasFixed)):

                eos.writeBool(self._beamWidthWasFixed[i])

        eos.writeBool(self._offIntensityExists)
        if self._offIntensityExists:

            Temperature.listToBin(self._offIntensity, eos)

        eos.writeBool(self._offIntensityErrorExists)
        if self._offIntensityErrorExists:

            Temperature.listToBin(self._offIntensityError, eos)

        eos.writeBool(self._offIntensityWasFixedExists)
        if self._offIntensityWasFixedExists:

            eos.writeBool(self._offIntensityWasFixed)

        eos.writeBool(self._peakIntensityExists)
        if self._peakIntensityExists:

            Temperature.listToBin(self._peakIntensity, eos)

        eos.writeBool(self._peakIntensityErrorExists)
        if self._peakIntensityErrorExists:

            Temperature.listToBin(self._peakIntensityError, eos)

        eos.writeBool(self._peakIntensityWasFixedExists)
        if self._peakIntensityWasFixedExists:

            eos.writeBool(self._peakIntensityWasFixed)

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
    def ambientTemperatureFromBin(row, eis):
        """
        Set the ambientTemperature in row from the EndianInput (eis) instance.
        """

        row._ambientTemperature = Temperature.fromBin(eis)

    @staticmethod
    def antennaMakeFromBin(row, eis):
        """
        Set the antennaMake in row from the EndianInput (eis) instance.
        """

        row._antennaMake = AntennaMake.literal(eis.readString())

    @staticmethod
    def atmPhaseCorrectionFromBin(row, eis):
        """
        Set the atmPhaseCorrection in row from the EndianInput (eis) instance.
        """

        row._atmPhaseCorrection = AtmPhaseCorrection.literal(eis.readString())

    @staticmethod
    def directionFromBin(row, eis):
        """
        Set the direction in row from the EndianInput (eis) instance.
        """

        row._direction = Angle.from1DBin(eis)

    @staticmethod
    def frequencyRangeFromBin(row, eis):
        """
        Set the frequencyRange in row from the EndianInput (eis) instance.
        """

        row._frequencyRange = Frequency.from1DBin(eis)

    @staticmethod
    def pointingModelModeFromBin(row, eis):
        """
        Set the pointingModelMode in row from the EndianInput (eis) instance.
        """

        row._pointingModelMode = PointingModelMode.literal(eis.readString())

    @staticmethod
    def pointingMethodFromBin(row, eis):
        """
        Set the pointingMethod in row from the EndianInput (eis) instance.
        """

        row._pointingMethod = PointingMethod.literal(eis.readString())

    @staticmethod
    def numReceptorFromBin(row, eis):
        """
        Set the numReceptor in row from the EndianInput (eis) instance.
        """

        row._numReceptor = eis.readInt()

    @staticmethod
    def polarizationTypesFromBin(row, eis):
        """
        Set the polarizationTypes in row from the EndianInput (eis) instance.
        """

        polarizationTypesDim1 = eis.readInt()
        thisList = []
        for i in range(polarizationTypesDim1):
            thisValue = PolarizationType.literal(eis.readString())
            thisList.append(thisValue)
        row._polarizationTypes = thisList

    @staticmethod
    def collOffsetRelativeFromBin(row, eis):
        """
        Set the collOffsetRelative in row from the EndianInput (eis) instance.
        """

        row._collOffsetRelative = Angle.from2DBin(eis)

    @staticmethod
    def collOffsetAbsoluteFromBin(row, eis):
        """
        Set the collOffsetAbsolute in row from the EndianInput (eis) instance.
        """

        row._collOffsetAbsolute = Angle.from2DBin(eis)

    @staticmethod
    def collErrorFromBin(row, eis):
        """
        Set the collError in row from the EndianInput (eis) instance.
        """

        row._collError = Angle.from2DBin(eis)

    @staticmethod
    def collOffsetTiedFromBin(row, eis):
        """
        Set the collOffsetTied in row from the EndianInput (eis) instance.
        """

        collOffsetTiedDim1 = eis.readInt()
        collOffsetTiedDim2 = eis.readInt()
        thisList = []
        for i in range(collOffsetTiedDim1):
            thisList_j = []
            for j in range(collOffsetTiedDim2):
                thisValue = eis.readBool()
                thisList_j.append(thisValue)
            thisList.append(thisList_j)
        row._collOffsetTied = thisList

    @staticmethod
    def reducedChiSquaredFromBin(row, eis):
        """
        Set the reducedChiSquared in row from the EndianInput (eis) instance.
        """

        reducedChiSquaredDim1 = eis.readInt()
        thisList = []
        for i in range(reducedChiSquaredDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._reducedChiSquared = thisList

    @staticmethod
    def averagedPolarizationsFromBin(row, eis):
        """
        Set the optional averagedPolarizations in row from the EndianInput (eis) instance.
        """
        row._averagedPolarizationsExists = eis.readBool()
        if row._averagedPolarizationsExists:

            row._averagedPolarizations = eis.readBool()

    @staticmethod
    def beamPAFromBin(row, eis):
        """
        Set the optional beamPA in row from the EndianInput (eis) instance.
        """
        row._beamPAExists = eis.readBool()
        if row._beamPAExists:

            row._beamPA = Angle.from1DBin(eis)

    @staticmethod
    def beamPAErrorFromBin(row, eis):
        """
        Set the optional beamPAError in row from the EndianInput (eis) instance.
        """
        row._beamPAErrorExists = eis.readBool()
        if row._beamPAErrorExists:

            row._beamPAError = Angle.from1DBin(eis)

    @staticmethod
    def beamPAWasFixedFromBin(row, eis):
        """
        Set the optional beamPAWasFixed in row from the EndianInput (eis) instance.
        """
        row._beamPAWasFixedExists = eis.readBool()
        if row._beamPAWasFixedExists:

            row._beamPAWasFixed = eis.readBool()

    @staticmethod
    def beamWidthFromBin(row, eis):
        """
        Set the optional beamWidth in row from the EndianInput (eis) instance.
        """
        row._beamWidthExists = eis.readBool()
        if row._beamWidthExists:

            row._beamWidth = Angle.from2DBin(eis)

    @staticmethod
    def beamWidthErrorFromBin(row, eis):
        """
        Set the optional beamWidthError in row from the EndianInput (eis) instance.
        """
        row._beamWidthErrorExists = eis.readBool()
        if row._beamWidthErrorExists:

            row._beamWidthError = Angle.from2DBin(eis)

    @staticmethod
    def beamWidthWasFixedFromBin(row, eis):
        """
        Set the optional beamWidthWasFixed in row from the EndianInput (eis) instance.
        """
        row._beamWidthWasFixedExists = eis.readBool()
        if row._beamWidthWasFixedExists:

            beamWidthWasFixedDim1 = eis.readInt()
            thisList = []
            for i in range(beamWidthWasFixedDim1):
                thisValue = eis.readBool()
                thisList.append(thisValue)
            row._beamWidthWasFixed = thisList

    @staticmethod
    def offIntensityFromBin(row, eis):
        """
        Set the optional offIntensity in row from the EndianInput (eis) instance.
        """
        row._offIntensityExists = eis.readBool()
        if row._offIntensityExists:

            row._offIntensity = Temperature.from1DBin(eis)

    @staticmethod
    def offIntensityErrorFromBin(row, eis):
        """
        Set the optional offIntensityError in row from the EndianInput (eis) instance.
        """
        row._offIntensityErrorExists = eis.readBool()
        if row._offIntensityErrorExists:

            row._offIntensityError = Temperature.from1DBin(eis)

    @staticmethod
    def offIntensityWasFixedFromBin(row, eis):
        """
        Set the optional offIntensityWasFixed in row from the EndianInput (eis) instance.
        """
        row._offIntensityWasFixedExists = eis.readBool()
        if row._offIntensityWasFixedExists:

            row._offIntensityWasFixed = eis.readBool()

    @staticmethod
    def peakIntensityFromBin(row, eis):
        """
        Set the optional peakIntensity in row from the EndianInput (eis) instance.
        """
        row._peakIntensityExists = eis.readBool()
        if row._peakIntensityExists:

            row._peakIntensity = Temperature.from1DBin(eis)

    @staticmethod
    def peakIntensityErrorFromBin(row, eis):
        """
        Set the optional peakIntensityError in row from the EndianInput (eis) instance.
        """
        row._peakIntensityErrorExists = eis.readBool()
        if row._peakIntensityErrorExists:

            row._peakIntensityError = Temperature.from1DBin(eis)

    @staticmethod
    def peakIntensityWasFixedFromBin(row, eis):
        """
        Set the optional peakIntensityWasFixed in row from the EndianInput (eis) instance.
        """
        row._peakIntensityWasFixedExists = eis.readBool()
        if row._peakIntensityWasFixedExists:

            row._peakIntensityWasFixed = eis.readBool()

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaName"] = CalPointingRow.antennaNameFromBin
        _fromBinMethods["receiverBand"] = CalPointingRow.receiverBandFromBin
        _fromBinMethods["calDataId"] = CalPointingRow.calDataIdFromBin
        _fromBinMethods["calReductionId"] = CalPointingRow.calReductionIdFromBin
        _fromBinMethods["startValidTime"] = CalPointingRow.startValidTimeFromBin
        _fromBinMethods["endValidTime"] = CalPointingRow.endValidTimeFromBin
        _fromBinMethods["ambientTemperature"] = CalPointingRow.ambientTemperatureFromBin
        _fromBinMethods["antennaMake"] = CalPointingRow.antennaMakeFromBin
        _fromBinMethods["atmPhaseCorrection"] = CalPointingRow.atmPhaseCorrectionFromBin
        _fromBinMethods["direction"] = CalPointingRow.directionFromBin
        _fromBinMethods["frequencyRange"] = CalPointingRow.frequencyRangeFromBin
        _fromBinMethods["pointingModelMode"] = CalPointingRow.pointingModelModeFromBin
        _fromBinMethods["pointingMethod"] = CalPointingRow.pointingMethodFromBin
        _fromBinMethods["numReceptor"] = CalPointingRow.numReceptorFromBin
        _fromBinMethods["polarizationTypes"] = CalPointingRow.polarizationTypesFromBin
        _fromBinMethods["collOffsetRelative"] = CalPointingRow.collOffsetRelativeFromBin
        _fromBinMethods["collOffsetAbsolute"] = CalPointingRow.collOffsetAbsoluteFromBin
        _fromBinMethods["collError"] = CalPointingRow.collErrorFromBin
        _fromBinMethods["collOffsetTied"] = CalPointingRow.collOffsetTiedFromBin
        _fromBinMethods["reducedChiSquared"] = CalPointingRow.reducedChiSquaredFromBin

        _fromBinMethods["averagedPolarizations"] = (
            CalPointingRow.averagedPolarizationsFromBin
        )
        _fromBinMethods["beamPA"] = CalPointingRow.beamPAFromBin
        _fromBinMethods["beamPAError"] = CalPointingRow.beamPAErrorFromBin
        _fromBinMethods["beamPAWasFixed"] = CalPointingRow.beamPAWasFixedFromBin
        _fromBinMethods["beamWidth"] = CalPointingRow.beamWidthFromBin
        _fromBinMethods["beamWidthError"] = CalPointingRow.beamWidthErrorFromBin
        _fromBinMethods["beamWidthWasFixed"] = CalPointingRow.beamWidthWasFixedFromBin
        _fromBinMethods["offIntensity"] = CalPointingRow.offIntensityFromBin
        _fromBinMethods["offIntensityError"] = CalPointingRow.offIntensityErrorFromBin
        _fromBinMethods["offIntensityWasFixed"] = (
            CalPointingRow.offIntensityWasFixedFromBin
        )
        _fromBinMethods["peakIntensity"] = CalPointingRow.peakIntensityFromBin
        _fromBinMethods["peakIntensityError"] = CalPointingRow.peakIntensityErrorFromBin
        _fromBinMethods["peakIntensityWasFixed"] = (
            CalPointingRow.peakIntensityWasFixedFromBin
        )

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CalPointingRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalPointing",
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
            listDims = pyasdm.utils.getListDims(direction)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of direction is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(direction, Angle):
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
            listDims = pyasdm.utils.getListDims(frequencyRange)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of frequencyRange is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(frequencyRange, Frequency):
                raise ValueError(
                    "type of the first value in frequencyRange is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._frequencyRange = copy.deepcopy(frequencyRange)
        except Exception as exc:
            raise ValueError("Invalid frequencyRange : " + str(exc))

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

    # ===> Attribute pointingMethod

    _pointingMethod = PointingMethod.from_int(0)

    def getPointingMethod(self):
        """
        Get pointingMethod.
        return pointingMethod as PointingMethod
        """

        return self._pointingMethod

    def setPointingMethod(self, pointingMethod):
        """
        Set pointingMethod with the specified PointingMethod value.
        pointingMethod The PointingMethod value to which pointingMethod is to be set.


        """

        self._pointingMethod = PointingMethod(pointingMethod)

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
            listDims = pyasdm.utils.getListDims(polarizationTypes)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of polarizationTypes is not correct")

            # the type of the values in the list must be PolarizationType
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(polarizationTypes, PolarizationType):
                raise ValueError(
                    "type of the first value in polarizationTypes is not PolarizationType as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._polarizationTypes = copy.deepcopy(polarizationTypes)
        except Exception as exc:
            raise ValueError("Invalid polarizationTypes : " + str(exc))

    # ===> Attribute collOffsetRelative

    _collOffsetRelative = None  # this is a 2D list of Angle

    def getCollOffsetRelative(self):
        """
        Get collOffsetRelative.
        return collOffsetRelative as Angle []  []
        """

        return copy.deepcopy(self._collOffsetRelative)

    def setCollOffsetRelative(self, collOffsetRelative):
        """
        Set collOffsetRelative with the specified Angle []  []  value.
        collOffsetRelative The Angle []  []  value to which collOffsetRelative is to be set.
        The value of collOffsetRelative can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(collOffsetRelative, list):
            raise ValueError("The value of collOffsetRelative must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(collOffsetRelative)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of collOffsetRelative is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(collOffsetRelative, Angle):
                raise ValueError(
                    "type of the first value in collOffsetRelative is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._collOffsetRelative = copy.deepcopy(collOffsetRelative)
        except Exception as exc:
            raise ValueError("Invalid collOffsetRelative : " + str(exc))

    # ===> Attribute collOffsetAbsolute

    _collOffsetAbsolute = None  # this is a 2D list of Angle

    def getCollOffsetAbsolute(self):
        """
        Get collOffsetAbsolute.
        return collOffsetAbsolute as Angle []  []
        """

        return copy.deepcopy(self._collOffsetAbsolute)

    def setCollOffsetAbsolute(self, collOffsetAbsolute):
        """
        Set collOffsetAbsolute with the specified Angle []  []  value.
        collOffsetAbsolute The Angle []  []  value to which collOffsetAbsolute is to be set.
        The value of collOffsetAbsolute can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(collOffsetAbsolute, list):
            raise ValueError("The value of collOffsetAbsolute must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(collOffsetAbsolute)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of collOffsetAbsolute is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(collOffsetAbsolute, Angle):
                raise ValueError(
                    "type of the first value in collOffsetAbsolute is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._collOffsetAbsolute = copy.deepcopy(collOffsetAbsolute)
        except Exception as exc:
            raise ValueError("Invalid collOffsetAbsolute : " + str(exc))

    # ===> Attribute collError

    _collError = None  # this is a 2D list of Angle

    def getCollError(self):
        """
        Get collError.
        return collError as Angle []  []
        """

        return copy.deepcopy(self._collError)

    def setCollError(self, collError):
        """
        Set collError with the specified Angle []  []  value.
        collError The Angle []  []  value to which collError is to be set.
        The value of collError can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(collError, list):
            raise ValueError("The value of collError must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(collError)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of collError is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(collError, Angle):
                raise ValueError(
                    "type of the first value in collError is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._collError = copy.deepcopy(collError)
        except Exception as exc:
            raise ValueError("Invalid collError : " + str(exc))

    # ===> Attribute collOffsetTied

    _collOffsetTied = None  # this is a 2D list of bool

    def getCollOffsetTied(self):
        """
        Get collOffsetTied.
        return collOffsetTied as bool []  []
        """

        return copy.deepcopy(self._collOffsetTied)

    def setCollOffsetTied(self, collOffsetTied):
        """
        Set collOffsetTied with the specified bool []  []  value.
        collOffsetTied The bool []  []  value to which collOffsetTied is to be set.


        """

        # value must be a list
        if not isinstance(collOffsetTied, list):
            raise ValueError("The value of collOffsetTied must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(collOffsetTied)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of collOffsetTied is not correct")

            # the type of the values in the list must be bool
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(collOffsetTied, bool):
                raise ValueError(
                    "type of the first value in collOffsetTied is not bool as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._collOffsetTied = copy.deepcopy(collOffsetTied)
        except Exception as exc:
            raise ValueError("Invalid collOffsetTied : " + str(exc))

    # ===> Attribute reducedChiSquared

    _reducedChiSquared = None  # this is a 1D list of float

    def getReducedChiSquared(self):
        """
        Get reducedChiSquared.
        return reducedChiSquared as float []
        """

        return copy.deepcopy(self._reducedChiSquared)

    def setReducedChiSquared(self, reducedChiSquared):
        """
        Set reducedChiSquared with the specified float []  value.
        reducedChiSquared The float []  value to which reducedChiSquared is to be set.


        """

        # value must be a list
        if not isinstance(reducedChiSquared, list):
            raise ValueError("The value of reducedChiSquared must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(reducedChiSquared)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of reducedChiSquared is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(reducedChiSquared, float):
                raise ValueError(
                    "type of the first value in reducedChiSquared is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._reducedChiSquared = copy.deepcopy(reducedChiSquared)
        except Exception as exc:
            raise ValueError("Invalid reducedChiSquared : " + str(exc))

    # ===> Attribute averagedPolarizations, which is optional
    _averagedPolarizationsExists = False

    _averagedPolarizations = None

    def isAveragedPolarizationsExists(self):
        """
        The attribute averagedPolarizations is optional. Return True if this attribute exists.
        return True if and only if the averagedPolarizations attribute exists.
        """
        return self._averagedPolarizationsExists

    def getAveragedPolarizations(self):
        """
        Get averagedPolarizations, which is optional.
        return averagedPolarizations as bool
        raises ValueError If averagedPolarizations does not exist.
        """
        if not self._averagedPolarizationsExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + averagedPolarizations
                + " attribute in table CalPointing does not exist!"
            )

        return self._averagedPolarizations

    def setAveragedPolarizations(self, averagedPolarizations):
        """
        Set averagedPolarizations with the specified bool value.
        averagedPolarizations The bool value to which averagedPolarizations is to be set.


        """

        self._averagedPolarizations = bool(averagedPolarizations)

        self._averagedPolarizationsExists = True

    def clearAveragedPolarizations(self):
        """
        Mark averagedPolarizations, which is an optional field, as non-existent.
        """
        self._averagedPolarizationsExists = False

    # ===> Attribute beamPA, which is optional
    _beamPAExists = False

    _beamPA = None  # this is a 1D list of Angle

    def isBeamPAExists(self):
        """
        The attribute beamPA is optional. Return True if this attribute exists.
        return True if and only if the beamPA attribute exists.
        """
        return self._beamPAExists

    def getBeamPA(self):
        """
        Get beamPA, which is optional.
        return beamPA as Angle []
        raises ValueError If beamPA does not exist.
        """
        if not self._beamPAExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + beamPA
                + " attribute in table CalPointing does not exist!"
            )

        return copy.deepcopy(self._beamPA)

    def setBeamPA(self, beamPA):
        """
        Set beamPA with the specified Angle []  value.
        beamPA The Angle []  value to which beamPA is to be set.
        The value of beamPA can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(beamPA, list):
            raise ValueError("The value of beamPA must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(beamPA)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of beamPA is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(beamPA, Angle):
                raise ValueError(
                    "type of the first value in beamPA is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._beamPA = copy.deepcopy(beamPA)
        except Exception as exc:
            raise ValueError("Invalid beamPA : " + str(exc))

        self._beamPAExists = True

    def clearBeamPA(self):
        """
        Mark beamPA, which is an optional field, as non-existent.
        """
        self._beamPAExists = False

    # ===> Attribute beamPAError, which is optional
    _beamPAErrorExists = False

    _beamPAError = None  # this is a 1D list of Angle

    def isBeamPAErrorExists(self):
        """
        The attribute beamPAError is optional. Return True if this attribute exists.
        return True if and only if the beamPAError attribute exists.
        """
        return self._beamPAErrorExists

    def getBeamPAError(self):
        """
        Get beamPAError, which is optional.
        return beamPAError as Angle []
        raises ValueError If beamPAError does not exist.
        """
        if not self._beamPAErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + beamPAError
                + " attribute in table CalPointing does not exist!"
            )

        return copy.deepcopy(self._beamPAError)

    def setBeamPAError(self, beamPAError):
        """
        Set beamPAError with the specified Angle []  value.
        beamPAError The Angle []  value to which beamPAError is to be set.
        The value of beamPAError can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(beamPAError, list):
            raise ValueError("The value of beamPAError must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(beamPAError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of beamPAError is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(beamPAError, Angle):
                raise ValueError(
                    "type of the first value in beamPAError is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._beamPAError = copy.deepcopy(beamPAError)
        except Exception as exc:
            raise ValueError("Invalid beamPAError : " + str(exc))

        self._beamPAErrorExists = True

    def clearBeamPAError(self):
        """
        Mark beamPAError, which is an optional field, as non-existent.
        """
        self._beamPAErrorExists = False

    # ===> Attribute beamPAWasFixed, which is optional
    _beamPAWasFixedExists = False

    _beamPAWasFixed = None

    def isBeamPAWasFixedExists(self):
        """
        The attribute beamPAWasFixed is optional. Return True if this attribute exists.
        return True if and only if the beamPAWasFixed attribute exists.
        """
        return self._beamPAWasFixedExists

    def getBeamPAWasFixed(self):
        """
        Get beamPAWasFixed, which is optional.
        return beamPAWasFixed as bool
        raises ValueError If beamPAWasFixed does not exist.
        """
        if not self._beamPAWasFixedExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + beamPAWasFixed
                + " attribute in table CalPointing does not exist!"
            )

        return self._beamPAWasFixed

    def setBeamPAWasFixed(self, beamPAWasFixed):
        """
        Set beamPAWasFixed with the specified bool value.
        beamPAWasFixed The bool value to which beamPAWasFixed is to be set.


        """

        self._beamPAWasFixed = bool(beamPAWasFixed)

        self._beamPAWasFixedExists = True

    def clearBeamPAWasFixed(self):
        """
        Mark beamPAWasFixed, which is an optional field, as non-existent.
        """
        self._beamPAWasFixedExists = False

    # ===> Attribute beamWidth, which is optional
    _beamWidthExists = False

    _beamWidth = None  # this is a 2D list of Angle

    def isBeamWidthExists(self):
        """
        The attribute beamWidth is optional. Return True if this attribute exists.
        return True if and only if the beamWidth attribute exists.
        """
        return self._beamWidthExists

    def getBeamWidth(self):
        """
        Get beamWidth, which is optional.
        return beamWidth as Angle []  []
        raises ValueError If beamWidth does not exist.
        """
        if not self._beamWidthExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + beamWidth
                + " attribute in table CalPointing does not exist!"
            )

        return copy.deepcopy(self._beamWidth)

    def setBeamWidth(self, beamWidth):
        """
        Set beamWidth with the specified Angle []  []  value.
        beamWidth The Angle []  []  value to which beamWidth is to be set.
        The value of beamWidth can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(beamWidth, list):
            raise ValueError("The value of beamWidth must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(beamWidth)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of beamWidth is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(beamWidth, Angle):
                raise ValueError(
                    "type of the first value in beamWidth is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._beamWidth = copy.deepcopy(beamWidth)
        except Exception as exc:
            raise ValueError("Invalid beamWidth : " + str(exc))

        self._beamWidthExists = True

    def clearBeamWidth(self):
        """
        Mark beamWidth, which is an optional field, as non-existent.
        """
        self._beamWidthExists = False

    # ===> Attribute beamWidthError, which is optional
    _beamWidthErrorExists = False

    _beamWidthError = None  # this is a 2D list of Angle

    def isBeamWidthErrorExists(self):
        """
        The attribute beamWidthError is optional. Return True if this attribute exists.
        return True if and only if the beamWidthError attribute exists.
        """
        return self._beamWidthErrorExists

    def getBeamWidthError(self):
        """
        Get beamWidthError, which is optional.
        return beamWidthError as Angle []  []
        raises ValueError If beamWidthError does not exist.
        """
        if not self._beamWidthErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + beamWidthError
                + " attribute in table CalPointing does not exist!"
            )

        return copy.deepcopy(self._beamWidthError)

    def setBeamWidthError(self, beamWidthError):
        """
        Set beamWidthError with the specified Angle []  []  value.
        beamWidthError The Angle []  []  value to which beamWidthError is to be set.
        The value of beamWidthError can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(beamWidthError, list):
            raise ValueError("The value of beamWidthError must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(beamWidthError)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of beamWidthError is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(beamWidthError, Angle):
                raise ValueError(
                    "type of the first value in beamWidthError is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._beamWidthError = copy.deepcopy(beamWidthError)
        except Exception as exc:
            raise ValueError("Invalid beamWidthError : " + str(exc))

        self._beamWidthErrorExists = True

    def clearBeamWidthError(self):
        """
        Mark beamWidthError, which is an optional field, as non-existent.
        """
        self._beamWidthErrorExists = False

    # ===> Attribute beamWidthWasFixed, which is optional
    _beamWidthWasFixedExists = False

    _beamWidthWasFixed = None  # this is a 1D list of bool

    def isBeamWidthWasFixedExists(self):
        """
        The attribute beamWidthWasFixed is optional. Return True if this attribute exists.
        return True if and only if the beamWidthWasFixed attribute exists.
        """
        return self._beamWidthWasFixedExists

    def getBeamWidthWasFixed(self):
        """
        Get beamWidthWasFixed, which is optional.
        return beamWidthWasFixed as bool []
        raises ValueError If beamWidthWasFixed does not exist.
        """
        if not self._beamWidthWasFixedExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + beamWidthWasFixed
                + " attribute in table CalPointing does not exist!"
            )

        return copy.deepcopy(self._beamWidthWasFixed)

    def setBeamWidthWasFixed(self, beamWidthWasFixed):
        """
        Set beamWidthWasFixed with the specified bool []  value.
        beamWidthWasFixed The bool []  value to which beamWidthWasFixed is to be set.


        """

        # value must be a list
        if not isinstance(beamWidthWasFixed, list):
            raise ValueError("The value of beamWidthWasFixed must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(beamWidthWasFixed)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of beamWidthWasFixed is not correct")

            # the type of the values in the list must be bool
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(beamWidthWasFixed, bool):
                raise ValueError(
                    "type of the first value in beamWidthWasFixed is not bool as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._beamWidthWasFixed = copy.deepcopy(beamWidthWasFixed)
        except Exception as exc:
            raise ValueError("Invalid beamWidthWasFixed : " + str(exc))

        self._beamWidthWasFixedExists = True

    def clearBeamWidthWasFixed(self):
        """
        Mark beamWidthWasFixed, which is an optional field, as non-existent.
        """
        self._beamWidthWasFixedExists = False

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
                + " attribute in table CalPointing does not exist!"
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
            listDims = pyasdm.utils.getListDims(offIntensity)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of offIntensity is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(offIntensity, Temperature):
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
                + " attribute in table CalPointing does not exist!"
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
            listDims = pyasdm.utils.getListDims(offIntensityError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of offIntensityError is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(offIntensityError, Temperature):
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
                + " attribute in table CalPointing does not exist!"
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
                + " attribute in table CalPointing does not exist!"
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
            listDims = pyasdm.utils.getListDims(peakIntensity)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of peakIntensity is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(peakIntensity, Temperature):
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
                + " attribute in table CalPointing does not exist!"
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
            listDims = pyasdm.utils.getListDims(peakIntensityError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of peakIntensityError is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(peakIntensityError, Temperature):
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
                + " attribute in table CalPointing does not exist!"
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
        antennaMake,
        atmPhaseCorrection,
        direction,
        frequencyRange,
        pointingModelMode,
        pointingMethod,
        numReceptor,
        polarizationTypes,
        collOffsetRelative,
        collOffsetAbsolute,
        collError,
        collOffsetTied,
        reducedChiSquared,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalPointingRow with
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

        # antennaMake is a AntennaMake, compare using the == operator on the getValue() output
        if not (self._antennaMake.getValue() == antennaMake.getValue()):
            return False

        # atmPhaseCorrection is a AtmPhaseCorrection, compare using the == operator on the getValue() output
        if not (self._atmPhaseCorrection.getValue() == atmPhaseCorrection.getValue()):
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

        # pointingModelMode is a PointingModelMode, compare using the == operator on the getValue() output
        if not (self._pointingModelMode.getValue() == pointingModelMode.getValue()):
            return False

        # pointingMethod is a PointingMethod, compare using the == operator on the getValue() output
        if not (self._pointingMethod.getValue() == pointingMethod.getValue()):
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

        # We compare two 2D arrays (lists).
        if collOffsetRelative is not None:
            if self._collOffsetRelative is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            collOffsetRelative_dims = pyasdm.utils.getListDims(collOffsetRelative)
            this_collOffsetRelative_dims = pyasdm.utils.getListDims(
                self._collOffsetRelative
            )
            if collOffsetRelative_dims != this_collOffsetRelative_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(collOffsetRelative_dims[0]):
                for j in range(collOffsetRelative_dims[1]):

                    # collOffsetRelative is a Angle, compare using the almostEquals method.
                    if not (
                        self._collOffsetRelative[i][j].almostEquals(
                            collOffsetRelative[i][j],
                            self.getTable().getCollOffsetRelativeEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if collOffsetAbsolute is not None:
            if self._collOffsetAbsolute is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            collOffsetAbsolute_dims = pyasdm.utils.getListDims(collOffsetAbsolute)
            this_collOffsetAbsolute_dims = pyasdm.utils.getListDims(
                self._collOffsetAbsolute
            )
            if collOffsetAbsolute_dims != this_collOffsetAbsolute_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(collOffsetAbsolute_dims[0]):
                for j in range(collOffsetAbsolute_dims[1]):

                    # collOffsetAbsolute is a Angle, compare using the almostEquals method.
                    if not (
                        self._collOffsetAbsolute[i][j].almostEquals(
                            collOffsetAbsolute[i][j],
                            self.getTable().getCollOffsetAbsoluteEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if collError is not None:
            if self._collError is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            collError_dims = pyasdm.utils.getListDims(collError)
            this_collError_dims = pyasdm.utils.getListDims(self._collError)
            if collError_dims != this_collError_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(collError_dims[0]):
                for j in range(collError_dims[1]):

                    # collError is a Angle, compare using the almostEquals method.
                    if not (
                        self._collError[i][j].almostEquals(
                            collError[i][j], self.getTable().getCollErrorEqTolerance()
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if collOffsetTied is not None:
            if self._collOffsetTied is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            collOffsetTied_dims = pyasdm.utils.getListDims(collOffsetTied)
            this_collOffsetTied_dims = pyasdm.utils.getListDims(self._collOffsetTied)
            if collOffsetTied_dims != this_collOffsetTied_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(collOffsetTied_dims[0]):
                for j in range(collOffsetTied_dims[1]):

                    # collOffsetTied is an array of bool, compare using == operator.
                    if not (self._collOffsetTied[i][j] == collOffsetTied[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._reducedChiSquared) != len(reducedChiSquared):
            return False
        for indx in range(len(reducedChiSquared)):

            # reducedChiSquared is a list of float, compare using == operator.
            if not (self._reducedChiSquared[indx] == reducedChiSquared[indx]):
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
            otherRow.getAntennaMake(),
            otherRow.getAtmPhaseCorrection(),
            otherRow.getDirection(),
            otherRow.getFrequencyRange(),
            otherRow.getPointingModelMode(),
            otherRow.getPointingMethod(),
            otherRow.getNumReceptor(),
            otherRow.getPolarizationTypes(),
            otherRow.getCollOffsetRelative(),
            otherRow.getCollOffsetAbsolute(),
            otherRow.getCollError(),
            otherRow.getCollOffsetTied(),
            otherRow.getReducedChiSquared(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        ambientTemperature,
        antennaMake,
        atmPhaseCorrection,
        direction,
        frequencyRange,
        pointingModelMode,
        pointingMethod,
        numReceptor,
        polarizationTypes,
        collOffsetRelative,
        collOffsetAbsolute,
        collError,
        collOffsetTied,
        reducedChiSquared,
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

        # antennaMake is a AntennaMake, compare using the == operator on the getValue() output
        if not (self._antennaMake.getValue() == antennaMake.getValue()):
            return False

        # atmPhaseCorrection is a AtmPhaseCorrection, compare using the == operator on the getValue() output
        if not (self._atmPhaseCorrection.getValue() == atmPhaseCorrection.getValue()):
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

        # pointingModelMode is a PointingModelMode, compare using the == operator on the getValue() output
        if not (self._pointingModelMode.getValue() == pointingModelMode.getValue()):
            return False

        # pointingMethod is a PointingMethod, compare using the == operator on the getValue() output
        if not (self._pointingMethod.getValue() == pointingMethod.getValue()):
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

        # We compare two 2D arrays (lists).
        if collOffsetRelative is not None:
            if self._collOffsetRelative is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            collOffsetRelative_dims = pyasdm.utils.getListDims(collOffsetRelative)
            this_collOffsetRelative_dims = pyasdm.utils.getListDims(
                self._collOffsetRelative
            )
            if collOffsetRelative_dims != this_collOffsetRelative_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(collOffsetRelative_dims[0]):
                for j in range(collOffsetRelative_dims[1]):

                    # collOffsetRelative is a Angle, compare using the almostEquals method.
                    if not (
                        self._collOffsetRelative[i][j].almostEquals(
                            collOffsetRelative[i][j],
                            self.getTable().getCollOffsetRelativeEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if collOffsetAbsolute is not None:
            if self._collOffsetAbsolute is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            collOffsetAbsolute_dims = pyasdm.utils.getListDims(collOffsetAbsolute)
            this_collOffsetAbsolute_dims = pyasdm.utils.getListDims(
                self._collOffsetAbsolute
            )
            if collOffsetAbsolute_dims != this_collOffsetAbsolute_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(collOffsetAbsolute_dims[0]):
                for j in range(collOffsetAbsolute_dims[1]):

                    # collOffsetAbsolute is a Angle, compare using the almostEquals method.
                    if not (
                        self._collOffsetAbsolute[i][j].almostEquals(
                            collOffsetAbsolute[i][j],
                            self.getTable().getCollOffsetAbsoluteEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if collError is not None:
            if self._collError is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            collError_dims = pyasdm.utils.getListDims(collError)
            this_collError_dims = pyasdm.utils.getListDims(self._collError)
            if collError_dims != this_collError_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(collError_dims[0]):
                for j in range(collError_dims[1]):

                    # collError is a Angle, compare using the almostEquals method.
                    if not (
                        self._collError[i][j].almostEquals(
                            collError[i][j], self.getTable().getCollErrorEqTolerance()
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if collOffsetTied is not None:
            if self._collOffsetTied is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            collOffsetTied_dims = pyasdm.utils.getListDims(collOffsetTied)
            this_collOffsetTied_dims = pyasdm.utils.getListDims(self._collOffsetTied)
            if collOffsetTied_dims != this_collOffsetTied_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(collOffsetTied_dims[0]):
                for j in range(collOffsetTied_dims[1]):

                    # collOffsetTied is an array of bool, compare using == operator.
                    if not (self._collOffsetTied[i][j] == collOffsetTied[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._reducedChiSquared) != len(reducedChiSquared):
            return False
        for indx in range(len(reducedChiSquared)):

            # reducedChiSquared is a list of float, compare using == operator.
            if not (self._reducedChiSquared[indx] == reducedChiSquared[indx]):
                return False

        return True


# initialize the dictionary that maps fields to init methods
CalPointingRow.initFromBinMethods()
