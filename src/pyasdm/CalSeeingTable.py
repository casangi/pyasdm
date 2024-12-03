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
# File CalSeeingTable.py
#

import pyasdm.ASDM

from .CalSeeingRow import CalSeeingRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class CalSeeingTable(Representable):
    """
    The CalSeeingTable class is an Alma table.

     Role
     The seeing parameters deduced from TelCal calibrations.

     Generated from model's revision -1, branch

     Attributes of CalSeeing

                  Key

    atmPhaseCorrection AtmPhaseCorrection describes how the atmospheric phase correction has been applied.

    calDataId Tag refers to a unique row in CalData Table.

    calReductionId Tag refers to a unique row in CalReduction Table.



                  Value (Mandatory)

    startValidTime ArrayTime  the start time of result validity period.

    endValidTime ArrayTime  the end time of result validity period.

    frequencyRange Frequency []   2  the range of frequencies over which this result is valid.

    integrationTime Interval  the duration of averaging for the evaluation of the RMS.

    numBaseLengths int  the number of baselines for which the the RMS phase data is evaluated.

    baselineLengths Length []   numBaseLengths  the lengths of the baselines (one value per baseline).

    phaseRMS Angle []   numBaseLengths  the RMS of phase fluctuations (one value per baseline).

    seeing Angle  the seeing parameter, deduced for the LO1.

    seeingError Angle  the uncertainty on the seeing parameter.



                  Value (Optional)

    exponent float  the exponent of the spatial structure function.

    outerScale Length  the outer scale.

    outerScaleRMS Angle  the RMS of phase fluctuations at scale length outerScale.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "CalSeeing"

    # the list of field names that make up key 'key'.
    _key = ["atmPhaseCorrection", "calDataId", "calReductionId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = True  # if True archive binary else archive XML
    _fileAsBin = True  # if True file binary else file XML

    # A list to store the CalSeeingRow instances
    _privateRows = []

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on frequencyRange during an add operation on the table
    _frequencyRangeEqTolerance = Frequency(0.0)

    def setFrequencyRangeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on frequencyRange
        """
        self._frequencyRangeEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on frequencyRange
    def getFrequencyRangeEqTolerance(self):
        """
        A getter for the tolerance on frequencyRange
        """
        return self._frequencyRangeEqTolerance

    # The tolerance which will be used on baselineLengths during an add operation on the table
    _baselineLengthsEqTolerance = Length(0.0)

    def setBaselineLengthsEqTolerance(self, tolerance):
        """
        A setter for the tolerance on baselineLengths
        """
        self._baselineLengthsEqTolerance = Length(tolerance)

    # A getter for the tolerance on baselineLengths
    def getBaselineLengthsEqTolerance(self):
        """
        A getter for the tolerance on baselineLengths
        """
        return self._baselineLengthsEqTolerance

    # The tolerance which will be used on phaseRMS during an add operation on the table
    _phaseRMSEqTolerance = Angle(0.0)

    def setPhaseRMSEqTolerance(self, tolerance):
        """
        A setter for the tolerance on phaseRMS
        """
        self._phaseRMSEqTolerance = Angle(tolerance)

    # A getter for the tolerance on phaseRMS
    def getPhaseRMSEqTolerance(self):
        """
        A getter for the tolerance on phaseRMS
        """
        return self._phaseRMSEqTolerance

    # The tolerance which will be used on seeing during an add operation on the table
    _seeingEqTolerance = Angle(0.0)

    def setSeeingEqTolerance(self, tolerance):
        """
        A setter for the tolerance on seeing
        """
        self._seeingEqTolerance = Angle(tolerance)

    # A getter for the tolerance on seeing
    def getSeeingEqTolerance(self):
        """
        A getter for the tolerance on seeing
        """
        return self._seeingEqTolerance

    # The tolerance which will be used on seeingError during an add operation on the table
    _seeingErrorEqTolerance = Angle(0.0)

    def setSeeingErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on seeingError
        """
        self._seeingErrorEqTolerance = Angle(tolerance)

    # A getter for the tolerance on seeingError
    def getSeeingErrorEqTolerance(self):
        """
        A getter for the tolerance on seeingError
        """
        return self._seeingErrorEqTolerance

    # The tolerance which will be used on outerScale during an add operation on the table
    _outerScaleEqTolerance = Length(0.0)

    def setOuterScaleEqTolerance(self, tolerance):
        """
        A setter for the tolerance on outerScale
        """
        self._outerScaleEqTolerance = Length(tolerance)

    # A getter for the tolerance on outerScale
    def getOuterScaleEqTolerance(self):
        """
        A getter for the tolerance on outerScale
        """
        return self._outerScaleEqTolerance

    # The tolerance which will be used on outerScaleRMS during an add operation on the table
    _outerScaleRMSEqTolerance = Angle(0.0)

    def setOuterScaleRMSEqTolerance(self, tolerance):
        """
        A setter for the tolerance on outerScaleRMS
        """
        self._outerScaleRMSEqTolerance = Angle(tolerance)

    # A getter for the tolerance on outerScaleRMS
    def getOuterScaleRMSEqTolerance(self):
        """
        A getter for the tolerance on outerScaleRMS
        """
        return self._outerScaleRMSEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    @staticmethod
    def Key(atmPhaseCorrection, calDataId, calReductionId):
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
        Create a CalSeeingTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("CalSeeingTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("CalSeeingTable")
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
        Returns "CalSeeingTable" followed by the current size of the table
        between parenthesis.
        Example : CalSeeingTable(12)
        """
        return "CalSeeingTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = CalSeeingRow(self)
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
                newrow.getAtmPhaseCorrection(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey(
                "["
                + x.getAtmPhaseCorrection()
                + "|"
                + x.getCalDataId()
                + "|"
                + x.getCalReductionId()
                + "]",
                "CalSeeing",
            )

        row.add(newrow)
        privateRows.add(newrow)
        newrow.isAdded()
        return newrow

    def newRow(
        self,
        atmPhaseCorrection,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        frequencyRange,
        integrationTime,
        numBaseLengths,
        baselineLengths,
        phaseRMS,
        seeing,
        seeingError,
    ):
        """
        Create a new CalSeeingRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = CalSeeingRow(self)

        thisRow.setAtmPhaseCorrection(atmPhaseCorrection)

        thisRow.setCalDataId(calDataId)

        thisRow.setCalReductionId(calReductionId)

        thisRow.setStartValidTime(startValidTime)

        thisRow.setEndValidTime(endValidTime)

        thisRow.setFrequencyRange(frequencyRange)

        thisRow.setIntegrationTime(integrationTime)

        thisRow.setNumBaseLengths(numBaseLengths)

        thisRow.setBaselineLengths(baselineLengths)

        thisRow.setPhaseRMS(phaseRMS)

        thisRow.setSeeing(seeing)

        thisRow.setSeeingError(seeingError)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new CalSeeingRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new CalSeeingRow with default values for its attributes.
        """

        return CalSeeingRow(self, row)

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
                newrow.getAtmPhaseCorrection(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey("Duplicate key exception in ", "CalSeeingTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of CalSeeingRow
        """
        return self._privateRows

    def getRowByKey(self, atmPhaseCorrection, calDataId, calReductionId):
        """
        Returns a CalSeeingRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        @param atmPhaseCorrection.

        @param calDataId.

        @param calReductionId.

        """
        for row in self._privateRows:

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
        atmPhaseCorrection,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        frequencyRange,
        integrationTime,
        numBaseLengths,
        baselineLengths,
        phaseRMS,
        seeing,
        seeingError,
    ):
        """
                Look up the table for a row whose all attributes
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param atmPhaseCorrection.

        param calDataId.

        param calReductionId.

        param startValidTime.

        param endValidTime.

        param frequencyRange.

        param integrationTime.

        param numBaseLengths.

        param baselineLengths.

        param phaseRMS.

        param seeing.

        param seeingError.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                atmPhaseCorrection,
                calDataId,
                calReductionId,
                startValidTime,
                endValidTime,
                frequencyRange,
                integrationTime,
                numBaseLengths,
                baselineLengths,
                phaseRMS,
                seeing,
                seeingError,
            ):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for CalSeeing (CalSeeingTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<CalSeeingTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clsng="http://Alma/XASDM/CalSeeingTable" xsi:schemaLocation="http://Alma/XASDM/CalSeeingTable http://almaobservatory.org/XML/XASDM/4/CalSeeingTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</CalSeeingTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a CalSeeing (CalSeeingTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of CalSeeingTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "CalSeeingTable":
            raise ConversionException(
                "XML is not from a the expected table", "CalSeeingTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException(
                "schemaVersion not found in XML", "CalSeeingTable"
            )
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "CalSeeingTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "CalSeeingTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "CalSeeingTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "CalSeeingTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "CalSeeingTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "CalSeeingTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "CalSeeingTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalSeeingTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalSeeingTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalSeeingTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "CalSeeingTable",
            )

        if os.path.exists(os.path.join(directory, "CalSeeing.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalSeeing.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalSeeing table", "CalSeeingTable"
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
        with open(os.path.join(directory, "CalSeeing.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("CalSeeing.xml is empty", "CalSeeingTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'CalSeeing.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'CalSeeing.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalSeeing)"
                % directory,
                "CalSeeingTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for CalSeeing")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "CalSeeing.xml")
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
