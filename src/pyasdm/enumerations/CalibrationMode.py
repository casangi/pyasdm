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
# File CalibrationMode.py

# to keep track of the attributes added to this class for each value of this enumeration

_calibrationModeDict = {}

# the possible enumerations

_HOLOGRAPHY = 0  # Holography receiver

_INTERFEROMETRY = 1  # interferometry

_OPTICAL = 2  # Optical telescope

_RADIOMETRY = 3  # total power

_WVR = 4  # water vapour radiometry receiver


# their names in a dictionary
_calibrationModeNames = {}

_calibrationModeNames[_HOLOGRAPHY] = "HOLOGRAPHY"

_calibrationModeNames[_INTERFEROMETRY] = "INTERFEROMETRY"

_calibrationModeNames[_OPTICAL] = "OPTICAL"

_calibrationModeNames[_RADIOMETRY] = "RADIOMETRY"

_calibrationModeNames[_WVR] = "WVR"


class CalibrationMode:
    """
    A class for the CalibrationMode enumeration.
    """

    # The value of this CalibrationMode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, calibrationMode):
        # construct a CalibrationMode from an integer, a string, or another CalibrationMode
        # if calibrationMode is a string, convert it to an instance of this class using literal
        if isinstance(calibrationMode, CalibrationMode):
            # copy constructor
            self._value = calibrationMode.getValue()
            self._name = calibrationMode.getName()
        elif isinstance(calibrationMode, str):
            # convert it to an instance of this class using literal
            thisEnum = CalibrationMode.literal(calibrationMode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if calibrationMode not in _calibrationModeNames:
                raise ValueError("unrecognized CalibrationMode")
            self._value = calibrationMode
            self._name = _calibrationModeNames[calibrationMode]
            if self._name not in _calibrationModeDict:
                # add this CalibrationMode as an attribute to this class using its name
                setattr(CalibrationMode, self._name, self)
                _calibrationModeDict[self._name] = getattr(CalibrationMode, self._name)

    def getValue(self):
        """
        Return the integer value of this enumeration.
        """
        return self._value

    def getName(self):
        """
        Return the name of this enumeration.
        """
        return self._name

    def __str__(self):
        """
        Equivalent to getName()
        """
        return self.getName()

    def __eq__(self, other):
        """
        Returns True if other is a CalibrationMode and its value is the same as this one.
        """
        return isinstance(other, CalibrationMode) and (
            other.getValue() == self.getValue()
        )

    def __ne__(self, other):
        """
        Returns True if other is not equal to self
        """
        return not (self == other)

    # by convention with the code in java and c++, these are all static methods
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
        the number of known enumerators in CalibrationMode
        """
        return len(_calibrationModeNames)

    @staticmethod
    def name(calibrationMode):
        """
        Returns the string form of calibrationMode
        """
        return str(calibrationMode)

    @staticmethod
    def names():
        """
        Return the list of all known CalibrationMode enumeration names
        """
        return list(_calibrationModeNames.values())

    @staticmethod
    def newCalibrationMode(name):
        """
        Equivalent to the literal method
        """
        return CalibrationMode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the CalibrationMode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(CalibrationMode, name):
            raise ValueError("Unrecognized CalibrationMode name")
        return CalibrationMode(getattr(CalibrationMode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a CalibrationMode from an integration matching an enumeration.
        """
        return CalibrationMode(i)


HOLOGRAPHY = CalibrationMode(_HOLOGRAPHY)

INTERFEROMETRY = CalibrationMode(_INTERFEROMETRY)

OPTICAL = CalibrationMode(_OPTICAL)

RADIOMETRY = CalibrationMode(_RADIOMETRY)

WVR = CalibrationMode(_WVR)
