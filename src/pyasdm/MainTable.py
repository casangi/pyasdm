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
# File MainTable.py

# this will eventually be generated code

import pyasdm.ASDM

from .MainRow import MainRow
from .Representable import Representable
from .types.Entity import Entity
from .types.EntityId import EntityId

# using minidom instead of Parser
from xml.dom import minidom

import os

class MainTable(Representable):
    """
    The MainTable class is an ASDM table.

    Eventually this description will also have generated text describing the contents of this table.
    """

    # this is True if the file is considered present in memory (nothing to be loaded)
    # the default state is True, ASDM will set this to False when it's loaded and this table has non-zero rows
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table
    _tableName = "Main"
    
    # the list of field names that make up the key
    _key = ["time","configDescriptionId","fieldId"]

    # the ASDM container that this table belongs to (set by constructor
    _container = None

    _fileAsBin = False  # if true file binary else file XML
    # _archiveAsBin not used by python implementation

    # the thing to hold the list of MainRow instances goes here
    # for not, just a list
    _privateRows = []

    # context is a dictionary of lists of rows where the keys are the
    # the keys for this table, returned by the key() member function
    # for a given row, the lists of rows should be maintained sorted in time-order
    _context = {}

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0
    

    # list of attributes (field in each row)
    attributesNames = ["time",
                       "configDescriptionId",
                       "fieldId",
                       "numAntenna",
                       "timeSampling",
                       "interval",
                       "numIntegration",
                       "scanNumber",
                       "subscanNumber",
                       "dataSize",
                       "dataUID",
                       "stateId",
                       "execBlockId"]

    attributesTypes = ["ArrayTime",
                       "Tag",
                       "Tag",
                       "int",
                       "TimeSampling",
                       "Interval",
                       "int",
                       "int",
                       "int",
                       "long",
                       "EntityRef",
                       "Tag[]",
                       "Tag"]

    keyAttributesNames = ["time",
                          "configDescriptionId",
                          "fieldId"]

    requiredValueAttributesNames = ["numAntenna",
                                    "timeSampling",
                                    "interval",
                                    "numIntegration",
                                    "scanNumber",
                                    "subscanNumber",
                                    "dataSize",
                                    "dataUID",
                                    "stateId",
                                    "execBlockId"]

    optionalValueAttributesNames = []
    
    def getKeyName(self):
        """
        Return the list of field names that make up the key as a list of strings
        """
        return (self._key)

    @staticmethod
    def Key(configurationDescriptionId, fieldId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with an "_" character.
        Both parameters are Tag instances.
        """
        result = configurationDescriptionId.toString() + "_" + fieldId.toString() + "_";
        return(result)

    def insertByTime(self, thisRow, rows):
        """
        Insert a MainRow in a vector of MainRow so that it's ordered by ascending time.
        thisRow is the row to be inserted, returns thisRow
        rows is the list of rows where thisRow should be inserted
        """

        # rows should be a member of self returned by some other method. So long as this
        # uses list methods to insert elements into rows it should appropriately update
        # that list in self

        thisRowTime = thisRow.getTime().get()
        
        # is rows empty or are rows are being added already sorted in ascending time
        if len(rows) == 0 or (thisRowTime > rows[-1].getTime().get()):
            # just append it, and mark it as added
            rows.append(thisRow)
            self._privateRows.append(thisRow)
            thisRow.isAdded()
            return thisRow

        # does this belong at the head of rows
        if thisRowTime < rows[0].getTime().get():
            rows.insert(0,thisRow)
            self._privateRows.append(thisRow)
            thisRow.isAdded()
            return thisRow

        # need to find where to insert thisRow in rows
        # use a dichotomy method to find the insertion index
        k0 = 0
        k1 = len(rows)-1
        while (k0 != (k1 - 1)):
            if (thisRowTime == rows[k0].getTime().get()):
                if rows[k0].equalByRequiredValue(thisRow):
                    # this row is already inserted, do not insert it again
                    return (row[k0])
                else:
                    # this is a duplicate row with different required values, it can not be added
                    raise ValueError("DuplicateKey exception in MainTable")
            elif (thisRowTime == rows[k1].getTime().get()):
                if rows[k1].equalByRequiredValue(thisRow):
                    # this row is already inserted, do not insert it again
                    return (row[k1])
                else:
                    # this is a duplicate row with different required values, it can not be added
                    raise ValueError("DuplicateKey exception in MainTable")
            else:
                if (thisRowTime <= rows[int((k0+k1)/2)].getTime().get()):
                    k1 = int(K0+k1) / 2
                else:
                    k0 = int(k0+k1) / 2
        # it's either k0 or k1 or it goes at k1 (after k0)
        if (thisRowTime == rows[k0].getTime().get()):
            if rows[k0].equalByRequiredValue(thisRow):
                # this row is already inserted, do not insert it again
                return (row[k0])
            else:
                # this is a duplicate row with different required values, it can not be added
                raise ValueError("DuplicateKey exception in MainTable")
        elif (thisRowTime == rows[k1].getTime().get()):
            if rows[k1].equalByRequiredValue(thisRow):
                # this row is already inserted, do not insert it again
                return (row[k1])
            else:
                # this is a duplicate row with different required values, it can not be added
                raise ValueError("DuplicateKey exception in MainTable")
        # it goes at k1
        rows.insert(k1,thisRow)
        self._privateRows.append(thisRow)
        thisRow.isAdded()
        return thisRow
                

    def getAttributesNames(self):
        return (self.attributesNames)

    def getAttributesType(self):
        return (self.attributesTypes)

    def inKey(self, s):
        return (s in self.keyAttributesNames)

    def __init__(self, container):
        """
        Create a MainTable attached to container, which must be an ASDM instance
        """
        if not isinstance(container, pyasdm.ASDM):
            raise(ValueError("MainTable constructor must use an ASDM instance"))

        self._container = container
        entity = Entity()
        entity.setEntityId(EntityId("uid://X0/X0/X0"))
        entity.setEntityIdEncrypted("na")
        entity.setEntityTypeName("MainTable")
        entity.setEntityVersion("1")
        entity.setInstanceVersion("1")
        self._entity = entity

        # The default MainTable has no rows and so is presentInMemory
        self._presentInMemory = True
        self._loadInProgress = False

    def setNotPresentInMemory(self):
        """
        Set the state to indicate it is not present in memory and needs to be loaded before being used
        This is used by the ASDM class when loaded from a file and this table is present with non-zero rows.
        Tables are loaded on demand when the get function in the ASDM for that table is used.
        """
        self._presentInMemory = False

    def checkPresenceInMemory(self):
        """
        Check if the table is present in memory. If not, load the table from file using the
        directory of the container.
        """
        # NOTE: if setFromFile throws an exception that presentInMemory will remain False
        # and loadInProgress will remain True, preventing another attempt at loading.
        # more complex solutions are then nececssary to read that file and it's not worth
        # complicating this code here to handle a need to eventually try again to reload that file
        if (not self._presentInMemory and not self._loadInProgress):
            self._loadInProgress = True
            self.setFromFile(self.getContainer().getDirectory())
            self._presentInMemory = True
            self._loadInProgress = False

    def getContainer(self):
        """
        Return the container to which this table belongs
        """
        return (self._container)

    def size(self):
        """
        The number of rows in the table
        """
        return (len(self._privateRows))
        
    def getName(self):
        """
        The name of this table
        """
        return (self._tableName)

    def toString(self):
        """
        Returns 'MainTable' followed by the current size of the table
        between parenthesis.
        Example : SpectralWindowTable(12)
        """
        return ("MainTable("+size()+")")

    def add(self, row):
        """
        Add a row to this table. 'row' is the MainRow to be added
        If this table conains a MainRow whose attributes (key and mandatory values) are equal to those in row
        then this returns that MainRow, otherwise 'row' is returned.
        If this table contains a MainRow with a key equal to that of 'row'
        but having a value section different from 'row' then an exception is thrown.
        The row is inserted in table in such a way that all rows having the same
        value of (configurationId, fieldId) are stored by ascending time.
        """
        # in the Java implementation this appears to be identical to checkAndAdd, although
        # it does capture the DuplicateKey exception by insertByTime here, but it just rethrows it,
        # so lets use that here
        return self._checkAndAdd(row)

    def newRow(self,  time=None, configDescriptionId=None, fieldId=None,
               numAntenna=None, timeSampling=None, interval=None,
               numIntegration=None, scanNumber=None, subscanNumber=None,
               dataSize=None, dataUID=None, stateId=None, execBlockId=None):
        """
        Create a new MainRow. The new row is not added to this table, but it does know about table.
        If time is None it assumes all of the other arguments are None and it returns
        the default MainRow (values must be set later).
        Alternatively, the full set of values must be given to full set the MainRow values (values are not check to see if they are valid)
        (the autoincrementable attribute if any is not in the parameter list)
        """

        thisRow = None
        thisRow = MainRow(self)
        if time is not None:
            thisRow.setTime(time)
            thisRow.setConfigDescriptionId(configDescriptionId)
            thisRow.setFieldId(fieldId)
            thisRow.setNumAntenna(numAntenna)
            thisRow.setTimeSampling(timeSampling)
            thisRow.setInterval(interval)
            thisRow.setNumIntegration(numIntegration)
            thisRow.setScanNumber(scanNumber)
            thisRow.setSubscanNumber(subscanNumber)
            thisRow.setDataSize(dataSize)
            thisRow.setDataUID(dataUID)
            thisRow.setStateId(stateId)
            thisRow.setExecblockId(execBlockId)

        return thisRow

    def _checkAndAdd(self,row):
        """
        Append a row to it's table, used by the input conversion methods. Not indented for external use."
        """
        rowKey = MainTable.Key(
            row.getConfigDescriptionId(),
            row.getFieldId()
            )

        if rowKey not in self._context:
            self._context[rowKey] = []
            
        self.insertByTime(row, self._context[rowKey])
        
    # methods returning rows
    def get(self):
        """
        get all rows as a list of MainRows
        """
        return (self._privateRows)

    def getByContext(self, configDescriptionId, fieldId):
        """
        Return all of the rows sorted by ascending startTime for a given context.
        The context is defined by the the two Tag instances give as parameters
        A None value is returned if the table containsno rows for the given
        (configDescriptionId, fieldId).
        configDescription and fieldId are Tag types
        """
        thisKey = MainTable.Key(configDescriptionId, fieldId)
        result = None
        if thisKey in self._context:
            result = self._context(thisKey)

        return result
        
    def getRowByKey(self, time, configDescriptionId, fieldId):
        """
        return the row having the key whose values are passed as parameters, or
        None if no row exists for that key
        time is an ArrayTime, configDescriptionId and fieldId are Tag type
        """
        rowKey  = MainTable.Key(configDescriptionId, fieldId)
        result = None
        if rowKey in self._context:
            rows = self._context[rowKey]
            if len(rows) == 1:
                # single row
                if time.get() == rows[0].getTime().get():
                    result = rows[0]
                # otherwise the time don't match, returning None
            elif len(rows) > 1:
                if time.get() >= rows[0].getTime().get() and time.get() <= rows[-1].getTime().get():
                    # the time falls within the available range
                    # more than one row
                    # use a dichotomy method for the general case
                    k0 = 0
                    k1 = len(rows)-1
                    while(k0!=k1 and result is None):
                        thisRow = rows[k0]
                        if (thisRow.getTime().get() == time.get()):
                            result = thisRow
                        else:
                            thisRow = rows[k1]
                            if (thisRow.getTime().get() == time.get()):
                                result = thisRow
                            else:
                                thisRow = rows[int((k0+k1)/2)]
                                if (time.get() <= thisRow.getTime().get()):
                                    k1 = int(k0+k1)/2
                                else:
                                    k0 = int(k0+k1)/2
        return result

    def getRows(self):
        # in the typed langauges this exists so that colletions of rows can be returned
        # as a single type for generic row access. That's not necessary here and
        # this method is identical to get
        return self.get()

    # conversionmethods
    def toFITS(self):
        """
        Not implemented for Main
        """
        return None

    def fromFITS(self, fits):
        """
        Not implemented for Main
        """
        return None

    def toXML(self):
        """
        Translate this table to an XML representation conform
        to the schema defined or Main (MainTable.xsd).
        Return a string containing the XML representation.
        """
        result = ""
        result += "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?> "
        result += "<MainTable xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:main=\"http://Alma/XASDM/MainTable\" xsi:schemaLocation=\"http://Alma/XASDM/MainTable http://almaobservatory.org/XML/XASDM/4/MainTable.xsd\" schemaVersion=\"4\" schemaRevision=\"-1\">\n"
        result += self._entity.toXML()
        s = self._container.getEntity().toXML();
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</MainTable>"
        return(result)

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of an XML document that is
        required to conform to the XML schema defined for a Main (MainTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of MainTable
        if (not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "MainTable"):
            raise ValueError("XML is not from a Main table")
        
        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute,which must be there
        if (not tabdom.hasAttributes()) or (tabdom.attributes.getNamedItem('schemaVersion') is None):
            raise ValueError("schemaVersion for Main table not found in XML")
        versionStr = tabdom.attributes.getNamedItem('schemaVersion').value
        # raises a ValueError if not an integer
        self.setVersion(int(versionStr))

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ValueError("Main table XML is missing all of the expected elements")

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ValueError("More than one Entity found for Main table XML")
                tabEntity = Entity(thisNode.toxml())
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ValueError("More than one ContainerEntity found for Main table XML")
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRow()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except ValueError as exc:
                    msg = "DuplicateKey in row in MainTable : %s" % str(exc)
                    raise ValueError(msg) from None
                
        if tabEntity is None:
            raise ValueError("No Entity seen for Main table in XML")
        if not hasContainerEntity:
            raise ValueError("No ContainerEntity seen for Main table in XML")

        self.setEntity(tabEntity)
                
    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a Maintable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed
        """
        
        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ValueError("directory must be a path to an existing directory")

        if os.path.exists(directory+"/Main.xml"):
            self.setFromXMLFile(directory)
        elif os.path.exists(directory+"/Main.bin"):
            self.setFromMIMEFile(directory)
        else:
            raise ValueError("No file found for the Main table")

    def setFromMIMEFile(self, directory):
        """
        This is the function used by setFromFile with the file is a bin file
        """
        
        print("setFromMIMEFile not implemented yet for Main table")

    def setFromXMLFile(self, directory):
        """
        This is the function used by setFromFile when the file is an XML file
        """
        
        # setFromFile has already established that this exists
        # read the entire file into a string
        xmlstr = None
        with open(directory+"/Main.xml") as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ValueError("Main.xml is empty")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.
        
        Depending on the boolean value of _fileAsBin a binary serialization of this (fileAsBin=True)
        will be saved in a file "Main.bin" or an XML representation (fileAsBin==False) will be saved
        in a file "Main.xml".
        The file is always written in a directory whose name is passed as a parameter.
        """

        # check if directory exists
        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ValueError("Cannot write into directory %s. This file already exists and is not a directory. (MainTable)" % directory)

        if not os.path.exists(directory):
            # don't catch FileNotFoundHere - assume it can be created there
            os.mkdir(directory)

        if (self._fileAsBin):
            print("fileAsBin not yet implemented for Main")
        else:
            # exported as an XML file
            filePath = os.path.join(directory,'Main.xml')
            if os.path.exists(filePath):
                # try and delete it
                # do not catch any exceptions here
                os.remove(filePath)
            with open(filePath, 'w') as f:
                f.write(self.toXML())
                f.close()

    def getEntity(self):
        """
        Return the table's entity
        """
        return self._entity

    def setEntity(self, e):
        """
        Set the table's entity
        """
        if not isinstance(e, Entity):
            raise(ValueError("setEntity must use an Entity value"))

        self._entity = e

    def getVersion(self):
        return self._version

    def setVersion(self, version):
        if not isinstance(version, int):
            raise ValueError("version must be an int")

        self._version = version


    
