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
# File CalibrationDevice.py

# to keep track of the attributes added to this class for each value of this enumeration

_calibrationDeviceDict = {}

# the possible enumerations

_AMBIENT_LOAD = 0  # An absorbing load at the ambient temperature.

_COLD_LOAD = 1  # A cooled absorbing load.

_HOT_LOAD = 2  # A heated absorbing load.

_NOISE_TUBE_LOAD = 3  # A noise tube.

_QUARTER_WAVE_PLATE = 4  # A transparent plate that introduces a 90-degree phase difference between othogonal polarizations.

_SOLAR_FILTER = 5  # An optical attenuator (to protect receiver from solar heat).

_NONE = 6  # No device, the receiver looks at the sky (through the telescope).


# their names in a dictionary
_calibrationDeviceNames = {}

_calibrationDeviceNames[_AMBIENT_LOAD] = "AMBIENT_LOAD"

_calibrationDeviceNames[_COLD_LOAD] = "COLD_LOAD"

_calibrationDeviceNames[_HOT_LOAD] = "HOT_LOAD"

_calibrationDeviceNames[_NOISE_TUBE_LOAD] = "NOISE_TUBE_LOAD"

_calibrationDeviceNames[_QUARTER_WAVE_PLATE] = "QUARTER_WAVE_PLATE"

_calibrationDeviceNames[_SOLAR_FILTER] = "SOLAR_FILTER"

_calibrationDeviceNames[_NONE] = "NONE"


class CalibrationDevice:
    """
    A class for the CalibrationDevice enumeration.
    """

    # The value of this CalibrationDevice, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, calibrationDevice):
        # construct a CalibrationDevice from an integer, a string, or another CalibrationDevice
        # if calibrationDevice is a string, convert it to an instance of this class using literal
        if isinstance(calibrationDevice, CalibrationDevice):
            # copy constructor
            self._value = calibrationDevice.getValue()
            self._name = calibrationDevice.getName()
        elif isinstance(calibrationDevice, str):
            # convert it to an instance of this class using literal
            thisEnum = CalibrationDevice.literal(calibrationDevice)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if calibrationDevice not in _calibrationDeviceNames:
                raise ValueError("unrecognized CalibrationDevice")
            self._value = calibrationDevice
            self._name = _calibrationDeviceNames[calibrationDevice]
            if self._name not in _calibrationDeviceDict:
                # add this CalibrationDevice as an attribute to this class using its name
                setattr(CalibrationDevice, self._name, self)
                _calibrationDeviceDict[self._name] = getattr(
                    CalibrationDevice, self._name
                )

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
        the number of known enumerators in CalibrationDevice
        """
        return len(_calibrationDeviceNames)

    @staticmethod
    def name(calibrationDevice):
        """
        Returns the string form of the CalibrationDevice
        """
        return calibrationDevice.getName()

    @staticmethod
    def toString(calibrationDevice):
        """
        Equivalent to the name method
        """
        return CalibrationDevice.name(calibrationDevice)

    @staticmethod
    def names():
        """
        Return the list of all known CalibrationDevice enumeration names
        """
        return list(_calibrationDeviceNames.values())

    @staticmethod
    def newCalibrationDevice(name):
        """
        Equivalent to the literal method
        """
        return CalibrationDevice.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the CalibrationDevice enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(CalibrationDevice, name):
            raise ValueError("Unrecognized CalibrationDevice name")
        return CalibrationDevice(getattr(CalibrationDevice, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a CalibrationDevice from an integration matching an enumeration.
        """
        return CalibrationDevice(i)


AMBIENT_LOAD = CalibrationDevice(_AMBIENT_LOAD)

COLD_LOAD = CalibrationDevice(_COLD_LOAD)

HOT_LOAD = CalibrationDevice(_HOT_LOAD)

NOISE_TUBE_LOAD = CalibrationDevice(_NOISE_TUBE_LOAD)

QUARTER_WAVE_PLATE = CalibrationDevice(_QUARTER_WAVE_PLATE)

SOLAR_FILTER = CalibrationDevice(_SOLAR_FILTER)

NONE = CalibrationDevice(_NONE)
