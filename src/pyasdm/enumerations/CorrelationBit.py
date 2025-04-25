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
# File CorrelationBit.py

# to keep track of the attributes added to this class for each value of this enumeration

_correlationBitDict = {}

# the possible enumerations

_BITS_2x2 = 0  # two bit correlation

_BITS_3x3 = 1  #  three bit correlation

_BITS_4x4 = 2  # four bit correlation


# their names in a dictionary
_correlationBitNames = {}

_correlationBitNames[_BITS_2x2] = "BITS_2x2"

_correlationBitNames[_BITS_3x3] = "BITS_3x3"

_correlationBitNames[_BITS_4x4] = "BITS_4x4"


class CorrelationBit:
    """
    A class for the CorrelationBit enumeration.
    """

    # The value of this CorrelationBit, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, correlationBit):
        # construct a CorrelationBit from an integer, a string, or another CorrelationBit
        # if correlationBit is a string, convert it to an instance of this class using literal
        if isinstance(correlationBit, CorrelationBit):
            # copy constructor
            self._value = correlationBit.getValue()
            self._name = correlationBit.getName()
        elif isinstance(correlationBit, str):
            # convert it to an instance of this class using literal
            thisEnum = CorrelationBit.literal(correlationBit)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if correlationBit not in _correlationBitNames:
                raise ValueError("unrecognized CorrelationBit")
            self._value = correlationBit
            self._name = _correlationBitNames[correlationBit]
            if self._name not in _correlationBitDict:
                # add this CorrelationBit as an attribute to this class using its name
                setattr(CorrelationBit, self._name, self)
                _correlationBitDict[self._name] = getattr(CorrelationBit, self._name)

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
        Returns True if other is a CorrelationBit and its value is the same as this one.
        """
        return isinstance(other, CorrelationBit) and (
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
        the number of known enumerators in CorrelationBit
        """
        return len(_correlationBitNames)

    @staticmethod
    def name(correlationBit):
        """
        Returns the string form of correlationBit
        """
        return str(correlationBit)

    @staticmethod
    def names():
        """
        Return the list of all known CorrelationBit enumeration names
        """
        return list(_correlationBitNames.values())

    @staticmethod
    def newCorrelationBit(name):
        """
        Equivalent to the literal method
        """
        return CorrelationBit.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the CorrelationBit enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(CorrelationBit, name):
            raise ValueError("Unrecognized CorrelationBit name")
        return CorrelationBit(getattr(CorrelationBit, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a CorrelationBit from an integration matching an enumeration.
        """
        return CorrelationBit(i)


BITS_2x2 = CorrelationBit(_BITS_2x2)

BITS_3x3 = CorrelationBit(_BITS_3x3)

BITS_4x4 = CorrelationBit(_BITS_4x4)
