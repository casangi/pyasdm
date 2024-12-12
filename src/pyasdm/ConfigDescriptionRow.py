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
# File ConfigDescriptionRow.py
#

import pyasdm.ConfigDescriptionTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.CorrelationMode import CorrelationMode


from pyasdm.enumerations.AtmPhaseCorrection import AtmPhaseCorrection


from pyasdm.enumerations.ProcessorType import ProcessorType


from pyasdm.enumerations.SpectralResolutionType import SpectralResolutionType


from pyasdm.enumerations.SpectralResolutionType import SpectralResolutionType


from xml.dom import minidom

import copy


class ConfigDescriptionRow:
    """
    The ConfigDescriptionRow class is a row of a ConfigDescriptionTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a ConfigDescriptionRow.
        When row is None, create an empty row attached to table, which must be a ConfigDescriptionTable.
        When row is given, copy those values in to the new row. The row argument must be a ConfigDescriptionRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.ConfigDescriptionTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._numAntenna = 0

        self._numDataDescription = 0

        self._numFeed = 0

        self._correlationMode = CorrelationMode.from_int(0)

        self._configDescriptionId = Tag()

        self._numAtmPhaseCorrection = 0

        self._atmPhaseCorrection = []  # this is a list of AtmPhaseCorrection []

        self._processorType = ProcessorType.from_int(0)

        self._phasedArrayListExists = False

        self._phasedArrayList = []  # this is a list of int []

        self._spectralType = SpectralResolutionType.from_int(0)

        self._numAssocValuesExists = False

        self._numAssocValues = 0

        self._assocNatureExists = False

        self._assocNature = []  # this is a list of SpectralResolutionType []

        # extrinsic attributes

        self._antennaId = []  # this is a list of Tag []

        self._assocConfigDescriptionIdExists = False

        self._assocConfigDescriptionId = []  # this is a list of Tag []

        self._dataDescriptionId = []  # this is a list of Tag []

        self._feedId = []  # this is a list of int []

        self._processorId = Tag()

        self._switchCycleId = []  # this is a list of Tag []

        if row is not None:
            if not isinstance(row, ConfigDescriptionRow):
                raise ValueError("row must be a MainRow")

            # copy constructor

            self._configDescriptionId = Tag(row._configDescriptionId)

            self._numAntenna = row._numAntenna

            self._numDataDescription = row._numDataDescription

            self._numFeed = row._numFeed

            # We force the attribute of the result to be not None
            if row._correlationMode is None:
                self._correlationMode = CorrelationMode.from_int(0)
            else:
                self._correlationMode = CorrelationMode(row._correlationMode)

            self._numAtmPhaseCorrection = row._numAtmPhaseCorrection

            # atmPhaseCorrection is a  list , make a deep copy
            self._atmPhaseCorrection = copy.deepcopy(row._atmPhaseCorrection)

            # We force the attribute of the result to be not None
            if row._processorType is None:
                self._processorType = ProcessorType.from_int(0)
            else:
                self._processorType = ProcessorType(row._processorType)

            # We force the attribute of the result to be not None
            if row._spectralType is None:
                self._spectralType = SpectralResolutionType.from_int(0)
            else:
                self._spectralType = SpectralResolutionType(row._spectralType)

            # antennaId is a list, let's populate self._antennaId element by element.
            if self._antennaId is None:
                self._antennaId = []

            for i in range(len(row._antennaId)):

                self._antennaId.append(Tag(row._antennaId[i]))

            # feedId is a list, let's populate self._feedId element by element.
            if self._feedId is None:
                self._feedId = []

            for i in range(len(row._feedId)):

                self._feedId.append(row._feedId[i])

            # switchCycleId is a list, let's populate self._switchCycleId element by element.
            if self._switchCycleId is None:
                self._switchCycleId = []

            for i in range(len(row._switchCycleId)):

                self._switchCycleId.append(Tag(row._switchCycleId[i]))

            # dataDescriptionId is a list, let's populate self._dataDescriptionId element by element.
            if self._dataDescriptionId is None:
                self._dataDescriptionId = []

            for i in range(len(row._dataDescriptionId)):

                self._dataDescriptionId.append(Tag(row._dataDescriptionId[i]))

            self._processorId = Tag(row._processorId)

            # by default set systematically phasedArrayList's value to something not None

            if row._phasedArrayListExists:

                # phasedArrayList is a list, make a deep copy
                self.phasedArrayList = copy.deepcopy(row.phasedArrayList)

                self._phasedArrayListExists = True

            # by default set systematically numAssocValues's value to something not None

            if row._numAssocValuesExists:

                self._numAssocValues = row._numAssocValues

                self._numAssocValuesExists = True

            # by default set systematically assocNature's value to something not None

            if row._assocNatureExists:

                # assocNature is a list, make a deep copy
                self.assocNature = copy.deepcopy(row.assocNature)

                self._assocNatureExists = True

            # by default set systematically assocConfigDescriptionId's value to something not None

            if row._assocConfigDescriptionIdExists:

                # assocConfigDescriptionId is a list , let's populate self.assocConfigDescriptionId element by element.
                if self._assocConfigDescriptionId is None:
                    self._assocConfigDescriptionId = []
                for i in range(len(row._assocConfigDescriptionId)):

                    self._assocConfigDescriptionId.append(
                        Tag(row._assocConfigDescriptionId[i])
                    )

                self._assocConfigDescriptionIdExists = True

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

        result += Parser.valueToXML("numAntenna", self._numAntenna)

        result += Parser.valueToXML("numDataDescription", self._numDataDescription)

        result += Parser.valueToXML("numFeed", self._numFeed)

        result += Parser.valueToXML(
            "correlationMode", CorrelationMode.name(self._correlationMode)
        )

        result += Parser.extendedValueToXML(
            "configDescriptionId", self._configDescriptionId
        )

        result += Parser.valueToXML(
            "numAtmPhaseCorrection", self._numAtmPhaseCorrection
        )

        result += Parser.listEnumValueToXML(
            "atmPhaseCorrection", self._atmPhaseCorrection
        )

        result += Parser.valueToXML(
            "processorType", ProcessorType.name(self._processorType)
        )

        if self._phasedArrayListExists:

            result += Parser.listValueToXML("phasedArrayList", self._phasedArrayList)

        result += Parser.valueToXML(
            "spectralType", SpectralResolutionType.name(self._spectralType)
        )

        if self._numAssocValuesExists:

            result += Parser.valueToXML("numAssocValues", self._numAssocValues)

        if self._assocNatureExists:

            result += Parser.listEnumValueToXML("assocNature", self._assocNature)

        # extrinsic attributes

        result += Parser.listExtendedValueToXML("antennaId", self._antennaId)

        if self._assocConfigDescriptionIdExists:

            result += Parser.listExtendedValueToXML(
                "assocConfigDescriptionId", self._assocConfigDescriptionId
            )

        result += Parser.listExtendedValueToXML(
            "dataDescriptionId", self._dataDescriptionId
        )

        result += Parser.listValueToXML("feedId", self._feedId)

        result += Parser.extendedValueToXML("processorId", self._processorId)

        result += Parser.listExtendedValueToXML("switchCycleId", self._switchCycleId)

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
                "xmlrow is not a string or a minidom.Element", "ConfigDescriptionTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException(
                "the argument is not a row", "ConfigDescriptionTable"
            )

        # intrinsic attribute values

        numAntennaNode = rowdom.getElementsByTagName("numAntenna")[0]

        self._numAntenna = int(numAntennaNode.firstChild.data.strip())

        numDataDescriptionNode = rowdom.getElementsByTagName("numDataDescription")[0]

        self._numDataDescription = int(numDataDescriptionNode.firstChild.data.strip())

        numFeedNode = rowdom.getElementsByTagName("numFeed")[0]

        self._numFeed = int(numFeedNode.firstChild.data.strip())

        correlationModeNode = rowdom.getElementsByTagName("correlationMode")[0]

        self._correlationMode = CorrelationMode.newCorrelationMode(
            correlationModeNode.firstChild.data.strip()
        )

        configDescriptionIdNode = rowdom.getElementsByTagName("configDescriptionId")[0]

        self._configDescriptionId = Tag(configDescriptionIdNode.firstChild.data.strip())

        numAtmPhaseCorrectionNode = rowdom.getElementsByTagName(
            "numAtmPhaseCorrection"
        )[0]

        self._numAtmPhaseCorrection = int(
            numAtmPhaseCorrectionNode.firstChild.data.strip()
        )

        atmPhaseCorrectionNode = rowdom.getElementsByTagName("atmPhaseCorrection")[0]

        atmPhaseCorrectionStr = atmPhaseCorrectionNode.firstChild.data.strip()
        self._atmPhaseCorrection = Parser.stringListToLists(
            atmPhaseCorrectionStr, AtmPhaseCorrection, "ConfigDescription", False
        )

        processorTypeNode = rowdom.getElementsByTagName("processorType")[0]

        self._processorType = ProcessorType.newProcessorType(
            processorTypeNode.firstChild.data.strip()
        )

        phasedArrayListNode = rowdom.getElementsByTagName("phasedArrayList")
        if len(phasedArrayListNode) > 0:

            phasedArrayListStr = phasedArrayListNode[0].firstChild.data.strip()

            self._phasedArrayList = Parser.stringListToLists(
                phasedArrayListStr, int, "ConfigDescription", False
            )

            self._phasedArrayListExists = True

        spectralTypeNode = rowdom.getElementsByTagName("spectralType")[0]

        self._spectralType = SpectralResolutionType.newSpectralResolutionType(
            spectralTypeNode.firstChild.data.strip()
        )

        numAssocValuesNode = rowdom.getElementsByTagName("numAssocValues")
        if len(numAssocValuesNode) > 0:

            self._numAssocValues = int(numAssocValuesNode[0].firstChild.data.strip())

            self._numAssocValuesExists = True

        assocNatureNode = rowdom.getElementsByTagName("assocNature")
        if len(assocNatureNode) > 0:

            assocNatureStr = assocNatureNode[0].firstChild.data.strip()
            self._assocNature = Parser.stringListToLists(
                assocNatureStr, SpectralResolutionType, "ConfigDescription", False
            )

            self._assocNatureExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        antennaIdStr = antennaIdNode.firstChild.data.strip()

        self._antennaId = Parser.stringListToLists(
            antennaIdStr, Tag, "ConfigDescription", True
        )

        assocConfigDescriptionIdNode = rowdom.getElementsByTagName(
            "assocConfigDescriptionId"
        )
        if len(assocConfigDescriptionIdNode) > 0:

            assocConfigDescriptionIdStr = assocConfigDescriptionIdNode[
                0
            ].firstChild.data.strip()

            self._assocConfigDescriptionId = Parser.stringListToLists(
                assocConfigDescriptionIdStr, Tag, "ConfigDescription", True
            )

            self._assocConfigDescriptionIdExists = True

        dataDescriptionIdNode = rowdom.getElementsByTagName("dataDescriptionId")[0]

        dataDescriptionIdStr = dataDescriptionIdNode.firstChild.data.strip()

        self._dataDescriptionId = Parser.stringListToLists(
            dataDescriptionIdStr, Tag, "ConfigDescription", True
        )

        feedIdNode = rowdom.getElementsByTagName("feedId")[0]

        feedIdStr = feedIdNode.firstChild.data.strip()

        self._feedId = Parser.stringListToLists(
            feedIdStr, int, "ConfigDescription", False
        )

        processorIdNode = rowdom.getElementsByTagName("processorId")[0]

        self._processorId = Tag(processorIdNode.firstChild.data.strip())

        switchCycleIdNode = rowdom.getElementsByTagName("switchCycleId")[0]

        switchCycleIdStr = switchCycleIdNode.firstChild.data.strip()

        self._switchCycleId = Parser.stringListToLists(
            switchCycleIdStr, Tag, "ConfigDescription", True
        )

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

    # ===> Attribute numAntenna

    _numAntenna = 0

    def getNumAntenna(self):
        """
        Get numAntenna.
        return numAntenna as int
        """

        return self._numAntenna

    def setNumAntenna(self, numAntenna):
        """
        Set numAntenna with the specified int value.
        numAntenna The int value to which numAntenna is to be set.


        """

        self._numAntenna = int(numAntenna)

    # ===> Attribute numDataDescription

    _numDataDescription = 0

    def getNumDataDescription(self):
        """
        Get numDataDescription.
        return numDataDescription as int
        """

        return self._numDataDescription

    def setNumDataDescription(self, numDataDescription):
        """
        Set numDataDescription with the specified int value.
        numDataDescription The int value to which numDataDescription is to be set.


        """

        self._numDataDescription = int(numDataDescription)

    # ===> Attribute numFeed

    _numFeed = 0

    def getNumFeed(self):
        """
        Get numFeed.
        return numFeed as int
        """

        return self._numFeed

    def setNumFeed(self, numFeed):
        """
        Set numFeed with the specified int value.
        numFeed The int value to which numFeed is to be set.


        """

        self._numFeed = int(numFeed)

    # ===> Attribute correlationMode

    _correlationMode = CorrelationMode.from_int(0)

    def getCorrelationMode(self):
        """
        Get correlationMode.
        return correlationMode as CorrelationMode
        """

        return self._correlationMode

    def setCorrelationMode(self, correlationMode):
        """
        Set correlationMode with the specified CorrelationMode value.
        correlationMode The CorrelationMode value to which correlationMode is to be set.


        """

        self._correlationMode = CorrelationMode(correlationMode)

    # ===> Attribute configDescriptionId

    _configDescriptionId = Tag()

    def getConfigDescriptionId(self):
        """
        Get configDescriptionId.
        return configDescriptionId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._configDescriptionId)

    def setConfigDescriptionId(self, configDescriptionId):
        """
        Set configDescriptionId with the specified Tag value.
        configDescriptionId The Tag value to which configDescriptionId is to be set.
        The value of configDescriptionId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the configDescriptionId field, which is part of the key, after this row has been added to this table."
            )

        self._configDescriptionId = Tag(configDescriptionId)

    # ===> Attribute numAtmPhaseCorrection

    _numAtmPhaseCorrection = 0

    def getNumAtmPhaseCorrection(self):
        """
        Get numAtmPhaseCorrection.
        return numAtmPhaseCorrection as int
        """

        return self._numAtmPhaseCorrection

    def setNumAtmPhaseCorrection(self, numAtmPhaseCorrection):
        """
        Set numAtmPhaseCorrection with the specified int value.
        numAtmPhaseCorrection The int value to which numAtmPhaseCorrection is to be set.


        """

        self._numAtmPhaseCorrection = int(numAtmPhaseCorrection)

    # ===> Attribute atmPhaseCorrection

    _atmPhaseCorrection = None  # this is a 1D list of AtmPhaseCorrection

    def getAtmPhaseCorrection(self):
        """
        Get atmPhaseCorrection.
        return atmPhaseCorrection as AtmPhaseCorrection []
        """

        return copy.deepcopy(self._atmPhaseCorrection)

    def setAtmPhaseCorrection(self, atmPhaseCorrection):
        """
        Set atmPhaseCorrection with the specified AtmPhaseCorrection []  value.
        atmPhaseCorrection The AtmPhaseCorrection []  value to which atmPhaseCorrection is to be set.


        """

        # value must be a list
        if not isinstance(atmPhaseCorrection, list):
            raise ValueError("The value of atmPhaseCorrection must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(atmPhaseCorrection)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of atmPhaseCorrection is not correct")

            # the type of the values in the list must be AtmPhaseCorrection
            # note : this only checks the first value found
            if not Parser.checkListType(atmPhaseCorrection, AtmPhaseCorrection):
                raise ValueError(
                    "type of the first value in atmPhaseCorrection is not AtmPhaseCorrection as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._atmPhaseCorrection = copy.deepcopy(atmPhaseCorrection)
        except Exception as exc:
            raise ValueError("Invalid atmPhaseCorrection : " + str(exc))

    # ===> Attribute processorType

    _processorType = ProcessorType.from_int(0)

    def getProcessorType(self):
        """
        Get processorType.
        return processorType as ProcessorType
        """

        return self._processorType

    def setProcessorType(self, processorType):
        """
        Set processorType with the specified ProcessorType value.
        processorType The ProcessorType value to which processorType is to be set.


        """

        self._processorType = ProcessorType(processorType)

    # ===> Attribute phasedArrayList, which is optional
    _phasedArrayListExists = False

    _phasedArrayList = None  # this is a 1D list of int

    def isPhasedArrayListExists(self):
        """
        The attribute phasedArrayList is optional. Return True if this attribute exists.
        return True if and only if the phasedArrayList attribute exists.
        """
        return self._phasedArrayListExists

    def getPhasedArrayList(self):
        """
        Get phasedArrayList, which is optional.
        return phasedArrayList as int []
        raises ValueError If phasedArrayList does not exist.
        """
        if not self._phasedArrayListExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + phasedArrayList
                + " attribute in table ConfigDescription does not exist!"
            )

        return copy.deepcopy(self._phasedArrayList)

    def setPhasedArrayList(self, phasedArrayList):
        """
        Set phasedArrayList with the specified int []  value.
        phasedArrayList The int []  value to which phasedArrayList is to be set.


        """

        # value must be a list
        if not isinstance(phasedArrayList, list):
            raise ValueError("The value of phasedArrayList must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(phasedArrayList)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of phasedArrayList is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not Parser.checkListType(phasedArrayList, int):
                raise ValueError(
                    "type of the first value in phasedArrayList is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phasedArrayList = copy.deepcopy(phasedArrayList)
        except Exception as exc:
            raise ValueError("Invalid phasedArrayList : " + str(exc))

        self._phasedArrayListExists = True

    def clearPhasedArrayList(self):
        """
        Mark phasedArrayList, which is an optional field, as non-existent.
        """
        self._phasedArrayListExists = False

    # ===> Attribute spectralType

    _spectralType = SpectralResolutionType.from_int(0)

    def getSpectralType(self):
        """
        Get spectralType.
        return spectralType as SpectralResolutionType
        """

        return self._spectralType

    def setSpectralType(self, spectralType):
        """
        Set spectralType with the specified SpectralResolutionType value.
        spectralType The SpectralResolutionType value to which spectralType is to be set.


        """

        self._spectralType = SpectralResolutionType(spectralType)

    # ===> Attribute numAssocValues, which is optional
    _numAssocValuesExists = False

    _numAssocValues = 0

    def isNumAssocValuesExists(self):
        """
        The attribute numAssocValues is optional. Return True if this attribute exists.
        return True if and only if the numAssocValues attribute exists.
        """
        return self._numAssocValuesExists

    def getNumAssocValues(self):
        """
        Get numAssocValues, which is optional.
        return numAssocValues as int
        raises ValueError If numAssocValues does not exist.
        """
        if not self._numAssocValuesExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numAssocValues
                + " attribute in table ConfigDescription does not exist!"
            )

        return self._numAssocValues

    def setNumAssocValues(self, numAssocValues):
        """
        Set numAssocValues with the specified int value.
        numAssocValues The int value to which numAssocValues is to be set.


        """

        self._numAssocValues = int(numAssocValues)

        self._numAssocValuesExists = True

    def clearNumAssocValues(self):
        """
        Mark numAssocValues, which is an optional field, as non-existent.
        """
        self._numAssocValuesExists = False

    # ===> Attribute assocNature, which is optional
    _assocNatureExists = False

    _assocNature = None  # this is a 1D list of SpectralResolutionType

    def isAssocNatureExists(self):
        """
        The attribute assocNature is optional. Return True if this attribute exists.
        return True if and only if the assocNature attribute exists.
        """
        return self._assocNatureExists

    def getAssocNature(self):
        """
        Get assocNature, which is optional.
        return assocNature as SpectralResolutionType []
        raises ValueError If assocNature does not exist.
        """
        if not self._assocNatureExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + assocNature
                + " attribute in table ConfigDescription does not exist!"
            )

        return copy.deepcopy(self._assocNature)

    def setAssocNature(self, assocNature):
        """
        Set assocNature with the specified SpectralResolutionType []  value.
        assocNature The SpectralResolutionType []  value to which assocNature is to be set.


        """

        # value must be a list
        if not isinstance(assocNature, list):
            raise ValueError("The value of assocNature must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(assocNature)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of assocNature is not correct")

            # the type of the values in the list must be SpectralResolutionType
            # note : this only checks the first value found
            if not Parser.checkListType(assocNature, SpectralResolutionType):
                raise ValueError(
                    "type of the first value in assocNature is not SpectralResolutionType as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._assocNature = copy.deepcopy(assocNature)
        except Exception as exc:
            raise ValueError("Invalid assocNature : " + str(exc))

        self._assocNatureExists = True

    def clearAssocNature(self):
        """
        Mark assocNature, which is an optional field, as non-existent.
        """
        self._assocNatureExists = False

    # Extrinsic Table Attributes

    # ===> Attribute antennaId

    _antennaId = []  # this is a list of Tag []

    def getAntennaId(self):
        """
        Get antennaId.
        return antennaId as Tag []
        """

        return copy.deepcopy(self._antennaId)

    def setAntennaId(self, antennaId):
        """
        Set antennaId with the specified Tag []  value.
        antennaId The Tag []  value to which antennaId is to be set.
        The value of antennaId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(antennaId, list):
            raise ValueError("The value of antennaId must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(antennaId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of antennaId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not Parser.checkListType(antennaId, Tag):
                raise ValueError(
                    "type of the first value in antennaId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._antennaId = copy.deepcopy(antennaId)
        except Exception as exc:
            raise ValueError("Invalid antennaId : " + str(exc))

    # ===> Attribute assocConfigDescriptionId, which is optional
    _assocConfigDescriptionIdExists = False

    _assocConfigDescriptionId = []  # this is a list of Tag []

    def isAssocConfigDescriptionIdExists(self):
        """
        The attribute assocConfigDescriptionId is optional. Return True if this attribute exists.
        return True if and only if the assocConfigDescriptionId attribute exists.
        """
        return self._assocConfigDescriptionIdExists

    def getAssocConfigDescriptionId(self):
        """
        Get assocConfigDescriptionId, which is optional.
        return assocConfigDescriptionId as Tag []
        raises ValueError If assocConfigDescriptionId does not exist.
        """
        if not self._assocConfigDescriptionIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + assocConfigDescriptionId
                + " attribute in table ConfigDescription does not exist!"
            )

        return copy.deepcopy(self._assocConfigDescriptionId)

    def setAssocConfigDescriptionId(self, assocConfigDescriptionId):
        """
        Set assocConfigDescriptionId with the specified Tag []  value.
        assocConfigDescriptionId The Tag []  value to which assocConfigDescriptionId is to be set.
        The value of assocConfigDescriptionId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(assocConfigDescriptionId, list):
            raise ValueError("The value of assocConfigDescriptionId must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(assocConfigDescriptionId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of assocConfigDescriptionId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not Parser.checkListType(assocConfigDescriptionId, Tag):
                raise ValueError(
                    "type of the first value in assocConfigDescriptionId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._assocConfigDescriptionId = copy.deepcopy(assocConfigDescriptionId)
        except Exception as exc:
            raise ValueError("Invalid assocConfigDescriptionId : " + str(exc))

        self._assocConfigDescriptionIdExists = True

    def clearAssocConfigDescriptionId(self):
        """
        Mark assocConfigDescriptionId, which is an optional field, as non-existent.
        """
        self._assocConfigDescriptionIdExists = False

    # ===> Attribute dataDescriptionId

    _dataDescriptionId = []  # this is a list of Tag []

    def getDataDescriptionId(self):
        """
        Get dataDescriptionId.
        return dataDescriptionId as Tag []
        """

        return copy.deepcopy(self._dataDescriptionId)

    def setDataDescriptionId(self, dataDescriptionId):
        """
        Set dataDescriptionId with the specified Tag []  value.
        dataDescriptionId The Tag []  value to which dataDescriptionId is to be set.
        The value of dataDescriptionId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(dataDescriptionId, list):
            raise ValueError("The value of dataDescriptionId must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(dataDescriptionId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of dataDescriptionId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not Parser.checkListType(dataDescriptionId, Tag):
                raise ValueError(
                    "type of the first value in dataDescriptionId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._dataDescriptionId = copy.deepcopy(dataDescriptionId)
        except Exception as exc:
            raise ValueError("Invalid dataDescriptionId : " + str(exc))

    # ===> Attribute feedId

    _feedId = []  # this is a list of int []

    def getFeedId(self):
        """
        Get feedId.
        return feedId as int []
        """

        return copy.deepcopy(self._feedId)

    def setFeedId(self, feedId):
        """
        Set feedId with the specified int []  value.
        feedId The int []  value to which feedId is to be set.


        """

        # value must be a list
        if not isinstance(feedId, list):
            raise ValueError("The value of feedId must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(feedId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of feedId is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not Parser.checkListType(feedId, int):
                raise ValueError(
                    "type of the first value in feedId is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._feedId = copy.deepcopy(feedId)
        except Exception as exc:
            raise ValueError("Invalid feedId : " + str(exc))

    # ===> Attribute processorId

    _processorId = Tag()

    def getProcessorId(self):
        """
        Get processorId.
        return processorId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._processorId)

    def setProcessorId(self, processorId):
        """
        Set processorId with the specified Tag value.
        processorId The Tag value to which processorId is to be set.
        The value of processorId can be anything allowed by the Tag constructor.

        """

        self._processorId = Tag(processorId)

    # ===> Attribute switchCycleId

    _switchCycleId = []  # this is a list of Tag []

    def getSwitchCycleId(self):
        """
        Get switchCycleId.
        return switchCycleId as Tag []
        """

        return copy.deepcopy(self._switchCycleId)

    def setSwitchCycleId(self, switchCycleId):
        """
        Set switchCycleId with the specified Tag []  value.
        switchCycleId The Tag []  value to which switchCycleId is to be set.
        The value of switchCycleId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(switchCycleId, list):
            raise ValueError("The value of switchCycleId must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(switchCycleId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of switchCycleId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not Parser.checkListType(switchCycleId, Tag):
                raise ValueError(
                    "type of the first value in switchCycleId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._switchCycleId = copy.deepcopy(switchCycleId)
        except Exception as exc:
            raise ValueError("Invalid switchCycleId : " + str(exc))

    # Links

    def setOneAssocConfigDescriptionId(self, index, assocConfigDescriptionId):
        """
        Set assocConfigDescriptionId[i] with the specified Tag value.
        index The index in assocConfigDescriptionId where to set the Tag value.
        assocConfigDescriptionId The Tag value to which assocConfigDescriptionId[i] is to be set.
        Raises an exception if that value does not already exist in this row
        """
        if not self._assocConfigDescriptionIdExists():
            raise ValueError(
                "The optional attribute, assocConfigDescriptionId, does not exist in this row. This value can not be set using this method."
            )
        self._assocConfigDescriptionId[index] = Tag(assocConfigDescriptionId)

    # ===> hasmany link from a row of ConfigDescription table to many rows of ConfigDescription table.

    def addAssocConfigDescriptionId(self, id):
        """
        Append a Tag to assocConfigDescriptionId
        id the Tag to be appended to assocConfigDescriptionId
        """
        if isinstance(id, list):
            for i in range(len(id)):
                self._assocConfigDescriptionId.append(Tag(id[i]))
        else:
            self._assocConfigDescriptionId.append(Tag(id))

        if not self._assocConfigDescriptionIdExists:
            self._assocConfigDescriptionIdExists = True

    def getOneAssocConfigDescriptionId(self, i):
        """
        Returns the Tag stored in assocConfigDescriptionId at position i.
        """
        return self._assocConfigDescriptionId[i]

    def getConfigDescriptionUsingAssocConfigDescriptionId(self, i):
        """
        Returns the ConfigDescriptionRow linked to this row via the Tag stored in assocConfigDescriptionId
        at position i.
        """

        return (
            self._table.getContainer()
            .getConfigDescription()
            .getRowByKey(self._assocConfigDescriptionId[i])
        )

    def getConfigDescriptionsUsingAssocConfigDescriptionId(self):
        """
        Returns the array of ConfigDescriptionRow linked to this row via the Tags stored in assocConfigDescriptionId
        """
        result = []
        for thisItem in self._assocConfigDescriptionId:
            result.append(
                self._table.getContainer().getConfigDescription().getRowByKey(thisItem)
            )

        return result

    def setOneAntennaId(self, index, antennaId):
        """
        Set antennaId[i] with the specified Tag value.
        index The index in antennaId where to set the Tag value.
        antennaId The Tag value to which antennaId[i] is to be set.
        Raises an exception if that value does not already exist in this row.

        """

        self._antennaId[index] = Tag(antennaId)

    # ===> hasmany link from a row of ConfigDescription table to many rows of Antenna table.

    def addAntennaId(self, id):
        """
        Append a Tag to antennaId
        id the Tag to be appended to antennaId
        """
        if isinstance(id, list):
            for i in range(len(id)):
                self._antennaId.append(Tag(id[i]))
        else:
            self._antennaId.append(Tag(id))

    def getOneAntennaId(self, i):
        """
        Returns the Tag stored in antennaId at position i.
        """
        return self._antennaId[i]

    def getAntennaUsingAntennaId(self, i):
        """
        Returns the AntennaRow linked to this row via the Tag stored in antennaId
        at position i.
        """

        return self._table.getContainer().getAntenna().getRowByKey(self._antennaId[i])

    def getAntennasUsingAntennaId(self):
        """
        Returns the array of AntennaRow linked to this row via the Tags stored in antennaId
        """
        result = []
        for thisItem in self._antennaId:
            result.append(self._table.getContainer().getAntenna().getRowByKey(thisItem))

        return result

    def setOneFeedId(self, index, feedId):
        """
        Set feedId[i] with the specified int value.
        index The index in feedId where to set the int value.
        feedId The int value to which feedId[i] is to be set.
        Raises an exception if that value does not already exist in this row.

        """

        self._feedId[index] = int(feedId)

    # ===> Slices link from a row of ConfigDescription table to a collection of row of Feed table.
    def addFeedId(self, id):
        """
        Append a new id or list of ids to feedId
        """
        if isinstance(id, list):
            for thisId in id:
                feedId.append(SimplePythonType(id))
        else:
            feedId.append(SimplePythonType(id))

    def getOneFeed(self, i):
        """
        Using the feedId at location i in this row, return the corresponding row from FeedTable
        """

        # was self._feedId[i]
        j = self._feedId[i]
        return self._table.getContainer().getFeed().getRowByFeedId(j)

    def getFeeds(self):
        """
        Get all of the rows at FeedTable corresponding to each of the values of feedId from this row.
        returns a list of FeedRow
        """
        result = []

        for thisValue in self._feedId:
            tr = self._table.getContainer().getFeed().getRowByFeedId(thisValue)
            # this may return more than one row
            if isinstance(tr, list):
                for thisRow in tr:
                    result.append(tr[k])
            else:
                result.append(tr)
        return copy.deepcopy(result)

    def setOneSwitchCycleId(self, index, switchCycleId):
        """
        Set switchCycleId[i] with the specified Tag value.
        index The index in switchCycleId where to set the Tag value.
        switchCycleId The Tag value to which switchCycleId[i] is to be set.
        Raises an exception if that value does not already exist in this row.

        """

        self._switchCycleId[index] = Tag(switchCycleId)

    # ===> hasmany link from a row of ConfigDescription table to many rows of SwitchCycle table.

    def addSwitchCycleId(self, id):
        """
        Append a Tag to switchCycleId
        id the Tag to be appended to switchCycleId
        """
        if isinstance(id, list):
            for i in range(len(id)):
                self._switchCycleId.append(Tag(id[i]))
        else:
            self._switchCycleId.append(Tag(id))

    def getOneSwitchCycleId(self, i):
        """
        Returns the Tag stored in switchCycleId at position i.
        """
        return self._switchCycleId[i]

    def getSwitchCycleUsingSwitchCycleId(self, i):
        """
        Returns the SwitchCycleRow linked to this row via the Tag stored in switchCycleId
        at position i.
        """

        return (
            self._table.getContainer()
            .getSwitchCycle()
            .getRowByKey(self._switchCycleId[i])
        )

    def getSwitchCyclesUsingSwitchCycleId(self):
        """
        Returns the array of SwitchCycleRow linked to this row via the Tags stored in switchCycleId
        """
        result = []
        for thisItem in self._switchCycleId:
            result.append(
                self._table.getContainer().getSwitchCycle().getRowByKey(thisItem)
            )

        return result

    def setOneDataDescriptionId(self, index, dataDescriptionId):
        """
        Set dataDescriptionId[i] with the specified Tag value.
        index The index in dataDescriptionId where to set the Tag value.
        dataDescriptionId The Tag value to which dataDescriptionId[i] is to be set.
        Raises an exception if that value does not already exist in this row.

        """

        self._dataDescriptionId[index] = Tag(dataDescriptionId)

    # ===> hasmany link from a row of ConfigDescription table to many rows of DataDescription table.

    def addDataDescriptionId(self, id):
        """
        Append a Tag to dataDescriptionId
        id the Tag to be appended to dataDescriptionId
        """
        if isinstance(id, list):
            for i in range(len(id)):
                self._dataDescriptionId.append(Tag(id[i]))
        else:
            self._dataDescriptionId.append(Tag(id))

    def getOneDataDescriptionId(self, i):
        """
        Returns the Tag stored in dataDescriptionId at position i.
        """
        return self._dataDescriptionId[i]

    def getDataDescriptionUsingDataDescriptionId(self, i):
        """
        Returns the DataDescriptionRow linked to this row via the Tag stored in dataDescriptionId
        at position i.
        """

        return (
            self._table.getContainer()
            .getDataDescription()
            .getRowByKey(self._dataDescriptionId[i])
        )

    def getDataDescriptionsUsingDataDescriptionId(self):
        """
        Returns the array of DataDescriptionRow linked to this row via the Tags stored in dataDescriptionId
        """
        result = []
        for thisItem in self._dataDescriptionId:
            result.append(
                self._table.getContainer().getDataDescription().getRowByKey(thisItem)
            )

        return result

    def getProcessorUsingProcessorId(self):
        """
        Returns the row in the Processor table having Processor.processorId == processorId

        """

        return self._table.getContainer().getProcessor().getRowByKey(self._processorId)

    # comparison methods

    def compareNoAutoInc(
        self,
        numAntenna,
        numDataDescription,
        numFeed,
        correlationMode,
        numAtmPhaseCorrection,
        atmPhaseCorrection,
        processorType,
        spectralType,
        antennaId,
        feedId,
        switchCycleId,
        dataDescriptionId,
        processorId,
    ):
        """
        Compare each attribute except the autoincrementable one of this ConfigDescriptionRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # numAntenna is a int, compare using the == operator.
        if not (self._numAntenna == numAntenna):
            return False

        # numDataDescription is a int, compare using the == operator.
        if not (self._numDataDescription == numDataDescription):
            return False

        # numFeed is a int, compare using the == operator.
        if not (self._numFeed == numFeed):
            return False

        # correlationMode is a CorrelationMode, compare using the == operator on the getValue() output
        if not (self._correlationMode.getValue() == correlationMode.getValue()):
            return False

        # numAtmPhaseCorrection is a int, compare using the == operator.
        if not (self._numAtmPhaseCorrection == numAtmPhaseCorrection):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._atmPhaseCorrection) != len(atmPhaseCorrection):
            return False
        for indx in range(len(atmPhaseCorrection)):

            # atmPhaseCorrection is a list of AtmPhaseCorrection, compare using == operator.
            if not (self._atmPhaseCorrection[indx] == atmPhaseCorrection[indx]):
                return False

        # processorType is a ProcessorType, compare using the == operator on the getValue() output
        if not (self._processorType.getValue() == processorType.getValue()):
            return False

        # spectralType is a SpectralResolutionType, compare using the == operator on the getValue() output
        if not (self._spectralType.getValue() == spectralType.getValue()):
            return False

        # antennaId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._antennaId) != len(antennaId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._antennaId)):
            if not (self._antennaId[indx].equals(antennaId[indx])):
                return False

        # feedId is an extrinsic attribute which is a list of int.
        # the lists must have the same length
        if len(self._feedId) != len(feedId):
            return False

        # feedId is a list of int, compare using the != operator.
        for indx in range(len(feedId)):
            if self._feedId[i] != feedId[i]:
                return False

        # switchCycleId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._switchCycleId) != len(switchCycleId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._switchCycleId)):
            if not (self._switchCycleId[indx].equals(switchCycleId[indx])):
                return False

        # dataDescriptionId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._dataDescriptionId) != len(dataDescriptionId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._dataDescriptionId)):
            if not (self._dataDescriptionId[indx].equals(dataDescriptionId[indx])):
                return False

        # processorId is a Tag, compare using the equals method.
        if not self._processorId.equals(processorId):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumAntenna(),
            otherRow.getNumDataDescription(),
            otherRow.getNumFeed(),
            otherRow.getCorrelationMode(),
            otherRow.getNumAtmPhaseCorrection(),
            otherRow.getAtmPhaseCorrection(),
            otherRow.getProcessorType(),
            otherRow.getSpectralType(),
            otherRow.getAntennaId(),
            otherRow.getFeedId(),
            otherRow.getSwitchCycleId(),
            otherRow.getDataDescriptionId(),
            otherRow.getProcessorId(),
        )

    def compareRequiredValue(
        self,
        numAntenna,
        numDataDescription,
        numFeed,
        correlationMode,
        numAtmPhaseCorrection,
        atmPhaseCorrection,
        processorType,
        spectralType,
        antennaId,
        feedId,
        switchCycleId,
        dataDescriptionId,
        processorId,
    ):

        # numAntenna is a int, compare using the == operator.
        if not (self._numAntenna == numAntenna):
            return False

        # numDataDescription is a int, compare using the == operator.
        if not (self._numDataDescription == numDataDescription):
            return False

        # numFeed is a int, compare using the == operator.
        if not (self._numFeed == numFeed):
            return False

        # correlationMode is a CorrelationMode, compare using the == operator on the getValue() output
        if not (self._correlationMode.getValue() == correlationMode.getValue()):
            return False

        # numAtmPhaseCorrection is a int, compare using the == operator.
        if not (self._numAtmPhaseCorrection == numAtmPhaseCorrection):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._atmPhaseCorrection) != len(atmPhaseCorrection):
            return False
        for indx in range(len(atmPhaseCorrection)):

            # atmPhaseCorrection is a list of AtmPhaseCorrection, compare using == operator.
            if not (self._atmPhaseCorrection[indx] == atmPhaseCorrection[indx]):
                return False

        # processorType is a ProcessorType, compare using the == operator on the getValue() output
        if not (self._processorType.getValue() == processorType.getValue()):
            return False

        # spectralType is a SpectralResolutionType, compare using the == operator on the getValue() output
        if not (self._spectralType.getValue() == spectralType.getValue()):
            return False

        # antennaId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._antennaId) != len(antennaId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._antennaId)):
            if not (self._antennaId[indx].equals(antennaId[indx])):
                return False

        # feedId is an extrinsic attribute which is a list of int.
        # the lists must have the same length
        if len(self._feedId) != len(feedId):
            return False

        # feedId is a list of int, compare using the != operator.
        for indx in range(len(feedId)):
            if self._feedId[i] != feedId[i]:
                return False

        # switchCycleId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._switchCycleId) != len(switchCycleId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._switchCycleId)):
            if not (self._switchCycleId[indx].equals(switchCycleId[indx])):
                return False

        # dataDescriptionId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._dataDescriptionId) != len(dataDescriptionId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._dataDescriptionId)):
            if not (self._dataDescriptionId[indx].equals(dataDescriptionId[indx])):
                return False

        # processorId is a Tag, compare using the equals method.
        if not self._processorId.equals(processorId):
            return False

        return True
