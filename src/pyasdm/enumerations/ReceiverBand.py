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
# File ReceiverBand.py

# to keep track of the attributes added to this class for each value of this enumeration

_receiverBandDict = {}

# the possible enumerations

_ALMA_RB_01 = 0  # ALMA Receiver band 01

_ALMA_RB_02 = 1  # ALMA Receiver band 02

_ALMA_RB_03 = 2  # ALMA Receiver band 03

_ALMA_RB_04 = 3  # ALMA Receiver band 04

_ALMA_RB_05 = 4  # ALMA Receiver band 05

_ALMA_RB_06 = 5  # ALMA Receiver band 06

_ALMA_RB_07 = 6  # ALMA Receiver band 07

_ALMA_RB_08 = 7  # ALMA Receiver band 08

_ALMA_RB_09 = 8  # ALMA Receiver band 09

_ALMA_RB_10 = 9  # ALMA Receiver band 10

_ALMA_RB_ALL = 10  # all ALMA receiver bands.

_ALMA_HOLOGRAPHY_RECEIVER = 11  # Alma transmitter Holography receiver.

_BURE_01 = 12  # Plateau de Bure receiver band #1.

_BURE_02 = 13  # Plateau de Bure receiver band #2.

_BURE_03 = 14  # Plateau de Bure receiver band #3.

_BURE_04 = 15  # Plateau de Bure receiver band #4

_EVLA_4 = 16  #

_EVLA_P = 17  #

_EVLA_L = 18  #

_EVLA_C = 19  #

_EVLA_S = 20  #

_EVLA_X = 21  #

_EVLA_Ku = 22  #

_EVLA_K = 23  #

_EVLA_Ka = 24  #

_EVLA_Q = 25  #

_UNSPECIFIED = 26  # receiver band of unspecified origin.


# their names in a dictionary
_receiverBandNames = {}

_receiverBandNames[_ALMA_RB_01] = "ALMA_RB_01"

_receiverBandNames[_ALMA_RB_02] = "ALMA_RB_02"

_receiverBandNames[_ALMA_RB_03] = "ALMA_RB_03"

_receiverBandNames[_ALMA_RB_04] = "ALMA_RB_04"

_receiverBandNames[_ALMA_RB_05] = "ALMA_RB_05"

_receiverBandNames[_ALMA_RB_06] = "ALMA_RB_06"

_receiverBandNames[_ALMA_RB_07] = "ALMA_RB_07"

_receiverBandNames[_ALMA_RB_08] = "ALMA_RB_08"

_receiverBandNames[_ALMA_RB_09] = "ALMA_RB_09"

_receiverBandNames[_ALMA_RB_10] = "ALMA_RB_10"

_receiverBandNames[_ALMA_RB_ALL] = "ALMA_RB_ALL"

_receiverBandNames[_ALMA_HOLOGRAPHY_RECEIVER] = "ALMA_HOLOGRAPHY_RECEIVER"

_receiverBandNames[_BURE_01] = "BURE_01"

_receiverBandNames[_BURE_02] = "BURE_02"

_receiverBandNames[_BURE_03] = "BURE_03"

_receiverBandNames[_BURE_04] = "BURE_04"

_receiverBandNames[_EVLA_4] = "EVLA_4"

_receiverBandNames[_EVLA_P] = "EVLA_P"

_receiverBandNames[_EVLA_L] = "EVLA_L"

_receiverBandNames[_EVLA_C] = "EVLA_C"

_receiverBandNames[_EVLA_S] = "EVLA_S"

_receiverBandNames[_EVLA_X] = "EVLA_X"

_receiverBandNames[_EVLA_Ku] = "EVLA_Ku"

_receiverBandNames[_EVLA_K] = "EVLA_K"

_receiverBandNames[_EVLA_Ka] = "EVLA_Ka"

_receiverBandNames[_EVLA_Q] = "EVLA_Q"

_receiverBandNames[_UNSPECIFIED] = "UNSPECIFIED"


class ReceiverBand:
    """
    A class for the ReceiverBand enumeration.
    """

    # The value of this ReceiverBand, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, receiverBand):
        # construct a ReceiverBand from an integer, a string, or another ReceiverBand
        # if receiverBand is a string, convert it to an instance of this class using literal
        if isinstance(receiverBand, ReceiverBand):
            # copy constructor
            self._value = receiverBand.getValue()
            self._name = receiverBand.getName()
        elif isinstance(receiverBand, str):
            # convert it to an instance of this class using literal
            thisEnum = ReceiverBand.literal(receiverBand)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if receiverBand not in _receiverBandNames:
                raise ValueError("unrecognized ReceiverBand")
            self._value = receiverBand
            self._name = _receiverBandNames[receiverBand]
            if self._name not in _receiverBandDict:
                # add this ReceiverBand as an attribute to this class using its name
                setattr(ReceiverBand, self._name, self)
                _receiverBandDict[self._name] = getattr(ReceiverBand, self._name)

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
        Returns True if other is a ReceiverBand and its value is the same as this one.
        """
        return isinstance(other, ReceiverBand) and (other.getValue() == self.getValue())

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
        the number of known enumerators in ReceiverBand
        """
        return len(_receiverBandNames)

    @staticmethod
    def name(receiverBand):
        """
        Returns the string form of receiverBand
        """
        return str(receiverBand)

    @staticmethod
    def names():
        """
        Return the list of all known ReceiverBand enumeration names
        """
        return list(_receiverBandNames.values())

    @staticmethod
    def newReceiverBand(name):
        """
        Equivalent to the literal method
        """
        return ReceiverBand.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the ReceiverBand enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(ReceiverBand, name):
            raise ValueError("Unrecognized ReceiverBand name")
        return ReceiverBand(getattr(ReceiverBand, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a ReceiverBand from an integration matching an enumeration.
        """
        return ReceiverBand(i)


ALMA_RB_01 = ReceiverBand(_ALMA_RB_01)

ALMA_RB_02 = ReceiverBand(_ALMA_RB_02)

ALMA_RB_03 = ReceiverBand(_ALMA_RB_03)

ALMA_RB_04 = ReceiverBand(_ALMA_RB_04)

ALMA_RB_05 = ReceiverBand(_ALMA_RB_05)

ALMA_RB_06 = ReceiverBand(_ALMA_RB_06)

ALMA_RB_07 = ReceiverBand(_ALMA_RB_07)

ALMA_RB_08 = ReceiverBand(_ALMA_RB_08)

ALMA_RB_09 = ReceiverBand(_ALMA_RB_09)

ALMA_RB_10 = ReceiverBand(_ALMA_RB_10)

ALMA_RB_ALL = ReceiverBand(_ALMA_RB_ALL)

ALMA_HOLOGRAPHY_RECEIVER = ReceiverBand(_ALMA_HOLOGRAPHY_RECEIVER)

BURE_01 = ReceiverBand(_BURE_01)

BURE_02 = ReceiverBand(_BURE_02)

BURE_03 = ReceiverBand(_BURE_03)

BURE_04 = ReceiverBand(_BURE_04)

EVLA_4 = ReceiverBand(_EVLA_4)

EVLA_P = ReceiverBand(_EVLA_P)

EVLA_L = ReceiverBand(_EVLA_L)

EVLA_C = ReceiverBand(_EVLA_C)

EVLA_S = ReceiverBand(_EVLA_S)

EVLA_X = ReceiverBand(_EVLA_X)

EVLA_Ku = ReceiverBand(_EVLA_Ku)

EVLA_K = ReceiverBand(_EVLA_K)

EVLA_Ka = ReceiverBand(_EVLA_Ka)

EVLA_Q = ReceiverBand(_EVLA_Q)

UNSPECIFIED = ReceiverBand(_UNSPECIFIED)
