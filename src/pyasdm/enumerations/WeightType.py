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
# File WeightType.py

# to keep track of the attributes added to this class for each value of this enumeration

_weightTypeDict = {}

# the possible enumerations

_K = 0  # Based on System temperature.

_JY = 1  # Based on Flux (include antenna efficiency).

_COUNT_WEIGHT = 2  # Square-root of the number of samples (i.e. sqrt(bandwidth * time))


# their names in a dictionary
_weightTypeNames = {}

_weightTypeNames[_K] = "K"

_weightTypeNames[_JY] = "JY"

_weightTypeNames[_COUNT_WEIGHT] = "COUNT_WEIGHT"


class WeightType:
    """
    A class for the WeightType enumeration.
    """

    # The value of this WeightType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, weightType):
        # construct a WeightType from an integer, a string, or another WeightType
        # if weightType is a string, convert it to an instance of this class using literal
        if isinstance(weightType, WeightType):
            # copy constructor
            self._value = weightType.getValue()
            self._name = weightType.getName()
        elif isinstance(weightType, str):
            # convert it to an instance of this class using literal
            thisEnum = WeightType.literal(weightType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if weightType not in _weightTypeNames:
                raise ValueError("unrecognized WeightType")
            self._value = weightType
            self._name = _weightTypeNames[weightType]
            if self._name not in _weightTypeDict:
                # add this WeightType as an attribute to this class using its name
                setattr(WeightType, self._name, self)
                _weightTypeDict[self._name] = getattr(WeightType, self._name)

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
        Returns True if other is a WeightType and its value is the same as this one.
        """
        return isinstance(other, WeightType) and (other.getValue() == self.getValue())

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
        the number of known enumerators in WeightType
        """
        return len(_weightTypeNames)

    @staticmethod
    def name(weightType):
        """
        Returns the string form of weightType
        """
        return str(weightType)

    @staticmethod
    def names():
        """
        Return the list of all known WeightType enumeration names
        """
        return list(_weightTypeNames.values())

    @staticmethod
    def newWeightType(name):
        """
        Equivalent to the literal method
        """
        return WeightType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the WeightType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(WeightType, name):
            raise ValueError("Unrecognized WeightType name")
        return WeightType(getattr(WeightType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a WeightType from an integration matching an enumeration.
        """
        return WeightType(i)


K = WeightType(_K)

JY = WeightType(_JY)

COUNT_WEIGHT = WeightType(_COUNT_WEIGHT)
