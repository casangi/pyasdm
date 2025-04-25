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
# File FilterMode.py

# to keep track of the attributes added to this class for each value of this enumeration

_filterModeDict = {}

# the possible enumerations

_FILTER_NA = 0  #  Not Applicable (2 antenna prototype). The Tunable Filter Banks are not implemented

_FILTER_TDM = (
    1  # Time Division Mode. In this mode the Tunable Filter banks are bypassed
)

_FILTER_TFB = 2  # The Tunable Filter Bank is implemented and used

_UNDEFINED = 3  # Not defined or not applicable.


# their names in a dictionary
_filterModeNames = {}

_filterModeNames[_FILTER_NA] = "FILTER_NA"

_filterModeNames[_FILTER_TDM] = "FILTER_TDM"

_filterModeNames[_FILTER_TFB] = "FILTER_TFB"

_filterModeNames[_UNDEFINED] = "UNDEFINED"


class FilterMode:
    """
    A class for the FilterMode enumeration.
    """

    # The value of this FilterMode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, filterMode):
        # construct a FilterMode from an integer, a string, or another FilterMode
        # if filterMode is a string, convert it to an instance of this class using literal
        if isinstance(filterMode, FilterMode):
            # copy constructor
            self._value = filterMode.getValue()
            self._name = filterMode.getName()
        elif isinstance(filterMode, str):
            # convert it to an instance of this class using literal
            thisEnum = FilterMode.literal(filterMode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if filterMode not in _filterModeNames:
                raise ValueError("unrecognized FilterMode")
            self._value = filterMode
            self._name = _filterModeNames[filterMode]
            if self._name not in _filterModeDict:
                # add this FilterMode as an attribute to this class using its name
                setattr(FilterMode, self._name, self)
                _filterModeDict[self._name] = getattr(FilterMode, self._name)

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
        Returns True if other is a FilterMode and its value is the same as this one.
        """
        return isinstance(other, FilterMode) and (other.getValue() == self.getValue())

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
        the number of known enumerators in FilterMode
        """
        return len(_filterModeNames)

    @staticmethod
    def name(filterMode):
        """
        Returns the string form of filterMode
        """
        return str(filterMode)

    @staticmethod
    def names():
        """
        Return the list of all known FilterMode enumeration names
        """
        return list(_filterModeNames.values())

    @staticmethod
    def newFilterMode(name):
        """
        Equivalent to the literal method
        """
        return FilterMode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the FilterMode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(FilterMode, name):
            raise ValueError("Unrecognized FilterMode name")
        return FilterMode(getattr(FilterMode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a FilterMode from an integration matching an enumeration.
        """
        return FilterMode(i)


FILTER_NA = FilterMode(_FILTER_NA)

FILTER_TDM = FilterMode(_FILTER_TDM)

FILTER_TFB = FilterMode(_FILTER_TFB)

UNDEFINED = FilterMode(_UNDEFINED)
