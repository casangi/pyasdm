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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307  USA
#
# File Length.py
#

import pyasdm.utils


class Length:
    """
    The Length class implements a concept of a length in meters.

    This version adapted from the c++ and java implementation originally authored by Allen Farris
    """

    # Kilometer, km, an allowed unit of length.
    KILOMETER = "km"

    # Meter, m, an allowed unit of length.
    METER = "m"

    # Centimeter, cm, an allowed unit of length.
    CENTIMETER = "cm"

    # Millimeter, mm, an allowed unit of length.
    MILLIMETER = "mm"

    # An array of strings containing the allowable units of Length.
    AllowedUnits = [KILOMETER, METER, CENTIMETER, MILLIMETER]

    @staticmethod
    def unit():
        """
        Return the canonical unit associated with this Length, meter.
        return The unit associated with this Length.
        """
        return Length.METER

    @staticmethod
    def sum(l1, l2):
        """
        Return a new Length that is the sum of the
        specified lengths, l1 +  l2.
        l1 The first Length of the pair.
        l2 The second Length of the pair.
        return A new Length that is the sum of the specified lengths, l1 +  l2.
        """
        if not (isinstance(l1, Length) and isinstance(l2, Length)):
            raise ValueError("l1 and l2 must both be Length instances")

        return Length(l1._length + l2._length)

    @staticmethod
    def subtract(l1, l2):
        """
        Return a new Length that is the difference of the
        specified lengths, l1 - l2.
        l1 The first Length of the pair.
        l2 The second Length of the pair.
        return A new Length that is the difference of the specified lengths, l1 - l2.
        """
        if not (isinstance(l1, Length) and isinstance(l2, Length)):
            raise ValueError("l1 and l2 must both be Length instances")

        return Length(l1.length - l2.length)

    @staticmethod
    def multiply(l, factor):
        """
        Return a new Length that is the product of a specified
        length and some specified factor, l * factor.
        l The base length
        factor The factor that is used to multiply the value.
        return A new Length that is the product of a specified length and
        some specified factor, l * factor.
        """
        if not isinstance(l, Length):
            raise ValueError("l must be a Length")

        return Length(l.length * factor)

    @staticmethod
    def divide(l, factor):
        """
        Return a new Length that is a specified length divided by a
        specified factor, l / factor.
        l The base length
        factor The factor that is used to divide the value.
        return A new Length that is the quotient of a specified
        length and some specified factor, l / factor.
        """
        if not isinstance(l, Length):
            raise ValueError("l be a Length")

        return Length(l.length / factor)

    @staticmethod
    def getInstance(stringList):
        """
        Retrieve a value from a list of strings and convert that to a Length

        This is used when parsing Length lists from an XML representation to
        eventually construct a list of Length instances. The string values
        are float representation of a length in meters

        Returns a tuple of (Length, stringList) where Length is the new Length
        created by this call and stringList is the remaining, unused, part of
        stringList after removing the first element.
        """
        if not isinstance(stringList, list):
            raise ValueError("stringList is not a list")

        # this will raise an error if there aren't any elements on stringList
        floatVal = float(stringList[0])
        return (Length(floatVal), stringList[1:])

    # The length in meters.
    _length = 0.0

    def __init__(self, value=0.0, units=None):
        """
        Create a Length with an initial value and units.
        The default Length (no arguments) is zero (0.0) meters.
        The default units (none specified) is METER.
        The units must be one of the 4 recognized units: METER,
        KILOMETER, CENTIMETER, and MILLIMETER.
        Any value that is not a Length is valid so long as it can
        be converted to a float as float(value) (including a parseable string).
        If value is a Length instance then this is the copy constructor
        and any value of units other than None is illegal.
        """
        if isinstance(value, Length):
            if units is not None:
                raise ValueError("units can not be specied when value is a Length")
            self._length = value._length
        else:
            self.set(value, units)

    def get(self, units=None):
        """
        Return the value of this length in the specified units.
        When units is None (the default) the returned units are METER.
        Recognized units are None (METER), METER, KILOMETER, CENTIMETER, and MILLIMETER
        """
        if units is None or units == self.METER:
            return self._length
        if units == self.KILOMETER:
            return self._length / 1000.0
        if units == self.CENTIMETER:
            return self._length * 100.0
        if units == MILLIMETER:
            return self._length * 1000.0

        raise ValueError(str(units) + " is not an alllowable unit.")

    def set(self, value, units=None):
        """
        Set the value of this length to the given value in the specified units.
        Any value is valid so long as it can be converted into a float using float(value)
        (including a parseable string).
        The units is a string argument that detaults to METER as defined here.
        Recognized units are METER, KILOMETER, CENTIMETER, and MILLIMETER (also definied here).
        """

        # make sure that this is a float even if the value is an int or a string
        # other types probably work, too
        value = float(value)

        if units is None or units == self.METER:
            self._length = value
        elif units == self.KILOMETER:
            self._length = value * 1000.0
        elif units == self.CENTIMETER:
            self._length = value / 100.0
        elif units == self.MILLIMETER:
            self._length = value / 1000.0
        else:
            raise ValueError(str(units) + " is not an alllowable unit.")

    def __str__(self):
        """
        Return the value of this length as a string in the default units of METER.
        """
        return str(self.get())

    @staticmethod
    def values(items):
        """
        return a list of floats containing the value of the list of Length objects
        passed in the items argument.
        items may also be a list of lists (2D array) of Length objects. If the first
        item is a list then this method assumes that items is a list of lists and the
        return value is a list of lists of floats.
        The list of lists case is done by calling this method recursively and so it should
        work for higher orders of lists of lists. That use case is not tested.
        """
        result = []
        if isinstance(items[0], list):
            # this is a list of lists, assume they are all lists
            for item in items:
                thisResult = Length.values(item)
                result.append(thisResult)
        else:
            if not isinstance(items[0], Length):
                raise ValueError("items must contain Length instances")
            # only check the first item
            for item in items:
                result.append(item.get())
        return result

    def toBin(self, eos):
        """
        Write this Length out, in meters, to a EndianOutput.
        """
        eos.writeDouble(self.get())

    @staticmethod
    def listToBin(lengthList, eos):
        """
        Write a list of Length to the EndianOutput.
        The list may have 1, 2 or 3 dimensions.
        """
        if not isinstance(lengthList, list):
            raise ValueError("lengthList is not a list")

        # this is used to determine the number of dimensions
        listDims = pyasdm.utils.getListDims(lengthList)
        ndims = len(listDims)
        if ndims == 1:
            Length.listTo1DBin(lengthList, eos)
        elif ndims == 2:
            Length.listTo2DBin(lengthList, eos)
        elif ndims == 3:
            Length.listTo3DBin(lengthList, eos)
        else:
            raise ValueError(
                "unsupport number of dimensions in lengthList in Length.listToBin : "
                + str(ndims)
            )

    @staticmethod
    def listTo1DBin(lengthList, eos):
        """
        Write a 1D list of Length to the EndianOutput
        """
        if not isinstance(lengthList, list):
            raise ValueError("lengthList is not a list")

        # ndim is always written, even for 0-element lists
        eos.writeInt(len(lengthList))

        # only check the first value
        if (len(lengthList) > 0) and not isinstance(lengthList[0], Length):
            raise (ValueError("lengthList is not a list of Length"))

        for thisLength in lengthList:
            thisLength.toBin(eos)

    @staticmethod
    def listTo2DBin(lengthList, eos):
        """
        Write a 2D list of Length to the EndianOutput
        """
        if not isinstance(lengthList, list):
            raise ValueError("lengthList is not a list")

        ndim1 = len(lengthList)
        ndim2 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(lengthList[0], list):
                raise ValueError("lengthList is not a 2D")

            ndim2 = len(lengthList[0])
            if ndim2 > 0 and not isinstance(lengthList[0][0], Length):
                raise ValueError("lengthListis a not a 2D list of Length")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)

        for thisList in lengthList:
            for thisLength in thisList:
                thisLength.toBin(eos)

    @staticmethod
    def listTo3DBin(lengthList, eos):
        """
        Write a 3D list of Length to the EndianOutput
        """
        if not isinstance(lengthList, list):
            raise ValueError("lengthList is not a list")

        ndim1 = len(lengthList)
        ndim2 = 0
        ndim3 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(lengthList[0], list):
                raise ValueError("lengthList is not a 3D list")

            ndim2 = len(lengthList[0])
            if ndim2 > 0:
                if not isinstance(lengthList[0][0], list):
                    raise ValueError("lengthList is a not a 3D list")
                ndim3 = len(lengthList[0][0])
                if (ndim3 > 0) and not isinstance(lengthList[0][0][0], Length):
                    raise ValueError("lengthList is not a 3D list of Length")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)
        eos.writeInt(ndim3)

        for thisList in lengthList:
            for middleList in thisList:
                for thisLength in middleList:
                    thisLength.toBin(eos)

    @staticmethod
    def fromBin(eis):
        """
        Read the binary representation of an Length, in meters,
        from an EndianInput instance and use the read value to set a
        Length.

        return a Length
        """
        return Length(eis.readDouble())

    @staticmethod
    def from1DBin(eis):
        """
        Read a list of binary Length values, in meters, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        result = []
        for i in range(dim1):
            result.append(Length.fromBin(eis))

        return result

    @staticmethod
    def from2DBin(eis):
        """
        Read a 2D list of binary Length values, in meters, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        dim2 = eis.readInt()
        result = []
        for i in range(dim1):
            innerList = []
            for j in range(dim2):
                innerList.append(Length.fromBin(eis))
            result.append(innerList)

        return result

    @staticmethod
    def from3Dbin(eis):
        """
        Read a 3D list of binary Length values, in meters, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        dim2 = eis.readInt()
        dim3 = eis.readInt()
        result = []
        for i in range(dim1):
            middleList = []
            for j in range(dim2):
                innerList = []
                for k in range(dim3):
                    innerList.append(Length.fromBin(eis))
                middleList.append(innerList)
            result.append(middleList)

        return result

    def equals(self, otherLength):
        """
        Return True if and only if the specified other length is a Length
        that has a value that is equal to this length.
        """
        return isinstance(otherLength, Length) and (self._length == otherLength._length)

    def almostEquals(self, otherLength, toleranceLength):
        """
        Returns True if and only if otherLength and toleranceLength are both Lengths
        and if the distance (absolute value of the difference) between this Length
        and otherLength is less than the absolute value of toleranceLength.
        """
        result = False
        if isinstance(otherLength, Length) and isinstance(toleranceLength, Length):
            result = abs(self._length - otherLength._length) <= abs(
                toleranceLength._length
            )

        return result

    def isZero(self):
        """
        Return True if and only if this length is zero (0.0).
        """
        return self._length == 0.0

    def compareTo(self, otherLength):
        """
        Compare this Length to the specified otherLength, which must be a Length.
        Returning -1, 0, or +1 if this Length is less than, equal to, or greater
        than the other Length.
        """
        if not isinstance(otherLength, Length):
            raise ValueError("Attempt to compare a Length to a non-Length.")

        result = 0
        if self._length < otherLength._length:
            result = -1
        elif self._length > otherLength._length:
            result = 1

        return result

    def __eq__(self, otherLength):
        """
        Returns True if and only if this Length is equal to the otherLength.
        this is equivalent to the equals method.
        """
        return self.equals(otherLength)

    def __ne__(self, otherLength):
        """
        Returns True if and only if this Length is not equal to otherLength
        """
        return isinstance(otherLength, Length) and (self._length != otherLength._length)

    def __lt__(self, otherLength):
        """
        Returns True if and only if this Length is less than to otherLength
        """
        return isinstance(otherLength, Length) and (self._length < otherLength._length)

    def __le__(self, otherLength):
        """
        Returns True if and only if this Length is less than or equal to otherLength
        """
        return isinstance(otherLength, Length) and (self._length <= otherLength._length)

    def __gt__(self, otherLength):
        """
        Returns True if and only if this Length is greater than otherLength
        """
        return isinstance(otherLength, Length) and (self._length > otherLength._length)

    def __ge__(self, otherLength):
        """
        Returns True if and only if this Length is greater than or equal to otherLength
        """
        return isinstance(otherLength, Length) and (self._length >= otherLength._length)

    def __add__(self, otherLength):
        """
        Add otherLength, which must be a Length, to this Length, returning this Length
        """
        if not isinstance(otherLength, Length):
            raise ValueError("otherLength must be a Length")

        self._length += otherLength._length
        return self

    def __sub__(self, otherLength):
        """
        Subtract a specified Length from this length, (this - x).
        """
        if not isinstance(otherLength, length):
            raise ValueError("otherLength must be a length")

        self._length -= otherLengthx._length
        return self

    def __mul__(self, factor):
        """
        Multiply this length by some factor, (this * factor).
        Return this length after multiplication.
        """
        self._length *= factor
        return self

    def __truediv__(factor):
        """
        Divide this length by some factor, (this / factor).
        Return this length after division.
        """
        self._length /= factor
        return self
