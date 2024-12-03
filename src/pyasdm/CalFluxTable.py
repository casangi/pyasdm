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
# File CalFluxTable.py
#

import pyasdm.ASDM

from .CalFluxRow import CalFluxRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class CalFluxTable(Representable):
    """
    The CalFluxTable class is an Alma table.

     Role
     Result of flux calibration performed on-line by TelCal. Atmospheric absorption is corrected for. No ionosphere correction has been applied.

     Generated from model's revision -1, branch

     Attributes of CalFlux

                  Key

    sourceName str the name of the source.

    calDataId Tag refers to a unique row in CalData Table.

    calReductionId Tag refers to a unique row in CalReduction Table.



                  Value (Mandatory)

    startValidTime ArrayTime  the start time of result validity period.

    endValidTime ArrayTime  the end time of result validity period.

    numFrequencyRanges int  the number of frequency ranges.

    numStokes int  the number of Stokes parameters.

    frequencyRanges Frequency []  []   numFrequencyRanges, 2  the frequency ranges (one pair of values per range).

    fluxMethod FluxCalibrationMethod  identifies the flux determination method.

    flux double []  []   numStokes, numFrequencyRanges  the flux densities (one value par Stokes parameter per frequency range) expressed in Jansky (Jy).

    fluxError double []  []   numStokes, numFrequencyRanges  the uncertainties on the flux densities (one value per Stokes parameter per frequency range).

    stokes StokesParameter []   numStokes  the Stokes parameter.



                  Value (Optional)

    direction Angle []   2  the direction of the source.

    directionCode DirectionReferenceCode  identifies the reference frame of the source's direction.

    directionEquinox Angle  equinox associated with the reference frame of the source's direction.

    PA Angle []  []   numStokes, numFrequencyRanges  the position's angles for the source model (one value per Stokes parameter per frequency range).

    PAError Angle []  []   numStokes, numFrequencyRanges  the uncertainties on the position's angles (one value per Stokes parameter per frequency range).

    size Angle []  []  []   numStokes, numFrequencyRanges, 2  the sizes of the source (one pair of angles per Stokes parameter per frequency range).

    sizeError Angle []  []  []   numStokes, numFrequencyRanges, 2  the uncertainties of the sizes of the source (one pair of angles per Stokes parameter per frequency range).

    sourceModel SourceModel  identifies the source model.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "CalFlux"

    # the list of field names that make up key 'key'.
    _key = ["sourceName", "calDataId", "calReductionId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = True  # if True archive binary else archive XML
    _fileAsBin = True  # if True file binary else file XML

    # A list to store the CalFluxRow instances
    _privateRows = []

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on frequencyRanges during an add operation on the table
    _frequencyRangesEqTolerance = Frequency(0.0)

    def setFrequencyRangesEqTolerance(self, tolerance):
        """
        A setter for the tolerance on frequencyRanges
        """
        self._frequencyRangesEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on frequencyRanges
    def getFrequencyRangesEqTolerance(self):
        """
        A getter for the tolerance on frequencyRanges
        """
        return self._frequencyRangesEqTolerance

    # The tolerance which will be used on direction during an add operation on the table
    _directionEqTolerance = Angle(0.0)

    def setDirectionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on direction
        """
        self._directionEqTolerance = Angle(tolerance)

    # A getter for the tolerance on direction
    def getDirectionEqTolerance(self):
        """
        A getter for the tolerance on direction
        """
        return self._directionEqTolerance

    # The tolerance which will be used on directionEquinox during an add operation on the table
    _directionEquinoxEqTolerance = Angle(0.0)

    def setDirectionEquinoxEqTolerance(self, tolerance):
        """
        A setter for the tolerance on directionEquinox
        """
        self._directionEquinoxEqTolerance = Angle(tolerance)

    # A getter for the tolerance on directionEquinox
    def getDirectionEquinoxEqTolerance(self):
        """
        A getter for the tolerance on directionEquinox
        """
        return self._directionEquinoxEqTolerance

    # The tolerance which will be used on PA during an add operation on the table
    _PAEqTolerance = Angle(0.0)

    def setPAEqTolerance(self, tolerance):
        """
        A setter for the tolerance on PA
        """
        self._PAEqTolerance = Angle(tolerance)

    # A getter for the tolerance on PA
    def getPAEqTolerance(self):
        """
        A getter for the tolerance on PA
        """
        return self._PAEqTolerance

    # The tolerance which will be used on PAError during an add operation on the table
    _PAErrorEqTolerance = Angle(0.0)

    def setPAErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on PAError
        """
        self._PAErrorEqTolerance = Angle(tolerance)

    # A getter for the tolerance on PAError
    def getPAErrorEqTolerance(self):
        """
        A getter for the tolerance on PAError
        """
        return self._PAErrorEqTolerance

    # The tolerance which will be used on size during an add operation on the table
    _sizeEqTolerance = Angle(0.0)

    def setSizeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on size
        """
        self._sizeEqTolerance = Angle(tolerance)

    # A getter for the tolerance on size
    def getSizeEqTolerance(self):
        """
        A getter for the tolerance on size
        """
        return self._sizeEqTolerance

    # The tolerance which will be used on sizeError during an add operation on the table
    _sizeErrorEqTolerance = Angle(0.0)

    def setSizeErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on sizeError
        """
        self._sizeErrorEqTolerance = Angle(tolerance)

    # A getter for the tolerance on sizeError
    def getSizeErrorEqTolerance(self):
        """
        A getter for the tolerance on sizeError
        """
        return self._sizeErrorEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    @staticmethod
    def Key(sourceName, calDataId, calReductionId):
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
        Create a CalFluxTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("CalFluxTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("CalFluxTable")
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
        Returns "CalFluxTable" followed by the current size of the table
        between parenthesis.
        Example : CalFluxTable(12)
        """
        return "CalFluxTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = CalFluxRow(self)
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
                newrow.getSourceName(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey(
                "["
                + x.getSourceName()
                + "|"
                + x.getCalDataId()
                + "|"
                + x.getCalReductionId()
                + "]",
                "CalFlux",
            )

        row.add(newrow)
        privateRows.add(newrow)
        newrow.isAdded()
        return newrow

    def newRow(
        self,
        sourceName,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numFrequencyRanges,
        numStokes,
        frequencyRanges,
        fluxMethod,
        flux,
        fluxError,
        stokes,
    ):
        """
        Create a new CalFluxRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = CalFluxRow(self)

        thisRow.setSourceName(sourceName)

        thisRow.setCalDataId(calDataId)

        thisRow.setCalReductionId(calReductionId)

        thisRow.setStartValidTime(startValidTime)

        thisRow.setEndValidTime(endValidTime)

        thisRow.setNumFrequencyRanges(numFrequencyRanges)

        thisRow.setNumStokes(numStokes)

        thisRow.setFrequencyRanges(frequencyRanges)

        thisRow.setFluxMethod(fluxMethod)

        thisRow.setFlux(flux)

        thisRow.setFluxError(fluxError)

        thisRow.setStokes(stokes)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new CalFluxRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new CalFluxRow with default values for its attributes.
        """

        return CalFluxRow(self, row)

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
                newrow.getSourceName(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey("Duplicate key exception in ", "CalFluxTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of CalFluxRow
        """
        return self._privateRows

    def getRowByKey(self, sourceName, calDataId, calReductionId):
        """
        Returns a CalFluxRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        @param sourceName.

        @param calDataId.

        @param calReductionId.

        """
        for row in self._privateRows:

            if row.getSourceName() != sourceName:
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
        sourceName,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numFrequencyRanges,
        numStokes,
        frequencyRanges,
        fluxMethod,
        flux,
        fluxError,
        stokes,
    ):
        """
                Look up the table for a row whose all attributes
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param sourceName.

        param calDataId.

        param calReductionId.

        param startValidTime.

        param endValidTime.

        param numFrequencyRanges.

        param numStokes.

        param frequencyRanges.

        param fluxMethod.

        param flux.

        param fluxError.

        param stokes.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                sourceName,
                calDataId,
                calReductionId,
                startValidTime,
                endValidTime,
                numFrequencyRanges,
                numStokes,
                frequencyRanges,
                fluxMethod,
                flux,
                fluxError,
                stokes,
            ):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for CalFlux (CalFluxTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<CalFluxTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clflx="http://Alma/XASDM/CalFluxTable" xsi:schemaLocation="http://Alma/XASDM/CalFluxTable http://almaobservatory.org/XML/XASDM/4/CalFluxTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</CalFluxTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a CalFlux (CalFluxTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of CalFluxTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "CalFluxTable":
            raise ConversionException(
                "XML is not from a the expected table", "CalFluxTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException("schemaVersion not found in XML", "CalFluxTable")
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "CalFluxTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "CalFluxTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "CalFluxTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "CalFluxTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "CalFluxTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "CalFluxTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "CalFluxTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalFluxTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalFluxTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalFluxTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "CalFluxTable",
            )

        if os.path.exists(os.path.join(directory, "CalFlux.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalFlux.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalFlux table", "CalFluxTable"
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
        with open(os.path.join(directory, "CalFlux.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("CalFlux.xml is empty", "CalFluxTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'CalFlux.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'CalFlux.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalFlux)"
                % directory,
                "CalFluxTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for CalFlux")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "CalFlux.xml")
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
