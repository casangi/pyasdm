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
# File CalDataOrigin.py

# to keep track of the attributes added to this class for each value of this enumeration

_calDataOriginDict = {}

# the possible enumerations

_TOTAL_POWER = 0  # Total Power data (from detectors)

_WVR = 1  # Water vapour radiometrers

_CHANNEL_AVERAGE_AUTO = 2  # Autocorrelations from channel average data

_CHANNEL_AVERAGE_CROSS = 3  # Crosscorrelations from channel average data

_FULL_RESOLUTION_AUTO = 4  # Autocorrelations from full-resolution data

_FULL_RESOLUTION_CROSS = 5  # Cross correlations from full-resolution data

_OPTICAL_POINTING = 6  # Optical pointing data

_HOLOGRAPHY = 7  # data from holography receivers

_NONE = 8  # Not applicable


# their names in a dictionary
_calDataOriginNames = {}

_calDataOriginNames[_TOTAL_POWER] = "TOTAL_POWER"

_calDataOriginNames[_WVR] = "WVR"

_calDataOriginNames[_CHANNEL_AVERAGE_AUTO] = "CHANNEL_AVERAGE_AUTO"

_calDataOriginNames[_CHANNEL_AVERAGE_CROSS] = "CHANNEL_AVERAGE_CROSS"

_calDataOriginNames[_FULL_RESOLUTION_AUTO] = "FULL_RESOLUTION_AUTO"

_calDataOriginNames[_FULL_RESOLUTION_CROSS] = "FULL_RESOLUTION_CROSS"

_calDataOriginNames[_OPTICAL_POINTING] = "OPTICAL_POINTING"

_calDataOriginNames[_HOLOGRAPHY] = "HOLOGRAPHY"

_calDataOriginNames[_NONE] = "NONE"


class CalDataOrigin:
    """
    A class for the CalDataOrigin enumeration.
    """

    # The value of this CalDataOrigin, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, calDataOrigin):
        # construct a CalDataOrigin from an integer, a string, or another CalDataOrigin
        # if calDataOrigin is a string, convert it to an instance of this class using literal
        if isinstance(calDataOrigin, CalDataOrigin):
            # copy constructor
            self._value = calDataOrigin.getValue()
            self._name = calDataOrigin.getName()
        elif isinstance(calDataOrigin, str):
            # convert it to an instance of this class using literal
            thisEnum = CalDataOrigin.literal(calDataOrigin)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if calDataOrigin not in _calDataOriginNames:
                raise ValueError("unrecognized CalDataOrigin")
            self._value = calDataOrigin
            self._name = _calDataOriginNames[calDataOrigin]
            if self._name not in _calDataOriginDict:
                # add this CalDataOrigin as an attribute to this class using its name
                setattr(CalDataOrigin, self._name, self)
                _calDataOriginDict[self._name] = getattr(CalDataOrigin, self._name)

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
        Returns True if other is a CalDataOrigin and its value is the same as this one.
        """
        return isinstance(other, CalDataOrigin) and (
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
        the number of known enumerators in CalDataOrigin
        """
        return len(_calDataOriginNames)

    @staticmethod
    def name(calDataOrigin):
        """
        Returns the string form of calDataOrigin
        """
        return str(calDataOrigin)

    @staticmethod
    def names():
        """
        Return the list of all known CalDataOrigin enumeration names
        """
        return list(_calDataOriginNames.values())

    @staticmethod
    def newCalDataOrigin(name):
        """
        Equivalent to the literal method
        """
        return CalDataOrigin.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the CalDataOrigin enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(CalDataOrigin, name):
            raise ValueError("Unrecognized CalDataOrigin name")
        return CalDataOrigin(getattr(CalDataOrigin, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a CalDataOrigin from an integration matching an enumeration.
        """
        return CalDataOrigin(i)


TOTAL_POWER = CalDataOrigin(_TOTAL_POWER)

WVR = CalDataOrigin(_WVR)

CHANNEL_AVERAGE_AUTO = CalDataOrigin(_CHANNEL_AVERAGE_AUTO)

CHANNEL_AVERAGE_CROSS = CalDataOrigin(_CHANNEL_AVERAGE_CROSS)

FULL_RESOLUTION_AUTO = CalDataOrigin(_FULL_RESOLUTION_AUTO)

FULL_RESOLUTION_CROSS = CalDataOrigin(_FULL_RESOLUTION_CROSS)

OPTICAL_POINTING = CalDataOrigin(_OPTICAL_POINTING)

HOLOGRAPHY = CalDataOrigin(_HOLOGRAPHY)

NONE = CalDataOrigin(_NONE)
