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
# File FluxCalibrationMethod.py

# to keep track of the attributes added to this class for each value of this enumeration

_fluxCalibrationMethodDict = {}

# the possible enumerations

_ABSOLUTE = 0  # Absolute flux calibration (based on standard antenna)

_RELATIVE = 1  # Relative flux calibration (based on a primary calibrator)

_EFFICIENCY = 2  # Flux calibrator based on tabulated antenna efficiciency


# their names in a dictionary
_fluxCalibrationMethodNames = {}

_fluxCalibrationMethodNames[_ABSOLUTE] = "ABSOLUTE"

_fluxCalibrationMethodNames[_RELATIVE] = "RELATIVE"

_fluxCalibrationMethodNames[_EFFICIENCY] = "EFFICIENCY"


class FluxCalibrationMethod:
    """
    A class for the FluxCalibrationMethod enumeration.
    """

    # The value of this FluxCalibrationMethod, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, fluxCalibrationMethod):
        # construct a FluxCalibrationMethod from an integer, a string, or another FluxCalibrationMethod
        # if fluxCalibrationMethod is a string, convert it to an instance of this class using literal
        if isinstance(fluxCalibrationMethod, FluxCalibrationMethod):
            # copy constructor
            self._value = fluxCalibrationMethod.getValue()
            self._name = fluxCalibrationMethod.getName()
        elif isinstance(fluxCalibrationMethod, str):
            # convert it to an instance of this class using literal
            thisEnum = FluxCalibrationMethod.literal(fluxCalibrationMethod)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if fluxCalibrationMethod not in _fluxCalibrationMethodNames:
                raise ValueError("unrecognized FluxCalibrationMethod")
            self._value = fluxCalibrationMethod
            self._name = _fluxCalibrationMethodNames[fluxCalibrationMethod]
            if self._name not in _fluxCalibrationMethodDict:
                # add this FluxCalibrationMethod as an attribute to this class using its name
                setattr(FluxCalibrationMethod, self._name, self)
                _fluxCalibrationMethodDict[self._name] = getattr(
                    FluxCalibrationMethod, self._name
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
        the number of known enumerators in FluxCalibrationMethod
        """
        return len(_fluxCalibrationMethodNames)

    @staticmethod
    def name(fluxCalibrationMethod):
        """
        Returns the string form of the FluxCalibrationMethod
        """
        return fluxCalibrationMethod.getName()

    @staticmethod
    def toString(fluxCalibrationMethod):
        """
        Equivalent to the name method
        """
        return FluxCalibrationMethod.name(fluxCalibrationMethod)

    @staticmethod
    def names():
        """
        Return the list of all known FluxCalibrationMethod enumeration names
        """
        return list(_fluxCalibrationMethodNames.values())

    @staticmethod
    def newFluxCalibrationMethod(name):
        """
        Equivalent to the literal method
        """
        return FluxCalibrationMethod.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the FluxCalibrationMethod enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(FluxCalibrationMethod, name):
            raise ValueError("Unrecognized FluxCalibrationMethod name")
        return FluxCalibrationMethod(getattr(FluxCalibrationMethod, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a FluxCalibrationMethod from an integration matching an enumeration.
        """
        return FluxCalibrationMethod(i)


ABSOLUTE = FluxCalibrationMethod(_ABSOLUTE)

RELATIVE = FluxCalibrationMethod(_RELATIVE)

EFFICIENCY = FluxCalibrationMethod(_EFFICIENCY)
