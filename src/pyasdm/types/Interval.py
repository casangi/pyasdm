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
# File Interval.py

# this file was adapted from the c++ implementation
# original author, Allen Farris
# IDL (ACS) dependencies are not implemented here


"""
The Interval class implements a concept of an interval
of time in units of nanoseconds.
"""

import pyasdm.utils

class Interval:

    # the interval, in nanoseconds, this should be an integer, it should not be used directly
    _value = 0

    # intended for inernal use, used throughout this class
    # if value is an instance of Interval, returns value.value
    # if value is an integer, returns value
    # if value is a string, returns int(value)
    # else throws an exception  ** needs an exception here, is ValueError appropriate?
    @staticmethod
    def _getIntervalValue(value):
        if value is None:
            return 0

        if isinstance(value, Interval):
            return value.value
        elif type(value) is int:
            return value
        elif type(value) is str:
            return int(value)
        else:
            raise ValueError(
                "value is not an Interval, int, or str for _getIntervalValue"
            )
        # it should never get here
        return None

    @staticmethod
    def getInstance(stringList):
        """
        Retrieve a value from a list of strings and convert that to an Interval

        This is used when parsing Interval lists from an XML representation to
        eventually construct a list of Interval instances. The string values
        are integer representation of an integer representing an interval in nanoseconds.

        Returns a tuple of (Interval, stringList) where Interval is the new Interval
        created by this call and stringList is the remaining, unused, part of
        stringList after removing the first element.
        """
        if not isinstance(stringList, list):
            raise ValueError("stringList is not a list")

        # this will raise an error if there aren't any elements on stringList
        intVal = int(stringList[0])
        return (Interval(intVal), stringList[1:])

    # create an interval of time, defaults to 0
    #
    # The value is the length of the interval, in nanoseconds
    #
    def __init__(self, value=None):
        self.value = self._getIntervalValue(value)

    # the operators, they all work with either Interval, int, or str values

    # these operators change the value of this Interval using the argument and return this Interval

    # +=
    def __iadd__(self, other):
        self.value += self._getIntervalValue(other)
        return self

    # -=
    def __isub__(self, other):
        self.value -= self._getIntervalValue(other)
        return self

    # *=
    def __imul__(self, other):
        self.value *= self._getIntervalValue(other)
        return self

    # /=
    def __idoiv__(self, other):
        # note: this may lose precision because of the need for value and other to both be integers
        self.value /= self._getIntervalValue(other)
        # this may be unnecessary
        self.value = int(self.value)
        return self

    # binary operators, these return a new Interval and do not change self
    # +
    def __add__(self, other):
        return Interval(self.value + self._getIntervalValue(other))

    # =
    def __sub__(self, other):
        return Interval(self.value - self._getIntervalValue(other))

    # *
    def __mul__(self, other):
        return Interval(self.value * self._getIntervalValue(other))

    # /
    def __truediv__(self, other):
        # note - this may lose precision because of the need for this to be an integer
        return Interval(int(self.value / self._getIntervalValue(other)))

    # comparison operators
    def __lt__(self, other):
        return self.value < self._getIntervalValue(other)

    def __gt__(self, other):
        return self.value > self._getIntervalValue(other)

    def __le__(self, other):
        return self.value <= self._getIntervalValue(other)

    def __ge__(self, other):
        return self.value <= self._getIntervalValue(other)

    def __eq__(self, other):
        return self.value == self._getIntervalValue(other)

    def __ne__(self, other):
        return self.value != self._getIntervalValue(other)

    # unary operators, they return a new Interval and do not change this Interval
    def __neg__(self):
        return Interval(-self.value)

    def __pos__(self):
        return Interval(self.value)

    # Return True if and only if other is an Interval and its value is equal to this interval
    def equals(self, other):
        if not isinstance(other, Interval):
            return False
        return self.value == other.value

    def isZero(self):
        return self.value == 0

    def __str__(self):
        return str(self.value)

    # get the value, always nanoseconds
    def get(self):
        return self.value

    # set the value, always nanoseconds
    def set(self, value):
        self.value = int(value)

    # the units are always "nanosec", derived classes may change or add to that
    def unit(self):
        return "nanosec"

    # set the value from a string, throws a ValueError when string isn't properly formatted
    def fromString(self, s):
        self.value = int(s)

    def copy(self):
        tmp = Interval()
        tmp.value = self.value
        return tmp

    def toBin(self, eos):
        """
        Write this Interval out, in nanoseconds, to a EndianOutput.
        """
        eos.writeLong(self.get())

    @staticmethod
    def listToBin(intervalList, eos):
        """
        Write a list of Interval to the EndianOutput.
        The list may have 1, 2 or 3 dimensions.
        """
        if not isinstance(intervalList, list):
            raise ValueError("intervalList is not a list")

        # this is used to determine the number of dimensions
        listDims = pyasdm.utils.getListDims(intervalList)
        ndims = len(listDims)
        if ndims == 1:
            Interval.listTo1DBin(intervalList, eos)
        elif ndims == 2:
            Interval.listTo2DBin(intervalList, eos)
        elif ndims == 3:
            Interval.listTo3DBin(intervalList, eos)
        else:
            raise ValueError(
                "unsupport number of dimensions in intervalList in Interval.listToBin : "
                + str(ndims)
            )

    @staticmethod
    def listTo1DBin(intervalList, eos):
        """
        Write a 1D list of Interval to the EndianOutput
        """
        if not isinstance(intervalList, list):
            raise ValueError("intervalList is not a list")

        # ndim is always written, even for 0-element lists
        eos.writeInt(len(intervalList))

        # only check the first value
        if (len(intervalList) > 0) and not isinstance(intervalList[0], Interval):
            raise (ValueError("intervalList is not a list of Interval"))

        for thisInterval in intervalList:
            thisInterval.toBin(eos)

    @staticmethod
    def listTo2DBin(intervalList, eos):
        """
        Write a 2D list of Interval to the EndianOutput
        """
        if not isinstance(intervalList, list):
            raise ValueError("intervalList is not a list")

        ndim1 = len(intervalList)
        ndim2 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(intervalList[0], list):
                raise ValueError("intervalList is not a 2D")

            ndim2 = len(intervalList[0])
            if ndim2 > 0 and not isinstance(intervalList[0][0], Interval):
                raise ValueError("intervalListis a not a 2D list of Interval")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)

        for thisList in intervalList:
            for thisInterval in thisList:
                thisInterval.toBin(eos)

    @staticmethod
    def listTo3DBin(intervalList, eos):
        """
        Write a 3D list of Interval to the EndianOutput
        """
        if not isinstance(intervalList, list):
            raise ValueError("intervalList is not a list")

        ndim1 = len(intervalList)
        ndim2 = 0
        ndim3 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(intervalList[0], list):
                raise ValueError("intervalList is not a 3D list")

            ndim2 = len(intervalList[0])
            if ndim2 > 0:
                if not isinstance(intervalList[0][0], list):
                    raise ValueError("intervalList is a not a 3D list")
                ndim3 = len(intervalList[0][0])
                if (ndim3 > 0) and not isinstance(intervalList[0][0][0], Interval):
                    raise ValueError("intervalList is not a 3D list of Interval")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)
        eos.writeInt(ndim3)

        for thisList in intervalList:
            for middleList in thisList:
                for thisInterval in middleList:
                    thisInterval.toBin(eos)

    @staticmethod
    def fromBin(eis):
        """
        Read the binary representation of an Interval, in nanoseconds,
        from an EndianInput instance and use the read value to set an
        Interval.

        return an Interval
        """
        return Interval(eis.readLong())

    @staticmethod
    def from1DBin(eis):
        """
        Read a list of binary Interval values, in nanoseconds, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        result = []
        for i in range(dim1):
            result.append(Interval.fromBin(eis))

        return result

    @staticmethod
    def from2DBin(eis):
        """
        Read a 2D list of binary Interval values, in nanoseconds, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        dim2 = eis.readInt()
        result = []
        for i in range(dim1):
            innerList = []
            for j in range(dim2):
                innerList.append(Interval.fromBin(eis))
            result.append(innerList)

        return result

    @staticmethod
    def from3Dbin(eis):
        """
        Read a 3D list of binary Interval values, in nanoseconds, from an
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
                    innerList.append(Interval.fromBin(eis))
                middleList.append(innerList)
            result.append(middleList)

        return result
