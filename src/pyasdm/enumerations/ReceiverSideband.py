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
# File ReceiverSideband.py

# to keep track of the attributes added to this class for each value of this enumeration

_receiverSidebandDict = {}

# the possible enumerations

_NOSB = 0  # direct output signal (no frequency conversion).

_DSB = 1  # double side band ouput.

_SSB = 2  # single side band receiver.

_TSB = 3  # receiver with dual output.


# their names in a dictionary
_receiverSidebandNames = {}

_receiverSidebandNames[_NOSB] = "NOSB"

_receiverSidebandNames[_DSB] = "DSB"

_receiverSidebandNames[_SSB] = "SSB"

_receiverSidebandNames[_TSB] = "TSB"


class ReceiverSideband:
    """
    A class for the ReceiverSideband enumeration.
    """

    # The value of this ReceiverSideband, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, receiverSideband):
        # construct a ReceiverSideband from an integer, a string, or another ReceiverSideband
        # if receiverSideband is a string, convert it to an instance of this class using literal
        if isinstance(receiverSideband, ReceiverSideband):
            # copy constructor
            self._value = receiverSideband.getValue()
            self._name = receiverSideband.getName()
        elif isinstance(receiverSideband, str):
            # convert it to an instance of this class using literal
            thisEnum = ReceiverSideband.literal(receiverSideband)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if receiverSideband not in _receiverSidebandNames:
                raise ValueError("unrecognized ReceiverSideband")
            self._value = receiverSideband
            self._name = _receiverSidebandNames[receiverSideband]
            if self._name not in _receiverSidebandDict:
                # add this ReceiverSideband as an attribute to this class using its name
                setattr(ReceiverSideband, self._name, self)
                _receiverSidebandDict[self._name] = getattr(
                    ReceiverSideband, self._name
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
        Returns True if other is a ReceiverSideband and its value is the same as this one.
        """
        return isinstance(other, ReceiverSideband) and (
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
        the number of known enumerators in ReceiverSideband
        """
        return len(_receiverSidebandNames)

    @staticmethod
    def name(receiverSideband):
        """
        Returns the string form of receiverSideband
        """
        return str(receiverSideband)

    @staticmethod
    def names():
        """
        Return the list of all known ReceiverSideband enumeration names
        """
        return list(_receiverSidebandNames.values())

    @staticmethod
    def newReceiverSideband(name):
        """
        Equivalent to the literal method
        """
        return ReceiverSideband.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the ReceiverSideband enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(ReceiverSideband, name):
            raise ValueError("Unrecognized ReceiverSideband name")
        return ReceiverSideband(getattr(ReceiverSideband, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a ReceiverSideband from an integration matching an enumeration.
        """
        return ReceiverSideband(i)


NOSB = ReceiverSideband(_NOSB)

DSB = ReceiverSideband(_DSB)

SSB = ReceiverSideband(_SSB)

TSB = ReceiverSideband(_TSB)
