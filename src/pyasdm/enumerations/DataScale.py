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
# File DataScale.py

# to keep track of the attributes added to this class for each value of this enumeration

_dataScaleDict = {}

# the possible enumerations

_K = 0  # Visibilities in Antenna temperature scale (in Kelvin).

_JY = 1  # Visibilities in Flux Density scale (Jansky).

_CORRELATION = 2  # Correlated Power: WIDAR raw output, normalised by DataValid count.

_CORRELATION_COEFFICIENT = (
    3  # Correlation Coe\14;cient (Correlated Power scaled by autocorrelations).
)


# their names in a dictionary
_dataScaleNames = {}

_dataScaleNames[_K] = "K"

_dataScaleNames[_JY] = "JY"

_dataScaleNames[_CORRELATION] = "CORRELATION"

_dataScaleNames[_CORRELATION_COEFFICIENT] = "CORRELATION_COEFFICIENT"


class DataScale:
    """
    A class for the DataScale enumeration.
    """

    # The value of this DataScale, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, dataScale):
        # construct a DataScale from an integer, a string, or another DataScale
        # if dataScale is a string, convert it to an instance of this class using literal
        if isinstance(dataScale, DataScale):
            # copy constructor
            self._value = dataScale.getValue()
            self._name = dataScale.getName()
        elif isinstance(dataScale, str):
            # convert it to an instance of this class using literal
            thisEnum = DataScale.literal(dataScale)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if dataScale not in _dataScaleNames:
                raise ValueError("unrecognized DataScale")
            self._value = dataScale
            self._name = _dataScaleNames[dataScale]
            if self._name not in _dataScaleDict:
                # add this DataScale as an attribute to this class using its name
                setattr(DataScale, self._name, self)
                _dataScaleDict[self._name] = getattr(DataScale, self._name)

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
        Returns True if other is a DataScale and its value is the same as this one.
        """
        return isinstance(other, DataScale) and (other.getValue() == self.getValue())

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
        the number of known enumerators in DataScale
        """
        return len(_dataScaleNames)

    @staticmethod
    def name(dataScale):
        """
        Returns the string form of dataScale
        """
        return str(dataScale)

    @staticmethod
    def names():
        """
        Return the list of all known DataScale enumeration names
        """
        return list(_dataScaleNames.values())

    @staticmethod
    def newDataScale(name):
        """
        Equivalent to the literal method
        """
        return DataScale.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the DataScale enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(DataScale, name):
            raise ValueError("Unrecognized DataScale name")
        return DataScale(getattr(DataScale, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a DataScale from an integration matching an enumeration.
        """
        return DataScale(i)


K = DataScale(_K)

JY = DataScale(_JY)

CORRELATION = DataScale(_CORRELATION)

CORRELATION_COEFFICIENT = DataScale(_CORRELATION_COEFFICIENT)
