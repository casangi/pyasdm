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
# File DopplerTrackingMode.py

# to keep track of the attributes added to this class for each value of this enumeration

_dopplerTrackingModeDict = {}

# the possible enumerations

_NONE = 0  # No Doppler tracking.

_CONTINUOUS = 1  # Continuous (every integration) Doppler tracking.

_SCAN_BASED = 2  # Doppler tracking only at scan boundaries.  This means we update  the observing frequency to the correct value, but only at scan boundaries.

_SB_BASED = 3  # Doppler tracking only at the beginning of the Scheduling Block.  We set the frequency at the beginning of the observation but leave it fixed thereafter.  For the EVLA this is referred to as  'Doppler setting'.


# their names in a dictionary
_dopplerTrackingModeNames = {}

_dopplerTrackingModeNames[_NONE] = "NONE"

_dopplerTrackingModeNames[_CONTINUOUS] = "CONTINUOUS"

_dopplerTrackingModeNames[_SCAN_BASED] = "SCAN_BASED"

_dopplerTrackingModeNames[_SB_BASED] = "SB_BASED"


class DopplerTrackingMode:
    """
    A class for the DopplerTrackingMode enumeration.
    """

    # The value of this DopplerTrackingMode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, dopplerTrackingMode):
        # construct a DopplerTrackingMode from an integer, a string, or another DopplerTrackingMode
        # if dopplerTrackingMode is a string, convert it to an instance of this class using literal
        if isinstance(dopplerTrackingMode, DopplerTrackingMode):
            # copy constructor
            self._value = dopplerTrackingMode.getValue()
            self._name = dopplerTrackingMode.getName()
        elif isinstance(dopplerTrackingMode, str):
            # convert it to an instance of this class using literal
            thisEnum = DopplerTrackingMode.literal(dopplerTrackingMode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if dopplerTrackingMode not in _dopplerTrackingModeNames:
                raise ValueError("unrecognized DopplerTrackingMode")
            self._value = dopplerTrackingMode
            self._name = _dopplerTrackingModeNames[dopplerTrackingMode]
            if self._name not in _dopplerTrackingModeDict:
                # add this DopplerTrackingMode as an attribute to this class using its name
                setattr(DopplerTrackingMode, self._name, self)
                _dopplerTrackingModeDict[self._name] = getattr(
                    DopplerTrackingMode, self._name
                )

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
        Returns True if other is a DopplerTrackingMode and its value is the same as this one.
        """
        return isinstance(other, DopplerTrackingMode) and (
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
        the number of known enumerators in DopplerTrackingMode
        """
        return len(_dopplerTrackingModeNames)

    @staticmethod
    def name(dopplerTrackingMode):
        """
        Returns the string form of dopplerTrackingMode
        """
        return str(dopplerTrackingMode)

    @staticmethod
    def names():
        """
        Return the list of all known DopplerTrackingMode enumeration names
        """
        return list(_dopplerTrackingModeNames.values())

    @staticmethod
    def newDopplerTrackingMode(name):
        """
        Equivalent to the literal method
        """
        return DopplerTrackingMode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the DopplerTrackingMode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(DopplerTrackingMode, name):
            raise ValueError("Unrecognized DopplerTrackingMode name")
        return DopplerTrackingMode(getattr(DopplerTrackingMode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a DopplerTrackingMode from an integration matching an enumeration.
        """
        return DopplerTrackingMode(i)


NONE = DopplerTrackingMode(_NONE)

CONTINUOUS = DopplerTrackingMode(_CONTINUOUS)

SCAN_BASED = DopplerTrackingMode(_SCAN_BASED)

SB_BASED = DopplerTrackingMode(_SB_BASED)
