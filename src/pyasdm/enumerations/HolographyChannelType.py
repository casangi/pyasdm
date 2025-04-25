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
# File HolographyChannelType.py

# to keep track of the attributes added to this class for each value of this enumeration

_holographyChannelTypeDict = {}

# the possible enumerations

_Q2 = 0  # Quadrature channel auto-product

_QR = 1  # Quadrature channel times Reference channel cross-product

_QS = 2  # Quadrature channel times Signal channel cross-product

_R2 = 3  # Reference channel auto-product

_RS = 4  # Reference channel times Signal channel cross-product

_S2 = 5  # Signal channel auto-product


# their names in a dictionary
_holographyChannelTypeNames = {}

_holographyChannelTypeNames[_Q2] = "Q2"

_holographyChannelTypeNames[_QR] = "QR"

_holographyChannelTypeNames[_QS] = "QS"

_holographyChannelTypeNames[_R2] = "R2"

_holographyChannelTypeNames[_RS] = "RS"

_holographyChannelTypeNames[_S2] = "S2"


class HolographyChannelType:
    """
    A class for the HolographyChannelType enumeration.
    """

    # The value of this HolographyChannelType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, holographyChannelType):
        # construct a HolographyChannelType from an integer, a string, or another HolographyChannelType
        # if holographyChannelType is a string, convert it to an instance of this class using literal
        if isinstance(holographyChannelType, HolographyChannelType):
            # copy constructor
            self._value = holographyChannelType.getValue()
            self._name = holographyChannelType.getName()
        elif isinstance(holographyChannelType, str):
            # convert it to an instance of this class using literal
            thisEnum = HolographyChannelType.literal(holographyChannelType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if holographyChannelType not in _holographyChannelTypeNames:
                raise ValueError("unrecognized HolographyChannelType")
            self._value = holographyChannelType
            self._name = _holographyChannelTypeNames[holographyChannelType]
            if self._name not in _holographyChannelTypeDict:
                # add this HolographyChannelType as an attribute to this class using its name
                setattr(HolographyChannelType, self._name, self)
                _holographyChannelTypeDict[self._name] = getattr(
                    HolographyChannelType, self._name
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
        Returns True if other is a HolographyChannelType and its value is the same as this one.
        """
        return isinstance(other, HolographyChannelType) and (
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
        the number of known enumerators in HolographyChannelType
        """
        return len(_holographyChannelTypeNames)

    @staticmethod
    def name(holographyChannelType):
        """
        Returns the string form of holographyChannelType
        """
        return str(holographyChannelType)

    @staticmethod
    def names():
        """
        Return the list of all known HolographyChannelType enumeration names
        """
        return list(_holographyChannelTypeNames.values())

    @staticmethod
    def newHolographyChannelType(name):
        """
        Equivalent to the literal method
        """
        return HolographyChannelType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the HolographyChannelType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(HolographyChannelType, name):
            raise ValueError("Unrecognized HolographyChannelType name")
        return HolographyChannelType(getattr(HolographyChannelType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a HolographyChannelType from an integration matching an enumeration.
        """
        return HolographyChannelType(i)


Q2 = HolographyChannelType(_Q2)

QR = HolographyChannelType(_QR)

QS = HolographyChannelType(_QS)

R2 = HolographyChannelType(_R2)

RS = HolographyChannelType(_RS)

S2 = HolographyChannelType(_S2)
