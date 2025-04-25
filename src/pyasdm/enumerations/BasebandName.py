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
# File BasebandName.py

# to keep track of the attributes added to this class for each value of this enumeration

_basebandNameDict = {}

# the possible enumerations

_NOBB = 0  # Baseband not applicable.

_BB_1 = 1  # Baseband one

_BB_2 = 2  # Baseband two

_BB_3 = 3  # Baseband three

_BB_4 = 4  # Baseband four

_BB_5 = 5  # Baseband five (not ALMA)

_BB_6 = 6  # Baseband six (not ALMA)

_BB_7 = 7  # Baseband seven (not ALMA)

_BB_8 = 8  # Baseband eight (not ALMA)

_BB_ALL = 9  # All ALMA basebands (i.e. all available basebands)

_A1C1_3BIT = 10  #

_A2C2_3BIT = 11  #

_AC_8BIT = 12  #

_B1D1_3BIT = 13  #

_B2D2_3BIT = 14  #

_BD_8BIT = 15  #


# their names in a dictionary
_basebandNameNames = {}

_basebandNameNames[_NOBB] = "NOBB"

_basebandNameNames[_BB_1] = "BB_1"

_basebandNameNames[_BB_2] = "BB_2"

_basebandNameNames[_BB_3] = "BB_3"

_basebandNameNames[_BB_4] = "BB_4"

_basebandNameNames[_BB_5] = "BB_5"

_basebandNameNames[_BB_6] = "BB_6"

_basebandNameNames[_BB_7] = "BB_7"

_basebandNameNames[_BB_8] = "BB_8"

_basebandNameNames[_BB_ALL] = "BB_ALL"

_basebandNameNames[_A1C1_3BIT] = "A1C1_3BIT"

_basebandNameNames[_A2C2_3BIT] = "A2C2_3BIT"

_basebandNameNames[_AC_8BIT] = "AC_8BIT"

_basebandNameNames[_B1D1_3BIT] = "B1D1_3BIT"

_basebandNameNames[_B2D2_3BIT] = "B2D2_3BIT"

_basebandNameNames[_BD_8BIT] = "BD_8BIT"


class BasebandName:
    """
    A class for the BasebandName enumeration.
    """

    # The value of this BasebandName, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, basebandName):
        # construct a BasebandName from an integer, a string, or another BasebandName
        # if basebandName is a string, convert it to an instance of this class using literal
        if isinstance(basebandName, BasebandName):
            # copy constructor
            self._value = basebandName.getValue()
            self._name = basebandName.getName()
        elif isinstance(basebandName, str):
            # convert it to an instance of this class using literal
            thisEnum = BasebandName.literal(basebandName)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if basebandName not in _basebandNameNames:
                raise ValueError("unrecognized BasebandName")
            self._value = basebandName
            self._name = _basebandNameNames[basebandName]
            if self._name not in _basebandNameDict:
                # add this BasebandName as an attribute to this class using its name
                setattr(BasebandName, self._name, self)
                _basebandNameDict[self._name] = getattr(BasebandName, self._name)

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
        Returns True if other is a BasebandName and its value is the same as this one.
        """
        return isinstance(other, BasebandName) and (other.getValue() == self.getValue())

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
        the number of known enumerators in BasebandName
        """
        return len(_basebandNameNames)

    @staticmethod
    def name(basebandName):
        """
        Returns the string form of basebandName
        """
        return str(basebandName)

    @staticmethod
    def names():
        """
        Return the list of all known BasebandName enumeration names
        """
        return list(_basebandNameNames.values())

    @staticmethod
    def newBasebandName(name):
        """
        Equivalent to the literal method
        """
        return BasebandName.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the BasebandName enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(BasebandName, name):
            raise ValueError("Unrecognized BasebandName name")
        return BasebandName(getattr(BasebandName, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a BasebandName from an integration matching an enumeration.
        """
        return BasebandName(i)


NOBB = BasebandName(_NOBB)

BB_1 = BasebandName(_BB_1)

BB_2 = BasebandName(_BB_2)

BB_3 = BasebandName(_BB_3)

BB_4 = BasebandName(_BB_4)

BB_5 = BasebandName(_BB_5)

BB_6 = BasebandName(_BB_6)

BB_7 = BasebandName(_BB_7)

BB_8 = BasebandName(_BB_8)

BB_ALL = BasebandName(_BB_ALL)

A1C1_3BIT = BasebandName(_A1C1_3BIT)

A2C2_3BIT = BasebandName(_A2C2_3BIT)

AC_8BIT = BasebandName(_AC_8BIT)

B1D1_3BIT = BasebandName(_B1D1_3BIT)

B2D2_3BIT = BasebandName(_B2D2_3BIT)

BD_8BIT = BasebandName(_BD_8BIT)
