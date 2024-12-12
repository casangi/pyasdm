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

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey
from .exceptions.UniquenessViolationException import UniquenessViolationException

from xml.dom import minidom

import os


class ExecBlockTable:
    """
    The ExecBlockTable class is an Alma table.

    Role
    Characteristics of the Execution block.

    Generated from model's revision -1, branch

    Attributes of ExecBlock

                 Key


    execBlockId Tag (auto-incrementable)     identifies a unique row in ExecBlock Table. </TD>




                 Value (Mandatory)

    startTime  ArrayTime  the start time of the execution block.

    endTime  ArrayTime  the end time of the execution block.

    execBlockNum  int  indicates the position of the execution block in the project (sequential numbering starting at 1).

    execBlockUID  EntityRef  the archive's UID of the execution block.

    projectUID  EntityRef  the archive's UID of the project.

    configName  str  the name of the array's configuration.

    telescopeName  str  the name of the telescope.

    observerName  str  the name of the observer.

    numObservingLog (numObservingLog) int  the number of elements in the (array) attribute observingLog.

    observingLog  str []   numObservingLog   logs of the observation during this execution block.

    sessionReference  EntityRef  the observing session reference.

    baseRangeMin  Length  the length of the shortest baseline.

    baseRangeMax  Length  the length of the longest baseline.

    baseRmsMinor  Length  the minor axis of the representative ellipse of baseline lengths.

    baseRmsMajor  Length  the major axis of the representative ellipse of baseline lengths.

    basePa  Angle  the baselines position angle.

    aborted  bool  the execution block has been aborted (true) or has completed (false).

    numAntenna (numAntenna) int  the number of antennas.

    antennaId  Tag []   numAntenna  refers to the relevant rows in AntennaTable.

    sBSummaryId  Tag  refers to a unique row  in SBSummaryTable.



                 Value (Optional)

    releaseDate  ArrayTime  the date when the data go to the public domain.

    schedulerMode  str  the mode of scheduling.

    siteAltitude  Length  the altitude of the site.

    siteLongitude  Angle  the longitude of the site.

    siteLatitude  Angle  the latitude of the site.

    observingScript  str  The text of the observation script.

    observingScriptUID  EntityRef  A reference to the Entity which contains the observing script.

    scaleId  Tag  refers to a unique row in the table Scale.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # The name of this table.
    _tableName = "ExecBlock"

    # The list of field names that make up key 'key'.
    _key = ["execBlockId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # archive as bin not used by python implementation
    # _archiveAsBin = False # If True archive binary else archive XML
    _fileAsBin = False  # If True file binary else file XML

    # A data structure to store the ExecBlockRow s.
    # In all cases we maintain a private list of ExecBlockRow s.
    _privateRows = []

    # non-temporal ASDM in Java had a private row element here to also hold  ExecBlockRow s. Not needed in python.

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
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._baseRangeMinEqTolerance = Length(tolerance)

    def getBaseRangeMinEqTolerance(self):
        """
        A getter for the tolerance on baseRangeMin
        Returns the tolerance as a  Length
        """
        return self._baseRangeMinEqTolerance

    # The tolerance which will be used on baseRangeMax during an add operation on the table
    _baseRangeMaxEqTolerance = Length(0.0)

    def setBaseRangeMaxEqTolerance(self, tolerance):
        """
        A setter for the tolerance on baseRangeMax
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._baseRangeMaxEqTolerance = Length(tolerance)

    def getBaseRangeMaxEqTolerance(self):
        """
        A getter for the tolerance on baseRangeMax
        Returns the tolerance as a  Length
        """
        return self._baseRangeMaxEqTolerance

    # The tolerance which will be used on baseRmsMinor during an add operation on the table
    _baseRmsMinorEqTolerance = Length(0.0)

    def setBaseRmsMinorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on baseRmsMinor
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._baseRmsMinorEqTolerance = Length(tolerance)

    def getBaseRmsMinorEqTolerance(self):
        """
        A getter for the tolerance on baseRmsMinor
        Returns the tolerance as a  Length
        """
        return self._baseRmsMinorEqTolerance

    # The tolerance which will be used on baseRmsMajor during an add operation on the table
    _baseRmsMajorEqTolerance = Length(0.0)

    def setBaseRmsMajorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on baseRmsMajor
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._baseRmsMajorEqTolerance = Length(tolerance)

    def getBaseRmsMajorEqTolerance(self):
        """
        A getter for the tolerance on baseRmsMajor
        Returns the tolerance as a  Length
        """
        return self._baseRmsMajorEqTolerance

    # The tolerance which will be used on basePa during an add operation on the table
    _basePaEqTolerance = Angle(0.0)

    def setBasePaEqTolerance(self, tolerance):
        """
        A setter for the tolerance on basePa
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._basePaEqTolerance = Angle(tolerance)

    def getBasePaEqTolerance(self):
        """
        A getter for the tolerance on basePa
        Returns the tolerance as a  Angle
        """
        return self._basePaEqTolerance

    # The tolerance which will be used on siteAltitude during an add operation on the table
    _siteAltitudeEqTolerance = Length(0.0)

    def setSiteAltitudeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on siteAltitude
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._siteAltitudeEqTolerance = Length(tolerance)

    def getSiteAltitudeEqTolerance(self):
        """
        A getter for the tolerance on siteAltitude
        Returns the tolerance as a  Length
        """
        return self._siteAltitudeEqTolerance

    # The tolerance which will be used on siteLongitude during an add operation on the table
    _siteLongitudeEqTolerance = Angle(0.0)

    def setSiteLongitudeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on siteLongitude
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._siteLongitudeEqTolerance = Angle(tolerance)

    def getSiteLongitudeEqTolerance(self):
        """
        A getter for the tolerance on siteLongitude
        Returns the tolerance as a  Angle
        """
        return self._siteLongitudeEqTolerance

    # The tolerance which will be used on siteLatitude during an add operation on the table
    _siteLatitudeEqTolerance = Angle(0.0)

    def setSiteLatitudeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on siteLatitude
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._siteLatitudeEqTolerance = Angle(tolerance)

    def getSiteLatitudeEqTolerance(self):
        """
        A getter for the tolerance on siteLatitude
        Returns the tolerance as a  Angle
        """
        return self._siteLatitudeEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up key key
        as a list of strings.
        """
        return self._key

    # a dictionary for the autoincrementation algorithm
    # the key is the key, excluding that auto-incrementable
    # the value is an integer that's the largest auto-incrementable for that key
    _noAutoIncIds = {}

    def autoIncrement(self, key, x):
        """
        For internal use.
        key is a key string
        x is a row.
        """
        if key not in self._noAutoIncIds:
            # There is not yet a combination of the non autoinc attributes values in the dict

            # Initialize  execBlockId to Tag(0).
            x.setExecBlockId(Tag(0, TagType.ExecBlock))

            # Record it in the dict.
            self._noAutoIncIds[key] = 0
        else:
            # There is already a combination of the non autoinc attributes values in the dict
            nextInt = int(self._noAutoIncIds[key]) + 1

            # Initialize  execBlockId to Tag(nextInt).
            x.setExecBlockId(Tag(nextInt, TagType.ExecBlock))

            # Record it in the hashtable.
            self._noAutoIncIds[key] = nextInt

    def __init__(self, container):
        """
        Create a ExecBlockTable attached to container.

        container must be a ASDM instance
        All tables must know the container
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

        self._privateRows = []

        self._noAutoIncIds = {}

        self._version = 0

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
        # NOTE: if setFromFile raises an exception then presentInMemory will remain False
        # and loadInProgress will remain True, preventing another attempt at loading.
        # more complex solutions are then necessary to read that file and it's not worth
        # complicating this code here to handle a need to eventually try again to reload that file
        if not self._presentInMemory and not self._loadInProgress:
            print("ExecBlock is not present in memory, setting from file")
            self._loadInProgress = True
            self.setFromFile(self.getContainer().getDirectory())
            self._presentInMemory = True
            self._loadInProgress = False

    def getContainer(self):
        """
        Return the container to which this table belongs.
        return a ASDM.
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

    def add(self, x):
        """
        Look up the table for a row whose noautoincrementable attributes are matching their
        homologues in x.  If a row is found that row else autoincrement x.\execBlockId,
        add x to its table and returns x.

        returns a ExecBlockRow.
        x. A row to be added.
        """
        if not isinstance(x, ExecBlockRow):
            raise ValueError("x must be a  ExecBlockRow instance.")

        aRow = self.lookup(
            x.getStartTime(),
            x.getEndTime(),
            x.getExecBlockNum(),
            x.getExecBlockUID(),
            x.getProjectUID(),
            x.getConfigName(),
            x.getTelescopeName(),
            x.getObserverName(),
            x.getNumObservingLog(),
            x.getObservingLog(),
            x.getSessionReference(),
            x.getBaseRangeMin(),
            x.getBaseRangeMax(),
            x.getBaseRmsMinor(),
            x.getBaseRmsMajor(),
            x.getBasePa(),
            x.getAborted(),
            x.getNumAntenna(),
            x.getAntennaId(),
            x.getSBSummaryId(),
        )
        if aRow is not None:
            return aRow

        # Autoincrement execBlockId
        x.setExecBlockId(Tag(self.size(), TagType.ExecBlock))

        self._privateRows.add(x)
        x.isAdded()
        return x

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
        Create a new ExecBlockRow initialized to the specified values.

        The new row is not added to this table, but it does know about it.
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

    def checkAndAdd(self, x):
        """
        A method to append a row to it's table, used by input conversion methods.
        Not indended for external use.

        If this table has an autoincrementable attribute then check if
        x verifies the rule of uniqueness and raise an exception if not.

        Append x to its table.
        x is the row to be appended.
        returns x.
        """

        if (
            self.lookup(
                x.getStartTime(),
                x.getEndTime(),
                x.getExecBlockNum(),
                x.getExecBlockUID(),
                x.getProjectUID(),
                x.getConfigName(),
                x.getTelescopeName(),
                x.getObserverName(),
                x.getNumObservingLog(),
                x.getObservingLog(),
                x.getSessionReference(),
                x.getBaseRangeMin(),
                x.getBaseRangeMax(),
                x.getBaseRmsMinor(),
                x.getBaseRmsMajor(),
                x.getBasePa(),
                x.getAborted(),
                x.getNumAntenna(),
                x.getAntennaId(),
                x.getSBSummaryId(),
            )
            is not None
        ):
            raise UniquenessViolationException(
                "Uniqueness violation exception in table ExecBlockTable"
            )

        if self.getRowByKey(x.getExecBlockId()) is not None:
            raise DuplicateKey("Duplicate key exception in ", "ExecBlockTable")

        self._privateRows.append(x)
        x.isAdded()
        return x

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows.
        return Alls rows as a list of ExecBlockRow
        """
        return self._privateRows

    def getRowByKey(self, execBlockId):
        """
        Returns a ExecBlockRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        param execBlockId.

        """
        for row in self._privateRows:

            if not row.getExecBlockId().equals(execBlockId):
                continue

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

    def getRows(self):
        """
        get the rows, synonymous with the get method.
        """
        return self.get()

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for ExecBlock (ExecBlockTable.xsd).

        returns a string containing the XML representation.
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
        if not isinstance(xmlstr, str):
            raise ConversionException("xmlstr must be a string")

        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of "ExecBlockTable".
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "ExecBlockTable":
            raise ConversionException(
                "XML is not from the expected table", "ExecBlockTable"
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which is not always there
        versionStr = "-1"
        if tabdom.hasAttributes() and (
            tabdom.attributes.getNamedItem("schemaVersion") is not None
        ):
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
                    self.checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str(exc), "ExecBlockTable") from None

                except UniquenessViolationException as exc:
                    msg = (
                        "UniquenessViolationException in row in ExecBlockTable : %s"
                        % str(exc)
                    )

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "ExecBlockTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "ExecBlockTable")

        self.setEntity(tabEntity)

    def MIMEXMLPart(self):
        print("MIMEXMLPart not implemented for <ExecBlockTable")
        return
        # the JAVA code looks like this
        # String UID = this.getEntity().getEntityId().toString();
        # String withoutUID = UID.substring(6);
        # String containerUID = this.getContainer().getEntity().getEntityId().toString();
        #
        # StringBuffer sb = new StringBuffer()
        # .append("<?xml version='1.0'  encoding='ISO-8859-1'?>")
        # .append("\n")
        # .append("<ExecBlockTable xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:excblk=\"http://Alma/XASDM/ExecBlockTable\" xsi:schemaLocation=\"http://Alma/XASDM/ExecBlockTable http://almaobservatory.org/XML/XASDM/4/ExecBlockTable.xsd\" schemaVersion=\"4\" schemaRevision=\"-1\">\n")
        # .append("<Entity entityId='")
        # .append(UID)
        # .append("' entityIdEncrypted='na' entityTypeName='ExecBlockTable' schemaVersion='1' documentVersion='1'/>\n")
        # .append("<ContainerEntity entityId='")
        # .append(containerUID)
        # .append("' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n")
        # .append("<BulkStoreRef file_id='")
        # .append(withoutUID)
        # .append("' byteOrder='Big_Endian' />\n")
        # .append("<Attributes>\n")

        # .append("<execBlockId/>\n")
        # .append("<startTime/>\n")
        # .append("<endTime/>\n")
        # .append("<execBlockNum/>\n")
        # .append("<execBlockUID/>\n")
        # .append("<projectUID/>\n")
        # .append("<configName/>\n")
        # .append("<telescopeName/>\n")
        # .append("<observerName/>\n")
        # .append("<numObservingLog/>\n")
        # .append("<observingLog/>\n")
        # .append("<sessionReference/>\n")
        # .append("<baseRangeMin/>\n")
        # .append("<baseRangeMax/>\n")
        # .append("<baseRmsMinor/>\n")
        # .append("<baseRmsMajor/>\n")
        # .append("<basePa/>\n")
        # .append("<aborted/>\n")
        # .append("<numAntenna/>\n")
        # .append("<antennaId/>\n")
        # .append("<sBSummaryId/>\n")

        # .append("<releaseDate/>\n")
        # .append("<schedulerMode/>\n")
        # .append("<siteAltitude/>\n")
        # .append("<siteLongitude/>\n")
        # .append("<siteLatitude/>\n")
        # .append("<observingScript/>\n")
        # .append("<observingScriptUID/>\n")
        # .append("<scaleId/>\n")
        # .append("</Attributes>\n")
        # .append("</ExecBlockTable>\n");
        # return sb.toString();

    def toMIME(self):
        """
        Serialize this into a stream of bytes and encapsulates that stream into a MIME message.
        returns a string containing the MIME message.
        """
        print("toMIME not yet implemented for ExecBlock")
        return
        # the Java code looks like this - returns a Byte array
        # ByteArrayOutputStream bos = new ByteArrayOutputStream();
        # DataOutputStream dos = new DataOutputStream(bos);

        # String UID = this.getEntity().getEntityId().toString();
        # String execBlockUID = this.getContainer().getEntity().getEntityId().toString();
        # try {
        #     // The XML Header part.
        #     dos.writeBytes("MIME-Version: 1.0");
        #     dos.writeBytes("\n");
        #    dos
        #     .writeBytes("Content-Type: Multipart/Related; boundary='MIME_boundary'; type='text/xml'; start= '<header.xml>'");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-Description: Correlator");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("alma-uid:" + UID);
        #    dos.writeBytes("\n");
        #    dos.writeBytes("\n");
        #
        #    // The MIME XML part header.
        #    dos.writeBytes("--MIME_boundary");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-Type: text/xml; charset='ISO-8859-1'");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-Transfer-Encoding: 8bit");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-ID: <header.xml>");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("\n");
        #
        #    // The MIME XML part content.
        #    dos.writeBytes(MIMEXMLPart());
        #    // have updated their code to the new XML header.
        #    //
        #    //dos.writeBytes(oldMIMEXMLPart());
        #
        #    // The MIME binary part header
        #    dos.writeBytes("--MIME_boundary");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-Type: binary/octet-stream");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-ID: <content.bin>");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("\n");
        #
        #    // The binary part.
        #    entity.toBin(dos);
        #    container.getEntity().toBin(dos);
        #    dos.writeInt(size());

        #    for (ExecBlockRow row: privateRows) row.toBin(dos);

        #    // The closing MIME boundary
        #    dos.writeBytes("\n--MIME_boundary--");
        #    dos.writeBytes("\n");

        # } catch (IOException e) {
        #    throw new ConversionException(
        #            "Error while reading binary data , the message was "
        #            + e.getMessage(), "ExecBlock");
        # }

        # return bos.toByteArray();

    # Java code looks like this
    # static private boolean binaryPartFound(DataInputStream dis, String s, int pos) throws IOException {
    #    int posl = pos;
    #    int count = 0;
    #    dis.mark(1000000);
    #    try {
    #        while (dis.readByte() != s.charAt(posl)){
    #            count ++;
    #        }
    #    }
    #    catch (EOFException e) {
    #        return false;
    #    }
    #
    #    if (posl == (s.length() - 1)) return true;
    #
    #    if (pos == 0) {
    #        posl++;
    #        return binaryPartFound(dis, s, posl);
    #    }
    #    else {
    #        if (count > 0) { dis.reset();  return binaryPartFound(dis, s, 0) ; }
    #        else {
    #            posl++;
    #            return binaryPartFound(dis, s, posl);
    #        }
    #    }
    # }

    # private String xmlHeaderPart (String s) throws ConversionException {
    #    String xmlPartMIMEHeader = "Content-ID: <header.xml>\n\n";
    #    String binPartMIMEHeader = "--MIME_boundary\nContent-Type: binary/octet-stream\nContent-ID: <content.bin>\n\n";
    #
    #    // Detect the XML header.
    #    int loc0 = s.indexOf(xmlPartMIMEHeader);
    #    if (loc0 == -1 ) throw new ConversionException("Failed to detect the beginning of the XML header", "ExecBlock");
    #
    #    loc0 += xmlPartMIMEHeader.length();
    #
    #    // Look for the string announcing the binary part.
    #    int loc1 = s.indexOf(binPartMIMEHeader, loc0);
    #    if (loc1 == -1) throw new ConversionException("Failed to detect the beginning of the binary part", "ExecBlock");
    #
    #    return s.substring(loc0, loc1).trim();
    # }

    # setFromMIME(byte[]   data) throws ConversionException {
    # *
    # Extracts the binary part of a MIME message and deserialize its content
    # to fill this with the result of the deserialization.
    # @param data the string containing the MIME message.
    # @throws ConversionException
    # /
    # ByteOrder byteOrder = null;
    # //
    # // Look for the part containing the XML header.
    # // Very empirically we assume that the first MIME part , the one which contains the
    # // XML header, always fits in the first 1000 bytes of the MIME message !!
    # //
    # String header = xmlHeaderPart(new String(data, 0, Math.min(10000, data.length)));
    # org.jdom.Document document = null;
    # SAXBuilder sxb = new SAXBuilder();
    #
    # // Firstly build a document out of the XML.
    # try {
    #    document = sxb.build(new ByteArrayInputStream(header.getBytes()));
    # }
    # catch (Exception e) {
    #     throw new ConversionException(e.getMessage(), "ExecBlock");
    # }
    #
    # //
    # // Let's define a default order for the sequence of attributes.
    # //
    # ArrayList<String> attributesSeq = new ArrayList<String> ();

    #     attributesSeq.add("execBlockId"); attributesSeq.add("startTime"); attributesSeq.add("endTime"); attributesSeq.add("execBlockNum"); attributesSeq.add("execBlockUID"); attributesSeq.add("projectUID"); attributesSeq.add("configName"); attributesSeq.add("telescopeName"); attributesSeq.add("observerName"); attributesSeq.add("numObservingLog"); attributesSeq.add("observingLog"); attributesSeq.add("sessionReference"); attributesSeq.add("baseRangeMin"); attributesSeq.add("baseRangeMax"); attributesSeq.add("baseRmsMinor"); attributesSeq.add("baseRmsMajor"); attributesSeq.add("basePa"); attributesSeq.add("aborted"); attributesSeq.add("numAntenna"); attributesSeq.add("antennaId"); attributesSeq.add("sBSummaryId");
    #     attributesSeq.add("releaseDate");  attributesSeq.add("schedulerMode");  attributesSeq.add("siteAltitude");  attributesSeq.add("siteLongitude");  attributesSeq.add("siteLatitude");  attributesSeq.add("observingScript");  attributesSeq.add("observingScriptUID");  attributesSeq.add("scaleId");

    # XPath xpath = null;
    # //
    # // And then look for the possible XML contents.
    # try {
    #     // Is it an "<ASDMBinaryTable ...." document (old) ?
    #    if (XPath.newInstance("/ASDMBinaryTable")
    #            .selectSingleNode(document) != null)
    #        byteOrder = ByteOrder.BIG_ENDIAN;
    #    else {
    #        // Then it must be a "<ExecBlockTable ...." document
    #        // With a BulkStoreRef child element....
    #        XPath xpa = XPath.newInstance("/ExecBlockTable/BulkStoreRef/@byteOrder");
    #        Object node = xpa.selectSingleNode(document.getRootElement());
    #        if (node == null)
    #            throw new ConversionException("No element found for the XPath expression '/ExecBlockTable/BulkStoreRef/@byteOrder'. Invalid XML header '"+header+"'.", "ExecBlock");
    #
    #        // Yes ? then it must have a "BulkStoreRef" element with a
    #        // "byteOrder" attribute.
    #        String bo = xpa.valueOf(document.getRootElement());
    #        if (bo.equals("Little_Endian"))
    #            byteOrder = ByteOrder.LITTLE_ENDIAN;
    #        else if (bo.equals("Big_Endian"))
    #            byteOrder = ByteOrder.BIG_ENDIAN;
    #        else
    #            throw new ConversionException("No valid value retrieved for the node '/ExecBlockTable/BulkStoreRef/@byteOrder'. Invalid XML header '"+header+"'.", "ExecBlock");
    #
    #        // And also it must have an Attributes element with children.
    #        xpa = XPath.newInstance("/ExecBlockTable/Attributes#");
    #        List nodes = xpa.selectNodes(document.getRootElement());
    #        if (nodes==null || nodes.size()==0)
    #            throw new ConversionException("No element found for the XPath expression '/ExecBlockTable/Attributes#'. Invalid XML header '"+header+"'.", "ExecBlock");
    #
    #        Iterator iter = nodes.iterator();
    #        attributesSeq.clear();
    #        int i = 0;
    #        while (iter.hasNext()){
    #            attributesSeq.add(((Element) iter.next()).getName());
    #            i += 1;
    #        }
    #    }
    # } catch (Exception e) {
    #    throw new ConversionException(e.getMessage(), "ExecBlock");
    # }

    # //
    # // Now that we know what is the byte order of the binary data
    # // Let's extract them from the second MIME part and parse them
    # //
    # ByteArrayInputStream bis = new ByteArrayInputStream(data);
    # DataInputStream dis = new DataInputStream(bis);
    # BODataInputStream bodis = new BODataInputStream(dis, byteOrder);
    #
    # String terminator = "Content-Type: binary/octet-stream\nContent-ID: <content.bin>\n\n";
    # entity = null;
    # try {
    #    if (binaryPartFound(dis, terminator, 0) == false) {
    #        throw new ConversionException ("Failed to detect the beginning of the binary part", "ExecBlock");
    #    }
    #
    #    entity = Entity.fromBin(bodis);
    #
    #    Entity containerEntity = Entity.fromBin(bodis);
    #
    #    int numRows = bodis.readInt();
    #    for (int i = 0; i < numRows; i++) {
    #    this.checkAndAdd(ExecBlockRow.fromBin(bodis, this, attributesSeq.toArray(new String[0])));
    #    }
    # } catch (TagFormatException e) {
    #    throw new ConversionException( "Error while reading binary data , the message was "
    #        + e.getMessage(), "ExecBlock");
    # }catch (IOException e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "ExecBlock");
    # } catch (DuplicateKey e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "ExecBlock");
    # }catch (Exception e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "ExecBlock");
    # }
    # }

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a ExecBlockTable as those produced  by the toFile method.
        This table is populated with the result of the parsing.
        param directory The name of the directory containing the file te be read and parsed.
        raises ConversionException If any error occurs while reading the
        files in the directory or parsing them.
        """
        if not isinstance(directory, str):
            print("directory must be a string")

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "ExecBlockTable",
            )

        if os.path.exists(os.path.join(directory, "ExecBlock.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "ExecBlock.bin")):
            self.setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the ExecBlock table", "ExecBlockTable"
            )

    def setFromMIMEFile(self, directory):
        """
        Set this table from a MIME file.
        Used internally by setFromFile. Not intented for external use.
        """
        print("setFromMIME file not yet implemented for ExecBlockTable")
        return

        # java code looks like this
        # File file = new File(directory+"/ExecBlock.bin");
        #
        # byte[] bytes = null;
        #
        # try {
        #     InputStream is = new FileInputStream(file);
        #     long length = file.length();
        #     if (length > Integer.MAX_VALUE)
        #         throw new ConversionException ("File " + file.getName() + " is too large", "ExecBlock");
        #
        #    bytes = new byte[(int)length];
        #    int offset = 0;
        #    int numRead = 0;
        #
        #   while (offset < bytes.length && (numRead=is.read(bytes, offset, bytes.length-offset)) >= 0) {
        #       offset += numRead;
        #   }
        #
        #    if (offset < bytes.length) {
        #        throw new ConversionException("Could not completely read file "+file.getName(), "ExecBlock");
        #    }
        #    is.close();
        # }
        # catch (IOException e) {
        #    throw new ConversionException("Error while reading "+file.getName()+". The message was " + e.getMessage(),
        #    "ExecBlock");
        # }

        # setFromMIME(bytes);
        # // Changed 24 Sep, 2015 - The export policy cannot be changed by what has been observed at import time. M Caillat
        # // archiveAsBin = true;
        # // fileAsBin = true;

    # }

    def setFromXMLFile(self, directory):
        """
        This is the function used by setFromFile when the file is an XML file
        Not intended for external use.
        """

        # setFromFile has already established that this exists
        # read the entire file into a string
        xmlstr = None
        try:
            with open(os.path.join(directory, "ExecBlock.xml")) as f:
                xmlstr = f.read()
        except Exception as exc:
            # reraise it as a ConversionException
            raise ConversionException(str(exc), "ExecBlockTable") from None

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)
            # TBD: when fileAsBin is implemented this should be removed
            # this will at least preserve the case where fileAsBin was changed for
            # a table such that the archive has it in XML but the current rule is to
            # write it out as binary
            if self._fileAsBin:
                print(
                    "ExecBlock found as XML but it should be written as binary, which is not yet implemetned. Setting to write as XML to preserve this content."
                )
                self._fileAsBin = False

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of its _fileAsBin data member a binary serialization
        of this (_fileAsBin==True) will be saved in a file "ExecBlock.bin" or
        an XML representation (_fileAsBin==False) will be saved in a file "ExecBlock.xml".
        The file is always written in a directory whose name is passed as a parameter.
        param directory The name of directory where the file containing the table's
        representation will be saved.
        raises ConversionException for any errors while writing that file.
        """
        if not isinstance(directory, str):
            raise ConversionException("directory must be a string")

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (ExecBlock)"
                % directory,
                "ExecBlockTable",
            )

        # if not let's create it.
        try:
            if not os.path.exists(directory):
                # if it can't be created a FileNotFound exception is the most likely result
                os.mkdir(directory)
        except Exception as exc:
            # reraise any exception as a ConversionException
            raise ConversionException(
                "Could not create directory "
                + directory
                + " exception caught "
                + str(exc),
                "ExecBlockTable",
            ) from None

        if self._fileAsBin:
            print("fileAsBin not yet implemented for ExecBlock")
            # the Java code looks like this
            #
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)
            #
            # File xmlFile = new File(directory+"/ExecBlock.xml");
            # if (xmlFile.exists())
            #    if (!xmlFile.delete())
            #        throw new ConversionException("Problem while trying to delete a previous version of '"+xmlFile.toString()+"'", "ExecBlock");
            #
            # File binFile = new File(directory+"/ExecBlock.bin");
            # if (binFile.exists())
            #    if (!binFile.delete())
            #        throw new ConversionException("Problem while trying to delete a previous version of '"+binFile.toString()+"'", "ExecBlock");
            #
            # try {
            #    BufferedWriter out = new BufferedWriter(new FileWriter(xmlFile));
            #    out.write(MIMEXMLPart());
            #    out.close();
            #

            #  OutputStream osBin = new FileOutputStream(binFile);
            #  osBin.write(toMIME());
            #  osBin.close();

        # }
        # catch (FileNotFoundException e) {
        #     throw new ConversionException("Problem while writing the binary representation, the message was : " + e.getMessage(), "ExecBlock");
        # }
        # catch (IOException e) {
        #      throw new ConversionException("Problem while writing the binary representation, the message was : " + e.getMessage(), "ExecBlock");
        # }
        # }
        else:
            # The table is totally exported in a XML file.
            filePath = os.path.join(directory, "ExecBlock.xml")
            if os.path.exists(filePath):
                try:
                    # try to delete it, this will raise an exception if the user does not have permission to do that
                    os.remove(filePath)
                except Exception as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(
                        "Could not remove existing "
                        + filePath
                        + " exception caught "
                        + str(exc),
                        "ExecBlockTable",
                    ) from None

            try:
                with open(filePath, "w") as f:
                    f.write(self.toXML())
                    f.close()

                    # Java code uses a BufferedWriter to capture the output of toXML to the file
            except Exception as exc:
                # reraise it as a ConversionException
                raise ConversionException(
                    "Problem while writing the XML representation, the message was : "
                    + str(exc),
                    "ExecBlock",
                ) from None

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
