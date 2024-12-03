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
# File HistoryTable.py
#

import pyasdm.ASDM

from .HistoryRow import HistoryRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class HistoryTable(Representable):
    """
    The HistoryTable class is an Alma table.

     Role
     History information.

     Generated from model's revision -1, branch

     Attributes of History

                  Key

    execBlockId Tag

    time ArrayTime



                  Value (Mandatory)

    message str

    priority str

    origin str

    objectId str

    application str

    cliCommand str

    appParms str



    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "History"

    # the list of field names that make up key 'key'.
    _key = ["execBlockId", "time"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = False  # if True archive binary else archive XML
    _fileAsBin = False  # if True file binary else file XML

    # A list to store the HistoryRow instances
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
    def Key(execBlockId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        The parameter values are assumed to be the appropriate type for that parameter.
        """
        result = ""

        result += execBlockId.toString() + "_"

        return result

    def insertByTime(self, thisRow, rows):
        """
        Insert a HistoryRow in a list of HistoryRow so that it's ordered by ascending time.
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
                    raise DuplicateKey("DuplicateKey exception in ", "HistoryTable")
            elif thisRowTime == rows[k1].getTime().get():
                if rows[k1].equalByRequiredValue(thisRow):
                    # this row is already inserted, do not insert it again
                    return rows[k1]
                else:
                    # this is a duplicate row with different required values, it can not be added
                    raise DuplicateKey("DuplicateKey exception in ", "HistoryTable")
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
                raise DuplicateKey("DuplicateKey exception in ", "HistoryTable")
        elif thisRowTime == rows[k1].getTime().get():
            if rows[k1].equalByRequiredValue(thisRow):
                # this row is already inserted, do not insert it again
                return rows[k1]
            else:
                # this is a duplicate row with different required values, it can not be added
                raise DuplicateKey("DuplicateKey exception in ", "HistoryTable")

        # it goes at k1
        rows.insert(k1, thisRow)
        self._privateRows.append(thisRow)
        thisRow.isAdded()
        return thisRow

    def __init__(self, container):
        """
        Create a HistoryTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("HistoryTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("HistoryTable")
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
        Returns "HistoryTable" followed by the current size of the table
        between parenthesis.
        Example : HistoryTable(12)
        """
        return "HistoryTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = HistoryRow(self)
        return thisRow

    def add(self, row):
        """
        Add a row to this table. 'row' is the row to be added.
        If this table contains a row whose attributes (key and mandatory values) are equal to those in 'row'
        then this returns that row, otherwise 'row' is returned.
        If this table contains a row with a key equal to that of 'row'
        but having a value section different from 'row' then an exception is raised.
        The row is inserted in the table in such a way that all rows having the same value of
        ( execBlockId ) are stored by ascending time.
        """
        # the original code in the Java template is identical to that for _checkAndAdd
        # so use that method here.
        return self._checkAndAdd(row)

    def newRow(
        self,
        execBlockId,
        time,
        message,
        priority,
        origin,
        objectId,
        application,
        cliCommand,
        appParms,
    ):
        """
        Create a new HistoryRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = HistoryRow(self)

        thisRow.setExecBlockId(execBlockId)

        thisRow.setTime(time)

        thisRow.setMessage(message)

        thisRow.setPriority(priority)

        thisRow.setOrigin(origin)

        thisRow.setObjectId(objectId)

        thisRow.setApplication(application)

        thisRow.setCliCommand(cliCommand)

        thisRow.setAppParms(appParms)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new HistoryRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new HistoryRow with default values for its attributes.
        """

        return HistoryRow(self, row)

    # ====> Append a row to its table.

    def _checkAndAdd(self, newrow):
        """
        A method to append a row to its table, used by input conversion
        methods. Not intended for external use.
        Returns the added row.
        """

        rowKey = HistoryTable.Key(newrow.getExecBlockId())

        if rowKey not in self._context:
            self._context[rowKey] = []

        return self.insertByTime(newrow, self._context[rowKey])

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as a list of HistoryRow
        """
        return self._privateRows

    def getByContext(self, execBlockId):
        """
        Return all the rows sorted by ascending startTime for a given context.
        The context is defined by the value of ( execBlockId ).
        A None value is returned if the table contains no rows for the given
        ( execBlockId ).
        """
        thisKey = HistoryTable.Key(execBlockId)

        result = None
        if thisKey in self._context:
            result = self._context(thisKey)

        return result

    def getRowByKey(self, execBlockId, time):
        """
        return the row having the key whose values are passed as parameters or
        None if no row exists for that key.
        """
        rowKey = HistoryTable.Key(execBlockId)
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
        to the schema defined for History (HistoryTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<HistoryTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:histry="http://Alma/XASDM/HistoryTable" xsi:schemaLocation="http://Alma/XASDM/HistoryTable http://almaobservatory.org/XML/XASDM/4/HistoryTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</HistoryTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a History (HistoryTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of HistoryTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "HistoryTable":
            raise ConversionException(
                "XML is not from a the expected table", "HistoryTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException("schemaVersion not found in XML", "HistoryTable")
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "HistoryTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "HistoryTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "HistoryTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "HistoryTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "HistoryTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "HistoryTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "HistoryTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "HistoryTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "HistoryTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a HistoryTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "HistoryTable",
            )

        if os.path.exists(os.path.join(directory, "History.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "History.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the History table", "HistoryTable"
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
        with open(os.path.join(directory, "History.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("History.xml is empty", "HistoryTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'History.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'History.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (History)"
                % directory,
                "HistoryTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for History")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "History.xml")
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
