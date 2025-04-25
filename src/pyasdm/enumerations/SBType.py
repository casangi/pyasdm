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
# File SBType.py

# to keep track of the attributes added to this class for each value of this enumeration

_sBTypeDict = {}

# the possible enumerations

_OBSERVATORY = 0  # Observatory mode scheduling block

_OBSERVER = 1  # Observer mode scheduling block

_EXPERT = 2  # Expert mode scheduling block


# their names in a dictionary
_sBTypeNames = {}

_sBTypeNames[_OBSERVATORY] = "OBSERVATORY"

_sBTypeNames[_OBSERVER] = "OBSERVER"

_sBTypeNames[_EXPERT] = "EXPERT"


class SBType:
    """
    A class for the SBType enumeration.
    """

    # The value of this SBType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, sBType):
        # construct a SBType from an integer, a string, or another SBType
        # if sBType is a string, convert it to an instance of this class using literal
        if isinstance(sBType, SBType):
            # copy constructor
            self._value = sBType.getValue()
            self._name = sBType.getName()
        elif isinstance(sBType, str):
            # convert it to an instance of this class using literal
            thisEnum = SBType.literal(sBType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if sBType not in _sBTypeNames:
                raise ValueError("unrecognized SBType")
            self._value = sBType
            self._name = _sBTypeNames[sBType]
            if self._name not in _sBTypeDict:
                # add this SBType as an attribute to this class using its name
                setattr(SBType, self._name, self)
                _sBTypeDict[self._name] = getattr(SBType, self._name)

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
        Returns True if other is a SBType and its value is the same as this one.
        """
        return isinstance(other, SBType) and (other.getValue() == self.getValue())

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
        the number of known enumerators in SBType
        """
        return len(_sBTypeNames)

    @staticmethod
    def name(sBType):
        """
        Returns the string form of sBType
        """
        return str(sBType)

    @staticmethod
    def names():
        """
        Return the list of all known SBType enumeration names
        """
        return list(_sBTypeNames.values())

    @staticmethod
    def newSBType(name):
        """
        Equivalent to the literal method
        """
        return SBType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the SBType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(SBType, name):
            raise ValueError("Unrecognized SBType name")
        return SBType(getattr(SBType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a SBType from an integration matching an enumeration.
        """
        return SBType(i)


OBSERVATORY = SBType(_OBSERVATORY)

OBSERVER = SBType(_OBSERVER)

EXPERT = SBType(_EXPERT)
