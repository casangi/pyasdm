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
# File AccumMode.py

# to keep track of the attributes added to this class for each value of this enumeration

_accumModeDict = {}

# the possible enumerations

_FAST = 0  # fast dump time. ALMA use case : 1 ms dump time, available only for autocorrelation.

_NORMAL = 1  # normal dump time. ALMA use case : 16ms dump time, available for both autocorrelation and cross-orrelation.

_UNDEFINED = 2  # Not defined or not applicable.


# their names in a dictionary
_accumModeNames = {}

_accumModeNames[_FAST] = "FAST"

_accumModeNames[_NORMAL] = "NORMAL"

_accumModeNames[_UNDEFINED] = "UNDEFINED"


class AccumMode:
    """
    A class for the AccumMode enumeration.
    """

    # The value of this AccumMode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, accumMode):
        # construct a AccumMode from an integer, a string, or another AccumMode
        # if accumMode is a string, convert it to an instance of this class using literal
        if isinstance(accumMode, AccumMode):
            # copy constructor
            self._value = accumMode.getValue()
            self._name = accumMode.getName()
        elif isinstance(accumMode, str):
            # convert it to an instance of this class using literal
            thisEnum = AccumMode.literal(accumMode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if accumMode not in _accumModeNames:
                raise ValueError("unrecognized AccumMode")
            self._value = accumMode
            self._name = _accumModeNames[accumMode]
            if self._name not in _accumModeDict:
                # add this AccumMode as an attribute to this class using its name
                setattr(AccumMode, self._name, self)
                _accumModeDict[self._name] = getattr(AccumMode, self._name)

    def getValue(self):
        return self._value

    def getName(self):
        return self._name

    # by convention with the other languages, these are all static methods
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
        the number of known enumerators in AccumMode
        """
        return len(_accumModeNames)

    @staticmethod
    def name(accumMode):
        """
        Returns the string form of the AccumMode
        """
        return accumMode.getName()

    @staticmethod
    def toString(accumMode):
        """
        Equivalent to the name method
        """
        return AccumMode.name(accumMode)

    @staticmethod
    def names():
        """
        Return the list of all known AccumMode enumeration names
        """
        return list(_accumModeNames.values())

    @staticmethod
    def newAccumMode(name):
        """
        Equivalent to the literal method
        """
        return AccumMode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the AccumMode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(AccumMode, name):
            raise ValueError("Unrecognized AccumMode name")
        return AccumMode(getattr(AccumMode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a AccumMode from an integration matching an enumeration.
        """
        return AccumMode(i)


FAST = AccumMode(_FAST)

NORMAL = AccumMode(_NORMAL)

UNDEFINED = AccumMode(_UNDEFINED)
