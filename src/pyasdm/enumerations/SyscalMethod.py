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
# File SyscalMethod.py

# to keep track of the attributes added to this class for each value of this enumeration

_syscalMethodDict = {}

# the possible enumerations

_TEMPERATURE_SCALE = 0  # Use single direction data to compute ta* scale

_SKYDIP = 1  # Use a skydip (observing the sky at various elevations) to get atmospheric opacity

_SIDEBAND_RATIO = 2  # Measure the sideband gain ratio.


# their names in a dictionary
_syscalMethodNames = {}

_syscalMethodNames[_TEMPERATURE_SCALE] = "TEMPERATURE_SCALE"

_syscalMethodNames[_SKYDIP] = "SKYDIP"

_syscalMethodNames[_SIDEBAND_RATIO] = "SIDEBAND_RATIO"


class SyscalMethod:
    """
    A class for the SyscalMethod enumeration.
    """

    # The value of this SyscalMethod, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, syscalMethod):
        # construct a SyscalMethod from an integer, a string, or another SyscalMethod
        # if syscalMethod is a string, convert it to an instance of this class using literal
        if isinstance(syscalMethod, SyscalMethod):
            # copy constructor
            self._value = syscalMethod.getValue()
            self._name = syscalMethod.getName()
        elif isinstance(syscalMethod, str):
            # convert it to an instance of this class using literal
            thisEnum = SyscalMethod.literal(syscalMethod)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if syscalMethod not in _syscalMethodNames:
                raise ValueError("unrecognized SyscalMethod")
            self._value = syscalMethod
            self._name = _syscalMethodNames[syscalMethod]
            if self._name not in _syscalMethodDict:
                # add this SyscalMethod as an attribute to this class using its name
                setattr(SyscalMethod, self._name, self)
                _syscalMethodDict[self._name] = getattr(SyscalMethod, self._name)

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
        the number of known enumerators in SyscalMethod
        """
        return len(_syscalMethodNames)

    @staticmethod
    def name(syscalMethod):
        """
        Returns the string form of the SyscalMethod
        """
        return syscalMethod.getName()

    @staticmethod
    def toString(syscalMethod):
        """
        Equivalent to the name method
        """
        return SyscalMethod.name(syscalMethod)

    @staticmethod
    def names():
        """
        Return the list of all known SyscalMethod enumeration names
        """
        return list(_syscalMethodNames.values())

    @staticmethod
    def newSyscalMethod(name):
        """
        Equivalent to the literal method
        """
        return SyscalMethod.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the SyscalMethod enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(SyscalMethod, name):
            raise ValueError("Unrecognized SyscalMethod name")
        return SyscalMethod(getattr(SyscalMethod, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a SyscalMethod from an integration matching an enumeration.
        """
        return SyscalMethod(i)


TEMPERATURE_SCALE = SyscalMethod(_TEMPERATURE_SCALE)

SKYDIP = SyscalMethod(_SKYDIP)

SIDEBAND_RATIO = SyscalMethod(_SIDEBAND_RATIO)
