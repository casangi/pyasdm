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
# File CalType.py

# to keep track of the attributes added to this class for each value of this enumeration

_calTypeDict = {}

# the possible enumerations

_CAL_AMPLI = 0  #

_CAL_ATMOSPHERE = 1  #

_CAL_BANDPASS = 2  #

_CAL_CURVE = 3  #

_CAL_DELAY = 4  #

_CAL_FLUX = 5  #

_CAL_FOCUS = 6  #

_CAL_FOCUS_MODEL = 7  #

_CAL_GAIN = 8  #

_CAL_HOLOGRAPHY = 9  #

_CAL_PHASE = 10  #

_CAL_POINTING = 11  #

_CAL_POINTING_MODEL = 12  #

_CAL_POSITION = 13  #

_CAL_PRIMARY_BEAM = 14  #

_CAL_SEEING = 15  #

_CAL_WVR = 16  #

_CAL_APPPHASE = 17  # Calibration for phasing of ALMA. Applicable at ALMA.


# their names in a dictionary
_calTypeNames = {}

_calTypeNames[_CAL_AMPLI] = "CAL_AMPLI"

_calTypeNames[_CAL_ATMOSPHERE] = "CAL_ATMOSPHERE"

_calTypeNames[_CAL_BANDPASS] = "CAL_BANDPASS"

_calTypeNames[_CAL_CURVE] = "CAL_CURVE"

_calTypeNames[_CAL_DELAY] = "CAL_DELAY"

_calTypeNames[_CAL_FLUX] = "CAL_FLUX"

_calTypeNames[_CAL_FOCUS] = "CAL_FOCUS"

_calTypeNames[_CAL_FOCUS_MODEL] = "CAL_FOCUS_MODEL"

_calTypeNames[_CAL_GAIN] = "CAL_GAIN"

_calTypeNames[_CAL_HOLOGRAPHY] = "CAL_HOLOGRAPHY"

_calTypeNames[_CAL_PHASE] = "CAL_PHASE"

_calTypeNames[_CAL_POINTING] = "CAL_POINTING"

_calTypeNames[_CAL_POINTING_MODEL] = "CAL_POINTING_MODEL"

_calTypeNames[_CAL_POSITION] = "CAL_POSITION"

_calTypeNames[_CAL_PRIMARY_BEAM] = "CAL_PRIMARY_BEAM"

_calTypeNames[_CAL_SEEING] = "CAL_SEEING"

_calTypeNames[_CAL_WVR] = "CAL_WVR"

_calTypeNames[_CAL_APPPHASE] = "CAL_APPPHASE"


class CalType:
    """
    A class for the CalType enumeration.
    """

    # The value of this CalType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, calType):
        # construct a CalType from an integer, a string, or another CalType
        # if calType is a string, convert it to an instance of this class using literal
        if isinstance(calType, CalType):
            # copy constructor
            self._value = calType.getValue()
            self._name = calType.getName()
        elif isinstance(calType, str):
            # convert it to an instance of this class using literal
            thisEnum = CalType.literal(calType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if calType not in _calTypeNames:
                raise ValueError("unrecognized CalType")
            self._value = calType
            self._name = _calTypeNames[calType]
            if self._name not in _calTypeDict:
                # add this CalType as an attribute to this class using its name
                setattr(CalType, self._name, self)
                _calTypeDict[self._name] = getattr(CalType, self._name)

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
        Returns True if other is a CalType and its value is the same as this one.
        """
        return isinstance(other, CalType) and (other.getValue() == self.getValue())

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
        the number of known enumerators in CalType
        """
        return len(_calTypeNames)

    @staticmethod
    def name(calType):
        """
        Returns the string form of calType
        """
        return str(calType)

    @staticmethod
    def names():
        """
        Return the list of all known CalType enumeration names
        """
        return list(_calTypeNames.values())

    @staticmethod
    def newCalType(name):
        """
        Equivalent to the literal method
        """
        return CalType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the CalType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(CalType, name):
            raise ValueError("Unrecognized CalType name")
        return CalType(getattr(CalType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a CalType from an integration matching an enumeration.
        """
        return CalType(i)


CAL_AMPLI = CalType(_CAL_AMPLI)

CAL_ATMOSPHERE = CalType(_CAL_ATMOSPHERE)

CAL_BANDPASS = CalType(_CAL_BANDPASS)

CAL_CURVE = CalType(_CAL_CURVE)

CAL_DELAY = CalType(_CAL_DELAY)

CAL_FLUX = CalType(_CAL_FLUX)

CAL_FOCUS = CalType(_CAL_FOCUS)

CAL_FOCUS_MODEL = CalType(_CAL_FOCUS_MODEL)

CAL_GAIN = CalType(_CAL_GAIN)

CAL_HOLOGRAPHY = CalType(_CAL_HOLOGRAPHY)

CAL_PHASE = CalType(_CAL_PHASE)

CAL_POINTING = CalType(_CAL_POINTING)

CAL_POINTING_MODEL = CalType(_CAL_POINTING_MODEL)

CAL_POSITION = CalType(_CAL_POSITION)

CAL_PRIMARY_BEAM = CalType(_CAL_PRIMARY_BEAM)

CAL_SEEING = CalType(_CAL_SEEING)

CAL_WVR = CalType(_CAL_WVR)

CAL_APPPHASE = CalType(_CAL_APPPHASE)
