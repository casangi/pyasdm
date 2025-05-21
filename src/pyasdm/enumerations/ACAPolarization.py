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
# File ACAPolarization.py

# to keep track of the attributes added to this class for each value of this enumeration

_aCAPolarizationDict = {}

# the possible enumerations

_ACA_STANDARD = (
    0  # Data product is the standard way (it is a standard observed Stokes parameter)
)

_ACA_XX_YY_SUM = 1  # ACA has calculated I by averaging XX and YY

_ACA_XX_50 = 2  # ACA has averaged XX and XX delayed by half a FFT period

_ACA_YY_50 = 3  # ACA has averaged YY and YY delayed by half a FFT period


# their names in a dictionary
_aCAPolarizationNames = {}

_aCAPolarizationNames[_ACA_STANDARD] = "ACA_STANDARD"

_aCAPolarizationNames[_ACA_XX_YY_SUM] = "ACA_XX_YY_SUM"

_aCAPolarizationNames[_ACA_XX_50] = "ACA_XX_50"

_aCAPolarizationNames[_ACA_YY_50] = "ACA_YY_50"


class ACAPolarization:
    """
    A class for the ACAPolarization enumeration.
    """

    # The value of this ACAPolarization, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, aCAPolarization):
        # construct a ACAPolarization from an integer, a string, or another ACAPolarization
        # if aCAPolarization is a string, convert it to an instance of this class using literal
        if isinstance(aCAPolarization, ACAPolarization):
            # copy constructor
            self._value = aCAPolarization.getValue()
            self._name = aCAPolarization.getName()
        elif isinstance(aCAPolarization, str):
            # convert it to an instance of this class using literal
            thisEnum = ACAPolarization.literal(aCAPolarization)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if aCAPolarization not in _aCAPolarizationNames:
                raise ValueError("unrecognized ACAPolarization")
            self._value = aCAPolarization
            self._name = _aCAPolarizationNames[aCAPolarization]
            if self._name not in _aCAPolarizationDict:
                # add this ACAPolarization as an attribute to this class using its name
                setattr(ACAPolarization, self._name, self)
                _aCAPolarizationDict[self._name] = getattr(ACAPolarization, self._name)

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
        Returns True if other is a ACAPolarization and its value is the same as this one.
        """
        return isinstance(other, ACAPolarization) and (
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
        the number of known enumerators in ACAPolarization
        """
        return len(_aCAPolarizationNames)

    @staticmethod
    def name(aCAPolarization):
        """
        Returns the string form of aCAPolarization
        """
        return str(aCAPolarization)

    @staticmethod
    def names():
        """
        Return the list of all known ACAPolarization enumeration names
        """
        return list(_aCAPolarizationNames.values())

    @staticmethod
    def newACAPolarization(name):
        """
        Equivalent to the literal method
        """
        return ACAPolarization.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the ACAPolarization enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(ACAPolarization, name):
            raise ValueError("Unrecognized ACAPolarization name")
        return ACAPolarization(getattr(ACAPolarization, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a ACAPolarization from an integration matching an enumeration.
        """
        return ACAPolarization(i)


ACA_STANDARD = ACAPolarization(_ACA_STANDARD)

ACA_XX_YY_SUM = ACAPolarization(_ACA_XX_YY_SUM)

ACA_XX_50 = ACAPolarization(_ACA_XX_50)

ACA_YY_50 = ACAPolarization(_ACA_YY_50)
