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
# File CalHolographyRow.py
#

import pyasdm.CalHolographyTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.AntennaMake import AntennaMake


from pyasdm.enumerations.PolarizationType import PolarizationType


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from xml.dom import minidom

import copy


class CalHolographyRow:
    """
    The CalHolographyRow class is a row of a CalHolographyTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalHolographyRow.
        When row is None, create an empty row attached to table, which must be a CalHolographyTable.
        When row is given, copy those values in to the new row. The row argument must be a CalHolographyRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalHolographyTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._antennaMake = AntennaMake.from_int(0)

        # this is a list of PolarizationType Enumeration, start off with it being empty
        self._polarizationTypes = []

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._receiverBand = ReceiverBand.from_int(0)

        if row is not None:
            if not isinstance(row, CalHolographyRow):
                raise ValueError("row must be a MainRow")

            self._antennaName = row._antennaName

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            # We force the attribute of the result to be not None
            if row._antennaMake is None:
                self._antennaMake = AntennaMake.from_int(0)
            else:
                self._antennaMake = AntennaMake(row._antennaMake)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            self._ambientTemperature = Temperature(row._ambientTemperature)

            # focusPosition is a  list , make a deep copy
            self._focusPosition = copy.deepcopy(row._focusPosition)

            # frequencyRange is a  list , make a deep copy
            self._frequencyRange = copy.deepcopy(row._frequencyRange)

            self._illuminationTaper = row._illuminationTaper

            self._numReceptor = row._numReceptor

            # polarizationTypes is a  list , make a deep copy
            self._polarizationTypes = copy.deepcopy(row._polarizationTypes)

            self._numPanelModes = row._numPanelModes

            # We force the attribute of the result to be not None
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            self._beamMapUID = EntityRef(row._beamMapUID)

            self._rawRMS = Length(row._rawRMS)

            self._weightedRMS = Length(row._weightedRMS)

            self._surfaceMapUID = EntityRef(row._surfaceMapUID)

            # direction is a  list , make a deep copy
            self._direction = copy.deepcopy(row._direction)

            # by default set systematically numScrew's value to something not None

            if row._numScrewExists:

                self._numScrew = row._numScrew

                self._numScrewExists = True

            # by default set systematically screwName's value to something not None

            if row._screwNameExists:

                # screwName is a list, make a deep copy
                self.screwName = copy.deepcopy(row.screwName)

                self._screwNameExists = True

            # by default set systematically screwMotion's value to something not None

            if row._screwMotionExists:

                # screwMotion is a list, make a deep copy
                self.screwMotion = copy.deepcopy(row.screwMotion)

                self._screwMotionExists = True

            # by default set systematically screwMotionError's value to something not None

            if row._screwMotionErrorExists:

                # screwMotionError is a list, make a deep copy
                self.screwMotionError = copy.deepcopy(row.screwMotionError)

                self._screwMotionErrorExists = True

            # by default set systematically gravCorrection's value to something not None

            if row._gravCorrectionExists:

                self._gravCorrection = row._gravCorrection

                self._gravCorrectionExists = True

            # by default set systematically gravOptRange's value to something not None

            if row._gravOptRangeExists:

                # gravOptRange is a list, make a deep copy
                self.gravOptRange = copy.deepcopy(row.gravOptRange)

                self._gravOptRangeExists = True

            # by default set systematically tempCorrection's value to something not None

            if row._tempCorrectionExists:

                self._tempCorrection = row._tempCorrection

                self._tempCorrectionExists = True

            # by default set systematically tempOptRange's value to something not None

            if row._tempOptRangeExists:

                # tempOptRange is a list, make a deep copy
                self.tempOptRange = copy.deepcopy(row.tempOptRange)

                self._tempOptRangeExists = True

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

        result += Parser.valueToXML("antennaMake", AntennaMake.name(self._antennaMake))

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.extendedValueToXML(
            "ambientTemperature", self._ambientTemperature
        )

        result += Parser.listExtendedValueToXML("focusPosition", self._focusPosition)

        result += Parser.listExtendedValueToXML("frequencyRange", self._frequencyRange)

        result += Parser.valueToXML("illuminationTaper", self._illuminationTaper)

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.valueToXML("numPanelModes", self._numPanelModes)

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.extendedValueToXML("beamMapUID", self._beamMapUID)

        result += Parser.extendedValueToXML("rawRMS", self._rawRMS)

        result += Parser.extendedValueToXML("weightedRMS", self._weightedRMS)

        result += Parser.extendedValueToXML("surfaceMapUID", self._surfaceMapUID)

        result += Parser.listExtendedValueToXML("direction", self._direction)

        if self._numScrewExists:

            result += Parser.valueToXML("numScrew", self._numScrew)

        if self._screwNameExists:

            result += Parser.listValueToXML("screwName", self._screwName)

        if self._screwMotionExists:

            result += Parser.listExtendedValueToXML("screwMotion", self._screwMotion)

        if self._screwMotionErrorExists:

            result += Parser.listExtendedValueToXML(
                "screwMotionError", self._screwMotionError
            )

        if self._gravCorrectionExists:

            result += Parser.valueToXML("gravCorrection", self._gravCorrection)

        if self._gravOptRangeExists:

            result += Parser.listExtendedValueToXML("gravOptRange", self._gravOptRange)

        if self._tempCorrectionExists:

            result += Parser.valueToXML("tempCorrection", self._tempCorrection)

        if self._tempOptRangeExists:

            result += Parser.listExtendedValueToXML("tempOptRange", self._tempOptRange)

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
                "xmlrow is not a string or a minidom.Element", "CalHolographyTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalHolographyTable")

        # intrinsic attribute values

        antennaNameNode = rowdom.getElementsByTagName("antennaName")[0]

        self._antennaName = str(antennaNameNode.firstChild.data)

        antennaMakeNode = rowdom.getElementsByTagName("antennaMake")[0]

        self._antennaMake = AntennaMake.newAntennaMake(antennaMakeNode.firstChild.data)

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data)

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data)

        ambientTemperatureNode = rowdom.getElementsByTagName("ambientTemperature")[0]

        self._ambientTemperature = Temperature(ambientTemperatureNode.firstChild.data)

        focusPositionNode = rowdom.getElementsByTagName("focusPosition")[0]

        focusPositionStr = focusPositionNode.firstChild.data
        self._focusPosition = Parser.stringListToLists(
            focusPositionStr, Length, "CalHolography"
        )

        frequencyRangeNode = rowdom.getElementsByTagName("frequencyRange")[0]

        frequencyRangeStr = frequencyRangeNode.firstChild.data
        self._frequencyRange = Parser.stringListToLists(
            frequencyRangeStr, Frequency, "CalHolography"
        )

        illuminationTaperNode = rowdom.getElementsByTagName("illuminationTaper")[0]

        self._illuminationTaper = double(illuminationTaperNode.firstChild.data)

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data)

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "CalHolography"
        )

        numPanelModesNode = rowdom.getElementsByTagName("numPanelModes")[0]

        self._numPanelModes = int(numPanelModesNode.firstChild.data)

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data
        )

        beamMapUIDNode = rowdom.getElementsByTagName("beamMapUID")[0]

        self._beamMapUID = EntityRef(beamMapUIDNode.toxml())

        rawRMSNode = rowdom.getElementsByTagName("rawRMS")[0]

        self._rawRMS = Length(rawRMSNode.firstChild.data)

        weightedRMSNode = rowdom.getElementsByTagName("weightedRMS")[0]

        self._weightedRMS = Length(weightedRMSNode.firstChild.data)

        surfaceMapUIDNode = rowdom.getElementsByTagName("surfaceMapUID")[0]

        self._surfaceMapUID = EntityRef(surfaceMapUIDNode.toxml())

        directionNode = rowdom.getElementsByTagName("direction")[0]

        directionStr = directionNode.firstChild.data
        self._direction = Parser.stringListToLists(directionStr, Angle, "CalHolography")

        numScrewNode = rowdom.getElementsByTagName("numScrew")
        if len(numScrewNode) > 0:

            self._numScrew = int(numScrewNode[0].firstChild.data)

            self._numScrewExists = True

        screwNameNode = rowdom.getElementsByTagName("screwName")
        if len(screwNameNode) > 0:

            screwNameStr = screwNameNode[0].firstChild.data
            self._screwName = Parser.stringListToLists(
                screwNameStr, str, "CalHolography"
            )

            self._screwNameExists = True

        screwMotionNode = rowdom.getElementsByTagName("screwMotion")
        if len(screwMotionNode) > 0:

            screwMotionStr = screwMotionNode[0].firstChild.data
            self._screwMotion = Parser.stringListToLists(
                screwMotionStr, Length, "CalHolography"
            )

            self._screwMotionExists = True

        screwMotionErrorNode = rowdom.getElementsByTagName("screwMotionError")
        if len(screwMotionErrorNode) > 0:

            screwMotionErrorStr = screwMotionErrorNode[0].firstChild.data
            self._screwMotionError = Parser.stringListToLists(
                screwMotionErrorStr, Length, "CalHolography"
            )

            self._screwMotionErrorExists = True

        gravCorrectionNode = rowdom.getElementsByTagName("gravCorrection")
        if len(gravCorrectionNode) > 0:

            self._gravCorrection = bool(gravCorrectionNode[0].firstChild.data)

            self._gravCorrectionExists = True

        gravOptRangeNode = rowdom.getElementsByTagName("gravOptRange")
        if len(gravOptRangeNode) > 0:

            gravOptRangeStr = gravOptRangeNode[0].firstChild.data
            self._gravOptRange = Parser.stringListToLists(
                gravOptRangeStr, Angle, "CalHolography"
            )

            self._gravOptRangeExists = True

        tempCorrectionNode = rowdom.getElementsByTagName("tempCorrection")
        if len(tempCorrectionNode) > 0:

            self._tempCorrection = bool(tempCorrectionNode[0].firstChild.data)

            self._tempCorrectionExists = True

        tempOptRangeNode = rowdom.getElementsByTagName("tempOptRange")
        if len(tempOptRangeNode) > 0:

            tempOptRangeStr = tempOptRangeNode[0].firstChild.data
            self._tempOptRange = Parser.stringListToLists(
                tempOptRangeStr, Temperature, "CalHolography"
            )

            self._tempOptRangeExists = True

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

    # ===> Attribute focusPosition

    _focusPosition = None  # this is a 1D list of Length

    def getFocusPosition(self):
        """
        Get focusPosition.
        return focusPosition as Length []
        """

        return copy.deepcopy(self._focusPosition)

    def setFocusPosition(self, focusPosition):
        """
        Set focusPosition with the specified Length []  value.
        focusPosition The Length []  value to which focusPosition is to be set.
        The value of focusPosition can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(focusPosition, list):
            raise ValueError("The value of focusPosition must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(focusPosition)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of focusPosition is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(focusPosition, Length):
                raise ValueError(
                    "type of the first value in focusPosition is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._focusPosition = copy.deepcopy(focusPosition)
        except Exception as exc:
            raise ValueError("Invalid focusPosition : " + str(exc))

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

    # ===> Attribute illuminationTaper

    _illuminationTaper = None

    def getIlluminationTaper(self):
        """
        Get illuminationTaper.
        return illuminationTaper as double
        """

        return self._illuminationTaper

    def setIlluminationTaper(self, illuminationTaper):
        """
        Set illuminationTaper with the specified double value.
        illuminationTaper The double value to which illuminationTaper is to be set.


        """

        self._illuminationTaper = double(illuminationTaper)

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

    # ===> Attribute numPanelModes

    _numPanelModes = 0

    def getNumPanelModes(self):
        """
        Get numPanelModes.
        return numPanelModes as int
        """

        return self._numPanelModes

    def setNumPanelModes(self, numPanelModes):
        """
        Set numPanelModes with the specified int value.
        numPanelModes The int value to which numPanelModes is to be set.


        """

        self._numPanelModes = int(numPanelModes)

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

    # ===> Attribute beamMapUID

    _beamMapUID = EntityRef()

    def getBeamMapUID(self):
        """
        Get beamMapUID.
        return beamMapUID as EntityRef
        """

        # make sure it is a copy of EntityRef
        return EntityRef(self._beamMapUID)

    def setBeamMapUID(self, beamMapUID):
        """
        Set beamMapUID with the specified EntityRef value.
        beamMapUID The EntityRef value to which beamMapUID is to be set.
        The value of beamMapUID can be anything allowed by the EntityRef constructor.

        """

        self._beamMapUID = EntityRef(beamMapUID)

    # ===> Attribute rawRMS

    _rawRMS = Length()

    def getRawRMS(self):
        """
        Get rawRMS.
        return rawRMS as Length
        """

        # make sure it is a copy of Length
        return Length(self._rawRMS)

    def setRawRMS(self, rawRMS):
        """
        Set rawRMS with the specified Length value.
        rawRMS The Length value to which rawRMS is to be set.
        The value of rawRMS can be anything allowed by the Length constructor.

        """

        self._rawRMS = Length(rawRMS)

    # ===> Attribute weightedRMS

    _weightedRMS = Length()

    def getWeightedRMS(self):
        """
        Get weightedRMS.
        return weightedRMS as Length
        """

        # make sure it is a copy of Length
        return Length(self._weightedRMS)

    def setWeightedRMS(self, weightedRMS):
        """
        Set weightedRMS with the specified Length value.
        weightedRMS The Length value to which weightedRMS is to be set.
        The value of weightedRMS can be anything allowed by the Length constructor.

        """

        self._weightedRMS = Length(weightedRMS)

    # ===> Attribute surfaceMapUID

    _surfaceMapUID = EntityRef()

    def getSurfaceMapUID(self):
        """
        Get surfaceMapUID.
        return surfaceMapUID as EntityRef
        """

        # make sure it is a copy of EntityRef
        return EntityRef(self._surfaceMapUID)

    def setSurfaceMapUID(self, surfaceMapUID):
        """
        Set surfaceMapUID with the specified EntityRef value.
        surfaceMapUID The EntityRef value to which surfaceMapUID is to be set.
        The value of surfaceMapUID can be anything allowed by the EntityRef constructor.

        """

        self._surfaceMapUID = EntityRef(surfaceMapUID)

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

    # ===> Attribute numScrew, which is optional
    _numScrewExists = False

    _numScrew = 0

    def isNumScrewExists(self):
        """
        The attribute numScrew is optional. Return True if this attribute exists.
        return True if and only if the numScrew attribute exists.
        """
        return self._numScrewExists

    def getNumScrew(self):
        """
        Get numScrew, which is optional.
        return numScrew as int
        raises ValueError If numScrew does not exist.
        """
        if not self._numScrewExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numScrew
                + " attribute in table CalHolography does not exist!"
            )

        return self._numScrew

    def setNumScrew(self, numScrew):
        """
        Set numScrew with the specified int value.
        numScrew The int value to which numScrew is to be set.


        """

        self._numScrew = int(numScrew)

        self._numScrewExists = True

    def clearNumScrew(self):
        """
        Mark numScrew, which is an optional field, as non-existent.
        """
        self._numScrewExists = False

    # ===> Attribute screwName, which is optional
    _screwNameExists = False

    _screwName = None  # this is a 1D list of str

    def isScrewNameExists(self):
        """
        The attribute screwName is optional. Return True if this attribute exists.
        return True if and only if the screwName attribute exists.
        """
        return self._screwNameExists

    def getScrewName(self):
        """
        Get screwName, which is optional.
        return screwName as str []
        raises ValueError If screwName does not exist.
        """
        if not self._screwNameExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + screwName
                + " attribute in table CalHolography does not exist!"
            )

        return copy.deepcopy(self._screwName)

    def setScrewName(self, screwName):
        """
        Set screwName with the specified str []  value.
        screwName The str []  value to which screwName is to be set.


        """

        # value must be a list
        if not isinstance(screwName, list):
            raise ValueError("The value of screwName must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(screwName)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of screwName is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not Parser.checkListType(screwName, str):
                raise ValueError(
                    "type of the first value in screwName is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._screwName = copy.deepcopy(screwName)
        except Exception as exc:
            raise ValueError("Invalid screwName : " + str(exc))

        self._screwNameExists = True

    def clearScrewName(self):
        """
        Mark screwName, which is an optional field, as non-existent.
        """
        self._screwNameExists = False

    # ===> Attribute screwMotion, which is optional
    _screwMotionExists = False

    _screwMotion = None  # this is a 1D list of Length

    def isScrewMotionExists(self):
        """
        The attribute screwMotion is optional. Return True if this attribute exists.
        return True if and only if the screwMotion attribute exists.
        """
        return self._screwMotionExists

    def getScrewMotion(self):
        """
        Get screwMotion, which is optional.
        return screwMotion as Length []
        raises ValueError If screwMotion does not exist.
        """
        if not self._screwMotionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + screwMotion
                + " attribute in table CalHolography does not exist!"
            )

        return copy.deepcopy(self._screwMotion)

    def setScrewMotion(self, screwMotion):
        """
        Set screwMotion with the specified Length []  value.
        screwMotion The Length []  value to which screwMotion is to be set.
        The value of screwMotion can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(screwMotion, list):
            raise ValueError("The value of screwMotion must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(screwMotion)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of screwMotion is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(screwMotion, Length):
                raise ValueError(
                    "type of the first value in screwMotion is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._screwMotion = copy.deepcopy(screwMotion)
        except Exception as exc:
            raise ValueError("Invalid screwMotion : " + str(exc))

        self._screwMotionExists = True

    def clearScrewMotion(self):
        """
        Mark screwMotion, which is an optional field, as non-existent.
        """
        self._screwMotionExists = False

    # ===> Attribute screwMotionError, which is optional
    _screwMotionErrorExists = False

    _screwMotionError = None  # this is a 1D list of Length

    def isScrewMotionErrorExists(self):
        """
        The attribute screwMotionError is optional. Return True if this attribute exists.
        return True if and only if the screwMotionError attribute exists.
        """
        return self._screwMotionErrorExists

    def getScrewMotionError(self):
        """
        Get screwMotionError, which is optional.
        return screwMotionError as Length []
        raises ValueError If screwMotionError does not exist.
        """
        if not self._screwMotionErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + screwMotionError
                + " attribute in table CalHolography does not exist!"
            )

        return copy.deepcopy(self._screwMotionError)

    def setScrewMotionError(self, screwMotionError):
        """
        Set screwMotionError with the specified Length []  value.
        screwMotionError The Length []  value to which screwMotionError is to be set.
        The value of screwMotionError can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(screwMotionError, list):
            raise ValueError("The value of screwMotionError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(screwMotionError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of screwMotionError is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(screwMotionError, Length):
                raise ValueError(
                    "type of the first value in screwMotionError is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._screwMotionError = copy.deepcopy(screwMotionError)
        except Exception as exc:
            raise ValueError("Invalid screwMotionError : " + str(exc))

        self._screwMotionErrorExists = True

    def clearScrewMotionError(self):
        """
        Mark screwMotionError, which is an optional field, as non-existent.
        """
        self._screwMotionErrorExists = False

    # ===> Attribute gravCorrection, which is optional
    _gravCorrectionExists = False

    _gravCorrection = None

    def isGravCorrectionExists(self):
        """
        The attribute gravCorrection is optional. Return True if this attribute exists.
        return True if and only if the gravCorrection attribute exists.
        """
        return self._gravCorrectionExists

    def getGravCorrection(self):
        """
        Get gravCorrection, which is optional.
        return gravCorrection as bool
        raises ValueError If gravCorrection does not exist.
        """
        if not self._gravCorrectionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + gravCorrection
                + " attribute in table CalHolography does not exist!"
            )

        return self._gravCorrection

    def setGravCorrection(self, gravCorrection):
        """
        Set gravCorrection with the specified bool value.
        gravCorrection The bool value to which gravCorrection is to be set.


        """

        self._gravCorrection = bool(gravCorrection)

        self._gravCorrectionExists = True

    def clearGravCorrection(self):
        """
        Mark gravCorrection, which is an optional field, as non-existent.
        """
        self._gravCorrectionExists = False

    # ===> Attribute gravOptRange, which is optional
    _gravOptRangeExists = False

    _gravOptRange = None  # this is a 1D list of Angle

    def isGravOptRangeExists(self):
        """
        The attribute gravOptRange is optional. Return True if this attribute exists.
        return True if and only if the gravOptRange attribute exists.
        """
        return self._gravOptRangeExists

    def getGravOptRange(self):
        """
        Get gravOptRange, which is optional.
        return gravOptRange as Angle []
        raises ValueError If gravOptRange does not exist.
        """
        if not self._gravOptRangeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + gravOptRange
                + " attribute in table CalHolography does not exist!"
            )

        return copy.deepcopy(self._gravOptRange)

    def setGravOptRange(self, gravOptRange):
        """
        Set gravOptRange with the specified Angle []  value.
        gravOptRange The Angle []  value to which gravOptRange is to be set.
        The value of gravOptRange can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(gravOptRange, list):
            raise ValueError("The value of gravOptRange must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(gravOptRange)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of gravOptRange is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(gravOptRange, Angle):
                raise ValueError(
                    "type of the first value in gravOptRange is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._gravOptRange = copy.deepcopy(gravOptRange)
        except Exception as exc:
            raise ValueError("Invalid gravOptRange : " + str(exc))

        self._gravOptRangeExists = True

    def clearGravOptRange(self):
        """
        Mark gravOptRange, which is an optional field, as non-existent.
        """
        self._gravOptRangeExists = False

    # ===> Attribute tempCorrection, which is optional
    _tempCorrectionExists = False

    _tempCorrection = None

    def isTempCorrectionExists(self):
        """
        The attribute tempCorrection is optional. Return True if this attribute exists.
        return True if and only if the tempCorrection attribute exists.
        """
        return self._tempCorrectionExists

    def getTempCorrection(self):
        """
        Get tempCorrection, which is optional.
        return tempCorrection as bool
        raises ValueError If tempCorrection does not exist.
        """
        if not self._tempCorrectionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tempCorrection
                + " attribute in table CalHolography does not exist!"
            )

        return self._tempCorrection

    def setTempCorrection(self, tempCorrection):
        """
        Set tempCorrection with the specified bool value.
        tempCorrection The bool value to which tempCorrection is to be set.


        """

        self._tempCorrection = bool(tempCorrection)

        self._tempCorrectionExists = True

    def clearTempCorrection(self):
        """
        Mark tempCorrection, which is an optional field, as non-existent.
        """
        self._tempCorrectionExists = False

    # ===> Attribute tempOptRange, which is optional
    _tempOptRangeExists = False

    _tempOptRange = None  # this is a 1D list of Temperature

    def isTempOptRangeExists(self):
        """
        The attribute tempOptRange is optional. Return True if this attribute exists.
        return True if and only if the tempOptRange attribute exists.
        """
        return self._tempOptRangeExists

    def getTempOptRange(self):
        """
        Get tempOptRange, which is optional.
        return tempOptRange as Temperature []
        raises ValueError If tempOptRange does not exist.
        """
        if not self._tempOptRangeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tempOptRange
                + " attribute in table CalHolography does not exist!"
            )

        return copy.deepcopy(self._tempOptRange)

    def setTempOptRange(self, tempOptRange):
        """
        Set tempOptRange with the specified Temperature []  value.
        tempOptRange The Temperature []  value to which tempOptRange is to be set.
        The value of tempOptRange can be anything allowed by the Temperature []  constructor.

        """

        # value must be a list
        if not isinstance(tempOptRange, list):
            raise ValueError("The value of tempOptRange must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tempOptRange)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of tempOptRange is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(tempOptRange, Temperature):
                raise ValueError(
                    "type of the first value in tempOptRange is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tempOptRange = copy.deepcopy(tempOptRange)
        except Exception as exc:
            raise ValueError("Invalid tempOptRange : " + str(exc))

        self._tempOptRangeExists = True

    def clearTempOptRange(self):
        """
        Mark tempOptRange, which is an optional field, as non-existent.
        """
        self._tempOptRangeExists = False

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
        calDataId,
        calReductionId,
        antennaMake,
        startValidTime,
        endValidTime,
        ambientTemperature,
        focusPosition,
        frequencyRange,
        illuminationTaper,
        numReceptor,
        polarizationTypes,
        numPanelModes,
        receiverBand,
        beamMapUID,
        rawRMS,
        weightedRMS,
        surfaceMapUID,
        direction,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalHolographyRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaName is a str, compare using the == operator.
        if not (self._antennaName == antennaName):
            return False

        # calDataId is a Tag, compare using the equals method.
        if not self._calDataId.equals(calDataId):
            return False

        # calReductionId is a Tag, compare using the equals method.
        if not self._calReductionId.equals(calReductionId):
            return False

        # antennaMake is a AntennaMake, compare using the == operator on the getValue() output
        if not (self._antennaMake.getValue() == antennaMake.getValue()):
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

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._focusPosition) != len(focusPosition):
            return False
        for indx in range(len(focusPosition)):

            # focusPosition is a list of Length, compare using the almostEquals method.
            if not self._focusPosition[indx].almostEquals(
                focusPosition[indx], self.getTable().getFocusPositionEqTolerance()
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

        # illuminationTaper is a double, compare using the == operator.
        if not (self._illuminationTaper == illuminationTaper):
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

        # numPanelModes is a int, compare using the == operator.
        if not (self._numPanelModes == numPanelModes):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
            return False

        # beamMapUID is a EntityRef, compare using the equals method.
        if not self._beamMapUID.equals(beamMapUID):
            return False

        # rawRMS is a Length, compare using the almostEquals method.
        if not self._rawRMS.almostEquals(
            rawRMS, self.getTable().getRawRMSEqTolerance()
        ):
            return False

        # weightedRMS is a Length, compare using the almostEquals method.
        if not self._weightedRMS.almostEquals(
            weightedRMS, self.getTable().getWeightedRMSEqTolerance()
        ):
            return False

        # surfaceMapUID is a EntityRef, compare using the equals method.
        if not self._surfaceMapUID.equals(surfaceMapUID):
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

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getAntennaMake(),
            otherRow.getStartValidTime(),
            otherRow.getEndValidTime(),
            otherRow.getAmbientTemperature(),
            otherRow.getFocusPosition(),
            otherRow.getFrequencyRange(),
            otherRow.getIlluminationTaper(),
            otherRow.getNumReceptor(),
            otherRow.getPolarizationTypes(),
            otherRow.getNumPanelModes(),
            otherRow.getReceiverBand(),
            otherRow.getBeamMapUID(),
            otherRow.getRawRMS(),
            otherRow.getWeightedRMS(),
            otherRow.getSurfaceMapUID(),
            otherRow.getDirection(),
        )

    def compareRequiredValue(
        self,
        antennaMake,
        startValidTime,
        endValidTime,
        ambientTemperature,
        focusPosition,
        frequencyRange,
        illuminationTaper,
        numReceptor,
        polarizationTypes,
        numPanelModes,
        receiverBand,
        beamMapUID,
        rawRMS,
        weightedRMS,
        surfaceMapUID,
        direction,
    ):

        # antennaMake is a AntennaMake, compare using the == operator on the getValue() output
        if not (self._antennaMake.getValue() == antennaMake.getValue()):
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

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._focusPosition) != len(focusPosition):
            return False
        for indx in range(len(focusPosition)):

            # focusPosition is a list of Length, compare using the almostEquals method.
            if not self._focusPosition[indx].almostEquals(
                focusPosition[indx], self.getTable().getFocusPositionEqTolerance()
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

        # illuminationTaper is a double, compare using the == operator.
        if not (self._illuminationTaper == illuminationTaper):
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

        # numPanelModes is a int, compare using the == operator.
        if not (self._numPanelModes == numPanelModes):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
            return False

        # beamMapUID is a EntityRef, compare using the equals method.
        if not self._beamMapUID.equals(beamMapUID):
            return False

        # rawRMS is a Length, compare using the almostEquals method.
        if not self._rawRMS.almostEquals(
            rawRMS, self.getTable().getRawRMSEqTolerance()
        ):
            return False

        # weightedRMS is a Length, compare using the almostEquals method.
        if not self._weightedRMS.almostEquals(
            weightedRMS, self.getTable().getWeightedRMSEqTolerance()
        ):
            return False

        # surfaceMapUID is a EntityRef, compare using the equals method.
        if not self._surfaceMapUID.equals(surfaceMapUID):
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

        return True
