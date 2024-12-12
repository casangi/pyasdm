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
# File CalDelayRow.py
#

import pyasdm.CalDelayTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.AtmPhaseCorrection import AtmPhaseCorrection


from pyasdm.enumerations.BasebandName import BasebandName


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.PolarizationType import PolarizationType


from pyasdm.enumerations.ReceiverSideband import ReceiverSideband


from xml.dom import minidom

import copy


class CalDelayRow:
    """
    The CalDelayRow class is a row of a CalDelayTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalDelayRow.
        When row is None, create an empty row attached to table, which must be a CalDelayTable.
        When row is given, copy those values in to the new row. The row argument must be a CalDelayRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalDelayTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._antennaName = None

        self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)

        self._basebandName = BasebandName.from_int(0)

        self._receiverBand = ReceiverBand.from_int(0)

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._refAntennaName = None

        self._numReceptor = 0

        self._delayError = []  # this is a list of float []

        self._delayOffset = []  # this is a list of float []

        self._polarizationTypes = []  # this is a list of PolarizationType []

        self._reducedChiSquared = []  # this is a list of float []

        self._appliedDelay = []  # this is a list of float []

        self._crossDelayOffsetExists = False

        self._crossDelayOffset = None

        self._crossDelayOffsetErrorExists = False

        self._crossDelayOffsetError = None

        self._numSidebandExists = False

        self._numSideband = 0

        self._refFreqExists = False

        self._refFreq = []  # this is a list of Frequency []

        self._refFreqPhaseExists = False

        self._refFreqPhase = []  # this is a list of Angle []

        self._sidebandsExists = False

        self._sidebands = []  # this is a list of ReceiverSideband []

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalDelayRow):
                raise ValueError("row must be a MainRow")

            # copy constructor

            self._antennaName = row._antennaName

            # We force the attribute of the result to be not None
            if row._atmPhaseCorrection is None:
                self._atmPhaseCorrection = AtmPhaseCorrection.from_int(0)
            else:
                self._atmPhaseCorrection = AtmPhaseCorrection(row._atmPhaseCorrection)

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

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            self._refAntennaName = row._refAntennaName

            self._numReceptor = row._numReceptor

            # delayError is a  list , make a deep copy
            self._delayError = copy.deepcopy(row._delayError)

            # delayOffset is a  list , make a deep copy
            self._delayOffset = copy.deepcopy(row._delayOffset)

            # polarizationTypes is a  list , make a deep copy
            self._polarizationTypes = copy.deepcopy(row._polarizationTypes)

            # reducedChiSquared is a  list , make a deep copy
            self._reducedChiSquared = copy.deepcopy(row._reducedChiSquared)

            # appliedDelay is a  list , make a deep copy
            self._appliedDelay = copy.deepcopy(row._appliedDelay)

            # by default set systematically crossDelayOffset's value to something not None

            if row._crossDelayOffsetExists:

                self._crossDelayOffset = row._crossDelayOffset

                self._crossDelayOffsetExists = True

            # by default set systematically crossDelayOffsetError's value to something not None

            if row._crossDelayOffsetErrorExists:

                self._crossDelayOffsetError = row._crossDelayOffsetError

                self._crossDelayOffsetErrorExists = True

            # by default set systematically numSideband's value to something not None

            if row._numSidebandExists:

                self._numSideband = row._numSideband

                self._numSidebandExists = True

            # by default set systematically refFreq's value to something not None

            if row._refFreqExists:

                # refFreq is a list, make a deep copy
                self.refFreq = copy.deepcopy(row.refFreq)

                self._refFreqExists = True

            # by default set systematically refFreqPhase's value to something not None

            if row._refFreqPhaseExists:

                # refFreqPhase is a list, make a deep copy
                self.refFreqPhase = copy.deepcopy(row.refFreqPhase)

                self._refFreqPhaseExists = True

            # by default set systematically sidebands's value to something not None

            if row._sidebandsExists:

                # sidebands is a list, make a deep copy
                self.sidebands = copy.deepcopy(row.sidebands)

                self._sidebandsExists = True

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
            "basebandName", BasebandName.name(self._basebandName)
        )

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.valueToXML("refAntennaName", self._refAntennaName)

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listValueToXML("delayError", self._delayError)

        result += Parser.listValueToXML("delayOffset", self._delayOffset)

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.listValueToXML("reducedChiSquared", self._reducedChiSquared)

        result += Parser.listValueToXML("appliedDelay", self._appliedDelay)

        if self._crossDelayOffsetExists:

            result += Parser.valueToXML("crossDelayOffset", self._crossDelayOffset)

        if self._crossDelayOffsetErrorExists:

            result += Parser.valueToXML(
                "crossDelayOffsetError", self._crossDelayOffsetError
            )

        if self._numSidebandExists:

            result += Parser.valueToXML("numSideband", self._numSideband)

        if self._refFreqExists:

            result += Parser.listExtendedValueToXML("refFreq", self._refFreq)

        if self._refFreqPhaseExists:

            result += Parser.listExtendedValueToXML("refFreqPhase", self._refFreqPhase)

        if self._sidebandsExists:

            result += Parser.listEnumValueToXML("sidebands", self._sidebands)

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
                "xmlrow is not a string or a minidom.Element", "CalDelayTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalDelayTable")

        # intrinsic attribute values

        antennaNameNode = rowdom.getElementsByTagName("antennaName")[0]

        self._antennaName = str(antennaNameNode.firstChild.data.strip())

        atmPhaseCorrectionNode = rowdom.getElementsByTagName("atmPhaseCorrection")[0]

        self._atmPhaseCorrection = AtmPhaseCorrection.newAtmPhaseCorrection(
            atmPhaseCorrectionNode.firstChild.data.strip()
        )

        basebandNameNode = rowdom.getElementsByTagName("basebandName")[0]

        self._basebandName = BasebandName.newBasebandName(
            basebandNameNode.firstChild.data.strip()
        )

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data.strip()
        )

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        refAntennaNameNode = rowdom.getElementsByTagName("refAntennaName")[0]

        self._refAntennaName = str(refAntennaNameNode.firstChild.data.strip())

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        delayErrorNode = rowdom.getElementsByTagName("delayError")[0]

        delayErrorStr = delayErrorNode.firstChild.data.strip()

        self._delayError = Parser.stringListToLists(
            delayErrorStr, float, "CalDelay", False
        )

        delayOffsetNode = rowdom.getElementsByTagName("delayOffset")[0]

        delayOffsetStr = delayOffsetNode.firstChild.data.strip()

        self._delayOffset = Parser.stringListToLists(
            delayOffsetStr, float, "CalDelay", False
        )

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data.strip()
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "CalDelay", False
        )

        reducedChiSquaredNode = rowdom.getElementsByTagName("reducedChiSquared")[0]

        reducedChiSquaredStr = reducedChiSquaredNode.firstChild.data.strip()

        self._reducedChiSquared = Parser.stringListToLists(
            reducedChiSquaredStr, float, "CalDelay", False
        )

        appliedDelayNode = rowdom.getElementsByTagName("appliedDelay")[0]

        appliedDelayStr = appliedDelayNode.firstChild.data.strip()

        self._appliedDelay = Parser.stringListToLists(
            appliedDelayStr, float, "CalDelay", False
        )

        crossDelayOffsetNode = rowdom.getElementsByTagName("crossDelayOffset")
        if len(crossDelayOffsetNode) > 0:

            self._crossDelayOffset = float(
                crossDelayOffsetNode[0].firstChild.data.strip()
            )

            self._crossDelayOffsetExists = True

        crossDelayOffsetErrorNode = rowdom.getElementsByTagName("crossDelayOffsetError")
        if len(crossDelayOffsetErrorNode) > 0:

            self._crossDelayOffsetError = float(
                crossDelayOffsetErrorNode[0].firstChild.data.strip()
            )

            self._crossDelayOffsetErrorExists = True

        numSidebandNode = rowdom.getElementsByTagName("numSideband")
        if len(numSidebandNode) > 0:

            self._numSideband = int(numSidebandNode[0].firstChild.data.strip())

            self._numSidebandExists = True

        refFreqNode = rowdom.getElementsByTagName("refFreq")
        if len(refFreqNode) > 0:

            refFreqStr = refFreqNode[0].firstChild.data.strip()

            self._refFreq = Parser.stringListToLists(
                refFreqStr, Frequency, "CalDelay", True
            )

            self._refFreqExists = True

        refFreqPhaseNode = rowdom.getElementsByTagName("refFreqPhase")
        if len(refFreqPhaseNode) > 0:

            refFreqPhaseStr = refFreqPhaseNode[0].firstChild.data.strip()

            self._refFreqPhase = Parser.stringListToLists(
                refFreqPhaseStr, Angle, "CalDelay", True
            )

            self._refFreqPhaseExists = True

        sidebandsNode = rowdom.getElementsByTagName("sidebands")
        if len(sidebandsNode) > 0:

            sidebandsStr = sidebandsNode[0].firstChild.data.strip()
            self._sidebands = Parser.stringListToLists(
                sidebandsStr, ReceiverSideband, "CalDelay", False
            )

            self._sidebandsExists = True

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

    # ===> Attribute refAntennaName

    _refAntennaName = None

    def getRefAntennaName(self):
        """
        Get refAntennaName.
        return refAntennaName as str
        """

        return self._refAntennaName

    def setRefAntennaName(self, refAntennaName):
        """
        Set refAntennaName with the specified str value.
        refAntennaName The str value to which refAntennaName is to be set.


        """

        self._refAntennaName = str(refAntennaName)

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

    # ===> Attribute delayError

    _delayError = None  # this is a 1D list of float

    def getDelayError(self):
        """
        Get delayError.
        return delayError as float []
        """

        return copy.deepcopy(self._delayError)

    def setDelayError(self, delayError):
        """
        Set delayError with the specified float []  value.
        delayError The float []  value to which delayError is to be set.


        """

        # value must be a list
        if not isinstance(delayError, list):
            raise ValueError("The value of delayError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(delayError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of delayError is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(delayError, float):
                raise ValueError(
                    "type of the first value in delayError is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._delayError = copy.deepcopy(delayError)
        except Exception as exc:
            raise ValueError("Invalid delayError : " + str(exc))

    # ===> Attribute delayOffset

    _delayOffset = None  # this is a 1D list of float

    def getDelayOffset(self):
        """
        Get delayOffset.
        return delayOffset as float []
        """

        return copy.deepcopy(self._delayOffset)

    def setDelayOffset(self, delayOffset):
        """
        Set delayOffset with the specified float []  value.
        delayOffset The float []  value to which delayOffset is to be set.


        """

        # value must be a list
        if not isinstance(delayOffset, list):
            raise ValueError("The value of delayOffset must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(delayOffset)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of delayOffset is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(delayOffset, float):
                raise ValueError(
                    "type of the first value in delayOffset is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._delayOffset = copy.deepcopy(delayOffset)
        except Exception as exc:
            raise ValueError("Invalid delayOffset : " + str(exc))

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
            listDims = Parser.getListDims(reducedChiSquared)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of reducedChiSquared is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(reducedChiSquared, float):
                raise ValueError(
                    "type of the first value in reducedChiSquared is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._reducedChiSquared = copy.deepcopy(reducedChiSquared)
        except Exception as exc:
            raise ValueError("Invalid reducedChiSquared : " + str(exc))

    # ===> Attribute appliedDelay

    _appliedDelay = None  # this is a 1D list of float

    def getAppliedDelay(self):
        """
        Get appliedDelay.
        return appliedDelay as float []
        """

        return copy.deepcopy(self._appliedDelay)

    def setAppliedDelay(self, appliedDelay):
        """
        Set appliedDelay with the specified float []  value.
        appliedDelay The float []  value to which appliedDelay is to be set.


        """

        # value must be a list
        if not isinstance(appliedDelay, list):
            raise ValueError("The value of appliedDelay must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(appliedDelay)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of appliedDelay is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(appliedDelay, float):
                raise ValueError(
                    "type of the first value in appliedDelay is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._appliedDelay = copy.deepcopy(appliedDelay)
        except Exception as exc:
            raise ValueError("Invalid appliedDelay : " + str(exc))

    # ===> Attribute crossDelayOffset, which is optional
    _crossDelayOffsetExists = False

    _crossDelayOffset = None

    def isCrossDelayOffsetExists(self):
        """
        The attribute crossDelayOffset is optional. Return True if this attribute exists.
        return True if and only if the crossDelayOffset attribute exists.
        """
        return self._crossDelayOffsetExists

    def getCrossDelayOffset(self):
        """
        Get crossDelayOffset, which is optional.
        return crossDelayOffset as float
        raises ValueError If crossDelayOffset does not exist.
        """
        if not self._crossDelayOffsetExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + crossDelayOffset
                + " attribute in table CalDelay does not exist!"
            )

        return self._crossDelayOffset

    def setCrossDelayOffset(self, crossDelayOffset):
        """
        Set crossDelayOffset with the specified float value.
        crossDelayOffset The float value to which crossDelayOffset is to be set.


        """

        self._crossDelayOffset = float(crossDelayOffset)

        self._crossDelayOffsetExists = True

    def clearCrossDelayOffset(self):
        """
        Mark crossDelayOffset, which is an optional field, as non-existent.
        """
        self._crossDelayOffsetExists = False

    # ===> Attribute crossDelayOffsetError, which is optional
    _crossDelayOffsetErrorExists = False

    _crossDelayOffsetError = None

    def isCrossDelayOffsetErrorExists(self):
        """
        The attribute crossDelayOffsetError is optional. Return True if this attribute exists.
        return True if and only if the crossDelayOffsetError attribute exists.
        """
        return self._crossDelayOffsetErrorExists

    def getCrossDelayOffsetError(self):
        """
        Get crossDelayOffsetError, which is optional.
        return crossDelayOffsetError as float
        raises ValueError If crossDelayOffsetError does not exist.
        """
        if not self._crossDelayOffsetErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + crossDelayOffsetError
                + " attribute in table CalDelay does not exist!"
            )

        return self._crossDelayOffsetError

    def setCrossDelayOffsetError(self, crossDelayOffsetError):
        """
        Set crossDelayOffsetError with the specified float value.
        crossDelayOffsetError The float value to which crossDelayOffsetError is to be set.


        """

        self._crossDelayOffsetError = float(crossDelayOffsetError)

        self._crossDelayOffsetErrorExists = True

    def clearCrossDelayOffsetError(self):
        """
        Mark crossDelayOffsetError, which is an optional field, as non-existent.
        """
        self._crossDelayOffsetErrorExists = False

    # ===> Attribute numSideband, which is optional
    _numSidebandExists = False

    _numSideband = 0

    def isNumSidebandExists(self):
        """
        The attribute numSideband is optional. Return True if this attribute exists.
        return True if and only if the numSideband attribute exists.
        """
        return self._numSidebandExists

    def getNumSideband(self):
        """
        Get numSideband, which is optional.
        return numSideband as int
        raises ValueError If numSideband does not exist.
        """
        if not self._numSidebandExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numSideband
                + " attribute in table CalDelay does not exist!"
            )

        return self._numSideband

    def setNumSideband(self, numSideband):
        """
        Set numSideband with the specified int value.
        numSideband The int value to which numSideband is to be set.


        """

        self._numSideband = int(numSideband)

        self._numSidebandExists = True

    def clearNumSideband(self):
        """
        Mark numSideband, which is an optional field, as non-existent.
        """
        self._numSidebandExists = False

    # ===> Attribute refFreq, which is optional
    _refFreqExists = False

    _refFreq = None  # this is a 1D list of Frequency

    def isRefFreqExists(self):
        """
        The attribute refFreq is optional. Return True if this attribute exists.
        return True if and only if the refFreq attribute exists.
        """
        return self._refFreqExists

    def getRefFreq(self):
        """
        Get refFreq, which is optional.
        return refFreq as Frequency []
        raises ValueError If refFreq does not exist.
        """
        if not self._refFreqExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + refFreq
                + " attribute in table CalDelay does not exist!"
            )

        return copy.deepcopy(self._refFreq)

    def setRefFreq(self, refFreq):
        """
        Set refFreq with the specified Frequency []  value.
        refFreq The Frequency []  value to which refFreq is to be set.
        The value of refFreq can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(refFreq, list):
            raise ValueError("The value of refFreq must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(refFreq)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of refFreq is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(refFreq, Frequency):
                raise ValueError(
                    "type of the first value in refFreq is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._refFreq = copy.deepcopy(refFreq)
        except Exception as exc:
            raise ValueError("Invalid refFreq : " + str(exc))

        self._refFreqExists = True

    def clearRefFreq(self):
        """
        Mark refFreq, which is an optional field, as non-existent.
        """
        self._refFreqExists = False

    # ===> Attribute refFreqPhase, which is optional
    _refFreqPhaseExists = False

    _refFreqPhase = None  # this is a 1D list of Angle

    def isRefFreqPhaseExists(self):
        """
        The attribute refFreqPhase is optional. Return True if this attribute exists.
        return True if and only if the refFreqPhase attribute exists.
        """
        return self._refFreqPhaseExists

    def getRefFreqPhase(self):
        """
        Get refFreqPhase, which is optional.
        return refFreqPhase as Angle []
        raises ValueError If refFreqPhase does not exist.
        """
        if not self._refFreqPhaseExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + refFreqPhase
                + " attribute in table CalDelay does not exist!"
            )

        return copy.deepcopy(self._refFreqPhase)

    def setRefFreqPhase(self, refFreqPhase):
        """
        Set refFreqPhase with the specified Angle []  value.
        refFreqPhase The Angle []  value to which refFreqPhase is to be set.
        The value of refFreqPhase can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(refFreqPhase, list):
            raise ValueError("The value of refFreqPhase must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(refFreqPhase)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of refFreqPhase is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not Parser.checkListType(refFreqPhase, Angle):
                raise ValueError(
                    "type of the first value in refFreqPhase is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._refFreqPhase = copy.deepcopy(refFreqPhase)
        except Exception as exc:
            raise ValueError("Invalid refFreqPhase : " + str(exc))

        self._refFreqPhaseExists = True

    def clearRefFreqPhase(self):
        """
        Mark refFreqPhase, which is an optional field, as non-existent.
        """
        self._refFreqPhaseExists = False

    # ===> Attribute sidebands, which is optional
    _sidebandsExists = False

    _sidebands = None  # this is a 1D list of ReceiverSideband

    def isSidebandsExists(self):
        """
        The attribute sidebands is optional. Return True if this attribute exists.
        return True if and only if the sidebands attribute exists.
        """
        return self._sidebandsExists

    def getSidebands(self):
        """
        Get sidebands, which is optional.
        return sidebands as ReceiverSideband []
        raises ValueError If sidebands does not exist.
        """
        if not self._sidebandsExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sidebands
                + " attribute in table CalDelay does not exist!"
            )

        return copy.deepcopy(self._sidebands)

    def setSidebands(self, sidebands):
        """
        Set sidebands with the specified ReceiverSideband []  value.
        sidebands The ReceiverSideband []  value to which sidebands is to be set.


        """

        # value must be a list
        if not isinstance(sidebands, list):
            raise ValueError("The value of sidebands must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(sidebands)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of sidebands is not correct")

            # the type of the values in the list must be ReceiverSideband
            # note : this only checks the first value found
            if not Parser.checkListType(sidebands, ReceiverSideband):
                raise ValueError(
                    "type of the first value in sidebands is not ReceiverSideband as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._sidebands = copy.deepcopy(sidebands)
        except Exception as exc:
            raise ValueError("Invalid sidebands : " + str(exc))

        self._sidebandsExists = True

    def clearSidebands(self):
        """
        Mark sidebands, which is an optional field, as non-existent.
        """
        self._sidebandsExists = False

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
        basebandName,
        receiverBand,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        refAntennaName,
        numReceptor,
        delayError,
        delayOffset,
        polarizationTypes,
        reducedChiSquared,
        appliedDelay,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalDelayRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaName is a str, compare using the == operator.
        if not (self._antennaName == antennaName):
            return False

        # atmPhaseCorrection is a AtmPhaseCorrection, compare using the == operator on the getValue() output
        if not (self._atmPhaseCorrection.getValue() == atmPhaseCorrection.getValue()):
            return False

        # basebandName is a BasebandName, compare using the == operator on the getValue() output
        if not (self._basebandName.getValue() == basebandName.getValue()):
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

        # refAntennaName is a str, compare using the == operator.
        if not (self._refAntennaName == refAntennaName):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._delayError) != len(delayError):
            return False
        for indx in range(len(delayError)):

            # delayError is a list of float, compare using == operator.
            if not (self._delayError[indx] == delayError[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._delayOffset) != len(delayOffset):
            return False
        for indx in range(len(delayOffset)):

            # delayOffset is a list of float, compare using == operator.
            if not (self._delayOffset[indx] == delayOffset[indx]):
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
        if len(self._reducedChiSquared) != len(reducedChiSquared):
            return False
        for indx in range(len(reducedChiSquared)):

            # reducedChiSquared is a list of float, compare using == operator.
            if not (self._reducedChiSquared[indx] == reducedChiSquared[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._appliedDelay) != len(appliedDelay):
            return False
        for indx in range(len(appliedDelay)):

            # appliedDelay is a list of float, compare using == operator.
            if not (self._appliedDelay[indx] == appliedDelay[indx]):
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
            otherRow.getRefAntennaName(),
            otherRow.getNumReceptor(),
            otherRow.getDelayError(),
            otherRow.getDelayOffset(),
            otherRow.getPolarizationTypes(),
            otherRow.getReducedChiSquared(),
            otherRow.getAppliedDelay(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        refAntennaName,
        numReceptor,
        delayError,
        delayOffset,
        polarizationTypes,
        reducedChiSquared,
        appliedDelay,
    ):

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # refAntennaName is a str, compare using the == operator.
        if not (self._refAntennaName == refAntennaName):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._delayError) != len(delayError):
            return False
        for indx in range(len(delayError)):

            # delayError is a list of float, compare using == operator.
            if not (self._delayError[indx] == delayError[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._delayOffset) != len(delayOffset):
            return False
        for indx in range(len(delayOffset)):

            # delayOffset is a list of float, compare using == operator.
            if not (self._delayOffset[indx] == delayOffset[indx]):
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
        if len(self._reducedChiSquared) != len(reducedChiSquared):
            return False
        for indx in range(len(reducedChiSquared)):

            # reducedChiSquared is a list of float, compare using == operator.
            if not (self._reducedChiSquared[indx] == reducedChiSquared[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._appliedDelay) != len(appliedDelay):
            return False
        for indx in range(len(appliedDelay)):

            # appliedDelay is a list of float, compare using == operator.
            if not (self._appliedDelay[indx] == appliedDelay[indx]):
                return False

        return True
