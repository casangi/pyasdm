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
# File FlagTable.py
#

import pyasdm.ASDM

from .FlagRow import FlagRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class FlagTable(Representable):
    """
        The FlagTable class is an Alma table.

         Role
         This table is used for flagging visibility data and is used in addition to the Binary Data Format flags produced by the correlator software.

         Generated from model's revision -1, branch

         Attributes of Flag

                      Key

        flagId Tag identifies a unique row in the table.



                      Value (Mandatory)

        startTime ArrayTime  the start time of the flagging period.

        endTime ArrayTime  the end time of the flagging period.

        reason str  Extensible list of flagging conditions.

        numAntenna int  The number of antennas to which the flagging refers.By convention numAntenna== 0 means that the flag applies to all the existing antennas, in such a case the array antennaId can be left empty.

        antennaId Tag []   numAntenna  An array of Tag which refers to a collection of rows in the Antenna table. The flag applies to the antennas described in these rows. It is an error to have different elements with a same value in this array.



                      Value (Optional)

        numPolarizationType int  The number of polarization types , i.e. the size of the attribute polarizationType. By convention numPolarizationType == 0 means that the flag applies to all the defined polarization types. \b Remark : numPolarizationType and polarizationType, both optional, must be both present or both absent in one same row of the table, except if numPolarizationType==0 in which case all the defined polarization types are involved in the flagging.

        numSpectralWindow int  The number of spectral windows targeted by the flagging. By convention numSpectralWindow == 0 means that the flag applies to all the existing spectral windows. \b Remark : numSpectralWindow and spectralWindow, both optional, must be both present or both absent in one same row of the table, except if numSpectralWindow==0, in which case all the declared spectral windows are involved in the flagging.

        numPairedAntenna int  The number of antennas to be paired with to form the flagged baselines. By convention, numPairedAntenna == 0 means that the flag applies to all baselines built on the antennas declared in the attribute antennaId. \b Remark: numPairedAntenna and pairedAntenna, both optional, must be both present or both absent except if numPairedAntenna==0 in which case one has to consider all the baselines defined upon the antennas announced in  antennaId.

        numChan int  Number of channels to be flaggged.

        polarizationType PolarizationType []   numPolarizationType  An array of values of type PolarizationType. It specifies the polarization types where the flagging applies. It is an error to have different elements with a same value in this array.

        channel int []  []   numChan, 3  An array of triplets where the first element is the number spectralWindowId. The second and third values are the startChannel and endChannel,
    respectively, which specify
    the channels where flagging applies. It is
    an error to have different elements with a
    same value in this array.


        pairedAntennaId Tag []   numPairedAntenna  An array of Tag which refers to rows in the Antenna table. These rows contain the description of the antennas which are paired to form the flagged baselines. It is an error to have distinct elements with a same value in this array.

        spectralWindowId Tag []   numSpectralWindow  An array of Tag  which refers to a collection of rows in the SpectralWindow table. The flag applies to the spectral windows described in these rows. It is an error to have different elements with a same value in this array.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "Flag"

    # the list of field names that make up key 'key'.
    _key = ["flagId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = False  # if True archive binary else archive XML
    _fileAsBin = False  # if True file binary else file XML

    # A list to store the FlagRow instances
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
        Create a FlagTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("FlagTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("FlagTable")
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
        Returns "FlagTable" followed by the current size of the table
        between parenthesis.
        Example : FlagTable(12)
        """
        return "FlagTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = FlagRow(self)
        return thisRow

    def add(self, newrow):
        """
        Look up the table for a row whose noautoincrementable attributes are matching their
        homologues in newrow.  If a row is found return that row else autoincrement newrow.flagId,
        add newrow to its table and return newrow.

        returns a FlagRow.
        """

        aRow = self.lookup(
            newrow.getStartTime(),
            newrow.getEndTime(),
            newrow.getReason(),
            newrow.getNumAntenna(),
            newrow.getAntennaId(),
        )
        if aRow is not None:
            return aRow

        # Autoincrement flagId, same as the number of this row in the table
        newrow.setFlagId(Tag(size(), TagType.Flag))

        newrow.isAdded()
        return newrow

    def newRow(self, startTime, endTime, reason, numAntenna, antennaId):
        """
        Create a new FlagRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = FlagRow(self)

        thisRow.setStartTime(startTime)

        thisRow.setEndTime(endTime)

        thisRow.setReason(reason)

        thisRow.setNumAntenna(numAntenna)

        thisRow.setAntennaId(antennaId)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new FlagRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new FlagRow with default values for its attributes.
        """

        return FlagRow(self, row)

    # ====> Append a row to its table.

    def _checkAndAdd(self, newrow):
        """
        A private method to append a row to its table, used by input conversion
        methods. Not intended for external use.

        If this table has an autoincrementable attribute then check if newrow verifies the rule of uniqueness and raise an exception if not.
        Returns newrow.
        """

        if (
            self.lookup(
                newrow.getStartTime(),
                newrow.getEndTime(),
                newrow.getReason(),
                newrow.getNumAntenna(),
                newrow.getAntennaId(),
            )
            is not None
        ):
            raise UniquenessViolationException(
                "Uniqueness violation exception in table FlagTable"
            )

        if self.getRowByKey(newrow.getFlagId()) is not None:
            raise DuplicateKey("Duplicate key exception in ", "FlagTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of FlagRow
        """
        return self._privateRows

    def getRowByKey(self, flagId):
        """
        Returns a FlagRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        @param flagId.

        """
        for row in self._privateRows:

            if not row.getFlagId().equals(flagId):
                continue

            # this row matches these parameters
            return row
        # no match found
        return None

    def lookup(self, startTime, endTime, reason, numAntenna, antennaId):
        """
                Look up the table for a row whose all attributes  except the autoincrementable one
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param startTime.

        param endTime.

        param reason.

        param numAntenna.

        param antennaId.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(startTime, endTime, reason, numAntenna, antennaId):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for Flag (FlagTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<FlagTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:flag="http://Alma/XASDM/FlagTable" xsi:schemaLocation="http://Alma/XASDM/FlagTable http://almaobservatory.org/XML/XASDM/4/FlagTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</FlagTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a Flag (FlagTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of FlagTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "FlagTable":
            raise ConversionException(
                "XML is not from a the expected table", "FlagTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException("schemaVersion not found in XML", "FlagTable")
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "FlagTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "FlagTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "FlagTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "FlagTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "FlagTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "FlagTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "FlagTable") from None

                except ValueError as exc:
                    # TBD when this turns up via template
                    msg = "UniquenessViolationException in row in FlagTable : %s" % str(
                        exc
                    )

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "FlagTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "FlagTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a FlagTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "FlagTable",
            )

        if os.path.exists(os.path.join(directory, "Flag.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "Flag.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException("No file found for the Flag table", "FlagTable")

    def setFromMIMEFile(self, directory):
        print("setFromMIMEFile not implemented yet")

    def setFromXMLFile(self, directory):
        """
        This is the function used by setFromFile when the file is an XML file
        """

        # setFromFile has already established that this exists
        # read the entire file into a string
        xmlstr = None
        with open(os.path.join(directory, "Flag.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("Flag.xml is empty", "FlagTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'Flag.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'Flag.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (Flag)"
                % directory,
                "FlagTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for Flag")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "Flag.xml")
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
