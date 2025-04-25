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
# File SwitchingMode.py

# to keep track of the attributes added to this class for each value of this enumeration

_switchingModeDict = {}

# the possible enumerations

_NO_SWITCHING = 0  # No switching

_LOAD_SWITCHING = 1  # Receiver beam is switched between sky and load

_POSITION_SWITCHING = 2  # Antenna (main reflector) pointing direction  is switched

_PHASE_SWITCHING = 3  # 90 degrees phase switching  (switching mode used for sideband separation or rejection with DSB receivers)

_FREQUENCY_SWITCHING = 4  # LO frequency is switched (definition context sensitive: fast if cycle shrorter than the integration duration, slow if e.g. step one step per subscan)

_NUTATOR_SWITCHING = (
    5  # Switching between different directions by nutating the sub-reflector
)

_CHOPPER_WHEEL = 6  # Switching using a chopper wheel


# their names in a dictionary
_switchingModeNames = {}

_switchingModeNames[_NO_SWITCHING] = "NO_SWITCHING"

_switchingModeNames[_LOAD_SWITCHING] = "LOAD_SWITCHING"

_switchingModeNames[_POSITION_SWITCHING] = "POSITION_SWITCHING"

_switchingModeNames[_PHASE_SWITCHING] = "PHASE_SWITCHING"

_switchingModeNames[_FREQUENCY_SWITCHING] = "FREQUENCY_SWITCHING"

_switchingModeNames[_NUTATOR_SWITCHING] = "NUTATOR_SWITCHING"

_switchingModeNames[_CHOPPER_WHEEL] = "CHOPPER_WHEEL"


class SwitchingMode:
    """
    A class for the SwitchingMode enumeration.
    """

    # The value of this SwitchingMode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, switchingMode):
        # construct a SwitchingMode from an integer, a string, or another SwitchingMode
        # if switchingMode is a string, convert it to an instance of this class using literal
        if isinstance(switchingMode, SwitchingMode):
            # copy constructor
            self._value = switchingMode.getValue()
            self._name = switchingMode.getName()
        elif isinstance(switchingMode, str):
            # convert it to an instance of this class using literal
            thisEnum = SwitchingMode.literal(switchingMode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if switchingMode not in _switchingModeNames:
                raise ValueError("unrecognized SwitchingMode")
            self._value = switchingMode
            self._name = _switchingModeNames[switchingMode]
            if self._name not in _switchingModeDict:
                # add this SwitchingMode as an attribute to this class using its name
                setattr(SwitchingMode, self._name, self)
                _switchingModeDict[self._name] = getattr(SwitchingMode, self._name)

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
        Returns True if other is a SwitchingMode and its value is the same as this one.
        """
        return isinstance(other, SwitchingMode) and (
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
        the number of known enumerators in SwitchingMode
        """
        return len(_switchingModeNames)

    @staticmethod
    def name(switchingMode):
        """
        Returns the string form of switchingMode
        """
        return str(switchingMode)

    @staticmethod
    def names():
        """
        Return the list of all known SwitchingMode enumeration names
        """
        return list(_switchingModeNames.values())

    @staticmethod
    def newSwitchingMode(name):
        """
        Equivalent to the literal method
        """
        return SwitchingMode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the SwitchingMode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(SwitchingMode, name):
            raise ValueError("Unrecognized SwitchingMode name")
        return SwitchingMode(getattr(SwitchingMode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a SwitchingMode from an integration matching an enumeration.
        """
        return SwitchingMode(i)


NO_SWITCHING = SwitchingMode(_NO_SWITCHING)

LOAD_SWITCHING = SwitchingMode(_LOAD_SWITCHING)

POSITION_SWITCHING = SwitchingMode(_POSITION_SWITCHING)

PHASE_SWITCHING = SwitchingMode(_PHASE_SWITCHING)

FREQUENCY_SWITCHING = SwitchingMode(_FREQUENCY_SWITCHING)

NUTATOR_SWITCHING = SwitchingMode(_NUTATOR_SWITCHING)

CHOPPER_WHEEL = SwitchingMode(_CHOPPER_WHEEL)
