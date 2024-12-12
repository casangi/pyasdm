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
# File PointingMethod.py

# to keep track of the attributes added to this class for each value of this enumeration

_pointingMethodDict = {}

# the possible enumerations

_THREE_POINT = 0  # Three-point scan

_FOUR_POINT = 1  # Four-point scan

_FIVE_POINT = 2  # Five-point scan

_CROSS = 3  # Cross scan

_CIRCLE = 4  # Circular scan

_HOLOGRAPHY = 5  #


# their names in a dictionary
_pointingMethodNames = {}

_pointingMethodNames[_THREE_POINT] = "THREE_POINT"

_pointingMethodNames[_FOUR_POINT] = "FOUR_POINT"

_pointingMethodNames[_FIVE_POINT] = "FIVE_POINT"

_pointingMethodNames[_CROSS] = "CROSS"

_pointingMethodNames[_CIRCLE] = "CIRCLE"

_pointingMethodNames[_HOLOGRAPHY] = "HOLOGRAPHY"


class PointingMethod:
    """
    A class for the PointingMethod enumeration.
    """

    # The value of this PointingMethod, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, pointingMethod):
        # construct a PointingMethod from an integer, a string, or another PointingMethod
        # if pointingMethod is a string, convert it to an instance of this class using literal
        if isinstance(pointingMethod, PointingMethod):
            # copy constructor
            self._value = pointingMethod.getValue()
            self._name = pointingMethod.getName()
        elif isinstance(pointingMethod, str):
            # convert it to an instance of this class using literal
            thisEnum = PointingMethod.literal(pointingMethod)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if pointingMethod not in _pointingMethodNames:
                raise ValueError("unrecognized PointingMethod")
            self._value = pointingMethod
            self._name = _pointingMethodNames[pointingMethod]
            if self._name not in _pointingMethodDict:
                # add this PointingMethod as an attribute to this class using its name
                setattr(PointingMethod, self._name, self)
                _pointingMethodDict[self._name] = getattr(PointingMethod, self._name)

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
        the number of known enumerators in PointingMethod
        """
        return len(_pointingMethodNames)

    @staticmethod
    def name(pointingMethod):
        """
        Returns the string form of the PointingMethod
        """
        return pointingMethod.getName()

    @staticmethod
    def toString(pointingMethod):
        """
        Equivalent to the name method
        """
        return PointingMethod.name(pointingMethod)

    @staticmethod
    def names():
        """
        Return the list of all known PointingMethod enumeration names
        """
        return list(_pointingMethodNames.values())

    @staticmethod
    def newPointingMethod(name):
        """
        Equivalent to the literal method
        """
        return PointingMethod.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the PointingMethod enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(PointingMethod, name):
            raise ValueError("Unrecognized PointingMethod name")
        return PointingMethod(getattr(PointingMethod, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a PointingMethod from an integration matching an enumeration.
        """
        return PointingMethod(i)


THREE_POINT = PointingMethod(_THREE_POINT)

FOUR_POINT = PointingMethod(_FOUR_POINT)

FIVE_POINT = PointingMethod(_FIVE_POINT)

CROSS = PointingMethod(_CROSS)

CIRCLE = PointingMethod(_CIRCLE)

HOLOGRAPHY = PointingMethod(_HOLOGRAPHY)
