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
# File PrimaryBeamDescription.py

# to keep track of the attributes added to this class for each value of this enumeration

_primaryBeamDescriptionDict = {}

# the possible enumerations

_COMPLEX_FIELD_PATTERN = (
    0  # Electric Field Pattern image at infinite distance from antenna.
)

_APERTURE_FIELD_DISTRIBUTION = 1  # Electric Field aperture distribution.


# their names in a dictionary
_primaryBeamDescriptionNames = {}

_primaryBeamDescriptionNames[_COMPLEX_FIELD_PATTERN] = "COMPLEX_FIELD_PATTERN"

_primaryBeamDescriptionNames[_APERTURE_FIELD_DISTRIBUTION] = (
    "APERTURE_FIELD_DISTRIBUTION"
)


class PrimaryBeamDescription:
    """
    A class for the PrimaryBeamDescription enumeration.
    """

    # The value of this PrimaryBeamDescription, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, primaryBeamDescription):
        # construct a PrimaryBeamDescription from an integer, a string, or another PrimaryBeamDescription
        # if primaryBeamDescription is a string, convert it to an instance of this class using literal
        if isinstance(primaryBeamDescription, PrimaryBeamDescription):
            # copy constructor
            self._value = primaryBeamDescription.getValue()
            self._name = primaryBeamDescription.getName()
        elif isinstance(primaryBeamDescription, str):
            # convert it to an instance of this class using literal
            thisEnum = PrimaryBeamDescription.literal(primaryBeamDescription)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if primaryBeamDescription not in _primaryBeamDescriptionNames:
                raise ValueError("unrecognized PrimaryBeamDescription")
            self._value = primaryBeamDescription
            self._name = _primaryBeamDescriptionNames[primaryBeamDescription]
            if self._name not in _primaryBeamDescriptionDict:
                # add this PrimaryBeamDescription as an attribute to this class using its name
                setattr(PrimaryBeamDescription, self._name, self)
                _primaryBeamDescriptionDict[self._name] = getattr(
                    PrimaryBeamDescription, self._name
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
        Returns True if other is a PrimaryBeamDescription and its value is the same as this one.
        """
        return isinstance(other, PrimaryBeamDescription) and (
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
        the number of known enumerators in PrimaryBeamDescription
        """
        return len(_primaryBeamDescriptionNames)

    @staticmethod
    def name(primaryBeamDescription):
        """
        Returns the string form of primaryBeamDescription
        """
        return str(primaryBeamDescription)

    @staticmethod
    def names():
        """
        Return the list of all known PrimaryBeamDescription enumeration names
        """
        return list(_primaryBeamDescriptionNames.values())

    @staticmethod
    def newPrimaryBeamDescription(name):
        """
        Equivalent to the literal method
        """
        return PrimaryBeamDescription.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the PrimaryBeamDescription enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(PrimaryBeamDescription, name):
            raise ValueError("Unrecognized PrimaryBeamDescription name")
        return PrimaryBeamDescription(getattr(PrimaryBeamDescription, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a PrimaryBeamDescription from an integration matching an enumeration.
        """
        return PrimaryBeamDescription(i)


COMPLEX_FIELD_PATTERN = PrimaryBeamDescription(_COMPLEX_FIELD_PATTERN)

APERTURE_FIELD_DISTRIBUTION = PrimaryBeamDescription(_APERTURE_FIELD_DISTRIBUTION)
