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

# for BIN input and output
from pyasdm.ByteOrder import ByteOrder
from pyasdm.EndianInput import EndianInput
from pyasdm.EndianOutput import EndianOutput

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey
from .exceptions.UniquenessViolationException import UniquenessViolationException

from xml.dom import minidom

import os
import io


class ExecBlockTable:
    """
    The ExecBlockTable class is an Alma table.

    Characteristics of the Execution block.

    Shown here are the fields found in each row.

    The key fields are shown first and used (together) to index a unique row. Key fields
    are all required and indicated by "Key." following the description.

    Other fields are required unless "optional" is shown for that field.

    The field description text here is as found in the model used to generate the code.

    Types may be an enumeration or extended pyasdm type. Fields that are python lists
    are indicated that by "[]" in the type and having the word "Array" at the start of
    description followed by the expected number of elements in that list in parentheses.
    Lists (arrays) may be multi-dimensional (lists of lists) and are indicated
    by [][] ... etc as needed to indicate the expected number of
    dimensions. Multi-dimenstional lists will show the expected number of elements
    for each dimension also in the parenthese after "Array".

    The use of "auto-incrementable" indicates that that field is auto-generated
    when the table is created and that field is set, as necessary, to create a
    unique key for the specific row being added, by incrementing that value from
    the previous highest value needed for the rest of the elements of the key on
    that row. Such a field can not be set independently, it is only set when
    the row is added to the table by that auto-increment mechanism.

    Attributes:



        execBlockId (Tag): identifies a unique row in ExecBlock Table. auto-incrementable, key.





        startTime (ArrayTime): the start time of the execution block.

        endTime (ArrayTime): the end time of the execution block.

        execBlockNum (int): indicates the position of the execution block in the project (sequential numbering starting at 1).

        execBlockUID (EntityRef): the archive's UID of the execution block.

        projectUID (EntityRef): the archive's UID of the project.

        configName (str): the name of the array's configuration.

        telescopeName (str): the name of the telescope.

        observerName (str): the name of the observer.

        numObservingLog (int): the number of elements in the (array) attribute observingLog.

        observingLog (str [] ): Array(numObservingLog)  logs of the observation during this execution block.

        sessionReference (EntityRef): the observing session reference.

        baseRangeMin (Length): the length of the shortest baseline.

        baseRangeMax (Length): the length of the longest baseline.

        baseRmsMinor (Length): the minor axis of the representative ellipse of baseline lengths.

        baseRmsMajor (Length): the major axis of the representative ellipse of baseline lengths.

        basePa (Angle): the baselines position angle.

        aborted (bool): the execution block has been aborted (true) or has completed (false).

        numAntenna (int): the number of antennas.

        antennaId (Tag [] ): Array(numAntenna) refers to the relevant rows in AntennaTable.

        sBSummaryId (Tag): refers to a unique row  in SBSummaryTable.




        releaseDate (ArrayTime): the date when the data go to the public domain. Optional.

        schedulerMode (str): the mode of scheduling. Optional.

        siteAltitude (Length): the altitude of the site. Optional.

        siteLongitude (Angle): the longitude of the site. Optional.

        siteLatitude (Angle): the latitude of the site. Optional.

        observingScript (str): The text of the observation script. Optional.

        observingScriptUID (EntityRef): A reference to the Entity which contains the observing script. Optional.

        scaleId (Tag): refers to a unique row in the table Scale. Optional.


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
            # print("ExecBlock is not present in memory, setting from file")
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

    def __str__(self):
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
        homologues in x.  If a row is found that row else autoincrement x.execBlockId,
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

    def MIMEXMLPart(self, byteOrder):
        """
        Used in both the small XML file as well as the bin file when writing out as binary.
        The byte order is set by byteOrder.
        """
        uidStr = str(self.getEntity().getEntityId())
        withoutUID = uidStr[6:]
        containerUID = str(self.getContainer().getEntity().getEntityId())

        result = ""
        result += "<?xml version='1.0'  encoding='ISO-8859-1'?>"
        result += "\n"
        result += '<ExecBlockTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:excblk="http://Alma/XASDM/ExecBlockTable" xsi:schemaLocation="http://Alma/XASDM/ExecBlockTable http://almaobservatory.org/XML/XASDM/4/ExecBlockTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += "<Entity entityId='"
        result += uidStr
        result += "' entityIdEncrypted='na' entityTypeName='ExecBlockTable' schemaVersion='1' documentVersion='1'/>\n"
        result += "<ContainerEntity entityId='"
        result += containerUID
        result += "' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n"
        result += "<BulkStoreRef file_id='"
        result += withoutUID
        result += "' byteOrder='" + str(byteOrder) + "' />\n"
        result += "<Attributes>\n"

        result += "<execBlockId/>\n"
        result += "<startTime/>\n"
        result += "<endTime/>\n"
        result += "<execBlockNum/>\n"
        result += "<execBlockUID/>\n"
        result += "<projectUID/>\n"
        result += "<configName/>\n"
        result += "<telescopeName/>\n"
        result += "<observerName/>\n"
        result += "<numObservingLog/>\n"
        result += "<observingLog/>\n"
        result += "<sessionReference/>\n"
        result += "<baseRangeMin/>\n"
        result += "<baseRangeMax/>\n"
        result += "<baseRmsMinor/>\n"
        result += "<baseRmsMajor/>\n"
        result += "<basePa/>\n"
        result += "<aborted/>\n"
        result += "<numAntenna/>\n"
        result += "<antennaId/>\n"
        result += "<sBSummaryId/>\n"

        result += "<releaseDate/>\n"
        result += "<schedulerMode/>\n"
        result += "<siteAltitude/>\n"
        result += "<siteLongitude/>\n"
        result += "<siteLatitude/>\n"
        result += "<observingScript/>\n"
        result += "<observingScriptUID/>\n"
        result += "<scaleId/>\n"
        result += "</Attributes>\n"
        result += "</ExecBlockTable>\n"

        return result

    def toMIME(self, mimeFilePath, mimeXMLpart, byteOrder):
        """
        Write this out to mimeFilePath as a serialized MIME file with
        a leading XML part and a following binary part.

        The mimeXMLpart is a string that should have already been written
        to the corresponding small XML file (and is returned by the
        MIMEXMLPart method here). The byteOrder is a ByteOrder instance
        that gives the byte order to use when writing the binary data.
        That instance should have also been used to generate mimeXMLpart.
        """

        # mimeFilePath should have already been removed if it already existed.

        with open(mimeFilePath, "wb") as outBuffer:

            uidStr = str(self.getEntity().getEntityId())

            # The XML Header part.
            outBuffer.write(bytes("MIME-Version: 1.0", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(
                bytes(
                    "Content-Type: Multipart/Related; boundary='MIME_boundary'; type='text/xml'; start= '<header.xml>'",
                    "utf-8",
                )
            )
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-Description: Correlator", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("alma-uid:" + uidStr, "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))

            # The MIME XML part header.
            outBuffer.write(bytes("--MIME_boundary", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(
                bytes("Content-Type: text/xml; charset='ISO-8859-1'", "utf-8")
            )
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-Transfer-Encoding: 8bit", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-ID: <header.xml>", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))

            # The MIME XML part content.
            outBuffer.write(bytes(mimeXMLpart, "utf-8"))

            # The MIME binary part header
            outBuffer.write(bytes("--MIME_boundary", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-Type: binary/octet-stream", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-ID: <content.bin>", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))

            # The binary part, needs an EndianOutput instance

            eos = EndianOutput(outBuffer, byteOrder)
            self.getEntity().toBin(eos)
            self.getContainer().getEntity().toBin(eos)
            eos.writeInt(len(self._privateRows))

            # and all of the rows
            for thisRow in self._privateRows:
                thisRow.toBin(eos)

            # The closing MIME boundary
            outBuffer.write(bytes("\n--MIME_boundary--", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))

            # close the eos, also closes outBuffer, no penalty for doing that more than once
            eos.close()

    def setFromMIME(self, byteStream):
        """
        Extracts the binary part of a MIME message and deserialize its content
        to fill this with the result of the deserialization.
        param byteStream the previously opened io.BufferedReader instance
        containing the data to be extracted.

        It is the responsibility of this method to close byteStream.
        """

        if not (isinstance(byteStream, io.BufferedReader) and byteStream.seekable()):
            byteStream.close()
            raise ConversionException(
                "opened byteStream is not the expected io.BufferedReader or it is not seekable, this should never happen.",
                "ExecBlock",
            )

        xmlPartMIMEHeader = bytes(str("Content-ID: <header.xml>\n\n").encode())
        binPartMIMEHeader = bytes(
            str(
                "--MIME_boundary\nContent-Type: binary/octet-stream\nContent-ID: <content.bin>\n\n"
            ).encode()
        )

        # follow the Java example and grab the first 10000 bytes, which will always contain the header
        headerBytes = byteStream.read(10000)

        # Detect the XML header.
        loc0 = headerBytes.find(xmlPartMIMEHeader)
        # c++ code also looks for a string with an additional CRLF after each newline if the above fails, but Java
        # doesn't and even c++ doesn't follow that up when failing to find the binPartMIMEHeader, so go with the Java example
        if loc0 < 0:
            byteStream.close()
            raise ConversionException(
                "Failed to detect the begining of the XML header.", "ExecBlock"
            )

        loc0 += len(xmlPartMIMEHeader)

        # Look for the string announcing the binary part.
        loc1 = headerBytes.find(binPartMIMEHeader, loc0)
        if loc1 < 0:
            byteStream.close()
            raise ConversionException(
                "Failed to detect the begining of the binary part.", "ExecBlock"
            )

        # extract the XML header as a string
        xmlHeader = headerBytes[loc0:loc1].decode()

        xmldom = minidom.parseString(xmlHeader)
        if not xmldom.hasChildNodes():
            byteStream.close()
            raise ConversionException("XML is not properly structured.", "ExecBlock")

        attributesSeq = []
        byteOrderStr = None
        versionStr = "-1"

        hdrdom = xmldom.firstChild
        if hdrdom.nodeName == "ASDMBinaryTable":
            # old style of binary data
            # assume Big_Endian and the default order of the elements
            byteOrderStr = "Big_Endian"

            attributesSeq.append("execBlockId")

            attributesSeq.append("startTime")

            attributesSeq.append("endTime")

            attributesSeq.append("execBlockNum")

            attributesSeq.append("execBlockUID")

            attributesSeq.append("projectUID")

            attributesSeq.append("configName")

            attributesSeq.append("telescopeName")

            attributesSeq.append("observerName")

            attributesSeq.append("numObservingLog")

            attributesSeq.append("observingLog")

            attributesSeq.append("sessionReference")

            attributesSeq.append("baseRangeMin")

            attributesSeq.append("baseRangeMax")

            attributesSeq.append("baseRmsMinor")

            attributesSeq.append("baseRmsMajor")

            attributesSeq.append("basePa")

            attributesSeq.append("aborted")

            attributesSeq.append("numAntenna")

            attributesSeq.append("antennaId")

            attributesSeq.append("sBSummaryId")

            attributesSeq.append("releaseDate")

            attributesSeq.append("schedulerMode")

            attributesSeq.append("siteAltitude")

            attributesSeq.append("siteLongitude")

            attributesSeq.append("siteLatitude")

            attributesSeq.append("observingScript")

            attributesSeq.append("observingScriptUID")

            attributesSeq.append("scaleId")

            versionStr = "2"

        else:
            # c++ and Java just assume it then must be a ExecBlock table
            # this is more insistant, just in case
            if hdrdom.nodeName != "ExecBlockTable":
                byteStream.close()
                raise ConversionException(
                    "XML Header is not from the expected table.", "ExecBlock"
                )

            # schemaVersion becomes versionStr
            if (
                hdrdom.hasAttributes()
                and hdrdom.attributes.getNamedItem("schemaVersion") is not None
            ):
                versionStr = hdrdom.attributes.getNamedItem("schemaVersion").value

            if not hdrdom.hasChildNodes():
                byteStream.close()
                raise ConversionException(
                    "THe XML header is missing all of the expected elements.",
                    "ExecBlock",
                )

            # loop through the child nodes, looking for BulkStoreRef and Attributes
            for hdrnode in hdrdom.childNodes:
                if hdrnode.nodeName == "BulkStoreRef":
                    if byteOrderStr is not None:
                        byteStream.close()
                        raise ConversionException(
                            "More than one BulkStoreRef element seen. Invalid XML header.",
                            "ExecBlock",
                        )
                    if not hdrnode.hasAttributes():
                        byteStream.close()
                        raise ConversionException(
                            "BulkStoreRef does not contain any attributes. Invalid XML header.",
                            "ExecBlock",
                        )
                    byteOrderAttr = hdrnode.attributes.getNamedItem("byteOrder")
                    if byteOrderAttr is None:
                        byteStream.close()
                        raise ConversionException(
                            "byteOrder attribute not found in BulkStoreRef element. Invalid XML header.",
                            "ExecBlock",
                        )
                    byteOrderStr = byteOrderAttr.value
                elif hdrnode.nodeName == "Attributes":
                    if len(attributesSeq) > 0:
                        byteStream.close()
                        raise ConversionException(
                            "More than one Attributes node seen. Invalid XML header.",
                            "ExecBlock",
                        )
                    if not hdrnode.hasChildNodes():
                        byteStream.close()
                        raise ConversionException(
                            "Attributes element has no child nodes. Invalid XML header.",
                            "ExecBlock",
                        )
                    for attrnode in hdrnode.childNodes:
                        if attrnode.nodeType == attrnode.ELEMENT_NODE:
                            attributesSeq.append(str(attrnode.nodeName))

        if byteOrderStr is None:
            byteStream.close()
            raise ConversionException(
                "BulkStoreRef element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "ExecBlock",
            )

        if len(attributesSeq) == 0:
            byteStream.close()
            raise ConversionException(
                "Attributes element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "ExecBlock",
            )

        byteOrder = ByteOrder(byteOrderStr)

        # seek to the start of the binary part
        byteStream.seek(loc1 + len(binPartMIMEHeader))

        # and create the class that manages that stream and returns values as requested
        eis = EndianInput(byteStream, byteOrder)

        self._entity = Entity.fromBin(eis)

        # containerEntity is not used, but it is next
        containerEntity = Entity.fromBin(eis)

        # the number of rows
        numRows = eis.readInt()

        # c++ checks numRows against what is reported in the ASDM for this table, this is what Java does
        try:
            for i in range(numRows):
                self.checkAndAdd(ExecBlockRow.fromBin(eis, self, attributesSeq))
                # print("row %s added, loc = %s" % (i, eis.tell()))
        except Exception as exc:
            byteStream.close()
            eis.close()
            raise ConversionException(
                "Error while reading binary data, the exception was " + str(exc),
                "ExecBlock",
            ) from None

        # there is no harm in closing both
        # print("closing")
        eis.close()
        byteStream.close()
        # print("checking")
        # print("eis : %s" % eis.closed())
        # print("byteStream : %s" % byteStream.closed)

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
        Used internally by setFromFile. Not intended for external use.
        """
        # The java and c++ versions read all of the contents into a byte array.
        # This uses a buffered byte stream. Created here and then
        # handed off to the setFromMIME method, which is responsible for closing it.

        filename = os.path.join(directory, "ExecBlock.bin")
        byteStream = None
        try:
            byteStream = open(filename, "rb")
        except Exception as exc:
            raise ConversionException(
                "Error while opening " + filename + ". The exception was " + str(exc),
                "ExecBlock",
            )

        self.setFromMIME(byteStream)

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
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)

            # Java defaults to Big_Endian
            # c++ defaults to Machine, go with c++
            byteOrder = ByteOrder()

            # first, just the short XML file
            xmlFilePath = os.path.join(directory, "ExecBlock.xml")
            if os.path.exists(xmlFilePath):
                try:
                    os.remove(xmlFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + xmlFilePath
                        + ", exception caught "
                        + str(exc),
                        "ExecBlock",
                    ) from None

            # used in both files
            mimeXMLpart = self.MIMEXMLPart(byteOrder)

            # this is all that is written to the XML file
            with open(xmlFilePath, "w") as xmlfile:
                xmlfile.write(mimeXMLpart)

            # now open the possibly much longer MIME file
            mimeFilePath = os.path.join(directory, "ExecBlock.bin")
            if os.path.exists(mimeFilePath):
                try:
                    os.remove(mimeFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + mimeFilePath
                        + ", exception caught "
                        + str(exc),
                        "ExecBlock",
                    ) from None

            # the details are all handled in toMIME
            self.toMIME(mimeFilePath, mimeXMLpart, byteOrder)
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
