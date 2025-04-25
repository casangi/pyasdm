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
# File SidebandProcessingMode.py

# to keep track of the attributes added to this class for each value of this enumeration

_sidebandProcessingModeDict = {}

# the possible enumerations

_NONE = 0  # No processing

_PHASE_SWITCH_SEPARATION = 1  # Side band separation using 90-degree phase switching

_FREQUENCY_OFFSET_SEPARATION = (
    2  # Side band separation using offsets of first ans second oscillators
)

_PHASE_SWITCH_REJECTION = 3  # Side band rejection 90-degree phase switching

_FREQUENCY_OFFSET_REJECTION = (
    4  # Side band rejection using offsets of first and second oscillators
)


# their names in a dictionary
_sidebandProcessingModeNames = {}

_sidebandProcessingModeNames[_NONE] = "NONE"

_sidebandProcessingModeNames[_PHASE_SWITCH_SEPARATION] = "PHASE_SWITCH_SEPARATION"

_sidebandProcessingModeNames[_FREQUENCY_OFFSET_SEPARATION] = (
    "FREQUENCY_OFFSET_SEPARATION"
)

_sidebandProcessingModeNames[_PHASE_SWITCH_REJECTION] = "PHASE_SWITCH_REJECTION"

_sidebandProcessingModeNames[_FREQUENCY_OFFSET_REJECTION] = "FREQUENCY_OFFSET_REJECTION"


class SidebandProcessingMode:
    """
    A class for the SidebandProcessingMode enumeration.
    """

    # The value of this SidebandProcessingMode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, sidebandProcessingMode):
        # construct a SidebandProcessingMode from an integer, a string, or another SidebandProcessingMode
        # if sidebandProcessingMode is a string, convert it to an instance of this class using literal
        if isinstance(sidebandProcessingMode, SidebandProcessingMode):
            # copy constructor
            self._value = sidebandProcessingMode.getValue()
            self._name = sidebandProcessingMode.getName()
        elif isinstance(sidebandProcessingMode, str):
            # convert it to an instance of this class using literal
            thisEnum = SidebandProcessingMode.literal(sidebandProcessingMode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if sidebandProcessingMode not in _sidebandProcessingModeNames:
                raise ValueError("unrecognized SidebandProcessingMode")
            self._value = sidebandProcessingMode
            self._name = _sidebandProcessingModeNames[sidebandProcessingMode]
            if self._name not in _sidebandProcessingModeDict:
                # add this SidebandProcessingMode as an attribute to this class using its name
                setattr(SidebandProcessingMode, self._name, self)
                _sidebandProcessingModeDict[self._name] = getattr(
                    SidebandProcessingMode, self._name
                )

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
        Returns True if other is a SidebandProcessingMode and its value is the same as this one.
        """
        return isinstance(other, SidebandProcessingMode) and (
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
        the number of known enumerators in SidebandProcessingMode
        """
        return len(_sidebandProcessingModeNames)

    @staticmethod
    def name(sidebandProcessingMode):
        """
        Returns the string form of sidebandProcessingMode
        """
        return str(sidebandProcessingMode)

    @staticmethod
    def names():
        """
        Return the list of all known SidebandProcessingMode enumeration names
        """
        return list(_sidebandProcessingModeNames.values())

    @staticmethod
    def newSidebandProcessingMode(name):
        """
        Equivalent to the literal method
        """
        return SidebandProcessingMode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the SidebandProcessingMode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(SidebandProcessingMode, name):
            raise ValueError("Unrecognized SidebandProcessingMode name")
        return SidebandProcessingMode(getattr(SidebandProcessingMode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a SidebandProcessingMode from an integration matching an enumeration.
        """
        return SidebandProcessingMode(i)


NONE = SidebandProcessingMode(_NONE)

PHASE_SWITCH_SEPARATION = SidebandProcessingMode(_PHASE_SWITCH_SEPARATION)

FREQUENCY_OFFSET_SEPARATION = SidebandProcessingMode(_FREQUENCY_OFFSET_SEPARATION)

PHASE_SWITCH_REJECTION = SidebandProcessingMode(_PHASE_SWITCH_REJECTION)

FREQUENCY_OFFSET_REJECTION = SidebandProcessingMode(_FREQUENCY_OFFSET_REJECTION)
