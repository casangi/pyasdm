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
# File InvalidatingCondition.py

# to keep track of the attributes added to this class for each value of this enumeration

_invalidatingConditionDict = {}

# the possible enumerations

_ANTENNA_DISCONNECT = 0  # Antenna was disconnected

_ANTENNA_MOVE = 1  # Antenna was moved

_ANTENNA_POWER_DOWN = 2  # Antenna was powered down

_RECEIVER_EXCHANGE = 3  # Receiver was exchanged

_RECEIVER_POWER_DOWN = 4  # Receiver was powered down


# their names in a dictionary
_invalidatingConditionNames = {}

_invalidatingConditionNames[_ANTENNA_DISCONNECT] = "ANTENNA_DISCONNECT"

_invalidatingConditionNames[_ANTENNA_MOVE] = "ANTENNA_MOVE"

_invalidatingConditionNames[_ANTENNA_POWER_DOWN] = "ANTENNA_POWER_DOWN"

_invalidatingConditionNames[_RECEIVER_EXCHANGE] = "RECEIVER_EXCHANGE"

_invalidatingConditionNames[_RECEIVER_POWER_DOWN] = "RECEIVER_POWER_DOWN"


class InvalidatingCondition:
    """
    A class for the InvalidatingCondition enumeration.
    """

    # The value of this InvalidatingCondition, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, invalidatingCondition):
        # construct a InvalidatingCondition from an integer, a string, or another InvalidatingCondition
        # if invalidatingCondition is a string, convert it to an instance of this class using literal
        if isinstance(invalidatingCondition, InvalidatingCondition):
            # copy constructor
            self._value = invalidatingCondition.getValue()
            self._name = invalidatingCondition.getName()
        elif isinstance(invalidatingCondition, str):
            # convert it to an instance of this class using literal
            thisEnum = InvalidatingCondition.literal(invalidatingCondition)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if invalidatingCondition not in _invalidatingConditionNames:
                raise ValueError("unrecognized InvalidatingCondition")
            self._value = invalidatingCondition
            self._name = _invalidatingConditionNames[invalidatingCondition]
            if self._name not in _invalidatingConditionDict:
                # add this InvalidatingCondition as an attribute to this class using its name
                setattr(InvalidatingCondition, self._name, self)
                _invalidatingConditionDict[self._name] = getattr(
                    InvalidatingCondition, self._name
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
        Returns True if other is a InvalidatingCondition and its value is the same as this one.
        """
        return isinstance(other, InvalidatingCondition) and (
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
        the number of known enumerators in InvalidatingCondition
        """
        return len(_invalidatingConditionNames)

    @staticmethod
    def name(invalidatingCondition):
        """
        Returns the string form of invalidatingCondition
        """
        return str(invalidatingCondition)

    @staticmethod
    def names():
        """
        Return the list of all known InvalidatingCondition enumeration names
        """
        return list(_invalidatingConditionNames.values())

    @staticmethod
    def newInvalidatingCondition(name):
        """
        Equivalent to the literal method
        """
        return InvalidatingCondition.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the InvalidatingCondition enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(InvalidatingCondition, name):
            raise ValueError("Unrecognized InvalidatingCondition name")
        return InvalidatingCondition(getattr(InvalidatingCondition, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a InvalidatingCondition from an integration matching an enumeration.
        """
        return InvalidatingCondition(i)


ANTENNA_DISCONNECT = InvalidatingCondition(_ANTENNA_DISCONNECT)

ANTENNA_MOVE = InvalidatingCondition(_ANTENNA_MOVE)

ANTENNA_POWER_DOWN = InvalidatingCondition(_ANTENNA_POWER_DOWN)

RECEIVER_EXCHANGE = InvalidatingCondition(_RECEIVER_EXCHANGE)

RECEIVER_POWER_DOWN = InvalidatingCondition(_RECEIVER_POWER_DOWN)
