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
# File FrequencyReferenceCode.py

# to keep track of the attributes added to this class for each value of this enumeration

_frequencyReferenceCodeDict = {}

# the possible enumerations

_LABREST = 0  # spectral line rest frequency.

_LSRD = 1  # dynamic local standard of rest.

_LSRK = 2  # kinematic local standard rest.

_BARY = 3  # barycentric frequency.

_REST = 4  # spectral line frequency

_GEO = 5  # geocentric frequency.

_GALACTO = 6  # galactocentric frequency.

_TOPO = 7  # topocentric frequency.


# their names in a dictionary
_frequencyReferenceCodeNames = {}

_frequencyReferenceCodeNames[_LABREST] = "LABREST"

_frequencyReferenceCodeNames[_LSRD] = "LSRD"

_frequencyReferenceCodeNames[_LSRK] = "LSRK"

_frequencyReferenceCodeNames[_BARY] = "BARY"

_frequencyReferenceCodeNames[_REST] = "REST"

_frequencyReferenceCodeNames[_GEO] = "GEO"

_frequencyReferenceCodeNames[_GALACTO] = "GALACTO"

_frequencyReferenceCodeNames[_TOPO] = "TOPO"


class FrequencyReferenceCode:
    """
    A class for the FrequencyReferenceCode enumeration.
    """

    # The value of this FrequencyReferenceCode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, frequencyReferenceCode):
        # construct a FrequencyReferenceCode from an integer, a string, or another FrequencyReferenceCode
        # if frequencyReferenceCode is a string, convert it to an instance of this class using literal
        if isinstance(frequencyReferenceCode, FrequencyReferenceCode):
            # copy constructor
            self._value = frequencyReferenceCode.getValue()
            self._name = frequencyReferenceCode.getName()
        elif isinstance(frequencyReferenceCode, str):
            # convert it to an instance of this class using literal
            thisEnum = FrequencyReferenceCode.literal(frequencyReferenceCode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if frequencyReferenceCode not in _frequencyReferenceCodeNames:
                raise ValueError("unrecognized FrequencyReferenceCode")
            self._value = frequencyReferenceCode
            self._name = _frequencyReferenceCodeNames[frequencyReferenceCode]
            if self._name not in _frequencyReferenceCodeDict:
                # add this FrequencyReferenceCode as an attribute to this class using its name
                setattr(FrequencyReferenceCode, self._name, self)
                _frequencyReferenceCodeDict[self._name] = getattr(
                    FrequencyReferenceCode, self._name
                )

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
        the number of known enumerators in FrequencyReferenceCode
        """
        return len(_frequencyReferenceCodeNames)

    @staticmethod
    def name(frequencyReferenceCode):
        """
        Returns the string form of the FrequencyReferenceCode
        """
        return frequencyReferenceCode.getName()

    @staticmethod
    def toString(frequencyReferenceCode):
        """
        Equivalent to the name method
        """
        return FrequencyReferenceCode.name(frequencyReferenceCode)

    @staticmethod
    def names():
        """
        Return the list of all known FrequencyReferenceCode enumeration names
        """
        return list(_frequencyReferenceCodeNames.values())

    @staticmethod
    def newFrequencyReferenceCode(name):
        """
        Equivalent to the literal method
        """
        return FrequencyReferenceCode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the FrequencyReferenceCode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(FrequencyReferenceCode, name):
            raise ValueError("Unrecognized FrequencyReferenceCode name")
        return FrequencyReferenceCode(getattr(FrequencyReferenceCode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a FrequencyReferenceCode from an integration matching an enumeration.
        """
        return FrequencyReferenceCode(i)


LABREST = FrequencyReferenceCode(_LABREST)

LSRD = FrequencyReferenceCode(_LSRD)

LSRK = FrequencyReferenceCode(_LSRK)

BARY = FrequencyReferenceCode(_BARY)

REST = FrequencyReferenceCode(_REST)

GEO = FrequencyReferenceCode(_GEO)

GALACTO = FrequencyReferenceCode(_GALACTO)

TOPO = FrequencyReferenceCode(_TOPO)
