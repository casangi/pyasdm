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
# File CorrelationMode.py

# to keep track of the attributes added to this class for each value of this enumeration

_correlationModeDict = {}

# the possible enumerations

_CROSS_ONLY = 0  # Cross-correlations only [not for ALMA]

_AUTO_ONLY = 1  # Auto-correlations only

_CROSS_AND_AUTO = 2  # Auto-correlations and Cross-correlations


# their names in a dictionary
_correlationModeNames = {}

_correlationModeNames[_CROSS_ONLY] = "CROSS_ONLY"

_correlationModeNames[_AUTO_ONLY] = "AUTO_ONLY"

_correlationModeNames[_CROSS_AND_AUTO] = "CROSS_AND_AUTO"


class CorrelationMode:
    """
    A class for the CorrelationMode enumeration.
    """

    # The value of this CorrelationMode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, correlationMode):
        # construct a CorrelationMode from an integer, a string, or another CorrelationMode
        # if correlationMode is a string, convert it to an instance of this class using literal
        if isinstance(correlationMode, CorrelationMode):
            # copy constructor
            self._value = correlationMode.getValue()
            self._name = correlationMode.getName()
        elif isinstance(correlationMode, str):
            # convert it to an instance of this class using literal
            thisEnum = CorrelationMode.literal(correlationMode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if correlationMode not in _correlationModeNames:
                raise ValueError("unrecognized CorrelationMode")
            self._value = correlationMode
            self._name = _correlationModeNames[correlationMode]
            if self._name not in _correlationModeDict:
                # add this CorrelationMode as an attribute to this class using its name
                setattr(CorrelationMode, self._name, self)
                _correlationModeDict[self._name] = getattr(CorrelationMode, self._name)

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
        the number of known enumerators in CorrelationMode
        """
        return len(_correlationModeNames)

    @staticmethod
    def name(correlationMode):
        """
        Returns the string form of the CorrelationMode
        """
        return correlationMode.getName()

    @staticmethod
    def toString(correlationMode):
        """
        Equivalent to the name method
        """
        return CorrelationMode.name(correlationMode)

    @staticmethod
    def names():
        """
        Return the list of all known CorrelationMode enumeration names
        """
        return list(_correlationModeNames.values())

    @staticmethod
    def newCorrelationMode(name):
        """
        Equivalent to the literal method
        """
        return CorrelationMode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the CorrelationMode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(CorrelationMode, name):
            raise ValueError("Unrecognized CorrelationMode name")
        return CorrelationMode(getattr(CorrelationMode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a CorrelationMode from an integration matching an enumeration.
        """
        return CorrelationMode(i)


CROSS_ONLY = CorrelationMode(_CROSS_ONLY)

AUTO_ONLY = CorrelationMode(_AUTO_ONLY)

CROSS_AND_AUTO = CorrelationMode(_CROSS_AND_AUTO)
