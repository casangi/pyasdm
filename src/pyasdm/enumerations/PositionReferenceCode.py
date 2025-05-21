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
# File PositionReferenceCode.py

# to keep track of the attributes added to this class for each value of this enumeration

_positionReferenceCodeDict = {}

# the possible enumerations

_ITRF = 0  # International Terrestrial Reference Frame.

_WGS84 = 1  # World Geodetic System.

_SITE = 2  # Site reference coordinate system (ALMA-80.05.00.00-009-B-SPE).

_STATION = 3  # Antenna station reference coordinate system (ALMA-80.05.00.00-009-SPE).

_YOKE = 4  # Antenna yoke reference coordinate system (ALMA-980.05.00.00-009-B-SPE)

_REFLECTOR = (
    5  # Antenna reflector reference coordinate system (ALMA-80.05.00.00-009-B-SPE).
)


# their names in a dictionary
_positionReferenceCodeNames = {}

_positionReferenceCodeNames[_ITRF] = "ITRF"

_positionReferenceCodeNames[_WGS84] = "WGS84"

_positionReferenceCodeNames[_SITE] = "SITE"

_positionReferenceCodeNames[_STATION] = "STATION"

_positionReferenceCodeNames[_YOKE] = "YOKE"

_positionReferenceCodeNames[_REFLECTOR] = "REFLECTOR"


class PositionReferenceCode:
    """
    A class for the PositionReferenceCode enumeration.
    """

    # The value of this PositionReferenceCode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, positionReferenceCode):
        # construct a PositionReferenceCode from an integer, a string, or another PositionReferenceCode
        # if positionReferenceCode is a string, convert it to an instance of this class using literal
        if isinstance(positionReferenceCode, PositionReferenceCode):
            # copy constructor
            self._value = positionReferenceCode.getValue()
            self._name = positionReferenceCode.getName()
        elif isinstance(positionReferenceCode, str):
            # convert it to an instance of this class using literal
            thisEnum = PositionReferenceCode.literal(positionReferenceCode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if positionReferenceCode not in _positionReferenceCodeNames:
                raise ValueError("unrecognized PositionReferenceCode")
            self._value = positionReferenceCode
            self._name = _positionReferenceCodeNames[positionReferenceCode]
            if self._name not in _positionReferenceCodeDict:
                # add this PositionReferenceCode as an attribute to this class using its name
                setattr(PositionReferenceCode, self._name, self)
                _positionReferenceCodeDict[self._name] = getattr(
                    PositionReferenceCode, self._name
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
        Returns True if other is a PositionReferenceCode and its value is the same as this one.
        """
        return isinstance(other, PositionReferenceCode) and (
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
        the number of known enumerators in PositionReferenceCode
        """
        return len(_positionReferenceCodeNames)

    @staticmethod
    def name(positionReferenceCode):
        """
        Returns the string form of positionReferenceCode
        """
        return str(positionReferenceCode)

    @staticmethod
    def names():
        """
        Return the list of all known PositionReferenceCode enumeration names
        """
        return list(_positionReferenceCodeNames.values())

    @staticmethod
    def newPositionReferenceCode(name):
        """
        Equivalent to the literal method
        """
        return PositionReferenceCode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the PositionReferenceCode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(PositionReferenceCode, name):
            raise ValueError("Unrecognized PositionReferenceCode name")
        return PositionReferenceCode(getattr(PositionReferenceCode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a PositionReferenceCode from an integration matching an enumeration.
        """
        return PositionReferenceCode(i)


ITRF = PositionReferenceCode(_ITRF)

WGS84 = PositionReferenceCode(_WGS84)

SITE = PositionReferenceCode(_SITE)

STATION = PositionReferenceCode(_STATION)

YOKE = PositionReferenceCode(_YOKE)

REFLECTOR = PositionReferenceCode(_REFLECTOR)
