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
# File CalCurveType.py

# to keep track of the attributes added to this class for each value of this enumeration

_calCurveTypeDict = {}

# the possible enumerations

_AMPLITUDE = 0  # Calibration curve is Amplitude

_PHASE = 1  # Calibration curve is phase

_UNDEFINED = 2  # Not applicable.


# their names in a dictionary
_calCurveTypeNames = {}

_calCurveTypeNames[_AMPLITUDE] = "AMPLITUDE"

_calCurveTypeNames[_PHASE] = "PHASE"

_calCurveTypeNames[_UNDEFINED] = "UNDEFINED"


class CalCurveType:
    """
    A class for the CalCurveType enumeration.
    """

    # The value of this CalCurveType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, calCurveType):
        # construct a CalCurveType from an integer, a string, or another CalCurveType
        # if calCurveType is a string, convert it to an instance of this class using literal
        if isinstance(calCurveType, CalCurveType):
            # copy constructor
            self._value = calCurveType.getValue()
            self._name = calCurveType.getName()
        elif isinstance(calCurveType, str):
            # convert it to an instance of this class using literal
            thisEnum = CalCurveType.literal(calCurveType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if calCurveType not in _calCurveTypeNames:
                raise ValueError("unrecognized CalCurveType")
            self._value = calCurveType
            self._name = _calCurveTypeNames[calCurveType]
            if self._name not in _calCurveTypeDict:
                # add this CalCurveType as an attribute to this class using its name
                setattr(CalCurveType, self._name, self)
                _calCurveTypeDict[self._name] = getattr(CalCurveType, self._name)

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
        Returns True if other is a CalCurveType and its value is the same as this one.
        """
        return isinstance(other, CalCurveType) and (other.getValue() == self.getValue())

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
        the number of known enumerators in CalCurveType
        """
        return len(_calCurveTypeNames)

    @staticmethod
    def name(calCurveType):
        """
        Returns the string form of calCurveType
        """
        return str(calCurveType)

    @staticmethod
    def names():
        """
        Return the list of all known CalCurveType enumeration names
        """
        return list(_calCurveTypeNames.values())

    @staticmethod
    def newCalCurveType(name):
        """
        Equivalent to the literal method
        """
        return CalCurveType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the CalCurveType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(CalCurveType, name):
            raise ValueError("Unrecognized CalCurveType name")
        return CalCurveType(getattr(CalCurveType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a CalCurveType from an integration matching an enumeration.
        """
        return CalCurveType(i)


AMPLITUDE = CalCurveType(_AMPLITUDE)

PHASE = CalCurveType(_PHASE)

UNDEFINED = CalCurveType(_UNDEFINED)
