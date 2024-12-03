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
# File WeatherTable.py
#

import pyasdm.ASDM

from .WeatherRow import WeatherRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class WeatherTable(Representable):
    """
    The WeatherTable class is an Alma table.

     Role
     Weather station information.

     Generated from model's revision -1, branch

     Attributes of Weather

                  Key

    stationId Tag refers to a unique row in StationTable.

    timeInterval ArrayTimeInterval the time interval for which the row's content is valid.




                  Value (Optional)

    pressure Pressure  the ambient pressure.

    relHumidity Humidity  the relative humidity.

    temperature Temperature  the ambient temperature.

    windDirection Angle  the wind direction.

    windSpeed Speed  the wind speed.

    windMax Speed  the maximum wind speed

    dewPoint Temperature  the dew point's value.

    numLayer int  NLayer the number of layers in the temperature profile.

    layerHeight Length []   numLayer  the height of each layer for the temperature profile.

    temperatureProfile Temperature []   numLayer  the temperature on the atmosphere at each height.

    cloudMonitor Temperature  the temperature of the cloud monitor.

    numWVR int  the number of WVR channels.

    wvrTemp Temperature []   numWVR  the observed temperature in each WVR channel.

    water double  the water precipitable content.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "Weather"

    # the list of field names that make up key 'key'.
    _key = ["stationId", "timeInterval"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = False  # if True archive binary else archive XML
    _fileAsBin = False  # if True file binary else file XML

    # A list to store the WeatherRow instances
    _privateRows = []

    # context is a dictionary where each key is a string resulting
    # from a call to the method Key and the value is a list of rows
    # maintained in time-order
    _context = {}

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on pressure during an add operation on the table
    _pressureEqTolerance = Pressure(0.0)

    def setPressureEqTolerance(self, tolerance):
        """
        A setter for the tolerance on pressure
        """
        self._pressureEqTolerance = Pressure(tolerance)

    # A getter for the tolerance on pressure
    def getPressureEqTolerance(self):
        """
        A getter for the tolerance on pressure
        """
        return self._pressureEqTolerance

    # The tolerance which will be used on relHumidity during an add operation on the table
    _relHumidityEqTolerance = Humidity(0.0)

    def setRelHumidityEqTolerance(self, tolerance):
        """
        A setter for the tolerance on relHumidity
        """
        self._relHumidityEqTolerance = Humidity(tolerance)

    # A getter for the tolerance on relHumidity
    def getRelHumidityEqTolerance(self):
        """
        A getter for the tolerance on relHumidity
        """
        return self._relHumidityEqTolerance

    # The tolerance which will be used on temperature during an add operation on the table
    _temperatureEqTolerance = Temperature(0.0)

    def setTemperatureEqTolerance(self, tolerance):
        """
        A setter for the tolerance on temperature
        """
        self._temperatureEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on temperature
    def getTemperatureEqTolerance(self):
        """
        A getter for the tolerance on temperature
        """
        return self._temperatureEqTolerance

    # The tolerance which will be used on windDirection during an add operation on the table
    _windDirectionEqTolerance = Angle(0.0)

    def setWindDirectionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on windDirection
        """
        self._windDirectionEqTolerance = Angle(tolerance)

    # A getter for the tolerance on windDirection
    def getWindDirectionEqTolerance(self):
        """
        A getter for the tolerance on windDirection
        """
        return self._windDirectionEqTolerance

    # The tolerance which will be used on windSpeed during an add operation on the table
    _windSpeedEqTolerance = Speed(0.0)

    def setWindSpeedEqTolerance(self, tolerance):
        """
        A setter for the tolerance on windSpeed
        """
        self._windSpeedEqTolerance = Speed(tolerance)

    # A getter for the tolerance on windSpeed
    def getWindSpeedEqTolerance(self):
        """
        A getter for the tolerance on windSpeed
        """
        return self._windSpeedEqTolerance

    # The tolerance which will be used on windMax during an add operation on the table
    _windMaxEqTolerance = Speed(0.0)

    def setWindMaxEqTolerance(self, tolerance):
        """
        A setter for the tolerance on windMax
        """
        self._windMaxEqTolerance = Speed(tolerance)

    # A getter for the tolerance on windMax
    def getWindMaxEqTolerance(self):
        """
        A getter for the tolerance on windMax
        """
        return self._windMaxEqTolerance

    # The tolerance which will be used on dewPoint during an add operation on the table
    _dewPointEqTolerance = Temperature(0.0)

    def setDewPointEqTolerance(self, tolerance):
        """
        A setter for the tolerance on dewPoint
        """
        self._dewPointEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on dewPoint
    def getDewPointEqTolerance(self):
        """
        A getter for the tolerance on dewPoint
        """
        return self._dewPointEqTolerance

    # The tolerance which will be used on layerHeight during an add operation on the table
    _layerHeightEqTolerance = Length(0.0)

    def setLayerHeightEqTolerance(self, tolerance):
        """
        A setter for the tolerance on layerHeight
        """
        self._layerHeightEqTolerance = Length(tolerance)

    # A getter for the tolerance on layerHeight
    def getLayerHeightEqTolerance(self):
        """
        A getter for the tolerance on layerHeight
        """
        return self._layerHeightEqTolerance

    # The tolerance which will be used on temperatureProfile during an add operation on the table
    _temperatureProfileEqTolerance = Temperature(0.0)

    def setTemperatureProfileEqTolerance(self, tolerance):
        """
        A setter for the tolerance on temperatureProfile
        """
        self._temperatureProfileEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on temperatureProfile
    def getTemperatureProfileEqTolerance(self):
        """
        A getter for the tolerance on temperatureProfile
        """
        return self._temperatureProfileEqTolerance

    # The tolerance which will be used on cloudMonitor during an add operation on the table
    _cloudMonitorEqTolerance = Temperature(0.0)

    def setCloudMonitorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on cloudMonitor
        """
        self._cloudMonitorEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on cloudMonitor
    def getCloudMonitorEqTolerance(self):
        """
        A getter for the tolerance on cloudMonitor
        """
        return self._cloudMonitorEqTolerance

    # The tolerance which will be used on wvrTemp during an add operation on the table
    _wvrTempEqTolerance = Temperature(0.0)

    def setWvrTempEqTolerance(self, tolerance):
        """
        A setter for the tolerance on wvrTemp
        """
        self._wvrTempEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on wvrTemp
    def getWvrTempEqTolerance(self):
        """
        A getter for the tolerance on wvrTemp
        """
        return self._wvrTempEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    @staticmethod
    def Key(stationId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        The parameter values are assumed to be the appropriate type for that parameter.
        """
        result = ""

        result += stationId.toString() + "_"

        return result

    def insertByStartTime(self, x, rowlist):
        """
        Insert a WeatherRow in a list of WeatherRow so that it's ordered by ascending start time.

        x is a WeatherRow to be inserted.
        rowlist is the list where to x is to be inserted.

        The inserted row is returned.
        """
        insertionIndex = 0

        # get the ArrayTime at the start of the interval found in x.
        start = x.timeInterval.getStart()

        # is the rowlist None
        if rowlist is None:
            rowlist = []
        # is rowlist empty
        if len(rowlist) == 0:
            rowlist.append(x)
            self._privateRows.append(x)
            x.isAdded()
            return x

        # case where x goes at the end of rowlist
        # the last row in the list
        last = rowlist[-1]

        if start.get() > last.timeInterval.getStart().get():
            # Modify the duration of last if and only if the start time of x
            # is located strictly before the end time of last.

            if start.get() < (
                last.timeInterval.getStart().get()
                + last.timeInterval.getDuration().get()
            ):
                last.timeInterval.setDuration(
                    start.get() - last.timeInterval.getStart().get()
                )

            rowlist.append(x)
            self._privateRows.append(x)
            x.isAdded()
            return x

        # case where x goes at the beginning of rowlist
        # the first row in the list
        first = rowlist[0]

        if start.get() < first.timeInterval.getStart().get():
            # Modify the duration of x if and only if the start time of first
            # is located strictly before the end time of x.

            if first.timeInterval.getStart().get() < (
                start.get() + x.timeInterval.getDuration().get()
            ):
                x.timeInterval.setDuration(
                    first.timeInterval.getStart().get() - start.get()
                )
            x.timeInterval.setDuration(
                first.timeInterval.getStart().get() - start.get()
            )
            rowlist.insert(0, x)
            self._privateRows.add(x)
            x.isAdded()
            return x

        # Case where x has to be inserted inside rowlist
        # let's use a dichotomy method to find the insertion index.

        k0 = 0
        k1 = len(rowlist) - 1

        while k0 != (k1 - 1):
            if start.get() == rowlist[k0].timeInterval.getStart().get():
                if rowlist[k0].equalByRequiredValue(x):
                    # this row already exists at k0, nothing to insert or add, return that row
                    return rowlist[k0]
                else:
                    # the time matches, but the rest of the required parameters do not, duplicate keys
                    raise DuplicateKey("DuplicateKey exception in ", "WeatherTable")
            elif start.get() == rowlist[k1].timeInterval.getStart().get():
                if rowlist[k1].equalByRequiredValue(x):
                    # this row already exists at k1, nothing to insert or add, return that row
                    return rowlist[k1]
                else:
                    # the time matches, but the rest of the required parameters do not, duplicate keys
                    raise DuplicateKey("DuplicateKey exception in ", "WeatherTable")
            else:
                # make sure integers are used throughout this step
                if (
                    start.get()
                    <= rowlist[int((k0 + k1) / 2)].timeInterval.getStart().get()
                ):
                    k1 = int((k0 + k1) / 2)
                else:
                    k0 = int((k0 + k1) / 2)

        if start.get() == rowlist[k0].timeInterval.getStart().get():
            if row.get[k0].equalByRequiredValue(x):
                # this row already exists at k0, nothing to insert or add, return that row
                return rowlist[k0]
            else:
                # the time matches, but the rest of the required parameters do not, duplicate keys
                raise DuplicateKey("DuplicateKey exception in ", "WeatherTable")
        elif start.get() == rowlist[k1].timeInterval.getStart().get():
            if rowlist[k1].equalByRequiredValue(x):
                return rowlist[k1]
            else:
                # the time matches, but the rest of the required parameters do not, duplicate keys
                raise DuplicateKey("DuplicateKey exception in ", "WeatherTable")

        rowlist[k0].timeInterval.setDuration(
            start.get() - rowlist[k0].timeInterval.getStart().get()
        )
        x.timeInterval.setDuration(
            rowlist[k0 + 1].timeInterval.getStart().get() - start.get()
        )
        row.insertElementAt(k1, x)
        self._privateRows.add(x)
        x.isAdded()
        return x

    def __init__(self, container):
        """
        Create a WeatherTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("WeatherTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("WeatherTable")
        self._entity.setEntityVersion("1")
        self._entity.setInstanceVersion("1")

        # the default table has no rows and so is presentInMemory
        self._presentInMemory = True
        self._loadInProgress = False

    def setNotPresentInMemory(self):
        """
        Set the state to indicate it is not present in memory and needs to be loaded before being used.
        This is used by the container class when loaded from a file and this table is present with non-zero rows.
        Tables are loaded on demand when the get function in the container for that table is used.
        """
        self._presentInMemory = False

    def checkPresenceInMemory(self):
        """
        Check if the table is present in memory. If not, load the table from the file using the
        directory of the container.
        """
        # NOTE: if setFromFile throws an exception then presentInMemory will remain False
        # and loadInProgress will remain True, preventing another attempt at loading.
        # more complex solutions are then necessary to read that file and it's not worth
        # complicating this code here to handle a need to eventually try again to reload that file
        if not self._presentInMemory and not self._loadInProgress:
            self._loadInProgress = True
            self.setFromFile(self.getContainer().getDirectory())
            self._presentInMemory = True
            self._loadInProgress = False

    def getContainer(self):
        """
        Return the container to which this table belongs.
        """
        return self._container

    def size(self):
        """
        Return the number of rows in the table.
        """
        return len(self._privateRows)

    def getName(self):
        """
        Return the name of this table.
        """
        return self._tableName

    def toString(self):
        """
        Returns "WeatherTable" followed by the current size of the table
        between parenthesis.
        Example : WeatherTable(12)
        """
        return "WeatherTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = WeatherRow(self)
        return thisRow

    def add(self, row):
        """
        Add a row.
        row the WeatherRow to be added.

        return a WeatherRow. If the table contains a WeatherRow whose attributes (key and mandatory values) are equal to those in row
        then this returns that previously added WeatherRow, otherwise row is returned.

        raises DuplicateKey when the table contains a WeatherRow with a key equal to the key in row but having
        a value section different from the values in x.

        note: The row is inserted in the table in such a way that all the rows having the same value of
        ( stationId ) are stored by ascending time.
        """

        # get the key for row
        k = self.Key(row.getStationId())

        if k not in self._context:
            # add a list to context for this key for this
            self._context[k] = []

        result = None
        try:
            result = self.insertByStartTime(x, self._context[k])
        except DuplicateKey as exc:
            raise  # this will simply reraise that exception

        return result

    def newRow(self, stationId, timeInterval):
        """
        Create a new WeatherRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = WeatherRow(self)

        thisRow.setStationId(stationId)

        thisRow.setTimeInterval(timeInterval)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new WeatherRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new WeatherRow with default values for its attributes.
        """

        return WeatherRow(self, row)

    # ====> Append a row to its table.

    def _checkAndAdd(self, newrow):
        """
        A method to append a row to its table, used by input conversion
        methods. Not intended for external use.
        Returns the added row.
        """

        thisKey = self.Key(newrow.getStationId())

        if thisKey not in self._context:
            self._context[thisKey] = []

        return self.insertByStartTime(newrow, self._context[thisKey])

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as a list of WeatherRow
        """
        return self._privateRows

    def getByContext(self, stationId):
        """
        Return all the rows sorted by ascending startTime for a given context.
        The context is defined by the value of ( stationId ).
        A None value is returned if the table contains no rows for the given
        ( stationId ).
        """
        thisKey = WeatherTable.Key(stationId)

        result = None
        if thisKey in self._context:
            result = self._context(thisKey)

        return result

    def getRowByKey(self, stationId, timeInterval):
        """
        Returns a WeatherRow given a key.
        return the row having the key whose values are passed as parameters, or None
        if no row exists for that key.
        """

        keystr = self.Key(stationId)

        if keystr not in context:
            return None

        contextRows = context[keystr]
        # Is the context list empty...impossible in principle !
        if len(contextRows) == 0:
            return None

        # only one element in the context list
        if len(contextRows) == 1:
            r = contextRows[0]
            if r.getTimeInterval().contains(timeInterval.getStart()):
                return r
            return None

        # Optimizations
        last = contextRows[-1]
        if timeInterval.getStart().get() >= (
            last.getTimeInterval().getStart().get()
            + last.getTimeInterval().getDuration().get()
        ):
            # the key is past the end of contextRows
            return None

        first = contextRows[0]
        if timeInterval.getStart().get() < first.getTimeInterval().getStart().get():
            # the key is before the start of contextRows
            return None

        # the key falls in the range of context and there's more than one row, find the row, if it exists in context
        # let's use dichotomy method
        k0 = 0
        k1 = len(contextRows) - 1
        while k0 != k1:
            # Is the start time contained in the time interval of row at k0
            r = contextRows[k0]
            if r.getTimeInterval().contains(timeInterval.getStart()):
                return r

            # Is the start time contained in the time interval of row at k1
            r = contextRows[k1]
            if r.getTimeInterval().contains(timeInterval.getStart()):
                return r

            # Are the rows at k0 and at k1 consecutive
            # Then we know for sure that there is no row containing the start of timeInterval.
            if k1 == (k0 + 1):
                return None

            # make sure indexing here is always done with integer and k0 and k1 remain integers
            r = contextRows[int((k0 + k1) / 2)]
            if timeInterval.getStart().get() <= r.getTimeInterval().getStart().get():
                k1 = int((k0 + k1) / 2)
            else:
                k0 = int((k0 + k1) / 2)

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for Weather (WeatherTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<WeatherTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:weathr="http://Alma/XASDM/WeatherTable" xsi:schemaLocation="http://Alma/XASDM/WeatherTable http://almaobservatory.org/XML/XASDM/4/WeatherTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</WeatherTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a Weather (WeatherTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of WeatherTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "WeatherTable":
            raise ConversionException(
                "XML is not from a the expected table", "WeatherTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException("schemaVersion not found in XML", "WeatherTable")
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "WeatherTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "WeatherTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "WeatherTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "WeatherTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "WeatherTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "WeatherTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "WeatherTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "WeatherTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "WeatherTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a WeatherTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "WeatherTable",
            )

        if os.path.exists(os.path.join(directory, "Weather.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "Weather.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the Weather table", "WeatherTable"
            )

    def setFromMIMEFile(self, directory):
        print("setFromMIMEFile not implemented yet")

    def setFromXMLFile(self, directory):
        """
        This is the function used by setFromFile when the file is an XML file
        """

        # setFromFile has already established that this exists
        # read the entire file into a string
        xmlstr = None
        with open(os.path.join(directory, "Weather.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("Weather.xml is empty", "WeatherTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'Weather.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'Weather.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (Weather)"
                % directory,
                "WeatherTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for Weather")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "Weather.xml")
            if os.path.exists(filePath):
                # try to delete it, this will raise an exception if the user does not have permission to do that
                os.remove(filePath)
            with open(filePath, "w") as f:
                f.write(self.toXML())
                f.close()

    def getEntity(self):
        """
        Returns the table's entity.
        """
        return self._entity

    def setEntity(self, e):
        """
        Set the table's entity
        The parameter, e, must be an Entity
        """
        if not isinstance(e, Entity):
            raise (ValueError("setEntity must use an Entity value"))

        self._entity = Entity(e)

    def getVersion(self):
        return self._version

    def setVersion(self, version):
        if not isinstance(version, int):
            raise ValueError("version must be an int")

        self._version = version
