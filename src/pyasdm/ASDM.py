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

from pyasdm.Parser import Parser

# will need to import each table type here
# from pysdm.MainTable import MainTable

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
    _fileAsBin = False            # if True file binary else file XML
    # _hasBeenAdded = False         # to be compatible with the tables generated code, deferred
    _entity = Entity()            # this tables entity
    _timeOfCreation = ArrayTime() # the creation time for this ASDM
    # _xmlnsPrefix = ""             # the XMLNS prefix for this ASDM, not used in Java, defer until needed
    _version = 0                  # the version integer

    # c++ has an origin value, not java, defer : FILE, ARCHIVE, EX_NIHILO
    # c++ has loadTablesOnDemand and checkRowUniqueness, neither in java - defer
    # c++ has directory with a getter, java does not - defer
    
    # each table will appear here as a data member
    # _main = MainTable()

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
        self._timeOfCreation.init(gmnow.tm_year, gmnow.tm_mon, gmnow.tm_mday, gmnow.tm_hour, gmnow.tm_min, gmnow.tm_sec)

    # getters and setters
    def getMain(self):
        """
        get the MainTable
        """
        print("Not implemented yet")
        return (None)

    def getEntity(self):
        return(self._entity)

    def setEntity(self, e):
        if not isinstance(e, Entity):
            raise ValueError("invalid argument to setEntity, must be an Entity")
        self._entity = e

    def getName(self):
        """
        Meaningless, but required to make this the same interface as tables
        """
        return()

    def size(self):
        """
        Meaningless, but required to make this the same interface as tables
        """
        return(0)

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
        return(self._xmlnsPrefix)

    def setXmlnsPrefix(self, xmlnsPrefix):
        if not isinstance(xmlnsPrefix, str):
            raise ValueError("xmlnsPrefix must be a str")

        self._xmlnsPrefix = xmlnsPrefix

    def setFromFile(self, directory):
        """
        Reads and parses a collection of files as those produced by the toFile method.
        This dataset is populated with the result of the parsing.
        direactory is the name of the directory containing the files
        """
        # directory must exist as a directory.
        if not os.path.isdir(directory):
            raise ValueError("directory must be a path to an existing directory")

        if self._fileAsBin:
            raise ValueError("fileAsBin not implemented yet for ASDM")
        else :
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

    def fromXML(self, xmlstr):
        """
        Parse the XML representation of an ASDM stored in a string and fills this object
        data values as appropriate. 
        """
        xmlParser = Parser(xmlstr)
        if not xmlParser.isStr("<ASDM"):
            raise ValueError("'<ASDM' not found in XML")

        # find schemaVersion="..." in xmlstr
        startSchema = xmlstr.find("schemaVersion")
        if startSchema < 0:
            raise ValueError("schemaVersion not found in XML")
        nextEquals = xmlstr.find("=",startSchema+1)
        if nextEquals < 0:
            raise ValueError("correctly formatted schemaVersion not found in XML")
        firstQuote = xmlstr.find('"',nextEquals+1)
        if firstQuote < 0:
            raise ValueError("correctly formatted schemaVersion not found in XML")
        lastQuote = xmlstr.find('"',firstQuote+1)
        if lastQuote < 0:
            raise ValueError("correctly formatted schemaVersion not found in XML")
        schemaVersion = xmlstr[(firstQuote+1):lastQuote]
        print("schemaVersion = %s" % schemaVersion)
        self.setVersion(int(schemaVersion))

        s = xmlParser.getElement("<Entity",">")
        if s is None:
            raise ValueError("'<Entity ... >' not found in XML")
        e = Entity()
        e.setFromXML(s)
        if not e.getEntityTypeName() == "ASDM":
            raise ValueError("First Entity found in XML is not ASDM as expected")
        self.setEntity(e)

        s = xmlParser.getElementContent("<TimeOfCreation>","</TimeOfCreation>")
        if s is None:
            raise ValueError("TimeOfCreation element not found in XML")
        tofc = ArrayTime(s)
        self.setTimeOfCreation(tofc)

        # Do we have an element startTimeDurationInXML
        s = xmlParser.getElement("<startTimeDurationInXML",">")
        if s is not None:
            print("has startTImeDurationInXML : %s" % s)

        # Do we have an element startTimeDurationInBin
        s = xmlParser.getElement("<startTimeDurationInBin",">")
        if s is not None:
            print("has startTimeDurationInBin : %s" % s)

        # get each table in the dataset
        s = xmlParser.getElementContent("<Table>","</Table>")
        tabParser = None
        tableName = None
        numberOfRows = 0
        while (s is not None):
            tabParser = Parser(s)
            s = tabParser.getElementContent("<Name>","</Name>")
            if s is None:
                raise ValueError("Name element missing from a table element in XML")
            tableName = s
            s = tabParser.getElementContent("<NumberRows>","</NumberRows>")
            if s is None:
                raise ValueError("NumberOfRows element not seen for table %s in XML" % tableName)
            # bad formatting here will raise a ValueError, java catches the equivalent and issues it's own error
            numberOfRows = int(s)
            if (numberOfRows > 0):
                s = tabParser.getElement("<Entity",">")
                if s is None:
                    raise ValueError("missing Entity element for table %s in XML" % tableName)
                print("%s Entity = %s" % (tableName, s))
                e = Entity(s)
                if (not e.getEntityTypeName() == (tableName + "Table")):
                    raise ValueError("Unexpected entity type name for table %s = %s in XML" % (e.getEntityTypeName(),tableName))
                print("Table Entity: %s = %s" % (tableName, e.toString()))
            s = xmlParser.getElementContent("<Table>","</Table>")
        if not xmlParser.isStr("</ASDM>"):
            raise ValueError("no trailing '</ASDM>' found in XML")
