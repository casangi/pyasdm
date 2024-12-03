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
# File CalPointingTable.py
#

import pyasdm.ASDM

from .CalPointingRow import CalPointingRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class CalPointingTable(Representable):
    """
    The CalPointingTable class is an Alma table.

     Role
     Result of the pointing calibration performed on-line by TelCal.

     Generated from model's revision -1, branch

     Attributes of CalPointing

                  Key

    antennaName str Antenna Name

    receiverBand ReceiverBand identifies the receiver band.

    calDataId Tag refers to a unique row in CalData Table.

    calReductionId Tag refers to a unique row in CalReduction Table.



                  Value (Mandatory)

    startValidTime ArrayTime  the start time of result validity period.

    endValidTime ArrayTime  the end time of result validity period.

    ambientTemperature Temperature  the ambient temperature.

    antennaMake AntennaMake  identifies the antenna make.

    atmPhaseCorrection AtmPhaseCorrection  describes how the atmospheric phase correction has been applied.

    direction Angle []   2  the antenna pointing direction.

    frequencyRange Frequency []   2  the frequency range over which the result is valid.

    pointingModelMode PointingModelMode  identifies the pointing model mode.

    pointingMethod PointingMethod  identifies the pointing method.

    numReceptor int  the number of receptors.

    polarizationTypes PolarizationType []   numReceptor  identifies the polarizations types (one value per receptor).

    collOffsetRelative Angle []  []   numReceptor, 2  the collimation offsets (relative) (one pair of angles  per receptor).

    collOffsetAbsolute Angle []  []   numReceptor, 2  the collimation offsets (absolute) (one pair of angles per receptor).

    collError Angle []  []   numReceptor, 2  the uncertainties on collimation (one pair of angles per receptor)

    collOffsetTied bool []  []   numReceptor, 2  indicates if a collimation offset was tied (true) or not tied (false) to another polar (one pair of boolean values per receptor).

    reducedChiSquared double []   numReceptor  a measure of the quality of the least square fit.



                  Value (Optional)

    averagedPolarizations bool  true when the polarizations were averaged together to improve sensitivity.

    beamPA Angle []   numReceptor  the fitted beam position angles (one value per receptor).

    beamPAError Angle []   numReceptor  the uncertaintes on the fitted beam position angles (one value per receptor).

    beamPAWasFixed bool  indicates if the beam position was fixed (true) or not fixed (false).

    beamWidth Angle []  []   numReceptor, 2  the fitted beam widths (one pair of angles per receptor).

    beamWidthError Angle []  []   numReceptor, 2  the uncertainties on the fitted beam widths (one pair of angles per receptor).

    beamWidthWasFixed bool []   2  indicates if the beam width was fixed (true) or not fixed (true) (one pair of booleans).

    offIntensity Temperature []   numReceptor  the off intensity levels (one value per receptor).

    offIntensityError Temperature []   numReceptor  the uncertainties on the off intensity levels (one value per receptor).

    offIntensityWasFixed bool  indicates if the off intensity level was fixed (true) or not fixed (false).

    peakIntensity Temperature []   numReceptor  the maximum intensities (one value per receptor).

    peakIntensityError Temperature []   numReceptor  the uncertainties on the maximum intensities (one value per receptor).

    peakIntensityWasFixed bool  the maximum intensity was fixed.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "CalPointing"

    # the list of field names that make up key 'key'.
    _key = ["antennaName", "receiverBand", "calDataId", "calReductionId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = True  # if True archive binary else archive XML
    _fileAsBin = True  # if True file binary else file XML

    # A list to store the CalPointingRow instances
    _privateRows = []

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on ambientTemperature during an add operation on the table
    _ambientTemperatureEqTolerance = Temperature(0.0)

    def setAmbientTemperatureEqTolerance(self, tolerance):
        """
        A setter for the tolerance on ambientTemperature
        """
        self._ambientTemperatureEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on ambientTemperature
    def getAmbientTemperatureEqTolerance(self):
        """
        A getter for the tolerance on ambientTemperature
        """
        return self._ambientTemperatureEqTolerance

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

    # The tolerance which will be used on collOffsetRelative during an add operation on the table
    _collOffsetRelativeEqTolerance = Angle(0.0)

    def setCollOffsetRelativeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on collOffsetRelative
        """
        self._collOffsetRelativeEqTolerance = Angle(tolerance)

    # A getter for the tolerance on collOffsetRelative
    def getCollOffsetRelativeEqTolerance(self):
        """
        A getter for the tolerance on collOffsetRelative
        """
        return self._collOffsetRelativeEqTolerance

    # The tolerance which will be used on collOffsetAbsolute during an add operation on the table
    _collOffsetAbsoluteEqTolerance = Angle(0.0)

    def setCollOffsetAbsoluteEqTolerance(self, tolerance):
        """
        A setter for the tolerance on collOffsetAbsolute
        """
        self._collOffsetAbsoluteEqTolerance = Angle(tolerance)

    # A getter for the tolerance on collOffsetAbsolute
    def getCollOffsetAbsoluteEqTolerance(self):
        """
        A getter for the tolerance on collOffsetAbsolute
        """
        return self._collOffsetAbsoluteEqTolerance

    # The tolerance which will be used on collError during an add operation on the table
    _collErrorEqTolerance = Angle(0.0)

    def setCollErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on collError
        """
        self._collErrorEqTolerance = Angle(tolerance)

    # A getter for the tolerance on collError
    def getCollErrorEqTolerance(self):
        """
        A getter for the tolerance on collError
        """
        return self._collErrorEqTolerance

    # The tolerance which will be used on beamPA during an add operation on the table
    _beamPAEqTolerance = Angle(0.0)

    def setBeamPAEqTolerance(self, tolerance):
        """
        A setter for the tolerance on beamPA
        """
        self._beamPAEqTolerance = Angle(tolerance)

    # A getter for the tolerance on beamPA
    def getBeamPAEqTolerance(self):
        """
        A getter for the tolerance on beamPA
        """
        return self._beamPAEqTolerance

    # The tolerance which will be used on beamPAError during an add operation on the table
    _beamPAErrorEqTolerance = Angle(0.0)

    def setBeamPAErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on beamPAError
        """
        self._beamPAErrorEqTolerance = Angle(tolerance)

    # A getter for the tolerance on beamPAError
    def getBeamPAErrorEqTolerance(self):
        """
        A getter for the tolerance on beamPAError
        """
        return self._beamPAErrorEqTolerance

    # The tolerance which will be used on beamWidth during an add operation on the table
    _beamWidthEqTolerance = Angle(0.0)

    def setBeamWidthEqTolerance(self, tolerance):
        """
        A setter for the tolerance on beamWidth
        """
        self._beamWidthEqTolerance = Angle(tolerance)

    # A getter for the tolerance on beamWidth
    def getBeamWidthEqTolerance(self):
        """
        A getter for the tolerance on beamWidth
        """
        return self._beamWidthEqTolerance

    # The tolerance which will be used on beamWidthError during an add operation on the table
    _beamWidthErrorEqTolerance = Angle(0.0)

    def setBeamWidthErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on beamWidthError
        """
        self._beamWidthErrorEqTolerance = Angle(tolerance)

    # A getter for the tolerance on beamWidthError
    def getBeamWidthErrorEqTolerance(self):
        """
        A getter for the tolerance on beamWidthError
        """
        return self._beamWidthErrorEqTolerance

    # The tolerance which will be used on offIntensity during an add operation on the table
    _offIntensityEqTolerance = Temperature(0.0)

    def setOffIntensityEqTolerance(self, tolerance):
        """
        A setter for the tolerance on offIntensity
        """
        self._offIntensityEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on offIntensity
    def getOffIntensityEqTolerance(self):
        """
        A getter for the tolerance on offIntensity
        """
        return self._offIntensityEqTolerance

    # The tolerance which will be used on offIntensityError during an add operation on the table
    _offIntensityErrorEqTolerance = Temperature(0.0)

    def setOffIntensityErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on offIntensityError
        """
        self._offIntensityErrorEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on offIntensityError
    def getOffIntensityErrorEqTolerance(self):
        """
        A getter for the tolerance on offIntensityError
        """
        return self._offIntensityErrorEqTolerance

    # The tolerance which will be used on peakIntensity during an add operation on the table
    _peakIntensityEqTolerance = Temperature(0.0)

    def setPeakIntensityEqTolerance(self, tolerance):
        """
        A setter for the tolerance on peakIntensity
        """
        self._peakIntensityEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on peakIntensity
    def getPeakIntensityEqTolerance(self):
        """
        A getter for the tolerance on peakIntensity
        """
        return self._peakIntensityEqTolerance

    # The tolerance which will be used on peakIntensityError during an add operation on the table
    _peakIntensityErrorEqTolerance = Temperature(0.0)

    def setPeakIntensityErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on peakIntensityError
        """
        self._peakIntensityErrorEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on peakIntensityError
    def getPeakIntensityErrorEqTolerance(self):
        """
        A getter for the tolerance on peakIntensityError
        """
        return self._peakIntensityErrorEqTolerance

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
        Create a CalPointingTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("CalPointingTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("CalPointingTable")
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
        Returns "CalPointingTable" followed by the current size of the table
        between parenthesis.
        Example : CalPointingTable(12)
        """
        return "CalPointingTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = CalPointingRow(self)
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
                "CalPointing",
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
        ambientTemperature,
        antennaMake,
        atmPhaseCorrection,
        direction,
        frequencyRange,
        pointingModelMode,
        pointingMethod,
        numReceptor,
        polarizationTypes,
        collOffsetRelative,
        collOffsetAbsolute,
        collError,
        collOffsetTied,
        reducedChiSquared,
    ):
        """
        Create a new CalPointingRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = CalPointingRow(self)

        thisRow.setAntennaName(antennaName)

        thisRow.setReceiverBand(receiverBand)

        thisRow.setCalDataId(calDataId)

        thisRow.setCalReductionId(calReductionId)

        thisRow.setStartValidTime(startValidTime)

        thisRow.setEndValidTime(endValidTime)

        thisRow.setAmbientTemperature(ambientTemperature)

        thisRow.setAntennaMake(antennaMake)

        thisRow.setAtmPhaseCorrection(atmPhaseCorrection)

        thisRow.setDirection(direction)

        thisRow.setFrequencyRange(frequencyRange)

        thisRow.setPointingModelMode(pointingModelMode)

        thisRow.setPointingMethod(pointingMethod)

        thisRow.setNumReceptor(numReceptor)

        thisRow.setPolarizationTypes(polarizationTypes)

        thisRow.setCollOffsetRelative(collOffsetRelative)

        thisRow.setCollOffsetAbsolute(collOffsetAbsolute)

        thisRow.setCollError(collError)

        thisRow.setCollOffsetTied(collOffsetTied)

        thisRow.setReducedChiSquared(reducedChiSquared)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new CalPointingRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new CalPointingRow with default values for its attributes.
        """

        return CalPointingRow(self, row)

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
            raise DuplicateKey("Duplicate key exception in ", "CalPointingTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of CalPointingRow
        """
        return self._privateRows

    def getRowByKey(self, antennaName, receiverBand, calDataId, calReductionId):
        """
        Returns a CalPointingRow given a key.
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
        ambientTemperature,
        antennaMake,
        atmPhaseCorrection,
        direction,
        frequencyRange,
        pointingModelMode,
        pointingMethod,
        numReceptor,
        polarizationTypes,
        collOffsetRelative,
        collOffsetAbsolute,
        collError,
        collOffsetTied,
        reducedChiSquared,
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

        param ambientTemperature.

        param antennaMake.

        param atmPhaseCorrection.

        param direction.

        param frequencyRange.

        param pointingModelMode.

        param pointingMethod.

        param numReceptor.

        param polarizationTypes.

        param collOffsetRelative.

        param collOffsetAbsolute.

        param collError.

        param collOffsetTied.

        param reducedChiSquared.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                antennaName,
                receiverBand,
                calDataId,
                calReductionId,
                startValidTime,
                endValidTime,
                ambientTemperature,
                antennaMake,
                atmPhaseCorrection,
                direction,
                frequencyRange,
                pointingModelMode,
                pointingMethod,
                numReceptor,
                polarizationTypes,
                collOffsetRelative,
                collOffsetAbsolute,
                collError,
                collOffsetTied,
                reducedChiSquared,
            ):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for CalPointing (CalPointingTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<CalPointingTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clpntg="http://Alma/XASDM/CalPointingTable" xsi:schemaLocation="http://Alma/XASDM/CalPointingTable http://almaobservatory.org/XML/XASDM/4/CalPointingTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</CalPointingTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a CalPointing (CalPointingTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of CalPointingTable.
        if (
            not xmldom.hasChildNodes()
            or xmldom.firstChild.nodeName != "CalPointingTable"
        ):
            raise ConversionException(
                "XML is not from a the expected table", "CalPointingTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException(
                "schemaVersion not found in XML", "CalPointingTable"
            )
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "CalPointingTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "CalPointingTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "CalPointingTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "CalPointingTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "CalPointingTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "CalPointingTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "CalPointingTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalPointingTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalPointingTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalPointingTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "CalPointingTable",
            )

        if os.path.exists(os.path.join(directory, "CalPointing.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalPointing.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalPointing table", "CalPointingTable"
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
        with open(os.path.join(directory, "CalPointing.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("CalPointing.xml is empty", "CalPointingTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'CalPointing.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'CalPointing.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalPointing)"
                % directory,
                "CalPointingTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for CalPointing")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "CalPointing.xml")
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
