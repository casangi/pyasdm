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
# File MainTable.py
#

import pyasdm.ASDM

from .MainRow import MainRow
from .Representable import Representable
from .types.Entity import Entity
from .types.EntityId import EntityId

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class MainTable(Representable):
    """
    The MainTable class is an Alma table.

     Role
      Contains links to all data subsets. Each data subset is contained in a separate entity, usually a BLOB.


     Generated from model's revision -1, branch

     Attributes of Main

                  Key

    time ArrayTime mid point of scheduled period.

    configDescriptionId Tag Configuration description identifier.

    fieldId Tag Field identifier.



                  Value (Mandatory)

    numAntenna int  Number of antennas.

    timeSampling TimeSampling  time sampling mode.

    interval Interval  data sampling interval.

    numIntegration int  number of integrations.

    scanNumber int  scan number.

    subscanNumber int  subscan number.

    dataSize int  size of the binary data , as a number of bytes.

    dataUID EntityRef  reference to the binary data.

    stateId Tag []   numAntenna  State identifier.

    execBlockId Tag  ExecBlock identifier.



    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "Main"

    # the list of field names that make up key 'key'.
    _key = ["time", "configDescriptionId", "fieldId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = False  # if True archive binary else archive XML
    _fileAsBin = False  # if True file binary else file XML

    # A list to store the MainRow instances
    _privateRows = []

    # context is a dictionary where each key is a string resulting
    # from a call to the method Key and the value is a list of rows
    # maintained in time-order
    _context = {}

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    @staticmethod
    def Key(configDescriptionId, fieldId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        The parameter values are assumed to be the appropriate type for that parameter.
        """
        result = ""

        result += configDescriptionId.toString() + "_"

        result += fieldId.toString() + "_"

        return result

    def insertByTime(self, thisRow, rows):
        """
        Insert a MainRow in a list of MainRow so that it's ordered by ascending time.
        thisRow is the row to be inserted.
        rows is the list of rows where thisRow should be inserted, already ordered by ascending time.
        This method also appends row to the list of all rows held by this table.
        Returns the inserted row.
        """
        # rows should be a member of self or found in a member of self (dictionary of lists of rows)
        # So long as this method uses list methods to insert elements into rows that internal list of
        # rows will contain the result of this insertion

        thisRowTime = thisRow.getTime().get()

        # is rows empty or does this belong at the end of rows
        if len(rows) == 0 or (thisRowTime > rows[-1].getTime().get()):
            rows.append(thisRow)
            self._privateRows.append(thisRow)
            thisRow.isAdded()
            return thisRow

        # does this belong at the head of rows
        if thisRowTime < rows[0].getTime().get():
            rows.insert(0, thisRow)
            self._privateRows.append(thisRow)
            thisRow.isAdded()
            return thisRow

        # need to find where to insert thisRow in rows
        # use a dichotomy method to find the insertion index
        # these values must always be integers
        k0 = 0
        k1 = len(rows) - 1
        while k0 != (k1 - 1):
            if thisRowTime == rows[k0].getTime().get():
                if rows[k0].equalByRequiredValue(thisRow):
                    # this row is already inserted, do not insert it again
                    return rows[k0]
                else:
                    # this is a duplicate row with different required values, it can not be added
                    raise DuplicateKey("DuplicateKey exception in ", "MainTable")
            elif thisRowTime == rows[k1].getTime().get():
                if rows[k1].equalByRequiredValue(thisRow):
                    # this row is already inserted, do not insert it again
                    return rows[k1]
                else:
                    # this is a duplicate row with different required values, it can not be added
                    raise DuplicateKey("DuplicateKey exception in ", "MainTable")
            else:
                if thisRowTime <= rows[int((k0 + k1) / 2)].getTime().get():
                    k1 = int((k0 + k1) / 2)
                else:
                    k0 = int((k0 + k1) / 2)
        # it's either already at k0 or k1 or it should be inserted at k1
        if thisRowTime == rows[k0].getTime().get():
            if rows[k0].equalByRequiredValue(thisRow):
                # this row is already inserted, do not insert it again
                return rows[k0]
            else:
                # this is a duplicate row with different required values, it can not be added
                raise DuplicateKey("DuplicateKey exception in ", "MainTable")
        elif thisRowTime == rows[k1].getTime().get():
            if rows[k1].equalByRequiredValue(thisRow):
                # this row is already inserted, do not insert it again
                return rows[k1]
            else:
                # this is a duplicate row with different required values, it can not be added
                raise DuplicateKey("DuplicateKey exception in ", "MainTable")

        # it goes at k1
        rows.insert(k1, thisRow)
        self._privateRows.append(thisRow)
        thisRow.isAdded()
        return thisRow

    def __init__(self, container):
        """
        Create a MainTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("MainTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("MainTable")
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
        Returns "MainTable" followed by the current size of the table
        between parenthesis.
        Example : MainTable(12)
        """
        return "MainTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = MainRow(self)
        return thisRow

    def add(self, row):
        """
        Add a row to this table. 'row' is the MainRow to be added.
        If this table contains a MainRow whose attributes (key and mandatory values) are equal to those in 'row'
        then this returns that MainRow, otherwise 'row' is returned.
        If this table contains a MainRow with a key equal to that of 'row'
        but having a value section different from 'row' then an exception is raised.
        The row is inserted in the table in such a way that all rows having the same value of
        ( configDescriptionId, fieldId ) are stored by ascending time.
        """
        # the original code in the Java template is identical to that for checkAndAdd
        # so use that method here.
        return self._checkAndAdd(row)

    def newRow(
        self,
        time,
        configDescriptionId,
        fieldId,
        numAntenna,
        timeSampling,
        interval,
        numIntegration,
        scanNumber,
        subscanNumber,
        dataSize,
        dataUID,
        stateId,
        execBlockId,
    ):
        """
        Create a new MainRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = MainRow(self)

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

        thisRow.setExecBlockId(execBlockId)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new MainRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is null then the method returns a new MainRow with default values for its attributes.
        """

        return MainRow(self, row)

    # ====> Append a row to its table.

    def _checkAndAdd(self, row):
        """
        Append a row to it's table, used by the input conversion methods. Not intended for external use.
        Returns the added row.
        """
        rowKey = MainTable.Key(row.getConfigDescriptionId(), row.getFieldId())

        if rowKey not in self._context:
            self._context[rowKey] = []

        return self.insertByTime(row, self._context[rowKey])

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as a list of MainRow
        """
        return self._privateRows

    def getByContext(self, configDescriptionId, fieldId):
        """
        Return all the rows sorted by ascending startTime for a given context.
        The context is defined by the value of ( configDescriptionId, fieldId ).
        A None value is returned if the table contains no rows for the given
        ( configDescriptionId, fieldId ).
        """
        thisKey = MainTable.Key(configDescriptionId, fieldId)

        result = None
        if thisKey in self._context:
            result = self._context(thisKey)

        return result

    def getRowByKey(self, time, configDescriptionId, fieldId):
        """
        return the row having the key whose values are passed as parameters or
        None if no row exists for that key.
        """
        rowKey = MainTable.Key(configDescriptionId, fieldId)
        result = None
        if rowKey in self._context:
            rows = self._context[rowKey]
            # zero elements case excluded by the if statements here, returning None
            if len(rows) == 1:
                # single row in the context
                if time.get() == rows[0].getTime().get():
                    result = rows[0]
                # otherwise the times don't match, returning None
            elif len(rows) > 1:
                inRange = time.get() >= rows[0].getTime().get()
                inRange = inRange and (time.get() <= rows[-1].getTime().get())
                if inRange:
                    # the time falls within the available range
                    # more than one row
                    # use a dichotomy method for the general case
                    # k0 and k1 must always be integers
                    k0 = 0
                    k1 = len(rows) - 1
                    while k0 != k1 and result is None:
                        thisRow = rows[k0]
                        if thisRow.getTime().get() == time.get():
                            result = thisRow
                        else:
                            thisRow = rows[k1]
                            if thisRow.getTime().get() == time.get():
                                result = thisRow
                            else:
                                thisRow = rows[int((k0 + k1) / 2)]
                                if time.get() <= thisRow.getTime().get():
                                    k1 = int((k0 + k1) / 2)
                                else:
                                    k0 = int((k0 + k1) / 2)
        return result

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for Main (MainTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<MainTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:main="http://Alma/XASDM/MainTable" xsi:schemaLocation="http://Alma/XASDM/MainTable http://almaobservatory.org/XML/XASDM/4/MainTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</MainTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a Main (MainTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of MainTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "MainTable":
            raise ConversionException(
                "XML is not from a the expected table", "MainTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException("schemaVersion not found in XML", "MainTable")
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "MainTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "MainTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "MainTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "MainTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "MainTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "MainTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "MainTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "MainTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "MainTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a MainTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "MainTable",
            )

        if os.path.exists(os.path.join(directory, "Main.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "Main.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException("No file found for the Main table", "MainTable")

    def setFromMIMEFile(self, directory):
        print("setFromMIMEFile not implemented yet")

    def setFromXMLFile(self, directory):
        """
        This is the function used by setFromFile when the file is an XML file
        """

        # setFromFile has already established that this exists
        # read the entire file into a string
        xmlstr = None
        with open(os.path.join(directory, "Main.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("Main.xml is empty", "MainTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'Main.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'Main.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (Main)"
                % directory,
                "MainTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for Main")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "Main.xml")
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
