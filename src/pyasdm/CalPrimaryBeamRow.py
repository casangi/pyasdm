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
# File CalPrimaryBeamRow.py
#

import pyasdm.CalPrimaryBeamTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.AntennaMake import AntennaMake


from pyasdm.enumerations.PolarizationType import PolarizationType


from pyasdm.enumerations.PrimaryBeamDescription import PrimaryBeamDescription


from xml.dom import minidom

import copy


class CalPrimaryBeamRow:
    """
    The CalPrimaryBeamRow class is a row of a CalPrimaryBeamTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalPrimaryBeamRow.
        When row is None, create an empty row attached to table, which must be a CalPrimaryBeamTable.
        When row is given, copy those values in to the new row. The row argument must be a CalPrimaryBeamRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalPrimaryBeamTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._receiverBand = ReceiverBand.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._antennaMake = AntennaMake.from_int(0)

        # this is a list of PolarizationType Enumeration, start off with it being empty
        self._polarizationTypes = []

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._descriptionType = PrimaryBeamDescription.from_int(0)

        if row is not None:
            if not isinstance(row, CalPrimaryBeamRow):
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

            self._numSubband = row._numSubband

            # frequencyRange is a  list , make a deep copy
            self._frequencyRange = copy.deepcopy(row._frequencyRange)

            self._numReceptor = row._numReceptor

            # polarizationTypes is a  list , make a deep copy
            self._polarizationTypes = copy.deepcopy(row._polarizationTypes)

            # mainBeamEfficiency is a  list , make a deep copy
            self._mainBeamEfficiency = copy.deepcopy(row._mainBeamEfficiency)

            self._beamDescriptionUID = EntityRef(row._beamDescriptionUID)

            self._relativeAmplitudeRms = row._relativeAmplitudeRms

            # direction is a  list , make a deep copy
            self._direction = copy.deepcopy(row._direction)

            # minValidDirection is a  list , make a deep copy
            self._minValidDirection = copy.deepcopy(row._minValidDirection)

            # maxValidDirection is a  list , make a deep copy
            self._maxValidDirection = copy.deepcopy(row._maxValidDirection)

            # We force the attribute of the result to be not None
            if row._descriptionType is None:
                self._descriptionType = PrimaryBeamDescription.from_int(0)
            else:
                self._descriptionType = PrimaryBeamDescription(row._descriptionType)

            # imageChannelNumber is a  list , make a deep copy
            self._imageChannelNumber = copy.deepcopy(row._imageChannelNumber)

            # imageNominalFrequency is a  list , make a deep copy
            self._imageNominalFrequency = copy.deepcopy(row._imageNominalFrequency)

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

        result += Parser.valueToXML("numSubband", self._numSubband)

        result += Parser.listExtendedValueToXML("frequencyRange", self._frequencyRange)

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.listValueToXML("mainBeamEfficiency", self._mainBeamEfficiency)

        result += Parser.extendedValueToXML(
            "beamDescriptionUID", self._beamDescriptionUID
        )

        result += Parser.valueToXML("relativeAmplitudeRms", self._relativeAmplitudeRms)

        result += Parser.listExtendedValueToXML("direction", self._direction)

        result += Parser.listExtendedValueToXML(
            "minValidDirection", self._minValidDirection
        )

        result += Parser.listExtendedValueToXML(
            "maxValidDirection", self._maxValidDirection
        )

        result += Parser.valueToXML(
            "descriptionType", PrimaryBeamDescription.name(self._descriptionType)
        )

        result += Parser.listValueToXML("imageChannelNumber", self._imageChannelNumber)

        result += Parser.listExtendedValueToXML(
            "imageNominalFrequency", self._imageNominalFrequency
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
                "xmlrow is not a string or a minidom.Element", "CalPrimaryBeamTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException(
                "the argument is not a row", "CalPrimaryBeamTable"
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

        numSubbandNode = rowdom.getElementsByTagName("numSubband")[0]

        self._numSubband = int(numSubbandNode.firstChild.data)

        frequencyRangeNode = rowdom.getElementsByTagName("frequencyRange")[0]

        frequencyRangeStr = frequencyRangeNode.firstChild.data
        self._frequencyRange = Parser.stringListToLists(
            frequencyRangeStr, Frequency, "CalPrimaryBeam"
        )

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data)

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "CalPrimaryBeam"
        )

        mainBeamEfficiencyNode = rowdom.getElementsByTagName("mainBeamEfficiency")[0]

        mainBeamEfficiencyStr = mainBeamEfficiencyNode.firstChild.data
        self._mainBeamEfficiency = Parser.stringListToLists(
            mainBeamEfficiencyStr, double, "CalPrimaryBeam"
        )

        beamDescriptionUIDNode = rowdom.getElementsByTagName("beamDescriptionUID")[0]

        self._beamDescriptionUID = EntityRef(beamDescriptionUIDNode.toxml())

        relativeAmplitudeRmsNode = rowdom.getElementsByTagName("relativeAmplitudeRms")[
            0
        ]

        self._relativeAmplitudeRms = float(relativeAmplitudeRmsNode.firstChild.data)

        directionNode = rowdom.getElementsByTagName("direction")[0]

        directionStr = directionNode.firstChild.data
        self._direction = Parser.stringListToLists(
            directionStr, Angle, "CalPrimaryBeam"
        )

        minValidDirectionNode = rowdom.getElementsByTagName("minValidDirection")[0]

        minValidDirectionStr = minValidDirectionNode.firstChild.data
        self._minValidDirection = Parser.stringListToLists(
            minValidDirectionStr, Angle, "CalPrimaryBeam"
        )

        maxValidDirectionNode = rowdom.getElementsByTagName("maxValidDirection")[0]

        maxValidDirectionStr = maxValidDirectionNode.firstChild.data
        self._maxValidDirection = Parser.stringListToLists(
            maxValidDirectionStr, Angle, "CalPrimaryBeam"
        )

        descriptionTypeNode = rowdom.getElementsByTagName("descriptionType")[0]

        self._descriptionType = PrimaryBeamDescription.newPrimaryBeamDescription(
            descriptionTypeNode.firstChild.data
        )

        imageChannelNumberNode = rowdom.getElementsByTagName("imageChannelNumber")[0]

        imageChannelNumberStr = imageChannelNumberNode.firstChild.data
        self._imageChannelNumber = Parser.stringListToLists(
            imageChannelNumberStr, int, "CalPrimaryBeam"
        )

        imageNominalFrequencyNode = rowdom.getElementsByTagName(
            "imageNominalFrequency"
        )[0]

        imageNominalFrequencyStr = imageNominalFrequencyNode.firstChild.data
        self._imageNominalFrequency = Parser.stringListToLists(
            imageNominalFrequencyStr, Frequency, "CalPrimaryBeam"
        )

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

    # ===> Attribute numSubband

    _numSubband = 0

    def getNumSubband(self):
        """
        Get numSubband.
        return numSubband as int
        """

        return self._numSubband

    def setNumSubband(self, numSubband):
        """
        Set numSubband with the specified int value.
        numSubband The int value to which numSubband is to be set.


        """

        self._numSubband = int(numSubband)

    # ===> Attribute frequencyRange

    _frequencyRange = None  # this is a 2D list of Frequency

    def getFrequencyRange(self):
        """
        Get frequencyRange.
        return frequencyRange as Frequency []  []
        """

        return copy.deepcopy(self._frequencyRange)

    def setFrequencyRange(self, frequencyRange):
        """
        Set frequencyRange with the specified Frequency []  []  value.
        frequencyRange The Frequency []  []  value to which frequencyRange is to be set.
        The value of frequencyRange can be anything allowed by the Frequency []  []  constructor.

        """

        # value must be a list
        if not isinstance(frequencyRange, list):
            raise ValueError("The value of frequencyRange must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(frequencyRange)

            shapeOK = len(listDims) == 2

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

    # ===> Attribute mainBeamEfficiency

    _mainBeamEfficiency = None  # this is a 1D list of double

    def getMainBeamEfficiency(self):
        """
        Get mainBeamEfficiency.
        return mainBeamEfficiency as double []
        """

        return copy.deepcopy(self._mainBeamEfficiency)

    def setMainBeamEfficiency(self, mainBeamEfficiency):
        """
        Set mainBeamEfficiency with the specified double []  value.
        mainBeamEfficiency The double []  value to which mainBeamEfficiency is to be set.


        """

        # value must be a list
        if not isinstance(mainBeamEfficiency, list):
            raise ValueError("The value of mainBeamEfficiency must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(mainBeamEfficiency)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of mainBeamEfficiency is not correct")

            # the type of the values in the list must be double
            # note : this only checks the first value found
            if not Parser.checkListType(mainBeamEfficiency, double):
                raise ValueError(
                    "type of the first value in mainBeamEfficiency is not double as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._mainBeamEfficiency = copy.deepcopy(mainBeamEfficiency)
        except Exception as exc:
            raise ValueError("Invalid mainBeamEfficiency : " + str(exc))

    # ===> Attribute beamDescriptionUID

    _beamDescriptionUID = EntityRef()

    def getBeamDescriptionUID(self):
        """
        Get beamDescriptionUID.
        return beamDescriptionUID as EntityRef
        """

        # make sure it is a copy of EntityRef
        return EntityRef(self._beamDescriptionUID)

    def setBeamDescriptionUID(self, beamDescriptionUID):
        """
        Set beamDescriptionUID with the specified EntityRef value.
        beamDescriptionUID The EntityRef value to which beamDescriptionUID is to be set.
        The value of beamDescriptionUID can be anything allowed by the EntityRef constructor.

        """

        self._beamDescriptionUID = EntityRef(beamDescriptionUID)

    # ===> Attribute relativeAmplitudeRms

    _relativeAmplitudeRms = None

    def getRelativeAmplitudeRms(self):
        """
        Get relativeAmplitudeRms.
        return relativeAmplitudeRms as float
        """

        return self._relativeAmplitudeRms

    def setRelativeAmplitudeRms(self, relativeAmplitudeRms):
        """
        Set relativeAmplitudeRms with the specified float value.
        relativeAmplitudeRms The float value to which relativeAmplitudeRms is to be set.


        """

        self._relativeAmplitudeRms = float(relativeAmplitudeRms)

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

    # ===> Attribute minValidDirection

    _minValidDirection = None  # this is a 1D list of Angle

    def getMinValidDirection(self):
        """
        Get minValidDirection.
        return minValidDirection as Angle []
        """

        return copy.deepcopy(self._minValidDirection)

    def setMinValidDirection(self, minValidDirection):
        """
        Set minValidDirection with the specified Angle []  value.
        minValidDirection The Angle []  value to which minValidDirection is to be set.
        The value of minValidDirection can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(minValidDirection, list):
            raise ValueError("The value of minValidDirection must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(minValidDirection)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of minValidDirection is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(minValidDirection, Angle):
                raise ValueError(
                    "type of the first value in minValidDirection is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._minValidDirection = copy.deepcopy(minValidDirection)
        except Exception as exc:
            raise ValueError("Invalid minValidDirection : " + str(exc))

    # ===> Attribute maxValidDirection

    _maxValidDirection = None  # this is a 1D list of Angle

    def getMaxValidDirection(self):
        """
        Get maxValidDirection.
        return maxValidDirection as Angle []
        """

        return copy.deepcopy(self._maxValidDirection)

    def setMaxValidDirection(self, maxValidDirection):
        """
        Set maxValidDirection with the specified Angle []  value.
        maxValidDirection The Angle []  value to which maxValidDirection is to be set.
        The value of maxValidDirection can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(maxValidDirection, list):
            raise ValueError("The value of maxValidDirection must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(maxValidDirection)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of maxValidDirection is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(maxValidDirection, Angle):
                raise ValueError(
                    "type of the first value in maxValidDirection is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._maxValidDirection = copy.deepcopy(maxValidDirection)
        except Exception as exc:
            raise ValueError("Invalid maxValidDirection : " + str(exc))

    # ===> Attribute descriptionType

    _descriptionType = PrimaryBeamDescription.from_int(0)

    def getDescriptionType(self):
        """
        Get descriptionType.
        return descriptionType as PrimaryBeamDescription
        """

        return self._descriptionType

    def setDescriptionType(self, descriptionType):
        """
        Set descriptionType with the specified PrimaryBeamDescription value.
        descriptionType The PrimaryBeamDescription value to which descriptionType is to be set.


        """

        self._descriptionType = PrimaryBeamDescription(descriptionType)

    # ===> Attribute imageChannelNumber

    _imageChannelNumber = None  # this is a 1D list of int

    def getImageChannelNumber(self):
        """
        Get imageChannelNumber.
        return imageChannelNumber as int []
        """

        return copy.deepcopy(self._imageChannelNumber)

    def setImageChannelNumber(self, imageChannelNumber):
        """
        Set imageChannelNumber with the specified int []  value.
        imageChannelNumber The int []  value to which imageChannelNumber is to be set.


        """

        # value must be a list
        if not isinstance(imageChannelNumber, list):
            raise ValueError("The value of imageChannelNumber must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(imageChannelNumber)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of imageChannelNumber is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not Parser.checkListType(imageChannelNumber, int):
                raise ValueError(
                    "type of the first value in imageChannelNumber is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._imageChannelNumber = copy.deepcopy(imageChannelNumber)
        except Exception as exc:
            raise ValueError("Invalid imageChannelNumber : " + str(exc))

    # ===> Attribute imageNominalFrequency

    _imageNominalFrequency = None  # this is a 1D list of Frequency

    def getImageNominalFrequency(self):
        """
        Get imageNominalFrequency.
        return imageNominalFrequency as Frequency []
        """

        return copy.deepcopy(self._imageNominalFrequency)

    def setImageNominalFrequency(self, imageNominalFrequency):
        """
        Set imageNominalFrequency with the specified Frequency []  value.
        imageNominalFrequency The Frequency []  value to which imageNominalFrequency is to be set.
        The value of imageNominalFrequency can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(imageNominalFrequency, list):
            raise ValueError("The value of imageNominalFrequency must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(imageNominalFrequency)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of imageNominalFrequency is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(imageNominalFrequency, Frequency):
                raise ValueError(
                    "type of the first value in imageNominalFrequency is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._imageNominalFrequency = copy.deepcopy(imageNominalFrequency)
        except Exception as exc:
            raise ValueError("Invalid imageNominalFrequency : " + str(exc))

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
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        antennaMake,
        numSubband,
        frequencyRange,
        numReceptor,
        polarizationTypes,
        mainBeamEfficiency,
        beamDescriptionUID,
        relativeAmplitudeRms,
        direction,
        minValidDirection,
        maxValidDirection,
        descriptionType,
        imageChannelNumber,
        imageNominalFrequency,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalPrimaryBeamRow with
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

        # numSubband is a int, compare using the == operator.
        if not (self._numSubband == numSubband):
            return False

        # We compare two 2D arrays (lists)
        if frequencyRange is not None:
            if self._frequencyRange is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            frequencyRange_dims = Parser.getListDims(frequencyRange)
            this_frequencyRange_dims = Parser.getListDims(self._frequencyRange)
            if frequencyRange_dims != this_frequencyRange_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(frequencyRange_dims[0]):
                for j in range(frequencyRange_dims[0]):

                    # frequencyRange is a Frequency, compare using the almostEquals method.
                    if not (
                        self._frequencyRange[i][j].almostEquals(
                            frequencyRange[i][j],
                            this.getTable().getFrequencyRangeEqTolerance(),
                        )
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
        if len(self._mainBeamEfficiency) != len(mainBeamEfficiency):
            return False
        for indx in range(len(mainBeamEfficiency)):

            # mainBeamEfficiency is a list of double, compare using == operator.
            if not (self._mainBeamEfficiency[indx] == mainBeamEfficiency[indx]):
                return False

        # beamDescriptionUID is a EntityRef, compare using the equals method.
        if not self._beamDescriptionUID.equals(beamDescriptionUID):
            return False

        # relativeAmplitudeRms is a float, compare using the == operator.
        if not (self._relativeAmplitudeRms == relativeAmplitudeRms):
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
        if len(self._minValidDirection) != len(minValidDirection):
            return False
        for indx in range(len(minValidDirection)):

            # minValidDirection is a list of Angle, compare using the almostEquals method.
            if not self._minValidDirection[indx].almostEquals(
                minValidDirection[indx],
                self.getTable().getMinValidDirectionEqTolerance(),
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._maxValidDirection) != len(maxValidDirection):
            return False
        for indx in range(len(maxValidDirection)):

            # maxValidDirection is a list of Angle, compare using the almostEquals method.
            if not self._maxValidDirection[indx].almostEquals(
                maxValidDirection[indx],
                self.getTable().getMaxValidDirectionEqTolerance(),
            ):
                return False

        # descriptionType is a PrimaryBeamDescription, compare using the == operator on the getValue() output
        if not (self._descriptionType.getValue() == descriptionType.getValue()):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._imageChannelNumber) != len(imageChannelNumber):
            return False
        for indx in range(len(imageChannelNumber)):

            # imageChannelNumber is a list of int, compare using == operator.
            if not (self._imageChannelNumber[indx] == imageChannelNumber[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._imageNominalFrequency) != len(imageNominalFrequency):
            return False
        for indx in range(len(imageNominalFrequency)):

            # imageNominalFrequency is a list of Frequency, compare using the almostEquals method.
            if not self._imageNominalFrequency[indx].almostEquals(
                imageNominalFrequency[indx],
                self.getTable().getImageNominalFrequencyEqTolerance(),
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
            otherRow.getAntennaMake(),
            otherRow.getNumSubband(),
            otherRow.getFrequencyRange(),
            otherRow.getNumReceptor(),
            otherRow.getPolarizationTypes(),
            otherRow.getMainBeamEfficiency(),
            otherRow.getBeamDescriptionUID(),
            otherRow.getRelativeAmplitudeRms(),
            otherRow.getDirection(),
            otherRow.getMinValidDirection(),
            otherRow.getMaxValidDirection(),
            otherRow.getDescriptionType(),
            otherRow.getImageChannelNumber(),
            otherRow.getImageNominalFrequency(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        antennaMake,
        numSubband,
        frequencyRange,
        numReceptor,
        polarizationTypes,
        mainBeamEfficiency,
        beamDescriptionUID,
        relativeAmplitudeRms,
        direction,
        minValidDirection,
        maxValidDirection,
        descriptionType,
        imageChannelNumber,
        imageNominalFrequency,
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

        # numSubband is a int, compare using the == operator.
        if not (self._numSubband == numSubband):
            return False

        # We compare two 2D arrays (lists)
        if frequencyRange is not None:
            if self._frequencyRange is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            frequencyRange_dims = Parser.getListDims(frequencyRange)
            this_frequencyRange_dims = Parser.getListDims(self._frequencyRange)
            if frequencyRange_dims != this_frequencyRange_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(frequencyRange_dims[0]):
                for j in range(frequencyRange_dims[0]):

                    # frequencyRange is a Frequency, compare using the almostEquals method.
                    if not (
                        self._frequencyRange[i][j].almostEquals(
                            frequencyRange[i][j],
                            this.getTable().getFrequencyRangeEqTolerance(),
                        )
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
        if len(self._mainBeamEfficiency) != len(mainBeamEfficiency):
            return False
        for indx in range(len(mainBeamEfficiency)):

            # mainBeamEfficiency is a list of double, compare using == operator.
            if not (self._mainBeamEfficiency[indx] == mainBeamEfficiency[indx]):
                return False

        # beamDescriptionUID is a EntityRef, compare using the equals method.
        if not self._beamDescriptionUID.equals(beamDescriptionUID):
            return False

        # relativeAmplitudeRms is a float, compare using the == operator.
        if not (self._relativeAmplitudeRms == relativeAmplitudeRms):
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
        if len(self._minValidDirection) != len(minValidDirection):
            return False
        for indx in range(len(minValidDirection)):

            # minValidDirection is a list of Angle, compare using the almostEquals method.
            if not self._minValidDirection[indx].almostEquals(
                minValidDirection[indx],
                self.getTable().getMinValidDirectionEqTolerance(),
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._maxValidDirection) != len(maxValidDirection):
            return False
        for indx in range(len(maxValidDirection)):

            # maxValidDirection is a list of Angle, compare using the almostEquals method.
            if not self._maxValidDirection[indx].almostEquals(
                maxValidDirection[indx],
                self.getTable().getMaxValidDirectionEqTolerance(),
            ):
                return False

        # descriptionType is a PrimaryBeamDescription, compare using the == operator on the getValue() output
        if not (self._descriptionType.getValue() == descriptionType.getValue()):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._imageChannelNumber) != len(imageChannelNumber):
            return False
        for indx in range(len(imageChannelNumber)):

            # imageChannelNumber is a list of int, compare using == operator.
            if not (self._imageChannelNumber[indx] == imageChannelNumber[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._imageNominalFrequency) != len(imageNominalFrequency):
            return False
        for indx in range(len(imageNominalFrequency)):

            # imageNominalFrequency is a list of Frequency, compare using the almostEquals method.
            if not self._imageNominalFrequency[indx].almostEquals(
                imageNominalFrequency[indx],
                self.getTable().getImageNominalFrequencyEqTolerance(),
            ):
                return False

        return True
