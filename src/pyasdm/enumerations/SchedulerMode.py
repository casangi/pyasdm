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
# File SchedulerMode.py

# to keep track of the attributes added to this class for each value of this enumeration

_schedulerModeDict = {}

# the possible enumerations

_DYNAMIC = 0  # Dynamic scheduling

_INTERACTIVE = 1  # Interactive scheduling

_MANUAL = 2  # Manual scheduling

_QUEUED = 3  # Queued scheduling


# their names in a dictionary
_schedulerModeNames = {}

_schedulerModeNames[_DYNAMIC] = "DYNAMIC"

_schedulerModeNames[_INTERACTIVE] = "INTERACTIVE"

_schedulerModeNames[_MANUAL] = "MANUAL"

_schedulerModeNames[_QUEUED] = "QUEUED"


class SchedulerMode:
    """
    A class for the SchedulerMode enumeration.
    """

    # The value of this SchedulerMode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, schedulerMode):
        # construct a SchedulerMode from an integer, a string, or another SchedulerMode
        # if schedulerMode is a string, convert it to an instance of this class using literal
        if isinstance(schedulerMode, SchedulerMode):
            # copy constructor
            self._value = schedulerMode.getValue()
            self._name = schedulerMode.getName()
        elif isinstance(schedulerMode, str):
            # convert it to an instance of this class using literal
            thisEnum = SchedulerMode.literal(schedulerMode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if schedulerMode not in _schedulerModeNames:
                raise ValueError("unrecognized SchedulerMode")
            self._value = schedulerMode
            self._name = _schedulerModeNames[schedulerMode]
            if self._name not in _schedulerModeDict:
                # add this SchedulerMode as an attribute to this class using its name
                setattr(SchedulerMode, self._name, self)
                _schedulerModeDict[self._name] = getattr(SchedulerMode, self._name)

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
        Returns True if other is a SchedulerMode and its value is the same as this one.
        """
        return isinstance(other, SchedulerMode) and (
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
        the number of known enumerators in SchedulerMode
        """
        return len(_schedulerModeNames)

    @staticmethod
    def name(schedulerMode):
        """
        Returns the string form of schedulerMode
        """
        return str(schedulerMode)

    @staticmethod
    def names():
        """
        Return the list of all known SchedulerMode enumeration names
        """
        return list(_schedulerModeNames.values())

    @staticmethod
    def newSchedulerMode(name):
        """
        Equivalent to the literal method
        """
        return SchedulerMode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the SchedulerMode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(SchedulerMode, name):
            raise ValueError("Unrecognized SchedulerMode name")
        return SchedulerMode(getattr(SchedulerMode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a SchedulerMode from an integration matching an enumeration.
        """
        return SchedulerMode(i)


DYNAMIC = SchedulerMode(_DYNAMIC)

INTERACTIVE = SchedulerMode(_INTERACTIVE)

MANUAL = SchedulerMode(_MANUAL)

QUEUED = SchedulerMode(_QUEUED)
