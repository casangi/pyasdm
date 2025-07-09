# ALMA - Atacama Large Millimeter Array
# (c) European Southern Observatory, 2024
# (c) Associated Universities Inc., 2024
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
# File ASDM.py
#

from pyasdm.types.ArrayTime import ArrayTime
from pyasdm.types.ArrayTimeInterval import ArrayTimeInterval
from pyasdm.types.Entity import Entity
from pyasdm.types.EntityId import EntityId

# using minidom instead of Parser
from xml.dom import minidom

# import each table

from pyasdm.MainTable import MainTable

from pyasdm.AlmaRadiometerTable import AlmaRadiometerTable

from pyasdm.AnnotationTable import AnnotationTable

from pyasdm.AntennaTable import AntennaTable

from pyasdm.CalAmpliTable import CalAmpliTable

from pyasdm.CalAntennaSolutionsTable import CalAntennaSolutionsTable

from pyasdm.CalAppPhaseTable import CalAppPhaseTable

from pyasdm.CalAtmosphereTable import CalAtmosphereTable

from pyasdm.CalBandpassTable import CalBandpassTable

from pyasdm.CalCurveTable import CalCurveTable

from pyasdm.CalDataTable import CalDataTable

from pyasdm.CalDelayTable import CalDelayTable

from pyasdm.CalDeviceTable import CalDeviceTable

from pyasdm.CalFluxTable import CalFluxTable

from pyasdm.CalFocusTable import CalFocusTable

from pyasdm.CalFocusModelTable import CalFocusModelTable

from pyasdm.CalGainTable import CalGainTable

from pyasdm.CalHolographyTable import CalHolographyTable

from pyasdm.CalPhaseTable import CalPhaseTable

from pyasdm.CalPointingTable import CalPointingTable

from pyasdm.CalPointingModelTable import CalPointingModelTable

from pyasdm.CalPositionTable import CalPositionTable

from pyasdm.CalPrimaryBeamTable import CalPrimaryBeamTable

from pyasdm.CalReductionTable import CalReductionTable

from pyasdm.CalSeeingTable import CalSeeingTable

from pyasdm.CalWVRTable import CalWVRTable

from pyasdm.ConfigDescriptionTable import ConfigDescriptionTable

from pyasdm.CorrelatorModeTable import CorrelatorModeTable

from pyasdm.DataDescriptionTable import DataDescriptionTable

from pyasdm.DelayModelTable import DelayModelTable

from pyasdm.DelayModelFixedParametersTable import DelayModelFixedParametersTable

from pyasdm.DelayModelVariableParametersTable import DelayModelVariableParametersTable

from pyasdm.DopplerTable import DopplerTable

from pyasdm.EphemerisTable import EphemerisTable

from pyasdm.ExecBlockTable import ExecBlockTable

from pyasdm.FeedTable import FeedTable

from pyasdm.FieldTable import FieldTable

from pyasdm.FlagTable import FlagTable

from pyasdm.FlagCmdTable import FlagCmdTable

from pyasdm.FocusTable import FocusTable

from pyasdm.FocusModelTable import FocusModelTable

from pyasdm.FreqOffsetTable import FreqOffsetTable

from pyasdm.GainTrackingTable import GainTrackingTable

from pyasdm.HistoryTable import HistoryTable

from pyasdm.HolographyTable import HolographyTable

from pyasdm.ObservationTable import ObservationTable

from pyasdm.PointingTable import PointingTable

from pyasdm.PointingModelTable import PointingModelTable

from pyasdm.PolarizationTable import PolarizationTable

from pyasdm.ProcessorTable import ProcessorTable

from pyasdm.PulsarTable import PulsarTable

from pyasdm.ReceiverTable import ReceiverTable

from pyasdm.SBSummaryTable import SBSummaryTable

from pyasdm.ScaleTable import ScaleTable

from pyasdm.ScanTable import ScanTable

from pyasdm.SeeingTable import SeeingTable

from pyasdm.SourceTable import SourceTable

from pyasdm.SpectralWindowTable import SpectralWindowTable

from pyasdm.SquareLawDetectorTable import SquareLawDetectorTable

from pyasdm.StateTable import StateTable

from pyasdm.StationTable import StationTable

from pyasdm.SubscanTable import SubscanTable

from pyasdm.SwitchCycleTable import SwitchCycleTable

from pyasdm.SysCalTable import SysCalTable

from pyasdm.SysPowerTable import SysPowerTable

from pyasdm.TotalPowerTable import TotalPowerTable

from pyasdm.VLAWVRTable import VLAWVRTable

from pyasdm.WVMCalTable import WVMCalTable

from pyasdm.WeatherTable import WeatherTable


from pyasdm.exceptions.ConversionException import ConversionException

import time
import os
import errno


class ASDM:
    """
    The ASDM class is the container for all tables.  Its instantation
    create a complete set of tables.

    Adapted from the Java and c++ code.

    Generated from model's revision -1, branch
    """

    # data members
    # _archiveAsBin is not used here, included in a comment because it's in the model
    # _archiveAsBin = False # if true archive binary else archive XML
    _fileAsBin = False  # if true file binary else file XML
    # _hasBeenAdded = False # Just to be "compatible" with tables generated code. Not used here.

    # This Container's entity.
    _entity = Entity()

    # attributes of this container are defind with their getters and setters

    # the directory appropriate for this ASDM, set by setFromFile
    _directory = None

    # tables are always loaded on demand when access from this class, not currently an option to turn that off in pyasdm

    # The dictionary of Entity objects representing the tables
    # this is populated when the ASDM is populated. Tables are loaded on demand when accessed here
    # if there is an entry in this dictionary, otherwise the table getter for that table will
    # return an empty table.
    _tableEntity = {}

    # table getter map, the value for a given name is the getter function for that table
    _tableGetters = {}

    _main = None

    _almaRadiometer = None

    _annotation = None

    _antenna = None

    _calAmpli = None

    _calAntennaSolutions = None

    _calAppPhase = None

    _calAtmosphere = None

    _calBandpass = None

    _calCurve = None

    _calData = None

    _calDelay = None

    _calDevice = None

    _calFlux = None

    _calFocus = None

    _calFocusModel = None

    _calGain = None

    _calHolography = None

    _calPhase = None

    _calPointing = None

    _calPointingModel = None

    _calPosition = None

    _calPrimaryBeam = None

    _calReduction = None

    _calSeeing = None

    _calWVR = None

    _configDescription = None

    _correlatorMode = None

    _dataDescription = None

    _delayModel = None

    _delayModelFixedParameters = None

    _delayModelVariableParameters = None

    _doppler = None

    _ephemeris = None

    _execBlock = None

    _feed = None

    _field = None

    _flag = None

    _flagCmd = None

    _focus = None

    _focusModel = None

    _freqOffset = None

    _gainTracking = None

    _history = None

    _holography = None

    _observation = None

    _pointing = None

    _pointingModel = None

    _polarization = None

    _processor = None

    _pulsar = None

    _receiver = None

    _sBSummary = None

    _scale = None

    _scan = None

    _seeing = None

    _source = None

    _spectralWindow = None

    _squareLawDetector = None

    _state = None

    _station = None

    _subscan = None

    _switchCycle = None

    _sysCal = None

    _sysPower = None

    _totalPower = None

    _vLAWVR = None

    _wVMCal = None

    _weather = None

    # defer on getTables() unless necessary, would return a list of all of the tables

    def __init__(self):
        """
        Create an empty ASDM with empty instances
        of the tables that belong to that container.
        """

        self._directory = None
        self._tableEntity = {}
        self._tableGetters = {}

        # initialize the attribute values

        self._timeOfCreation = ArrayTime()

        self._version = 0

        self._xmlnsPrefix = None

        # set the default entity.
        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("ASDM")
        self._entity.setEntityVersion("1")
        self._entity.setInstanceVersion("1")

        # Define a default creation time - now
        gmnow = time.gmtime()
        self._timeOfCreation.init(
            gmnow.tm_year,
            gmnow.tm_mon,
            gmnow.tm_mday,
            gmnow.tm_hour,
            gmnow.tm_min,
            gmnow.tm_sec,
        )

        # initialize the tables as empty but attached to this container

        self._main = MainTable(self)

        self._almaRadiometer = AlmaRadiometerTable(self)

        self._annotation = AnnotationTable(self)

        self._antenna = AntennaTable(self)

        self._calAmpli = CalAmpliTable(self)

        self._calAntennaSolutions = CalAntennaSolutionsTable(self)

        self._calAppPhase = CalAppPhaseTable(self)

        self._calAtmosphere = CalAtmosphereTable(self)

        self._calBandpass = CalBandpassTable(self)

        self._calCurve = CalCurveTable(self)

        self._calData = CalDataTable(self)

        self._calDelay = CalDelayTable(self)

        self._calDevice = CalDeviceTable(self)

        self._calFlux = CalFluxTable(self)

        self._calFocus = CalFocusTable(self)

        self._calFocusModel = CalFocusModelTable(self)

        self._calGain = CalGainTable(self)

        self._calHolography = CalHolographyTable(self)

        self._calPhase = CalPhaseTable(self)

        self._calPointing = CalPointingTable(self)

        self._calPointingModel = CalPointingModelTable(self)

        self._calPosition = CalPositionTable(self)

        self._calPrimaryBeam = CalPrimaryBeamTable(self)

        self._calReduction = CalReductionTable(self)

        self._calSeeing = CalSeeingTable(self)

        self._calWVR = CalWVRTable(self)

        self._configDescription = ConfigDescriptionTable(self)

        self._correlatorMode = CorrelatorModeTable(self)

        self._dataDescription = DataDescriptionTable(self)

        self._delayModel = DelayModelTable(self)

        self._delayModelFixedParameters = DelayModelFixedParametersTable(self)

        self._delayModelVariableParameters = DelayModelVariableParametersTable(self)

        self._doppler = DopplerTable(self)

        self._ephemeris = EphemerisTable(self)

        self._execBlock = ExecBlockTable(self)

        self._feed = FeedTable(self)

        self._field = FieldTable(self)

        self._flag = FlagTable(self)

        self._flagCmd = FlagCmdTable(self)

        self._focus = FocusTable(self)

        self._focusModel = FocusModelTable(self)

        self._freqOffset = FreqOffsetTable(self)

        self._gainTracking = GainTrackingTable(self)

        self._history = HistoryTable(self)

        self._holography = HolographyTable(self)

        self._observation = ObservationTable(self)

        self._pointing = PointingTable(self)

        self._pointingModel = PointingModelTable(self)

        self._polarization = PolarizationTable(self)

        self._processor = ProcessorTable(self)

        self._pulsar = PulsarTable(self)

        self._receiver = ReceiverTable(self)

        self._sBSummary = SBSummaryTable(self)

        self._scale = ScaleTable(self)

        self._scan = ScanTable(self)

        self._seeing = SeeingTable(self)

        self._source = SourceTable(self)

        self._spectralWindow = SpectralWindowTable(self)

        self._squareLawDetector = SquareLawDetectorTable(self)

        self._state = StateTable(self)

        self._station = StationTable(self)

        self._subscan = SubscanTable(self)

        self._switchCycle = SwitchCycleTable(self)

        self._sysCal = SysCalTable(self)

        self._sysPower = SysPowerTable(self)

        self._totalPower = TotalPowerTable(self)

        self._vLAWVR = VLAWVRTable(self)

        self._wVMCal = WVMCalTable(self)

        self._weather = WeatherTable(self)

    def getDirectory(self):
        """
        returns the directory used in the setFromFile call.
        This directory is used when the tables are first retrieved if they need to be loaded (on demand).
        This returns None if the directory has not yet been set.
        """
        return self._directory

    # the table getters

    def getMain(self):
        """
        Get the Main table.
        return The table Main as a MainTable.
        """
        self._main.checkPresenceInMemory()
        return self._main

    # associate the function with the table name in a map
    _tableGetters["Main"] = getMain

    def getAlmaRadiometer(self):
        """
        Get the AlmaRadiometer table.
        return The table AlmaRadiometer as a AlmaRadiometerTable.
        """
        self._almaRadiometer.checkPresenceInMemory()
        return self._almaRadiometer

    # associate the function with the table name in a map
    _tableGetters["AlmaRadiometer"] = getAlmaRadiometer

    def getAnnotation(self):
        """
        Get the Annotation table.
        return The table Annotation as a AnnotationTable.
        """
        self._annotation.checkPresenceInMemory()
        return self._annotation

    # associate the function with the table name in a map
    _tableGetters["Annotation"] = getAnnotation

    def getAntenna(self):
        """
        Get the Antenna table.
        return The table Antenna as a AntennaTable.
        """
        self._antenna.checkPresenceInMemory()
        return self._antenna

    # associate the function with the table name in a map
    _tableGetters["Antenna"] = getAntenna

    def getCalAmpli(self):
        """
        Get the CalAmpli table.
        return The table CalAmpli as a CalAmpliTable.
        """
        self._calAmpli.checkPresenceInMemory()
        return self._calAmpli

    # associate the function with the table name in a map
    _tableGetters["CalAmpli"] = getCalAmpli

    def getCalAntennaSolutions(self):
        """
        Get the CalAntennaSolutions table.
        return The table CalAntennaSolutions as a CalAntennaSolutionsTable.
        """
        self._calAntennaSolutions.checkPresenceInMemory()
        return self._calAntennaSolutions

    # associate the function with the table name in a map
    _tableGetters["CalAntennaSolutions"] = getCalAntennaSolutions

    def getCalAppPhase(self):
        """
        Get the CalAppPhase table.
        return The table CalAppPhase as a CalAppPhaseTable.
        """
        self._calAppPhase.checkPresenceInMemory()
        return self._calAppPhase

    # associate the function with the table name in a map
    _tableGetters["CalAppPhase"] = getCalAppPhase

    def getCalAtmosphere(self):
        """
        Get the CalAtmosphere table.
        return The table CalAtmosphere as a CalAtmosphereTable.
        """
        self._calAtmosphere.checkPresenceInMemory()
        return self._calAtmosphere

    # associate the function with the table name in a map
    _tableGetters["CalAtmosphere"] = getCalAtmosphere

    def getCalBandpass(self):
        """
        Get the CalBandpass table.
        return The table CalBandpass as a CalBandpassTable.
        """
        self._calBandpass.checkPresenceInMemory()
        return self._calBandpass

    # associate the function with the table name in a map
    _tableGetters["CalBandpass"] = getCalBandpass

    def getCalCurve(self):
        """
        Get the CalCurve table.
        return The table CalCurve as a CalCurveTable.
        """
        self._calCurve.checkPresenceInMemory()
        return self._calCurve

    # associate the function with the table name in a map
    _tableGetters["CalCurve"] = getCalCurve

    def getCalData(self):
        """
        Get the CalData table.
        return The table CalData as a CalDataTable.
        """
        self._calData.checkPresenceInMemory()
        return self._calData

    # associate the function with the table name in a map
    _tableGetters["CalData"] = getCalData

    def getCalDelay(self):
        """
        Get the CalDelay table.
        return The table CalDelay as a CalDelayTable.
        """
        self._calDelay.checkPresenceInMemory()
        return self._calDelay

    # associate the function with the table name in a map
    _tableGetters["CalDelay"] = getCalDelay

    def getCalDevice(self):
        """
        Get the CalDevice table.
        return The table CalDevice as a CalDeviceTable.
        """
        self._calDevice.checkPresenceInMemory()
        return self._calDevice

    # associate the function with the table name in a map
    _tableGetters["CalDevice"] = getCalDevice

    def getCalFlux(self):
        """
        Get the CalFlux table.
        return The table CalFlux as a CalFluxTable.
        """
        self._calFlux.checkPresenceInMemory()
        return self._calFlux

    # associate the function with the table name in a map
    _tableGetters["CalFlux"] = getCalFlux

    def getCalFocus(self):
        """
        Get the CalFocus table.
        return The table CalFocus as a CalFocusTable.
        """
        self._calFocus.checkPresenceInMemory()
        return self._calFocus

    # associate the function with the table name in a map
    _tableGetters["CalFocus"] = getCalFocus

    def getCalFocusModel(self):
        """
        Get the CalFocusModel table.
        return The table CalFocusModel as a CalFocusModelTable.
        """
        self._calFocusModel.checkPresenceInMemory()
        return self._calFocusModel

    # associate the function with the table name in a map
    _tableGetters["CalFocusModel"] = getCalFocusModel

    def getCalGain(self):
        """
        Get the CalGain table.
        return The table CalGain as a CalGainTable.
        """
        self._calGain.checkPresenceInMemory()
        return self._calGain

    # associate the function with the table name in a map
    _tableGetters["CalGain"] = getCalGain

    def getCalHolography(self):
        """
        Get the CalHolography table.
        return The table CalHolography as a CalHolographyTable.
        """
        self._calHolography.checkPresenceInMemory()
        return self._calHolography

    # associate the function with the table name in a map
    _tableGetters["CalHolography"] = getCalHolography

    def getCalPhase(self):
        """
        Get the CalPhase table.
        return The table CalPhase as a CalPhaseTable.
        """
        self._calPhase.checkPresenceInMemory()
        return self._calPhase

    # associate the function with the table name in a map
    _tableGetters["CalPhase"] = getCalPhase

    def getCalPointing(self):
        """
        Get the CalPointing table.
        return The table CalPointing as a CalPointingTable.
        """
        self._calPointing.checkPresenceInMemory()
        return self._calPointing

    # associate the function with the table name in a map
    _tableGetters["CalPointing"] = getCalPointing

    def getCalPointingModel(self):
        """
        Get the CalPointingModel table.
        return The table CalPointingModel as a CalPointingModelTable.
        """
        self._calPointingModel.checkPresenceInMemory()
        return self._calPointingModel

    # associate the function with the table name in a map
    _tableGetters["CalPointingModel"] = getCalPointingModel

    def getCalPosition(self):
        """
        Get the CalPosition table.
        return The table CalPosition as a CalPositionTable.
        """
        self._calPosition.checkPresenceInMemory()
        return self._calPosition

    # associate the function with the table name in a map
    _tableGetters["CalPosition"] = getCalPosition

    def getCalPrimaryBeam(self):
        """
        Get the CalPrimaryBeam table.
        return The table CalPrimaryBeam as a CalPrimaryBeamTable.
        """
        self._calPrimaryBeam.checkPresenceInMemory()
        return self._calPrimaryBeam

    # associate the function with the table name in a map
    _tableGetters["CalPrimaryBeam"] = getCalPrimaryBeam

    def getCalReduction(self):
        """
        Get the CalReduction table.
        return The table CalReduction as a CalReductionTable.
        """
        self._calReduction.checkPresenceInMemory()
        return self._calReduction

    # associate the function with the table name in a map
    _tableGetters["CalReduction"] = getCalReduction

    def getCalSeeing(self):
        """
        Get the CalSeeing table.
        return The table CalSeeing as a CalSeeingTable.
        """
        self._calSeeing.checkPresenceInMemory()
        return self._calSeeing

    # associate the function with the table name in a map
    _tableGetters["CalSeeing"] = getCalSeeing

    def getCalWVR(self):
        """
        Get the CalWVR table.
        return The table CalWVR as a CalWVRTable.
        """
        self._calWVR.checkPresenceInMemory()
        return self._calWVR

    # associate the function with the table name in a map
    _tableGetters["CalWVR"] = getCalWVR

    def getConfigDescription(self):
        """
        Get the ConfigDescription table.
        return The table ConfigDescription as a ConfigDescriptionTable.
        """
        self._configDescription.checkPresenceInMemory()
        return self._configDescription

    # associate the function with the table name in a map
    _tableGetters["ConfigDescription"] = getConfigDescription

    def getCorrelatorMode(self):
        """
        Get the CorrelatorMode table.
        return The table CorrelatorMode as a CorrelatorModeTable.
        """
        self._correlatorMode.checkPresenceInMemory()
        return self._correlatorMode

    # associate the function with the table name in a map
    _tableGetters["CorrelatorMode"] = getCorrelatorMode

    def getDataDescription(self):
        """
        Get the DataDescription table.
        return The table DataDescription as a DataDescriptionTable.
        """
        self._dataDescription.checkPresenceInMemory()
        return self._dataDescription

    # associate the function with the table name in a map
    _tableGetters["DataDescription"] = getDataDescription

    def getDelayModel(self):
        """
        Get the DelayModel table.
        return The table DelayModel as a DelayModelTable.
        """
        self._delayModel.checkPresenceInMemory()
        return self._delayModel

    # associate the function with the table name in a map
    _tableGetters["DelayModel"] = getDelayModel

    def getDelayModelFixedParameters(self):
        """
        Get the DelayModelFixedParameters table.
        return The table DelayModelFixedParameters as a DelayModelFixedParametersTable.
        """
        self._delayModelFixedParameters.checkPresenceInMemory()
        return self._delayModelFixedParameters

    # associate the function with the table name in a map
    _tableGetters["DelayModelFixedParameters"] = getDelayModelFixedParameters

    def getDelayModelVariableParameters(self):
        """
        Get the DelayModelVariableParameters table.
        return The table DelayModelVariableParameters as a DelayModelVariableParametersTable.
        """
        self._delayModelVariableParameters.checkPresenceInMemory()
        return self._delayModelVariableParameters

    # associate the function with the table name in a map
    _tableGetters["DelayModelVariableParameters"] = getDelayModelVariableParameters

    def getDoppler(self):
        """
        Get the Doppler table.
        return The table Doppler as a DopplerTable.
        """
        self._doppler.checkPresenceInMemory()
        return self._doppler

    # associate the function with the table name in a map
    _tableGetters["Doppler"] = getDoppler

    def getEphemeris(self):
        """
        Get the Ephemeris table.
        return The table Ephemeris as a EphemerisTable.
        """
        self._ephemeris.checkPresenceInMemory()
        return self._ephemeris

    # associate the function with the table name in a map
    _tableGetters["Ephemeris"] = getEphemeris

    def getExecBlock(self):
        """
        Get the ExecBlock table.
        return The table ExecBlock as a ExecBlockTable.
        """
        self._execBlock.checkPresenceInMemory()
        return self._execBlock

    # associate the function with the table name in a map
    _tableGetters["ExecBlock"] = getExecBlock

    def getFeed(self):
        """
        Get the Feed table.
        return The table Feed as a FeedTable.
        """
        self._feed.checkPresenceInMemory()
        return self._feed

    # associate the function with the table name in a map
    _tableGetters["Feed"] = getFeed

    def getField(self):
        """
        Get the Field table.
        return The table Field as a FieldTable.
        """
        self._field.checkPresenceInMemory()
        return self._field

    # associate the function with the table name in a map
    _tableGetters["Field"] = getField

    def getFlag(self):
        """
        Get the Flag table.
        return The table Flag as a FlagTable.
        """
        self._flag.checkPresenceInMemory()
        return self._flag

    # associate the function with the table name in a map
    _tableGetters["Flag"] = getFlag

    def getFlagCmd(self):
        """
        Get the FlagCmd table.
        return The table FlagCmd as a FlagCmdTable.
        """
        self._flagCmd.checkPresenceInMemory()
        return self._flagCmd

    # associate the function with the table name in a map
    _tableGetters["FlagCmd"] = getFlagCmd

    def getFocus(self):
        """
        Get the Focus table.
        return The table Focus as a FocusTable.
        """
        self._focus.checkPresenceInMemory()
        return self._focus

    # associate the function with the table name in a map
    _tableGetters["Focus"] = getFocus

    def getFocusModel(self):
        """
        Get the FocusModel table.
        return The table FocusModel as a FocusModelTable.
        """
        self._focusModel.checkPresenceInMemory()
        return self._focusModel

    # associate the function with the table name in a map
    _tableGetters["FocusModel"] = getFocusModel

    def getFreqOffset(self):
        """
        Get the FreqOffset table.
        return The table FreqOffset as a FreqOffsetTable.
        """
        self._freqOffset.checkPresenceInMemory()
        return self._freqOffset

    # associate the function with the table name in a map
    _tableGetters["FreqOffset"] = getFreqOffset

    def getGainTracking(self):
        """
        Get the GainTracking table.
        return The table GainTracking as a GainTrackingTable.
        """
        self._gainTracking.checkPresenceInMemory()
        return self._gainTracking

    # associate the function with the table name in a map
    _tableGetters["GainTracking"] = getGainTracking

    def getHistory(self):
        """
        Get the History table.
        return The table History as a HistoryTable.
        """
        self._history.checkPresenceInMemory()
        return self._history

    # associate the function with the table name in a map
    _tableGetters["History"] = getHistory

    def getHolography(self):
        """
        Get the Holography table.
        return The table Holography as a HolographyTable.
        """
        self._holography.checkPresenceInMemory()
        return self._holography

    # associate the function with the table name in a map
    _tableGetters["Holography"] = getHolography

    def getObservation(self):
        """
        Get the Observation table.
        return The table Observation as a ObservationTable.
        """
        self._observation.checkPresenceInMemory()
        return self._observation

    # associate the function with the table name in a map
    _tableGetters["Observation"] = getObservation

    def getPointing(self):
        """
        Get the Pointing table.
        return The table Pointing as a PointingTable.
        """
        self._pointing.checkPresenceInMemory()
        return self._pointing

    # associate the function with the table name in a map
    _tableGetters["Pointing"] = getPointing

    def getPointingModel(self):
        """
        Get the PointingModel table.
        return The table PointingModel as a PointingModelTable.
        """
        self._pointingModel.checkPresenceInMemory()
        return self._pointingModel

    # associate the function with the table name in a map
    _tableGetters["PointingModel"] = getPointingModel

    def getPolarization(self):
        """
        Get the Polarization table.
        return The table Polarization as a PolarizationTable.
        """
        self._polarization.checkPresenceInMemory()
        return self._polarization

    # associate the function with the table name in a map
    _tableGetters["Polarization"] = getPolarization

    def getProcessor(self):
        """
        Get the Processor table.
        return The table Processor as a ProcessorTable.
        """
        self._processor.checkPresenceInMemory()
        return self._processor

    # associate the function with the table name in a map
    _tableGetters["Processor"] = getProcessor

    def getPulsar(self):
        """
        Get the Pulsar table.
        return The table Pulsar as a PulsarTable.
        """
        self._pulsar.checkPresenceInMemory()
        return self._pulsar

    # associate the function with the table name in a map
    _tableGetters["Pulsar"] = getPulsar

    def getReceiver(self):
        """
        Get the Receiver table.
        return The table Receiver as a ReceiverTable.
        """
        self._receiver.checkPresenceInMemory()
        return self._receiver

    # associate the function with the table name in a map
    _tableGetters["Receiver"] = getReceiver

    def getSBSummary(self):
        """
        Get the SBSummary table.
        return The table SBSummary as a SBSummaryTable.
        """
        self._sBSummary.checkPresenceInMemory()
        return self._sBSummary

    # associate the function with the table name in a map
    _tableGetters["SBSummary"] = getSBSummary

    def getScale(self):
        """
        Get the Scale table.
        return The table Scale as a ScaleTable.
        """
        self._scale.checkPresenceInMemory()
        return self._scale

    # associate the function with the table name in a map
    _tableGetters["Scale"] = getScale

    def getScan(self):
        """
        Get the Scan table.
        return The table Scan as a ScanTable.
        """
        self._scan.checkPresenceInMemory()
        return self._scan

    # associate the function with the table name in a map
    _tableGetters["Scan"] = getScan

    def getSeeing(self):
        """
        Get the Seeing table.
        return The table Seeing as a SeeingTable.
        """
        self._seeing.checkPresenceInMemory()
        return self._seeing

    # associate the function with the table name in a map
    _tableGetters["Seeing"] = getSeeing

    def getSource(self):
        """
        Get the Source table.
        return The table Source as a SourceTable.
        """
        self._source.checkPresenceInMemory()
        return self._source

    # associate the function with the table name in a map
    _tableGetters["Source"] = getSource

    def getSpectralWindow(self):
        """
        Get the SpectralWindow table.
        return The table SpectralWindow as a SpectralWindowTable.
        """
        self._spectralWindow.checkPresenceInMemory()
        return self._spectralWindow

    # associate the function with the table name in a map
    _tableGetters["SpectralWindow"] = getSpectralWindow

    def getSquareLawDetector(self):
        """
        Get the SquareLawDetector table.
        return The table SquareLawDetector as a SquareLawDetectorTable.
        """
        self._squareLawDetector.checkPresenceInMemory()
        return self._squareLawDetector

    # associate the function with the table name in a map
    _tableGetters["SquareLawDetector"] = getSquareLawDetector

    def getState(self):
        """
        Get the State table.
        return The table State as a StateTable.
        """
        self._state.checkPresenceInMemory()
        return self._state

    # associate the function with the table name in a map
    _tableGetters["State"] = getState

    def getStation(self):
        """
        Get the Station table.
        return The table Station as a StationTable.
        """
        self._station.checkPresenceInMemory()
        return self._station

    # associate the function with the table name in a map
    _tableGetters["Station"] = getStation

    def getSubscan(self):
        """
        Get the Subscan table.
        return The table Subscan as a SubscanTable.
        """
        self._subscan.checkPresenceInMemory()
        return self._subscan

    # associate the function with the table name in a map
    _tableGetters["Subscan"] = getSubscan

    def getSwitchCycle(self):
        """
        Get the SwitchCycle table.
        return The table SwitchCycle as a SwitchCycleTable.
        """
        self._switchCycle.checkPresenceInMemory()
        return self._switchCycle

    # associate the function with the table name in a map
    _tableGetters["SwitchCycle"] = getSwitchCycle

    def getSysCal(self):
        """
        Get the SysCal table.
        return The table SysCal as a SysCalTable.
        """
        self._sysCal.checkPresenceInMemory()
        return self._sysCal

    # associate the function with the table name in a map
    _tableGetters["SysCal"] = getSysCal

    def getSysPower(self):
        """
        Get the SysPower table.
        return The table SysPower as a SysPowerTable.
        """
        self._sysPower.checkPresenceInMemory()
        return self._sysPower

    # associate the function with the table name in a map
    _tableGetters["SysPower"] = getSysPower

    def getTotalPower(self):
        """
        Get the TotalPower table.
        return The table TotalPower as a TotalPowerTable.
        """
        self._totalPower.checkPresenceInMemory()
        return self._totalPower

    # associate the function with the table name in a map
    _tableGetters["TotalPower"] = getTotalPower

    def getVLAWVR(self):
        """
        Get the VLAWVR table.
        return The table VLAWVR as a VLAWVRTable.
        """
        self._vLAWVR.checkPresenceInMemory()
        return self._vLAWVR

    # associate the function with the table name in a map
    _tableGetters["VLAWVR"] = getVLAWVR

    def getWVMCal(self):
        """
        Get the WVMCal table.
        return The table WVMCal as a WVMCalTable.
        """
        self._wVMCal.checkPresenceInMemory()
        return self._wVMCal

    # associate the function with the table name in a map
    _tableGetters["WVMCal"] = getWVMCal

    def getWeather(self):
        """
        Get the Weather table.
        return The table Weather as a WeatherTable.
        """
        self._weather.checkPresenceInMemory()
        return self._weather

    # associate the function with the table name in a map
    _tableGetters["Weather"] = getWeather

    # attribute getters and setters

    # ===> Attribute timeOfCreation

    _timeOfCreation = ArrayTime()

    def getTimeOfCreation(self):
        """
        Get timeOfCreation.
        return timeOfCreation as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._timeOfCreation)

    def setTimeOfCreation(self, timeOfCreation):
        """
        Set timeOfCreation with the specified ArrayTime value.
        timeOfCreation The ArrayTime value to which timeOfCreation is to be set.
        The value of timeOfCreation can be anything allowed by the ArrayTime constructor.

        """

        self._timeOfCreation = ArrayTime(timeOfCreation)

    # ===> Attribute version

    _version = 0

    def getVersion(self):
        """
        Get version.
        return version as int
        """

        return self._version

    def setVersion(self, version):
        """
        Set version with the specified int value.
        version The int value to which version is to be set.


        """

        self._version = int(version)

    # ===> Attribute xmlnsPrefix

    _xmlnsPrefix = None

    def getXmlnsPrefix(self):
        """
        Get xmlnsPrefix.
        return xmlnsPrefix as str
        """

        return self._xmlnsPrefix

    def setXmlnsPrefix(self, xmlnsPrefix):
        """
        Set xmlnsPrefix with the specified str value.
        xmlnsPrefix The str value to which xmlnsPrefix is to be set.


        """

        self._xmlnsPrefix = str(xmlnsPrefix)

    def addTableRowToXML(self, xmlstr, atable):
        """
        Appends the XML row for the given table to the given XML string, returning the new XML string.
        """
        xmlstr += "<Table> "
        xmlstr += "<Name> "
        xmlstr += atable.getName()
        xmlstr += " "
        xmlstr += "</Name> "
        xmlstr += "<NumberRows> "
        xmlstr += str(atable.size())
        xmlstr += " "
        xmlstr += "</NumberRows> "
        if atable.size() > 0:
            if atable.getEntity().isNull():
                raise ConversionException("Table entity is null.", atable.getName())
            xmlstr += atable.getEntity().toXML()
        xmlstr += "</Table>\n"
        return xmlstr

    def toXML(self):
        """
        Produces the XML representation of this.
        Returns a string containing the XML representation of this.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<ASDM xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:cntnr="http://Alma/XASDM/ASDM" xsi:schemaLocation="http://Alma/XASDM/ASDM http://almaobservatory.org/XML/XASDM/4/ASDM.xsd" schemaVersion="4" schemaRevision="-1"> '

        if self._entity.isNull():
            raise ConversionException("Container entity cannot be null.", "Container")

        result += self._entity.toXML()
        result += " "
        result += "<TimeOfCreation> "
        result += self._timeOfCreation.toFITS()
        result += " "
        result += "</TimeOfCreation>\n"

        # do each table via the getters, which populates each as necessary

        result = self.addTableRowToXML(result, self.getMain())
        # print("ASDM result row for table added as necessary for Main, size = " + str(self.getMain().size()))

        result = self.addTableRowToXML(result, self.getAlmaRadiometer())
        # print("ASDM result row for table added as necessary for AlmaRadiometer, size = " + str(self.getAlmaRadiometer().size()))

        result = self.addTableRowToXML(result, self.getAnnotation())
        # print("ASDM result row for table added as necessary for Annotation, size = " + str(self.getAnnotation().size()))

        result = self.addTableRowToXML(result, self.getAntenna())
        # print("ASDM result row for table added as necessary for Antenna, size = " + str(self.getAntenna().size()))

        result = self.addTableRowToXML(result, self.getCalAmpli())
        # print("ASDM result row for table added as necessary for CalAmpli, size = " + str(self.getCalAmpli().size()))

        result = self.addTableRowToXML(result, self.getCalAntennaSolutions())
        # print("ASDM result row for table added as necessary for CalAntennaSolutions, size = " + str(self.getCalAntennaSolutions().size()))

        result = self.addTableRowToXML(result, self.getCalAppPhase())
        # print("ASDM result row for table added as necessary for CalAppPhase, size = " + str(self.getCalAppPhase().size()))

        result = self.addTableRowToXML(result, self.getCalAtmosphere())
        # print("ASDM result row for table added as necessary for CalAtmosphere, size = " + str(self.getCalAtmosphere().size()))

        result = self.addTableRowToXML(result, self.getCalBandpass())
        # print("ASDM result row for table added as necessary for CalBandpass, size = " + str(self.getCalBandpass().size()))

        result = self.addTableRowToXML(result, self.getCalCurve())
        # print("ASDM result row for table added as necessary for CalCurve, size = " + str(self.getCalCurve().size()))

        result = self.addTableRowToXML(result, self.getCalData())
        # print("ASDM result row for table added as necessary for CalData, size = " + str(self.getCalData().size()))

        result = self.addTableRowToXML(result, self.getCalDelay())
        # print("ASDM result row for table added as necessary for CalDelay, size = " + str(self.getCalDelay().size()))

        result = self.addTableRowToXML(result, self.getCalDevice())
        # print("ASDM result row for table added as necessary for CalDevice, size = " + str(self.getCalDevice().size()))

        result = self.addTableRowToXML(result, self.getCalFlux())
        # print("ASDM result row for table added as necessary for CalFlux, size = " + str(self.getCalFlux().size()))

        result = self.addTableRowToXML(result, self.getCalFocus())
        # print("ASDM result row for table added as necessary for CalFocus, size = " + str(self.getCalFocus().size()))

        result = self.addTableRowToXML(result, self.getCalFocusModel())
        # print("ASDM result row for table added as necessary for CalFocusModel, size = " + str(self.getCalFocusModel().size()))

        result = self.addTableRowToXML(result, self.getCalGain())
        # print("ASDM result row for table added as necessary for CalGain, size = " + str(self.getCalGain().size()))

        result = self.addTableRowToXML(result, self.getCalHolography())
        # print("ASDM result row for table added as necessary for CalHolography, size = " + str(self.getCalHolography().size()))

        result = self.addTableRowToXML(result, self.getCalPhase())
        # print("ASDM result row for table added as necessary for CalPhase, size = " + str(self.getCalPhase().size()))

        result = self.addTableRowToXML(result, self.getCalPointing())
        # print("ASDM result row for table added as necessary for CalPointing, size = " + str(self.getCalPointing().size()))

        result = self.addTableRowToXML(result, self.getCalPointingModel())
        # print("ASDM result row for table added as necessary for CalPointingModel, size = " + str(self.getCalPointingModel().size()))

        result = self.addTableRowToXML(result, self.getCalPosition())
        # print("ASDM result row for table added as necessary for CalPosition, size = " + str(self.getCalPosition().size()))

        result = self.addTableRowToXML(result, self.getCalPrimaryBeam())
        # print("ASDM result row for table added as necessary for CalPrimaryBeam, size = " + str(self.getCalPrimaryBeam().size()))

        result = self.addTableRowToXML(result, self.getCalReduction())
        # print("ASDM result row for table added as necessary for CalReduction, size = " + str(self.getCalReduction().size()))

        result = self.addTableRowToXML(result, self.getCalSeeing())
        # print("ASDM result row for table added as necessary for CalSeeing, size = " + str(self.getCalSeeing().size()))

        result = self.addTableRowToXML(result, self.getCalWVR())
        # print("ASDM result row for table added as necessary for CalWVR, size = " + str(self.getCalWVR().size()))

        result = self.addTableRowToXML(result, self.getConfigDescription())
        # print("ASDM result row for table added as necessary for ConfigDescription, size = " + str(self.getConfigDescription().size()))

        result = self.addTableRowToXML(result, self.getCorrelatorMode())
        # print("ASDM result row for table added as necessary for CorrelatorMode, size = " + str(self.getCorrelatorMode().size()))

        result = self.addTableRowToXML(result, self.getDataDescription())
        # print("ASDM result row for table added as necessary for DataDescription, size = " + str(self.getDataDescription().size()))

        result = self.addTableRowToXML(result, self.getDelayModel())
        # print("ASDM result row for table added as necessary for DelayModel, size = " + str(self.getDelayModel().size()))

        result = self.addTableRowToXML(result, self.getDelayModelFixedParameters())
        # print("ASDM result row for table added as necessary for DelayModelFixedParameters, size = " + str(self.getDelayModelFixedParameters().size()))

        result = self.addTableRowToXML(result, self.getDelayModelVariableParameters())
        # print("ASDM result row for table added as necessary for DelayModelVariableParameters, size = " + str(self.getDelayModelVariableParameters().size()))

        result = self.addTableRowToXML(result, self.getDoppler())
        # print("ASDM result row for table added as necessary for Doppler, size = " + str(self.getDoppler().size()))

        result = self.addTableRowToXML(result, self.getEphemeris())
        # print("ASDM result row for table added as necessary for Ephemeris, size = " + str(self.getEphemeris().size()))

        result = self.addTableRowToXML(result, self.getExecBlock())
        # print("ASDM result row for table added as necessary for ExecBlock, size = " + str(self.getExecBlock().size()))

        result = self.addTableRowToXML(result, self.getFeed())
        # print("ASDM result row for table added as necessary for Feed, size = " + str(self.getFeed().size()))

        result = self.addTableRowToXML(result, self.getField())
        # print("ASDM result row for table added as necessary for Field, size = " + str(self.getField().size()))

        result = self.addTableRowToXML(result, self.getFlag())
        # print("ASDM result row for table added as necessary for Flag, size = " + str(self.getFlag().size()))

        result = self.addTableRowToXML(result, self.getFlagCmd())
        # print("ASDM result row for table added as necessary for FlagCmd, size = " + str(self.getFlagCmd().size()))

        result = self.addTableRowToXML(result, self.getFocus())
        # print("ASDM result row for table added as necessary for Focus, size = " + str(self.getFocus().size()))

        result = self.addTableRowToXML(result, self.getFocusModel())
        # print("ASDM result row for table added as necessary for FocusModel, size = " + str(self.getFocusModel().size()))

        result = self.addTableRowToXML(result, self.getFreqOffset())
        # print("ASDM result row for table added as necessary for FreqOffset, size = " + str(self.getFreqOffset().size()))

        result = self.addTableRowToXML(result, self.getGainTracking())
        # print("ASDM result row for table added as necessary for GainTracking, size = " + str(self.getGainTracking().size()))

        result = self.addTableRowToXML(result, self.getHistory())
        # print("ASDM result row for table added as necessary for History, size = " + str(self.getHistory().size()))

        result = self.addTableRowToXML(result, self.getHolography())
        # print("ASDM result row for table added as necessary for Holography, size = " + str(self.getHolography().size()))

        result = self.addTableRowToXML(result, self.getObservation())
        # print("ASDM result row for table added as necessary for Observation, size = " + str(self.getObservation().size()))

        result = self.addTableRowToXML(result, self.getPointing())
        # print("ASDM result row for table added as necessary for Pointing, size = " + str(self.getPointing().size()))

        result = self.addTableRowToXML(result, self.getPointingModel())
        # print("ASDM result row for table added as necessary for PointingModel, size = " + str(self.getPointingModel().size()))

        result = self.addTableRowToXML(result, self.getPolarization())
        # print("ASDM result row for table added as necessary for Polarization, size = " + str(self.getPolarization().size()))

        result = self.addTableRowToXML(result, self.getProcessor())
        # print("ASDM result row for table added as necessary for Processor, size = " + str(self.getProcessor().size()))

        result = self.addTableRowToXML(result, self.getPulsar())
        # print("ASDM result row for table added as necessary for Pulsar, size = " + str(self.getPulsar().size()))

        result = self.addTableRowToXML(result, self.getReceiver())
        # print("ASDM result row for table added as necessary for Receiver, size = " + str(self.getReceiver().size()))

        result = self.addTableRowToXML(result, self.getSBSummary())
        # print("ASDM result row for table added as necessary for SBSummary, size = " + str(self.getSBSummary().size()))

        result = self.addTableRowToXML(result, self.getScale())
        # print("ASDM result row for table added as necessary for Scale, size = " + str(self.getScale().size()))

        result = self.addTableRowToXML(result, self.getScan())
        # print("ASDM result row for table added as necessary for Scan, size = " + str(self.getScan().size()))

        result = self.addTableRowToXML(result, self.getSeeing())
        # print("ASDM result row for table added as necessary for Seeing, size = " + str(self.getSeeing().size()))

        result = self.addTableRowToXML(result, self.getSource())
        # print("ASDM result row for table added as necessary for Source, size = " + str(self.getSource().size()))

        result = self.addTableRowToXML(result, self.getSpectralWindow())
        # print("ASDM result row for table added as necessary for SpectralWindow, size = " + str(self.getSpectralWindow().size()))

        result = self.addTableRowToXML(result, self.getSquareLawDetector())
        # print("ASDM result row for table added as necessary for SquareLawDetector, size = " + str(self.getSquareLawDetector().size()))

        result = self.addTableRowToXML(result, self.getState())
        # print("ASDM result row for table added as necessary for State, size = " + str(self.getState().size()))

        result = self.addTableRowToXML(result, self.getStation())
        # print("ASDM result row for table added as necessary for Station, size = " + str(self.getStation().size()))

        result = self.addTableRowToXML(result, self.getSubscan())
        # print("ASDM result row for table added as necessary for Subscan, size = " + str(self.getSubscan().size()))

        result = self.addTableRowToXML(result, self.getSwitchCycle())
        # print("ASDM result row for table added as necessary for SwitchCycle, size = " + str(self.getSwitchCycle().size()))

        result = self.addTableRowToXML(result, self.getSysCal())
        # print("ASDM result row for table added as necessary for SysCal, size = " + str(self.getSysCal().size()))

        result = self.addTableRowToXML(result, self.getSysPower())
        # print("ASDM result row for table added as necessary for SysPower, size = " + str(self.getSysPower().size()))

        result = self.addTableRowToXML(result, self.getTotalPower())
        # print("ASDM result row for table added as necessary for TotalPower, size = " + str(self.getTotalPower().size()))

        result = self.addTableRowToXML(result, self.getVLAWVR())
        # print("ASDM result row for table added as necessary for VLAWVR, size = " + str(self.getVLAWVR().size()))

        result = self.addTableRowToXML(result, self.getWVMCal())
        # print("ASDM result row for table added as necessary for WVMCal, size = " + str(self.getWVMCal().size()))

        result = self.addTableRowToXML(result, self.getWeather())
        # print("ASDM result row for table added as necessary for Weather, size = " + str(self.getWeather().size()))

        result += "</ASDM>"
        return result

    def fromXML(self, xmlstr):
        """
        Parses the XML representation of an ASDM stored in a string and fills this
        (supposedly empty) with the result of the parsing.
        param xmlstr The XML of the ASDM as a string.
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have a single child node with a name of ASDM
        # ignore everything but the first child node
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "ASDM":
            raise ConversionError("XML is not from an ASDM", "ASDM")
        asdmdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        # default to an unknown version, caught later
        versionStr = "-1"
        # in early versions, schemaVersion is missing
        schemaVersionAttr = asdmdom.attributes.getNamedItem("schemaVersion")
        if schemaVersionAttr is not None:
            versionStr = schemaVersionAttr.value

        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except ValueError as ex:
            # all errors here should appear as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer as expected", "ASDM"
            )

        # can not continue if version is < 3
        # eventually an earlier version should be possible, but not yet
        if self.getVersion() < 3:
            raise ConversionException(
                "Only ASDM versions >=3 can be processed. Older versions require a pre-processing step that is not yet available.",
                "ASDM",
            )

        # go through the child nodes of asdmdom
        # only Table nodes should appear more than once
        asdmEntity = None
        asdmToC = None
        hasStartTimeDurationInXML = False
        hasStartTimeDurationInBin = False

        if not asdmdom.hasChildNodes():
            raise ConversionError("XML is missing all of the expected elements", "ASDM")

        for thisNode in asdmdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if asdmEntity is not None:
                    raise ConversionError("More than one Entity found", "ASDM")
                asdmEntity = Entity(thisNode.toxml())
            elif nodeName == "TimeOfCreation":
                if asdmToC is not None:
                    raise ConversionError("More than one TimeOfCreation found", "ASDM")
                # strip off any leading and trailing whitespace
                asdmToC = ArrayTime(thisNode.firstChild.data.strip())
            elif nodeName == "startTimeDurationInXML":
                if hasStartTimeDurationInXML:
                    # it's already been seen
                    raise ConversionError(
                        "More than one startTimeDurationInXML found", "ASDM"
                    )
                ArrayTimeInterval.setStartTimeDurationInXML(True)
                hasStartTimeDurationInXML = True
            elif nodeName == "startTimeDurationInBin":
                if hasStartTimeDurationInBin:
                    # it's already been seen
                    raise ConversionError(
                        "More than one startTimeDurationInBin found", "ASDM"
                    )
                ArrayTimeInterval.setStartTimeDurationInBin(True)
                hasStartTimeDurationInBin = True
            elif nodeName == "Table":
                # each table must have one of Name, NumberRows, and Entity
                # allow for a missing Entity if NumberRows is 0
                tabName = None
                tabSize = None
                tabEntity = None

                for thisTabNode in thisNode.childNodes:
                    tabNodeName = thisTabNode.nodeName
                    if tabNodeName == "Name":
                        if tabName is not None:
                            raise ConversionError(
                                "More than one Name seen for the same Table", "ASDM"
                            )
                        # strip off any leading and trailing whitespace
                        tabName = thisTabNode.firstChild.data.strip()
                    elif tabNodeName == "NumberRows":
                        if tabSize is not None:
                            raise ConversionError(
                                "More than one NumberOfRows seen for the same Table",
                                "ASDM",
                            )
                        # it's not necessary to strip the leading and trailing whitepspace, conversion to an int won't care
                        tabSize = int(thisTabNode.firstChild.data)
                    elif tabNodeName == "Entity":
                        if tabEntity is not None:
                            raise ConversionError(
                                "More than one Entity seen for the same Table", "ASDM"
                            )
                        tabEntity = Entity(thisTabNode.toxml())

                # name and size must be there
                if tabName is None or tabSize is None:
                    raise ConversionError(
                        "A table is not named or the number of rows is not given",
                        "ASDM",
                    )
                if tabSize > 0:
                    if tabEntity is None:
                        msg = "No Entity given for %s table of size %s" % (
                            tabName,
                            tabSize,
                        )
                        raise ConversionError(msg, "ASDM")
                    # remember all non-zero tables in _tableEntity
                    self._tableEntity[tabName] = tabEntity

        if asdmEntity is None:
            raise ConversionError("No Entity seen for ASDM element", "ASDM")
        if asdmToC is None:
            raise ConversionError("No Entity seen for ASDM element", "ASDM")

        # mark the tables that were found having a non-zero size as not present in memory
        # so that they can be loaded on demand as necessary

        if "Main" in self._tableEntity:
            self._main.setNotPresentInMemory()

        if "AlmaRadiometer" in self._tableEntity:
            self._almaRadiometer.setNotPresentInMemory()

        if "Annotation" in self._tableEntity:
            self._annotation.setNotPresentInMemory()

        if "Antenna" in self._tableEntity:
            self._antenna.setNotPresentInMemory()

        if "CalAmpli" in self._tableEntity:
            self._calAmpli.setNotPresentInMemory()

        if "CalAntennaSolutions" in self._tableEntity:
            self._calAntennaSolutions.setNotPresentInMemory()

        if "CalAppPhase" in self._tableEntity:
            self._calAppPhase.setNotPresentInMemory()

        if "CalAtmosphere" in self._tableEntity:
            self._calAtmosphere.setNotPresentInMemory()

        if "CalBandpass" in self._tableEntity:
            self._calBandpass.setNotPresentInMemory()

        if "CalCurve" in self._tableEntity:
            self._calCurve.setNotPresentInMemory()

        if "CalData" in self._tableEntity:
            self._calData.setNotPresentInMemory()

        if "CalDelay" in self._tableEntity:
            self._calDelay.setNotPresentInMemory()

        if "CalDevice" in self._tableEntity:
            self._calDevice.setNotPresentInMemory()

        if "CalFlux" in self._tableEntity:
            self._calFlux.setNotPresentInMemory()

        if "CalFocus" in self._tableEntity:
            self._calFocus.setNotPresentInMemory()

        if "CalFocusModel" in self._tableEntity:
            self._calFocusModel.setNotPresentInMemory()

        if "CalGain" in self._tableEntity:
            self._calGain.setNotPresentInMemory()

        if "CalHolography" in self._tableEntity:
            self._calHolography.setNotPresentInMemory()

        if "CalPhase" in self._tableEntity:
            self._calPhase.setNotPresentInMemory()

        if "CalPointing" in self._tableEntity:
            self._calPointing.setNotPresentInMemory()

        if "CalPointingModel" in self._tableEntity:
            self._calPointingModel.setNotPresentInMemory()

        if "CalPosition" in self._tableEntity:
            self._calPosition.setNotPresentInMemory()

        if "CalPrimaryBeam" in self._tableEntity:
            self._calPrimaryBeam.setNotPresentInMemory()

        if "CalReduction" in self._tableEntity:
            self._calReduction.setNotPresentInMemory()

        if "CalSeeing" in self._tableEntity:
            self._calSeeing.setNotPresentInMemory()

        if "CalWVR" in self._tableEntity:
            self._calWVR.setNotPresentInMemory()

        if "ConfigDescription" in self._tableEntity:
            self._configDescription.setNotPresentInMemory()

        if "CorrelatorMode" in self._tableEntity:
            self._correlatorMode.setNotPresentInMemory()

        if "DataDescription" in self._tableEntity:
            self._dataDescription.setNotPresentInMemory()

        if "DelayModel" in self._tableEntity:
            self._delayModel.setNotPresentInMemory()

        if "DelayModelFixedParameters" in self._tableEntity:
            self._delayModelFixedParameters.setNotPresentInMemory()

        if "DelayModelVariableParameters" in self._tableEntity:
            self._delayModelVariableParameters.setNotPresentInMemory()

        if "Doppler" in self._tableEntity:
            self._doppler.setNotPresentInMemory()

        if "Ephemeris" in self._tableEntity:
            self._ephemeris.setNotPresentInMemory()

        if "ExecBlock" in self._tableEntity:
            self._execBlock.setNotPresentInMemory()

        if "Feed" in self._tableEntity:
            self._feed.setNotPresentInMemory()

        if "Field" in self._tableEntity:
            self._field.setNotPresentInMemory()

        if "Flag" in self._tableEntity:
            self._flag.setNotPresentInMemory()

        if "FlagCmd" in self._tableEntity:
            self._flagCmd.setNotPresentInMemory()

        if "Focus" in self._tableEntity:
            self._focus.setNotPresentInMemory()

        if "FocusModel" in self._tableEntity:
            self._focusModel.setNotPresentInMemory()

        if "FreqOffset" in self._tableEntity:
            self._freqOffset.setNotPresentInMemory()

        if "GainTracking" in self._tableEntity:
            self._gainTracking.setNotPresentInMemory()

        if "History" in self._tableEntity:
            self._history.setNotPresentInMemory()

        if "Holography" in self._tableEntity:
            self._holography.setNotPresentInMemory()

        if "Observation" in self._tableEntity:
            self._observation.setNotPresentInMemory()

        if "Pointing" in self._tableEntity:
            self._pointing.setNotPresentInMemory()

        if "PointingModel" in self._tableEntity:
            self._pointingModel.setNotPresentInMemory()

        if "Polarization" in self._tableEntity:
            self._polarization.setNotPresentInMemory()

        if "Processor" in self._tableEntity:
            self._processor.setNotPresentInMemory()

        if "Pulsar" in self._tableEntity:
            self._pulsar.setNotPresentInMemory()

        if "Receiver" in self._tableEntity:
            self._receiver.setNotPresentInMemory()

        if "SBSummary" in self._tableEntity:
            self._sBSummary.setNotPresentInMemory()

        if "Scale" in self._tableEntity:
            self._scale.setNotPresentInMemory()

        if "Scan" in self._tableEntity:
            self._scan.setNotPresentInMemory()

        if "Seeing" in self._tableEntity:
            self._seeing.setNotPresentInMemory()

        if "Source" in self._tableEntity:
            self._source.setNotPresentInMemory()

        if "SpectralWindow" in self._tableEntity:
            self._spectralWindow.setNotPresentInMemory()

        if "SquareLawDetector" in self._tableEntity:
            self._squareLawDetector.setNotPresentInMemory()

        if "State" in self._tableEntity:
            self._state.setNotPresentInMemory()

        if "Station" in self._tableEntity:
            self._station.setNotPresentInMemory()

        if "Subscan" in self._tableEntity:
            self._subscan.setNotPresentInMemory()

        if "SwitchCycle" in self._tableEntity:
            self._switchCycle.setNotPresentInMemory()

        if "SysCal" in self._tableEntity:
            self._sysCal.setNotPresentInMemory()

        if "SysPower" in self._tableEntity:
            self._sysPower.setNotPresentInMemory()

        if "TotalPower" in self._tableEntity:
            self._totalPower.setNotPresentInMemory()

        if "VLAWVR" in self._tableEntity:
            self._vLAWVR.setNotPresentInMemory()

        if "WVMCal" in self._tableEntity:
            self._wVMCal.setNotPresentInMemory()

        if "Weather" in self._tableEntity:
            self._weather.setNotPresentInMemory()

        self.setEntity(asdmEntity)
        self.setTimeOfCreation(asdmToC)

    @staticmethod
    def getFromXML(directory):
        """
        Get an ASDM dataset, given the full path name of the
        directory containing the XML version of the dataset.
        @param xmlDirectory The full path name of the directory
        containing this dataset.
        return The complete dataset that belongs to the container
        in this directory.
        raises ConversionException If any error occurs reading the
        files in the directory or in converting the tables from XML.
        """
        thisASDM = ASDM()
        thisASDM.setFromFile(directory)
        return thisASDM

    def toFile(self, directory):
        """
        Write this ASDM dataset to the specified directory
        as a collection of files.

        The container itself is written into an XML file. Each table of the container
        having at least one row is written into a binary or an XML file depending on
        the value of its "fileAsBin" field.

        param directory The directory to which this dataset is written.
        raises ConversionException If any error occurs in converting the
        container.  This method will not overwrite
        any existing file; a ConversionException is also
        raised in this case.
        """
        # Check if the directory exists
        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannnot write into directory "
                + directory
                + ". This file already exists and is not a directory",
                "ASDM",
            )

        if not os.path.exists(directory):
            try:
                os.mkdir(directory)
            except Exception as ex:
                # rethrow this as a ConversionException
                raise ConversionException(
                    "Could not create directory " + directory, "ASDM"
                ) from None

        fileName = None
        if self._fileAsBin:
            # this should never happen for an ASDM
            fileName = os.path.join(directory, "ASDM.bin")
        else:
            fileName = os.path.join(directory, "ASDM.xml")

        with open(fileName, "w") as f:
            if self._fileAsBin:
                # this should never happen, Java just passes here without any code
                pass
            else:
                f.write(self.toXML())

        # Then send each of its table to its own file.

        if self.getMain().size() > 0:
            print("writing Main of size = " + str(self.getMain().size()))
            self.getMain().toFile(directory)

        if self.getAlmaRadiometer().size() > 0:
            print(
                "writing AlmaRadiometer of size = "
                + str(self.getAlmaRadiometer().size())
            )
            self.getAlmaRadiometer().toFile(directory)

        if self.getAnnotation().size() > 0:
            print("writing Annotation of size = " + str(self.getAnnotation().size()))
            self.getAnnotation().toFile(directory)

        if self.getAntenna().size() > 0:
            print("writing Antenna of size = " + str(self.getAntenna().size()))
            self.getAntenna().toFile(directory)

        if self.getCalAmpli().size() > 0:
            print("writing CalAmpli of size = " + str(self.getCalAmpli().size()))
            self.getCalAmpli().toFile(directory)

        if self.getCalAntennaSolutions().size() > 0:
            print(
                "writing CalAntennaSolutions of size = "
                + str(self.getCalAntennaSolutions().size())
            )
            self.getCalAntennaSolutions().toFile(directory)

        if self.getCalAppPhase().size() > 0:
            print("writing CalAppPhase of size = " + str(self.getCalAppPhase().size()))
            self.getCalAppPhase().toFile(directory)

        if self.getCalAtmosphere().size() > 0:
            print(
                "writing CalAtmosphere of size = " + str(self.getCalAtmosphere().size())
            )
            self.getCalAtmosphere().toFile(directory)

        if self.getCalBandpass().size() > 0:
            print("writing CalBandpass of size = " + str(self.getCalBandpass().size()))
            self.getCalBandpass().toFile(directory)

        if self.getCalCurve().size() > 0:
            print("writing CalCurve of size = " + str(self.getCalCurve().size()))
            self.getCalCurve().toFile(directory)

        if self.getCalData().size() > 0:
            print("writing CalData of size = " + str(self.getCalData().size()))
            self.getCalData().toFile(directory)

        if self.getCalDelay().size() > 0:
            print("writing CalDelay of size = " + str(self.getCalDelay().size()))
            self.getCalDelay().toFile(directory)

        if self.getCalDevice().size() > 0:
            print("writing CalDevice of size = " + str(self.getCalDevice().size()))
            self.getCalDevice().toFile(directory)

        if self.getCalFlux().size() > 0:
            print("writing CalFlux of size = " + str(self.getCalFlux().size()))
            self.getCalFlux().toFile(directory)

        if self.getCalFocus().size() > 0:
            print("writing CalFocus of size = " + str(self.getCalFocus().size()))
            self.getCalFocus().toFile(directory)

        if self.getCalFocusModel().size() > 0:
            print(
                "writing CalFocusModel of size = " + str(self.getCalFocusModel().size())
            )
            self.getCalFocusModel().toFile(directory)

        if self.getCalGain().size() > 0:
            print("writing CalGain of size = " + str(self.getCalGain().size()))
            self.getCalGain().toFile(directory)

        if self.getCalHolography().size() > 0:
            print(
                "writing CalHolography of size = " + str(self.getCalHolography().size())
            )
            self.getCalHolography().toFile(directory)

        if self.getCalPhase().size() > 0:
            print("writing CalPhase of size = " + str(self.getCalPhase().size()))
            self.getCalPhase().toFile(directory)

        if self.getCalPointing().size() > 0:
            print("writing CalPointing of size = " + str(self.getCalPointing().size()))
            self.getCalPointing().toFile(directory)

        if self.getCalPointingModel().size() > 0:
            print(
                "writing CalPointingModel of size = "
                + str(self.getCalPointingModel().size())
            )
            self.getCalPointingModel().toFile(directory)

        if self.getCalPosition().size() > 0:
            print("writing CalPosition of size = " + str(self.getCalPosition().size()))
            self.getCalPosition().toFile(directory)

        if self.getCalPrimaryBeam().size() > 0:
            print(
                "writing CalPrimaryBeam of size = "
                + str(self.getCalPrimaryBeam().size())
            )
            self.getCalPrimaryBeam().toFile(directory)

        if self.getCalReduction().size() > 0:
            print(
                "writing CalReduction of size = " + str(self.getCalReduction().size())
            )
            self.getCalReduction().toFile(directory)

        if self.getCalSeeing().size() > 0:
            print("writing CalSeeing of size = " + str(self.getCalSeeing().size()))
            self.getCalSeeing().toFile(directory)

        if self.getCalWVR().size() > 0:
            print("writing CalWVR of size = " + str(self.getCalWVR().size()))
            self.getCalWVR().toFile(directory)

        if self.getConfigDescription().size() > 0:
            print(
                "writing ConfigDescription of size = "
                + str(self.getConfigDescription().size())
            )
            self.getConfigDescription().toFile(directory)

        if self.getCorrelatorMode().size() > 0:
            print(
                "writing CorrelatorMode of size = "
                + str(self.getCorrelatorMode().size())
            )
            self.getCorrelatorMode().toFile(directory)

        if self.getDataDescription().size() > 0:
            print(
                "writing DataDescription of size = "
                + str(self.getDataDescription().size())
            )
            self.getDataDescription().toFile(directory)

        if self.getDelayModel().size() > 0:
            print("writing DelayModel of size = " + str(self.getDelayModel().size()))
            self.getDelayModel().toFile(directory)

        if self.getDelayModelFixedParameters().size() > 0:
            print(
                "writing DelayModelFixedParameters of size = "
                + str(self.getDelayModelFixedParameters().size())
            )
            self.getDelayModelFixedParameters().toFile(directory)

        if self.getDelayModelVariableParameters().size() > 0:
            print(
                "writing DelayModelVariableParameters of size = "
                + str(self.getDelayModelVariableParameters().size())
            )
            self.getDelayModelVariableParameters().toFile(directory)

        if self.getDoppler().size() > 0:
            print("writing Doppler of size = " + str(self.getDoppler().size()))
            self.getDoppler().toFile(directory)

        if self.getEphemeris().size() > 0:
            print("writing Ephemeris of size = " + str(self.getEphemeris().size()))
            self.getEphemeris().toFile(directory)

        if self.getExecBlock().size() > 0:
            print("writing ExecBlock of size = " + str(self.getExecBlock().size()))
            self.getExecBlock().toFile(directory)

        if self.getFeed().size() > 0:
            print("writing Feed of size = " + str(self.getFeed().size()))
            self.getFeed().toFile(directory)

        if self.getField().size() > 0:
            print("writing Field of size = " + str(self.getField().size()))
            self.getField().toFile(directory)

        if self.getFlag().size() > 0:
            print("writing Flag of size = " + str(self.getFlag().size()))
            self.getFlag().toFile(directory)

        if self.getFlagCmd().size() > 0:
            print("writing FlagCmd of size = " + str(self.getFlagCmd().size()))
            self.getFlagCmd().toFile(directory)

        if self.getFocus().size() > 0:
            print("writing Focus of size = " + str(self.getFocus().size()))
            self.getFocus().toFile(directory)

        if self.getFocusModel().size() > 0:
            print("writing FocusModel of size = " + str(self.getFocusModel().size()))
            self.getFocusModel().toFile(directory)

        if self.getFreqOffset().size() > 0:
            print("writing FreqOffset of size = " + str(self.getFreqOffset().size()))
            self.getFreqOffset().toFile(directory)

        if self.getGainTracking().size() > 0:
            print(
                "writing GainTracking of size = " + str(self.getGainTracking().size())
            )
            self.getGainTracking().toFile(directory)

        if self.getHistory().size() > 0:
            print("writing History of size = " + str(self.getHistory().size()))
            self.getHistory().toFile(directory)

        if self.getHolography().size() > 0:
            print("writing Holography of size = " + str(self.getHolography().size()))
            self.getHolography().toFile(directory)

        if self.getObservation().size() > 0:
            print("writing Observation of size = " + str(self.getObservation().size()))
            self.getObservation().toFile(directory)

        if self.getPointing().size() > 0:
            print("writing Pointing of size = " + str(self.getPointing().size()))
            self.getPointing().toFile(directory)

        if self.getPointingModel().size() > 0:
            print(
                "writing PointingModel of size = " + str(self.getPointingModel().size())
            )
            self.getPointingModel().toFile(directory)

        if self.getPolarization().size() > 0:
            print(
                "writing Polarization of size = " + str(self.getPolarization().size())
            )
            self.getPolarization().toFile(directory)

        if self.getProcessor().size() > 0:
            print("writing Processor of size = " + str(self.getProcessor().size()))
            self.getProcessor().toFile(directory)

        if self.getPulsar().size() > 0:
            print("writing Pulsar of size = " + str(self.getPulsar().size()))
            self.getPulsar().toFile(directory)

        if self.getReceiver().size() > 0:
            print("writing Receiver of size = " + str(self.getReceiver().size()))
            self.getReceiver().toFile(directory)

        if self.getSBSummary().size() > 0:
            print("writing SBSummary of size = " + str(self.getSBSummary().size()))
            self.getSBSummary().toFile(directory)

        if self.getScale().size() > 0:
            print("writing Scale of size = " + str(self.getScale().size()))
            self.getScale().toFile(directory)

        if self.getScan().size() > 0:
            print("writing Scan of size = " + str(self.getScan().size()))
            self.getScan().toFile(directory)

        if self.getSeeing().size() > 0:
            print("writing Seeing of size = " + str(self.getSeeing().size()))
            self.getSeeing().toFile(directory)

        if self.getSource().size() > 0:
            print("writing Source of size = " + str(self.getSource().size()))
            self.getSource().toFile(directory)

        if self.getSpectralWindow().size() > 0:
            print(
                "writing SpectralWindow of size = "
                + str(self.getSpectralWindow().size())
            )
            self.getSpectralWindow().toFile(directory)

        if self.getSquareLawDetector().size() > 0:
            print(
                "writing SquareLawDetector of size = "
                + str(self.getSquareLawDetector().size())
            )
            self.getSquareLawDetector().toFile(directory)

        if self.getState().size() > 0:
            print("writing State of size = " + str(self.getState().size()))
            self.getState().toFile(directory)

        if self.getStation().size() > 0:
            print("writing Station of size = " + str(self.getStation().size()))
            self.getStation().toFile(directory)

        if self.getSubscan().size() > 0:
            print("writing Subscan of size = " + str(self.getSubscan().size()))
            self.getSubscan().toFile(directory)

        if self.getSwitchCycle().size() > 0:
            print("writing SwitchCycle of size = " + str(self.getSwitchCycle().size()))
            self.getSwitchCycle().toFile(directory)

        if self.getSysCal().size() > 0:
            print("writing SysCal of size = " + str(self.getSysCal().size()))
            self.getSysCal().toFile(directory)

        if self.getSysPower().size() > 0:
            print("writing SysPower of size = " + str(self.getSysPower().size()))
            self.getSysPower().toFile(directory)

        if self.getTotalPower().size() > 0:
            print("writing TotalPower of size = " + str(self.getTotalPower().size()))
            self.getTotalPower().toFile(directory)

        if self.getVLAWVR().size() > 0:
            print("writing VLAWVR of size = " + str(self.getVLAWVR().size()))
            self.getVLAWVR().toFile(directory)

        if self.getWVMCal().size() > 0:
            print("writing WVMCal of size = " + str(self.getWVMCal().size()))
            self.getWVMCal().toFile(directory)

        if self.getWeather().size() > 0:
            print("writing Weather of size = " + str(self.getWeather().size()))
            self.getWeather().toFile(directory)

    def setFromFile(self, directory):
        """
        Reads and parses a collection of files as those produced by the toFile method.
        This dataset is populated with the result of the parsing.
        param directory The name of the directory containing the files.
        raises ConversionException If any error occurs while reading the
        files in the directory or parsing them.

        os.path.expanduser is used on directory before directory is used.
        The expanded version is kept internally and returned and used as necessary.
        """

        directory = os.path.expanduser(directory)
        # directory must exist as a directory.
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " does not exist or is not a directory.",
                "ASDM",
            )

        self._directory = directory

        if self._fileAsBin:
            raise RuntimeError("fileAsBin not implemented for ASDM")
        else:
            fileName = os.path.join(directory, "ASDM.xml")

            if not os.path.exists(fileName):
                raise ConversionException(
                    "File " + fileName + " does not exist.", "ASDM"
                )

            # c++ uses ASDMUtils to find the origin and version and as necessary it
            # applies a transfer to massage older xml into the current version
            # skip that step for now and use the xml as is (Java does that, but it
            # makes it impossible to use these classes to read older versions

            xmlstr = None
            with open(fileName) as f:
                xmlstr = f.read()

            if xmlstr is None:
                raise ConversionException(filename + " is empty", "ASDM")

            self.fromXML(xmlstr)

    def getEntity(self):
        return self._entity

    def setEntity(self, e):
        if not isinstance(e, Entity):
            raise ValueError("invalid argument to setEntity, must be an Entity")
        self._entity = e

    def getTable(self, tableName):
        """
        Get the table by name. Returns the named table.
        raises a ValueError if tableName is not a known table.
        """
        if tableName not in self._tableGetters:
            raise ValueError(tableName + " is not a known table")
        theGetter = self._tableGetters[tableName]
        return theGetter()

    def status(self):
        print("tables status")

        if "Main" in self._tableEntity:
            print(
                "'Main' : IS present in _tableEntity, presentInMemory = "
                + str(self._main._presentInMemory)
                + " size = "
                + str(self._main.size())
            )
        else:
            print(
                "'Main' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._main._presentInMemory)
                + " size = "
                + str(self._main.size())
            )

        if "AlmaRadiometer" in self._tableEntity:
            print(
                "'AlmaRadiometer' : IS present in _tableEntity, presentInMemory = "
                + str(self._almaRadiometer._presentInMemory)
                + " size = "
                + str(self._almaRadiometer.size())
            )
        else:
            print(
                "'AlmaRadiometer' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._almaRadiometer._presentInMemory)
                + " size = "
                + str(self._almaRadiometer.size())
            )

        if "Annotation" in self._tableEntity:
            print(
                "'Annotation' : IS present in _tableEntity, presentInMemory = "
                + str(self._annotation._presentInMemory)
                + " size = "
                + str(self._annotation.size())
            )
        else:
            print(
                "'Annotation' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._annotation._presentInMemory)
                + " size = "
                + str(self._annotation.size())
            )

        if "Antenna" in self._tableEntity:
            print(
                "'Antenna' : IS present in _tableEntity, presentInMemory = "
                + str(self._antenna._presentInMemory)
                + " size = "
                + str(self._antenna.size())
            )
        else:
            print(
                "'Antenna' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._antenna._presentInMemory)
                + " size = "
                + str(self._antenna.size())
            )

        if "CalAmpli" in self._tableEntity:
            print(
                "'CalAmpli' : IS present in _tableEntity, presentInMemory = "
                + str(self._calAmpli._presentInMemory)
                + " size = "
                + str(self._calAmpli.size())
            )
        else:
            print(
                "'CalAmpli' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calAmpli._presentInMemory)
                + " size = "
                + str(self._calAmpli.size())
            )

        if "CalAntennaSolutions" in self._tableEntity:
            print(
                "'CalAntennaSolutions' : IS present in _tableEntity, presentInMemory = "
                + str(self._calAntennaSolutions._presentInMemory)
                + " size = "
                + str(self._calAntennaSolutions.size())
            )
        else:
            print(
                "'CalAntennaSolutions' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calAntennaSolutions._presentInMemory)
                + " size = "
                + str(self._calAntennaSolutions.size())
            )

        if "CalAppPhase" in self._tableEntity:
            print(
                "'CalAppPhase' : IS present in _tableEntity, presentInMemory = "
                + str(self._calAppPhase._presentInMemory)
                + " size = "
                + str(self._calAppPhase.size())
            )
        else:
            print(
                "'CalAppPhase' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calAppPhase._presentInMemory)
                + " size = "
                + str(self._calAppPhase.size())
            )

        if "CalAtmosphere" in self._tableEntity:
            print(
                "'CalAtmosphere' : IS present in _tableEntity, presentInMemory = "
                + str(self._calAtmosphere._presentInMemory)
                + " size = "
                + str(self._calAtmosphere.size())
            )
        else:
            print(
                "'CalAtmosphere' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calAtmosphere._presentInMemory)
                + " size = "
                + str(self._calAtmosphere.size())
            )

        if "CalBandpass" in self._tableEntity:
            print(
                "'CalBandpass' : IS present in _tableEntity, presentInMemory = "
                + str(self._calBandpass._presentInMemory)
                + " size = "
                + str(self._calBandpass.size())
            )
        else:
            print(
                "'CalBandpass' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calBandpass._presentInMemory)
                + " size = "
                + str(self._calBandpass.size())
            )

        if "CalCurve" in self._tableEntity:
            print(
                "'CalCurve' : IS present in _tableEntity, presentInMemory = "
                + str(self._calCurve._presentInMemory)
                + " size = "
                + str(self._calCurve.size())
            )
        else:
            print(
                "'CalCurve' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calCurve._presentInMemory)
                + " size = "
                + str(self._calCurve.size())
            )

        if "CalData" in self._tableEntity:
            print(
                "'CalData' : IS present in _tableEntity, presentInMemory = "
                + str(self._calData._presentInMemory)
                + " size = "
                + str(self._calData.size())
            )
        else:
            print(
                "'CalData' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calData._presentInMemory)
                + " size = "
                + str(self._calData.size())
            )

        if "CalDelay" in self._tableEntity:
            print(
                "'CalDelay' : IS present in _tableEntity, presentInMemory = "
                + str(self._calDelay._presentInMemory)
                + " size = "
                + str(self._calDelay.size())
            )
        else:
            print(
                "'CalDelay' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calDelay._presentInMemory)
                + " size = "
                + str(self._calDelay.size())
            )

        if "CalDevice" in self._tableEntity:
            print(
                "'CalDevice' : IS present in _tableEntity, presentInMemory = "
                + str(self._calDevice._presentInMemory)
                + " size = "
                + str(self._calDevice.size())
            )
        else:
            print(
                "'CalDevice' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calDevice._presentInMemory)
                + " size = "
                + str(self._calDevice.size())
            )

        if "CalFlux" in self._tableEntity:
            print(
                "'CalFlux' : IS present in _tableEntity, presentInMemory = "
                + str(self._calFlux._presentInMemory)
                + " size = "
                + str(self._calFlux.size())
            )
        else:
            print(
                "'CalFlux' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calFlux._presentInMemory)
                + " size = "
                + str(self._calFlux.size())
            )

        if "CalFocus" in self._tableEntity:
            print(
                "'CalFocus' : IS present in _tableEntity, presentInMemory = "
                + str(self._calFocus._presentInMemory)
                + " size = "
                + str(self._calFocus.size())
            )
        else:
            print(
                "'CalFocus' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calFocus._presentInMemory)
                + " size = "
                + str(self._calFocus.size())
            )

        if "CalFocusModel" in self._tableEntity:
            print(
                "'CalFocusModel' : IS present in _tableEntity, presentInMemory = "
                + str(self._calFocusModel._presentInMemory)
                + " size = "
                + str(self._calFocusModel.size())
            )
        else:
            print(
                "'CalFocusModel' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calFocusModel._presentInMemory)
                + " size = "
                + str(self._calFocusModel.size())
            )

        if "CalGain" in self._tableEntity:
            print(
                "'CalGain' : IS present in _tableEntity, presentInMemory = "
                + str(self._calGain._presentInMemory)
                + " size = "
                + str(self._calGain.size())
            )
        else:
            print(
                "'CalGain' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calGain._presentInMemory)
                + " size = "
                + str(self._calGain.size())
            )

        if "CalHolography" in self._tableEntity:
            print(
                "'CalHolography' : IS present in _tableEntity, presentInMemory = "
                + str(self._calHolography._presentInMemory)
                + " size = "
                + str(self._calHolography.size())
            )
        else:
            print(
                "'CalHolography' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calHolography._presentInMemory)
                + " size = "
                + str(self._calHolography.size())
            )

        if "CalPhase" in self._tableEntity:
            print(
                "'CalPhase' : IS present in _tableEntity, presentInMemory = "
                + str(self._calPhase._presentInMemory)
                + " size = "
                + str(self._calPhase.size())
            )
        else:
            print(
                "'CalPhase' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calPhase._presentInMemory)
                + " size = "
                + str(self._calPhase.size())
            )

        if "CalPointing" in self._tableEntity:
            print(
                "'CalPointing' : IS present in _tableEntity, presentInMemory = "
                + str(self._calPointing._presentInMemory)
                + " size = "
                + str(self._calPointing.size())
            )
        else:
            print(
                "'CalPointing' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calPointing._presentInMemory)
                + " size = "
                + str(self._calPointing.size())
            )

        if "CalPointingModel" in self._tableEntity:
            print(
                "'CalPointingModel' : IS present in _tableEntity, presentInMemory = "
                + str(self._calPointingModel._presentInMemory)
                + " size = "
                + str(self._calPointingModel.size())
            )
        else:
            print(
                "'CalPointingModel' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calPointingModel._presentInMemory)
                + " size = "
                + str(self._calPointingModel.size())
            )

        if "CalPosition" in self._tableEntity:
            print(
                "'CalPosition' : IS present in _tableEntity, presentInMemory = "
                + str(self._calPosition._presentInMemory)
                + " size = "
                + str(self._calPosition.size())
            )
        else:
            print(
                "'CalPosition' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calPosition._presentInMemory)
                + " size = "
                + str(self._calPosition.size())
            )

        if "CalPrimaryBeam" in self._tableEntity:
            print(
                "'CalPrimaryBeam' : IS present in _tableEntity, presentInMemory = "
                + str(self._calPrimaryBeam._presentInMemory)
                + " size = "
                + str(self._calPrimaryBeam.size())
            )
        else:
            print(
                "'CalPrimaryBeam' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calPrimaryBeam._presentInMemory)
                + " size = "
                + str(self._calPrimaryBeam.size())
            )

        if "CalReduction" in self._tableEntity:
            print(
                "'CalReduction' : IS present in _tableEntity, presentInMemory = "
                + str(self._calReduction._presentInMemory)
                + " size = "
                + str(self._calReduction.size())
            )
        else:
            print(
                "'CalReduction' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calReduction._presentInMemory)
                + " size = "
                + str(self._calReduction.size())
            )

        if "CalSeeing" in self._tableEntity:
            print(
                "'CalSeeing' : IS present in _tableEntity, presentInMemory = "
                + str(self._calSeeing._presentInMemory)
                + " size = "
                + str(self._calSeeing.size())
            )
        else:
            print(
                "'CalSeeing' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calSeeing._presentInMemory)
                + " size = "
                + str(self._calSeeing.size())
            )

        if "CalWVR" in self._tableEntity:
            print(
                "'CalWVR' : IS present in _tableEntity, presentInMemory = "
                + str(self._calWVR._presentInMemory)
                + " size = "
                + str(self._calWVR.size())
            )
        else:
            print(
                "'CalWVR' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._calWVR._presentInMemory)
                + " size = "
                + str(self._calWVR.size())
            )

        if "ConfigDescription" in self._tableEntity:
            print(
                "'ConfigDescription' : IS present in _tableEntity, presentInMemory = "
                + str(self._configDescription._presentInMemory)
                + " size = "
                + str(self._configDescription.size())
            )
        else:
            print(
                "'ConfigDescription' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._configDescription._presentInMemory)
                + " size = "
                + str(self._configDescription.size())
            )

        if "CorrelatorMode" in self._tableEntity:
            print(
                "'CorrelatorMode' : IS present in _tableEntity, presentInMemory = "
                + str(self._correlatorMode._presentInMemory)
                + " size = "
                + str(self._correlatorMode.size())
            )
        else:
            print(
                "'CorrelatorMode' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._correlatorMode._presentInMemory)
                + " size = "
                + str(self._correlatorMode.size())
            )

        if "DataDescription" in self._tableEntity:
            print(
                "'DataDescription' : IS present in _tableEntity, presentInMemory = "
                + str(self._dataDescription._presentInMemory)
                + " size = "
                + str(self._dataDescription.size())
            )
        else:
            print(
                "'DataDescription' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._dataDescription._presentInMemory)
                + " size = "
                + str(self._dataDescription.size())
            )

        if "DelayModel" in self._tableEntity:
            print(
                "'DelayModel' : IS present in _tableEntity, presentInMemory = "
                + str(self._delayModel._presentInMemory)
                + " size = "
                + str(self._delayModel.size())
            )
        else:
            print(
                "'DelayModel' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._delayModel._presentInMemory)
                + " size = "
                + str(self._delayModel.size())
            )

        if "DelayModelFixedParameters" in self._tableEntity:
            print(
                "'DelayModelFixedParameters' : IS present in _tableEntity, presentInMemory = "
                + str(self._delayModelFixedParameters._presentInMemory)
                + " size = "
                + str(self._delayModelFixedParameters.size())
            )
        else:
            print(
                "'DelayModelFixedParameters' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._delayModelFixedParameters._presentInMemory)
                + " size = "
                + str(self._delayModelFixedParameters.size())
            )

        if "DelayModelVariableParameters" in self._tableEntity:
            print(
                "'DelayModelVariableParameters' : IS present in _tableEntity, presentInMemory = "
                + str(self._delayModelVariableParameters._presentInMemory)
                + " size = "
                + str(self._delayModelVariableParameters.size())
            )
        else:
            print(
                "'DelayModelVariableParameters' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._delayModelVariableParameters._presentInMemory)
                + " size = "
                + str(self._delayModelVariableParameters.size())
            )

        if "Doppler" in self._tableEntity:
            print(
                "'Doppler' : IS present in _tableEntity, presentInMemory = "
                + str(self._doppler._presentInMemory)
                + " size = "
                + str(self._doppler.size())
            )
        else:
            print(
                "'Doppler' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._doppler._presentInMemory)
                + " size = "
                + str(self._doppler.size())
            )

        if "Ephemeris" in self._tableEntity:
            print(
                "'Ephemeris' : IS present in _tableEntity, presentInMemory = "
                + str(self._ephemeris._presentInMemory)
                + " size = "
                + str(self._ephemeris.size())
            )
        else:
            print(
                "'Ephemeris' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._ephemeris._presentInMemory)
                + " size = "
                + str(self._ephemeris.size())
            )

        if "ExecBlock" in self._tableEntity:
            print(
                "'ExecBlock' : IS present in _tableEntity, presentInMemory = "
                + str(self._execBlock._presentInMemory)
                + " size = "
                + str(self._execBlock.size())
            )
        else:
            print(
                "'ExecBlock' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._execBlock._presentInMemory)
                + " size = "
                + str(self._execBlock.size())
            )

        if "Feed" in self._tableEntity:
            print(
                "'Feed' : IS present in _tableEntity, presentInMemory = "
                + str(self._feed._presentInMemory)
                + " size = "
                + str(self._feed.size())
            )
        else:
            print(
                "'Feed' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._feed._presentInMemory)
                + " size = "
                + str(self._feed.size())
            )

        if "Field" in self._tableEntity:
            print(
                "'Field' : IS present in _tableEntity, presentInMemory = "
                + str(self._field._presentInMemory)
                + " size = "
                + str(self._field.size())
            )
        else:
            print(
                "'Field' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._field._presentInMemory)
                + " size = "
                + str(self._field.size())
            )

        if "Flag" in self._tableEntity:
            print(
                "'Flag' : IS present in _tableEntity, presentInMemory = "
                + str(self._flag._presentInMemory)
                + " size = "
                + str(self._flag.size())
            )
        else:
            print(
                "'Flag' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._flag._presentInMemory)
                + " size = "
                + str(self._flag.size())
            )

        if "FlagCmd" in self._tableEntity:
            print(
                "'FlagCmd' : IS present in _tableEntity, presentInMemory = "
                + str(self._flagCmd._presentInMemory)
                + " size = "
                + str(self._flagCmd.size())
            )
        else:
            print(
                "'FlagCmd' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._flagCmd._presentInMemory)
                + " size = "
                + str(self._flagCmd.size())
            )

        if "Focus" in self._tableEntity:
            print(
                "'Focus' : IS present in _tableEntity, presentInMemory = "
                + str(self._focus._presentInMemory)
                + " size = "
                + str(self._focus.size())
            )
        else:
            print(
                "'Focus' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._focus._presentInMemory)
                + " size = "
                + str(self._focus.size())
            )

        if "FocusModel" in self._tableEntity:
            print(
                "'FocusModel' : IS present in _tableEntity, presentInMemory = "
                + str(self._focusModel._presentInMemory)
                + " size = "
                + str(self._focusModel.size())
            )
        else:
            print(
                "'FocusModel' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._focusModel._presentInMemory)
                + " size = "
                + str(self._focusModel.size())
            )

        if "FreqOffset" in self._tableEntity:
            print(
                "'FreqOffset' : IS present in _tableEntity, presentInMemory = "
                + str(self._freqOffset._presentInMemory)
                + " size = "
                + str(self._freqOffset.size())
            )
        else:
            print(
                "'FreqOffset' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._freqOffset._presentInMemory)
                + " size = "
                + str(self._freqOffset.size())
            )

        if "GainTracking" in self._tableEntity:
            print(
                "'GainTracking' : IS present in _tableEntity, presentInMemory = "
                + str(self._gainTracking._presentInMemory)
                + " size = "
                + str(self._gainTracking.size())
            )
        else:
            print(
                "'GainTracking' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._gainTracking._presentInMemory)
                + " size = "
                + str(self._gainTracking.size())
            )

        if "History" in self._tableEntity:
            print(
                "'History' : IS present in _tableEntity, presentInMemory = "
                + str(self._history._presentInMemory)
                + " size = "
                + str(self._history.size())
            )
        else:
            print(
                "'History' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._history._presentInMemory)
                + " size = "
                + str(self._history.size())
            )

        if "Holography" in self._tableEntity:
            print(
                "'Holography' : IS present in _tableEntity, presentInMemory = "
                + str(self._holography._presentInMemory)
                + " size = "
                + str(self._holography.size())
            )
        else:
            print(
                "'Holography' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._holography._presentInMemory)
                + " size = "
                + str(self._holography.size())
            )

        if "Observation" in self._tableEntity:
            print(
                "'Observation' : IS present in _tableEntity, presentInMemory = "
                + str(self._observation._presentInMemory)
                + " size = "
                + str(self._observation.size())
            )
        else:
            print(
                "'Observation' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._observation._presentInMemory)
                + " size = "
                + str(self._observation.size())
            )

        if "Pointing" in self._tableEntity:
            print(
                "'Pointing' : IS present in _tableEntity, presentInMemory = "
                + str(self._pointing._presentInMemory)
                + " size = "
                + str(self._pointing.size())
            )
        else:
            print(
                "'Pointing' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._pointing._presentInMemory)
                + " size = "
                + str(self._pointing.size())
            )

        if "PointingModel" in self._tableEntity:
            print(
                "'PointingModel' : IS present in _tableEntity, presentInMemory = "
                + str(self._pointingModel._presentInMemory)
                + " size = "
                + str(self._pointingModel.size())
            )
        else:
            print(
                "'PointingModel' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._pointingModel._presentInMemory)
                + " size = "
                + str(self._pointingModel.size())
            )

        if "Polarization" in self._tableEntity:
            print(
                "'Polarization' : IS present in _tableEntity, presentInMemory = "
                + str(self._polarization._presentInMemory)
                + " size = "
                + str(self._polarization.size())
            )
        else:
            print(
                "'Polarization' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._polarization._presentInMemory)
                + " size = "
                + str(self._polarization.size())
            )

        if "Processor" in self._tableEntity:
            print(
                "'Processor' : IS present in _tableEntity, presentInMemory = "
                + str(self._processor._presentInMemory)
                + " size = "
                + str(self._processor.size())
            )
        else:
            print(
                "'Processor' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._processor._presentInMemory)
                + " size = "
                + str(self._processor.size())
            )

        if "Pulsar" in self._tableEntity:
            print(
                "'Pulsar' : IS present in _tableEntity, presentInMemory = "
                + str(self._pulsar._presentInMemory)
                + " size = "
                + str(self._pulsar.size())
            )
        else:
            print(
                "'Pulsar' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._pulsar._presentInMemory)
                + " size = "
                + str(self._pulsar.size())
            )

        if "Receiver" in self._tableEntity:
            print(
                "'Receiver' : IS present in _tableEntity, presentInMemory = "
                + str(self._receiver._presentInMemory)
                + " size = "
                + str(self._receiver.size())
            )
        else:
            print(
                "'Receiver' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._receiver._presentInMemory)
                + " size = "
                + str(self._receiver.size())
            )

        if "SBSummary" in self._tableEntity:
            print(
                "'SBSummary' : IS present in _tableEntity, presentInMemory = "
                + str(self._sBSummary._presentInMemory)
                + " size = "
                + str(self._sBSummary.size())
            )
        else:
            print(
                "'SBSummary' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._sBSummary._presentInMemory)
                + " size = "
                + str(self._sBSummary.size())
            )

        if "Scale" in self._tableEntity:
            print(
                "'Scale' : IS present in _tableEntity, presentInMemory = "
                + str(self._scale._presentInMemory)
                + " size = "
                + str(self._scale.size())
            )
        else:
            print(
                "'Scale' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._scale._presentInMemory)
                + " size = "
                + str(self._scale.size())
            )

        if "Scan" in self._tableEntity:
            print(
                "'Scan' : IS present in _tableEntity, presentInMemory = "
                + str(self._scan._presentInMemory)
                + " size = "
                + str(self._scan.size())
            )
        else:
            print(
                "'Scan' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._scan._presentInMemory)
                + " size = "
                + str(self._scan.size())
            )

        if "Seeing" in self._tableEntity:
            print(
                "'Seeing' : IS present in _tableEntity, presentInMemory = "
                + str(self._seeing._presentInMemory)
                + " size = "
                + str(self._seeing.size())
            )
        else:
            print(
                "'Seeing' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._seeing._presentInMemory)
                + " size = "
                + str(self._seeing.size())
            )

        if "Source" in self._tableEntity:
            print(
                "'Source' : IS present in _tableEntity, presentInMemory = "
                + str(self._source._presentInMemory)
                + " size = "
                + str(self._source.size())
            )
        else:
            print(
                "'Source' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._source._presentInMemory)
                + " size = "
                + str(self._source.size())
            )

        if "SpectralWindow" in self._tableEntity:
            print(
                "'SpectralWindow' : IS present in _tableEntity, presentInMemory = "
                + str(self._spectralWindow._presentInMemory)
                + " size = "
                + str(self._spectralWindow.size())
            )
        else:
            print(
                "'SpectralWindow' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._spectralWindow._presentInMemory)
                + " size = "
                + str(self._spectralWindow.size())
            )

        if "SquareLawDetector" in self._tableEntity:
            print(
                "'SquareLawDetector' : IS present in _tableEntity, presentInMemory = "
                + str(self._squareLawDetector._presentInMemory)
                + " size = "
                + str(self._squareLawDetector.size())
            )
        else:
            print(
                "'SquareLawDetector' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._squareLawDetector._presentInMemory)
                + " size = "
                + str(self._squareLawDetector.size())
            )

        if "State" in self._tableEntity:
            print(
                "'State' : IS present in _tableEntity, presentInMemory = "
                + str(self._state._presentInMemory)
                + " size = "
                + str(self._state.size())
            )
        else:
            print(
                "'State' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._state._presentInMemory)
                + " size = "
                + str(self._state.size())
            )

        if "Station" in self._tableEntity:
            print(
                "'Station' : IS present in _tableEntity, presentInMemory = "
                + str(self._station._presentInMemory)
                + " size = "
                + str(self._station.size())
            )
        else:
            print(
                "'Station' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._station._presentInMemory)
                + " size = "
                + str(self._station.size())
            )

        if "Subscan" in self._tableEntity:
            print(
                "'Subscan' : IS present in _tableEntity, presentInMemory = "
                + str(self._subscan._presentInMemory)
                + " size = "
                + str(self._subscan.size())
            )
        else:
            print(
                "'Subscan' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._subscan._presentInMemory)
                + " size = "
                + str(self._subscan.size())
            )

        if "SwitchCycle" in self._tableEntity:
            print(
                "'SwitchCycle' : IS present in _tableEntity, presentInMemory = "
                + str(self._switchCycle._presentInMemory)
                + " size = "
                + str(self._switchCycle.size())
            )
        else:
            print(
                "'SwitchCycle' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._switchCycle._presentInMemory)
                + " size = "
                + str(self._switchCycle.size())
            )

        if "SysCal" in self._tableEntity:
            print(
                "'SysCal' : IS present in _tableEntity, presentInMemory = "
                + str(self._sysCal._presentInMemory)
                + " size = "
                + str(self._sysCal.size())
            )
        else:
            print(
                "'SysCal' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._sysCal._presentInMemory)
                + " size = "
                + str(self._sysCal.size())
            )

        if "SysPower" in self._tableEntity:
            print(
                "'SysPower' : IS present in _tableEntity, presentInMemory = "
                + str(self._sysPower._presentInMemory)
                + " size = "
                + str(self._sysPower.size())
            )
        else:
            print(
                "'SysPower' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._sysPower._presentInMemory)
                + " size = "
                + str(self._sysPower.size())
            )

        if "TotalPower" in self._tableEntity:
            print(
                "'TotalPower' : IS present in _tableEntity, presentInMemory = "
                + str(self._totalPower._presentInMemory)
                + " size = "
                + str(self._totalPower.size())
            )
        else:
            print(
                "'TotalPower' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._totalPower._presentInMemory)
                + " size = "
                + str(self._totalPower.size())
            )

        if "VLAWVR" in self._tableEntity:
            print(
                "'VLAWVR' : IS present in _tableEntity, presentInMemory = "
                + str(self._vLAWVR._presentInMemory)
                + " size = "
                + str(self._vLAWVR.size())
            )
        else:
            print(
                "'VLAWVR' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._vLAWVR._presentInMemory)
                + " size = "
                + str(self._vLAWVR.size())
            )

        if "WVMCal" in self._tableEntity:
            print(
                "'WVMCal' : IS present in _tableEntity, presentInMemory = "
                + str(self._wVMCal._presentInMemory)
                + " size = "
                + str(self._wVMCal.size())
            )
        else:
            print(
                "'WVMCal' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._wVMCal._presentInMemory)
                + " size = "
                + str(self._wVMCal.size())
            )

        if "Weather" in self._tableEntity:
            print(
                "'Weather' : IS present in _tableEntity, presentInMemory = "
                + str(self._weather._presentInMemory)
                + " size = "
                + str(self._weather.size())
            )
        else:
            print(
                "'Weather' : IS NOT present in _tableEntity, presentInMemory = "
                + str(self._weather._presentInMemory)
                + " size = "
                + str(self._weather.size())
            )
