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
# File CalDeviceRow.py
#

import pyasdm.CalDeviceTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.CalibrationDevice import CalibrationDevice


from xml.dom import minidom

import copy


class CalDeviceRow:
    """
    The CalDeviceRow class is a row of a CalDeviceTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalDeviceRow.
        When row is None, create an empty row attached to table, which must be a CalDeviceTable.
        When row is given, copy those values in to the new row. The row argument must be a CalDeviceRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalDeviceTable):
            raise ValueError("table must be a CalDeviceTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._timeInterval = ArrayTimeInterval()

        self._numCalload = 0

        self._calLoadNames = []  # this is a list of CalibrationDevice []

        self._numReceptorExists = False

        self._numReceptor = 0

        self._calEffExists = False

        self._calEff = []  # this is a list of float []  []

        self._noiseCalExists = False

        self._noiseCal = []  # this is a list of float []

        self._coupledNoiseCalExists = False

        self._coupledNoiseCal = []  # this is a list of float []  []

        self._temperatureLoadExists = False

        self._temperatureLoad = []  # this is a list of Temperature []

        # extrinsic attributes

        self._antennaId = Tag()

        self._feedId = 0

        self._spectralWindowId = Tag()

        if row is not None:
            if not isinstance(row, CalDeviceRow):
                raise ValueError("row must be a CalDeviceRow")

            # copy constructor

            self._antennaId = Tag(row._antennaId)

            self._spectralWindowId = Tag(row._spectralWindowId)

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._feedId = row._feedId

            self._numCalload = row._numCalload

            # calLoadNames is a  list , make a deep copy
            self._calLoadNames = copy.deepcopy(row._calLoadNames)

            # by default set systematically numReceptor's value to something not None

            if row._numReceptorExists:

                self._numReceptor = row._numReceptor

                self._numReceptorExists = True

            # by default set systematically calEff's value to something not None

            if row._calEffExists:

                # calEff is a list, make a deep copy
                self._calEff = copy.deepcopy(row._calEff)

                self._calEffExists = True

            # by default set systematically noiseCal's value to something not None

            if row._noiseCalExists:

                # noiseCal is a list, make a deep copy
                self._noiseCal = copy.deepcopy(row._noiseCal)

                self._noiseCalExists = True

            # by default set systematically coupledNoiseCal's value to something not None

            if row._coupledNoiseCalExists:

                # coupledNoiseCal is a list, make a deep copy
                self._coupledNoiseCal = copy.deepcopy(row._coupledNoiseCal)

                self._coupledNoiseCalExists = True

            # by default set systematically temperatureLoad's value to something not None

            if row._temperatureLoadExists:

                # temperatureLoad is a list, make a deep copy
                self._temperatureLoad = copy.deepcopy(row._temperatureLoad)

                self._temperatureLoadExists = True

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

        result += Parser.extendedValueToXML("timeInterval", self._timeInterval)

        result += Parser.valueToXML("numCalload", self._numCalload)

        result += Parser.listEnumValueToXML("calLoadNames", self._calLoadNames)

        if self._numReceptorExists:

            result += Parser.valueToXML("numReceptor", self._numReceptor)

        if self._calEffExists:

            result += Parser.listValueToXML("calEff", self._calEff)

        if self._noiseCalExists:

            result += Parser.listValueToXML("noiseCal", self._noiseCal)

        if self._coupledNoiseCalExists:

            result += Parser.listValueToXML("coupledNoiseCal", self._coupledNoiseCal)

        if self._temperatureLoadExists:

            result += Parser.listExtendedValueToXML(
                "temperatureLoad", self._temperatureLoad
            )

        # extrinsic attributes

        result += Parser.extendedValueToXML("antennaId", self._antennaId)

        result += Parser.valueToXML("feedId", self._feedId)

        result += Parser.extendedValueToXML("spectralWindowId", self._spectralWindowId)

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
                "xmlrow is not a string or a minidom.Element", "CalDeviceTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalDeviceTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        numCalloadNode = rowdom.getElementsByTagName("numCalload")[0]

        self._numCalload = int(numCalloadNode.firstChild.data.strip())

        calLoadNamesNode = rowdom.getElementsByTagName("calLoadNames")[0]

        calLoadNamesStr = calLoadNamesNode.firstChild.data.strip()
        self._calLoadNames = Parser.stringListToLists(
            calLoadNamesStr, CalibrationDevice, "CalDevice", False
        )

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")
        if len(numReceptorNode) > 0:

            self._numReceptor = int(numReceptorNode[0].firstChild.data.strip())

            self._numReceptorExists = True

        calEffNode = rowdom.getElementsByTagName("calEff")
        if len(calEffNode) > 0:

            calEffStr = calEffNode[0].firstChild.data.strip()

            self._calEff = Parser.stringListToLists(
                calEffStr, float, "CalDevice", False
            )

            self._calEffExists = True

        noiseCalNode = rowdom.getElementsByTagName("noiseCal")
        if len(noiseCalNode) > 0:

            noiseCalStr = noiseCalNode[0].firstChild.data.strip()

            self._noiseCal = Parser.stringListToLists(
                noiseCalStr, float, "CalDevice", False
            )

            self._noiseCalExists = True

        coupledNoiseCalNode = rowdom.getElementsByTagName("coupledNoiseCal")
        if len(coupledNoiseCalNode) > 0:

            coupledNoiseCalStr = coupledNoiseCalNode[0].firstChild.data.strip()

            self._coupledNoiseCal = Parser.stringListToLists(
                coupledNoiseCalStr, float, "CalDevice", False
            )

            self._coupledNoiseCalExists = True

        temperatureLoadNode = rowdom.getElementsByTagName("temperatureLoad")
        if len(temperatureLoadNode) > 0:

            temperatureLoadStr = temperatureLoadNode[0].firstChild.data.strip()

            self._temperatureLoad = Parser.stringListToLists(
                temperatureLoadStr, Temperature, "CalDevice", True
            )

            self._temperatureLoadExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        self._antennaId = Tag(antennaIdNode.firstChild.data.strip())

        feedIdNode = rowdom.getElementsByTagName("feedId")[0]

        self._feedId = int(feedIdNode.firstChild.data.strip())

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")[0]

        self._spectralWindowId = Tag(spectralWindowIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._antennaId.toBin(eos)

        self._spectralWindowId.toBin(eos)

        self._timeInterval.toBin(eos)

        eos.writeInt(self._feedId)

        eos.writeInt(self._numCalload)

        eos.writeInt(len(self._calLoadNames))
        for i in range(len(self._calLoadNames)):

            eos.writeString(str(self._calLoadNames[i]))

        eos.writeBool(self._numReceptorExists)
        if self._numReceptorExists:

            eos.writeInt(self._numReceptor)

        eos.writeBool(self._calEffExists)
        if self._calEffExists:

            # null array case, unsure if this is possible but this should work
            if self._calEff is None:
                eos.writeInt(0)
                eos.writeInt(0)
            else:
                calEff_dims = pyasdm.utils.getListDims(self._calEff)
            # assumes it really is 2D
            eos.writeInt(calEff_dims[0])
            eos.writeInt(calEff_dims[1])
            for i in range(calEff_dims[0]):
                for j in range(calEff_dims[1]):
                    eos.writeFloat(self._calEff[i][j])

        eos.writeBool(self._noiseCalExists)
        if self._noiseCalExists:

            eos.writeInt(len(self._noiseCal))
            for i in range(len(self._noiseCal)):

                eos.writeFloat(self._noiseCal[i])

        eos.writeBool(self._coupledNoiseCalExists)
        if self._coupledNoiseCalExists:

            # null array case, unsure if this is possible but this should work
            if self._coupledNoiseCal is None:
                eos.writeInt(0)
                eos.writeInt(0)
            else:
                coupledNoiseCal_dims = pyasdm.utils.getListDims(self._coupledNoiseCal)
            # assumes it really is 2D
            eos.writeInt(coupledNoiseCal_dims[0])
            eos.writeInt(coupledNoiseCal_dims[1])
            for i in range(coupledNoiseCal_dims[0]):
                for j in range(coupledNoiseCal_dims[1]):
                    eos.writeFloat(self._coupledNoiseCal[i][j])

        eos.writeBool(self._temperatureLoadExists)
        if self._temperatureLoadExists:

            Temperature.listToBin(self._temperatureLoad, eos)

    @staticmethod
    def antennaIdFromBin(row, eis):
        """
        Set the antennaId in row from the EndianInput (eis) instance.
        """

        row._antennaId = Tag.fromBin(eis)

    @staticmethod
    def spectralWindowIdFromBin(row, eis):
        """
        Set the spectralWindowId in row from the EndianInput (eis) instance.
        """

        row._spectralWindowId = Tag.fromBin(eis)

    @staticmethod
    def timeIntervalFromBin(row, eis):
        """
        Set the timeInterval in row from the EndianInput (eis) instance.
        """

        row._timeInterval = ArrayTimeInterval.fromBin(eis)

    @staticmethod
    def feedIdFromBin(row, eis):
        """
        Set the feedId in row from the EndianInput (eis) instance.
        """

        row._feedId = eis.readInt()

    @staticmethod
    def numCalloadFromBin(row, eis):
        """
        Set the numCalload in row from the EndianInput (eis) instance.
        """

        row._numCalload = eis.readInt()

    @staticmethod
    def calLoadNamesFromBin(row, eis):
        """
        Set the calLoadNames in row from the EndianInput (eis) instance.
        """

        calLoadNamesDim1 = eis.readInt()
        thisList = []
        for i in range(calLoadNamesDim1):
            thisValue = CalibrationDevice.literal(eis.readString())
            thisList.append(thisValue)
        row._calLoadNames = thisList

    @staticmethod
    def numReceptorFromBin(row, eis):
        """
        Set the optional numReceptor in row from the EndianInput (eis) instance.
        """
        row._numReceptorExists = eis.readBool()
        if row._numReceptorExists:

            row._numReceptor = eis.readInt()

    @staticmethod
    def calEffFromBin(row, eis):
        """
        Set the optional calEff in row from the EndianInput (eis) instance.
        """
        row._calEffExists = eis.readBool()
        if row._calEffExists:

            calEffDim1 = eis.readInt()
            calEffDim2 = eis.readInt()
            thisList = []
            for i in range(calEffDim1):
                thisList_j = []
                for j in range(calEffDim2):
                    thisValue = eis.readFloat()
                    thisList_j.append(thisValue)
                thisList.append(thisList_j)
            row._calEff = thisList

    @staticmethod
    def noiseCalFromBin(row, eis):
        """
        Set the optional noiseCal in row from the EndianInput (eis) instance.
        """
        row._noiseCalExists = eis.readBool()
        if row._noiseCalExists:

            noiseCalDim1 = eis.readInt()
            thisList = []
            for i in range(noiseCalDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._noiseCal = thisList

    @staticmethod
    def coupledNoiseCalFromBin(row, eis):
        """
        Set the optional coupledNoiseCal in row from the EndianInput (eis) instance.
        """
        row._coupledNoiseCalExists = eis.readBool()
        if row._coupledNoiseCalExists:

            coupledNoiseCalDim1 = eis.readInt()
            coupledNoiseCalDim2 = eis.readInt()
            thisList = []
            for i in range(coupledNoiseCalDim1):
                thisList_j = []
                for j in range(coupledNoiseCalDim2):
                    thisValue = eis.readFloat()
                    thisList_j.append(thisValue)
                thisList.append(thisList_j)
            row._coupledNoiseCal = thisList

    @staticmethod
    def temperatureLoadFromBin(row, eis):
        """
        Set the optional temperatureLoad in row from the EndianInput (eis) instance.
        """
        row._temperatureLoadExists = eis.readBool()
        if row._temperatureLoadExists:

            row._temperatureLoad = Temperature.from1DBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaId"] = CalDeviceRow.antennaIdFromBin
        _fromBinMethods["spectralWindowId"] = CalDeviceRow.spectralWindowIdFromBin
        _fromBinMethods["timeInterval"] = CalDeviceRow.timeIntervalFromBin
        _fromBinMethods["feedId"] = CalDeviceRow.feedIdFromBin
        _fromBinMethods["numCalload"] = CalDeviceRow.numCalloadFromBin
        _fromBinMethods["calLoadNames"] = CalDeviceRow.calLoadNamesFromBin

        _fromBinMethods["numReceptor"] = CalDeviceRow.numReceptorFromBin
        _fromBinMethods["calEff"] = CalDeviceRow.calEffFromBin
        _fromBinMethods["noiseCal"] = CalDeviceRow.noiseCalFromBin
        _fromBinMethods["coupledNoiseCal"] = CalDeviceRow.coupledNoiseCalFromBin
        _fromBinMethods["temperatureLoad"] = CalDeviceRow.temperatureLoadFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CalDeviceRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalDevice",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute timeInterval

    _timeInterval = ArrayTimeInterval()

    def getTimeInterval(self):
        """
        Get timeInterval.
        return timeInterval as ArrayTimeInterval
        """

        # make sure it is a copy of ArrayTimeInterval
        return ArrayTimeInterval(self._timeInterval)

    def setTimeInterval(self, timeInterval):
        """
        Set timeInterval with the specified ArrayTimeInterval value.
        timeInterval The ArrayTimeInterval value to which timeInterval is to be set.
        The value of timeInterval can be anything allowed by the ArrayTimeInterval constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the timeInterval field, which is part of the key, after this row has been added to this table."
            )

        self._timeInterval = ArrayTimeInterval(timeInterval)

    # ===> Attribute numCalload

    _numCalload = 0

    def getNumCalload(self):
        """
        Get numCalload.
        return numCalload as int
        """

        return self._numCalload

    def setNumCalload(self, numCalload):
        """
        Set numCalload with the specified int value.
        numCalload The int value to which numCalload is to be set.


        """

        self._numCalload = int(numCalload)

    # ===> Attribute calLoadNames

    _calLoadNames = None  # this is a 1D list of CalibrationDevice

    def getCalLoadNames(self):
        """
        Get calLoadNames.
        return calLoadNames as CalibrationDevice []
        """

        return copy.deepcopy(self._calLoadNames)

    def setCalLoadNames(self, calLoadNames):
        """
        Set calLoadNames with the specified CalibrationDevice []  value.
        calLoadNames The CalibrationDevice []  value to which calLoadNames is to be set.


        """

        # value must be a list
        if not isinstance(calLoadNames, list):
            raise ValueError("The value of calLoadNames must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(calLoadNames)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of calLoadNames is not correct")

            # the type of the values in the list must be CalibrationDevice
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(calLoadNames, CalibrationDevice):
                raise ValueError(
                    "type of the first value in calLoadNames is not CalibrationDevice as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._calLoadNames = copy.deepcopy(calLoadNames)
        except Exception as exc:
            raise ValueError("Invalid calLoadNames : " + str(exc))

    # ===> Attribute numReceptor, which is optional
    _numReceptorExists = False

    _numReceptor = 0

    def isNumReceptorExists(self):
        """
        The attribute numReceptor is optional. Return True if this attribute exists.
        return True if and only if the numReceptor attribute exists.
        """
        return self._numReceptorExists

    def getNumReceptor(self):
        """
        Get numReceptor, which is optional.
        return numReceptor as int
        raises ValueError If numReceptor does not exist.
        """
        if not self._numReceptorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numReceptor
                + " attribute in table CalDevice does not exist!"
            )

        return self._numReceptor

    def setNumReceptor(self, numReceptor):
        """
        Set numReceptor with the specified int value.
        numReceptor The int value to which numReceptor is to be set.


        """

        self._numReceptor = int(numReceptor)

        self._numReceptorExists = True

    def clearNumReceptor(self):
        """
        Mark numReceptor, which is an optional field, as non-existent.
        """
        self._numReceptorExists = False

    # ===> Attribute calEff, which is optional
    _calEffExists = False

    _calEff = None  # this is a 2D list of float

    def isCalEffExists(self):
        """
        The attribute calEff is optional. Return True if this attribute exists.
        return True if and only if the calEff attribute exists.
        """
        return self._calEffExists

    def getCalEff(self):
        """
        Get calEff, which is optional.
        return calEff as float []  []
        raises ValueError If calEff does not exist.
        """
        if not self._calEffExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + calEff
                + " attribute in table CalDevice does not exist!"
            )

        return copy.deepcopy(self._calEff)

    def setCalEff(self, calEff):
        """
        Set calEff with the specified float []  []  value.
        calEff The float []  []  value to which calEff is to be set.


        """

        # value must be a list
        if not isinstance(calEff, list):
            raise ValueError("The value of calEff must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(calEff)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of calEff is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(calEff, float):
                raise ValueError(
                    "type of the first value in calEff is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._calEff = copy.deepcopy(calEff)
        except Exception as exc:
            raise ValueError("Invalid calEff : " + str(exc))

        self._calEffExists = True

    def clearCalEff(self):
        """
        Mark calEff, which is an optional field, as non-existent.
        """
        self._calEffExists = False

    # ===> Attribute noiseCal, which is optional
    _noiseCalExists = False

    _noiseCal = None  # this is a 1D list of float

    def isNoiseCalExists(self):
        """
        The attribute noiseCal is optional. Return True if this attribute exists.
        return True if and only if the noiseCal attribute exists.
        """
        return self._noiseCalExists

    def getNoiseCal(self):
        """
        Get noiseCal, which is optional.
        return noiseCal as float []
        raises ValueError If noiseCal does not exist.
        """
        if not self._noiseCalExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + noiseCal
                + " attribute in table CalDevice does not exist!"
            )

        return copy.deepcopy(self._noiseCal)

    def setNoiseCal(self, noiseCal):
        """
        Set noiseCal with the specified float []  value.
        noiseCal The float []  value to which noiseCal is to be set.


        """

        # value must be a list
        if not isinstance(noiseCal, list):
            raise ValueError("The value of noiseCal must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(noiseCal)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of noiseCal is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(noiseCal, float):
                raise ValueError(
                    "type of the first value in noiseCal is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._noiseCal = copy.deepcopy(noiseCal)
        except Exception as exc:
            raise ValueError("Invalid noiseCal : " + str(exc))

        self._noiseCalExists = True

    def clearNoiseCal(self):
        """
        Mark noiseCal, which is an optional field, as non-existent.
        """
        self._noiseCalExists = False

    # ===> Attribute coupledNoiseCal, which is optional
    _coupledNoiseCalExists = False

    _coupledNoiseCal = None  # this is a 2D list of float

    def isCoupledNoiseCalExists(self):
        """
        The attribute coupledNoiseCal is optional. Return True if this attribute exists.
        return True if and only if the coupledNoiseCal attribute exists.
        """
        return self._coupledNoiseCalExists

    def getCoupledNoiseCal(self):
        """
        Get coupledNoiseCal, which is optional.
        return coupledNoiseCal as float []  []
        raises ValueError If coupledNoiseCal does not exist.
        """
        if not self._coupledNoiseCalExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + coupledNoiseCal
                + " attribute in table CalDevice does not exist!"
            )

        return copy.deepcopy(self._coupledNoiseCal)

    def setCoupledNoiseCal(self, coupledNoiseCal):
        """
        Set coupledNoiseCal with the specified float []  []  value.
        coupledNoiseCal The float []  []  value to which coupledNoiseCal is to be set.


        """

        # value must be a list
        if not isinstance(coupledNoiseCal, list):
            raise ValueError("The value of coupledNoiseCal must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(coupledNoiseCal)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of coupledNoiseCal is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(coupledNoiseCal, float):
                raise ValueError(
                    "type of the first value in coupledNoiseCal is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._coupledNoiseCal = copy.deepcopy(coupledNoiseCal)
        except Exception as exc:
            raise ValueError("Invalid coupledNoiseCal : " + str(exc))

        self._coupledNoiseCalExists = True

    def clearCoupledNoiseCal(self):
        """
        Mark coupledNoiseCal, which is an optional field, as non-existent.
        """
        self._coupledNoiseCalExists = False

    # ===> Attribute temperatureLoad, which is optional
    _temperatureLoadExists = False

    _temperatureLoad = None  # this is a 1D list of Temperature

    def isTemperatureLoadExists(self):
        """
        The attribute temperatureLoad is optional. Return True if this attribute exists.
        return True if and only if the temperatureLoad attribute exists.
        """
        return self._temperatureLoadExists

    def getTemperatureLoad(self):
        """
        Get temperatureLoad, which is optional.
        return temperatureLoad as Temperature []
        raises ValueError If temperatureLoad does not exist.
        """
        if not self._temperatureLoadExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + temperatureLoad
                + " attribute in table CalDevice does not exist!"
            )

        return copy.deepcopy(self._temperatureLoad)

    def setTemperatureLoad(self, temperatureLoad):
        """
        Set temperatureLoad with the specified Temperature []  value.
        temperatureLoad The Temperature []  value to which temperatureLoad is to be set.
        The value of temperatureLoad can be anything allowed by the Temperature []  constructor.

        """

        # value must be a list
        if not isinstance(temperatureLoad, list):
            raise ValueError("The value of temperatureLoad must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(temperatureLoad)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of temperatureLoad is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(temperatureLoad, Temperature):
                raise ValueError(
                    "type of the first value in temperatureLoad is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._temperatureLoad = copy.deepcopy(temperatureLoad)
        except Exception as exc:
            raise ValueError("Invalid temperatureLoad : " + str(exc))

        self._temperatureLoadExists = True

    def clearTemperatureLoad(self):
        """
        Mark temperatureLoad, which is an optional field, as non-existent.
        """
        self._temperatureLoadExists = False

    # Extrinsic Table Attributes

    # ===> Attribute antennaId

    _antennaId = Tag()

    def getAntennaId(self):
        """
        Get antennaId.
        return antennaId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._antennaId)

    def setAntennaId(self, antennaId):
        """
        Set antennaId with the specified Tag value.
        antennaId The Tag value to which antennaId is to be set.
        The value of antennaId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the antennaId field, which is part of the key, after this row has been added to this table."
            )

        self._antennaId = Tag(antennaId)

    # ===> Attribute feedId

    _feedId = 0

    def getFeedId(self):
        """
        Get feedId.
        return feedId as int
        """

        return self._feedId

    def setFeedId(self, feedId):
        """
        Set feedId with the specified int value.
        feedId The int value to which feedId is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the feedId field, which is part of the key, after this row has been added to this table."
            )

        self._feedId = int(feedId)

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

    # Links

    def getAntennaUsingAntennaId(self):
        """
        Returns the row in the Antenna table having Antenna.antennaId == antennaId

        """

        return self._table.getContainer().getAntenna().getRowByKey(self._antennaId)

    def getSpectralWindowUsingSpectralWindowId(self):
        """
        Returns the row in the SpectralWindow table having SpectralWindow.spectralWindowId == spectralWindowId

        """

        return (
            self._table.getContainer()
            .getSpectralWindow()
            .getRowByKey(self._spectralWindowId)
        )

    # ===> Slice link from a row of CalDevice table to a collection of row of Feed table.
    def getFeeds(self):
        """
        Get the collection of rows in the Feed table having feedId == this.feedId
        """

        return self._table.getContainer().getFeed().getRowByFeedId(self._feedId)

    # comparison methods

    def compareNoAutoInc(
        self,
        antennaId,
        spectralWindowId,
        timeInterval,
        feedId,
        numCalload,
        calLoadNames,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalDeviceRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaId is a Tag, compare using the equals method.
        if not self._antennaId.equals(antennaId):
            return False

        # spectralWindowId is a Tag, compare using the equals method.
        if not self._spectralWindowId.equals(spectralWindowId):
            return False

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # feedId is a int, compare using the == operator.
        if not (self._feedId == feedId):
            return False

        # numCalload is a int, compare using the == operator.
        if not (self._numCalload == numCalload):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._calLoadNames) != len(calLoadNames):
            return False
        for indx in range(len(calLoadNames)):

            # calLoadNames is a list of CalibrationDevice, compare using == operator.
            if not (self._calLoadNames[indx] == calLoadNames[indx]):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumCalload(), otherRow.getCalLoadNames()
        )

    def compareRequiredValue(self, numCalload, calLoadNames):

        # numCalload is a int, compare using the == operator.
        if not (self._numCalload == numCalload):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._calLoadNames) != len(calLoadNames):
            return False
        for indx in range(len(calLoadNames)):

            # calLoadNames is a list of CalibrationDevice, compare using == operator.
            if not (self._calLoadNames[indx] == calLoadNames[indx]):
                return False

        return True


# initialize the dictionary that maps fields to init methods
CalDeviceRow.initFromBinMethods()
