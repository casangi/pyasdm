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
# File ExecBlockTable.py
#

import pyasdm.ASDM

from .ExecBlockRow import ExecBlockRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class ExecBlockTable(Representable):
    """
    The ExecBlockTable class is an Alma table.

     Role
     Characteristics of the Execution block.

     Generated from model's revision -1, branch

     Attributes of ExecBlock

                  Key

    execBlockId Tag identifies a unique row in ExecBlock Table.



                  Value (Mandatory)

    startTime ArrayTime  the start time of the execution block.

    endTime ArrayTime  the end time of the execution block.

    execBlockNum int  indicates the position of the execution block in the project (sequential numbering starting at 1).

    execBlockUID EntityRef  the archive's UID of the execution block.

    projectUID EntityRef  the archive's UID of the project.

    configName str  the name of the array's configuration.

    telescopeName str  the name of the telescope.

    observerName str  the name of the observer.

    numObservingLog int  the number of elements in the (array) attribute observingLog.

    observingLog str []   numObservingLog   logs of the observation during this execution block.

    sessionReference EntityRef  the observing session reference.

    baseRangeMin Length  the length of the shortest baseline.

    baseRangeMax Length  the length of the longest baseline.

    baseRmsMinor Length  the minor axis of the representative ellipse of baseline lengths.

    baseRmsMajor Length  the major axis of the representative ellipse of baseline lengths.

    basePa Angle  the baselines position angle.

    aborted bool  the execution block has been aborted (true) or has completed (false).

    numAntenna int  the number of antennas.

    antennaId Tag []   numAntenna  refers to the relevant rows in AntennaTable.

    sBSummaryId Tag  refers to a unique row  in SBSummaryTable.



                  Value (Optional)

    releaseDate ArrayTime  the date when the data go to the public domain.

    schedulerMode str  the mode of scheduling.

    siteAltitude Length  the altitude of the site.

    siteLongitude Angle  the longitude of the site.

    siteLatitude Angle  the latitude of the site.

    observingScript str  The text of the observation script.

    observingScriptUID EntityRef  A reference to the Entity which contains the observing script.

    scaleId Tag  refers to a unique row in the table Scale.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "ExecBlock"

    # the list of field names that make up key 'key'.
    _key = ["execBlockId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = False  # if True archive binary else archive XML
    _fileAsBin = False  # if True file binary else file XML

    # A list to store the ExecBlockRow instances
    _privateRows = []

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on baseRangeMin during an add operation on the table
    _baseRangeMinEqTolerance = Length(0.0)

    def setBaseRangeMinEqTolerance(self, tolerance):
        """
        A setter for the tolerance on baseRangeMin
        """
        self._baseRangeMinEqTolerance = Length(tolerance)

    # A getter for the tolerance on baseRangeMin
    def getBaseRangeMinEqTolerance(self):
        """
        A getter for the tolerance on baseRangeMin
        """
        return self._baseRangeMinEqTolerance

    # The tolerance which will be used on baseRangeMax during an add operation on the table
    _baseRangeMaxEqTolerance = Length(0.0)

    def setBaseRangeMaxEqTolerance(self, tolerance):
        """
        A setter for the tolerance on baseRangeMax
        """
        self._baseRangeMaxEqTolerance = Length(tolerance)

    # A getter for the tolerance on baseRangeMax
    def getBaseRangeMaxEqTolerance(self):
        """
        A getter for the tolerance on baseRangeMax
        """
        return self._baseRangeMaxEqTolerance

    # The tolerance which will be used on baseRmsMinor during an add operation on the table
    _baseRmsMinorEqTolerance = Length(0.0)

    def setBaseRmsMinorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on baseRmsMinor
        """
        self._baseRmsMinorEqTolerance = Length(tolerance)

    # A getter for the tolerance on baseRmsMinor
    def getBaseRmsMinorEqTolerance(self):
        """
        A getter for the tolerance on baseRmsMinor
        """
        return self._baseRmsMinorEqTolerance

    # The tolerance which will be used on baseRmsMajor during an add operation on the table
    _baseRmsMajorEqTolerance = Length(0.0)

    def setBaseRmsMajorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on baseRmsMajor
        """
        self._baseRmsMajorEqTolerance = Length(tolerance)

    # A getter for the tolerance on baseRmsMajor
    def getBaseRmsMajorEqTolerance(self):
        """
        A getter for the tolerance on baseRmsMajor
        """
        return self._baseRmsMajorEqTolerance

    # The tolerance which will be used on basePa during an add operation on the table
    _basePaEqTolerance = Angle(0.0)

    def setBasePaEqTolerance(self, tolerance):
        """
        A setter for the tolerance on basePa
        """
        self._basePaEqTolerance = Angle(tolerance)

    # A getter for the tolerance on basePa
    def getBasePaEqTolerance(self):
        """
        A getter for the tolerance on basePa
        """
        return self._basePaEqTolerance

    # The tolerance which will be used on siteAltitude during an add operation on the table
    _siteAltitudeEqTolerance = Length(0.0)

    def setSiteAltitudeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on siteAltitude
        """
        self._siteAltitudeEqTolerance = Length(tolerance)

    # A getter for the tolerance on siteAltitude
    def getSiteAltitudeEqTolerance(self):
        """
        A getter for the tolerance on siteAltitude
        """
        return self._siteAltitudeEqTolerance

    # The tolerance which will be used on siteLongitude during an add operation on the table
    _siteLongitudeEqTolerance = Angle(0.0)

    def setSiteLongitudeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on siteLongitude
        """
        self._siteLongitudeEqTolerance = Angle(tolerance)

    # A getter for the tolerance on siteLongitude
    def getSiteLongitudeEqTolerance(self):
        """
        A getter for the tolerance on siteLongitude
        """
        return self._siteLongitudeEqTolerance

    # The tolerance which will be used on siteLatitude during an add operation on the table
    _siteLatitudeEqTolerance = Angle(0.0)

    def setSiteLatitudeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on siteLatitude
        """
        self._siteLatitudeEqTolerance = Angle(tolerance)

    # A getter for the tolerance on siteLatitude
    def getSiteLatitudeEqTolerance(self):
        """
        A getter for the tolerance on siteLatitude
        """
        return self._siteLatitudeEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    def __init__(self, container):
        """
        Create a ExecBlockTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("ExecBlockTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("ExecBlockTable")
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
        Returns "ExecBlockTable" followed by the current size of the table
        between parenthesis.
        Example : ExecBlockTable(12)
        """
        return "ExecBlockTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = ExecBlockRow(self)
        return thisRow

    def add(self, newrow):
        """
        Look up the table for a row whose noautoincrementable attributes are matching their
        homologues in newrow.  If a row is found return that row else autoincrement newrow.execBlockId,
        add newrow to its table and return newrow.

        returns a ExecBlockRow.
        """

        aRow = self.lookup(
            newrow.getStartTime(),
            newrow.getEndTime(),
            newrow.getExecBlockNum(),
            newrow.getExecBlockUID(),
            newrow.getProjectUID(),
            newrow.getConfigName(),
            newrow.getTelescopeName(),
            newrow.getObserverName(),
            newrow.getNumObservingLog(),
            newrow.getObservingLog(),
            newrow.getSessionReference(),
            newrow.getBaseRangeMin(),
            newrow.getBaseRangeMax(),
            newrow.getBaseRmsMinor(),
            newrow.getBaseRmsMajor(),
            newrow.getBasePa(),
            newrow.getAborted(),
            newrow.getNumAntenna(),
            newrow.getAntennaId(),
            newrow.getSBSummaryId(),
        )
        if aRow is not None:
            return aRow

        # Autoincrement execBlockId, same as the number of this row in the table
        newrow.setExecBlockId(Tag(size(), TagType.ExecBlock))

        newrow.isAdded()
        return newrow

    def newRow(
        self,
        startTime,
        endTime,
        execBlockNum,
        execBlockUID,
        projectUID,
        configName,
        telescopeName,
        observerName,
        numObservingLog,
        observingLog,
        sessionReference,
        baseRangeMin,
        baseRangeMax,
        baseRmsMinor,
        baseRmsMajor,
        basePa,
        aborted,
        numAntenna,
        antennaId,
        sBSummaryId,
    ):
        """
        Create a new ExecBlockRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = ExecBlockRow(self)

        thisRow.setStartTime(startTime)

        thisRow.setEndTime(endTime)

        thisRow.setExecBlockNum(execBlockNum)

        thisRow.setExecBlockUID(execBlockUID)

        thisRow.setProjectUID(projectUID)

        thisRow.setConfigName(configName)

        thisRow.setTelescopeName(telescopeName)

        thisRow.setObserverName(observerName)

        thisRow.setNumObservingLog(numObservingLog)

        thisRow.setObservingLog(observingLog)

        thisRow.setSessionReference(sessionReference)

        thisRow.setBaseRangeMin(baseRangeMin)

        thisRow.setBaseRangeMax(baseRangeMax)

        thisRow.setBaseRmsMinor(baseRmsMinor)

        thisRow.setBaseRmsMajor(baseRmsMajor)

        thisRow.setBasePa(basePa)

        thisRow.setAborted(aborted)

        thisRow.setNumAntenna(numAntenna)

        thisRow.setAntennaId(antennaId)

        thisRow.setSBSummaryId(sBSummaryId)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new ExecBlockRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new ExecBlockRow with default values for its attributes.
        """

        return ExecBlockRow(self, row)

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
                newrow.getExecBlockNum(),
                newrow.getExecBlockUID(),
                newrow.getProjectUID(),
                newrow.getConfigName(),
                newrow.getTelescopeName(),
                newrow.getObserverName(),
                newrow.getNumObservingLog(),
                newrow.getObservingLog(),
                newrow.getSessionReference(),
                newrow.getBaseRangeMin(),
                newrow.getBaseRangeMax(),
                newrow.getBaseRmsMinor(),
                newrow.getBaseRmsMajor(),
                newrow.getBasePa(),
                newrow.getAborted(),
                newrow.getNumAntenna(),
                newrow.getAntennaId(),
                newrow.getSBSummaryId(),
            )
            is not None
        ):
            raise UniquenessViolationException(
                "Uniqueness violation exception in table ExecBlockTable"
            )

        if self.getRowByKey(newrow.getExecBlockId()) is not None:
            raise DuplicateKey("Duplicate key exception in ", "ExecBlockTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of ExecBlockRow
        """
        return self._privateRows

    def getRowByKey(self, execBlockId):
        """
        Returns a ExecBlockRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        @param execBlockId.

        """
        for row in self._privateRows:

            if not row.getExecBlockId().equals(execBlockId):
                continue

            # this row matches these parameters
            return row
        # no match found
        return None

    def lookup(
        self,
        startTime,
        endTime,
        execBlockNum,
        execBlockUID,
        projectUID,
        configName,
        telescopeName,
        observerName,
        numObservingLog,
        observingLog,
        sessionReference,
        baseRangeMin,
        baseRangeMax,
        baseRmsMinor,
        baseRmsMajor,
        basePa,
        aborted,
        numAntenna,
        antennaId,
        sBSummaryId,
    ):
        """
                Look up the table for a row whose all attributes  except the autoincrementable one
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param startTime.

        param endTime.

        param execBlockNum.

        param execBlockUID.

        param projectUID.

        param configName.

        param telescopeName.

        param observerName.

        param numObservingLog.

        param observingLog.

        param sessionReference.

        param baseRangeMin.

        param baseRangeMax.

        param baseRmsMinor.

        param baseRmsMajor.

        param basePa.

        param aborted.

        param numAntenna.

        param antennaId.

        param sBSummaryId.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                startTime,
                endTime,
                execBlockNum,
                execBlockUID,
                projectUID,
                configName,
                telescopeName,
                observerName,
                numObservingLog,
                observingLog,
                sessionReference,
                baseRangeMin,
                baseRangeMax,
                baseRmsMinor,
                baseRmsMajor,
                basePa,
                aborted,
                numAntenna,
                antennaId,
                sBSummaryId,
            ):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for ExecBlock (ExecBlockTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<ExecBlockTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:excblk="http://Alma/XASDM/ExecBlockTable" xsi:schemaLocation="http://Alma/XASDM/ExecBlockTable http://almaobservatory.org/XML/XASDM/4/ExecBlockTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</ExecBlockTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a ExecBlock (ExecBlockTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of ExecBlockTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "ExecBlockTable":
            raise ConversionException(
                "XML is not from a the expected table", "ExecBlockTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException(
                "schemaVersion not found in XML", "ExecBlockTable"
            )
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "ExecBlockTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "ExecBlockTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "ExecBlockTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "ExecBlockTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "ExecBlockTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "ExecBlockTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "ExecBlockTable") from None

                except ValueError as exc:
                    # TBD when this turns up via template
                    msg = (
                        "UniquenessViolationException in row in ExecBlockTable : %s"
                        % str(exc)
                    )

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "ExecBlockTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "ExecBlockTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a ExecBlockTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "ExecBlockTable",
            )

        if os.path.exists(os.path.join(directory, "ExecBlock.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "ExecBlock.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the ExecBlock table", "ExecBlockTable"
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
        with open(os.path.join(directory, "ExecBlock.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("ExecBlock.xml is empty", "ExecBlockTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'ExecBlock.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'ExecBlock.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (ExecBlock)"
                % directory,
                "ExecBlockTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for ExecBlock")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "ExecBlock.xml")
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
