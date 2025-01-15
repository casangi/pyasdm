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

# Modelled on the EndianOSStream c++ class and a similar Java class

from .ByteOrder import ByteOrder

import io
import struct
import sys


class EndianOutput:
    """
    This class handles the conversion of values used by pyasdm
    objects into a buffered byte stream output previous opened.
    """

    # the buffered output being read
    _outStream = None

    # the specified byte order as a ByteOrder instance
    _byteOrder = None

    def __init__(self, outStream, byteOrder=None):
        """
        Initialize this class using the given output stream, which
        be an instance of io.BufferedWriter that was opened
        as 'open(<filepath>,"wb")' or something equivalent.

        If byteOrder is not given then the native byte order
        as found in sys.byteorder is used. When provided the
        """

        if not isinstance(outStream, io.BufferedWriter):
            raise ValueError("outStream must be an io.BufferedWriter instance")

        if byteOrder is None:
            # default to the local byte order
            byteOrder = ByteOrder()

        if not isinstance(byteOrder, ByteOrder):
            raise ValueError("byteOrder must be a ByteOrder instance when provided")

        self._outStream = outStream
        self._byteOrder = byteOrder

    def byteOrder(self):
        """
        Return the ByteOrder instance used by this EndianOutput.
        """
        return self.byteOrder

    def close(self):
        """
        Close the output stream being written to.
        """
        self._outStream.close()

    def closed(self):
        """
        Returns True if the output stream is closed.
        """
        return self._outStream.closed

    def writeBool(self, boolVal):
        """
        Write a a bool value as 1 byte to the output stream.
        """
        if not isinstance(boolVal, bool):
            raise ValueError("boolVal must be a bool instance")

        self._outStream.write(boolVal.to_bytes(1, self._byteOrder.getByteOrder()))

    def writeByte(self, byteVal):
        """
        Writes a bytes value to the output stream.
        If byteVal is an integer this assumes it can be represented as a single
        byte and it converts it to that representation.
        Any other type fir byteVal is an error
        """
        try:
            if isinstance(byteVal, int):
                byteVal = byteVal.to_bytes(1, self._byteOrder.getByteOrder())
        except OverflowError as exc:
            raise ValueError("is too large to convert to a single byte") from None

        if not isinstance(byteValue, bytes):
            raise ValueError(
                "byteVal must be a bytes instance of an int that can be converted to a bytes as a single byte"
            )

        self._outStream.write(byteVal)

    def writeShort(self, shortVal):
        """
        Write an integer to the output stream as a 2-element bytes instance
        """
        if not isinstance(shortVal, int):
            raise ValueError("shortVal must be an int instance")

        try:
            self._outStream.write(
                shortVal.to_bytes(2, self._byteOrder.getByteOrder(), signed=True)
            )
        except OverflowError as exc:
            raise ValueError(
                "shortVal is too large to convert to 2 bytes representing a short integer"
            ) from None

    def writeUShort(self, uShortVal):
        """
        Write an integer to the otuput stream as a 2-element bytes
        instance representing an unsigned integer.
        """
        if not isinstance(shortVal, int) or shortVal < 0:
            raise ValueError("shortVal must a postitive integer")

        try:
            self._outStream.write(
                uShortVal.to_bytes(2, self._byteOrder.getByteOrder(), signed=False)
            )
        except OverflowError as exc:
            raise ValueError(
                "uShhortVal is too large to convert to 2 bytes representing an unsigned short integer"
            ) from None

    def writeInt(self, intVal):
        """
        Write an integer to the output stream as a bytes instance,
        representing a 4-byte integer.
        """
        if not isinstance(intVal, int):
            raise ValueError("intVal must be an integer")

        try:
            self._outStream.write(
                intVal.to_bytes(4, self._byteOrder.getByteOrder(), signed=True)
            )
        except OverflowError as exc:
            raise ValueError(
                "intVal is too large to convert to 4 bytes representing an integer"
            ) from None

    def writeUInt(self, intVal):
        """
        Write an integer to the output stream as a bytes instance,
        representing an unsigned 4-byte integer.
        """
        if not isinstance(intVal, int) or intVal < 0:
            raise ValueError("intVal must be a positive integer")

        try:
            self._outStream.write(
                intVal.to_bytes(4, self._byteOrder.getByteOrder(), signed=False)
            )
        except OverflowError as exc:
            raise ValueError(
                "intVal is too large to convert to 4 bytes representing an unsigned integer"
            ) from None

    def writeLong(self, intVal):
        """
        Write an integer to the output stream as a bytes instance,
        representing an 8-byte integer.
        """
        if not isinstance(intVal, int):
            raise ValueError("intVal must be an integer")

        try:
            self._outStream.write(
                intVal.to_bytes(8, self._byteOrder.getByteOrder(), signed=True)
            )
        except OverflowError as exc:
            raise ValueError(
                "intVal is too large to convert to 8 bytes representing an integer"
            ) from None

    def writeULong(self, intVal):
        """
        Write an integer to the output stream as a bytes instance,
        representing an 8-byte unsigned integer.
        """
        if not isinstance(intVal, int) or intVal < 0:
            raise ValueError("intVal must be a positive integer")

        try:
            self._outStream.write(
                intVal.to_bytes(8, self._byteOrder.getByteOrder(), signed=False)
            )
        except OverflowError as exc:
            raise ValueError(
                "intVal is too large to convert to 8 bytes representing an unsigned integer"
            ) from None

    def writeFloat(self, floatVal):
        """
        Write a float value to the output stream as a 4-byte float
        """
        if not isinstance(floatVal, float):
            raise ValueError("floatVal must a float")

        # convert it to bytes in the native byte order using the "f" format
        asBytes = struct.pack("f", floatVal)

        # flip the byte order if the output byte order is not the native order
        if not self._byteOrder.isNative():
            asBytes = asBytes[::-1]

        self._outStream.write(asBytes)

    def writeDouble(self, dblVal):
        """
        Write a float value to the output stream as a 8-byte float
        """
        if not isinstance(dblVal, float):
            raise ValueError("dblVal must a float")

        # convert it to bytes in the native byte order using the "d" format
        asBytes = struct.pack("d", dblVal)

        # flip the byte order if the output byte order is not the native order
        if not self._byteOrder.isNative():
            asBytes = asBytes[::-1]

        self._outStream.write(asBytes)

    def writeString(self, strVal):
        """
        Write a string to the output stream as first a 4-byte integer
        representing the length of strVal followed by the bytes that make up
        strVal.
        """
        if not isinstance(strVal, str):
            raise ValueError("strVal is not a str")

        self.writeInt(len(strVal))
        self._outStream.write(bytes(strVal, "utf=8"))
