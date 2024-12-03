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
# File CalAtmosphereTable.py
#

import pyasdm.ASDM

from .CalAtmosphereRow import CalAtmosphereRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class CalAtmosphereTable(Representable):
    """
    The CalAtmosphereTable class is an Alma table.

     Role
     Results of atmosphere calibration by TelCal. This calibration determines the system temperatures corrected for atmospheric absorption. Ionospheric effects are not dealt with in the Table.

     Generated from model's revision -1, branch

     Attributes of CalAtmosphere

                  Key

    antennaName str the name of the antenna.

    receiverBand ReceiverBand identifies the receiver band.

    basebandName BasebandName identifies the baseband.

    calDataId Tag refers to a unique row in CalData Table.

    calReductionId Tag refers to a unique row in CalReduction Table.



                  Value (Mandatory)

    startValidTime ArrayTime  the start time of result validity period.

    endValidTime ArrayTime  the end time of result validity period.

    numFreq int  the number of frequency points.

    numLoad int  the number of loads.

    numReceptor int  the number of receptors.

    forwardEffSpectrum float []  []   numReceptor, numFreq  the spectra of forward efficiencies (one value per receptor, per frequency).

    frequencyRange Frequency []   2  the frequency range.

    groundPressure Pressure  the ground pressure.

    groundRelHumidity Humidity  the ground relative humidity.

    frequencySpectrum Frequency []   numFreq  the frequencies.

    groundTemperature Temperature  the ground temperature.

    polarizationTypes PolarizationType []   numReceptor  the polarizations of the receptors (an array with one value per receptor).

    powerSkySpectrum float []  []   numReceptor, numFreq  the powers on the sky (one value per receptor per frequency).

    powerLoadSpectrum float []  []  []   numLoad, numReceptor, numFreq  the powers on the loads (one value per load per receptor per frequency).

    syscalType SyscalMethod  the type of calibration used.

    tAtmSpectrum Temperature []  []   numReceptor, numFreq  the spectra of atmosphere physical  temperatures (one value per receptor per frequency).

    tRecSpectrum Temperature []  []   numReceptor, numFreq  the spectra of the receptors temperatures (one value  per receptor per frequency).

    tSysSpectrum Temperature []  []   numReceptor, numFreq  the spectra of system temperatures (one value  per receptor per frequency).

    tauSpectrum float []  []   numReceptor, numFreq  the spectra of atmosheric optical depths (one value  per receptor per frequency).

    tAtm Temperature []   numReceptor  the atmosphere physical temperatures (one value per receptor).

    tRec Temperature []   numReceptor  the receptors temperatures (one value per receptor).

    tSys Temperature []   numReceptor  the system temperatures (one value per receptor).

    tau float []   numReceptor  the atmospheric optical depths (one value per receptor).

    water Length []   numReceptor  the water vapor path lengths (one value per receptor).

    waterError Length []   numReceptor  the uncertainties of water vapor contents (one value per receptor).



                  Value (Optional)

    alphaSpectrum float []  []   numReceptor, numFreq  the alpha coefficients, two loads only (one value per receptor per frequency).

    forwardEfficiency float []   numReceptor  the forward efficiencies (one value per receptor).

    forwardEfficiencyError double []   numReceptor  the uncertainties on forwardEfficiency (one value per receptor).

    sbGain float []   numReceptor  the relative gains of LO1 sideband (one value per receptor).

    sbGainError float []   numReceptor  the uncertainties on the relative gains of LO1 sideband (one value per receptor).

    sbGainSpectrum float []  []   numReceptor, numFreq  the spectra of relative sideband gains (one value  per receptor per frequency).


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "CalAtmosphere"

    # the list of field names that make up key 'key'.
    _key = [
        "antennaName",
        "receiverBand",
        "basebandName",
        "calDataId",
        "calReductionId",
    ]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = True  # if True archive binary else archive XML
    _fileAsBin = True  # if True file binary else file XML

    # A list to store the CalAtmosphereRow instances
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

    # The tolerance which will be used on groundPressure during an add operation on the table
    _groundPressureEqTolerance = Pressure(0.0)

    def setGroundPressureEqTolerance(self, tolerance):
        """
        A setter for the tolerance on groundPressure
        """
        self._groundPressureEqTolerance = Pressure(tolerance)

    # A getter for the tolerance on groundPressure
    def getGroundPressureEqTolerance(self):
        """
        A getter for the tolerance on groundPressure
        """
        return self._groundPressureEqTolerance

    # The tolerance which will be used on groundRelHumidity during an add operation on the table
    _groundRelHumidityEqTolerance = Humidity(0.0)

    def setGroundRelHumidityEqTolerance(self, tolerance):
        """
        A setter for the tolerance on groundRelHumidity
        """
        self._groundRelHumidityEqTolerance = Humidity(tolerance)

    # A getter for the tolerance on groundRelHumidity
    def getGroundRelHumidityEqTolerance(self):
        """
        A getter for the tolerance on groundRelHumidity
        """
        return self._groundRelHumidityEqTolerance

    # The tolerance which will be used on frequencySpectrum during an add operation on the table
    _frequencySpectrumEqTolerance = Frequency(0.0)

    def setFrequencySpectrumEqTolerance(self, tolerance):
        """
        A setter for the tolerance on frequencySpectrum
        """
        self._frequencySpectrumEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on frequencySpectrum
    def getFrequencySpectrumEqTolerance(self):
        """
        A getter for the tolerance on frequencySpectrum
        """
        return self._frequencySpectrumEqTolerance

    # The tolerance which will be used on groundTemperature during an add operation on the table
    _groundTemperatureEqTolerance = Temperature(0.0)

    def setGroundTemperatureEqTolerance(self, tolerance):
        """
        A setter for the tolerance on groundTemperature
        """
        self._groundTemperatureEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on groundTemperature
    def getGroundTemperatureEqTolerance(self):
        """
        A getter for the tolerance on groundTemperature
        """
        return self._groundTemperatureEqTolerance

    # The tolerance which will be used on tAtmSpectrum during an add operation on the table
    _tAtmSpectrumEqTolerance = Temperature(0.0)

    def setTAtmSpectrumEqTolerance(self, tolerance):
        """
        A setter for the tolerance on tAtmSpectrum
        """
        self._tAtmSpectrumEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on tAtmSpectrum
    def getTAtmSpectrumEqTolerance(self):
        """
        A getter for the tolerance on tAtmSpectrum
        """
        return self._tAtmSpectrumEqTolerance

    # The tolerance which will be used on tRecSpectrum during an add operation on the table
    _tRecSpectrumEqTolerance = Temperature(0.0)

    def setTRecSpectrumEqTolerance(self, tolerance):
        """
        A setter for the tolerance on tRecSpectrum
        """
        self._tRecSpectrumEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on tRecSpectrum
    def getTRecSpectrumEqTolerance(self):
        """
        A getter for the tolerance on tRecSpectrum
        """
        return self._tRecSpectrumEqTolerance

    # The tolerance which will be used on tSysSpectrum during an add operation on the table
    _tSysSpectrumEqTolerance = Temperature(0.0)

    def setTSysSpectrumEqTolerance(self, tolerance):
        """
        A setter for the tolerance on tSysSpectrum
        """
        self._tSysSpectrumEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on tSysSpectrum
    def getTSysSpectrumEqTolerance(self):
        """
        A getter for the tolerance on tSysSpectrum
        """
        return self._tSysSpectrumEqTolerance

    # The tolerance which will be used on tAtm during an add operation on the table
    _tAtmEqTolerance = Temperature(0.0)

    def setTAtmEqTolerance(self, tolerance):
        """
        A setter for the tolerance on tAtm
        """
        self._tAtmEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on tAtm
    def getTAtmEqTolerance(self):
        """
        A getter for the tolerance on tAtm
        """
        return self._tAtmEqTolerance

    # The tolerance which will be used on tRec during an add operation on the table
    _tRecEqTolerance = Temperature(0.0)

    def setTRecEqTolerance(self, tolerance):
        """
        A setter for the tolerance on tRec
        """
        self._tRecEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on tRec
    def getTRecEqTolerance(self):
        """
        A getter for the tolerance on tRec
        """
        return self._tRecEqTolerance

    # The tolerance which will be used on tSys during an add operation on the table
    _tSysEqTolerance = Temperature(0.0)

    def setTSysEqTolerance(self, tolerance):
        """
        A setter for the tolerance on tSys
        """
        self._tSysEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on tSys
    def getTSysEqTolerance(self):
        """
        A getter for the tolerance on tSys
        """
        return self._tSysEqTolerance

    # The tolerance which will be used on water during an add operation on the table
    _waterEqTolerance = Length(0.0)

    def setWaterEqTolerance(self, tolerance):
        """
        A setter for the tolerance on water
        """
        self._waterEqTolerance = Length(tolerance)

    # A getter for the tolerance on water
    def getWaterEqTolerance(self):
        """
        A getter for the tolerance on water
        """
        return self._waterEqTolerance

    # The tolerance which will be used on waterError during an add operation on the table
    _waterErrorEqTolerance = Length(0.0)

    def setWaterErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on waterError
        """
        self._waterErrorEqTolerance = Length(tolerance)

    # A getter for the tolerance on waterError
    def getWaterErrorEqTolerance(self):
        """
        A getter for the tolerance on waterError
        """
        return self._waterErrorEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    @staticmethod
    def Key(antennaName, receiverBand, basebandName, calDataId, calReductionId):
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
        Create a CalAtmosphereTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (
                ValueError("CalAtmosphereTable constructor must use a ASDM instance")
            )

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("CalAtmosphereTable")
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
        Returns "CalAtmosphereTable" followed by the current size of the table
        between parenthesis.
        Example : CalAtmosphereTable(12)
        """
        return "CalAtmosphereTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = CalAtmosphereRow(self)
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
                newrow.getBasebandName(),
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
                + x.getBasebandName()
                + "|"
                + x.getCalDataId()
                + "|"
                + x.getCalReductionId()
                + "]",
                "CalAtmosphere",
            )

        row.add(newrow)
        privateRows.add(newrow)
        newrow.isAdded()
        return newrow

    def newRow(
        self,
        antennaName,
        receiverBand,
        basebandName,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numFreq,
        numLoad,
        numReceptor,
        forwardEffSpectrum,
        frequencyRange,
        groundPressure,
        groundRelHumidity,
        frequencySpectrum,
        groundTemperature,
        polarizationTypes,
        powerSkySpectrum,
        powerLoadSpectrum,
        syscalType,
        tAtmSpectrum,
        tRecSpectrum,
        tSysSpectrum,
        tauSpectrum,
        tAtm,
        tRec,
        tSys,
        tau,
        water,
        waterError,
    ):
        """
        Create a new CalAtmosphereRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = CalAtmosphereRow(self)

        thisRow.setAntennaName(antennaName)

        thisRow.setReceiverBand(receiverBand)

        thisRow.setBasebandName(basebandName)

        thisRow.setCalDataId(calDataId)

        thisRow.setCalReductionId(calReductionId)

        thisRow.setStartValidTime(startValidTime)

        thisRow.setEndValidTime(endValidTime)

        thisRow.setNumFreq(numFreq)

        thisRow.setNumLoad(numLoad)

        thisRow.setNumReceptor(numReceptor)

        thisRow.setForwardEffSpectrum(forwardEffSpectrum)

        thisRow.setFrequencyRange(frequencyRange)

        thisRow.setGroundPressure(groundPressure)

        thisRow.setGroundRelHumidity(groundRelHumidity)

        thisRow.setFrequencySpectrum(frequencySpectrum)

        thisRow.setGroundTemperature(groundTemperature)

        thisRow.setPolarizationTypes(polarizationTypes)

        thisRow.setPowerSkySpectrum(powerSkySpectrum)

        thisRow.setPowerLoadSpectrum(powerLoadSpectrum)

        thisRow.setSyscalType(syscalType)

        thisRow.setTAtmSpectrum(tAtmSpectrum)

        thisRow.setTRecSpectrum(tRecSpectrum)

        thisRow.setTSysSpectrum(tSysSpectrum)

        thisRow.setTauSpectrum(tauSpectrum)

        thisRow.setTAtm(tAtm)

        thisRow.setTRec(tRec)

        thisRow.setTSys(tSys)

        thisRow.setTau(tau)

        thisRow.setWater(water)

        thisRow.setWaterError(waterError)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new CalAtmosphereRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new CalAtmosphereRow with default values for its attributes.
        """

        return CalAtmosphereRow(self, row)

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
                newrow.getBasebandName(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey("Duplicate key exception in ", "CalAtmosphereTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of CalAtmosphereRow
        """
        return self._privateRows

    def getRowByKey(
        self, antennaName, receiverBand, basebandName, calDataId, calReductionId
    ):
        """
        Returns a CalAtmosphereRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        @param antennaName.

        @param receiverBand.

        @param basebandName.

        @param calDataId.

        @param calReductionId.

        """
        for row in self._privateRows:

            if row.getAntennaName() != antennaName:
                continue

            if row.getReceiverBand() != receiverBand:
                continue

            if row.getBasebandName() != basebandName:
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
        basebandName,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numFreq,
        numLoad,
        numReceptor,
        forwardEffSpectrum,
        frequencyRange,
        groundPressure,
        groundRelHumidity,
        frequencySpectrum,
        groundTemperature,
        polarizationTypes,
        powerSkySpectrum,
        powerLoadSpectrum,
        syscalType,
        tAtmSpectrum,
        tRecSpectrum,
        tSysSpectrum,
        tauSpectrum,
        tAtm,
        tRec,
        tSys,
        tau,
        water,
        waterError,
    ):
        """
                Look up the table for a row whose all attributes
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param antennaName.

        param receiverBand.

        param basebandName.

        param calDataId.

        param calReductionId.

        param startValidTime.

        param endValidTime.

        param numFreq.

        param numLoad.

        param numReceptor.

        param forwardEffSpectrum.

        param frequencyRange.

        param groundPressure.

        param groundRelHumidity.

        param frequencySpectrum.

        param groundTemperature.

        param polarizationTypes.

        param powerSkySpectrum.

        param powerLoadSpectrum.

        param syscalType.

        param tAtmSpectrum.

        param tRecSpectrum.

        param tSysSpectrum.

        param tauSpectrum.

        param tAtm.

        param tRec.

        param tSys.

        param tau.

        param water.

        param waterError.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                antennaName,
                receiverBand,
                basebandName,
                calDataId,
                calReductionId,
                startValidTime,
                endValidTime,
                numFreq,
                numLoad,
                numReceptor,
                forwardEffSpectrum,
                frequencyRange,
                groundPressure,
                groundRelHumidity,
                frequencySpectrum,
                groundTemperature,
                polarizationTypes,
                powerSkySpectrum,
                powerLoadSpectrum,
                syscalType,
                tAtmSpectrum,
                tRecSpectrum,
                tSysSpectrum,
                tauSpectrum,
                tAtm,
                tRec,
                tSys,
                tau,
                water,
                waterError,
            ):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for CalAtmosphere (CalAtmosphereTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<CalAtmosphereTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clatm="http://Alma/XASDM/CalAtmosphereTable" xsi:schemaLocation="http://Alma/XASDM/CalAtmosphereTable http://almaobservatory.org/XML/XASDM/4/CalAtmosphereTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</CalAtmosphereTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a CalAtmosphere (CalAtmosphereTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of CalAtmosphereTable.
        if (
            not xmldom.hasChildNodes()
            or xmldom.firstChild.nodeName != "CalAtmosphereTable"
        ):
            raise ConversionException(
                "XML is not from a the expected table", "CalAtmosphereTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException(
                "schemaVersion not found in XML", "CalAtmosphereTable"
            )
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "CalAtmosphereTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "CalAtmosphereTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "CalAtmosphereTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "CalAtmosphereTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "CalAtmosphereTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML",
                        "CalAtmosphereTable",
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "CalAtmosphereTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalAtmosphereTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalAtmosphereTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalAtmosphereTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "CalAtmosphereTable",
            )

        if os.path.exists(os.path.join(directory, "CalAtmosphere.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalAtmosphere.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalAtmosphere table", "CalAtmosphereTable"
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
        with open(os.path.join(directory, "CalAtmosphere.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException(
                "CalAtmosphere.xml is empty", "CalAtmosphereTable"
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
        of this (_fileAsBin=True) will be saved in a file 'CalAtmosphere.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'CalAtmosphere.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalAtmosphere)"
                % directory,
                "CalAtmosphereTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for CalAtmosphere")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "CalAtmosphere.xml")
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
