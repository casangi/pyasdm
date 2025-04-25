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
# File AntennaMake.py

# to keep track of the attributes added to this class for each value of this enumeration

_antennaMakeDict = {}

# the possible enumerations

_AEM_12 = 0  # 12m AEM antenna

_MITSUBISHI_7 = 1  # 7-m Mitsubishi antenna (ACA)

_MITSUBISHI_12_A = 2  # 12-m Mitsubishi antenna (ACA) (refurbished prototype)

_MITSUBISHI_12_B = 3  # 12-m Mitsubishi antenna (ACA) (production)

_VERTEX_12_ATF = 4  # 12-m Vertex antenna prototype

_AEM_12_ATF = 5  # 12-m AEM  antenna prototype

_VERTEX_12 = 6  # 12-m Vertex antenna

_IRAM_15 = 7  # 15-m IRAM antenna

_UNDEFINED = 8  # Not defined or not applicable.


# their names in a dictionary
_antennaMakeNames = {}

_antennaMakeNames[_AEM_12] = "AEM_12"

_antennaMakeNames[_MITSUBISHI_7] = "MITSUBISHI_7"

_antennaMakeNames[_MITSUBISHI_12_A] = "MITSUBISHI_12_A"

_antennaMakeNames[_MITSUBISHI_12_B] = "MITSUBISHI_12_B"

_antennaMakeNames[_VERTEX_12_ATF] = "VERTEX_12_ATF"

_antennaMakeNames[_AEM_12_ATF] = "AEM_12_ATF"

_antennaMakeNames[_VERTEX_12] = "VERTEX_12"

_antennaMakeNames[_IRAM_15] = "IRAM_15"

_antennaMakeNames[_UNDEFINED] = "UNDEFINED"


class AntennaMake:
    """
    A class for the AntennaMake enumeration.
    """

    # The value of this AntennaMake, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, antennaMake):
        # construct a AntennaMake from an integer, a string, or another AntennaMake
        # if antennaMake is a string, convert it to an instance of this class using literal
        if isinstance(antennaMake, AntennaMake):
            # copy constructor
            self._value = antennaMake.getValue()
            self._name = antennaMake.getName()
        elif isinstance(antennaMake, str):
            # convert it to an instance of this class using literal
            thisEnum = AntennaMake.literal(antennaMake)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if antennaMake not in _antennaMakeNames:
                raise ValueError("unrecognized AntennaMake")
            self._value = antennaMake
            self._name = _antennaMakeNames[antennaMake]
            if self._name not in _antennaMakeDict:
                # add this AntennaMake as an attribute to this class using its name
                setattr(AntennaMake, self._name, self)
                _antennaMakeDict[self._name] = getattr(AntennaMake, self._name)

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
        Returns True if other is a AntennaMake and its value is the same as this one.
        """
        return isinstance(other, AntennaMake) and (other.getValue() == self.getValue())

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
        the number of known enumerators in AntennaMake
        """
        return len(_antennaMakeNames)

    @staticmethod
    def name(antennaMake):
        """
        Returns the string form of antennaMake
        """
        return str(antennaMake)

    @staticmethod
    def names():
        """
        Return the list of all known AntennaMake enumeration names
        """
        return list(_antennaMakeNames.values())

    @staticmethod
    def newAntennaMake(name):
        """
        Equivalent to the literal method
        """
        return AntennaMake.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the AntennaMake enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(AntennaMake, name):
            raise ValueError("Unrecognized AntennaMake name")
        return AntennaMake(getattr(AntennaMake, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a AntennaMake from an integration matching an enumeration.
        """
        return AntennaMake(i)


AEM_12 = AntennaMake(_AEM_12)

MITSUBISHI_7 = AntennaMake(_MITSUBISHI_7)

MITSUBISHI_12_A = AntennaMake(_MITSUBISHI_12_A)

MITSUBISHI_12_B = AntennaMake(_MITSUBISHI_12_B)

VERTEX_12_ATF = AntennaMake(_VERTEX_12_ATF)

AEM_12_ATF = AntennaMake(_AEM_12_ATF)

VERTEX_12 = AntennaMake(_VERTEX_12)

IRAM_15 = AntennaMake(_IRAM_15)

UNDEFINED = AntennaMake(_UNDEFINED)
