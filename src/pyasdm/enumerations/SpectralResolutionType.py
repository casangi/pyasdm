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
# File SpectralResolutionType.py

# to keep track of the attributes added to this class for each value of this enumeration

_spectralResolutionTypeDict = {}

# the possible enumerations

_CHANNEL_AVERAGE = 0  #

_BASEBAND_WIDE = 1  #

_FULL_RESOLUTION = 2  #


# their names in a dictionary
_spectralResolutionTypeNames = {}

_spectralResolutionTypeNames[_CHANNEL_AVERAGE] = "CHANNEL_AVERAGE"

_spectralResolutionTypeNames[_BASEBAND_WIDE] = "BASEBAND_WIDE"

_spectralResolutionTypeNames[_FULL_RESOLUTION] = "FULL_RESOLUTION"


class SpectralResolutionType:
    """
    A class for the SpectralResolutionType enumeration.
    """

    # The value of this SpectralResolutionType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, spectralResolutionType):
        # construct a SpectralResolutionType from an integer, a string, or another SpectralResolutionType
        # if spectralResolutionType is a string, convert it to an instance of this class using literal
        if isinstance(spectralResolutionType, SpectralResolutionType):
            # copy constructor
            self._value = spectralResolutionType.getValue()
            self._name = spectralResolutionType.getName()
        elif isinstance(spectralResolutionType, str):
            # convert it to an instance of this class using literal
            thisEnum = SpectralResolutionType.literal(spectralResolutionType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if spectralResolutionType not in _spectralResolutionTypeNames:
                raise ValueError("unrecognized SpectralResolutionType")
            self._value = spectralResolutionType
            self._name = _spectralResolutionTypeNames[spectralResolutionType]
            if self._name not in _spectralResolutionTypeDict:
                # add this SpectralResolutionType as an attribute to this class using its name
                setattr(SpectralResolutionType, self._name, self)
                _spectralResolutionTypeDict[self._name] = getattr(
                    SpectralResolutionType, self._name
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
        Returns True if other is a SpectralResolutionType and its value is the same as this one.
        """
        return isinstance(other, SpectralResolutionType) and (
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
        the number of known enumerators in SpectralResolutionType
        """
        return len(_spectralResolutionTypeNames)

    @staticmethod
    def name(spectralResolutionType):
        """
        Returns the string form of spectralResolutionType
        """
        return str(spectralResolutionType)

    @staticmethod
    def names():
        """
        Return the list of all known SpectralResolutionType enumeration names
        """
        return list(_spectralResolutionTypeNames.values())

    @staticmethod
    def newSpectralResolutionType(name):
        """
        Equivalent to the literal method
        """
        return SpectralResolutionType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the SpectralResolutionType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(SpectralResolutionType, name):
            raise ValueError("Unrecognized SpectralResolutionType name")
        return SpectralResolutionType(getattr(SpectralResolutionType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a SpectralResolutionType from an integration matching an enumeration.
        """
        return SpectralResolutionType(i)


CHANNEL_AVERAGE = SpectralResolutionType(_CHANNEL_AVERAGE)

BASEBAND_WIDE = SpectralResolutionType(_BASEBAND_WIDE)

FULL_RESOLUTION = SpectralResolutionType(_FULL_RESOLUTION)
