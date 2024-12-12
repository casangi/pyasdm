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
# File AntennaType.py

# to keep track of the attributes added to this class for each value of this enumeration

_antennaTypeDict = {}

# the possible enumerations

_GROUND_BASED = 0  # Ground-based antenna

_SPACE_BASED = 1  # Antenna in a spacecraft

_TRACKING_STN = 2  # Space-tracking station antenna


# their names in a dictionary
_antennaTypeNames = {}

_antennaTypeNames[_GROUND_BASED] = "GROUND_BASED"

_antennaTypeNames[_SPACE_BASED] = "SPACE_BASED"

_antennaTypeNames[_TRACKING_STN] = "TRACKING_STN"


class AntennaType:
    """
    A class for the AntennaType enumeration.
    """

    # The value of this AntennaType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, antennaType):
        # construct a AntennaType from an integer, a string, or another AntennaType
        # if antennaType is a string, convert it to an instance of this class using literal
        if isinstance(antennaType, AntennaType):
            # copy constructor
            self._value = antennaType.getValue()
            self._name = antennaType.getName()
        elif isinstance(antennaType, str):
            # convert it to an instance of this class using literal
            thisEnum = AntennaType.literal(antennaType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if antennaType not in _antennaTypeNames:
                raise ValueError("unrecognized AntennaType")
            self._value = antennaType
            self._name = _antennaTypeNames[antennaType]
            if self._name not in _antennaTypeDict:
                # add this AntennaType as an attribute to this class using its name
                setattr(AntennaType, self._name, self)
                _antennaTypeDict[self._name] = getattr(AntennaType, self._name)

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
        the number of known enumerators in AntennaType
        """
        return len(_antennaTypeNames)

    @staticmethod
    def name(antennaType):
        """
        Returns the string form of the AntennaType
        """
        return antennaType.getName()

    @staticmethod
    def toString(antennaType):
        """
        Equivalent to the name method
        """
        return AntennaType.name(antennaType)

    @staticmethod
    def names():
        """
        Return the list of all known AntennaType enumeration names
        """
        return list(_antennaTypeNames.values())

    @staticmethod
    def newAntennaType(name):
        """
        Equivalent to the literal method
        """
        return AntennaType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the AntennaType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(AntennaType, name):
            raise ValueError("Unrecognized AntennaType name")
        return AntennaType(getattr(AntennaType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a AntennaType from an integration matching an enumeration.
        """
        return AntennaType(i)


GROUND_BASED = AntennaType(_GROUND_BASED)

SPACE_BASED = AntennaType(_SPACE_BASED)

TRACKING_STN = AntennaType(_TRACKING_STN)
