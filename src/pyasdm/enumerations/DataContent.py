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
# File DataContent.py

# to keep track of the attributes added to this class for each value of this enumeration

_dataContentDict = {}

# the possible enumerations

_CROSS_DATA = 0  # Cross-correlation data

_AUTO_DATA = 1  # Auto-correlation data

_ZERO_LAGS = 2  # Zero-lag data

_ACTUAL_TIMES = 3  # :Actual times (mid points of integrations)

_ACTUAL_DURATIONS = 4  # Actual duration of integrations

_WEIGHTS = 5  # Weights

_FLAGS = 6  # Baseband based flags


# their names in a dictionary
_dataContentNames = {}

_dataContentNames[_CROSS_DATA] = "CROSS_DATA"

_dataContentNames[_AUTO_DATA] = "AUTO_DATA"

_dataContentNames[_ZERO_LAGS] = "ZERO_LAGS"

_dataContentNames[_ACTUAL_TIMES] = "ACTUAL_TIMES"

_dataContentNames[_ACTUAL_DURATIONS] = "ACTUAL_DURATIONS"

_dataContentNames[_WEIGHTS] = "WEIGHTS"

_dataContentNames[_FLAGS] = "FLAGS"


class DataContent:
    """
    A class for the DataContent enumeration.
    """

    # The value of this DataContent, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, dataContent):
        # construct a DataContent from an integer, a string, or another DataContent
        # if dataContent is a string, convert it to an instance of this class using literal
        if isinstance(dataContent, DataContent):
            # copy constructor
            self._value = dataContent.getValue()
            self._name = dataContent.getName()
        elif isinstance(dataContent, str):
            # convert it to an instance of this class using literal
            thisEnum = DataContent.literal(dataContent)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if dataContent not in _dataContentNames:
                raise ValueError("unrecognized DataContent")
            self._value = dataContent
            self._name = _dataContentNames[dataContent]
            if self._name not in _dataContentDict:
                # add this DataContent as an attribute to this class using its name
                setattr(DataContent, self._name, self)
                _dataContentDict[self._name] = getattr(DataContent, self._name)

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
        Returns True if other is a DataContent and its value is the same as this one.
        """
        return isinstance(other, DataContent) and (other.getValue() == self.getValue())

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
        the number of known enumerators in DataContent
        """
        return len(_dataContentNames)

    @staticmethod
    def name(dataContent):
        """
        Returns the string form of dataContent
        """
        return str(dataContent)

    @staticmethod
    def names():
        """
        Return the list of all known DataContent enumeration names
        """
        return list(_dataContentNames.values())

    @staticmethod
    def newDataContent(name):
        """
        Equivalent to the literal method
        """
        return DataContent.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the DataContent enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(DataContent, name):
            raise ValueError("Unrecognized DataContent name")
        return DataContent(getattr(DataContent, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a DataContent from an integration matching an enumeration.
        """
        return DataContent(i)


CROSS_DATA = DataContent(_CROSS_DATA)

AUTO_DATA = DataContent(_AUTO_DATA)

ZERO_LAGS = DataContent(_ZERO_LAGS)

ACTUAL_TIMES = DataContent(_ACTUAL_TIMES)

ACTUAL_DURATIONS = DataContent(_ACTUAL_DURATIONS)

WEIGHTS = DataContent(_WEIGHTS)

FLAGS = DataContent(_FLAGS)
