# ALMA - Atacama Large Millimeter Array
# (c) European Southern Observatory, 2024
# (c) Associated Universities Inc., 2024
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
# File ASDM.py

# this will eventually be generated code

from pyasdm.types.ArrayTime import ArrayTime
from pyasdm.types.Entity import Entity
from pyasdm.types.EntityId import EntityId

# using minidom instead of Parser
from xml.dom import minidom

# will need to import each table type here
from pyasdm.MainTable import MainTable

import time
import os


class ASDM:
    """
    The ASDM class is the container for all tables. Its instantiation
    creates a complete set of tales.

    This will eventually be generated code
    """

    # data members
    # _archiveAsBin not used by the pyasdm code, omitted here
    _fileAsBin = False  # if True file binary else file XML
    # _hasBeenAdded = False         # to be compatible with the tables generated code, deferred
    _entity = Entity()  # this tables entity
    _timeOfCreation = ArrayTime()  # the creation time for this ASDM
    # _xmlnsPrefix = ""             # the XMLNS prefix for this ASDM, not used in Java, defer until needed
    _version = 0  # the version integer

    # the directory appropriate for this ASDM, set by setFromFile
    _directory = None

    # c++ has an origin value, not java, defer : FILE, ARCHIVE, EX_NIHILO
    # c++ has loadTablesOnDemand and checkRowUniqueness, neither in java - defer
    # c++ has directory with a getter, java does not - defer

    # dictionary of the Entity objects for each table found when the ASDM is populated
    # tables are loaded on demand when the table is retrieved via it's getter IF that table
    # has an entry in this dictionary, otherwise the detault (empty) Table is returned
    _tableEntity = {}

    # each table will appear here as a data member
    _main = None

    # defer on getTables() until necessary, would return a list or array of all of the tables

    # default constructor makes an empty ASDM

    def __init__(self):
        # most values initialized in the code above
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("ASDM")
        self._entity.setEntityVersion("1")
        self._entity.setInstanceVersion("1")

        # define a default creation time - now
        gmnow = time.gmtime()
        self._timeOfCreation.init(
            gmnow.tm_year,
            gmnow.tm_mon,
            gmnow.tm_mday,
            gmnow.tm_hour,
            gmnow.tm_min,
            gmnow.tm_sec,
        )

        self._main = MainTable(self)

    # getters and setters
    def getMain(self):
        """
        get the MainTable
        """
        self._main.checkPresenceInMemory()
        return self._main

    def getEntity(self):
        return self._entity

    def setEntity(self, e):
        if not isinstance(e, Entity):
            raise ValueError("invalid argument to setEntity, must be an Entity")
        self._entity = e

    def getDirectory(self):
        """
        The directory name is setFromFile was used, else None.
        """
        return self._directory

    def getName(self):
        """
        Meaningless, but required to make this the same interface as tables
        """
        return ()

    def size(self):
        """
        Meaningless, but required to make this the same interface as tables
        """
        return 0

    def getTable(self, tableName):
        """
        Return the named table
        """
        if not isinstance(tableName, str):
            raise ValueError("tableName must be a string")

        raise ValueError("No such table as " + tableName)

    def getTimeOfCreation(self):
        """
        Return the timeOfCreation as an ArrayTime
        """
        return self._timeOfCreation

    def setTimeOfCreation(self, timeOfCreation):
        """
        Set the time of creation. The argument must be an ArrayTime
        """
        if not isinstance(timeOfCreation, ArrayTime):
            raise ValueError("timeOFCreation must be an ArrayTime")

        self._timeOfCreation = timeOfCreation

    def getVersion(self):
        return self._version

    def setVersion(self, version):
        if not isinstance(version, int):
            raise ValueError("version must be an int")

        self._version = version

    def getXmlnsPrefix(self):
        return self._xmlnsPrefix

    def setXmlnsPrefix(self, xmlnsPrefix):
        if not isinstance(xmlnsPrefix, str):
            raise ValueError("xmlnsPrefix must be a str")

        self._xmlnsPrefix = xmlnsPrefix

    def toXML(self):
        """
        Produces the XML representation of this.
        Returns a string.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<ASDM xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:cntnr="http://Alma/XASDM/ASDM" xsi:schemaLocation="http://Alma/XASDM/ASDM http://almaobservatory.org/XML/XASDM/4/ASDM.xsd" schemaVersion="4" schemaRevision="-1"> '
        if self._entity.isNull():
            raise ValueError("Container entity cannot be null. (Container)")
        result += self._entity.toXML()
        result += " "
        result += "<TimeOfCreation> "
        result += self._timeOfCreation.toFITS()
        result += " "
        result += "</TimeOfCreation>"
        # this ultimately needs a list of tables, just do Main now
        result += "<Table> "
        result += "<Name> "
        result += self._main.getName()
        result += " "
        result += "</Name> "
        result += "<NumberRows> "
        result += str(self._main.size())
        result += " "
        result += "</NumberRows> "
        if self._main.size() > 0:
            if self._main.getEntity().isNull():
                raise ValueError("Table entity is null. (Main)")
            result += self._main.getEntity().toXML()
        result += "</Table> "
        result += "</ASDM>"
        return result

    def setFromFile(self, directory):
        """
        Reads and parses a collection of files as those produced by the toFile method.
        This dataset is populated with the result of the parsing.
        direactory is the name of the directory containing the files
        """
        # directory must exist as a directory.
        if not os.path.isdir(directory):
            raise ValueError("directory must be a path to an existing directory")

        self._directory = directory
        if self._fileAsBin:
            raise ValueError("fileAsBin not implemented yet for ASDM")
        else:
            fileName = directory + "/ASDM.xml"
            # c++ uses ASDMUtils to find the origin and version if parse requests that, deferring
            # it then uses a transformer file to get the xmlDoc, handles earlier versions
            # skip that here and go right to xmlDoc
            # read the entire file into a string
            if not os.path.exists(fileName):
                raise ValueError("no ASDM.xml found in %s" % directory)

            xmlstr = None
            with open(fileName) as f:
                xmlstr = f.read()

            if xmlstr is None:
                raise ValueError("ASDM.xml is empty")

            self.fromXML(xmlstr)

        # mark the tables found in the file with a non-zero size as not present in memory so they can be loaded on demain
        if "Main" in self._tableEntity:
            self._main.setNotPresentInMemory()

    def fromXML(self, xmlstr):
        """
        Parse the XML representation of an ASDM stored in a string and fills this object
        data values as appropriate.
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have a single child with a name of ASDM
        # ignore everything but the first child
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "ASDM":
            raise ValueError("XML is not from an ASDM file")
        asdmdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not asdmdom.hasAttributes()) or (
            asdmdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ValueError("schemaVersion for ASDM not found in XML")
        versionStr = asdmdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        self.setVersion(int(versionStr))

        # go though the child nodes of asdmdom, either Entity, TimeOfCreation or Table
        # only Table should appear more than once
        asdmEntity = None
        asdmToC = None

        # todo : startTimeDurationInXML and startTimeDurationInBin  - no examples found
        #  <startTimeDurationInXML someAttribute="1"> I think it's just the presence of this element
        # these become True (default is False) and need to be available for other uses

        if not asdmdom.hasChildNodes():
            raise ValueError("ASDM XML is missing all of the expected elements")

        for thisNode in asdmdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if asdmEntity is not None:
                    raise ValueError("More than one Entity found for ASDM XML")
                asdmEntity = Entity(thisNode.toxml())
            elif nodeName == "TimeOfCreation":
                if asdmToC is not None:
                    raise ValueError("More than one TimeOfCreation found for ASDM XML")
                asdmToC = ArrayTime(thisNode.firstChild.data)
            elif nodeName == "startTimeDurationInXML":
                print("startTimeDurationInXML seen")
            elif nodeName == "startTimeDurationInBin":
                print("startTimeDurationInBin seen")
            elif nodeName == "Table":
                # each table must have one of Name, NumberRows, and Entity
                # allow for a missing Entity if NumberRows is 0
                tabName = None
                tabSize = None
                tabEntity = None

                for thisTabNode in thisNode.childNodes:
                    tabNodeName = thisTabNode.nodeName
                    if tabNodeName == "Name":
                        if tabName is not None:
                            raise ValueError(
                                "More than one Name seen for the same Table in ASDM XML"
                            )
                        tabName = thisTabNode.firstChild.data
                    elif tabNodeName == "NumberRows":
                        if tabSize is not None:
                            raise ValueError(
                                "More than one NumberOfRows seen for the same Table in ASDM XML"
                            )
                        tabSize = int(thisTabNode.firstChild.data)
                    elif tabNodeName == "Entity":
                        if tabEntity is not None:
                            raise ValueError(
                                "More than one Entity seen for the same Table in ASDM XML"
                            )
                        tabEntity = Entity(thisTabNode.toxml())

                # name and size must be there
                if tabName is None or tabSize is None:
                    raise ValueError(
                        "A table in ASDM xml is not named or the number of rows is not given"
                    )
                if tabSize > 0:
                    if tabEntity is None:
                        raise ValueError(
                            "No Entity given for %s table of size %s"
                            % (tabName, tabSize)
                        )
                    self._tableEntity[tabName] = tabEntity

        if asdmEntity is None:
            raise ("No Entity seen for ASDM element in ASDM XML")
        if asdmToC is None:
            raise ("No TimeOfCreation seen in ASDM XML")

        self.setEntity(asdmEntity)
        self.setTimeOfCreation(asdmToC)

    def toFile(self, directory):
        """
        Write this ASDM dataset to the specified directory as a collection of files.

        The container itself is written into an XML file. Each table of the conainer
        having at least one row is written into a binary or an XML file depending on
        the value of its "fileAsBin" field.

        This method will not overwrite an existing file
        """
        # check if directory exists
        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ValueError(
                "Cannot write into directory %s. This file already exists and is not a directory (ASDM)"
                % directory
            )

        if not os.path.exists(directory):
            # don't catch any exceptions here, assume it can be found
            os.mkdir(directory)

        fileName = None
        if self._fileAsBin:
            # this should never happen for ASDM
            fileName = os.path.join(directory, "ASDM.bin")
        else:
            fileName = os.path.join(directory, "ASDM.xml")

        with open(fileName, "w") as f:
            if self._fileAsBin:
                # this should never happen, Java just passes here without any code
                pass
            else:
                f.write(self.toXML())
                f.close()

        # then send each of its table to its own file
        if self.getMain().size() > 0:
            self.getMain().toFile(directory)
