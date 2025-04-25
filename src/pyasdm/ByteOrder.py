# ALMA - Atacama Large Millimeter Array
# (c) European Southern Observatory, 2024
# (c) Associated Universities Inc., 2024
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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNUn
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307  USA
#
# File ByteOrder.py

# A similar class exists in the c++ implementation in Misc.h, Misc.cpp

import sys


class ByteOrder:
    """
    "Class to hold the byte order of a binary table"
    """

    # the name of this byte order as string
    # equivalent to the pythonic name as used by sys.byteorder
    # either "little" or "big"
    _name = None
    # this is True if the _name is equivalent to the native byte order
    _is_native = None

    def __init__(self, byteOrderStr=None):
        """
        Initialize this with a named string.
        Recognized strings are 'Little_Endian', 'Big_Endian' and 'Native'.
        'Native' endian is translated into one of the two other recognized strings
        using the sys.byteorder value where 'little' is 'Little_Endian' and anything
        else is 'Big_Endian',
        The default is 'Native'.
        """
        if byteOrderStr is None:
            byteOrderStr = "Native"

        self.fromString(byteOrderStr)

    def __str__(self):
        """
        return the name as used by ASDM tables.
        returns either "Little_Endian" or "Big_Endian"
        """
        if self._name == "little":
            return "Little_Endian"
        return "Big_Endian"

    def fromString(self, byteOrderStr):
        """
        Sets this value from a string.
        Recognized strings are 'Little_Endian', 'Big_Endian' and 'Native'.
        'Native' endian sets the byte order name to be the value of sys.byteorder.
        'Little_Endian' sets the byte order name to 'little' and
        'Big_Endian' sets the byte order name to 'big'
        """

        if byteOrderStr == "Native":
            self._name = sys.byteorder
            self._is_native = True

        elif byteOrderStr == "Little_Endian":
            self._name = "little"
            self._is_native = self._name == sys.byteorder

        elif byteOrderStr == "Big_Endian":
            self._name = "big"
            self._is_native = self._name == sys.byteorder

        else:
            raise ValueError(
                "Unrecognized byteOrderStr. Must be 'Little_Endian', 'Big_Endian', or 'Native'."
            )

    def getByteOrder(self):
        """
        Returns the byte order name, which is equivalent to sys.byteorder when isNative() returns True.
        This is the string that can be used in the byteorder field of the from_bytes methods of the native python types.
        """
        return self._name

    def isNative(self):
        """
        Returns true if this ByteOrder is equvialent to the native byteorder as found in sys.byteorder.
        """
        return self._is_native

NATIVE = ByteOrder("Native")
LITTLE = ByteOrder("Little_Endian")
BIG = ByteOrder("Big_Endian")
