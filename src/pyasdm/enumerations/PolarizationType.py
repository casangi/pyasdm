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
# File PolarizationType.py

# to keep track of the attributes added to this class for each value of this enumeration

_polarizationTypeDict = {}

# the possible enumerations

_R = 0  # Right-handed Circular

_L = 1  # Left-handed Circular

_X = 2  # X linear

_Y = 3  # Y linear

_BOTH = 4  # The receptor responds to both polarizations.


# their names in a dictionary
_polarizationTypeNames = {}

_polarizationTypeNames[_R] = "R"

_polarizationTypeNames[_L] = "L"

_polarizationTypeNames[_X] = "X"

_polarizationTypeNames[_Y] = "Y"

_polarizationTypeNames[_BOTH] = "BOTH"


class PolarizationType:
    """
    A class for the PolarizationType enumeration.
    """

    # The value of this PolarizationType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, polarizationType):
        # construct a PolarizationType from an integer, a string, or another PolarizationType
        # if polarizationType is a string, convert it to an instance of this class using literal
        if isinstance(polarizationType, PolarizationType):
            # copy constructor
            self._value = polarizationType.getValue()
            self._name = polarizationType.getName()
        elif isinstance(polarizationType, str):
            # convert it to an instance of this class using literal
            thisEnum = PolarizationType.literal(polarizationType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if polarizationType not in _polarizationTypeNames:
                raise ValueError("unrecognized PolarizationType")
            self._value = polarizationType
            self._name = _polarizationTypeNames[polarizationType]
            if self._name not in _polarizationTypeDict:
                # add this PolarizationType as an attribute to this class using its name
                setattr(PolarizationType, self._name, self)
                _polarizationTypeDict[self._name] = getattr(
                    PolarizationType, self._name
                )

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
        the number of known enumerators in PolarizationType
        """
        return len(_polarizationTypeNames)

    @staticmethod
    def name(polarizationType):
        """
        Returns the string form of the PolarizationType
        """
        return polarizationType.getName()

    @staticmethod
    def toString(polarizationType):
        """
        Equivalent to the name method
        """
        return PolarizationType.name(polarizationType)

    @staticmethod
    def names():
        """
        Return the list of all known PolarizationType enumeration names
        """
        return list(_polarizationTypeNames.values())

    @staticmethod
    def newPolarizationType(name):
        """
        Equivalent to the literal method
        """
        return PolarizationType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the PolarizationType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(PolarizationType, name):
            raise ValueError("Unrecognized PolarizationType name")
        return PolarizationType(getattr(PolarizationType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a PolarizationType from an integration matching an enumeration.
        """
        return PolarizationType(i)


R = PolarizationType(_R)

L = PolarizationType(_L)

X = PolarizationType(_X)

Y = PolarizationType(_Y)

BOTH = PolarizationType(_BOTH)
