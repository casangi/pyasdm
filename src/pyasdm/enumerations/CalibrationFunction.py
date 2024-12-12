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
# File CalibrationFunction.py

# to keep track of the attributes added to this class for each value of this enumeration

_calibrationFunctionDict = {}

# the possible enumerations

_FIRST = 0  # the scan is the first in a calibration set.

_LAST = 1  # the scan is the last in a calibration set.

_UNSPECIFIED = 2  # the function is not specified.


# their names in a dictionary
_calibrationFunctionNames = {}

_calibrationFunctionNames[_FIRST] = "FIRST"

_calibrationFunctionNames[_LAST] = "LAST"

_calibrationFunctionNames[_UNSPECIFIED] = "UNSPECIFIED"


class CalibrationFunction:
    """
    A class for the CalibrationFunction enumeration.
    """

    # The value of this CalibrationFunction, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, calibrationFunction):
        # construct a CalibrationFunction from an integer, a string, or another CalibrationFunction
        # if calibrationFunction is a string, convert it to an instance of this class using literal
        if isinstance(calibrationFunction, CalibrationFunction):
            # copy constructor
            self._value = calibrationFunction.getValue()
            self._name = calibrationFunction.getName()
        elif isinstance(calibrationFunction, str):
            # convert it to an instance of this class using literal
            thisEnum = CalibrationFunction.literal(calibrationFunction)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if calibrationFunction not in _calibrationFunctionNames:
                raise ValueError("unrecognized CalibrationFunction")
            self._value = calibrationFunction
            self._name = _calibrationFunctionNames[calibrationFunction]
            if self._name not in _calibrationFunctionDict:
                # add this CalibrationFunction as an attribute to this class using its name
                setattr(CalibrationFunction, self._name, self)
                _calibrationFunctionDict[self._name] = getattr(
                    CalibrationFunction, self._name
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
        the number of known enumerators in CalibrationFunction
        """
        return len(_calibrationFunctionNames)

    @staticmethod
    def name(calibrationFunction):
        """
        Returns the string form of the CalibrationFunction
        """
        return calibrationFunction.getName()

    @staticmethod
    def toString(calibrationFunction):
        """
        Equivalent to the name method
        """
        return CalibrationFunction.name(calibrationFunction)

    @staticmethod
    def names():
        """
        Return the list of all known CalibrationFunction enumeration names
        """
        return list(_calibrationFunctionNames.values())

    @staticmethod
    def newCalibrationFunction(name):
        """
        Equivalent to the literal method
        """
        return CalibrationFunction.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the CalibrationFunction enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(CalibrationFunction, name):
            raise ValueError("Unrecognized CalibrationFunction name")
        return CalibrationFunction(getattr(CalibrationFunction, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a CalibrationFunction from an integration matching an enumeration.
        """
        return CalibrationFunction(i)


FIRST = CalibrationFunction(_FIRST)

LAST = CalibrationFunction(_LAST)

UNSPECIFIED = CalibrationFunction(_UNSPECIFIED)
