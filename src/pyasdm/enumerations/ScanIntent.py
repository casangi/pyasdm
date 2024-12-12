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
# /////////////////////////////////////////////////////////////////
# // WARNING!  DO NOT MODIFY THIS FILE!                          //
# //  ---------------------------------------------------------  //
# // | This is generated code!  Do not modify this file.       | //
# // | Any changes will be lost when the file is re-generated. | //
# //  ---------------------------------------------------------  //
# /////////////////////////////////////////////////////////////////
#
# File ScanIntent.py

# to keep track of the attributes added to this class for each value of this enumeration

_scanIntentDict = {}

# the possible enumerations

_CALIBRATE_AMPLI = 0  # Amplitude calibration scan

_CALIBRATE_ATMOSPHERE = 1  # Atmosphere calibration scan

_CALIBRATE_BANDPASS = 2  # Bandpass calibration scan

_CALIBRATE_DELAY = 3  # Delay calibration scan

_CALIBRATE_FLUX = 4  # flux measurement scan.

_CALIBRATE_FOCUS = 5  # Focus calibration scan. Z coordinate to be derived

_CALIBRATE_FOCUS_X = 6  # Focus calibration scan; X focus coordinate to be derived

_CALIBRATE_FOCUS_Y = 7  # Focus calibration scan; Y focus coordinate to be derived

_CALIBRATE_PHASE = 8  # Phase calibration scan

_CALIBRATE_POINTING = 9  # Pointing calibration scan

_CALIBRATE_POLARIZATION = 10  # Polarization calibration scan

_CALIBRATE_SIDEBAND_RATIO = 11  # measure relative gains of sidebands.

_CALIBRATE_WVR = 12  # Data from the water vapor radiometers (and correlation data) are used to derive their calibration parameters.

_DO_SKYDIP = 13  # Skydip calibration scan

_MAP_ANTENNA_SURFACE = 14  # Holography calibration scan

_MAP_PRIMARY_BEAM = 15  # Data on a celestial calibration source are used to derive a map of the primary beam.

_OBSERVE_TARGET = 16  # Target source scan

_CALIBRATE_POL_LEAKAGE = 17  #

_CALIBRATE_POL_ANGLE = 18  #

_TEST = 19  # used for development.

_UNSPECIFIED = 20  # Unspecified scan intent

_CALIBRATE_ANTENNA_POSITION = 21  # Requested by EVLA.

_CALIBRATE_ANTENNA_PHASE = 22  # Requested by EVLA.

_MEASURE_RFI = 23  # Requested by EVLA.

_CALIBRATE_ANTENNA_POINTING_MODEL = 24  # Requested by EVLA.

_SYSTEM_CONFIGURATION = 25  # Requested by EVLA.

_CALIBRATE_APPPHASE_ACTIVE = (
    26  # Calculate and apply phasing solutions. Applicable at ALMA.
)

_CALIBRATE_APPPHASE_PASSIVE = (
    27  # Apply previously obtained phasing solutions. Applicable at ALMA.
)

_OBSERVE_CHECK_SOURCE = 28  #

_CALIBRATE_DIFFGAIN = 29  # Enable a gain differential target type


# their names in a dictionary
_scanIntentNames = {}

_scanIntentNames[_CALIBRATE_AMPLI] = "CALIBRATE_AMPLI"

_scanIntentNames[_CALIBRATE_ATMOSPHERE] = "CALIBRATE_ATMOSPHERE"

_scanIntentNames[_CALIBRATE_BANDPASS] = "CALIBRATE_BANDPASS"

_scanIntentNames[_CALIBRATE_DELAY] = "CALIBRATE_DELAY"

_scanIntentNames[_CALIBRATE_FLUX] = "CALIBRATE_FLUX"

_scanIntentNames[_CALIBRATE_FOCUS] = "CALIBRATE_FOCUS"

_scanIntentNames[_CALIBRATE_FOCUS_X] = "CALIBRATE_FOCUS_X"

_scanIntentNames[_CALIBRATE_FOCUS_Y] = "CALIBRATE_FOCUS_Y"

_scanIntentNames[_CALIBRATE_PHASE] = "CALIBRATE_PHASE"

_scanIntentNames[_CALIBRATE_POINTING] = "CALIBRATE_POINTING"

_scanIntentNames[_CALIBRATE_POLARIZATION] = "CALIBRATE_POLARIZATION"

_scanIntentNames[_CALIBRATE_SIDEBAND_RATIO] = "CALIBRATE_SIDEBAND_RATIO"

_scanIntentNames[_CALIBRATE_WVR] = "CALIBRATE_WVR"

_scanIntentNames[_DO_SKYDIP] = "DO_SKYDIP"

_scanIntentNames[_MAP_ANTENNA_SURFACE] = "MAP_ANTENNA_SURFACE"

_scanIntentNames[_MAP_PRIMARY_BEAM] = "MAP_PRIMARY_BEAM"

_scanIntentNames[_OBSERVE_TARGET] = "OBSERVE_TARGET"

_scanIntentNames[_CALIBRATE_POL_LEAKAGE] = "CALIBRATE_POL_LEAKAGE"

_scanIntentNames[_CALIBRATE_POL_ANGLE] = "CALIBRATE_POL_ANGLE"

_scanIntentNames[_TEST] = "TEST"

_scanIntentNames[_UNSPECIFIED] = "UNSPECIFIED"

_scanIntentNames[_CALIBRATE_ANTENNA_POSITION] = "CALIBRATE_ANTENNA_POSITION"

_scanIntentNames[_CALIBRATE_ANTENNA_PHASE] = "CALIBRATE_ANTENNA_PHASE"

_scanIntentNames[_MEASURE_RFI] = "MEASURE_RFI"

_scanIntentNames[_CALIBRATE_ANTENNA_POINTING_MODEL] = "CALIBRATE_ANTENNA_POINTING_MODEL"

_scanIntentNames[_SYSTEM_CONFIGURATION] = "SYSTEM_CONFIGURATION"

_scanIntentNames[_CALIBRATE_APPPHASE_ACTIVE] = "CALIBRATE_APPPHASE_ACTIVE"

_scanIntentNames[_CALIBRATE_APPPHASE_PASSIVE] = "CALIBRATE_APPPHASE_PASSIVE"

_scanIntentNames[_OBSERVE_CHECK_SOURCE] = "OBSERVE_CHECK_SOURCE"

_scanIntentNames[_CALIBRATE_DIFFGAIN] = "CALIBRATE_DIFFGAIN"


class ScanIntent:
    """
    A class for the ScanIntent enumeration.
    """

    # The value of this ScanIntent, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, scanIntent):
        # construct a ScanIntent from an integer, a string, or another ScanIntent
        # if scanIntent is a string, convert it to an instance of this class using literal
        if isinstance(scanIntent, ScanIntent):
            # copy constructor
            self._value = scanIntent.getValue()
            self._name = scanIntent.getName()
        elif isinstance(scanIntent, str):
            # convert it to an instance of this class using literal
            thisEnum = ScanIntent.literal(scanIntent)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if scanIntent not in _scanIntentNames:
                raise ValueError("unrecognized ScanIntent")
            self._value = scanIntent
            self._name = _scanIntentNames[scanIntent]
            if self._name not in _scanIntentDict:
                # add this ScanIntent as an attribute to this class using its name
                setattr(ScanIntent, self._name, self)
                _scanIntentDict[self._name] = getattr(ScanIntent, self._name)

    def getValue(self):
        return self._value

    def getName(self):
        return self._name

    # by convention with the other languages, these are all static methods
    @staticmethod
    def revision():
        """
        revision as a string.
        """
        return "-1"

    @staticmethod
    def version():
        """
        the major version number as an int.
        """
        return 1

    @staticmethod
    def size():
        """
        the number of known enumerators in ScanIntent
        """
        return len(_scanIntentNames)

    @staticmethod
    def name(scanIntent):
        """
        Returns the string form of the ScanIntent
        """
        return scanIntent.getName()

    @staticmethod
    def toString(scanIntent):
        """
        Equivalent to the name method
        """
        return ScanIntent.name(scanIntent)

    @staticmethod
    def names():
        """
        Return the list of all known ScanIntent enumeration names
        """
        return list(_scanIntentNames.values())

    @staticmethod
    def newScanIntent(name):
        """
        Equivalent to the literal method
        """
        return ScanIntent.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the ScanIntent enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(ScanIntent, name):
            raise ValueError("Unrecognized ScanIntent name")
        return ScanIntent(getattr(ScanIntent, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a ScanIntent from an integration matching an enumeration.
        """
        return ScanIntent(i)


CALIBRATE_AMPLI = ScanIntent(_CALIBRATE_AMPLI)

CALIBRATE_ATMOSPHERE = ScanIntent(_CALIBRATE_ATMOSPHERE)

CALIBRATE_BANDPASS = ScanIntent(_CALIBRATE_BANDPASS)

CALIBRATE_DELAY = ScanIntent(_CALIBRATE_DELAY)

CALIBRATE_FLUX = ScanIntent(_CALIBRATE_FLUX)

CALIBRATE_FOCUS = ScanIntent(_CALIBRATE_FOCUS)

CALIBRATE_FOCUS_X = ScanIntent(_CALIBRATE_FOCUS_X)

CALIBRATE_FOCUS_Y = ScanIntent(_CALIBRATE_FOCUS_Y)

CALIBRATE_PHASE = ScanIntent(_CALIBRATE_PHASE)

CALIBRATE_POINTING = ScanIntent(_CALIBRATE_POINTING)

CALIBRATE_POLARIZATION = ScanIntent(_CALIBRATE_POLARIZATION)

CALIBRATE_SIDEBAND_RATIO = ScanIntent(_CALIBRATE_SIDEBAND_RATIO)

CALIBRATE_WVR = ScanIntent(_CALIBRATE_WVR)

DO_SKYDIP = ScanIntent(_DO_SKYDIP)

MAP_ANTENNA_SURFACE = ScanIntent(_MAP_ANTENNA_SURFACE)

MAP_PRIMARY_BEAM = ScanIntent(_MAP_PRIMARY_BEAM)

OBSERVE_TARGET = ScanIntent(_OBSERVE_TARGET)

CALIBRATE_POL_LEAKAGE = ScanIntent(_CALIBRATE_POL_LEAKAGE)

CALIBRATE_POL_ANGLE = ScanIntent(_CALIBRATE_POL_ANGLE)

TEST = ScanIntent(_TEST)

UNSPECIFIED = ScanIntent(_UNSPECIFIED)

CALIBRATE_ANTENNA_POSITION = ScanIntent(_CALIBRATE_ANTENNA_POSITION)

CALIBRATE_ANTENNA_PHASE = ScanIntent(_CALIBRATE_ANTENNA_PHASE)

MEASURE_RFI = ScanIntent(_MEASURE_RFI)

CALIBRATE_ANTENNA_POINTING_MODEL = ScanIntent(_CALIBRATE_ANTENNA_POINTING_MODEL)

SYSTEM_CONFIGURATION = ScanIntent(_SYSTEM_CONFIGURATION)

CALIBRATE_APPPHASE_ACTIVE = ScanIntent(_CALIBRATE_APPPHASE_ACTIVE)

CALIBRATE_APPPHASE_PASSIVE = ScanIntent(_CALIBRATE_APPPHASE_PASSIVE)

OBSERVE_CHECK_SOURCE = ScanIntent(_OBSERVE_CHECK_SOURCE)

CALIBRATE_DIFFGAIN = ScanIntent(_CALIBRATE_DIFFGAIN)
