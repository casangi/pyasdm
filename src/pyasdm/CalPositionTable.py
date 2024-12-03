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
# File CalPositionTable.py
#

import pyasdm.ASDM

from .CalPositionRow import CalPositionRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class CalPositionTable(Representable):
    """
    The CalPositionTable class is an Alma table.

     Role
     Result of antenna positions calibration performed by TelCal.

     Generated from model's revision -1, branch

     Attributes of CalPosition

                  Key

    antennaName str the name of the antenna.

    atmPhaseCorrection AtmPhaseCorrection describes how the atmospheric phase correction has been applied.

    calDataId Tag refers to a unique row in CalData Table.

    calReductionId Tag refers to a unique row in CalReduction Table.



                  Value (Mandatory)

    startValidTime ArrayTime  the start time of result validity period.

    endValidTime ArrayTime  the end time of result validity period.

    antennaPosition Length []   3  the position of the antenna.

    stationName str  the name of the station.

    stationPosition Length []   3  the position of the station.

    positionMethod PositionMethod  identifies the method used for the position calibration.

    receiverBand ReceiverBand  identifies the receiver band.

    numAntenna int  the number of antennas of reference.

    refAntennaNames str []   numAntenna  the names of the antennas of reference (one string per antenna).

    axesOffset Length  the measured axe's offset.

    axesOffsetErr Length  the uncertainty on the determination of the axe's offset.

    axesOffsetFixed bool  the axe's offset was fixed (true) or not fixed (false).

    positionOffset Length []   3  the measured position offsets (a triple).

    positionErr Length []   3  the uncertainties on the measured position offsets (a triple).

    reducedChiSquared double  measures the quality of the fit.



                  Value (Optional)

    delayRms double  the RMS deviation for the observed delays.

    phaseRms Angle  the RMS deviation for the observed phases.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "CalPosition"

    # the list of field names that make up key 'key'.
    _key = ["antennaName", "atmPhaseCorrection", "calDataId", "calReductionId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = True  # if True archive binary else archive XML
    _fileAsBin = True  # if True file binary else file XML

    # A list to store the CalPositionRow instances
    _privateRows = []

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on antennaPosition during an add operation on the table
    _antennaPositionEqTolerance = Length(0.0)

    def setAntennaPositionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on antennaPosition
        """
        self._antennaPositionEqTolerance = Length(tolerance)

    # A getter for the tolerance on antennaPosition
    def getAntennaPositionEqTolerance(self):
        """
        A getter for the tolerance on antennaPosition
        """
        return self._antennaPositionEqTolerance

    # The tolerance which will be used on stationPosition during an add operation on the table
    _stationPositionEqTolerance = Length(0.0)

    def setStationPositionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on stationPosition
        """
        self._stationPositionEqTolerance = Length(tolerance)

    # A getter for the tolerance on stationPosition
    def getStationPositionEqTolerance(self):
        """
        A getter for the tolerance on stationPosition
        """
        return self._stationPositionEqTolerance

    # The tolerance which will be used on axesOffset during an add operation on the table
    _axesOffsetEqTolerance = Length(0.0)

    def setAxesOffsetEqTolerance(self, tolerance):
        """
        A setter for the tolerance on axesOffset
        """
        self._axesOffsetEqTolerance = Length(tolerance)

    # A getter for the tolerance on axesOffset
    def getAxesOffsetEqTolerance(self):
        """
        A getter for the tolerance on axesOffset
        """
        return self._axesOffsetEqTolerance

    # The tolerance which will be used on axesOffsetErr during an add operation on the table
    _axesOffsetErrEqTolerance = Length(0.0)

    def setAxesOffsetErrEqTolerance(self, tolerance):
        """
        A setter for the tolerance on axesOffsetErr
        """
        self._axesOffsetErrEqTolerance = Length(tolerance)

    # A getter for the tolerance on axesOffsetErr
    def getAxesOffsetErrEqTolerance(self):
        """
        A getter for the tolerance on axesOffsetErr
        """
        return self._axesOffsetErrEqTolerance

    # The tolerance which will be used on positionOffset during an add operation on the table
    _positionOffsetEqTolerance = Length(0.0)

    def setPositionOffsetEqTolerance(self, tolerance):
        """
        A setter for the tolerance on positionOffset
        """
        self._positionOffsetEqTolerance = Length(tolerance)

    # A getter for the tolerance on positionOffset
    def getPositionOffsetEqTolerance(self):
        """
        A getter for the tolerance on positionOffset
        """
        return self._positionOffsetEqTolerance

    # The tolerance which will be used on positionErr during an add operation on the table
    _positionErrEqTolerance = Length(0.0)

    def setPositionErrEqTolerance(self, tolerance):
        """
        A setter for the tolerance on positionErr
        """
        self._positionErrEqTolerance = Length(tolerance)

    # A getter for the tolerance on positionErr
    def getPositionErrEqTolerance(self):
        """
        A getter for the tolerance on positionErr
        """
        return self._positionErrEqTolerance

    # The tolerance which will be used on phaseRms during an add operation on the table
    _phaseRmsEqTolerance = Angle(0.0)

    def setPhaseRmsEqTolerance(self, tolerance):
        """
        A setter for the tolerance on phaseRms
        """
        self._phaseRmsEqTolerance = Angle(tolerance)

    # A getter for the tolerance on phaseRms
    def getPhaseRmsEqTolerance(self):
        """
        A getter for the tolerance on phaseRms
        """
        return self._phaseRmsEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    @staticmethod
    def Key(antennaName, atmPhaseCorrection, calDataId, calReductionId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        The parameter values are assumed to be the appropriate type for that parameter.
        """
        result = ""

        result += calDataId.toString() + "_"

        result += calReductionId.toString() + "_"

        return result

    def __init__(self, container):
        """
        Create a CalPositionTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("CalPositionTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("CalPositionTable")
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
        Returns "CalPositionTable" followed by the current size of the table
        between parenthesis.
        Example : CalPositionTable(12)
        """
        return "CalPositionTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = CalPositionRow(self)
        return thisRow

    def add(self, newrow):
        """
        Add a row.
        raises a DuplicateKey if the new row has a key that is already in the table.
        If newrow is a list then this method is called recursively on each element of that list.
        In that case None is returned.
        returns newrow
        """
        if isinstance(newrow, list):
            for thisrow in newrow:
                self.add(thisrow)
            # return None for the list case only
            return None

        # the single row case

        if (
            self.getRowByKey(
                newrow.getAntennaName(),
                newrow.getAtmPhaseCorrection(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey(
                "["
                + x.getAntennaName()
                + "|"
                + x.getAtmPhaseCorrection()
                + "|"
                + x.getCalDataId()
                + "|"
                + x.getCalReductionId()
                + "]",
                "CalPosition",
            )

        row.add(newrow)
        privateRows.add(newrow)
        newrow.isAdded()
        return newrow

    def newRow(
        self,
        antennaName,
        atmPhaseCorrection,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        antennaPosition,
        stationName,
        stationPosition,
        positionMethod,
        receiverBand,
        numAntenna,
        refAntennaNames,
        axesOffset,
        axesOffsetErr,
        axesOffsetFixed,
        positionOffset,
        positionErr,
        reducedChiSquared,
    ):
        """
        Create a new CalPositionRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = CalPositionRow(self)

        thisRow.setAntennaName(antennaName)

        thisRow.setAtmPhaseCorrection(atmPhaseCorrection)

        thisRow.setCalDataId(calDataId)

        thisRow.setCalReductionId(calReductionId)

        thisRow.setStartValidTime(startValidTime)

        thisRow.setEndValidTime(endValidTime)

        thisRow.setAntennaPosition(antennaPosition)

        thisRow.setStationName(stationName)

        thisRow.setStationPosition(stationPosition)

        thisRow.setPositionMethod(positionMethod)

        thisRow.setReceiverBand(receiverBand)

        thisRow.setNumAntenna(numAntenna)

        thisRow.setRefAntennaNames(refAntennaNames)

        thisRow.setAxesOffset(axesOffset)

        thisRow.setAxesOffsetErr(axesOffsetErr)

        thisRow.setAxesOffsetFixed(axesOffsetFixed)

        thisRow.setPositionOffset(positionOffset)

        thisRow.setPositionErr(positionErr)

        thisRow.setReducedChiSquared(reducedChiSquared)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new CalPositionRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new CalPositionRow with default values for its attributes.
        """

        return CalPositionRow(self, row)

    # ====> Append a row to its table.

    def _checkAndAdd(self, newrow):
        """
        A private method to append a row to its table, used by input conversion
        methods. Not intended for external use.

        If this table has an autoincrementable attribute then check if newrow verifies the rule of uniqueness and raise an exception if not.
        Returns newrow.
        """

        if (
            self.getRowByKey(
                newrow.getAntennaName(),
                newrow.getAtmPhaseCorrection(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey("Duplicate key exception in ", "CalPositionTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of CalPositionRow
        """
        return self._privateRows

    def getRowByKey(self, antennaName, atmPhaseCorrection, calDataId, calReductionId):
        """
        Returns a CalPositionRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        @param antennaName.

        @param atmPhaseCorrection.

        @param calDataId.

        @param calReductionId.

        """
        for row in self._privateRows:

            if row.getAntennaName() != antennaName:
                continue

            if row.getAtmPhaseCorrection() != atmPhaseCorrection:
                continue

            if not row.getCalDataId().equals(calDataId):
                continue

            if not row.getCalReductionId().equals(calReductionId):
                continue

            # this row matches these parameters
            return row
        # no match found
        return None

    def lookup(
        self,
        antennaName,
        atmPhaseCorrection,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        antennaPosition,
        stationName,
        stationPosition,
        positionMethod,
        receiverBand,
        numAntenna,
        refAntennaNames,
        axesOffset,
        axesOffsetErr,
        axesOffsetFixed,
        positionOffset,
        positionErr,
        reducedChiSquared,
    ):
        """
                Look up the table for a row whose all attributes
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param antennaName.

        param atmPhaseCorrection.

        param calDataId.

        param calReductionId.

        param startValidTime.

        param endValidTime.

        param antennaPosition.

        param stationName.

        param stationPosition.

        param positionMethod.

        param receiverBand.

        param numAntenna.

        param refAntennaNames.

        param axesOffset.

        param axesOffsetErr.

        param axesOffsetFixed.

        param positionOffset.

        param positionErr.

        param reducedChiSquared.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                antennaName,
                atmPhaseCorrection,
                calDataId,
                calReductionId,
                startValidTime,
                endValidTime,
                antennaPosition,
                stationName,
                stationPosition,
                positionMethod,
                receiverBand,
                numAntenna,
                refAntennaNames,
                axesOffset,
                axesOffsetErr,
                axesOffsetFixed,
                positionOffset,
                positionErr,
                reducedChiSquared,
            ):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for CalPosition (CalPositionTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<CalPositionTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clposn="http://Alma/XASDM/CalPositionTable" xsi:schemaLocation="http://Alma/XASDM/CalPositionTable http://almaobservatory.org/XML/XASDM/4/CalPositionTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</CalPositionTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a CalPosition (CalPositionTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of CalPositionTable.
        if (
            not xmldom.hasChildNodes()
            or xmldom.firstChild.nodeName != "CalPositionTable"
        ):
            raise ConversionException(
                "XML is not from a the expected table", "CalPositionTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException(
                "schemaVersion not found in XML", "CalPositionTable"
            )
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "CalPositionTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "CalPositionTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "CalPositionTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "CalPositionTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "CalPositionTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "CalPositionTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "CalPositionTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalPositionTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalPositionTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalPositionTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "CalPositionTable",
            )

        if os.path.exists(os.path.join(directory, "CalPosition.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalPosition.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalPosition table", "CalPositionTable"
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
        with open(os.path.join(directory, "CalPosition.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("CalPosition.xml is empty", "CalPositionTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'CalPosition.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'CalPosition.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalPosition)"
                % directory,
                "CalPositionTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for CalPosition")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "CalPosition.xml")
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
