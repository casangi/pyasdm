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
# File AnnotationTable.py
#

import pyasdm.ASDM

from .AnnotationRow import AnnotationRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class AnnotationTable(Representable):
    """
    The AnnotationTable class is an Alma table.

     Role
     The Annotation Table is intended to offer space for unexpected data to be  added in the software development process at short notice, without  redefining the data model.

     Generated from model's revision -1, branch

     Attributes of Annotation

                  Key

    annotationId Tag identifies a unique row in the table.



                  Value (Mandatory)

    time ArrayTime  mid point of the interval of time on which the recorded information is pertinent.

    issue str  name of this annotation.

    details str  details of this annotation.



                  Value (Optional)

    numAntenna int  number of antennas.

    basebandName BasebandName []   numBaseband  an array of numBaseband baseband names.

    numBaseband int  number of basebands.

    interval Interval  time interval

    dValue double  scalar data.

    vdValue double []     useful to store an array of double values.

    vvdValues double []  []   ,   useful to store an array of array(s) of double values.

    llValue int  useful to record a long long data.

    vllValue int []     useful to store an array of array(s) of long long values.

    vvllValue int []  []   ,   useful to store an array of array(s) long long values.

    sValue str  details of this annotation.

    antennaId Tag []   numAntenna  refers to a collection of rows in the AntennaTable.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "Annotation"

    # the list of field names that make up key 'key'.
    _key = ["annotationId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = False  # if True archive binary else archive XML
    _fileAsBin = False  # if True file binary else file XML

    # A list to store the AnnotationRow instances
    _privateRows = []

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    def __init__(self, container):
        """
        Create a AnnotationTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("AnnotationTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("AnnotationTable")
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
        Returns "AnnotationTable" followed by the current size of the table
        between parenthesis.
        Example : AnnotationTable(12)
        """
        return "AnnotationTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = AnnotationRow(self)
        return thisRow

    def add(self, newrow):
        """
        Look up the table for a row whose noautoincrementable attributes are matching their
        homologues in newrow.  If a row is found return that row else autoincrement newrow.annotationId,
        add newrow to its table and return newrow.

        returns a AnnotationRow.
        """

        aRow = self.lookup(newrow.getTime(), newrow.getIssue(), newrow.getDetails())
        if aRow is not None:
            return aRow

        # Autoincrement annotationId, same as the number of this row in the table
        newrow.setAnnotationId(Tag(size(), TagType.Annotation))

        newrow.isAdded()
        return newrow

    def newRow(self, time, issue, details):
        """
        Create a new AnnotationRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = AnnotationRow(self)

        thisRow.setTime(time)

        thisRow.setIssue(issue)

        thisRow.setDetails(details)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new AnnotationRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new AnnotationRow with default values for its attributes.
        """

        return AnnotationRow(self, row)

    # ====> Append a row to its table.

    def _checkAndAdd(self, newrow):
        """
        A private method to append a row to its table, used by input conversion
        methods. Not intended for external use.

        If this table has an autoincrementable attribute then check if newrow verifies the rule of uniqueness and raise an exception if not.
        Returns newrow.
        """

        if (
            self.lookup(newrow.getTime(), newrow.getIssue(), newrow.getDetails())
            is not None
        ):
            raise UniquenessViolationException(
                "Uniqueness violation exception in table AnnotationTable"
            )

        if self.getRowByKey(newrow.getAnnotationId()) is not None:
            raise DuplicateKey("Duplicate key exception in ", "AnnotationTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of AnnotationRow
        """
        return self._privateRows

    def getRowByKey(self, annotationId):
        """
        Returns a AnnotationRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        @param annotationId.

        """
        for row in self._privateRows:

            if not row.getAnnotationId().equals(annotationId):
                continue

            # this row matches these parameters
            return row
        # no match found
        return None

    def lookup(self, time, issue, details):
        """
                Look up the table for a row whose all attributes  except the autoincrementable one
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param time.

        param issue.

        param details.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(time, issue, details):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for Annotation (AnnotationTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<AnnotationTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:annttn="http://Alma/XASDM/AnnotationTable" xsi:schemaLocation="http://Alma/XASDM/AnnotationTable http://almaobservatory.org/XML/XASDM/4/AnnotationTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</AnnotationTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a Annotation (AnnotationTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of AnnotationTable.
        if (
            not xmldom.hasChildNodes()
            or xmldom.firstChild.nodeName != "AnnotationTable"
        ):
            raise ConversionException(
                "XML is not from a the expected table", "AnnotationTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException(
                "schemaVersion not found in XML", "AnnotationTable"
            )
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "AnnotationTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "AnnotationTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "AnnotationTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "AnnotationTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "AnnotationTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "AnnotationTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "AnnotationTable") from None

                except ValueError as exc:
                    # TBD when this turns up via template
                    msg = (
                        "UniquenessViolationException in row in AnnotationTable : %s"
                        % str(exc)
                    )

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "AnnotationTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "AnnotationTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a AnnotationTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "AnnotationTable",
            )

        if os.path.exists(os.path.join(directory, "Annotation.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "Annotation.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the Annotation table", "AnnotationTable"
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
        with open(os.path.join(directory, "Annotation.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("Annotation.xml is empty", "AnnotationTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'Annotation.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'Annotation.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (Annotation)"
                % directory,
                "AnnotationTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for Annotation")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "Annotation.xml")
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
