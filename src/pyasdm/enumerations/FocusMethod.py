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
# File FocusMethod.py

# to keep track of the attributes added to this class for each value of this enumeration

_focusMethodDict = {}

# the possible enumerations

_THREE_POINT = 0  # Three-point measurement

_FIVE_POINT = 1  # Five-point measurement

_HOLOGRAPHY = 2  #


# their names in a dictionary
_focusMethodNames = {}

_focusMethodNames[_THREE_POINT] = "THREE_POINT"

_focusMethodNames[_FIVE_POINT] = "FIVE_POINT"

_focusMethodNames[_HOLOGRAPHY] = "HOLOGRAPHY"


class FocusMethod:
    """
    A class for the FocusMethod enumeration.
    """

    # The value of this FocusMethod, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, focusMethod):
        # construct a FocusMethod from an integer, a string, or another FocusMethod
        # if focusMethod is a string, convert it to an instance of this class using literal
        if isinstance(focusMethod, FocusMethod):
            # copy constructor
            self._value = focusMethod.getValue()
            self._name = focusMethod.getName()
        elif isinstance(focusMethod, str):
            # convert it to an instance of this class using literal
            thisEnum = FocusMethod.literal(focusMethod)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if focusMethod not in _focusMethodNames:
                raise ValueError("unrecognized FocusMethod")
            self._value = focusMethod
            self._name = _focusMethodNames[focusMethod]
            if self._name not in _focusMethodDict:
                # add this FocusMethod as an attribute to this class using its name
                setattr(FocusMethod, self._name, self)
                _focusMethodDict[self._name] = getattr(FocusMethod, self._name)

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
        Returns True if other is a FocusMethod and its value is the same as this one.
        """
        return isinstance(other, FocusMethod) and (other.getValue() == self.getValue())

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
        the number of known enumerators in FocusMethod
        """
        return len(_focusMethodNames)

    @staticmethod
    def name(focusMethod):
        """
        Returns the string form of focusMethod
        """
        return str(focusMethod)

    @staticmethod
    def names():
        """
        Return the list of all known FocusMethod enumeration names
        """
        return list(_focusMethodNames.values())

    @staticmethod
    def newFocusMethod(name):
        """
        Equivalent to the literal method
        """
        return FocusMethod.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the FocusMethod enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(FocusMethod, name):
            raise ValueError("Unrecognized FocusMethod name")
        return FocusMethod(getattr(FocusMethod, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a FocusMethod from an integration matching an enumeration.
        """
        return FocusMethod(i)


THREE_POINT = FocusMethod(_THREE_POINT)

FIVE_POINT = FocusMethod(_FIVE_POINT)

HOLOGRAPHY = FocusMethod(_HOLOGRAPHY)
