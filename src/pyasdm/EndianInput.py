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
# File EndianInput.py

# Modelled on the EndianISStream c++ class and a similar Java class

from .ByteOrder import ByteOrder

import io
import struct
import sys


class EndianInput:
    """
    This class handles the conversion of a byte stream as opened
    from a file in 'rb' mode to values needed by the pyasdm objects.

    The class is intialized with an io.BufferedReader instance.
    This classes expects that seek works with that object.
    """

    # the io.BufferedReader being read
    _byteStream = None

    # the specified byte order as a ByteOrder instance
    _byteOrder = None

    def __init__(self, byteStream, byteOrder=None):
        """
        Initialize this class using the given bytestream, which must be
        an io.BufferedReader instance.

        The byteOrder defaults to the native order. When
        provided, byteOrder is a ByteOrder instance.
        """

        if not isinstance(byteStream, io.BufferedReader) and byteStream.seekable():
            raise ValueError("byteStream must be a seekable io.BufferedReader instance")

        if byteOrder is None:
            # default to the local byte order
            byteOrder = ByteOrder()

        if not isinstance(byteOrder, ByteOrder):
            raise ValueError("byteOrder must be a ByteOrder instance when provided")

        self._byteStream = byteStream
        self._byteOrder = byteOrder

    def byteOrder(self):
        """
        Return the ByteOrder instance used by this EndianInput.
        """
        return self._byteOrder

    def seek(self, offset):
        """
        Seek to some location in the stream being read. This always
        seeks relative to the start of the stream.

        Returns the new position (which should equal offset).
        """
        return self._byteStream.seek(offset)

    def close(self):
        """
        Close the byte stream being read.
        """
        self._byteStream.close()

    def tell(self):
        """
        Report the location of the byte stream.
        """
        return self._byteStream.tell()

    def closed(self):
        """
        Returns True if the byte stream is closed.
        """
        return self._byteStream.closed

    def readBool(self):
        """
        Return a bool using 1 byte in the byte list.
        """
        return bool.from_bytes(self._byteStream.read(1), self._byteOrder.getByteOrder())

    def readByte(self):
        """
        Return the byte at the current location
        """
        return self._byteStream.read(1)

    def readShort(self):
        """
        Return the signed 2-byte integer at the current location as a python int.
        """
        return int.from_bytes(
            self._byteStream.read(2), self._byteOrder.getByteOrder(), signed=True
        )

    def readUShort(self):
        """
        Return the unsigned short integer at the current location as a python int.
        """
        return int.from_bytes(
            self._byteStream.read(2), self.byteOrder.getByteOrder(), signed=False
        )

    def readInt(self):
        """
        Return the signed 4-byte integer at the current location as a python int.
        """
        return int.from_bytes(
            self._byteStream.read(4), self._byteOrder.getByteOrder(), signed=True
        )

    def readUInt(self):
        """
        Return the unsigned 4-byte integer at the current location as a python int.
        """
        return int.from_bytes(
            self._bytesStream.read(4), self._byteOrder.getByteOrder(), signed=False
        )

    def readLongLong(self):
        """
        Return the signed 8-byte integer at the current location as a python int.
        """
        return int.from_bytes(
            self._byteStream.read(8), self._byteOrder.getByteOrder(), signed=True
        )

    def readLong(self):
        """
        Equivalent to readLongLong
        """
        return self.readLongLong()

    def readULongLong(self):
        """
        Return the unsigned 8-byte integer at the current location as a python int.
        """
        return int.from_bytes(
            self._byteStream.read(8), self._byteOrder.getByteOrder(), signed=False
        )

    def readFloat(self):
        """
        Return the 4-byte float at the current location as a float.
        """
        if self._byteOrder.isNative():
            # can just unpack it as is
            return struct.unpack("f", self._byteStream.read(4))[0]
        else:
            # need to swap first, easiest through an int
            intVal = int.from_bytes(
                self._byteStream.read(4), self._byteOrder.getByteOrder()
            )
            # and unpack it into a float, in the native byte order
            return struct.unpack("f", intVal.to_bytes(4, sys.byteorder))[0]

    def readDouble(self):
        """
        Return the 8-byte float at the current location as a float.
        """
        if self._byteOrder.isNative():
            # can just unpack it as is
            return struct.unpack("d", self._byteStream.read(8))[0]
        else:
            # need to swap first, easiest through an int
            intVal = int.from_bytes(
                self._byteStream.read(8), self._byteOrder.getByteOrder()
            )
            # and unpack it into a double, in the native byte order
            return struct.unpack("d", intVal.to_bytes(8, sys.byteorder))[0]

    def readString(self):
        """
        Return the string at the start of the current location.

        String are encoded as a 4-byte int specifying the number of characters
        followed by those characters.
        """
        strLen = self.readInt()
        return str(self._byteStream.read(strLen).decode())

    def readStr(self):
        """
        Identical to readString. Used because the type of the string value in
        python is "str" and the template generator needs to use that type for
        various reasons in various palces and proving this here makes the
        tempalte code simpler.
        """
        return self.readString()
