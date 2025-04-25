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
# File TimeScale.py

# to keep track of the attributes added to this class for each value of this enumeration

_timeScaleDict = {}

# the possible enumerations

_UTC = 0  # Coordinated Universal Time.

_TAI = 1  # International Atomic Time.


# their names in a dictionary
_timeScaleNames = {}

_timeScaleNames[_UTC] = "UTC"

_timeScaleNames[_TAI] = "TAI"


class TimeScale:
    """
    A class for the TimeScale enumeration.
    """

    # The value of this TimeScale, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, timeScale):
        # construct a TimeScale from an integer, a string, or another TimeScale
        # if timeScale is a string, convert it to an instance of this class using literal
        if isinstance(timeScale, TimeScale):
            # copy constructor
            self._value = timeScale.getValue()
            self._name = timeScale.getName()
        elif isinstance(timeScale, str):
            # convert it to an instance of this class using literal
            thisEnum = TimeScale.literal(timeScale)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if timeScale not in _timeScaleNames:
                raise ValueError("unrecognized TimeScale")
            self._value = timeScale
            self._name = _timeScaleNames[timeScale]
            if self._name not in _timeScaleDict:
                # add this TimeScale as an attribute to this class using its name
                setattr(TimeScale, self._name, self)
                _timeScaleDict[self._name] = getattr(TimeScale, self._name)

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
        Returns True if other is a TimeScale and its value is the same as this one.
        """
        return isinstance(other, TimeScale) and (other.getValue() == self.getValue())

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
        the number of known enumerators in TimeScale
        """
        return len(_timeScaleNames)

    @staticmethod
    def name(timeScale):
        """
        Returns the string form of timeScale
        """
        return str(timeScale)

    @staticmethod
    def names():
        """
        Return the list of all known TimeScale enumeration names
        """
        return list(_timeScaleNames.values())

    @staticmethod
    def newTimeScale(name):
        """
        Equivalent to the literal method
        """
        return TimeScale.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the TimeScale enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(TimeScale, name):
            raise ValueError("Unrecognized TimeScale name")
        return TimeScale(getattr(TimeScale, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a TimeScale from an integration matching an enumeration.
        """
        return TimeScale(i)


UTC = TimeScale(_UTC)

TAI = TimeScale(_TAI)
