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
# File CalFocusTable.py
#

import pyasdm.ASDM

from .CalFocusRow import CalFocusRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class CalFocusTable(Representable):
    """
    The CalFocusTable class is an Alma table.

     Role
     Result of focus calibration performed on-line by TelCal.

     Generated from model's revision -1, branch

     Attributes of CalFocus

                  Key

    antennaName str the name of the antenna.

    receiverBand ReceiverBand identifies the receiver band.

    calDataId Tag refers to a unique row in CalData Table.

    calReductionId Tag refers to a unique row in CalReduction Table.



                  Value (Mandatory)

    startValidTime ArrayTime  the start time of the result validity period.

    endValidTime ArrayTime  the end time of the result validity period.

    ambientTemperature Temperature  the ambient temperature.

    atmPhaseCorrection AtmPhaseCorrection  qualifies how the atmospheric phase correction has been applied.

    focusMethod FocusMethod  identifies the method used during the calibration.

    frequencyRange Frequency []   2  the frequency range over which the result is valid.

    pointingDirection Angle []   2  the antenna pointing direction (horizontal coordinates).

    numReceptor int  the number of receptors.

    polarizationTypes PolarizationType []   numReceptor  identifies the polarization types (one value per receptor).

    wereFixed bool []   3  coordinates were fixed (true) or not fixed (false) (one value per individual coordinate).

    offset Length []  []   numReceptor, 3  the measured focus offsets in X,Y,Z (one triple of values per receptor).

    offsetError Length []  []   numReceptor, 3  the statistical uncertainties on measured focus offsets (one triple per receptor).

    offsetWasTied bool []  []   numReceptor, 3  focus was tied (true) or not tied (false) (one value per receptor and focus individual coordinate).

    reducedChiSquared double []  []   numReceptor, 3  a measure of the quality of the fit (one triple per receptor).

    position Length []  []   numReceptor, 3  the absolute focus position in X,Y,Z (one triple of values per receptor).



                  Value (Optional)

    polarizationsAveraged bool  Polarizations were averaged.

    focusCurveWidth Length []  []   numReceptor, 3  half power width of fitted focus curve (one triple per receptor).

    focusCurveWidthError Length []  []   numReceptor, 3  Uncertainty of the focus curve width.

    focusCurveWasFixed bool []   3  each coordinate of the focus curve width was set (true) or not set (false) to an assumed value.

    offIntensity Temperature []   numReceptor  the off intensity levels (one value per receptor).

    offIntensityError Temperature []   numReceptor  the uncertainties on the off intensity levels (one value per receptor).

    offIntensityWasFixed bool  the off intensity level was fixed (true) or not fixed (false).

    peakIntensity Temperature []   numReceptor  the maximum intensities (one value per receptor).

    peakIntensityError Temperature []   numReceptor  the uncertainties on the maximum intensities (one value per receptor).

    peakIntensityWasFixed bool  the maximum intensity was fixed (true) or not fixed (false).

    astigmPlus Length []   numReceptor  the astigmatism component with 0 degree symmetry axis.

    astigmPlusError Length []   numReceptor  the statistical error on astigmPlus

    astigmMult Length []   numReceptor  the astigmatism component with 45 degrees symmetry axis.

    astigmMultError Length []   numReceptor  the statistical error on astigmMult

    illumOffset Length []  []   numReceptor, 2  the illumination offset of the primary reflector expressed as a pair of values.

    illumOffsetError Length []  []   numReceptor, 2  the statistical error on illumOffset.

    fitRMS Length []   numReceptor  The RMS of the half path length after removing the best fit parabola.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "CalFocus"

    # the list of field names that make up key 'key'.
    _key = ["antennaName", "receiverBand", "calDataId", "calReductionId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = True  # if True archive binary else archive XML
    _fileAsBin = True  # if True file binary else file XML

    # A list to store the CalFocusRow instances
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

    # The tolerance which will be used on pointingDirection during an add operation on the table
    _pointingDirectionEqTolerance = Angle(0.0)

    def setPointingDirectionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on pointingDirection
        """
        self._pointingDirectionEqTolerance = Angle(tolerance)

    # A getter for the tolerance on pointingDirection
    def getPointingDirectionEqTolerance(self):
        """
        A getter for the tolerance on pointingDirection
        """
        return self._pointingDirectionEqTolerance

    # The tolerance which will be used on offset during an add operation on the table
    _offsetEqTolerance = Length(0.0)

    def setOffsetEqTolerance(self, tolerance):
        """
        A setter for the tolerance on offset
        """
        self._offsetEqTolerance = Length(tolerance)

    # A getter for the tolerance on offset
    def getOffsetEqTolerance(self):
        """
        A getter for the tolerance on offset
        """
        return self._offsetEqTolerance

    # The tolerance which will be used on offsetError during an add operation on the table
    _offsetErrorEqTolerance = Length(0.0)

    def setOffsetErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on offsetError
        """
        self._offsetErrorEqTolerance = Length(tolerance)

    # A getter for the tolerance on offsetError
    def getOffsetErrorEqTolerance(self):
        """
        A getter for the tolerance on offsetError
        """
        return self._offsetErrorEqTolerance

    # The tolerance which will be used on position during an add operation on the table
    _positionEqTolerance = Length(0.0)

    def setPositionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on position
        """
        self._positionEqTolerance = Length(tolerance)

    # A getter for the tolerance on position
    def getPositionEqTolerance(self):
        """
        A getter for the tolerance on position
        """
        return self._positionEqTolerance

    # The tolerance which will be used on focusCurveWidth during an add operation on the table
    _focusCurveWidthEqTolerance = Length(0.0)

    def setFocusCurveWidthEqTolerance(self, tolerance):
        """
        A setter for the tolerance on focusCurveWidth
        """
        self._focusCurveWidthEqTolerance = Length(tolerance)

    # A getter for the tolerance on focusCurveWidth
    def getFocusCurveWidthEqTolerance(self):
        """
        A getter for the tolerance on focusCurveWidth
        """
        return self._focusCurveWidthEqTolerance

    # The tolerance which will be used on focusCurveWidthError during an add operation on the table
    _focusCurveWidthErrorEqTolerance = Length(0.0)

    def setFocusCurveWidthErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on focusCurveWidthError
        """
        self._focusCurveWidthErrorEqTolerance = Length(tolerance)

    # A getter for the tolerance on focusCurveWidthError
    def getFocusCurveWidthErrorEqTolerance(self):
        """
        A getter for the tolerance on focusCurveWidthError
        """
        return self._focusCurveWidthErrorEqTolerance

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

    # The tolerance which will be used on astigmPlus during an add operation on the table
    _astigmPlusEqTolerance = Length(0.0)

    def setAstigmPlusEqTolerance(self, tolerance):
        """
        A setter for the tolerance on astigmPlus
        """
        self._astigmPlusEqTolerance = Length(tolerance)

    # A getter for the tolerance on astigmPlus
    def getAstigmPlusEqTolerance(self):
        """
        A getter for the tolerance on astigmPlus
        """
        return self._astigmPlusEqTolerance

    # The tolerance which will be used on astigmPlusError during an add operation on the table
    _astigmPlusErrorEqTolerance = Length(0.0)

    def setAstigmPlusErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on astigmPlusError
        """
        self._astigmPlusErrorEqTolerance = Length(tolerance)

    # A getter for the tolerance on astigmPlusError
    def getAstigmPlusErrorEqTolerance(self):
        """
        A getter for the tolerance on astigmPlusError
        """
        return self._astigmPlusErrorEqTolerance

    # The tolerance which will be used on astigmMult during an add operation on the table
    _astigmMultEqTolerance = Length(0.0)

    def setAstigmMultEqTolerance(self, tolerance):
        """
        A setter for the tolerance on astigmMult
        """
        self._astigmMultEqTolerance = Length(tolerance)

    # A getter for the tolerance on astigmMult
    def getAstigmMultEqTolerance(self):
        """
        A getter for the tolerance on astigmMult
        """
        return self._astigmMultEqTolerance

    # The tolerance which will be used on astigmMultError during an add operation on the table
    _astigmMultErrorEqTolerance = Length(0.0)

    def setAstigmMultErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on astigmMultError
        """
        self._astigmMultErrorEqTolerance = Length(tolerance)

    # A getter for the tolerance on astigmMultError
    def getAstigmMultErrorEqTolerance(self):
        """
        A getter for the tolerance on astigmMultError
        """
        return self._astigmMultErrorEqTolerance

    # The tolerance which will be used on illumOffset during an add operation on the table
    _illumOffsetEqTolerance = Length(0.0)

    def setIllumOffsetEqTolerance(self, tolerance):
        """
        A setter for the tolerance on illumOffset
        """
        self._illumOffsetEqTolerance = Length(tolerance)

    # A getter for the tolerance on illumOffset
    def getIllumOffsetEqTolerance(self):
        """
        A getter for the tolerance on illumOffset
        """
        return self._illumOffsetEqTolerance

    # The tolerance which will be used on illumOffsetError during an add operation on the table
    _illumOffsetErrorEqTolerance = Length(0.0)

    def setIllumOffsetErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on illumOffsetError
        """
        self._illumOffsetErrorEqTolerance = Length(tolerance)

    # A getter for the tolerance on illumOffsetError
    def getIllumOffsetErrorEqTolerance(self):
        """
        A getter for the tolerance on illumOffsetError
        """
        return self._illumOffsetErrorEqTolerance

    # The tolerance which will be used on fitRMS during an add operation on the table
    _fitRMSEqTolerance = Length(0.0)

    def setFitRMSEqTolerance(self, tolerance):
        """
        A setter for the tolerance on fitRMS
        """
        self._fitRMSEqTolerance = Length(tolerance)

    # A getter for the tolerance on fitRMS
    def getFitRMSEqTolerance(self):
        """
        A getter for the tolerance on fitRMS
        """
        return self._fitRMSEqTolerance

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
        Create a CalFocusTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("CalFocusTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("CalFocusTable")
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
        Returns "CalFocusTable" followed by the current size of the table
        between parenthesis.
        Example : CalFocusTable(12)
        """
        return "CalFocusTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = CalFocusRow(self)
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
                "CalFocus",
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
        atmPhaseCorrection,
        focusMethod,
        frequencyRange,
        pointingDirection,
        numReceptor,
        polarizationTypes,
        wereFixed,
        offset,
        offsetError,
        offsetWasTied,
        reducedChiSquared,
        position,
    ):
        """
        Create a new CalFocusRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = CalFocusRow(self)

        thisRow.setAntennaName(antennaName)

        thisRow.setReceiverBand(receiverBand)

        thisRow.setCalDataId(calDataId)

        thisRow.setCalReductionId(calReductionId)

        thisRow.setStartValidTime(startValidTime)

        thisRow.setEndValidTime(endValidTime)

        thisRow.setAmbientTemperature(ambientTemperature)

        thisRow.setAtmPhaseCorrection(atmPhaseCorrection)

        thisRow.setFocusMethod(focusMethod)

        thisRow.setFrequencyRange(frequencyRange)

        thisRow.setPointingDirection(pointingDirection)

        thisRow.setNumReceptor(numReceptor)

        thisRow.setPolarizationTypes(polarizationTypes)

        thisRow.setWereFixed(wereFixed)

        thisRow.setOffset(offset)

        thisRow.setOffsetError(offsetError)

        thisRow.setOffsetWasTied(offsetWasTied)

        thisRow.setReducedChiSquared(reducedChiSquared)

        thisRow.setPosition(position)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new CalFocusRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new CalFocusRow with default values for its attributes.
        """

        return CalFocusRow(self, row)

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
            raise DuplicateKey("Duplicate key exception in ", "CalFocusTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of CalFocusRow
        """
        return self._privateRows

    def getRowByKey(self, antennaName, receiverBand, calDataId, calReductionId):
        """
        Returns a CalFocusRow given a key.
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
        atmPhaseCorrection,
        focusMethod,
        frequencyRange,
        pointingDirection,
        numReceptor,
        polarizationTypes,
        wereFixed,
        offset,
        offsetError,
        offsetWasTied,
        reducedChiSquared,
        position,
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

        param atmPhaseCorrection.

        param focusMethod.

        param frequencyRange.

        param pointingDirection.

        param numReceptor.

        param polarizationTypes.

        param wereFixed.

        param offset.

        param offsetError.

        param offsetWasTied.

        param reducedChiSquared.

        param position.

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
                atmPhaseCorrection,
                focusMethod,
                frequencyRange,
                pointingDirection,
                numReceptor,
                polarizationTypes,
                wereFixed,
                offset,
                offsetError,
                offsetWasTied,
                reducedChiSquared,
                position,
            ):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for CalFocus (CalFocusTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<CalFocusTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clfcs="http://Alma/XASDM/CalFocusTable" xsi:schemaLocation="http://Alma/XASDM/CalFocusTable http://almaobservatory.org/XML/XASDM/4/CalFocusTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</CalFocusTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a CalFocus (CalFocusTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of CalFocusTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "CalFocusTable":
            raise ConversionException(
                "XML is not from a the expected table", "CalFocusTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException("schemaVersion not found in XML", "CalFocusTable")
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "CalFocusTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "CalFocusTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "CalFocusTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "CalFocusTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "CalFocusTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "CalFocusTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "CalFocusTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalFocusTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalFocusTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalFocusTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "CalFocusTable",
            )

        if os.path.exists(os.path.join(directory, "CalFocus.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalFocus.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalFocus table", "CalFocusTable"
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
        with open(os.path.join(directory, "CalFocus.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("CalFocus.xml is empty", "CalFocusTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'CalFocus.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'CalFocus.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalFocus)"
                % directory,
                "CalFocusTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for CalFocus")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "CalFocus.xml")
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
