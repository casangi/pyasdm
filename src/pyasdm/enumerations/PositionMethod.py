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
# File PositionMethod.py

# to keep track of the attributes added to this class for each value of this enumeration

_positionMethodDict = {}

# the possible enumerations

_DELAY_FITTING = 0  # Delays are measured for each source; the delays are used for fitting antenna position errors.

_PHASE_FITTING = 1  # Phases are measured for each source; these phases are used to fit antenna position errors.


# their names in a dictionary
_positionMethodNames = {}

_positionMethodNames[_DELAY_FITTING] = "DELAY_FITTING"

_positionMethodNames[_PHASE_FITTING] = "PHASE_FITTING"


class PositionMethod:
    """
    A class for the PositionMethod enumeration.
    """

    # The value of this PositionMethod, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, positionMethod):
        # construct a PositionMethod from an integer, a string, or another PositionMethod
        # if positionMethod is a string, convert it to an instance of this class using literal
        if isinstance(positionMethod, PositionMethod):
            # copy constructor
            self._value = positionMethod.getValue()
            self._name = positionMethod.getName()
        elif isinstance(positionMethod, str):
            # convert it to an instance of this class using literal
            thisEnum = PositionMethod.literal(positionMethod)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if positionMethod not in _positionMethodNames:
                raise ValueError("unrecognized PositionMethod")
            self._value = positionMethod
            self._name = _positionMethodNames[positionMethod]
            if self._name not in _positionMethodDict:
                # add this PositionMethod as an attribute to this class using its name
                setattr(PositionMethod, self._name, self)
                _positionMethodDict[self._name] = getattr(PositionMethod, self._name)

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
        Returns True if other is a PositionMethod and its value is the same as this one.
        """
        return isinstance(other, PositionMethod) and (
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
        the number of known enumerators in PositionMethod
        """
        return len(_positionMethodNames)

    @staticmethod
    def name(positionMethod):
        """
        Returns the string form of positionMethod
        """
        return str(positionMethod)

    @staticmethod
    def names():
        """
        Return the list of all known PositionMethod enumeration names
        """
        return list(_positionMethodNames.values())

    @staticmethod
    def newPositionMethod(name):
        """
        Equivalent to the literal method
        """
        return PositionMethod.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the PositionMethod enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(PositionMethod, name):
            raise ValueError("Unrecognized PositionMethod name")
        return PositionMethod(getattr(PositionMethod, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a PositionMethod from an integration matching an enumeration.
        """
        return PositionMethod(i)


DELAY_FITTING = PositionMethod(_DELAY_FITTING)

PHASE_FITTING = PositionMethod(_PHASE_FITTING)
