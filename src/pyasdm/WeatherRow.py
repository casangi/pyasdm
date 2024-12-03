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
# File WeatherRow.py
#

import pyasdm.WeatherTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from xml.dom import minidom

import copy


class WeatherRow:
    """
    The WeatherRow class is a row of a WeatherTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a WeatherRow.
        When row is None, create an empty row attached to table, which must be a WeatherTable.
        When row is given, copy those values in to the new row. The row argument must be a WeatherRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.WeatherTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        if row is not None:
            if not isinstance(row, WeatherRow):
                raise ValueError("row must be a MainRow")

            self._stationId = Tag(row._stationId)

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            # by default set systematically pressure's value to something not None

            if row._pressureExists:

                self._pressure = Pressure(row._pressure)

                self._pressureExists = True

            # by default set systematically relHumidity's value to something not None

            if row._relHumidityExists:

                self._relHumidity = Humidity(row._relHumidity)

                self._relHumidityExists = True

            # by default set systematically temperature's value to something not None

            if row._temperatureExists:

                self._temperature = Temperature(row._temperature)

                self._temperatureExists = True

            # by default set systematically windDirection's value to something not None

            if row._windDirectionExists:

                self._windDirection = Angle(row._windDirection)

                self._windDirectionExists = True

            # by default set systematically windSpeed's value to something not None

            if row._windSpeedExists:

                self._windSpeed = Speed(row._windSpeed)

                self._windSpeedExists = True

            # by default set systematically windMax's value to something not None

            if row._windMaxExists:

                self._windMax = Speed(row._windMax)

                self._windMaxExists = True

            # by default set systematically dewPoint's value to something not None

            if row._dewPointExists:

                self._dewPoint = Temperature(row._dewPoint)

                self._dewPointExists = True

            # by default set systematically numLayer's value to something not None

            if row._numLayerExists:

                self._numLayer = row._numLayer

                self._numLayerExists = True

            # by default set systematically layerHeight's value to something not None

            if row._layerHeightExists:

                # layerHeight is a list, make a deep copy
                self.layerHeight = copy.deepcopy(row.layerHeight)

                self._layerHeightExists = True

            # by default set systematically temperatureProfile's value to something not None

            if row._temperatureProfileExists:

                # temperatureProfile is a list, make a deep copy
                self.temperatureProfile = copy.deepcopy(row.temperatureProfile)

                self._temperatureProfileExists = True

            # by default set systematically cloudMonitor's value to something not None

            if row._cloudMonitorExists:

                self._cloudMonitor = Temperature(row._cloudMonitor)

                self._cloudMonitorExists = True

            # by default set systematically numWVR's value to something not None

            if row._numWVRExists:

                self._numWVR = row._numWVR

                self._numWVRExists = True

            # by default set systematically wvrTemp's value to something not None

            if row._wvrTempExists:

                # wvrTemp is a list, make a deep copy
                self.wvrTemp = copy.deepcopy(row.wvrTemp)

                self._wvrTempExists = True

            # by default set systematically water's value to something not None

            if row._waterExists:

                self._water = row._water

                self._waterExists = True

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

        if self._pressureExists:

            result += Parser.extendedValueToXML("pressure", self._pressure)

        if self._relHumidityExists:

            result += Parser.extendedValueToXML("relHumidity", self._relHumidity)

        if self._temperatureExists:

            result += Parser.extendedValueToXML("temperature", self._temperature)

        if self._windDirectionExists:

            result += Parser.extendedValueToXML("windDirection", self._windDirection)

        if self._windSpeedExists:

            result += Parser.extendedValueToXML("windSpeed", self._windSpeed)

        if self._windMaxExists:

            result += Parser.extendedValueToXML("windMax", self._windMax)

        if self._dewPointExists:

            result += Parser.extendedValueToXML("dewPoint", self._dewPoint)

        if self._numLayerExists:

            result += Parser.valueToXML("numLayer", self._numLayer)

        if self._layerHeightExists:

            result += Parser.listExtendedValueToXML("layerHeight", self._layerHeight)

        if self._temperatureProfileExists:

            result += Parser.listExtendedValueToXML(
                "temperatureProfile", self._temperatureProfile
            )

        if self._cloudMonitorExists:

            result += Parser.extendedValueToXML("cloudMonitor", self._cloudMonitor)

        if self._numWVRExists:

            result += Parser.valueToXML("numWVR", self._numWVR)

        if self._wvrTempExists:

            result += Parser.listExtendedValueToXML("wvrTemp", self._wvrTemp)

        if self._waterExists:

            result += Parser.valueToXML("water", self._water)

        # extrinsic attributes

        result += Parser.extendedValueToXML("stationId", self._stationId)

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
                "xmlrow is not a string or a minidom.Element", "WeatherTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "WeatherTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data)

        pressureNode = rowdom.getElementsByTagName("pressure")
        if len(pressureNode) > 0:

            self._pressure = Pressure(pressureNode[0].firstChild.data)

            self._pressureExists = True

        relHumidityNode = rowdom.getElementsByTagName("relHumidity")
        if len(relHumidityNode) > 0:

            self._relHumidity = Humidity(relHumidityNode[0].firstChild.data)

            self._relHumidityExists = True

        temperatureNode = rowdom.getElementsByTagName("temperature")
        if len(temperatureNode) > 0:

            self._temperature = Temperature(temperatureNode[0].firstChild.data)

            self._temperatureExists = True

        windDirectionNode = rowdom.getElementsByTagName("windDirection")
        if len(windDirectionNode) > 0:

            self._windDirection = Angle(windDirectionNode[0].firstChild.data)

            self._windDirectionExists = True

        windSpeedNode = rowdom.getElementsByTagName("windSpeed")
        if len(windSpeedNode) > 0:

            self._windSpeed = Speed(windSpeedNode[0].firstChild.data)

            self._windSpeedExists = True

        windMaxNode = rowdom.getElementsByTagName("windMax")
        if len(windMaxNode) > 0:

            self._windMax = Speed(windMaxNode[0].firstChild.data)

            self._windMaxExists = True

        dewPointNode = rowdom.getElementsByTagName("dewPoint")
        if len(dewPointNode) > 0:

            self._dewPoint = Temperature(dewPointNode[0].firstChild.data)

            self._dewPointExists = True

        numLayerNode = rowdom.getElementsByTagName("numLayer")
        if len(numLayerNode) > 0:

            self._numLayer = int(numLayerNode[0].firstChild.data)

            self._numLayerExists = True

        layerHeightNode = rowdom.getElementsByTagName("layerHeight")
        if len(layerHeightNode) > 0:

            layerHeightStr = layerHeightNode[0].firstChild.data
            self._layerHeight = Parser.stringListToLists(
                layerHeightStr, Length, "Weather"
            )

            self._layerHeightExists = True

        temperatureProfileNode = rowdom.getElementsByTagName("temperatureProfile")
        if len(temperatureProfileNode) > 0:

            temperatureProfileStr = temperatureProfileNode[0].firstChild.data
            self._temperatureProfile = Parser.stringListToLists(
                temperatureProfileStr, Temperature, "Weather"
            )

            self._temperatureProfileExists = True

        cloudMonitorNode = rowdom.getElementsByTagName("cloudMonitor")
        if len(cloudMonitorNode) > 0:

            self._cloudMonitor = Temperature(cloudMonitorNode[0].firstChild.data)

            self._cloudMonitorExists = True

        numWVRNode = rowdom.getElementsByTagName("numWVR")
        if len(numWVRNode) > 0:

            self._numWVR = int(numWVRNode[0].firstChild.data)

            self._numWVRExists = True

        wvrTempNode = rowdom.getElementsByTagName("wvrTemp")
        if len(wvrTempNode) > 0:

            wvrTempStr = wvrTempNode[0].firstChild.data
            self._wvrTemp = Parser.stringListToLists(wvrTempStr, Temperature, "Weather")

            self._wvrTempExists = True

        waterNode = rowdom.getElementsByTagName("water")
        if len(waterNode) > 0:

            self._water = double(waterNode[0].firstChild.data)

            self._waterExists = True

        # extrinsic attribute values

        stationIdNode = rowdom.getElementsByTagName("stationId")[0]

        self._stationId = Tag(stationIdNode.firstChild.data)

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

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

    # ===> Attribute pressure, which is optional
    _pressureExists = False

    _pressure = Pressure()

    def isPressureExists(self):
        """
        The attribute pressure is optional. Return True if this attribute exists.
        return True if and only if the pressure attribute exists.
        """
        return self._pressureExists

    def getPressure(self):
        """
        Get pressure, which is optional.
        return pressure as Pressure
        raises ValueError If pressure does not exist.
        """
        if not self._pressureExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + pressure
                + " attribute in table Weather does not exist!"
            )

        # make sure it is a copy of Pressure
        return Pressure(self._pressure)

    def setPressure(self, pressure):
        """
        Set pressure with the specified Pressure value.
        pressure The Pressure value to which pressure is to be set.
        The value of pressure can be anything allowed by the Pressure constructor.

        """

        self._pressure = Pressure(pressure)

        self._pressureExists = True

    def clearPressure(self):
        """
        Mark pressure, which is an optional field, as non-existent.
        """
        self._pressureExists = False

    # ===> Attribute relHumidity, which is optional
    _relHumidityExists = False

    _relHumidity = Humidity()

    def isRelHumidityExists(self):
        """
        The attribute relHumidity is optional. Return True if this attribute exists.
        return True if and only if the relHumidity attribute exists.
        """
        return self._relHumidityExists

    def getRelHumidity(self):
        """
        Get relHumidity, which is optional.
        return relHumidity as Humidity
        raises ValueError If relHumidity does not exist.
        """
        if not self._relHumidityExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + relHumidity
                + " attribute in table Weather does not exist!"
            )

        # make sure it is a copy of Humidity
        return Humidity(self._relHumidity)

    def setRelHumidity(self, relHumidity):
        """
        Set relHumidity with the specified Humidity value.
        relHumidity The Humidity value to which relHumidity is to be set.
        The value of relHumidity can be anything allowed by the Humidity constructor.

        """

        self._relHumidity = Humidity(relHumidity)

        self._relHumidityExists = True

    def clearRelHumidity(self):
        """
        Mark relHumidity, which is an optional field, as non-existent.
        """
        self._relHumidityExists = False

    # ===> Attribute temperature, which is optional
    _temperatureExists = False

    _temperature = Temperature()

    def isTemperatureExists(self):
        """
        The attribute temperature is optional. Return True if this attribute exists.
        return True if and only if the temperature attribute exists.
        """
        return self._temperatureExists

    def getTemperature(self):
        """
        Get temperature, which is optional.
        return temperature as Temperature
        raises ValueError If temperature does not exist.
        """
        if not self._temperatureExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + temperature
                + " attribute in table Weather does not exist!"
            )

        # make sure it is a copy of Temperature
        return Temperature(self._temperature)

    def setTemperature(self, temperature):
        """
        Set temperature with the specified Temperature value.
        temperature The Temperature value to which temperature is to be set.
        The value of temperature can be anything allowed by the Temperature constructor.

        """

        self._temperature = Temperature(temperature)

        self._temperatureExists = True

    def clearTemperature(self):
        """
        Mark temperature, which is an optional field, as non-existent.
        """
        self._temperatureExists = False

    # ===> Attribute windDirection, which is optional
    _windDirectionExists = False

    _windDirection = Angle()

    def isWindDirectionExists(self):
        """
        The attribute windDirection is optional. Return True if this attribute exists.
        return True if and only if the windDirection attribute exists.
        """
        return self._windDirectionExists

    def getWindDirection(self):
        """
        Get windDirection, which is optional.
        return windDirection as Angle
        raises ValueError If windDirection does not exist.
        """
        if not self._windDirectionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + windDirection
                + " attribute in table Weather does not exist!"
            )

        # make sure it is a copy of Angle
        return Angle(self._windDirection)

    def setWindDirection(self, windDirection):
        """
        Set windDirection with the specified Angle value.
        windDirection The Angle value to which windDirection is to be set.
        The value of windDirection can be anything allowed by the Angle constructor.

        """

        self._windDirection = Angle(windDirection)

        self._windDirectionExists = True

    def clearWindDirection(self):
        """
        Mark windDirection, which is an optional field, as non-existent.
        """
        self._windDirectionExists = False

    # ===> Attribute windSpeed, which is optional
    _windSpeedExists = False

    _windSpeed = Speed()

    def isWindSpeedExists(self):
        """
        The attribute windSpeed is optional. Return True if this attribute exists.
        return True if and only if the windSpeed attribute exists.
        """
        return self._windSpeedExists

    def getWindSpeed(self):
        """
        Get windSpeed, which is optional.
        return windSpeed as Speed
        raises ValueError If windSpeed does not exist.
        """
        if not self._windSpeedExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + windSpeed
                + " attribute in table Weather does not exist!"
            )

        # make sure it is a copy of Speed
        return Speed(self._windSpeed)

    def setWindSpeed(self, windSpeed):
        """
        Set windSpeed with the specified Speed value.
        windSpeed The Speed value to which windSpeed is to be set.
        The value of windSpeed can be anything allowed by the Speed constructor.

        """

        self._windSpeed = Speed(windSpeed)

        self._windSpeedExists = True

    def clearWindSpeed(self):
        """
        Mark windSpeed, which is an optional field, as non-existent.
        """
        self._windSpeedExists = False

    # ===> Attribute windMax, which is optional
    _windMaxExists = False

    _windMax = Speed()

    def isWindMaxExists(self):
        """
        The attribute windMax is optional. Return True if this attribute exists.
        return True if and only if the windMax attribute exists.
        """
        return self._windMaxExists

    def getWindMax(self):
        """
        Get windMax, which is optional.
        return windMax as Speed
        raises ValueError If windMax does not exist.
        """
        if not self._windMaxExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + windMax
                + " attribute in table Weather does not exist!"
            )

        # make sure it is a copy of Speed
        return Speed(self._windMax)

    def setWindMax(self, windMax):
        """
        Set windMax with the specified Speed value.
        windMax The Speed value to which windMax is to be set.
        The value of windMax can be anything allowed by the Speed constructor.

        """

        self._windMax = Speed(windMax)

        self._windMaxExists = True

    def clearWindMax(self):
        """
        Mark windMax, which is an optional field, as non-existent.
        """
        self._windMaxExists = False

    # ===> Attribute dewPoint, which is optional
    _dewPointExists = False

    _dewPoint = Temperature()

    def isDewPointExists(self):
        """
        The attribute dewPoint is optional. Return True if this attribute exists.
        return True if and only if the dewPoint attribute exists.
        """
        return self._dewPointExists

    def getDewPoint(self):
        """
        Get dewPoint, which is optional.
        return dewPoint as Temperature
        raises ValueError If dewPoint does not exist.
        """
        if not self._dewPointExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + dewPoint
                + " attribute in table Weather does not exist!"
            )

        # make sure it is a copy of Temperature
        return Temperature(self._dewPoint)

    def setDewPoint(self, dewPoint):
        """
        Set dewPoint with the specified Temperature value.
        dewPoint The Temperature value to which dewPoint is to be set.
        The value of dewPoint can be anything allowed by the Temperature constructor.

        """

        self._dewPoint = Temperature(dewPoint)

        self._dewPointExists = True

    def clearDewPoint(self):
        """
        Mark dewPoint, which is an optional field, as non-existent.
        """
        self._dewPointExists = False

    # ===> Attribute numLayer, which is optional
    _numLayerExists = False

    _numLayer = 0

    def isNumLayerExists(self):
        """
        The attribute numLayer is optional. Return True if this attribute exists.
        return True if and only if the numLayer attribute exists.
        """
        return self._numLayerExists

    def getNumLayer(self):
        """
        Get numLayer, which is optional.
        return numLayer as int
        raises ValueError If numLayer does not exist.
        """
        if not self._numLayerExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numLayer
                + " attribute in table Weather does not exist!"
            )

        return self._numLayer

    def setNumLayer(self, numLayer):
        """
        Set numLayer with the specified int value.
        numLayer The int value to which numLayer is to be set.


        """

        self._numLayer = int(numLayer)

        self._numLayerExists = True

    def clearNumLayer(self):
        """
        Mark numLayer, which is an optional field, as non-existent.
        """
        self._numLayerExists = False

    # ===> Attribute layerHeight, which is optional
    _layerHeightExists = False

    _layerHeight = None  # this is a 1D list of Length

    def isLayerHeightExists(self):
        """
        The attribute layerHeight is optional. Return True if this attribute exists.
        return True if and only if the layerHeight attribute exists.
        """
        return self._layerHeightExists

    def getLayerHeight(self):
        """
        Get layerHeight, which is optional.
        return layerHeight as Length []
        raises ValueError If layerHeight does not exist.
        """
        if not self._layerHeightExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + layerHeight
                + " attribute in table Weather does not exist!"
            )

        return copy.deepcopy(self._layerHeight)

    def setLayerHeight(self, layerHeight):
        """
        Set layerHeight with the specified Length []  value.
        layerHeight The Length []  value to which layerHeight is to be set.
        The value of layerHeight can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(layerHeight, list):
            raise ValueError("The value of layerHeight must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(layerHeight)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of layerHeight is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(layerHeight, Length):
                raise ValueError(
                    "type of the first value in layerHeight is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._layerHeight = copy.deepcopy(layerHeight)
        except Exception as exc:
            raise ValueError("Invalid layerHeight : " + str(exc))

        self._layerHeightExists = True

    def clearLayerHeight(self):
        """
        Mark layerHeight, which is an optional field, as non-existent.
        """
        self._layerHeightExists = False

    # ===> Attribute temperatureProfile, which is optional
    _temperatureProfileExists = False

    _temperatureProfile = None  # this is a 1D list of Temperature

    def isTemperatureProfileExists(self):
        """
        The attribute temperatureProfile is optional. Return True if this attribute exists.
        return True if and only if the temperatureProfile attribute exists.
        """
        return self._temperatureProfileExists

    def getTemperatureProfile(self):
        """
        Get temperatureProfile, which is optional.
        return temperatureProfile as Temperature []
        raises ValueError If temperatureProfile does not exist.
        """
        if not self._temperatureProfileExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + temperatureProfile
                + " attribute in table Weather does not exist!"
            )

        return copy.deepcopy(self._temperatureProfile)

    def setTemperatureProfile(self, temperatureProfile):
        """
        Set temperatureProfile with the specified Temperature []  value.
        temperatureProfile The Temperature []  value to which temperatureProfile is to be set.
        The value of temperatureProfile can be anything allowed by the Temperature []  constructor.

        """

        # value must be a list
        if not isinstance(temperatureProfile, list):
            raise ValueError("The value of temperatureProfile must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(temperatureProfile)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of temperatureProfile is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(temperatureProfile, Temperature):
                raise ValueError(
                    "type of the first value in temperatureProfile is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._temperatureProfile = copy.deepcopy(temperatureProfile)
        except Exception as exc:
            raise ValueError("Invalid temperatureProfile : " + str(exc))

        self._temperatureProfileExists = True

    def clearTemperatureProfile(self):
        """
        Mark temperatureProfile, which is an optional field, as non-existent.
        """
        self._temperatureProfileExists = False

    # ===> Attribute cloudMonitor, which is optional
    _cloudMonitorExists = False

    _cloudMonitor = Temperature()

    def isCloudMonitorExists(self):
        """
        The attribute cloudMonitor is optional. Return True if this attribute exists.
        return True if and only if the cloudMonitor attribute exists.
        """
        return self._cloudMonitorExists

    def getCloudMonitor(self):
        """
        Get cloudMonitor, which is optional.
        return cloudMonitor as Temperature
        raises ValueError If cloudMonitor does not exist.
        """
        if not self._cloudMonitorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + cloudMonitor
                + " attribute in table Weather does not exist!"
            )

        # make sure it is a copy of Temperature
        return Temperature(self._cloudMonitor)

    def setCloudMonitor(self, cloudMonitor):
        """
        Set cloudMonitor with the specified Temperature value.
        cloudMonitor The Temperature value to which cloudMonitor is to be set.
        The value of cloudMonitor can be anything allowed by the Temperature constructor.

        """

        self._cloudMonitor = Temperature(cloudMonitor)

        self._cloudMonitorExists = True

    def clearCloudMonitor(self):
        """
        Mark cloudMonitor, which is an optional field, as non-existent.
        """
        self._cloudMonitorExists = False

    # ===> Attribute numWVR, which is optional
    _numWVRExists = False

    _numWVR = 0

    def isNumWVRExists(self):
        """
        The attribute numWVR is optional. Return True if this attribute exists.
        return True if and only if the numWVR attribute exists.
        """
        return self._numWVRExists

    def getNumWVR(self):
        """
        Get numWVR, which is optional.
        return numWVR as int
        raises ValueError If numWVR does not exist.
        """
        if not self._numWVRExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numWVR
                + " attribute in table Weather does not exist!"
            )

        return self._numWVR

    def setNumWVR(self, numWVR):
        """
        Set numWVR with the specified int value.
        numWVR The int value to which numWVR is to be set.


        """

        self._numWVR = int(numWVR)

        self._numWVRExists = True

    def clearNumWVR(self):
        """
        Mark numWVR, which is an optional field, as non-existent.
        """
        self._numWVRExists = False

    # ===> Attribute wvrTemp, which is optional
    _wvrTempExists = False

    _wvrTemp = None  # this is a 1D list of Temperature

    def isWvrTempExists(self):
        """
        The attribute wvrTemp is optional. Return True if this attribute exists.
        return True if and only if the wvrTemp attribute exists.
        """
        return self._wvrTempExists

    def getWvrTemp(self):
        """
        Get wvrTemp, which is optional.
        return wvrTemp as Temperature []
        raises ValueError If wvrTemp does not exist.
        """
        if not self._wvrTempExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + wvrTemp
                + " attribute in table Weather does not exist!"
            )

        return copy.deepcopy(self._wvrTemp)

    def setWvrTemp(self, wvrTemp):
        """
        Set wvrTemp with the specified Temperature []  value.
        wvrTemp The Temperature []  value to which wvrTemp is to be set.
        The value of wvrTemp can be anything allowed by the Temperature []  constructor.

        """

        # value must be a list
        if not isinstance(wvrTemp, list):
            raise ValueError("The value of wvrTemp must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(wvrTemp)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of wvrTemp is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(wvrTemp, Temperature):
                raise ValueError(
                    "type of the first value in wvrTemp is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._wvrTemp = copy.deepcopy(wvrTemp)
        except Exception as exc:
            raise ValueError("Invalid wvrTemp : " + str(exc))

        self._wvrTempExists = True

    def clearWvrTemp(self):
        """
        Mark wvrTemp, which is an optional field, as non-existent.
        """
        self._wvrTempExists = False

    # ===> Attribute water, which is optional
    _waterExists = False

    _water = None

    def isWaterExists(self):
        """
        The attribute water is optional. Return True if this attribute exists.
        return True if and only if the water attribute exists.
        """
        return self._waterExists

    def getWater(self):
        """
        Get water, which is optional.
        return water as double
        raises ValueError If water does not exist.
        """
        if not self._waterExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + water
                + " attribute in table Weather does not exist!"
            )

        return self._water

    def setWater(self, water):
        """
        Set water with the specified double value.
        water The double value to which water is to be set.


        """

        self._water = double(water)

        self._waterExists = True

    def clearWater(self):
        """
        Mark water, which is an optional field, as non-existent.
        """
        self._waterExists = False

    # Extrinsic Table Attributes

    # ===> Attribute stationId

    _stationId = Tag()

    def getStationId(self):
        """
        Get stationId.
        return stationId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._stationId)

    def setStationId(self, stationId):
        """
        Set stationId with the specified Tag value.
        stationId The Tag value to which stationId is to be set.
        The value of stationId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the stationId field, which is part of the key, after this row has been added to this table."
            )

        self._stationId = Tag(stationId)

    # Links

    def getStationUsingStationId(self):
        """
        Returns the row in the Station table having Station.stationId == stationId

        """

        return self._table.getContainer().getStation().getRowByKey(self._stationId)

    # comparison methods

    def compareNoAutoInc(self, stationId, timeInterval):
        """
        Compare each attribute except the autoincrementable one of this WeatherRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # stationId is a Tag, compare using the equals method.
        if not self._stationId.equals(stationId):
            return False

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return True

    def compareRequiredValue(
        self,
    ):

        return True
