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
# File CorrelatorCalibration.py

# to keep track of the attributes added to this class for each value of this enumeration

_correlatorCalibrationDict = {}

# the possible enumerations

_NONE = 0  # No internal correlator calibration

_CORRELATOR_CALIBRATION = 1  # Internal correlator calibration.

_REAL_OBSERVATION = 2  # A 'real' observation.


# their names in a dictionary
_correlatorCalibrationNames = {}

_correlatorCalibrationNames[_NONE] = "NONE"

_correlatorCalibrationNames[_CORRELATOR_CALIBRATION] = "CORRELATOR_CALIBRATION"

_correlatorCalibrationNames[_REAL_OBSERVATION] = "REAL_OBSERVATION"


class CorrelatorCalibration:
    """
    A class for the CorrelatorCalibration enumeration.
    """

    # The value of this CorrelatorCalibration, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, correlatorCalibration):
        # construct a CorrelatorCalibration from an integer, a string, or another CorrelatorCalibration
        # if correlatorCalibration is a string, convert it to an instance of this class using literal
        if isinstance(correlatorCalibration, CorrelatorCalibration):
            # copy constructor
            self._value = correlatorCalibration.getValue()
            self._name = correlatorCalibration.getName()
        elif isinstance(correlatorCalibration, str):
            # convert it to an instance of this class using literal
            thisEnum = CorrelatorCalibration.literal(correlatorCalibration)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if correlatorCalibration not in _correlatorCalibrationNames:
                raise ValueError("unrecognized CorrelatorCalibration")
            self._value = correlatorCalibration
            self._name = _correlatorCalibrationNames[correlatorCalibration]
            if self._name not in _correlatorCalibrationDict:
                # add this CorrelatorCalibration as an attribute to this class using its name
                setattr(CorrelatorCalibration, self._name, self)
                _correlatorCalibrationDict[self._name] = getattr(
                    CorrelatorCalibration, self._name
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
        Returns True if other is a CorrelatorCalibration and its value is the same as this one.
        """
        return isinstance(other, CorrelatorCalibration) and (
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
        the number of known enumerators in CorrelatorCalibration
        """
        return len(_correlatorCalibrationNames)

    @staticmethod
    def name(correlatorCalibration):
        """
        Returns the string form of correlatorCalibration
        """
        return str(correlatorCalibration)

    @staticmethod
    def names():
        """
        Return the list of all known CorrelatorCalibration enumeration names
        """
        return list(_correlatorCalibrationNames.values())

    @staticmethod
    def newCorrelatorCalibration(name):
        """
        Equivalent to the literal method
        """
        return CorrelatorCalibration.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the CorrelatorCalibration enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(CorrelatorCalibration, name):
            raise ValueError("Unrecognized CorrelatorCalibration name")
        return CorrelatorCalibration(getattr(CorrelatorCalibration, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a CorrelatorCalibration from an integration matching an enumeration.
        """
        return CorrelatorCalibration(i)


NONE = CorrelatorCalibration(_NONE)

CORRELATOR_CALIBRATION = CorrelatorCalibration(_CORRELATOR_CALIBRATION)

REAL_OBSERVATION = CorrelatorCalibration(_REAL_OBSERVATION)
