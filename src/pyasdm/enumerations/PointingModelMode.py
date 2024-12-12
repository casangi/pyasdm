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
# File PointingModelMode.py

# to keep track of the attributes added to this class for each value of this enumeration

_pointingModelModeDict = {}

# the possible enumerations

_RADIO = 0  # Radio pointing model

_OPTICAL = 1  # Optical Pointing Model


# their names in a dictionary
_pointingModelModeNames = {}

_pointingModelModeNames[_RADIO] = "RADIO"

_pointingModelModeNames[_OPTICAL] = "OPTICAL"


class PointingModelMode:
    """
    A class for the PointingModelMode enumeration.
    """

    # The value of this PointingModelMode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, pointingModelMode):
        # construct a PointingModelMode from an integer, a string, or another PointingModelMode
        # if pointingModelMode is a string, convert it to an instance of this class using literal
        if isinstance(pointingModelMode, PointingModelMode):
            # copy constructor
            self._value = pointingModelMode.getValue()
            self._name = pointingModelMode.getName()
        elif isinstance(pointingModelMode, str):
            # convert it to an instance of this class using literal
            thisEnum = PointingModelMode.literal(pointingModelMode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if pointingModelMode not in _pointingModelModeNames:
                raise ValueError("unrecognized PointingModelMode")
            self._value = pointingModelMode
            self._name = _pointingModelModeNames[pointingModelMode]
            if self._name not in _pointingModelModeDict:
                # add this PointingModelMode as an attribute to this class using its name
                setattr(PointingModelMode, self._name, self)
                _pointingModelModeDict[self._name] = getattr(
                    PointingModelMode, self._name
                )

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
        the number of known enumerators in PointingModelMode
        """
        return len(_pointingModelModeNames)

    @staticmethod
    def name(pointingModelMode):
        """
        Returns the string form of the PointingModelMode
        """
        return pointingModelMode.getName()

    @staticmethod
    def toString(pointingModelMode):
        """
        Equivalent to the name method
        """
        return PointingModelMode.name(pointingModelMode)

    @staticmethod
    def names():
        """
        Return the list of all known PointingModelMode enumeration names
        """
        return list(_pointingModelModeNames.values())

    @staticmethod
    def newPointingModelMode(name):
        """
        Equivalent to the literal method
        """
        return PointingModelMode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the PointingModelMode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(PointingModelMode, name):
            raise ValueError("Unrecognized PointingModelMode name")
        return PointingModelMode(getattr(PointingModelMode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a PointingModelMode from an integration matching an enumeration.
        """
        return PointingModelMode(i)


RADIO = PointingModelMode(_RADIO)

OPTICAL = PointingModelMode(_OPTICAL)
