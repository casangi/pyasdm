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
# File DifferenceType.py

# to keep track of the attributes added to this class for each value of this enumeration

_differenceTypeDict = {}

# the possible enumerations

_PREDICTED = 0  #

_PRELIMINARY = 1  #

_RAPID = 2  #

_FINAL = 3  #


# their names in a dictionary
_differenceTypeNames = {}

_differenceTypeNames[_PREDICTED] = "PREDICTED"

_differenceTypeNames[_PRELIMINARY] = "PRELIMINARY"

_differenceTypeNames[_RAPID] = "RAPID"

_differenceTypeNames[_FINAL] = "FINAL"


class DifferenceType:
    """
    A class for the DifferenceType enumeration.
    """

    # The value of this DifferenceType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, differenceType):
        # construct a DifferenceType from an integer, a string, or another DifferenceType
        # if differenceType is a string, convert it to an instance of this class using literal
        if isinstance(differenceType, DifferenceType):
            # copy constructor
            self._value = differenceType.getValue()
            self._name = differenceType.getName()
        elif isinstance(differenceType, str):
            # convert it to an instance of this class using literal
            thisEnum = DifferenceType.literal(differenceType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if differenceType not in _differenceTypeNames:
                raise ValueError("unrecognized DifferenceType")
            self._value = differenceType
            self._name = _differenceTypeNames[differenceType]
            if self._name not in _differenceTypeDict:
                # add this DifferenceType as an attribute to this class using its name
                setattr(DifferenceType, self._name, self)
                _differenceTypeDict[self._name] = getattr(DifferenceType, self._name)

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
        the number of known enumerators in DifferenceType
        """
        return len(_differenceTypeNames)

    @staticmethod
    def name(differenceType):
        """
        Returns the string form of the DifferenceType
        """
        return differenceType.getName()

    @staticmethod
    def toString(differenceType):
        """
        Equivalent to the name method
        """
        return DifferenceType.name(differenceType)

    @staticmethod
    def names():
        """
        Return the list of all known DifferenceType enumeration names
        """
        return list(_differenceTypeNames.values())

    @staticmethod
    def newDifferenceType(name):
        """
        Equivalent to the literal method
        """
        return DifferenceType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the DifferenceType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(DifferenceType, name):
            raise ValueError("Unrecognized DifferenceType name")
        return DifferenceType(getattr(DifferenceType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a DifferenceType from an integration matching an enumeration.
        """
        return DifferenceType(i)


PREDICTED = DifferenceType(_PREDICTED)

PRELIMINARY = DifferenceType(_PRELIMINARY)

RAPID = DifferenceType(_RAPID)

FINAL = DifferenceType(_FINAL)
