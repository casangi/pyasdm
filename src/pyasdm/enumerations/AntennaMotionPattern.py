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
# File AntennaMotionPattern.py

# to keep track of the attributes added to this class for each value of this enumeration

_antennaMotionPatternDict = {}

# the possible enumerations

_NONE = 0  # No pattern.

_CROSS_SCAN = 1  # Crossed scan (continuous pattern)

_SPIRAL = 2  # Spiral pattern

_CIRCLE = 3  # Circular pattern

_THREE_POINTS = 4  # Three points pattern.

_FOUR_POINTS = 5  # Four points pattern.

_FIVE_POINTS = 6  # Five points pattern.

_TEST = 7  # Reserved for development.

_UNSPECIFIED = 8  # Unspecified pattern.

_STAR = 9  #

_LISSAJOUS = 10  #


# their names in a dictionary
_antennaMotionPatternNames = {}

_antennaMotionPatternNames[_NONE] = "NONE"

_antennaMotionPatternNames[_CROSS_SCAN] = "CROSS_SCAN"

_antennaMotionPatternNames[_SPIRAL] = "SPIRAL"

_antennaMotionPatternNames[_CIRCLE] = "CIRCLE"

_antennaMotionPatternNames[_THREE_POINTS] = "THREE_POINTS"

_antennaMotionPatternNames[_FOUR_POINTS] = "FOUR_POINTS"

_antennaMotionPatternNames[_FIVE_POINTS] = "FIVE_POINTS"

_antennaMotionPatternNames[_TEST] = "TEST"

_antennaMotionPatternNames[_UNSPECIFIED] = "UNSPECIFIED"

_antennaMotionPatternNames[_STAR] = "STAR"

_antennaMotionPatternNames[_LISSAJOUS] = "LISSAJOUS"


class AntennaMotionPattern:
    """
    A class for the AntennaMotionPattern enumeration.
    """

    # The value of this AntennaMotionPattern, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, antennaMotionPattern):
        # construct a AntennaMotionPattern from an integer, a string, or another AntennaMotionPattern
        # if antennaMotionPattern is a string, convert it to an instance of this class using literal
        if isinstance(antennaMotionPattern, AntennaMotionPattern):
            # copy constructor
            self._value = antennaMotionPattern.getValue()
            self._name = antennaMotionPattern.getName()
        elif isinstance(antennaMotionPattern, str):
            # convert it to an instance of this class using literal
            thisEnum = AntennaMotionPattern.literal(antennaMotionPattern)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if antennaMotionPattern not in _antennaMotionPatternNames:
                raise ValueError("unrecognized AntennaMotionPattern")
            self._value = antennaMotionPattern
            self._name = _antennaMotionPatternNames[antennaMotionPattern]
            if self._name not in _antennaMotionPatternDict:
                # add this AntennaMotionPattern as an attribute to this class using its name
                setattr(AntennaMotionPattern, self._name, self)
                _antennaMotionPatternDict[self._name] = getattr(
                    AntennaMotionPattern, self._name
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
        Returns True if other is a AntennaMotionPattern and its value is the same as this one.
        """
        return isinstance(other, AntennaMotionPattern) and (
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
        the number of known enumerators in AntennaMotionPattern
        """
        return len(_antennaMotionPatternNames)

    @staticmethod
    def name(antennaMotionPattern):
        """
        Returns the string form of antennaMotionPattern
        """
        return str(antennaMotionPattern)

    @staticmethod
    def names():
        """
        Return the list of all known AntennaMotionPattern enumeration names
        """
        return list(_antennaMotionPatternNames.values())

    @staticmethod
    def newAntennaMotionPattern(name):
        """
        Equivalent to the literal method
        """
        return AntennaMotionPattern.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the AntennaMotionPattern enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(AntennaMotionPattern, name):
            raise ValueError("Unrecognized AntennaMotionPattern name")
        return AntennaMotionPattern(getattr(AntennaMotionPattern, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a AntennaMotionPattern from an integration matching an enumeration.
        """
        return AntennaMotionPattern(i)


NONE = AntennaMotionPattern(_NONE)

CROSS_SCAN = AntennaMotionPattern(_CROSS_SCAN)

SPIRAL = AntennaMotionPattern(_SPIRAL)

CIRCLE = AntennaMotionPattern(_CIRCLE)

THREE_POINTS = AntennaMotionPattern(_THREE_POINTS)

FOUR_POINTS = AntennaMotionPattern(_FOUR_POINTS)

FIVE_POINTS = AntennaMotionPattern(_FIVE_POINTS)

TEST = AntennaMotionPattern(_TEST)

UNSPECIFIED = AntennaMotionPattern(_UNSPECIFIED)

STAR = AntennaMotionPattern(_STAR)

LISSAJOUS = AntennaMotionPattern(_LISSAJOUS)
