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
# File SubscanIntent.py

# to keep track of the attributes added to this class for each value of this enumeration

_subscanIntentDict = {}

# the possible enumerations

_ON_SOURCE = 0  # on-source measurement

_OFF_SOURCE = 1  # off-source measurement

_MIXED = 2  # Pointing measurement, some antennas are on -ource, some off-source

_REFERENCE = 3  # reference measurement (used for boresight in holography).

_SCANNING = 4  # antennas are scanning.

_HOT = 5  # hot load measurement.

_AMBIENT = 6  # ambient load measurement.

_SIGNAL = 7  # Signal sideband measurement.

_IMAGE = 8  # Image sideband measurement.

_TEST = 9  # reserved for development.

_UNSPECIFIED = 10  # Unspecified


# their names in a dictionary
_subscanIntentNames = {}

_subscanIntentNames[_ON_SOURCE] = "ON_SOURCE"

_subscanIntentNames[_OFF_SOURCE] = "OFF_SOURCE"

_subscanIntentNames[_MIXED] = "MIXED"

_subscanIntentNames[_REFERENCE] = "REFERENCE"

_subscanIntentNames[_SCANNING] = "SCANNING"

_subscanIntentNames[_HOT] = "HOT"

_subscanIntentNames[_AMBIENT] = "AMBIENT"

_subscanIntentNames[_SIGNAL] = "SIGNAL"

_subscanIntentNames[_IMAGE] = "IMAGE"

_subscanIntentNames[_TEST] = "TEST"

_subscanIntentNames[_UNSPECIFIED] = "UNSPECIFIED"


class SubscanIntent:
    """
    A class for the SubscanIntent enumeration.
    """

    # The value of this SubscanIntent, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, subscanIntent):
        # construct a SubscanIntent from an integer, a string, or another SubscanIntent
        # if subscanIntent is a string, convert it to an instance of this class using literal
        if isinstance(subscanIntent, SubscanIntent):
            # copy constructor
            self._value = subscanIntent.getValue()
            self._name = subscanIntent.getName()
        elif isinstance(subscanIntent, str):
            # convert it to an instance of this class using literal
            thisEnum = SubscanIntent.literal(subscanIntent)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if subscanIntent not in _subscanIntentNames:
                raise ValueError("unrecognized SubscanIntent")
            self._value = subscanIntent
            self._name = _subscanIntentNames[subscanIntent]
            if self._name not in _subscanIntentDict:
                # add this SubscanIntent as an attribute to this class using its name
                setattr(SubscanIntent, self._name, self)
                _subscanIntentDict[self._name] = getattr(SubscanIntent, self._name)

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
        the number of known enumerators in SubscanIntent
        """
        return len(_subscanIntentNames)

    @staticmethod
    def name(subscanIntent):
        """
        Returns the string form of the SubscanIntent
        """
        return subscanIntent.getName()

    @staticmethod
    def toString(subscanIntent):
        """
        Equivalent to the name method
        """
        return SubscanIntent.name(subscanIntent)

    @staticmethod
    def names():
        """
        Return the list of all known SubscanIntent enumeration names
        """
        return list(_subscanIntentNames.values())

    @staticmethod
    def newSubscanIntent(name):
        """
        Equivalent to the literal method
        """
        return SubscanIntent.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the SubscanIntent enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(SubscanIntent, name):
            raise ValueError("Unrecognized SubscanIntent name")
        return SubscanIntent(getattr(SubscanIntent, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a SubscanIntent from an integration matching an enumeration.
        """
        return SubscanIntent(i)


ON_SOURCE = SubscanIntent(_ON_SOURCE)

OFF_SOURCE = SubscanIntent(_OFF_SOURCE)

MIXED = SubscanIntent(_MIXED)

REFERENCE = SubscanIntent(_REFERENCE)

SCANNING = SubscanIntent(_SCANNING)

HOT = SubscanIntent(_HOT)

AMBIENT = SubscanIntent(_AMBIENT)

SIGNAL = SubscanIntent(_SIGNAL)

IMAGE = SubscanIntent(_IMAGE)

TEST = SubscanIntent(_TEST)

UNSPECIFIED = SubscanIntent(_UNSPECIFIED)
