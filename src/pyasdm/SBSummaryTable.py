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
# File SBSummaryTable.py
#

import pyasdm.ASDM

from .SBSummaryRow import SBSummaryRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class SBSummaryTable(Representable):
    """
    The SBSummaryTable class is an Alma table.

     Role
     Characteristics of the Scheduling Block that has been executed. Much of the  data here is reproduced from the Scheduling block itself.

     Generated from model's revision -1, branch

     Attributes of SBSummary

                  Key

    sBSummaryId Tag refers to a unique row in the table.



                  Value (Mandatory)

    sbSummaryUID EntityRef  the scheduling block archive's UID.

    projectUID EntityRef  the projet archive's UID.

    obsUnitSetUID EntityRef  the observing unit set archive's UID.

    frequency double  a representative frequency.

    frequencyBand ReceiverBand  the frequency band.

    sbType SBType  the type of scheduling block.

    sbDuration Interval  the duration of the scheduling block.

    numObservingMode int  the number of observing modes.

    observingMode str []   numObservingMode  the observing modes.

    numberRepeats int  the number of repeats.

    numScienceGoal int  the number of scientific goals.

    scienceGoal str []   numScienceGoal  the scientific goals.

    numWeatherConstraint int  the number of weather constraints.

    weatherConstraint str []   numWeatherConstraint  the weather constraints.



                  Value (Optional)

    centerDirection Angle []   2  the representative target direction.

    centerDirectionCode DirectionReferenceCode  identifies the direction reference frame associated with centerDirection.

    centerDirectionEquinox ArrayTime  the equinox associated to centerDirectionReferenceCode (if needed).


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "SBSummary"

    # the list of field names that make up key 'key'.
    _key = ["sBSummaryId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = False  # if True archive binary else archive XML
    _fileAsBin = False  # if True file binary else file XML

    # A list to store the SBSummaryRow instances
    _privateRows = []

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on centerDirection during an add operation on the table
    _centerDirectionEqTolerance = Angle(0.0)

    def setCenterDirectionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on centerDirection
        """
        self._centerDirectionEqTolerance = Angle(tolerance)

    # A getter for the tolerance on centerDirection
    def getCenterDirectionEqTolerance(self):
        """
        A getter for the tolerance on centerDirection
        """
        return self._centerDirectionEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    def __init__(self, container):
        """
        Create a SBSummaryTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("SBSummaryTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("SBSummaryTable")
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
        Returns "SBSummaryTable" followed by the current size of the table
        between parenthesis.
        Example : SBSummaryTable(12)
        """
        return "SBSummaryTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = SBSummaryRow(self)
        return thisRow

    def add(self, newrow):
        """
        Look up the table for a row whose noautoincrementable attributes are matching their
        homologues in newrow.  If a row is found return that row else autoincrement newrow.sBSummaryId,
        add newrow to its table and return newrow.

        returns a SBSummaryRow.
        """

        aRow = self.lookup(
            newrow.getSbSummaryUID(),
            newrow.getProjectUID(),
            newrow.getObsUnitSetUID(),
            newrow.getFrequency(),
            newrow.getFrequencyBand(),
            newrow.getSbType(),
            newrow.getSbDuration(),
            newrow.getNumObservingMode(),
            newrow.getObservingMode(),
            newrow.getNumberRepeats(),
            newrow.getNumScienceGoal(),
            newrow.getScienceGoal(),
            newrow.getNumWeatherConstraint(),
            newrow.getWeatherConstraint(),
        )
        if aRow is not None:
            return aRow

        # Autoincrement sBSummaryId, same as the number of this row in the table
        newrow.setSBSummaryId(Tag(size(), TagType.SBSummary))

        newrow.isAdded()
        return newrow

    def newRow(
        self,
        sbSummaryUID,
        projectUID,
        obsUnitSetUID,
        frequency,
        frequencyBand,
        sbType,
        sbDuration,
        numObservingMode,
        observingMode,
        numberRepeats,
        numScienceGoal,
        scienceGoal,
        numWeatherConstraint,
        weatherConstraint,
    ):
        """
        Create a new SBSummaryRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = SBSummaryRow(self)

        thisRow.setSbSummaryUID(sbSummaryUID)

        thisRow.setProjectUID(projectUID)

        thisRow.setObsUnitSetUID(obsUnitSetUID)

        thisRow.setFrequency(frequency)

        thisRow.setFrequencyBand(frequencyBand)

        thisRow.setSbType(sbType)

        thisRow.setSbDuration(sbDuration)

        thisRow.setNumObservingMode(numObservingMode)

        thisRow.setObservingMode(observingMode)

        thisRow.setNumberRepeats(numberRepeats)

        thisRow.setNumScienceGoal(numScienceGoal)

        thisRow.setScienceGoal(scienceGoal)

        thisRow.setNumWeatherConstraint(numWeatherConstraint)

        thisRow.setWeatherConstraint(weatherConstraint)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new SBSummaryRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new SBSummaryRow with default values for its attributes.
        """

        return SBSummaryRow(self, row)

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
                newrow.getSbSummaryUID(),
                newrow.getProjectUID(),
                newrow.getObsUnitSetUID(),
                newrow.getFrequency(),
                newrow.getFrequencyBand(),
                newrow.getSbType(),
                newrow.getSbDuration(),
                newrow.getNumObservingMode(),
                newrow.getObservingMode(),
                newrow.getNumberRepeats(),
                newrow.getNumScienceGoal(),
                newrow.getScienceGoal(),
                newrow.getNumWeatherConstraint(),
                newrow.getWeatherConstraint(),
            )
            is not None
        ):
            raise UniquenessViolationException(
                "Uniqueness violation exception in table SBSummaryTable"
            )

        if self.getRowByKey(newrow.getSBSummaryId()) is not None:
            raise DuplicateKey("Duplicate key exception in ", "SBSummaryTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of SBSummaryRow
        """
        return self._privateRows

    def getRowByKey(self, sBSummaryId):
        """
        Returns a SBSummaryRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        @param sBSummaryId.

        """
        for row in self._privateRows:

            if not row.getSBSummaryId().equals(sBSummaryId):
                continue

            # this row matches these parameters
            return row
        # no match found
        return None

    def lookup(
        self,
        sbSummaryUID,
        projectUID,
        obsUnitSetUID,
        frequency,
        frequencyBand,
        sbType,
        sbDuration,
        numObservingMode,
        observingMode,
        numberRepeats,
        numScienceGoal,
        scienceGoal,
        numWeatherConstraint,
        weatherConstraint,
    ):
        """
                Look up the table for a row whose all attributes  except the autoincrementable one
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param sbSummaryUID.

        param projectUID.

        param obsUnitSetUID.

        param frequency.

        param frequencyBand.

        param sbType.

        param sbDuration.

        param numObservingMode.

        param observingMode.

        param numberRepeats.

        param numScienceGoal.

        param scienceGoal.

        param numWeatherConstraint.

        param weatherConstraint.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                sbSummaryUID,
                projectUID,
                obsUnitSetUID,
                frequency,
                frequencyBand,
                sbType,
                sbDuration,
                numObservingMode,
                observingMode,
                numberRepeats,
                numScienceGoal,
                scienceGoal,
                numWeatherConstraint,
                weatherConstraint,
            ):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for SBSummary (SBSummaryTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<SBSummaryTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:sbsmmr="http://Alma/XASDM/SBSummaryTable" xsi:schemaLocation="http://Alma/XASDM/SBSummaryTable http://almaobservatory.org/XML/XASDM/4/SBSummaryTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</SBSummaryTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a SBSummary (SBSummaryTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of SBSummaryTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "SBSummaryTable":
            raise ConversionException(
                "XML is not from a the expected table", "SBSummaryTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException(
                "schemaVersion not found in XML", "SBSummaryTable"
            )
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "SBSummaryTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "SBSummaryTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "SBSummaryTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "SBSummaryTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "SBSummaryTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "SBSummaryTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "SBSummaryTable") from None

                except ValueError as exc:
                    # TBD when this turns up via template
                    msg = (
                        "UniquenessViolationException in row in SBSummaryTable : %s"
                        % str(exc)
                    )

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "SBSummaryTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "SBSummaryTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a SBSummaryTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "SBSummaryTable",
            )

        if os.path.exists(os.path.join(directory, "SBSummary.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "SBSummary.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the SBSummary table", "SBSummaryTable"
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
        with open(os.path.join(directory, "SBSummary.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("SBSummary.xml is empty", "SBSummaryTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'SBSummary.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'SBSummary.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (SBSummary)"
                % directory,
                "SBSummaryTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for SBSummary")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "SBSummary.xml")
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
