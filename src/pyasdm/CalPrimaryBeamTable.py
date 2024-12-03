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
# File CalPrimaryBeamTable.py
#

import pyasdm.ASDM

from .CalPrimaryBeamRow import CalPrimaryBeamRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class CalPrimaryBeamTable(Representable):
    """
    The CalPrimaryBeamTable class is an Alma table.

     Role
     Result of Primary Beam Map measurement.

     Generated from model's revision -1, branch

     Attributes of CalPrimaryBeam

                  Key

    antennaName str the name of the antenna.

    receiverBand ReceiverBand identifies the receiver band.

    calDataId Tag refers to a unique row in CalData Table.

    calReductionId Tag refers to a unique row in CalReduction Table.



                  Value (Mandatory)

    startValidTime ArrayTime  the start time of result validity period.

    endValidTime ArrayTime  the end time of result validity period.

    antennaMake AntennaMake  the antenna make.

    numSubband int  the number of subband images (frequency ranges simultaneously measured ).

    frequencyRange Frequency []  []   numSubband, 2  the range of frequencies over which the result is valid.

    numReceptor int  the number of receptors.

    polarizationTypes PolarizationType []   numReceptor  identifies the polarizations types of the receptors (one value per receptor).

    mainBeamEfficiency double []   numReceptor  the main beam efficiency as derived from the beam map.

    beamDescriptionUID EntityRef  refers to the beam description image.

    relativeAmplitudeRms float  the RMS fluctuations in terms of the relative beam amplitude.

    direction Angle []   2  the center direction.

    minValidDirection Angle []   2  the minimum center direction of validity.

    maxValidDirection Angle []   2  the maximum center direction of validity.

    descriptionType PrimaryBeamDescription  quantity used to describe beam.

    imageChannelNumber int []   numSubband  channel number in image for each subband.

    imageNominalFrequency Frequency []   numSubband  nominal frequency for subband.



    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "CalPrimaryBeam"

    # the list of field names that make up key 'key'.
    _key = ["antennaName", "receiverBand", "calDataId", "calReductionId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = True  # if True archive binary else archive XML
    _fileAsBin = True  # if True file binary else file XML

    # A list to store the CalPrimaryBeamRow instances
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

    # The tolerance which will be used on minValidDirection during an add operation on the table
    _minValidDirectionEqTolerance = Angle(0.0)

    def setMinValidDirectionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on minValidDirection
        """
        self._minValidDirectionEqTolerance = Angle(tolerance)

    # A getter for the tolerance on minValidDirection
    def getMinValidDirectionEqTolerance(self):
        """
        A getter for the tolerance on minValidDirection
        """
        return self._minValidDirectionEqTolerance

    # The tolerance which will be used on maxValidDirection during an add operation on the table
    _maxValidDirectionEqTolerance = Angle(0.0)

    def setMaxValidDirectionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on maxValidDirection
        """
        self._maxValidDirectionEqTolerance = Angle(tolerance)

    # A getter for the tolerance on maxValidDirection
    def getMaxValidDirectionEqTolerance(self):
        """
        A getter for the tolerance on maxValidDirection
        """
        return self._maxValidDirectionEqTolerance

    # The tolerance which will be used on imageNominalFrequency during an add operation on the table
    _imageNominalFrequencyEqTolerance = Frequency(0.0)

    def setImageNominalFrequencyEqTolerance(self, tolerance):
        """
        A setter for the tolerance on imageNominalFrequency
        """
        self._imageNominalFrequencyEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on imageNominalFrequency
    def getImageNominalFrequencyEqTolerance(self):
        """
        A getter for the tolerance on imageNominalFrequency
        """
        return self._imageNominalFrequencyEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    @staticmethod
    def Key(antennaName, receiverBand, calDataId, calReductionId):
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
        Create a CalPrimaryBeamTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (
                ValueError("CalPrimaryBeamTable constructor must use a ASDM instance")
            )

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("CalPrimaryBeamTable")
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
        Returns "CalPrimaryBeamTable" followed by the current size of the table
        between parenthesis.
        Example : CalPrimaryBeamTable(12)
        """
        return "CalPrimaryBeamTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = CalPrimaryBeamRow(self)
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
                newrow.getReceiverBand(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey(
                "["
                + x.getAntennaName()
                + "|"
                + x.getReceiverBand()
                + "|"
                + x.getCalDataId()
                + "|"
                + x.getCalReductionId()
                + "]",
                "CalPrimaryBeam",
            )

        row.add(newrow)
        privateRows.add(newrow)
        newrow.isAdded()
        return newrow

    def newRow(
        self,
        antennaName,
        receiverBand,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        antennaMake,
        numSubband,
        frequencyRange,
        numReceptor,
        polarizationTypes,
        mainBeamEfficiency,
        beamDescriptionUID,
        relativeAmplitudeRms,
        direction,
        minValidDirection,
        maxValidDirection,
        descriptionType,
        imageChannelNumber,
        imageNominalFrequency,
    ):
        """
        Create a new CalPrimaryBeamRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = CalPrimaryBeamRow(self)

        thisRow.setAntennaName(antennaName)

        thisRow.setReceiverBand(receiverBand)

        thisRow.setCalDataId(calDataId)

        thisRow.setCalReductionId(calReductionId)

        thisRow.setStartValidTime(startValidTime)

        thisRow.setEndValidTime(endValidTime)

        thisRow.setAntennaMake(antennaMake)

        thisRow.setNumSubband(numSubband)

        thisRow.setFrequencyRange(frequencyRange)

        thisRow.setNumReceptor(numReceptor)

        thisRow.setPolarizationTypes(polarizationTypes)

        thisRow.setMainBeamEfficiency(mainBeamEfficiency)

        thisRow.setBeamDescriptionUID(beamDescriptionUID)

        thisRow.setRelativeAmplitudeRms(relativeAmplitudeRms)

        thisRow.setDirection(direction)

        thisRow.setMinValidDirection(minValidDirection)

        thisRow.setMaxValidDirection(maxValidDirection)

        thisRow.setDescriptionType(descriptionType)

        thisRow.setImageChannelNumber(imageChannelNumber)

        thisRow.setImageNominalFrequency(imageNominalFrequency)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new CalPrimaryBeamRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new CalPrimaryBeamRow with default values for its attributes.
        """

        return CalPrimaryBeamRow(self, row)

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
                newrow.getReceiverBand(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey("Duplicate key exception in ", "CalPrimaryBeamTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of CalPrimaryBeamRow
        """
        return self._privateRows

    def getRowByKey(self, antennaName, receiverBand, calDataId, calReductionId):
        """
        Returns a CalPrimaryBeamRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        @param antennaName.

        @param receiverBand.

        @param calDataId.

        @param calReductionId.

        """
        for row in self._privateRows:

            if row.getAntennaName() != antennaName:
                continue

            if row.getReceiverBand() != receiverBand:
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
        receiverBand,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        antennaMake,
        numSubband,
        frequencyRange,
        numReceptor,
        polarizationTypes,
        mainBeamEfficiency,
        beamDescriptionUID,
        relativeAmplitudeRms,
        direction,
        minValidDirection,
        maxValidDirection,
        descriptionType,
        imageChannelNumber,
        imageNominalFrequency,
    ):
        """
                Look up the table for a row whose all attributes
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param antennaName.

        param receiverBand.

        param calDataId.

        param calReductionId.

        param startValidTime.

        param endValidTime.

        param antennaMake.

        param numSubband.

        param frequencyRange.

        param numReceptor.

        param polarizationTypes.

        param mainBeamEfficiency.

        param beamDescriptionUID.

        param relativeAmplitudeRms.

        param direction.

        param minValidDirection.

        param maxValidDirection.

        param descriptionType.

        param imageChannelNumber.

        param imageNominalFrequency.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                antennaName,
                receiverBand,
                calDataId,
                calReductionId,
                startValidTime,
                endValidTime,
                antennaMake,
                numSubband,
                frequencyRange,
                numReceptor,
                polarizationTypes,
                mainBeamEfficiency,
                beamDescriptionUID,
                relativeAmplitudeRms,
                direction,
                minValidDirection,
                maxValidDirection,
                descriptionType,
                imageChannelNumber,
                imageNominalFrequency,
            ):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for CalPrimaryBeam (CalPrimaryBeamTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<CalPrimaryBeamTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clprbm="http://Alma/XASDM/CalPrimaryBeamTable" xsi:schemaLocation="http://Alma/XASDM/CalPrimaryBeamTable http://almaobservatory.org/XML/XASDM/4/CalPrimaryBeamTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</CalPrimaryBeamTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a CalPrimaryBeam (CalPrimaryBeamTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of CalPrimaryBeamTable.
        if (
            not xmldom.hasChildNodes()
            or xmldom.firstChild.nodeName != "CalPrimaryBeamTable"
        ):
            raise ConversionException(
                "XML is not from a the expected table", "CalPrimaryBeamTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException(
                "schemaVersion not found in XML", "CalPrimaryBeamTable"
            )
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "CalPrimaryBeamTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "CalPrimaryBeamTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "CalPrimaryBeamTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "CalPrimaryBeamTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "CalPrimaryBeamTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML",
                        "CalPrimaryBeamTable",
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "CalPrimaryBeamTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalPrimaryBeamTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalPrimaryBeamTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalPrimaryBeamTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "CalPrimaryBeamTable",
            )

        if os.path.exists(os.path.join(directory, "CalPrimaryBeam.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalPrimaryBeam.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalPrimaryBeam table", "CalPrimaryBeamTable"
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
        with open(os.path.join(directory, "CalPrimaryBeam.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException(
                "CalPrimaryBeam.xml is empty", "CalPrimaryBeamTable"
            )

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'CalPrimaryBeam.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'CalPrimaryBeam.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalPrimaryBeam)"
                % directory,
                "CalPrimaryBeamTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for CalPrimaryBeam")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "CalPrimaryBeam.xml")
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
