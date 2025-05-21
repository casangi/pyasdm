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
# File SynthProf.py

# to keep track of the attributes added to this class for each value of this enumeration

_synthProfDict = {}

# the possible enumerations

_NOSYNTH = 0  #

_ACACORR = 1  #

_ACA_CDP = 2  #


# their names in a dictionary
_synthProfNames = {}

_synthProfNames[_NOSYNTH] = "NOSYNTH"

_synthProfNames[_ACACORR] = "ACACORR"

_synthProfNames[_ACA_CDP] = "ACA_CDP"


class SynthProf:
    """
    A class for the SynthProf enumeration.
    """

    # The value of this SynthProf, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, synthProf):
        # construct a SynthProf from an integer, a string, or another SynthProf
        # if synthProf is a string, convert it to an instance of this class using literal
        if isinstance(synthProf, SynthProf):
            # copy constructor
            self._value = synthProf.getValue()
            self._name = synthProf.getName()
        elif isinstance(synthProf, str):
            # convert it to an instance of this class using literal
            thisEnum = SynthProf.literal(synthProf)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if synthProf not in _synthProfNames:
                raise ValueError("unrecognized SynthProf")
            self._value = synthProf
            self._name = _synthProfNames[synthProf]
            if self._name not in _synthProfDict:
                # add this SynthProf as an attribute to this class using its name
                setattr(SynthProf, self._name, self)
                _synthProfDict[self._name] = getattr(SynthProf, self._name)

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
        Returns True if other is a SynthProf and its value is the same as this one.
        """
        return isinstance(other, SynthProf) and (other.getValue() == self.getValue())

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
        the number of known enumerators in SynthProf
        """
        return len(_synthProfNames)

    @staticmethod
    def name(synthProf):
        """
        Returns the string form of synthProf
        """
        return str(synthProf)

    @staticmethod
    def names():
        """
        Return the list of all known SynthProf enumeration names
        """
        return list(_synthProfNames.values())

    @staticmethod
    def newSynthProf(name):
        """
        Equivalent to the literal method
        """
        return SynthProf.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the SynthProf enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(SynthProf, name):
            raise ValueError("Unrecognized SynthProf name")
        return SynthProf(getattr(SynthProf, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a SynthProf from an integration matching an enumeration.
        """
        return SynthProf(i)


NOSYNTH = SynthProf(_NOSYNTH)

ACACORR = SynthProf(_ACACORR)

ACA_CDP = SynthProf(_ACA_CDP)
