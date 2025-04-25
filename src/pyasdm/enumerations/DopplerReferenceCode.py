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
# File DopplerReferenceCode.py

# to keep track of the attributes added to this class for each value of this enumeration

_dopplerReferenceCodeDict = {}

# the possible enumerations

_RADIO = 0  # radio definition : \f$ 1 - F \f$

_Z = 1  # redshift : \f$ - 1 + 1 / F \f$

_RATIO = 2  # frequency ratio : \f$ F \f$

_BETA = 3  # relativistic : \f$(1 - F^2) / (1 + F^2) \f$

_GAMMA = 4  # \f$(1 + F^2)/(2*F)\f$

_OPTICAL = 5  # \f$Z\f$Z

_RELATIVISTIC = 6  # idem BETA


# their names in a dictionary
_dopplerReferenceCodeNames = {}

_dopplerReferenceCodeNames[_RADIO] = "RADIO"

_dopplerReferenceCodeNames[_Z] = "Z"

_dopplerReferenceCodeNames[_RATIO] = "RATIO"

_dopplerReferenceCodeNames[_BETA] = "BETA"

_dopplerReferenceCodeNames[_GAMMA] = "GAMMA"

_dopplerReferenceCodeNames[_OPTICAL] = "OPTICAL"

_dopplerReferenceCodeNames[_RELATIVISTIC] = "RELATIVISTIC"


class DopplerReferenceCode:
    """
    A class for the DopplerReferenceCode enumeration.
    """

    # The value of this DopplerReferenceCode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, dopplerReferenceCode):
        # construct a DopplerReferenceCode from an integer, a string, or another DopplerReferenceCode
        # if dopplerReferenceCode is a string, convert it to an instance of this class using literal
        if isinstance(dopplerReferenceCode, DopplerReferenceCode):
            # copy constructor
            self._value = dopplerReferenceCode.getValue()
            self._name = dopplerReferenceCode.getName()
        elif isinstance(dopplerReferenceCode, str):
            # convert it to an instance of this class using literal
            thisEnum = DopplerReferenceCode.literal(dopplerReferenceCode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if dopplerReferenceCode not in _dopplerReferenceCodeNames:
                raise ValueError("unrecognized DopplerReferenceCode")
            self._value = dopplerReferenceCode
            self._name = _dopplerReferenceCodeNames[dopplerReferenceCode]
            if self._name not in _dopplerReferenceCodeDict:
                # add this DopplerReferenceCode as an attribute to this class using its name
                setattr(DopplerReferenceCode, self._name, self)
                _dopplerReferenceCodeDict[self._name] = getattr(
                    DopplerReferenceCode, self._name
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
        Returns True if other is a DopplerReferenceCode and its value is the same as this one.
        """
        return isinstance(other, DopplerReferenceCode) and (
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
        the number of known enumerators in DopplerReferenceCode
        """
        return len(_dopplerReferenceCodeNames)

    @staticmethod
    def name(dopplerReferenceCode):
        """
        Returns the string form of dopplerReferenceCode
        """
        return str(dopplerReferenceCode)

    @staticmethod
    def names():
        """
        Return the list of all known DopplerReferenceCode enumeration names
        """
        return list(_dopplerReferenceCodeNames.values())

    @staticmethod
    def newDopplerReferenceCode(name):
        """
        Equivalent to the literal method
        """
        return DopplerReferenceCode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the DopplerReferenceCode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(DopplerReferenceCode, name):
            raise ValueError("Unrecognized DopplerReferenceCode name")
        return DopplerReferenceCode(getattr(DopplerReferenceCode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a DopplerReferenceCode from an integration matching an enumeration.
        """
        return DopplerReferenceCode(i)


RADIO = DopplerReferenceCode(_RADIO)

Z = DopplerReferenceCode(_Z)

RATIO = DopplerReferenceCode(_RATIO)

BETA = DopplerReferenceCode(_BETA)

GAMMA = DopplerReferenceCode(_GAMMA)

OPTICAL = DopplerReferenceCode(_OPTICAL)

RELATIVISTIC = DopplerReferenceCode(_RELATIVISTIC)
