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
# File Pressure.py
#

import pyasdm.utils

class Pressure:
    """
    The Pressure class implements a concept of an atmospheric pressure in hectopascals.

    This version adapted from the c++ and java implementations, originall authored by Allen Farris.
    """

    @staticmethod
    def sum(a, b):
        """
        Return a new Pressure that is the sum of the
        specified hectopascals, a +  b.
        param a The first Pressure of the pair.
        param b The second Pressure of the pair.
        return A new Pressure that is the sum of the
        specified hectopascals, a +  b.
        """
        if not (isinstance(a, Pressure) and isinstance(b, Pressure)):
            raise ValueError("a and b must both be Pressure instances")

        return Pressure(a._pressure + b._pressure)

    @staticmethod
    def subtract(a, b):
        """
        Return a new Pressure that is the difference of the
        specified hectopascals, a - b.
        param a The first Pressure of the pair.
        param b The second Pressure of the pair.
        return A new Pressure that is the difference of the
        specified hectopascals, a - b.
        """
        if not (isinstance(a, Pressure) and isinstance(b, Pressure)):
            raise ValueError("a and b must both be Pressure instances")

        return Pressure(a._pressure - b._pressure)

    @staticmethod
    def multiply(a, factor):
        """
        Return a new Pressure that is the product of a specified
        pressure and some specified factor, a * factor.
        param a The base pressure
        param factor The factor that is used to multiply the value.
        return A new Pressure that is the product of a specified
        pressure and some specified factor, a * factor.
        """
        if not isinstance(a, Pressure):
            raise ValueError("a must be a Pressure")

        return Pressure(a._pressure * factor)

    @staticmethod
    def divide(a, factor):
        """
        Return a new Pressure that is a specified pressure divided by a
        specified factor, a / factor.
        param a The base pressure
        param factor The factor that is used to divide the value.
        return A new Pressure that is the product of a specified
        pressure and some specified factor, a / factor.
        """
        if not isinstance(a, Pressure):
            raise ValueError("a must be a Pressure")

        return Pressure(a._pressure / factor)

    @staticmethod
    def getInstance(stringList):
        """
        Retrieve a value from a list of strings and convert that to a Pressure

        This is used when parsing Pressure lists from an XML representation to
        eventually construct a list of Pressure instances. The string values
        are float representation of a pressure in hectopascals.

        Returns a tuple of (Pressure, stringList) where Pressure is the new Pressure
        created by this call and stringList is the remaining, unused, part of
        stringList after removing the first element.
        """
        if not isinstance(stringList, list):
            raise ValueError("stringList is not a list")

        # this will raise an error if there aren't any elements on stringList
        floatVal = float(stringList[0])
        return (Pressure(floatVal), stringList[1:])

    # The pressure in hectopascals.
    _pressure = 0.0

    def __init__(self, value=0.0):
        """
        Create a Pressure with an initial value in hectopascals.
        The default Pressure (no arguments) is zero (0.0) hectopascals.
        Any value that is not a Pressure is valid so long as it can be
        converted to a float as float(value) (including a parseable string).
        If value is a Pressure instance then this is the copy constructor.
        """
        if isinstance(value, Pressure):
            self._pressure = value._pressure
        else:
            self.set(value)

    def get(self):
        """
        Return the value of this pressure as a double in hectopascals.
        """
        return self._pressure

    def set(self, value):
        """
        Set the value of this pressure to the specified value in hectopascals.
        Any value is valid so long as it can be converted into a float using float(value)
        (including a parseable string).
        """
        self._pressure = float(value)

    def __str__(self):
        """
        Return the value of this pressure as a String in units of hectopascals.
        """
        return str(self.get())

    @staticmethod
    def values(items):
        """
        return a list of floats containing the value of the list of Pressure objects
        passed in the items argument.
        items may also be a list of lists(2D array) of Pressure objects. If the
        first item is a list then this method assumes that items is a list of lists
        and the return value is a list of lists of floats.
        The list of lists case is done by calling this method recursively and so it
        should work for higher orders of lists of lists. That use case is not tested.
        """
        result = []
        if isinstance(items[0], list):
            # this is a list of lists, assume they are all lists
            for item in items:
                thisResult = Pressure.values(item)
                result.append(thisResult)
        else:
            if not isinstance(items[0], Pressure):
                raise ValueError("items must contain Pressure instances")
            # only check the first item
            for item in items:
                result.append(item.get())
        return result

    def toBin(self, eos):
        """
        Write this Pressure out, in hectopascals, to a EndianOutput.
        """
        eos.writeDouble(self.get())

    @staticmethod
    def listToBin(pressureList, eos):
        """
        Write a list of Pressure to the EndianOutput.
        The list may have 1, 2 or 3 dimensions.
        """
        if not isinstance(pressureList, list):
            raise ValueError("pressureList is not a list")

        # this is used to determine the number of dimensions
        listDims = pyasdm.utils.getListDims(pressureList)
        ndims = len(listDims)
        if ndims == 1:
            Pressure.listTo1DBin(pressureList, eos)
        elif ndims == 2:
            Pressure.listTo2DBin(pressureList, eos)
        elif ndims == 3:
            Pressure.listTo3DBin(pressureList, eos)
        else:
            raise ValueError(
                "unsupport number of dimensions in pressureList in Pressure.listToBin : "
                + str(ndims)
            )

    @staticmethod
    def listTo1DBin(pressureList, eos):
        """
        Write a 1D list of Pressure to the EndianOutput
        """
        if not isinstance(pressureList, list):
            raise ValueError("pressureList is not a list")

        # ndim is always written, even for 0-element lists
        eos.writeInt(len(pressureList))

        # only check the first value
        if (len(pressureList) > 0) and not isinstance(pressureList[0], Pressure):
            raise (ValueError("pressureList is not a list of Pressure"))

        for thisPressure in pressureList:
            thisPressure.toBin(eos)

    @staticmethod
    def listTo2DBin(pressureList, eos):
        """
        Write a 2D list of Pressure to the EndianOutput
        """
        if not isinstance(pressureList, list):
            raise ValueError("pressureList is not a list")

        ndim1 = len(pressureList)
        ndim2 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(pressureList[0], list):
                raise ValueError("pressureList is not a 2D")

            ndim2 = len(pressureList[0])
            if ndim2 > 0 and not isinstance(pressureList[0][0], Pressure):
                raise ValueError("pressureListis a not a 2D list of Pressure")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)

        for thisList in pressureList:
            for thisPressure in thisList:
                thisPressure.toBin(eos)

    @staticmethod
    def listTo3DBin(pressureList, eos):
        """
        Write a 3D list of Pressure to the EndianOutput
        """
        if not isinstance(pressureList, list):
            raise ValueError("pressureList is not a list")

        ndim1 = len(pressureList)
        ndim2 = 0
        ndim3 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(pressureList[0], list):
                raise ValueError("pressureList is not a 3D list")

            ndim2 = len(pressureList[0])
            if ndim2 > 0:
                if not isinstance(pressureList[0][0], list):
                    raise ValueError("pressureList is a not a 3D list")
                ndim3 = len(pressureList[0][0])
                if (ndim3 > 0) and not isinstance(pressureList[0][0][0], Pressure):
                    raise ValueError("pressureList is not a 3D list of Pressure")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)
        eos.writeInt(ndim3)

        for thisList in pressureList:
            for middleList in thisList:
                for thisPressure in middleList:
                    thisPressure.toBin(eos)

    @staticmethod
    def fromBin(eis):
        """
        Read the binary representation of an Pressure, in hectopascals,
        from an EndianInput instance and use the read value to set a
        Pressure.

        return an Pressure
        """
        return Pressure(eis.readDouble())

    @staticmethod
    def from1DBin(eis):
        """
        Read a list of binary Pressure values, in hectopascals, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        result = []
        for i in range(dim1):
            result.append(Pressure.fromBin(eis))

        return result

    @staticmethod
    def from2DBin(eis):
        """
        Read a 2D list of binary Pressure values, in hectopascals, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        dim2 = eis.readInt()
        result = []
        for i in range(dim1):
            innerList = []
            for j in range(dim2):
                innerList.append(Pressure.fromBin(eis))
            result.append(innerList)

        return result

    @staticmethod
    def from3Dbin(eis):
        """
        Read a 3D list of binary Pressure values, in hectopascals, from an
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
                    innerList.append(Pressure.fromBin(eis))
                middleList.append(innerList)
            result.append(middleList)

        return result

    def equals(self, otherPressure):
        """
        Return True if and only if the specified other pressure is a
        Pressure and its value is equal to this pressure.
        param otherPressure The other pressure to which this pressure
        is being compared.
        return True if and only if the specified other pressure is an
        Pressure and its value is equal to this pressure.
        """
        return isinstance(otherPressure, Pressure) and (
            self._pressure == otherPressure._pressure
        )

    def almostEquals(self, otherPressure, tolerancePressure):
        """
        Return True if and only if otherPressure and tolerancePressure are both Pressure
        instances are if the absolute value of the difference between this and otherPressure
        is less than the absolute value of tolerancePressure.
        """
        result = False
        if isinstance(otherPressure, Pressure) and isinstance(
            tolerancePressure, Pressure
        ):
            result = abs(self._pressure - otherPressure._pressure) <= abs(
                tolerancePressure._pressure
            )

        return result

    def isZero(self):
        """
        Return True if and only if this pressure is zero (0.0).
        """
        return self._pressure == 0.0

    def compareTo(self, otherPressure):
        """
        Compare this Pressure to the specified otherPressuret, which must be
        a Pressure, returning -1, 0, or +1 if this pressure is less
        than, equal to, or greater than the specified other Pressure.
        """
        if not isinstance(otherPressure, Pressure):
            raise ("Attempt to compare a Pressure to a non-Pressure.")

        result = 0
        if self._pressure < otherPressure._pressure:
            result = -1
        if self._pressure > otherPressure._pressure:
            result = 1

        return result

    def __eq__(self, otherPressure):
        """
        Return True if and only if this Pressure is equal to the specified
        other Pressure.
        This is equivalent to the equals method.
        """
        return self.equals(otherPressure)

    def __ne__(self, otherPressure):
        """
        Return True if and only if this Pressure is not equal to the specified
        other Pressure.
        """
        return isinstance(otherPressure, Pressure) and (
            self._pressure != otherPressure._pressure
        )

    def __lt__(self, otherPressure):
        """
        Return True if and only if this Pressure is less than the specified
        other Pressure.
        """
        return isinstance(otherPressure, Pressure) and (
            self._pressure < otherPressure._pressure
        )

    def __le__(self, otherPressure):
        """
        Return True if and only if this Pressure is less than or equal to
        the specified other Pressure.
        """
        return isinstance(otherPressure, Pressure) and (
            self._pressure <= otherPressure._pressure
        )

    def __gt__(self, otherPressure):
        """
        Return True if and only if this Pressure is greater than the specified
        other Pressure.
        """
        return isinstance(otherPressure, Pressure) and (
            self._pressure > otherPressure._pressure
        )

    def __ge__(self, otherPressure):
        """
        Return True if and only if this Pressure is greater than or equal to
        the specified other Pressure.
        """
        return isinstance(otherPressure, Pressure) and (
            self._pressure >= otherPressure._pressure
        )

    def __add__(self, otherPressure):
        """
        Add otherPressure, which must be a Pressure, to this pressure, (this + x).
        param otherPressure The Pressure to be added to this pressure.
        return This pressure after the addition.
        """
        if not isinstance(otherPressure, Pressure):
            raise ValueError("Attempt to add a non-Pressure to a Pressure")

        self._pressure += otherPressure._pressure
        return self

    def __sub__(self, otherPressure):
        """
        Subtract otherPressure which must be a Pressure, from this pressure, (this - x).
        param otherPressure The Pressure to be subtracted from this pressure.
        return This pressure after the subtraction.
        """
        if not isinstance(otherPressure, Pressure):
            raise ValueError("Attempt to subtract a non-Pressure from a Pressure")

        self._pressure -= otherPressure._pressure
        return self

    def __mul__(self, factor):
        """
        Multiply this pressure by some factor, (this * factor).
        param factor The factor by which this pressure is to be multiplied.
        return This pressure after the multiplication.
        """
        self._pressure *= factor
        return self

    def __truediv__(self, factor):
        """
        Divide this pressure by some factor, (this / factor).
        param factor The factor by which this pressure is to be divided.
        return This pressure after the division.
        """
        self._pressure /= factor
        return self
