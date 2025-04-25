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
# File WVRMethod.py

# to keep track of the attributes added to this class for each value of this enumeration

_wVRMethodDict = {}

# the possible enumerations

_ATM_MODEL = 0  # WVR data reduction uses ATM model

_EMPIRICAL = 1  # WVR data reduction optimized using actual phase data


# their names in a dictionary
_wVRMethodNames = {}

_wVRMethodNames[_ATM_MODEL] = "ATM_MODEL"

_wVRMethodNames[_EMPIRICAL] = "EMPIRICAL"


class WVRMethod:
    """
    A class for the WVRMethod enumeration.
    """

    # The value of this WVRMethod, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, wVRMethod):
        # construct a WVRMethod from an integer, a string, or another WVRMethod
        # if wVRMethod is a string, convert it to an instance of this class using literal
        if isinstance(wVRMethod, WVRMethod):
            # copy constructor
            self._value = wVRMethod.getValue()
            self._name = wVRMethod.getName()
        elif isinstance(wVRMethod, str):
            # convert it to an instance of this class using literal
            thisEnum = WVRMethod.literal(wVRMethod)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if wVRMethod not in _wVRMethodNames:
                raise ValueError("unrecognized WVRMethod")
            self._value = wVRMethod
            self._name = _wVRMethodNames[wVRMethod]
            if self._name not in _wVRMethodDict:
                # add this WVRMethod as an attribute to this class using its name
                setattr(WVRMethod, self._name, self)
                _wVRMethodDict[self._name] = getattr(WVRMethod, self._name)

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
        Returns True if other is a WVRMethod and its value is the same as this one.
        """
        return isinstance(other, WVRMethod) and (other.getValue() == self.getValue())

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
        the number of known enumerators in WVRMethod
        """
        return len(_wVRMethodNames)

    @staticmethod
    def name(wVRMethod):
        """
        Returns the string form of wVRMethod
        """
        return str(wVRMethod)

    @staticmethod
    def names():
        """
        Return the list of all known WVRMethod enumeration names
        """
        return list(_wVRMethodNames.values())

    @staticmethod
    def newWVRMethod(name):
        """
        Equivalent to the literal method
        """
        return WVRMethod.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the WVRMethod enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(WVRMethod, name):
            raise ValueError("Unrecognized WVRMethod name")
        return WVRMethod(getattr(WVRMethod, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a WVRMethod from an integration matching an enumeration.
        """
        return WVRMethod(i)


ATM_MODEL = WVRMethod(_ATM_MODEL)

EMPIRICAL = WVRMethod(_EMPIRICAL)
