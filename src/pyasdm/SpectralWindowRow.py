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
# File SpectralWindowRow.py
#

import pyasdm.SpectralWindowTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.BasebandName import BasebandName


from pyasdm.enumerations.NetSideband import NetSideband


from pyasdm.enumerations.SidebandProcessingMode import SidebandProcessingMode


from pyasdm.enumerations.WindowFunction import WindowFunction


from pyasdm.enumerations.CorrelationBit import CorrelationBit


from pyasdm.enumerations.FrequencyReferenceCode import FrequencyReferenceCode


from pyasdm.enumerations.SpectralResolutionType import SpectralResolutionType


from xml.dom import minidom

import copy


class SpectralWindowRow:
    """
    The SpectralWindowRow class is a row of a SpectralWindowTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a SpectralWindowRow.
        When row is None, create an empty row attached to table, which must be a SpectralWindowTable.
        When row is given, copy those values in to the new row. The row argument must be a SpectralWindowRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.SpectralWindowTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._basebandName = BasebandName.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._netSideband = NetSideband.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._sidebandProcessingMode = SidebandProcessingMode.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._windowFunction = WindowFunction.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._correlationBit = CorrelationBit.from_int(0)

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._measFreqRef = FrequencyReferenceCode.from_int(0)

        # this is a list of SpectralResolutionType Enumeration, start off with it being empty
        self._assocNature = []

        if row is not None:
            if not isinstance(row, SpectralWindowRow):
                raise ValueError("row must be a MainRow")

            self._spectralWindowId = Tag(row._spectralWindowId)

            # We force the attribute of the result to be not None
            if row._basebandName is None:
                self._basebandName = BasebandName.from_int(0)
            else:
                self._basebandName = BasebandName(row._basebandName)

            # We force the attribute of the result to be not None
            if row._netSideband is None:
                self._netSideband = NetSideband.from_int(0)
            else:
                self._netSideband = NetSideband(row._netSideband)

            self._numChan = row._numChan

            self._refFreq = Frequency(row._refFreq)

            # We force the attribute of the result to be not None
            if row._sidebandProcessingMode is None:
                self._sidebandProcessingMode = SidebandProcessingMode.from_int(0)
            else:
                self._sidebandProcessingMode = SidebandProcessingMode(
                    row._sidebandProcessingMode
                )

            self._totBandwidth = Frequency(row._totBandwidth)

            # We force the attribute of the result to be not None
            if row._windowFunction is None:
                self._windowFunction = WindowFunction.from_int(0)
            else:
                self._windowFunction = WindowFunction(row._windowFunction)

            # by default set systematically numBin's value to something not None

            if row._numBinExists:

                self._numBin = row._numBin

                self._numBinExists = True

            # by default set systematically chanFreqStart's value to something not None

            if row._chanFreqStartExists:

                self._chanFreqStart = Frequency(row._chanFreqStart)

                self._chanFreqStartExists = True

            # by default set systematically chanFreqStep's value to something not None

            if row._chanFreqStepExists:

                self._chanFreqStep = Frequency(row._chanFreqStep)

                self._chanFreqStepExists = True

            # by default set systematically chanFreqArray's value to something not None

            if row._chanFreqArrayExists:

                # chanFreqArray is a list, make a deep copy
                self.chanFreqArray = copy.deepcopy(row.chanFreqArray)

                self._chanFreqArrayExists = True

            # by default set systematically chanWidth's value to something not None

            if row._chanWidthExists:

                self._chanWidth = Frequency(row._chanWidth)

                self._chanWidthExists = True

            # by default set systematically chanWidthArray's value to something not None

            if row._chanWidthArrayExists:

                # chanWidthArray is a list, make a deep copy
                self.chanWidthArray = copy.deepcopy(row.chanWidthArray)

                self._chanWidthArrayExists = True

            # by default set systematically correlationBit's value to something not None

            self.correlationBit = CorrelationBit.from_int(0)

            if row._correlationBitExists:

                if row._correlationBit is None:
                    self._correlationBit = row._correlationBit

                self._correlationBitExists = True

            # by default set systematically effectiveBw's value to something not None

            if row._effectiveBwExists:

                self._effectiveBw = Frequency(row._effectiveBw)

                self._effectiveBwExists = True

            # by default set systematically effectiveBwArray's value to something not None

            if row._effectiveBwArrayExists:

                # effectiveBwArray is a list, make a deep copy
                self.effectiveBwArray = copy.deepcopy(row.effectiveBwArray)

                self._effectiveBwArrayExists = True

            # by default set systematically freqGroup's value to something not None

            if row._freqGroupExists:

                self._freqGroup = row._freqGroup

                self._freqGroupExists = True

            # by default set systematically freqGroupName's value to something not None

            if row._freqGroupNameExists:

                self._freqGroupName = row._freqGroupName

                self._freqGroupNameExists = True

            # by default set systematically lineArray's value to something not None

            if row._lineArrayExists:

                # lineArray is a list, make a deep copy
                self.lineArray = copy.deepcopy(row.lineArray)

                self._lineArrayExists = True

            # by default set systematically measFreqRef's value to something not None

            self.measFreqRef = FrequencyReferenceCode.from_int(0)

            if row._measFreqRefExists:

                if row._measFreqRef is None:
                    self._measFreqRef = row._measFreqRef

                self._measFreqRefExists = True

            # by default set systematically name's value to something not None

            if row._nameExists:

                self._name = row._name

                self._nameExists = True

            # by default set systematically oversampling's value to something not None

            if row._oversamplingExists:

                self._oversampling = row._oversampling

                self._oversamplingExists = True

            # by default set systematically quantization's value to something not None

            if row._quantizationExists:

                self._quantization = row._quantization

                self._quantizationExists = True

            # by default set systematically refChan's value to something not None

            if row._refChanExists:

                self._refChan = row._refChan

                self._refChanExists = True

            # by default set systematically resolution's value to something not None

            if row._resolutionExists:

                self._resolution = Frequency(row._resolution)

                self._resolutionExists = True

            # by default set systematically resolutionArray's value to something not None

            if row._resolutionArrayExists:

                # resolutionArray is a list, make a deep copy
                self.resolutionArray = copy.deepcopy(row.resolutionArray)

                self._resolutionArrayExists = True

            # by default set systematically numAssocValues's value to something not None

            if row._numAssocValuesExists:

                self._numAssocValues = row._numAssocValues

                self._numAssocValuesExists = True

            # by default set systematically assocNature's value to something not None

            if row._assocNatureExists:

                # assocNature is a list, make a deep copy
                self.assocNature = copy.deepcopy(row.assocNature)

                self._assocNatureExists = True

            # by default set systematically assocSpectralWindowId's value to something not None

            if row._assocSpectralWindowIdExists:

                # assocSpectralWindowId is a list , let's populate self.assocSpectralWindowId element by element.
                if self._assocSpectralWindowId is None:
                    self._assocSpectralWindowId = []
                for i in range(len(row._assocSpectralWindowId)):

                    self._assocSpectralWindowId.append(
                        Tag(row._assocSpectralWindowId[i])
                    )

                self._assocSpectralWindowIdExists = True

            # by default set systematically imageSpectralWindowId's value to something not None

            if row._imageSpectralWindowIdExists:

                self._imageSpectralWindowId = Tag(row._imageSpectralWindowId)

                self._imageSpectralWindowIdExists = True

            # by default set systematically dopplerId's value to something not None

            if row._dopplerIdExists:

                self._dopplerId = row._dopplerId

                self._dopplerIdExists = True

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

        result += Parser.extendedValueToXML("spectralWindowId", self._spectralWindowId)

        result += Parser.valueToXML(
            "basebandName", BasebandName.name(self._basebandName)
        )

        result += Parser.valueToXML("netSideband", NetSideband.name(self._netSideband))

        result += Parser.valueToXML("numChan", self._numChan)

        if self._numBinExists:

            result += Parser.valueToXML("numBin", self._numBin)

        result += Parser.extendedValueToXML("refFreq", self._refFreq)

        result += Parser.valueToXML(
            "sidebandProcessingMode",
            SidebandProcessingMode.name(self._sidebandProcessingMode),
        )

        result += Parser.extendedValueToXML("totBandwidth", self._totBandwidth)

        result += Parser.valueToXML(
            "windowFunction", WindowFunction.name(self._windowFunction)
        )

        if self._chanFreqStartExists:

            result += Parser.extendedValueToXML("chanFreqStart", self._chanFreqStart)

        if self._chanFreqStepExists:

            result += Parser.extendedValueToXML("chanFreqStep", self._chanFreqStep)

        if self._chanFreqArrayExists:

            result += Parser.listExtendedValueToXML(
                "chanFreqArray", self._chanFreqArray
            )

        if self._chanWidthExists:

            result += Parser.extendedValueToXML("chanWidth", self._chanWidth)

        if self._chanWidthArrayExists:

            result += Parser.listExtendedValueToXML(
                "chanWidthArray", self._chanWidthArray
            )

        if self._correlationBitExists:

            result += Parser.valueToXML(
                "correlationBit", CorrelationBit.name(self._correlationBit)
            )

        if self._effectiveBwExists:

            result += Parser.extendedValueToXML("effectiveBw", self._effectiveBw)

        if self._effectiveBwArrayExists:

            result += Parser.listExtendedValueToXML(
                "effectiveBwArray", self._effectiveBwArray
            )

        if self._freqGroupExists:

            result += Parser.valueToXML("freqGroup", self._freqGroup)

        if self._freqGroupNameExists:

            result += Parser.valueToXML("freqGroupName", self._freqGroupName)

        if self._lineArrayExists:

            result += Parser.listValueToXML("lineArray", self._lineArray)

        if self._measFreqRefExists:

            result += Parser.valueToXML(
                "measFreqRef", FrequencyReferenceCode.name(self._measFreqRef)
            )

        if self._nameExists:

            result += Parser.valueToXML("name", self._name)

        if self._oversamplingExists:

            result += Parser.valueToXML("oversampling", self._oversampling)

        if self._quantizationExists:

            result += Parser.valueToXML("quantization", self._quantization)

        if self._refChanExists:

            result += Parser.valueToXML("refChan", self._refChan)

        if self._resolutionExists:

            result += Parser.extendedValueToXML("resolution", self._resolution)

        if self._resolutionArrayExists:

            result += Parser.listExtendedValueToXML(
                "resolutionArray", self._resolutionArray
            )

        if self._numAssocValuesExists:

            result += Parser.valueToXML("numAssocValues", self._numAssocValues)

        if self._assocNatureExists:

            result += Parser.listEnumValueToXML("assocNature", self._assocNature)

        # extrinsic attributes

        if self._assocSpectralWindowIdExists:

            result += Parser.listExtendedValueToXML(
                "assocSpectralWindowId", self._assocSpectralWindowId
            )

        if self._dopplerIdExists:

            result += Parser.valueToXML("dopplerId", self._dopplerId)

        if self._imageSpectralWindowIdExists:

            result += Parser.extendedValueToXML(
                "imageSpectralWindowId", self._imageSpectralWindowId
            )

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
                "xmlrow is not a string or a minidom.Element", "SpectralWindowTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException(
                "the argument is not a row", "SpectralWindowTable"
            )

        # intrinsic attribute values

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")[0]

        self._spectralWindowId = Tag(spectralWindowIdNode.firstChild.data)

        basebandNameNode = rowdom.getElementsByTagName("basebandName")[0]

        self._basebandName = BasebandName.newBasebandName(
            basebandNameNode.firstChild.data
        )

        netSidebandNode = rowdom.getElementsByTagName("netSideband")[0]

        self._netSideband = NetSideband.newNetSideband(netSidebandNode.firstChild.data)

        numChanNode = rowdom.getElementsByTagName("numChan")[0]

        self._numChan = int(numChanNode.firstChild.data)

        numBinNode = rowdom.getElementsByTagName("numBin")
        if len(numBinNode) > 0:

            self._numBin = int(numBinNode[0].firstChild.data)

            self._numBinExists = True

        refFreqNode = rowdom.getElementsByTagName("refFreq")[0]

        self._refFreq = Frequency(refFreqNode.firstChild.data)

        sidebandProcessingModeNode = rowdom.getElementsByTagName(
            "sidebandProcessingMode"
        )[0]

        self._sidebandProcessingMode = SidebandProcessingMode.newSidebandProcessingMode(
            sidebandProcessingModeNode.firstChild.data
        )

        totBandwidthNode = rowdom.getElementsByTagName("totBandwidth")[0]

        self._totBandwidth = Frequency(totBandwidthNode.firstChild.data)

        windowFunctionNode = rowdom.getElementsByTagName("windowFunction")[0]

        self._windowFunction = WindowFunction.newWindowFunction(
            windowFunctionNode.firstChild.data
        )

        chanFreqStartNode = rowdom.getElementsByTagName("chanFreqStart")
        if len(chanFreqStartNode) > 0:

            self._chanFreqStart = Frequency(chanFreqStartNode[0].firstChild.data)

            self._chanFreqStartExists = True

        chanFreqStepNode = rowdom.getElementsByTagName("chanFreqStep")
        if len(chanFreqStepNode) > 0:

            self._chanFreqStep = Frequency(chanFreqStepNode[0].firstChild.data)

            self._chanFreqStepExists = True

        chanFreqArrayNode = rowdom.getElementsByTagName("chanFreqArray")
        if len(chanFreqArrayNode) > 0:

            chanFreqArrayStr = chanFreqArrayNode[0].firstChild.data
            self._chanFreqArray = Parser.stringListToLists(
                chanFreqArrayStr, Frequency, "SpectralWindow"
            )

            self._chanFreqArrayExists = True

        chanWidthNode = rowdom.getElementsByTagName("chanWidth")
        if len(chanWidthNode) > 0:

            self._chanWidth = Frequency(chanWidthNode[0].firstChild.data)

            self._chanWidthExists = True

        chanWidthArrayNode = rowdom.getElementsByTagName("chanWidthArray")
        if len(chanWidthArrayNode) > 0:

            chanWidthArrayStr = chanWidthArrayNode[0].firstChild.data
            self._chanWidthArray = Parser.stringListToLists(
                chanWidthArrayStr, Frequency, "SpectralWindow"
            )

            self._chanWidthArrayExists = True

        correlationBitNode = rowdom.getElementsByTagName("correlationBit")
        if len(correlationBitNode) > 0:

            self._correlationBit = CorrelationBit.newCorrelationBit(
                correlationBitNode[0].firstChild.data
            )

            self._correlationBitExists = True

        effectiveBwNode = rowdom.getElementsByTagName("effectiveBw")
        if len(effectiveBwNode) > 0:

            self._effectiveBw = Frequency(effectiveBwNode[0].firstChild.data)

            self._effectiveBwExists = True

        effectiveBwArrayNode = rowdom.getElementsByTagName("effectiveBwArray")
        if len(effectiveBwArrayNode) > 0:

            effectiveBwArrayStr = effectiveBwArrayNode[0].firstChild.data
            self._effectiveBwArray = Parser.stringListToLists(
                effectiveBwArrayStr, Frequency, "SpectralWindow"
            )

            self._effectiveBwArrayExists = True

        freqGroupNode = rowdom.getElementsByTagName("freqGroup")
        if len(freqGroupNode) > 0:

            self._freqGroup = int(freqGroupNode[0].firstChild.data)

            self._freqGroupExists = True

        freqGroupNameNode = rowdom.getElementsByTagName("freqGroupName")
        if len(freqGroupNameNode) > 0:

            self._freqGroupName = str(freqGroupNameNode[0].firstChild.data)

            self._freqGroupNameExists = True

        lineArrayNode = rowdom.getElementsByTagName("lineArray")
        if len(lineArrayNode) > 0:

            lineArrayStr = lineArrayNode[0].firstChild.data
            self._lineArray = Parser.stringListToLists(
                lineArrayStr, bool, "SpectralWindow"
            )

            self._lineArrayExists = True

        measFreqRefNode = rowdom.getElementsByTagName("measFreqRef")
        if len(measFreqRefNode) > 0:

            self._measFreqRef = FrequencyReferenceCode.newFrequencyReferenceCode(
                measFreqRefNode[0].firstChild.data
            )

            self._measFreqRefExists = True

        nameNode = rowdom.getElementsByTagName("name")
        if len(nameNode) > 0:

            self._name = str(nameNode[0].firstChild.data)

            self._nameExists = True

        oversamplingNode = rowdom.getElementsByTagName("oversampling")
        if len(oversamplingNode) > 0:

            self._oversampling = bool(oversamplingNode[0].firstChild.data)

            self._oversamplingExists = True

        quantizationNode = rowdom.getElementsByTagName("quantization")
        if len(quantizationNode) > 0:

            self._quantization = bool(quantizationNode[0].firstChild.data)

            self._quantizationExists = True

        refChanNode = rowdom.getElementsByTagName("refChan")
        if len(refChanNode) > 0:

            self._refChan = double(refChanNode[0].firstChild.data)

            self._refChanExists = True

        resolutionNode = rowdom.getElementsByTagName("resolution")
        if len(resolutionNode) > 0:

            self._resolution = Frequency(resolutionNode[0].firstChild.data)

            self._resolutionExists = True

        resolutionArrayNode = rowdom.getElementsByTagName("resolutionArray")
        if len(resolutionArrayNode) > 0:

            resolutionArrayStr = resolutionArrayNode[0].firstChild.data
            self._resolutionArray = Parser.stringListToLists(
                resolutionArrayStr, Frequency, "SpectralWindow"
            )

            self._resolutionArrayExists = True

        numAssocValuesNode = rowdom.getElementsByTagName("numAssocValues")
        if len(numAssocValuesNode) > 0:

            self._numAssocValues = int(numAssocValuesNode[0].firstChild.data)

            self._numAssocValuesExists = True

        assocNatureNode = rowdom.getElementsByTagName("assocNature")
        if len(assocNatureNode) > 0:

            assocNatureStr = assocNatureNode[0].firstChild.data
            self._assocNature = Parser.stringListToLists(
                assocNatureStr, SpectralResolutionType, "SpectralWindow"
            )

            self._assocNatureExists = True

        # extrinsic attribute values

        assocSpectralWindowIdNode = rowdom.getElementsByTagName("assocSpectralWindowId")
        if len(assocSpectralWindowIdNode) > 0:

            assocSpectralWindowIdStr = assocSpectralWindowIdNode[0].firstChild.data
            self._assocSpectralWindowId = Parser.stringListToLists(
                assocSpectralWindowIdStr, Tag, "SpectralWindow"
            )

            self._assocSpectralWindowIdExists = True

        dopplerIdNode = rowdom.getElementsByTagName("dopplerId")
        if len(dopplerIdNode) > 0:

            self._dopplerId = int(dopplerIdNode[0].firstChild.data)

            self._dopplerIdExists = True

        imageSpectralWindowIdNode = rowdom.getElementsByTagName("imageSpectralWindowId")
        if len(imageSpectralWindowIdNode) > 0:

            self._imageSpectralWindowId = Tag(
                imageSpectralWindowIdNode[0].firstChild.data
            )

            self._imageSpectralWindowIdExists = True

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

    # ===> Attribute spectralWindowId

    _spectralWindowId = Tag()

    def getSpectralWindowId(self):
        """
        Get spectralWindowId.
        return spectralWindowId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._spectralWindowId)

    def setSpectralWindowId(self, spectralWindowId):
        """
        Set spectralWindowId with the specified Tag value.
        spectralWindowId The Tag value to which spectralWindowId is to be set.
        The value of spectralWindowId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the spectralWindowId field, which is part of the key, after this row has been added to this table."
            )

        self._spectralWindowId = Tag(spectralWindowId)

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


        """

        self._basebandName = BasebandName(basebandName)

    # ===> Attribute netSideband

    _netSideband = NetSideband.from_int(0)

    def getNetSideband(self):
        """
        Get netSideband.
        return netSideband as NetSideband
        """

        return self._netSideband

    def setNetSideband(self, netSideband):
        """
        Set netSideband with the specified NetSideband value.
        netSideband The NetSideband value to which netSideband is to be set.


        """

        self._netSideband = NetSideband(netSideband)

    # ===> Attribute numChan

    _numChan = 0

    def getNumChan(self):
        """
        Get numChan.
        return numChan as int
        """

        return self._numChan

    def setNumChan(self, numChan):
        """
        Set numChan with the specified int value.
        numChan The int value to which numChan is to be set.


        """

        self._numChan = int(numChan)

    # ===> Attribute numBin, which is optional
    _numBinExists = False

    _numBin = 0

    def isNumBinExists(self):
        """
        The attribute numBin is optional. Return True if this attribute exists.
        return True if and only if the numBin attribute exists.
        """
        return self._numBinExists

    def getNumBin(self):
        """
        Get numBin, which is optional.
        return numBin as int
        raises ValueError If numBin does not exist.
        """
        if not self._numBinExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numBin
                + " attribute in table SpectralWindow does not exist!"
            )

        return self._numBin

    def setNumBin(self, numBin):
        """
        Set numBin with the specified int value.
        numBin The int value to which numBin is to be set.


        """

        self._numBin = int(numBin)

        self._numBinExists = True

    def clearNumBin(self):
        """
        Mark numBin, which is an optional field, as non-existent.
        """
        self._numBinExists = False

    # ===> Attribute refFreq

    _refFreq = Frequency()

    def getRefFreq(self):
        """
        Get refFreq.
        return refFreq as Frequency
        """

        # make sure it is a copy of Frequency
        return Frequency(self._refFreq)

    def setRefFreq(self, refFreq):
        """
        Set refFreq with the specified Frequency value.
        refFreq The Frequency value to which refFreq is to be set.
        The value of refFreq can be anything allowed by the Frequency constructor.

        """

        self._refFreq = Frequency(refFreq)

    # ===> Attribute sidebandProcessingMode

    _sidebandProcessingMode = SidebandProcessingMode.from_int(0)

    def getSidebandProcessingMode(self):
        """
        Get sidebandProcessingMode.
        return sidebandProcessingMode as SidebandProcessingMode
        """

        return self._sidebandProcessingMode

    def setSidebandProcessingMode(self, sidebandProcessingMode):
        """
        Set sidebandProcessingMode with the specified SidebandProcessingMode value.
        sidebandProcessingMode The SidebandProcessingMode value to which sidebandProcessingMode is to be set.


        """

        self._sidebandProcessingMode = SidebandProcessingMode(sidebandProcessingMode)

    # ===> Attribute totBandwidth

    _totBandwidth = Frequency()

    def getTotBandwidth(self):
        """
        Get totBandwidth.
        return totBandwidth as Frequency
        """

        # make sure it is a copy of Frequency
        return Frequency(self._totBandwidth)

    def setTotBandwidth(self, totBandwidth):
        """
        Set totBandwidth with the specified Frequency value.
        totBandwidth The Frequency value to which totBandwidth is to be set.
        The value of totBandwidth can be anything allowed by the Frequency constructor.

        """

        self._totBandwidth = Frequency(totBandwidth)

    # ===> Attribute windowFunction

    _windowFunction = WindowFunction.from_int(0)

    def getWindowFunction(self):
        """
        Get windowFunction.
        return windowFunction as WindowFunction
        """

        return self._windowFunction

    def setWindowFunction(self, windowFunction):
        """
        Set windowFunction with the specified WindowFunction value.
        windowFunction The WindowFunction value to which windowFunction is to be set.


        """

        self._windowFunction = WindowFunction(windowFunction)

    # ===> Attribute chanFreqStart, which is optional
    _chanFreqStartExists = False

    _chanFreqStart = Frequency()

    def isChanFreqStartExists(self):
        """
        The attribute chanFreqStart is optional. Return True if this attribute exists.
        return True if and only if the chanFreqStart attribute exists.
        """
        return self._chanFreqStartExists

    def getChanFreqStart(self):
        """
        Get chanFreqStart, which is optional.
        return chanFreqStart as Frequency
        raises ValueError If chanFreqStart does not exist.
        """
        if not self._chanFreqStartExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + chanFreqStart
                + " attribute in table SpectralWindow does not exist!"
            )

        # make sure it is a copy of Frequency
        return Frequency(self._chanFreqStart)

    def setChanFreqStart(self, chanFreqStart):
        """
        Set chanFreqStart with the specified Frequency value.
        chanFreqStart The Frequency value to which chanFreqStart is to be set.
        The value of chanFreqStart can be anything allowed by the Frequency constructor.

        """

        self._chanFreqStart = Frequency(chanFreqStart)

        self._chanFreqStartExists = True

    def clearChanFreqStart(self):
        """
        Mark chanFreqStart, which is an optional field, as non-existent.
        """
        self._chanFreqStartExists = False

    # ===> Attribute chanFreqStep, which is optional
    _chanFreqStepExists = False

    _chanFreqStep = Frequency()

    def isChanFreqStepExists(self):
        """
        The attribute chanFreqStep is optional. Return True if this attribute exists.
        return True if and only if the chanFreqStep attribute exists.
        """
        return self._chanFreqStepExists

    def getChanFreqStep(self):
        """
        Get chanFreqStep, which is optional.
        return chanFreqStep as Frequency
        raises ValueError If chanFreqStep does not exist.
        """
        if not self._chanFreqStepExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + chanFreqStep
                + " attribute in table SpectralWindow does not exist!"
            )

        # make sure it is a copy of Frequency
        return Frequency(self._chanFreqStep)

    def setChanFreqStep(self, chanFreqStep):
        """
        Set chanFreqStep with the specified Frequency value.
        chanFreqStep The Frequency value to which chanFreqStep is to be set.
        The value of chanFreqStep can be anything allowed by the Frequency constructor.

        """

        self._chanFreqStep = Frequency(chanFreqStep)

        self._chanFreqStepExists = True

    def clearChanFreqStep(self):
        """
        Mark chanFreqStep, which is an optional field, as non-existent.
        """
        self._chanFreqStepExists = False

    # ===> Attribute chanFreqArray, which is optional
    _chanFreqArrayExists = False

    _chanFreqArray = None  # this is a 1D list of Frequency

    def isChanFreqArrayExists(self):
        """
        The attribute chanFreqArray is optional. Return True if this attribute exists.
        return True if and only if the chanFreqArray attribute exists.
        """
        return self._chanFreqArrayExists

    def getChanFreqArray(self):
        """
        Get chanFreqArray, which is optional.
        return chanFreqArray as Frequency []
        raises ValueError If chanFreqArray does not exist.
        """
        if not self._chanFreqArrayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + chanFreqArray
                + " attribute in table SpectralWindow does not exist!"
            )

        return copy.deepcopy(self._chanFreqArray)

    def setChanFreqArray(self, chanFreqArray):
        """
        Set chanFreqArray with the specified Frequency []  value.
        chanFreqArray The Frequency []  value to which chanFreqArray is to be set.
        The value of chanFreqArray can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(chanFreqArray, list):
            raise ValueError("The value of chanFreqArray must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(chanFreqArray)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of chanFreqArray is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(chanFreqArray, Frequency):
                raise ValueError(
                    "type of the first value in chanFreqArray is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._chanFreqArray = copy.deepcopy(chanFreqArray)
        except Exception as exc:
            raise ValueError("Invalid chanFreqArray : " + str(exc))

        self._chanFreqArrayExists = True

    def clearChanFreqArray(self):
        """
        Mark chanFreqArray, which is an optional field, as non-existent.
        """
        self._chanFreqArrayExists = False

    # ===> Attribute chanWidth, which is optional
    _chanWidthExists = False

    _chanWidth = Frequency()

    def isChanWidthExists(self):
        """
        The attribute chanWidth is optional. Return True if this attribute exists.
        return True if and only if the chanWidth attribute exists.
        """
        return self._chanWidthExists

    def getChanWidth(self):
        """
        Get chanWidth, which is optional.
        return chanWidth as Frequency
        raises ValueError If chanWidth does not exist.
        """
        if not self._chanWidthExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + chanWidth
                + " attribute in table SpectralWindow does not exist!"
            )

        # make sure it is a copy of Frequency
        return Frequency(self._chanWidth)

    def setChanWidth(self, chanWidth):
        """
        Set chanWidth with the specified Frequency value.
        chanWidth The Frequency value to which chanWidth is to be set.
        The value of chanWidth can be anything allowed by the Frequency constructor.

        """

        self._chanWidth = Frequency(chanWidth)

        self._chanWidthExists = True

    def clearChanWidth(self):
        """
        Mark chanWidth, which is an optional field, as non-existent.
        """
        self._chanWidthExists = False

    # ===> Attribute chanWidthArray, which is optional
    _chanWidthArrayExists = False

    _chanWidthArray = None  # this is a 1D list of Frequency

    def isChanWidthArrayExists(self):
        """
        The attribute chanWidthArray is optional. Return True if this attribute exists.
        return True if and only if the chanWidthArray attribute exists.
        """
        return self._chanWidthArrayExists

    def getChanWidthArray(self):
        """
        Get chanWidthArray, which is optional.
        return chanWidthArray as Frequency []
        raises ValueError If chanWidthArray does not exist.
        """
        if not self._chanWidthArrayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + chanWidthArray
                + " attribute in table SpectralWindow does not exist!"
            )

        return copy.deepcopy(self._chanWidthArray)

    def setChanWidthArray(self, chanWidthArray):
        """
        Set chanWidthArray with the specified Frequency []  value.
        chanWidthArray The Frequency []  value to which chanWidthArray is to be set.
        The value of chanWidthArray can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(chanWidthArray, list):
            raise ValueError("The value of chanWidthArray must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(chanWidthArray)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of chanWidthArray is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(chanWidthArray, Frequency):
                raise ValueError(
                    "type of the first value in chanWidthArray is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._chanWidthArray = copy.deepcopy(chanWidthArray)
        except Exception as exc:
            raise ValueError("Invalid chanWidthArray : " + str(exc))

        self._chanWidthArrayExists = True

    def clearChanWidthArray(self):
        """
        Mark chanWidthArray, which is an optional field, as non-existent.
        """
        self._chanWidthArrayExists = False

    # ===> Attribute correlationBit, which is optional
    _correlationBitExists = False

    _correlationBit = CorrelationBit.from_int(0)

    def isCorrelationBitExists(self):
        """
        The attribute correlationBit is optional. Return True if this attribute exists.
        return True if and only if the correlationBit attribute exists.
        """
        return self._correlationBitExists

    def getCorrelationBit(self):
        """
        Get correlationBit, which is optional.
        return correlationBit as CorrelationBit
        raises ValueError If correlationBit does not exist.
        """
        if not self._correlationBitExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + correlationBit
                + " attribute in table SpectralWindow does not exist!"
            )

        return self._correlationBit

    def setCorrelationBit(self, correlationBit):
        """
        Set correlationBit with the specified CorrelationBit value.
        correlationBit The CorrelationBit value to which correlationBit is to be set.


        """

        self._correlationBit = CorrelationBit(correlationBit)

        self._correlationBitExists = True

    def clearCorrelationBit(self):
        """
        Mark correlationBit, which is an optional field, as non-existent.
        """
        self._correlationBitExists = False

    # ===> Attribute effectiveBw, which is optional
    _effectiveBwExists = False

    _effectiveBw = Frequency()

    def isEffectiveBwExists(self):
        """
        The attribute effectiveBw is optional. Return True if this attribute exists.
        return True if and only if the effectiveBw attribute exists.
        """
        return self._effectiveBwExists

    def getEffectiveBw(self):
        """
        Get effectiveBw, which is optional.
        return effectiveBw as Frequency
        raises ValueError If effectiveBw does not exist.
        """
        if not self._effectiveBwExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + effectiveBw
                + " attribute in table SpectralWindow does not exist!"
            )

        # make sure it is a copy of Frequency
        return Frequency(self._effectiveBw)

    def setEffectiveBw(self, effectiveBw):
        """
        Set effectiveBw with the specified Frequency value.
        effectiveBw The Frequency value to which effectiveBw is to be set.
        The value of effectiveBw can be anything allowed by the Frequency constructor.

        """

        self._effectiveBw = Frequency(effectiveBw)

        self._effectiveBwExists = True

    def clearEffectiveBw(self):
        """
        Mark effectiveBw, which is an optional field, as non-existent.
        """
        self._effectiveBwExists = False

    # ===> Attribute effectiveBwArray, which is optional
    _effectiveBwArrayExists = False

    _effectiveBwArray = None  # this is a 1D list of Frequency

    def isEffectiveBwArrayExists(self):
        """
        The attribute effectiveBwArray is optional. Return True if this attribute exists.
        return True if and only if the effectiveBwArray attribute exists.
        """
        return self._effectiveBwArrayExists

    def getEffectiveBwArray(self):
        """
        Get effectiveBwArray, which is optional.
        return effectiveBwArray as Frequency []
        raises ValueError If effectiveBwArray does not exist.
        """
        if not self._effectiveBwArrayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + effectiveBwArray
                + " attribute in table SpectralWindow does not exist!"
            )

        return copy.deepcopy(self._effectiveBwArray)

    def setEffectiveBwArray(self, effectiveBwArray):
        """
        Set effectiveBwArray with the specified Frequency []  value.
        effectiveBwArray The Frequency []  value to which effectiveBwArray is to be set.
        The value of effectiveBwArray can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(effectiveBwArray, list):
            raise ValueError("The value of effectiveBwArray must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(effectiveBwArray)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of effectiveBwArray is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(effectiveBwArray, Frequency):
                raise ValueError(
                    "type of the first value in effectiveBwArray is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._effectiveBwArray = copy.deepcopy(effectiveBwArray)
        except Exception as exc:
            raise ValueError("Invalid effectiveBwArray : " + str(exc))

        self._effectiveBwArrayExists = True

    def clearEffectiveBwArray(self):
        """
        Mark effectiveBwArray, which is an optional field, as non-existent.
        """
        self._effectiveBwArrayExists = False

    # ===> Attribute freqGroup, which is optional
    _freqGroupExists = False

    _freqGroup = 0

    def isFreqGroupExists(self):
        """
        The attribute freqGroup is optional. Return True if this attribute exists.
        return True if and only if the freqGroup attribute exists.
        """
        return self._freqGroupExists

    def getFreqGroup(self):
        """
        Get freqGroup, which is optional.
        return freqGroup as int
        raises ValueError If freqGroup does not exist.
        """
        if not self._freqGroupExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + freqGroup
                + " attribute in table SpectralWindow does not exist!"
            )

        return self._freqGroup

    def setFreqGroup(self, freqGroup):
        """
        Set freqGroup with the specified int value.
        freqGroup The int value to which freqGroup is to be set.


        """

        self._freqGroup = int(freqGroup)

        self._freqGroupExists = True

    def clearFreqGroup(self):
        """
        Mark freqGroup, which is an optional field, as non-existent.
        """
        self._freqGroupExists = False

    # ===> Attribute freqGroupName, which is optional
    _freqGroupNameExists = False

    _freqGroupName = None

    def isFreqGroupNameExists(self):
        """
        The attribute freqGroupName is optional. Return True if this attribute exists.
        return True if and only if the freqGroupName attribute exists.
        """
        return self._freqGroupNameExists

    def getFreqGroupName(self):
        """
        Get freqGroupName, which is optional.
        return freqGroupName as str
        raises ValueError If freqGroupName does not exist.
        """
        if not self._freqGroupNameExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + freqGroupName
                + " attribute in table SpectralWindow does not exist!"
            )

        return self._freqGroupName

    def setFreqGroupName(self, freqGroupName):
        """
        Set freqGroupName with the specified str value.
        freqGroupName The str value to which freqGroupName is to be set.


        """

        self._freqGroupName = str(freqGroupName)

        self._freqGroupNameExists = True

    def clearFreqGroupName(self):
        """
        Mark freqGroupName, which is an optional field, as non-existent.
        """
        self._freqGroupNameExists = False

    # ===> Attribute lineArray, which is optional
    _lineArrayExists = False

    _lineArray = None  # this is a 1D list of bool

    def isLineArrayExists(self):
        """
        The attribute lineArray is optional. Return True if this attribute exists.
        return True if and only if the lineArray attribute exists.
        """
        return self._lineArrayExists

    def getLineArray(self):
        """
        Get lineArray, which is optional.
        return lineArray as bool []
        raises ValueError If lineArray does not exist.
        """
        if not self._lineArrayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + lineArray
                + " attribute in table SpectralWindow does not exist!"
            )

        return copy.deepcopy(self._lineArray)

    def setLineArray(self, lineArray):
        """
        Set lineArray with the specified bool []  value.
        lineArray The bool []  value to which lineArray is to be set.


        """

        # value must be a list
        if not isinstance(lineArray, list):
            raise ValueError("The value of lineArray must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(lineArray)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of lineArray is not correct")

            # the type of the values in the list must be bool
            # note : this only checks the first value found
            if not Parser.checkListType(lineArray, bool):
                raise ValueError(
                    "type of the first value in lineArray is not bool as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._lineArray = copy.deepcopy(lineArray)
        except Exception as exc:
            raise ValueError("Invalid lineArray : " + str(exc))

        self._lineArrayExists = True

    def clearLineArray(self):
        """
        Mark lineArray, which is an optional field, as non-existent.
        """
        self._lineArrayExists = False

    # ===> Attribute measFreqRef, which is optional
    _measFreqRefExists = False

    _measFreqRef = FrequencyReferenceCode.from_int(0)

    def isMeasFreqRefExists(self):
        """
        The attribute measFreqRef is optional. Return True if this attribute exists.
        return True if and only if the measFreqRef attribute exists.
        """
        return self._measFreqRefExists

    def getMeasFreqRef(self):
        """
        Get measFreqRef, which is optional.
        return measFreqRef as FrequencyReferenceCode
        raises ValueError If measFreqRef does not exist.
        """
        if not self._measFreqRefExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + measFreqRef
                + " attribute in table SpectralWindow does not exist!"
            )

        return self._measFreqRef

    def setMeasFreqRef(self, measFreqRef):
        """
        Set measFreqRef with the specified FrequencyReferenceCode value.
        measFreqRef The FrequencyReferenceCode value to which measFreqRef is to be set.


        """

        self._measFreqRef = FrequencyReferenceCode(measFreqRef)

        self._measFreqRefExists = True

    def clearMeasFreqRef(self):
        """
        Mark measFreqRef, which is an optional field, as non-existent.
        """
        self._measFreqRefExists = False

    # ===> Attribute name, which is optional
    _nameExists = False

    _name = None

    def isNameExists(self):
        """
        The attribute name is optional. Return True if this attribute exists.
        return True if and only if the name attribute exists.
        """
        return self._nameExists

    def getName(self):
        """
        Get name, which is optional.
        return name as str
        raises ValueError If name does not exist.
        """
        if not self._nameExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + name
                + " attribute in table SpectralWindow does not exist!"
            )

        return self._name

    def setName(self, name):
        """
        Set name with the specified str value.
        name The str value to which name is to be set.


        """

        self._name = str(name)

        self._nameExists = True

    def clearName(self):
        """
        Mark name, which is an optional field, as non-existent.
        """
        self._nameExists = False

    # ===> Attribute oversampling, which is optional
    _oversamplingExists = False

    _oversampling = None

    def isOversamplingExists(self):
        """
        The attribute oversampling is optional. Return True if this attribute exists.
        return True if and only if the oversampling attribute exists.
        """
        return self._oversamplingExists

    def getOversampling(self):
        """
        Get oversampling, which is optional.
        return oversampling as bool
        raises ValueError If oversampling does not exist.
        """
        if not self._oversamplingExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + oversampling
                + " attribute in table SpectralWindow does not exist!"
            )

        return self._oversampling

    def setOversampling(self, oversampling):
        """
        Set oversampling with the specified bool value.
        oversampling The bool value to which oversampling is to be set.


        """

        self._oversampling = bool(oversampling)

        self._oversamplingExists = True

    def clearOversampling(self):
        """
        Mark oversampling, which is an optional field, as non-existent.
        """
        self._oversamplingExists = False

    # ===> Attribute quantization, which is optional
    _quantizationExists = False

    _quantization = None

    def isQuantizationExists(self):
        """
        The attribute quantization is optional. Return True if this attribute exists.
        return True if and only if the quantization attribute exists.
        """
        return self._quantizationExists

    def getQuantization(self):
        """
        Get quantization, which is optional.
        return quantization as bool
        raises ValueError If quantization does not exist.
        """
        if not self._quantizationExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + quantization
                + " attribute in table SpectralWindow does not exist!"
            )

        return self._quantization

    def setQuantization(self, quantization):
        """
        Set quantization with the specified bool value.
        quantization The bool value to which quantization is to be set.


        """

        self._quantization = bool(quantization)

        self._quantizationExists = True

    def clearQuantization(self):
        """
        Mark quantization, which is an optional field, as non-existent.
        """
        self._quantizationExists = False

    # ===> Attribute refChan, which is optional
    _refChanExists = False

    _refChan = None

    def isRefChanExists(self):
        """
        The attribute refChan is optional. Return True if this attribute exists.
        return True if and only if the refChan attribute exists.
        """
        return self._refChanExists

    def getRefChan(self):
        """
        Get refChan, which is optional.
        return refChan as double
        raises ValueError If refChan does not exist.
        """
        if not self._refChanExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + refChan
                + " attribute in table SpectralWindow does not exist!"
            )

        return self._refChan

    def setRefChan(self, refChan):
        """
        Set refChan with the specified double value.
        refChan The double value to which refChan is to be set.


        """

        self._refChan = double(refChan)

        self._refChanExists = True

    def clearRefChan(self):
        """
        Mark refChan, which is an optional field, as non-existent.
        """
        self._refChanExists = False

    # ===> Attribute resolution, which is optional
    _resolutionExists = False

    _resolution = Frequency()

    def isResolutionExists(self):
        """
        The attribute resolution is optional. Return True if this attribute exists.
        return True if and only if the resolution attribute exists.
        """
        return self._resolutionExists

    def getResolution(self):
        """
        Get resolution, which is optional.
        return resolution as Frequency
        raises ValueError If resolution does not exist.
        """
        if not self._resolutionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + resolution
                + " attribute in table SpectralWindow does not exist!"
            )

        # make sure it is a copy of Frequency
        return Frequency(self._resolution)

    def setResolution(self, resolution):
        """
        Set resolution with the specified Frequency value.
        resolution The Frequency value to which resolution is to be set.
        The value of resolution can be anything allowed by the Frequency constructor.

        """

        self._resolution = Frequency(resolution)

        self._resolutionExists = True

    def clearResolution(self):
        """
        Mark resolution, which is an optional field, as non-existent.
        """
        self._resolutionExists = False

    # ===> Attribute resolutionArray, which is optional
    _resolutionArrayExists = False

    _resolutionArray = None  # this is a 1D list of Frequency

    def isResolutionArrayExists(self):
        """
        The attribute resolutionArray is optional. Return True if this attribute exists.
        return True if and only if the resolutionArray attribute exists.
        """
        return self._resolutionArrayExists

    def getResolutionArray(self):
        """
        Get resolutionArray, which is optional.
        return resolutionArray as Frequency []
        raises ValueError If resolutionArray does not exist.
        """
        if not self._resolutionArrayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + resolutionArray
                + " attribute in table SpectralWindow does not exist!"
            )

        return copy.deepcopy(self._resolutionArray)

    def setResolutionArray(self, resolutionArray):
        """
        Set resolutionArray with the specified Frequency []  value.
        resolutionArray The Frequency []  value to which resolutionArray is to be set.
        The value of resolutionArray can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(resolutionArray, list):
            raise ValueError("The value of resolutionArray must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(resolutionArray)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of resolutionArray is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(resolutionArray, Frequency):
                raise ValueError(
                    "type of the first value in resolutionArray is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._resolutionArray = copy.deepcopy(resolutionArray)
        except Exception as exc:
            raise ValueError("Invalid resolutionArray : " + str(exc))

        self._resolutionArrayExists = True

    def clearResolutionArray(self):
        """
        Mark resolutionArray, which is an optional field, as non-existent.
        """
        self._resolutionArrayExists = False

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
                + " attribute in table SpectralWindow does not exist!"
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
                + " attribute in table SpectralWindow does not exist!"
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

    # ===> Attribute assocSpectralWindowId, which is optional
    _assocSpectralWindowIdExists = False

    _assocSpectralWindowId = []  # this is a list of Tag []

    def isAssocSpectralWindowIdExists(self):
        """
        The attribute assocSpectralWindowId is optional. Return True if this attribute exists.
        return True if and only if the assocSpectralWindowId attribute exists.
        """
        return self._assocSpectralWindowIdExists

    def getAssocSpectralWindowId(self):
        """
        Get assocSpectralWindowId, which is optional.
        return assocSpectralWindowId as Tag []
        raises ValueError If assocSpectralWindowId does not exist.
        """
        if not self._assocSpectralWindowIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + assocSpectralWindowId
                + " attribute in table SpectralWindow does not exist!"
            )

        return copy.deepcopy(self._assocSpectralWindowId)

    def setAssocSpectralWindowId(self, assocSpectralWindowId):
        """
        Set assocSpectralWindowId with the specified Tag []  value.
        assocSpectralWindowId The Tag []  value to which assocSpectralWindowId is to be set.
        The value of assocSpectralWindowId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(assocSpectralWindowId, list):
            raise ValueError("The value of assocSpectralWindowId must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(assocSpectralWindowId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of assocSpectralWindowId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not Parser.checkListType(assocSpectralWindowId, Tag):
                raise ValueError(
                    "type of the first value in assocSpectralWindowId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._assocSpectralWindowId = copy.deepcopy(assocSpectralWindowId)
        except Exception as exc:
            raise ValueError("Invalid assocSpectralWindowId : " + str(exc))

        self._assocSpectralWindowIdExists = True

    def clearAssocSpectralWindowId(self):
        """
        Mark assocSpectralWindowId, which is an optional field, as non-existent.
        """
        self._assocSpectralWindowIdExists = False

    # ===> Attribute dopplerId, which is optional
    _dopplerIdExists = False

    _dopplerId = 0

    def isDopplerIdExists(self):
        """
        The attribute dopplerId is optional. Return True if this attribute exists.
        return True if and only if the dopplerId attribute exists.
        """
        return self._dopplerIdExists

    def getDopplerId(self):
        """
        Get dopplerId, which is optional.
        return dopplerId as int
        raises ValueError If dopplerId does not exist.
        """
        if not self._dopplerIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + dopplerId
                + " attribute in table SpectralWindow does not exist!"
            )

        return self._dopplerId

    def setDopplerId(self, dopplerId):
        """
        Set dopplerId with the specified int value.
        dopplerId The int value to which dopplerId is to be set.


        """

        self._dopplerId = int(dopplerId)

        self._dopplerIdExists = True

    def clearDopplerId(self):
        """
        Mark dopplerId, which is an optional field, as non-existent.
        """
        self._dopplerIdExists = False

    # ===> Attribute imageSpectralWindowId, which is optional
    _imageSpectralWindowIdExists = False

    _imageSpectralWindowId = Tag()

    def isImageSpectralWindowIdExists(self):
        """
        The attribute imageSpectralWindowId is optional. Return True if this attribute exists.
        return True if and only if the imageSpectralWindowId attribute exists.
        """
        return self._imageSpectralWindowIdExists

    def getImageSpectralWindowId(self):
        """
        Get imageSpectralWindowId, which is optional.
        return imageSpectralWindowId as Tag
        raises ValueError If imageSpectralWindowId does not exist.
        """
        if not self._imageSpectralWindowIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + imageSpectralWindowId
                + " attribute in table SpectralWindow does not exist!"
            )

        # make sure it is a copy of Tag
        return Tag(self._imageSpectralWindowId)

    def setImageSpectralWindowId(self, imageSpectralWindowId):
        """
        Set imageSpectralWindowId with the specified Tag value.
        imageSpectralWindowId The Tag value to which imageSpectralWindowId is to be set.
        The value of imageSpectralWindowId can be anything allowed by the Tag constructor.

        """

        self._imageSpectralWindowId = Tag(imageSpectralWindowId)

        self._imageSpectralWindowIdExists = True

    def clearImageSpectralWindowId(self):
        """
        Mark imageSpectralWindowId, which is an optional field, as non-existent.
        """
        self._imageSpectralWindowIdExists = False

    # Links

    def setOneAssocSpectralWindowId(self, index, assocSpectralWindowId):
        """
        Set assocSpectralWindowId[i] with the specified Tag value.
        index The index in assocSpectralWindowId where to set the Tag value.
        assocSpectralWindowId The Tag value to which assocSpectralWindowId[i] is to be set.
        Raises an exception if that value does not already exist in this row
        """
        if not self._assocSpectralWindowIdExists():
            raise ValueError(
                "The optional attribute, assocSpectralWindowId, does not exist in this row. This value can not be set using this method."
            )
        self._assocSpectralWindowId[index] = Tag(assocSpectralWindowId)

    # ===> hasmany link from a row of SpectralWindow table to many rows of SpectralWindow table.

    def addAssocSpectralWindowId(self, id):
        """
        Append a Tag to assocSpectralWindowId
        id the Tag to be appended to assocSpectralWindowId
        """
        if isinstance(id, list):
            for i in range(len(id)):
                self._assocSpectralWindowId.append(Tag(id[i]))
        else:
            self._assocSpectralWindowId.append(Tag(id))

        if not self._assocSpectralWindowIdExists:
            self._assocSpectralWindowIdExists = True

    def getOneAssocSpectralWindowId(self, i):
        """
        Returns the Tag stored in assocSpectralWindowId at position i.
        """
        return self._assocSpectralWindowId[i]

    def getSpectralWindowUsingAssocSpectralWindowId(self, i):
        """
        Returns the SpectralWindowRow linked to this row via the Tag stored in assocSpectralWindowId
        at position i.
        """

        return (
            self._table.getContainer()
            .getSpectralWindow()
            .getRowByKey(self._assocSpectralWindowId[i])
        )

    def getSpectralWindowsUsingAssocSpectralWindowId(self):
        """
        Returns the array of SpectralWindowRow linked to this row via the Tags stored in assocSpectralWindowId
        """
        result = []
        for thisItem in self._assocSpectralWindowId:
            result.append(
                self._table.getContainer().getSpectralWindow().getRowByKey(thisItem)
            )

        return result

    def getSpectralWindowUsingImageSpectralWindowId(self):
        """
        Returns the row in the SpectralWindow table having SpectralWindow.imageSpectralWindowId == imageSpectralWindowId

        Raise ValueError if the optional imageSpectralWindowId does not exist for this row.

        """

        if not _imageSpectralWindowIdExists:
            raise ValueError("imageSpectralWindowId does not exist for this row.")

        return (
            self._table.getContainer()
            .getSpectralWindow()
            .getRowByKey(self._imageSpectralWindowId)
        )

    # ===> Slice link from a row of SpectralWindow table to a collection of row of Doppler table.
    def getDopplers(self):
        """
        Get the collection of rows in the Doppler table having dopplerId == this.dopplerId
        """

        if self._dopplerIdExists:
            return (
                self._table.getContainer()
                .getDoppler()
                .getRowByDopplerId(self._dopplerId)
            )
        else:
            raise InvalidAccessException()

    # comparison methods

    def compareNoAutoInc(
        self,
        basebandName,
        netSideband,
        numChan,
        refFreq,
        sidebandProcessingMode,
        totBandwidth,
        windowFunction,
    ):
        """
        Compare each attribute except the autoincrementable one of this SpectralWindowRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # basebandName is a BasebandName, compare using the == operator on the getValue() output
        if not (self._basebandName.getValue() == basebandName.getValue()):
            return False

        # netSideband is a NetSideband, compare using the == operator on the getValue() output
        if not (self._netSideband.getValue() == netSideband.getValue()):
            return False

        # numChan is a int, compare using the == operator.
        if not (self._numChan == numChan):
            return False

        # refFreq is a Frequency, compare using the almostEquals method.
        if not self._refFreq.almostEquals(
            refFreq, self.getTable().getRefFreqEqTolerance()
        ):
            return False

        # sidebandProcessingMode is a SidebandProcessingMode, compare using the == operator on the getValue() output
        if not (
            self._sidebandProcessingMode.getValue() == sidebandProcessingMode.getValue()
        ):
            return False

        # totBandwidth is a Frequency, compare using the almostEquals method.
        if not self._totBandwidth.almostEquals(
            totBandwidth, self.getTable().getTotBandwidthEqTolerance()
        ):
            return False

        # windowFunction is a WindowFunction, compare using the == operator on the getValue() output
        if not (self._windowFunction.getValue() == windowFunction.getValue()):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getBasebandName(),
            otherRow.getNetSideband(),
            otherRow.getNumChan(),
            otherRow.getRefFreq(),
            otherRow.getSidebandProcessingMode(),
            otherRow.getTotBandwidth(),
            otherRow.getWindowFunction(),
        )

    def compareRequiredValue(
        self,
        basebandName,
        netSideband,
        numChan,
        refFreq,
        sidebandProcessingMode,
        totBandwidth,
        windowFunction,
    ):

        # basebandName is a BasebandName, compare using the == operator on the getValue() output
        if not (self._basebandName.getValue() == basebandName.getValue()):
            return False

        # netSideband is a NetSideband, compare using the == operator on the getValue() output
        if not (self._netSideband.getValue() == netSideband.getValue()):
            return False

        # numChan is a int, compare using the == operator.
        if not (self._numChan == numChan):
            return False

        # refFreq is a Frequency, compare using the almostEquals method.
        if not self._refFreq.almostEquals(
            refFreq, self.getTable().getRefFreqEqTolerance()
        ):
            return False

        # sidebandProcessingMode is a SidebandProcessingMode, compare using the == operator on the getValue() output
        if not (
            self._sidebandProcessingMode.getValue() == sidebandProcessingMode.getValue()
        ):
            return False

        # totBandwidth is a Frequency, compare using the almostEquals method.
        if not self._totBandwidth.almostEquals(
            totBandwidth, self.getTable().getTotBandwidthEqTolerance()
        ):
            return False

        # windowFunction is a WindowFunction, compare using the == operator on the getValue() output
        if not (self._windowFunction.getValue() == windowFunction.getValue()):
            return False

        return True
