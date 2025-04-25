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
# File AtmPhaseCorrection.py

# to keep track of the attributes added to this class for each value of this enumeration

_atmPhaseCorrectionDict = {}

# the possible enumerations

_AP_UNCORRECTED = 0  # Data has no WVR phase correction

_AP_CORRECTED = 1  # Data phases have been corrected using WVR data


# their names in a dictionary
_atmPhaseCorrectionNames = {}

_atmPhaseCorrectionNames[_AP_UNCORRECTED] = "AP_UNCORRECTED"

_atmPhaseCorrectionNames[_AP_CORRECTED] = "AP_CORRECTED"


class AtmPhaseCorrection:
    """
    A class for the AtmPhaseCorrection enumeration.
    """

    # The value of this AtmPhaseCorrection, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, atmPhaseCorrection):
        # construct a AtmPhaseCorrection from an integer, a string, or another AtmPhaseCorrection
        # if atmPhaseCorrection is a string, convert it to an instance of this class using literal
        if isinstance(atmPhaseCorrection, AtmPhaseCorrection):
            # copy constructor
            self._value = atmPhaseCorrection.getValue()
            self._name = atmPhaseCorrection.getName()
        elif isinstance(atmPhaseCorrection, str):
            # convert it to an instance of this class using literal
            thisEnum = AtmPhaseCorrection.literal(atmPhaseCorrection)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if atmPhaseCorrection not in _atmPhaseCorrectionNames:
                raise ValueError("unrecognized AtmPhaseCorrection")
            self._value = atmPhaseCorrection
            self._name = _atmPhaseCorrectionNames[atmPhaseCorrection]
            if self._name not in _atmPhaseCorrectionDict:
                # add this AtmPhaseCorrection as an attribute to this class using its name
                setattr(AtmPhaseCorrection, self._name, self)
                _atmPhaseCorrectionDict[self._name] = getattr(
                    AtmPhaseCorrection, self._name
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
        Returns True if other is a AtmPhaseCorrection and its value is the same as this one.
        """
        return isinstance(other, AtmPhaseCorrection) and (
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
        the number of known enumerators in AtmPhaseCorrection
        """
        return len(_atmPhaseCorrectionNames)

    @staticmethod
    def name(atmPhaseCorrection):
        """
        Returns the string form of atmPhaseCorrection
        """
        return str(atmPhaseCorrection)

    @staticmethod
    def names():
        """
        Return the list of all known AtmPhaseCorrection enumeration names
        """
        return list(_atmPhaseCorrectionNames.values())

    @staticmethod
    def newAtmPhaseCorrection(name):
        """
        Equivalent to the literal method
        """
        return AtmPhaseCorrection.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the AtmPhaseCorrection enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(AtmPhaseCorrection, name):
            raise ValueError("Unrecognized AtmPhaseCorrection name")
        return AtmPhaseCorrection(getattr(AtmPhaseCorrection, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a AtmPhaseCorrection from an integration matching an enumeration.
        """
        return AtmPhaseCorrection(i)


AP_UNCORRECTED = AtmPhaseCorrection(_AP_UNCORRECTED)

AP_CORRECTED = AtmPhaseCorrection(_AP_CORRECTED)
