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
# File TimeSampling.py

# to keep track of the attributes added to this class for each value of this enumeration

_timeSamplingDict = {}

# the possible enumerations

_SUBINTEGRATION = 0  # Part of an integration

_INTEGRATION = (
    1  # Part of a subscan. An integration may be composed of several sub-integrations.
)


# their names in a dictionary
_timeSamplingNames = {}

_timeSamplingNames[_SUBINTEGRATION] = "SUBINTEGRATION"

_timeSamplingNames[_INTEGRATION] = "INTEGRATION"


class TimeSampling:
    """
    A class for the TimeSampling enumeration.
    """

    # The value of this TimeSampling, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, timeSampling):
        # construct a TimeSampling from an integer, a string, or another TimeSampling
        # if timeSampling is a string, convert it to an instance of this class using literal
        if isinstance(timeSampling, TimeSampling):
            # copy constructor
            self._value = timeSampling.getValue()
            self._name = timeSampling.getName()
        elif isinstance(timeSampling, str):
            # convert it to an instance of this class using literal
            thisEnum = TimeSampling.literal(timeSampling)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if timeSampling not in _timeSamplingNames:
                raise ValueError("unrecognized TimeSampling")
            self._value = timeSampling
            self._name = _timeSamplingNames[timeSampling]
            if self._name not in _timeSamplingDict:
                # add this TimeSampling as an attribute to this class using its name
                setattr(TimeSampling, self._name, self)
                _timeSamplingDict[self._name] = getattr(TimeSampling, self._name)

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
        the number of known enumerators in TimeSampling
        """
        return len(_timeSamplingNames)

    @staticmethod
    def name(timeSampling):
        """
        Returns the string form of the TimeSampling
        """
        return timeSampling.getName()

    @staticmethod
    def toString(timeSampling):
        """
        Equivalent to the name method
        """
        return TimeSampling.name(timeSampling)

    @staticmethod
    def names():
        """
        Return the list of all known TimeSampling enumeration names
        """
        return list(_timeSamplingNames.values())

    @staticmethod
    def newTimeSampling(name):
        """
        Equivalent to the literal method
        """
        return TimeSampling.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the TimeSampling enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(TimeSampling, name):
            raise ValueError("Unrecognized TimeSampling name")
        return TimeSampling(getattr(TimeSampling, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a TimeSampling from an integration matching an enumeration.
        """
        return TimeSampling(i)


SUBINTEGRATION = TimeSampling(_SUBINTEGRATION)

INTEGRATION = TimeSampling(_INTEGRATION)
