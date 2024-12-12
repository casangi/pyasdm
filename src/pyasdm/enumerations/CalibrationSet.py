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
# File CalibrationSet.py

# to keep track of the attributes added to this class for each value of this enumeration

_calibrationSetDict = {}

# the possible enumerations

_NONE = 0  # Scan is not part of a calibration set.

_AMPLI_CURVE = 1  # Amplitude calibration scan (calibration curve to be derived).

_ANTENNA_POSITIONS = 2  # Antenna positions measurement.

_PHASE_CURVE = 3  # Phase calibration scan (calibration curve to be derived).

_POINTING_MODEL = 4  # Pointing calibration scan (pointing model to be derived).

_ACCUMULATE = 5  # Accumulate a scan in a calibration set.

_TEST = 6  # Reserved for development.

_UNSPECIFIED = 7  # Unspecified calibration intent.


# their names in a dictionary
_calibrationSetNames = {}

_calibrationSetNames[_NONE] = "NONE"

_calibrationSetNames[_AMPLI_CURVE] = "AMPLI_CURVE"

_calibrationSetNames[_ANTENNA_POSITIONS] = "ANTENNA_POSITIONS"

_calibrationSetNames[_PHASE_CURVE] = "PHASE_CURVE"

_calibrationSetNames[_POINTING_MODEL] = "POINTING_MODEL"

_calibrationSetNames[_ACCUMULATE] = "ACCUMULATE"

_calibrationSetNames[_TEST] = "TEST"

_calibrationSetNames[_UNSPECIFIED] = "UNSPECIFIED"


class CalibrationSet:
    """
    A class for the CalibrationSet enumeration.
    """

    # The value of this CalibrationSet, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, calibrationSet):
        # construct a CalibrationSet from an integer, a string, or another CalibrationSet
        # if calibrationSet is a string, convert it to an instance of this class using literal
        if isinstance(calibrationSet, CalibrationSet):
            # copy constructor
            self._value = calibrationSet.getValue()
            self._name = calibrationSet.getName()
        elif isinstance(calibrationSet, str):
            # convert it to an instance of this class using literal
            thisEnum = CalibrationSet.literal(calibrationSet)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if calibrationSet not in _calibrationSetNames:
                raise ValueError("unrecognized CalibrationSet")
            self._value = calibrationSet
            self._name = _calibrationSetNames[calibrationSet]
            if self._name not in _calibrationSetDict:
                # add this CalibrationSet as an attribute to this class using its name
                setattr(CalibrationSet, self._name, self)
                _calibrationSetDict[self._name] = getattr(CalibrationSet, self._name)

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
        the number of known enumerators in CalibrationSet
        """
        return len(_calibrationSetNames)

    @staticmethod
    def name(calibrationSet):
        """
        Returns the string form of the CalibrationSet
        """
        return calibrationSet.getName()

    @staticmethod
    def toString(calibrationSet):
        """
        Equivalent to the name method
        """
        return CalibrationSet.name(calibrationSet)

    @staticmethod
    def names():
        """
        Return the list of all known CalibrationSet enumeration names
        """
        return list(_calibrationSetNames.values())

    @staticmethod
    def newCalibrationSet(name):
        """
        Equivalent to the literal method
        """
        return CalibrationSet.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the CalibrationSet enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(CalibrationSet, name):
            raise ValueError("Unrecognized CalibrationSet name")
        return CalibrationSet(getattr(CalibrationSet, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a CalibrationSet from an integration matching an enumeration.
        """
        return CalibrationSet(i)


NONE = CalibrationSet(_NONE)

AMPLI_CURVE = CalibrationSet(_AMPLI_CURVE)

ANTENNA_POSITIONS = CalibrationSet(_ANTENNA_POSITIONS)

PHASE_CURVE = CalibrationSet(_PHASE_CURVE)

POINTING_MODEL = CalibrationSet(_POINTING_MODEL)

ACCUMULATE = CalibrationSet(_ACCUMULATE)

TEST = CalibrationSet(_TEST)

UNSPECIFIED = CalibrationSet(_UNSPECIFIED)
