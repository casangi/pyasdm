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
# File StationType.py

# to keep track of the attributes added to this class for each value of this enumeration

_stationTypeDict = {}

# the possible enumerations

_ANTENNA_PAD = 0  # Astronomical Antenna station

_MAINTENANCE_PAD = 1  # Maintenance antenna station

_WEATHER_STATION = 2  # Weather station


# their names in a dictionary
_stationTypeNames = {}

_stationTypeNames[_ANTENNA_PAD] = "ANTENNA_PAD"

_stationTypeNames[_MAINTENANCE_PAD] = "MAINTENANCE_PAD"

_stationTypeNames[_WEATHER_STATION] = "WEATHER_STATION"


class StationType:
    """
    A class for the StationType enumeration.
    """

    # The value of this StationType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, stationType):
        # construct a StationType from an integer, a string, or another StationType
        # if stationType is a string, convert it to an instance of this class using literal
        if isinstance(stationType, StationType):
            # copy constructor
            self._value = stationType.getValue()
            self._name = stationType.getName()
        elif isinstance(stationType, str):
            # convert it to an instance of this class using literal
            thisEnum = StationType.literal(stationType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if stationType not in _stationTypeNames:
                raise ValueError("unrecognized StationType")
            self._value = stationType
            self._name = _stationTypeNames[stationType]
            if self._name not in _stationTypeDict:
                # add this StationType as an attribute to this class using its name
                setattr(StationType, self._name, self)
                _stationTypeDict[self._name] = getattr(StationType, self._name)

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
        Returns True if other is a StationType and its value is the same as this one.
        """
        return isinstance(other, StationType) and (other.getValue() == self.getValue())

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
        the number of known enumerators in StationType
        """
        return len(_stationTypeNames)

    @staticmethod
    def name(stationType):
        """
        Returns the string form of stationType
        """
        return str(stationType)

    @staticmethod
    def names():
        """
        Return the list of all known StationType enumeration names
        """
        return list(_stationTypeNames.values())

    @staticmethod
    def newStationType(name):
        """
        Equivalent to the literal method
        """
        return StationType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the StationType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(StationType, name):
            raise ValueError("Unrecognized StationType name")
        return StationType(getattr(StationType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a StationType from an integration matching an enumeration.
        """
        return StationType(i)


ANTENNA_PAD = StationType(_ANTENNA_PAD)

MAINTENANCE_PAD = StationType(_MAINTENANCE_PAD)

WEATHER_STATION = StationType(_WEATHER_STATION)
