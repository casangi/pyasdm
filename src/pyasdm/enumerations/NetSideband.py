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
# File NetSideband.py

# to keep track of the attributes added to this class for each value of this enumeration

_netSidebandDict = {}

# the possible enumerations

_NOSB = 0  # No side band (no frequency conversion)

_LSB = 1  # Lower side band

_USB = 2  # Upper side band

_DSB = 3  # Double side band


# their names in a dictionary
_netSidebandNames = {}

_netSidebandNames[_NOSB] = "NOSB"

_netSidebandNames[_LSB] = "LSB"

_netSidebandNames[_USB] = "USB"

_netSidebandNames[_DSB] = "DSB"


class NetSideband:
    """
    A class for the NetSideband enumeration.
    """

    # The value of this NetSideband, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, netSideband):
        # construct a NetSideband from an integer, a string, or another NetSideband
        # if netSideband is a string, convert it to an instance of this class using literal
        if isinstance(netSideband, NetSideband):
            # copy constructor
            self._value = netSideband.getValue()
            self._name = netSideband.getName()
        elif isinstance(netSideband, str):
            # convert it to an instance of this class using literal
            thisEnum = NetSideband.literal(netSideband)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if netSideband not in _netSidebandNames:
                raise ValueError("unrecognized NetSideband")
            self._value = netSideband
            self._name = _netSidebandNames[netSideband]
            if self._name not in _netSidebandDict:
                # add this NetSideband as an attribute to this class using its name
                setattr(NetSideband, self._name, self)
                _netSidebandDict[self._name] = getattr(NetSideband, self._name)

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
        the number of known enumerators in NetSideband
        """
        return len(_netSidebandNames)

    @staticmethod
    def name(netSideband):
        """
        Returns the string form of the NetSideband
        """
        return netSideband.getName()

    @staticmethod
    def toString(netSideband):
        """
        Equivalent to the name method
        """
        return NetSideband.name(netSideband)

    @staticmethod
    def names():
        """
        Return the list of all known NetSideband enumeration names
        """
        return list(_netSidebandNames.values())

    @staticmethod
    def newNetSideband(name):
        """
        Equivalent to the literal method
        """
        return NetSideband.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the NetSideband enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(NetSideband, name):
            raise ValueError("Unrecognized NetSideband name")
        return NetSideband(getattr(NetSideband, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a NetSideband from an integration matching an enumeration.
        """
        return NetSideband(i)


NOSB = NetSideband(_NOSB)

LSB = NetSideband(_LSB)

USB = NetSideband(_USB)

DSB = NetSideband(_DSB)
