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

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey
from .exceptions.UniquenessViolationException import UniquenessViolationException

from xml.dom import minidom

import os


class CalFocusTable:
    """
    The CalFocusTable class is an Alma table.

    Role
    Result of focus calibration performed on-line by TelCal.

    Generated from model's revision -1, branch

    Attributes of CalFocus

                 Key


    antennaName str the name of the antenna. </TD>



    receiverBand ReceiverBand identifies the receiver band. </TD>



    calDataId Tag refers to a unique row in CalData Table. </TD>



    calReductionId Tag refers to a unique row in CalReduction Table. </TD>




                 Value (Mandatory)

    startValidTime  ArrayTime  the start time of the result validity period.

    endValidTime  ArrayTime  the end time of the result validity period.

    ambientTemperature  Temperature  the ambient temperature.

    atmPhaseCorrection  AtmPhaseCorrection  qualifies how the atmospheric phase correction has been applied.

    focusMethod  FocusMethod  identifies the method used during the calibration.

    frequencyRange  Frequency []   2  the frequency range over which the result is valid.

    pointingDirection  Angle []   2  the antenna pointing direction (horizontal coordinates).

    numReceptor (numReceptor) int  the number of receptors.

    polarizationTypes  PolarizationType []   numReceptor  identifies the polarization types (one value per receptor).

    wereFixed  bool []   3  coordinates were fixed (true) or not fixed (false) (one value per individual coordinate).

    offset  Length []  []   numReceptor, 3  the measured focus offsets in X,Y,Z (one triple of values per receptor).

    offsetError  Length []  []   numReceptor, 3  the statistical uncertainties on measured focus offsets (one triple per receptor).

    offsetWasTied  bool []  []   numReceptor, 3  focus was tied (true) or not tied (false) (one value per receptor and focus individual coordinate).

    reducedChiSquared  float []  []   numReceptor, 3  a measure of the quality of the fit (one triple per receptor).

    position  Length []  []   numReceptor, 3  the absolute focus position in X,Y,Z (one triple of values per receptor).



                 Value (Optional)

    polarizationsAveraged  bool  Polarizations were averaged.

    focusCurveWidth  Length []  []   numReceptor, 3  half power width of fitted focus curve (one triple per receptor).

    focusCurveWidthError  Length []  []   numReceptor, 3  Uncertainty of the focus curve width.

    focusCurveWasFixed  bool []   3  each coordinate of the focus curve width was set (true) or not set (false) to an assumed value.

    offIntensity  Temperature []   numReceptor  the off intensity levels (one value per receptor).

    offIntensityError  Temperature []   numReceptor  the uncertainties on the off intensity levels (one value per receptor).

    offIntensityWasFixed  bool  the off intensity level was fixed (true) or not fixed (false).

    peakIntensity  Temperature []   numReceptor  the maximum intensities (one value per receptor).

    peakIntensityError  Temperature []   numReceptor  the uncertainties on the maximum intensities (one value per receptor).

    peakIntensityWasFixed  bool  the maximum intensity was fixed (true) or not fixed (false).

    astigmPlus  Length []   numReceptor  the astigmatism component with 0 degree symmetry axis.

    astigmPlusError  Length []   numReceptor  the statistical error on astigmPlus

    astigmMult  Length []   numReceptor  the astigmatism component with 45 degrees symmetry axis.

    astigmMultError  Length []   numReceptor  the statistical error on astigmMult

    illumOffset  Length []  []   numReceptor, 2  the illumination offset of the primary reflector expressed as a pair of values.

    illumOffsetError  Length []  []   numReceptor, 2  the statistical error on illumOffset.

    fitRMS  Length []   numReceptor  The RMS of the half path length after removing the best fit parabola.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # The name of this table.
    _tableName = "CalFocus"

    # The list of field names that make up key 'key'.
    _key = ["antennaName", "receiverBand", "calDataId", "calReductionId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # archive as bin not used by python implementation
    # _archiveAsBin = True # If True archive binary else archive XML
    _fileAsBin = True  # If True file binary else file XML

    # A data structure to store the CalFocusRow s.
    # In all cases we maintain a private list of CalFocusRow s.
    _privateRows = []

    # non-temporal ASDM in Java had a private row element here to also hold  CalFocusRow s. Not needed in python.

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
        if not isinstance(tolerance, Temperature):
            print("tolerance must be a  Temperature instance")

        self._ambientTemperatureEqTolerance = Temperature(tolerance)

    def getAmbientTemperatureEqTolerance(self):
        """
        A getter for the tolerance on ambientTemperature
        Returns the tolerance as a  Temperature
        """
        return self._ambientTemperatureEqTolerance

    # The tolerance which will be used on frequencyRange during an add operation on the table
    _frequencyRangeEqTolerance = Frequency(0.0)

    def setFrequencyRangeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on frequencyRange
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._frequencyRangeEqTolerance = Frequency(tolerance)

    def getFrequencyRangeEqTolerance(self):
        """
        A getter for the tolerance on frequencyRange
        Returns the tolerance as a  Frequency
        """
        return self._frequencyRangeEqTolerance

    # The tolerance which will be used on pointingDirection during an add operation on the table
    _pointingDirectionEqTolerance = Angle(0.0)

    def setPointingDirectionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on pointingDirection
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._pointingDirectionEqTolerance = Angle(tolerance)

    def getPointingDirectionEqTolerance(self):
        """
        A getter for the tolerance on pointingDirection
        Returns the tolerance as a  Angle
        """
        return self._pointingDirectionEqTolerance

    # The tolerance which will be used on offset during an add operation on the table
    _offsetEqTolerance = Length(0.0)

    def setOffsetEqTolerance(self, tolerance):
        """
        A setter for the tolerance on offset
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._offsetEqTolerance = Length(tolerance)

    def getOffsetEqTolerance(self):
        """
        A getter for the tolerance on offset
        Returns the tolerance as a  Length
        """
        return self._offsetEqTolerance

    # The tolerance which will be used on offsetError during an add operation on the table
    _offsetErrorEqTolerance = Length(0.0)

    def setOffsetErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on offsetError
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._offsetErrorEqTolerance = Length(tolerance)

    def getOffsetErrorEqTolerance(self):
        """
        A getter for the tolerance on offsetError
        Returns the tolerance as a  Length
        """
        return self._offsetErrorEqTolerance

    # The tolerance which will be used on position during an add operation on the table
    _positionEqTolerance = Length(0.0)

    def setPositionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on position
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._positionEqTolerance = Length(tolerance)

    def getPositionEqTolerance(self):
        """
        A getter for the tolerance on position
        Returns the tolerance as a  Length
        """
        return self._positionEqTolerance

    # The tolerance which will be used on focusCurveWidth during an add operation on the table
    _focusCurveWidthEqTolerance = Length(0.0)

    def setFocusCurveWidthEqTolerance(self, tolerance):
        """
        A setter for the tolerance on focusCurveWidth
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._focusCurveWidthEqTolerance = Length(tolerance)

    def getFocusCurveWidthEqTolerance(self):
        """
        A getter for the tolerance on focusCurveWidth
        Returns the tolerance as a  Length
        """
        return self._focusCurveWidthEqTolerance

    # The tolerance which will be used on focusCurveWidthError during an add operation on the table
    _focusCurveWidthErrorEqTolerance = Length(0.0)

    def setFocusCurveWidthErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on focusCurveWidthError
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._focusCurveWidthErrorEqTolerance = Length(tolerance)

    def getFocusCurveWidthErrorEqTolerance(self):
        """
        A getter for the tolerance on focusCurveWidthError
        Returns the tolerance as a  Length
        """
        return self._focusCurveWidthErrorEqTolerance

    # The tolerance which will be used on offIntensity during an add operation on the table
    _offIntensityEqTolerance = Temperature(0.0)

    def setOffIntensityEqTolerance(self, tolerance):
        """
        A setter for the tolerance on offIntensity
        """
        if not isinstance(tolerance, Temperature):
            print("tolerance must be a  Temperature instance")

        self._offIntensityEqTolerance = Temperature(tolerance)

    def getOffIntensityEqTolerance(self):
        """
        A getter for the tolerance on offIntensity
        Returns the tolerance as a  Temperature
        """
        return self._offIntensityEqTolerance

    # The tolerance which will be used on offIntensityError during an add operation on the table
    _offIntensityErrorEqTolerance = Temperature(0.0)

    def setOffIntensityErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on offIntensityError
        """
        if not isinstance(tolerance, Temperature):
            print("tolerance must be a  Temperature instance")

        self._offIntensityErrorEqTolerance = Temperature(tolerance)

    def getOffIntensityErrorEqTolerance(self):
        """
        A getter for the tolerance on offIntensityError
        Returns the tolerance as a  Temperature
        """
        return self._offIntensityErrorEqTolerance

    # The tolerance which will be used on peakIntensity during an add operation on the table
    _peakIntensityEqTolerance = Temperature(0.0)

    def setPeakIntensityEqTolerance(self, tolerance):
        """
        A setter for the tolerance on peakIntensity
        """
        if not isinstance(tolerance, Temperature):
            print("tolerance must be a  Temperature instance")

        self._peakIntensityEqTolerance = Temperature(tolerance)

    def getPeakIntensityEqTolerance(self):
        """
        A getter for the tolerance on peakIntensity
        Returns the tolerance as a  Temperature
        """
        return self._peakIntensityEqTolerance

    # The tolerance which will be used on peakIntensityError during an add operation on the table
    _peakIntensityErrorEqTolerance = Temperature(0.0)

    def setPeakIntensityErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on peakIntensityError
        """
        if not isinstance(tolerance, Temperature):
            print("tolerance must be a  Temperature instance")

        self._peakIntensityErrorEqTolerance = Temperature(tolerance)

    def getPeakIntensityErrorEqTolerance(self):
        """
        A getter for the tolerance on peakIntensityError
        Returns the tolerance as a  Temperature
        """
        return self._peakIntensityErrorEqTolerance

    # The tolerance which will be used on astigmPlus during an add operation on the table
    _astigmPlusEqTolerance = Length(0.0)

    def setAstigmPlusEqTolerance(self, tolerance):
        """
        A setter for the tolerance on astigmPlus
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._astigmPlusEqTolerance = Length(tolerance)

    def getAstigmPlusEqTolerance(self):
        """
        A getter for the tolerance on astigmPlus
        Returns the tolerance as a  Length
        """
        return self._astigmPlusEqTolerance

    # The tolerance which will be used on astigmPlusError during an add operation on the table
    _astigmPlusErrorEqTolerance = Length(0.0)

    def setAstigmPlusErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on astigmPlusError
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._astigmPlusErrorEqTolerance = Length(tolerance)

    def getAstigmPlusErrorEqTolerance(self):
        """
        A getter for the tolerance on astigmPlusError
        Returns the tolerance as a  Length
        """
        return self._astigmPlusErrorEqTolerance

    # The tolerance which will be used on astigmMult during an add operation on the table
    _astigmMultEqTolerance = Length(0.0)

    def setAstigmMultEqTolerance(self, tolerance):
        """
        A setter for the tolerance on astigmMult
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._astigmMultEqTolerance = Length(tolerance)

    def getAstigmMultEqTolerance(self):
        """
        A getter for the tolerance on astigmMult
        Returns the tolerance as a  Length
        """
        return self._astigmMultEqTolerance

    # The tolerance which will be used on astigmMultError during an add operation on the table
    _astigmMultErrorEqTolerance = Length(0.0)

    def setAstigmMultErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on astigmMultError
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._astigmMultErrorEqTolerance = Length(tolerance)

    def getAstigmMultErrorEqTolerance(self):
        """
        A getter for the tolerance on astigmMultError
        Returns the tolerance as a  Length
        """
        return self._astigmMultErrorEqTolerance

    # The tolerance which will be used on illumOffset during an add operation on the table
    _illumOffsetEqTolerance = Length(0.0)

    def setIllumOffsetEqTolerance(self, tolerance):
        """
        A setter for the tolerance on illumOffset
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._illumOffsetEqTolerance = Length(tolerance)

    def getIllumOffsetEqTolerance(self):
        """
        A getter for the tolerance on illumOffset
        Returns the tolerance as a  Length
        """
        return self._illumOffsetEqTolerance

    # The tolerance which will be used on illumOffsetError during an add operation on the table
    _illumOffsetErrorEqTolerance = Length(0.0)

    def setIllumOffsetErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on illumOffsetError
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._illumOffsetErrorEqTolerance = Length(tolerance)

    def getIllumOffsetErrorEqTolerance(self):
        """
        A getter for the tolerance on illumOffsetError
        Returns the tolerance as a  Length
        """
        return self._illumOffsetErrorEqTolerance

    # The tolerance which will be used on fitRMS during an add operation on the table
    _fitRMSEqTolerance = Length(0.0)

    def setFitRMSEqTolerance(self, tolerance):
        """
        A setter for the tolerance on fitRMS
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._fitRMSEqTolerance = Length(tolerance)

    def getFitRMSEqTolerance(self):
        """
        A getter for the tolerance on fitRMS
        Returns the tolerance as a  Length
        """
        return self._fitRMSEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up key key
        as a list of strings.
        """
        return self._key

    def Key(self, antennaName, receiverBand, calDataId, calReductionId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        """
        result = ""

        result += calDataId.toString() + "_"

        result += calReductionId.toString() + "_"

        return result

    def __init__(self, container):
        """
        Create a CalFocusTable attached to container.

        container must be a ASDM instance
        All tables must know the container
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

        self._privateRows = []

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
            print("CalFocus is not present in memory, setting from file")
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

    def add(self, x):
        """
        Add a row.
        raises a DuplicateKey Thrown if the new row has a key that is already in the table.
        If x is a list then this method is called recursively on each element of that list.
        In that case, None is returned.
        returns the row that was added.
        """

        if isinstance(x, list):
            for thisrow in x:
                # check on correct type of thisrow happens in add
                self.add(thisrow)
            # return None fo the list case only
            return None

        # the single row case
        if not isinstance(x, CalFocusRow):
            raise ValueError("x must be a  CalFocusRow instance.")

        if (
            self.getRowByKey(
                x.getAntennaName(),
                x.getReceiverBand(),
                x.getCalDataId(),
                x.getCalReductionId(),
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

        self._privateRows.append(x)
        x.isAdded()
        return x

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
        Create a new CalFocusRow initialized to the specified values.

        The new row is not added to this table, but it does know about it.
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
            self.getRowByKey(
                x.getAntennaName(),
                x.getReceiverBand(),
                x.getCalDataId(),
                x.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey("Duplicate key exception in ", "CalFocusTable")

        self._privateRows.append(x)
        x.isAdded()
        return x

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows.
        return Alls rows as a list of CalFocusRow
        """
        return self._privateRows

    def getRowByKey(self, antennaName, receiverBand, calDataId, calReductionId):
        """
        Returns a CalFocusRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        param antennaName.

        param receiverBand.

        param calDataId.

        param calReductionId.

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

    def getRows(self):
        """
        get the rows, synonymous with the get method.
        """
        return self.get()

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for CalFocus (CalFocusTable.xsd).

        returns a string containing the XML representation.
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
        if not isinstance(xmlstr, str):
            raise ConversionException("xmlstr must be a string")

        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of "CalFocusTable".
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "CalFocusTable":
            raise ConversionException(
                "XML is not from the expected table", "CalFocusTable"
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
                    self.checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str(exc), "CalFocusTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalFocusTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalFocusTable")

        self.setEntity(tabEntity)

    def MIMEXMLPart(self):
        print("MIMEXMLPart not implemented for <CalFocusTable")
        return
        # the JAVA code looks like this
        # String UID = this.getEntity().getEntityId().toString();
        # String withoutUID = UID.substring(6);
        # String containerUID = this.getContainer().getEntity().getEntityId().toString();
        #
        # StringBuffer sb = new StringBuffer()
        # .append("<?xml version='1.0'  encoding='ISO-8859-1'?>")
        # .append("\n")
        # .append("<CalFocusTable xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:clfcs=\"http://Alma/XASDM/CalFocusTable\" xsi:schemaLocation=\"http://Alma/XASDM/CalFocusTable http://almaobservatory.org/XML/XASDM/4/CalFocusTable.xsd\" schemaVersion=\"4\" schemaRevision=\"-1\">\n")
        # .append("<Entity entityId='")
        # .append(UID)
        # .append("' entityIdEncrypted='na' entityTypeName='CalFocusTable' schemaVersion='1' documentVersion='1'/>\n")
        # .append("<ContainerEntity entityId='")
        # .append(containerUID)
        # .append("' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n")
        # .append("<BulkStoreRef file_id='")
        # .append(withoutUID)
        # .append("' byteOrder='Big_Endian' />\n")
        # .append("<Attributes>\n")

        # .append("<antennaName/>\n")
        # .append("<receiverBand/>\n")
        # .append("<calDataId/>\n")
        # .append("<calReductionId/>\n")
        # .append("<startValidTime/>\n")
        # .append("<endValidTime/>\n")
        # .append("<ambientTemperature/>\n")
        # .append("<atmPhaseCorrection/>\n")
        # .append("<focusMethod/>\n")
        # .append("<frequencyRange/>\n")
        # .append("<pointingDirection/>\n")
        # .append("<numReceptor/>\n")
        # .append("<polarizationTypes/>\n")
        # .append("<wereFixed/>\n")
        # .append("<offset/>\n")
        # .append("<offsetError/>\n")
        # .append("<offsetWasTied/>\n")
        # .append("<reducedChiSquared/>\n")
        # .append("<position/>\n")

        # .append("<polarizationsAveraged/>\n")
        # .append("<focusCurveWidth/>\n")
        # .append("<focusCurveWidthError/>\n")
        # .append("<focusCurveWasFixed/>\n")
        # .append("<offIntensity/>\n")
        # .append("<offIntensityError/>\n")
        # .append("<offIntensityWasFixed/>\n")
        # .append("<peakIntensity/>\n")
        # .append("<peakIntensityError/>\n")
        # .append("<peakIntensityWasFixed/>\n")
        # .append("<astigmPlus/>\n")
        # .append("<astigmPlusError/>\n")
        # .append("<astigmMult/>\n")
        # .append("<astigmMultError/>\n")
        # .append("<illumOffset/>\n")
        # .append("<illumOffsetError/>\n")
        # .append("<fitRMS/>\n")
        # .append("</Attributes>\n")
        # .append("</CalFocusTable>\n");
        # return sb.toString();

    def toMIME(self):
        """
        Serialize this into a stream of bytes and encapsulates that stream into a MIME message.
        returns a string containing the MIME message.
        """
        print("toMIME not yet implemented for CalFocus")
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

        #    for (CalFocusRow row: privateRows) row.toBin(dos);

        #    // The closing MIME boundary
        #    dos.writeBytes("\n--MIME_boundary--");
        #    dos.writeBytes("\n");

        # } catch (IOException e) {
        #    throw new ConversionException(
        #            "Error while reading binary data , the message was "
        #            + e.getMessage(), "CalFocus");
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
    #    if (loc0 == -1 ) throw new ConversionException("Failed to detect the beginning of the XML header", "CalFocus");
    #
    #    loc0 += xmlPartMIMEHeader.length();
    #
    #    // Look for the string announcing the binary part.
    #    int loc1 = s.indexOf(binPartMIMEHeader, loc0);
    #    if (loc1 == -1) throw new ConversionException("Failed to detect the beginning of the binary part", "CalFocus");
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
    #     throw new ConversionException(e.getMessage(), "CalFocus");
    # }
    #
    # //
    # // Let's define a default order for the sequence of attributes.
    # //
    # ArrayList<String> attributesSeq = new ArrayList<String> ();

    #     attributesSeq.add("antennaName"); attributesSeq.add("receiverBand"); attributesSeq.add("calDataId"); attributesSeq.add("calReductionId"); attributesSeq.add("startValidTime"); attributesSeq.add("endValidTime"); attributesSeq.add("ambientTemperature"); attributesSeq.add("atmPhaseCorrection"); attributesSeq.add("focusMethod"); attributesSeq.add("frequencyRange"); attributesSeq.add("pointingDirection"); attributesSeq.add("numReceptor"); attributesSeq.add("polarizationTypes"); attributesSeq.add("wereFixed"); attributesSeq.add("offset"); attributesSeq.add("offsetError"); attributesSeq.add("offsetWasTied"); attributesSeq.add("reducedChiSquared"); attributesSeq.add("position");
    #     attributesSeq.add("polarizationsAveraged");  attributesSeq.add("focusCurveWidth");  attributesSeq.add("focusCurveWidthError");  attributesSeq.add("focusCurveWasFixed");  attributesSeq.add("offIntensity");  attributesSeq.add("offIntensityError");  attributesSeq.add("offIntensityWasFixed");  attributesSeq.add("peakIntensity");  attributesSeq.add("peakIntensityError");  attributesSeq.add("peakIntensityWasFixed");  attributesSeq.add("astigmPlus");  attributesSeq.add("astigmPlusError");  attributesSeq.add("astigmMult");  attributesSeq.add("astigmMultError");  attributesSeq.add("illumOffset");  attributesSeq.add("illumOffsetError");  attributesSeq.add("fitRMS");

    # XPath xpath = null;
    # //
    # // And then look for the possible XML contents.
    # try {
    #     // Is it an "<ASDMBinaryTable ...." document (old) ?
    #    if (XPath.newInstance("/ASDMBinaryTable")
    #            .selectSingleNode(document) != null)
    #        byteOrder = ByteOrder.BIG_ENDIAN;
    #    else {
    #        // Then it must be a "<CalFocusTable ...." document
    #        // With a BulkStoreRef child element....
    #        XPath xpa = XPath.newInstance("/CalFocusTable/BulkStoreRef/@byteOrder");
    #        Object node = xpa.selectSingleNode(document.getRootElement());
    #        if (node == null)
    #            throw new ConversionException("No element found for the XPath expression '/CalFocusTable/BulkStoreRef/@byteOrder'. Invalid XML header '"+header+"'.", "CalFocus");
    #
    #        // Yes ? then it must have a "BulkStoreRef" element with a
    #        // "byteOrder" attribute.
    #        String bo = xpa.valueOf(document.getRootElement());
    #        if (bo.equals("Little_Endian"))
    #            byteOrder = ByteOrder.LITTLE_ENDIAN;
    #        else if (bo.equals("Big_Endian"))
    #            byteOrder = ByteOrder.BIG_ENDIAN;
    #        else
    #            throw new ConversionException("No valid value retrieved for the node '/CalFocusTable/BulkStoreRef/@byteOrder'. Invalid XML header '"+header+"'.", "CalFocus");
    #
    #        // And also it must have an Attributes element with children.
    #        xpa = XPath.newInstance("/CalFocusTable/Attributes#");
    #        List nodes = xpa.selectNodes(document.getRootElement());
    #        if (nodes==null || nodes.size()==0)
    #            throw new ConversionException("No element found for the XPath expression '/CalFocusTable/Attributes#'. Invalid XML header '"+header+"'.", "CalFocus");
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
    #    throw new ConversionException(e.getMessage(), "CalFocus");
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
    #        throw new ConversionException ("Failed to detect the beginning of the binary part", "CalFocus");
    #    }
    #
    #    entity = Entity.fromBin(bodis);
    #
    #    Entity containerEntity = Entity.fromBin(bodis);
    #
    #    int numRows = bodis.readInt();
    #    for (int i = 0; i < numRows; i++) {
    #    this.checkAndAdd(CalFocusRow.fromBin(bodis, this, attributesSeq.toArray(new String[0])));
    #    }
    # } catch (TagFormatException e) {
    #    throw new ConversionException( "Error while reading binary data , the message was "
    #        + e.getMessage(), "CalFocus");
    # }catch (IOException e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "CalFocus");
    # } catch (DuplicateKey e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "CalFocus");
    # }catch (Exception e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "CalFocus");
    # }
    # }

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalFocusTable as those produced  by the toFile method.
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
                "CalFocusTable",
            )

        if os.path.exists(os.path.join(directory, "CalFocus.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalFocus.bin")):
            self.setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalFocus table", "CalFocusTable"
            )

    def setFromMIMEFile(self, directory):
        """
        Set this table from a MIME file.
        Used internally by setFromFile. Not intented for external use.
        """
        print("setFromMIME file not yet implemented for CalFocusTable")
        return

        # java code looks like this
        # File file = new File(directory+"/CalFocus.bin");
        #
        # byte[] bytes = null;
        #
        # try {
        #     InputStream is = new FileInputStream(file);
        #     long length = file.length();
        #     if (length > Integer.MAX_VALUE)
        #         throw new ConversionException ("File " + file.getName() + " is too large", "CalFocus");
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
        #        throw new ConversionException("Could not completely read file "+file.getName(), "CalFocus");
        #    }
        #    is.close();
        # }
        # catch (IOException e) {
        #    throw new ConversionException("Error while reading "+file.getName()+". The message was " + e.getMessage(),
        #    "CalFocus");
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
            with open(os.path.join(directory, "CalFocus.xml")) as f:
                xmlstr = f.read()
        except Exception as exc:
            # reraise it as a ConversionException
            raise ConversionException(str(exc), "CalFocusTable") from None

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
                    "CalFocus found as XML but it should be written as binary, which is not yet implemetned. Setting to write as XML to preserve this content."
                )
                self._fileAsBin = False

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of its _fileAsBin data member a binary serialization
        of this (_fileAsBin==True) will be saved in a file "CalFocus.bin" or
        an XML representation (_fileAsBin==False) will be saved in a file "CalFocus.xml".
        The file is always written in a directory whose name is passed as a parameter.
        param directory The name of directory where the file containing the table's
        representation will be saved.
        raises ConversionException for any errors while writing that file.
        """
        if not isinstance(directory, str):
            raise ConversionException("directory must be a string")

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalFocus)"
                % directory,
                "CalFocusTable",
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
                "CalFocusTable",
            ) from None

        if self._fileAsBin:
            print("fileAsBin not yet implemented for CalFocus")
            # the Java code looks like this
            #
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)
            #
            # File xmlFile = new File(directory+"/CalFocus.xml");
            # if (xmlFile.exists())
            #    if (!xmlFile.delete())
            #        throw new ConversionException("Problem while trying to delete a previous version of '"+xmlFile.toString()+"'", "CalFocus");
            #
            # File binFile = new File(directory+"/CalFocus.bin");
            # if (binFile.exists())
            #    if (!binFile.delete())
            #        throw new ConversionException("Problem while trying to delete a previous version of '"+binFile.toString()+"'", "CalFocus");
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
        #     throw new ConversionException("Problem while writing the binary representation, the message was : " + e.getMessage(), "CalFocus");
        # }
        # catch (IOException e) {
        #      throw new ConversionException("Problem while writing the binary representation, the message was : " + e.getMessage(), "CalFocus");
        # }
        # }
        else:
            # The table is totally exported in a XML file.
            filePath = os.path.join(directory, "CalFocus.xml")
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
                        "CalFocusTable",
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
                    "CalFocus",
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
