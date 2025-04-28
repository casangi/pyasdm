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
# File Humidity.py
#

import pyasdm.utils

class Humidity:
    """
    The Humidity class implements a concept of a relative humidity in percent.

    This version adapted from the c++ and java implementations, originall authored by Allen Farris.
    """

    @staticmethod
    def sum(a, b):
        """
        Return a new Humidity that is the sum of the
        specified percents, a +  b.
        param a The first Humidity of the pair.
        param b The second Humidity of the pair.
        return A new Humidity that is the sum of the
        specified hectopascals, a +  b.
        """
        if not (isinstance(a, Humidity) and isinstance(b, Humidity)):
            raise ValueError("a and b must both be Humidity instances")

        return Humidity(a._percent + b._percent)

    @staticmethod
    def subtract(a, b):
        """
        Return a new Humidity that is the difference of the
        specified percents, a - b.
        param a The first Humidity of the pair.
        param b The second Humidity of the pair.
        return A new Humidity that is the difference of the
        specified hectopascals, a - b.
        """
        if not (isinstance(a, Humidity) and isinstance(b, Humidity)):
            raise ValueError("a and b must both be Humidity instances")

        return Humidity(a._percent - b._percent)

    @staticmethod
    def multiply(a, factor):
        """
        Return a new Humidity that is the product of a specified
        percent and some specified factor, a * factor.
        param a The base percent
        param factor The factor that is used to multiply the value.
        return A new Humidity that is the product of a specified
        percent and some specified factor, a * factor.
        """
        if not isinstance(a, Humidity):
            raise ValueError("a must be a Humidity")

        return Humidity(a._percent * factor)

    @staticmethod
    def divide(a, factor):
        """
        Return a new Humidity that is a specified percent divided by a
        specified factor, a / factor.
        param a The base percent
        param factor The factor that is used to divide the value.
        return A new Humidity that is the product of a specified
        percent and some specified factor, a / factor.
        """
        if not isinstance(a, Humidity):
            raise ValueError("a must be a Humidity")

        return Humidity(a._percent / factor)

    @staticmethod
    def getInstance(stringList):
        """
        Retrieve a value from a list of strings and convert that to a Humidity.

        This is used when parsing Humidity lists from an XML representation to
        eventually construct a list of Humidity instances. The string values
        are float representation of a relative humidity in percent.

        Returns a tuple of (Humidity, stringList) where Humidity is the new Humidity
        created by this call and stringList is the remaining, unused, part of
        stringList after removing the first element.
        """
        if not isinstance(stringList, list):
            raise ValueError("stringList is not a list")

        # this will raise an error if there aren't any elements on stringList
        floatVal = float(stringList[0])
        return (Humidity(floatVal), stringList[1:])

    # The percent in percents.
    _percent = 0.0

    def __init__(self, percent=0.0):
        """
        Create a Humidity with an initial value in percents.
        The default Humidity (no arguments) is zero (0.0) percents.
        Any percent that is not a Humidity is valid so long as it can be
        converted to a float as float(percent) (including a parseable string).
        If percent is a Humidity instance then this is the copy constructor.
        """
        if isinstance(percent, Humidity):
            self._percent = percent._percent
        else:
            self.set(percent)

    def get(self):
        """
        Return the value of this percent in percents.
        """
        return self._percent

    def set(self, percent):
        """
        Set the value of this percent to the specified percent in percents.
        Any value is valid so long as it can be converted into a float using float(percent)
        (including a parseable string).
        """
        self._percent = float(percent)

    def __str__(self):
        """
        Return the value of this humidity as a String in units of percents.
        """
        return str(self.get())

    @staticmethod
    def values(items):
        """
        return a list of floats containing the value of the list of Humidity objects
        passed in the items argument.
        items may also be a list of lists(2D array) of Humidity objects. If the
        first item is a list then this method assumes that items is a list of lists
        and the return value is a list of lists of floats.
        The list of lists case is done by calling this method recursively and so it
        should work for higher orders of lists of lists. That use case is not tested.
        """
        result = []
        if isinstance(items[0], list):
            # this is a list of lists, assume they are all lists
            for item in items:
                thisResult = Humidity.values(item)
                result.append(thisResult)
        else:
            if not isinstance(items[0], Humidity):
                raise ValueError("items must contain Humidity instances")
            # only check the first item
            for item in items:
                result.append(item.get())
        return result

    def toBin(self, eos):
        """
        Write this Humidity out, in percent, to a EndianOutput.
        """
        eos.writeDouble(self.get())

    @staticmethod
    def listToBin(humidityList, eos):
        """
        Write a list of Humidity to the EndianOutput.
        The list may have 1, 2 or 3 dimensions.
        """
        if not isinstance(humidityList, list):
            raise ValueError("humidityList is not a list")

        # this is used to determine the number of dimensions
        listDims = pyasdm.utils.getListDims(humidityList)
        ndims = len(listDims)
        if ndims == 1:
            Humidity.listTo1DBin(humidityList, eos)
        elif ndims == 2:
            Humidity.listTo2DBin(humidityList, eos)
        elif ndims == 3:
            Humidity.listTo3DBin(humidityList, eos)
        else:
            raise ValueError(
                "unsupport number of dimensions in humidityList in Humidity.listToBin : "
                + str(ndims)
            )

    @staticmethod
    def listTo1DBin(humidityList, eos):
        """
        Write a 1D list of Humidity to the EndianOutput
        """
        if not isinstance(humidityList, list):
            raise ValueError("humidityList is not a list")

        # ndim is always written, even for 0-element lists
        eos.writeInt(len(humidityList))

        # only check the first value
        if (len(humidityList) > 0) and not isinstance(humidityList[0], Humidity):
            raise (ValueError("humidityList is not a list of Humidity"))

        for thisHumidity in humidityList:
            thisHumidity.toBin(eos)

    @staticmethod
    def listTo2DBin(humidityList, eos):
        """
        Write a 2D list of Humidity to the EndianOutput
        """
        if not isinstance(humidityList, list):
            raise ValueError("humidityList is not a list")

        ndim1 = len(humidityList)
        ndim2 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(humidityList[0], list):
                raise ValueError("humidityList is not a 2D")

            ndim2 = len(humidityList[0])
            if ndim2 > 0 and not isinstance(humidityList[0][0], Humidity):
                raise ValueError("humidityListis a not a 2D list of Humidity")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)

        for thisList in humidityList:
            for thisHumidity in thisList:
                thisHumidity.toBin(eos)

    @staticmethod
    def listTo3DBin(humidityList, eos):
        """
        Write a 3D list of Humidity to the EndianOutput
        """
        if not isinstance(humidityList, list):
            raise ValueError("humidityList is not a list")

        ndim1 = len(humidityList)
        ndim2 = 0
        ndim3 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(humidityList[0], list):
                raise ValueError("humidityList is not a 3D list")

            ndim2 = len(humidityList[0])
            if ndim2 > 0:
                if not isinstance(humidityList[0][0], list):
                    raise ValueError("humidityList is a not a 3D list")
                ndim3 = len(humidityList[0][0])
                if (ndim3 > 0) and not isinstance(humidityList[0][0][0], Humidity):
                    raise ValueError("humidityList is not a 3D list of Humidity")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)
        eos.writeInt(ndim3)

        for thisList in humidityList:
            for middleList in thisList:
                for thisHumidity in middleList:
                    thisHumidityy.toBin(eos)

    @staticmethod
    def fromBin(eis):
        """
        Read the binary representation of an Humidity, in percent,
        from an EndianInput instance and use the read value to set a
        Humidity.

        return an Humidity
        """
        return Humidity(eis.readDouble())

    @staticmethod
    def from1DBin(eis):
        """
        Read a list of binary Humidity values, in percent, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        result = []
        for i in range(dim1):
            result.append(Humidity.fromBin(eis))

        return result

    @staticmethod
    def from2DBin(eis):
        """
        Read a 2D list of binary Humidity values, in percent, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        dim2 = eis.readInt()
        result = []
        for i in range(dim1):
            innerList = []
            for j in range(dim2):
                innerList.append(Humidity.fromBin(eis))
            result.append(innerList)

        return result

    @staticmethod
    def from3DBin(eis):
        """
        Read a 3D list of binary Humidity values, in percent, from an
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
                    innerList.append(Humidity.fromBin(eis))
                middleList.append(innerList)
            result.append(middleList)

        return result

    def equals(self, otherHumidity):
        """
        Return True if and only if the specified other humidity is a
        Humidity and its value is equal to this percent.
        param otherHumidity The other humidity to which this humidity
        is being compared.
        return True if and only if the specified other humidity is an
        Humidity and its value is equal to this humidity.
        """
        return isinstance(otherHumidity, Humidity) and (
            self._percent == otherHumidity._percent
        )

    def almostEquals(self, otherHumidity, toleranceHumidity):
        """
        Return True if and only if otherHumidity and toleranceHumidity are both Humidity
        instances are if the absolute value of the difference between this and otherHumidity
        is less than the absolute value of toleranceHumidity.
        """
        result = False
        if isinstance(otherHumidity, Humidity) and isinstance(
            toleranceHumidity, Humidity
        ):
            result = abs(self._percent - otherHumidity._percent) <= abs(
                toleranceHumidity._percent
            )

        return result

    def isZero(self):
        """
        Return True if and only if this percent is zero (0.0).
        """
        return self._percent == 0.0

    def compareTo(self, otherHumidity):
        """
        Compare this Humidity to the specified otherHumidityt, which must be
        a Humidity, returning -1, 0, or +1 if this percent is less
        than, equal to, or greater than the specified other Humidity.
        """
        if not isinstance(otherHumidity, Humidity):
            raise ("Attempt to compare a Humidity to a non-Humidity.")

        result = 0
        if self._percent < otherHumidity._percent:
            result = -1
        if self._percent > otherHumidity._percent:
            result = 1

        return result

    def __eq__(self, otherHumidity):
        """
        Return True if and only if this Humidity is equal to the specified
        other Humidity.
        This is equivalent to the equals method.
        """
        return self.equals(otherHumidity)

    def __ne__(self, otherHumidity):
        """
        Return True if and only if this Humidity is not equal to the specified
        other Humidity.
        """
        return isinstance(otherHumidity, Humidity) and (
            self._percent != otherHumidity._percent
        )

    def __lt__(self, otherHumidity):
        """
        Return True if and only if this Humidity is less than the specified
        other Humidity.
        """
        return isinstance(otherHumidity, Humidity) and (
            self._percent < otherHumidity._percent
        )

    def __le__(self, otherHumidity):
        """
        Return True if and only if this Humidity is less than or equal to
        the specified other Humidity.
        """
        return isinstance(otherHumidity, Humidity) and (
            self._percent <= otherHumidity._percent
        )

    def __gt__(self, otherHumidity):
        """
        Return True if and only if this Humidity is greater than the specified
        other Humidity.
        """
        return isinstance(otherHumidity, Humidity) and (
            self._percent > otherHumidity._percent
        )

    def __ge__(self, otherHumidity):
        """
        Return True if and only if this Humidity is greater than or equal to
        the specified other Humidity.
        """
        return isinstance(otherHumidity, Humidity) and (
            self._percent >= otherHumidity._percent
        )

    def __add__(self, otherHumidity):
        """
        Add otherHumidity, which must be a Humidity, to this percent, (this + x).
        param otherHumidity The Humidity to be added to this percent.
        return This percent after the addition.
        """
        if not isinstance(otherHumidity, Humidity):
            raise ValueError("Attempt to add a non-Humidity to a Humidity")

        self._percent += otherHumidity._percent
        return self

    def __sub__(self, otherHumidity):
        """
        Subtract otherHumidity which must be a Humidity, from this percent, (this - x).
        param otherHumidity The Humidity to be subtracted from this percent.
        return This percent after the subtraction.
        """
        if not isinstance(otherHumidity, Humidity):
            raise ValueError("Attempt to subtract a non-Humidity from a Humidity")

        self._percent -= otherHumidity._percent
        return self

    def __mul__(self, factor):
        """
        Multiply this percent by some factor, (this * factor).
        param factor The factor by which this percent is to be multiplied.
        return This percent after the multiplication.
        """
        self._percent *= factor
        return self

    def __truediv__(self, factor):
        """
        Divide this percent by some factor, (this / factor).
        param factor The factor by which this percent is to be divided.
        return This percent after the division.
        """
        self._percent /= factor
        return self
