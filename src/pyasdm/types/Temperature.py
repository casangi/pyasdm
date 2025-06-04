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
# File Temperature.py
#

import pyasdm.utils


class Temperature:
    """
    The Temperature class implements a concept of a temperature in degrees Centigrade.

    This version adapted from the c++ and java implementations, originall authored by Allen Farris.
    """

    @staticmethod
    def sum(a, b):
        """
        Return a new Temperature that is the sum of the
        specified temperatures, a +  b.
        param a The first Temperature of the pair.
        param b The second Temperature of the pair.
        return A new Temperature that is the sum of the
        specified temperatures, a +  b.
        """
        if not (isinstance(a, Temperature) and isinstance(b, Temperature)):
            raise ValueError("a and b must both be Temperature instances")

        return Temperature(a._temperature + b._temperature)

    @staticmethod
    def subtract(a, b):
        """
        Return a new Temperature that is the difference of the
        specified temperatures, a - b.
        param a The first Temperature of the pair.
        param b The second Temperature of the pair.
        return A new Temperature that is the difference of the
        specified temperatures, a - b.
        """
        if not (isinstance(a, Temperature) and isinstance(b, Temperature)):
            raise ValueError("a and b must both be Temperature instances")

        return Temperature(a._temperature - b._temperature)

    @staticmethod
    def multiply(a, factor):
        """
        Return a new Temperature that is the product of a specified
        temperature and some specified factor, a * factor.
        param a The base temperature
        param factor The factor that is used to multiply the value.
        return A new Temperature that is the product of a specified
        temperature and some specified factor, a * factor.
        """
        if not isinstance(a, Temperature):
            raise ValueError("a must be a Temperature")

        return Temperature(a._temperature * factor)

    @staticmethod
    def divide(a, factor):
        """
        Return a new Temperature that is a specified temperature divided by a
        specified factor, a / factor.
        param a The base temperature
        param factor The factor that is used to divide the value.
        return A new Temperature that is the product of a specified
        temperature and some specified factor, a / factor.
        """
        if not isinstance(a, Temperature):
            raise ValueError("a must be a Temperature")

        return Temperature(a._temperature / factor)

    @staticmethod
    def getInstance(stringList):
        """
        Retrieve a value from a list of strings and convert that to a Temperature

        This is used when parsing Temperature lists from an XML representation to
        eventually construct a list of Temperature instances. The string values
        are float representation of an angular rate in radians per second.

        Returns a tuple of (Temperature, stringList) where Temperature is the new Temperature
        created by this call and stringList is the remaining, unused, part of
        stringList after removing the first element.
        """
        if not isinstance(stringList, list):
            raise ValueError("stringList is not a list")

        # this will raise an error if there aren't any elements on stringList
        floatVal = float(stringList[0])
        return (Temperature(floatVal), stringList[1:])

    # The temperature in degrees Centigrade
    _temperature = 0.0

    def __init__(self, temperature=0.0):
        """
        Create a Temperature with an initial temperature in degrees Centigrade
        The default Temperature (no arguments) is zero (0.0) degrees Centigrade.
        Any temperature that is not a Temperature instance is valid so long as it can be
        converted to a float as float(temperature) (including a parseable string).
        If value is a Temperature instance then this is the copy constructor.
        """
        if isinstance(temperature, Temperature):
            self._temperature = temperature._temperature
        else:
            self.set(temperature)

    def get(self):
        """
        Return the value of this temperature as a double in degrees Centigrade.
        """
        return self._temperature

    def set(self, temperature):
        """
        Set the value of this temperature to the specified temperature in degrees Centigrade
        Any temperature is valid so long as it can be converted into a float using float(temperature)
        (including a parseable string).
        """
        self._temperature = float(temperature)

    def __str__(self):
        """
        Return the value of this temperature as a String in units of degrees Centigrade.
        """
        return str(self.get())

    @staticmethod
    def values(items):
        """
        return a list of floats containing the value of the list of Temperature objects
        passed in the items argument.
        items may also be a list of lists(2D array) of Temperature objects. If the
        first item is a list then this method assumes that items is a list of lists
        and the return value is a list of lists of floats.
        The list of lists case is done by calling this method recursively and so it
        should work for higher orders of lists of lists. That use case is not tested.
        """
        result = []
        if isinstance(items[0], list):
            # this is a list of lists, assume they are all lists
            for item in items:
                thisResult = Temperature.values(item)
                result.append(thisResult)
        else:
            if not isinstance(items[0], Temperature):
                raise ValueError("items must contain Temperature instances")
            # only check the first item
            for item in items:
                result.append(item.get())
        return result

    def toBin(self, eos):
        """
        Write this Temperature out, in degrees Centigrade, to a EndianOutput.
        """
        eos.writeDouble(self.get())

    @staticmethod
    def listToBin(temperatureList, eos):
        """
        Write a list of Temperature to the EndianOutput.
        The list may have 1, 2 or 3 dimensions.
        """
        if not isinstance(temperatureList, list):
            raise ValueError("temperatureList is not a list")

        # this is used to determine the number of dimensions
        listDims = pyasdm.utils.getListDims(temperatureList)
        ndims = len(listDims)
        if ndims == 1:
            Temperature.listTo1DBin(temperatureList, eos)
        elif ndims == 2:
            Temperature.listTo2DBin(temperatureList, eos)
        elif ndims == 3:
            Temperature.listTo3DBin(temperatureList, eos)
        else:
            raise ValueError(
                "unsupport number of dimensions in temperatureList in Temperature.listToBin : "
                + str(ndims)
            )

    @staticmethod
    def listTo1DBin(temperatureList, eos):
        """
        Write a 1D list of Temperature to the EndianOutput
        """
        if not isinstance(temperatureList, list):
            raise ValueError("temperatureList is not a list")

        # ndim is always written, even for 0-element lists
        eos.writeInt(len(temperatureList))

        # only check the first value
        if (len(temperatureList) > 0) and not isinstance(
            temperatureList[0], Temperature
        ):
            raise (ValueError("temperatureList is not a list of Temperature"))

        for thisTemperature in temperatureList:
            thisTemperature.toBin(eos)

    @staticmethod
    def listTo2DBin(temperatureList, eos):
        """
        Write a 2D list of Temperature to the EndianOutput
        """
        if not isinstance(temperatureList, list):
            raise ValueError("temperatureList is not a list")

        ndim1 = len(temperatureList)
        ndim2 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(temperatureList[0], list):
                raise ValueError("temperatureList is not a 2D")

            ndim2 = len(temperatureList[0])
            if ndim2 > 0 and not isinstance(temperatureList[0][0], Temperature):
                raise ValueError("temperatureListis a not a 2D list of Temperature")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)

        for thisList in temperatureList:
            for thisTemperature in thisList:
                thisTemperature.toBin(eos)

    @staticmethod
    def listTo3DBin(temperatureList, eos):
        """
        Write a 3D list of Temperature to the EndianOutput
        """
        if not isinstance(temperatureList, list):
            raise ValueError("temperatureList is not a list")

        ndim1 = len(temperatureList)
        ndim2 = 0
        ndim3 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(temperatureList[0], list):
                raise ValueError("temperatureList is not a 3D list")

            ndim2 = len(temperatureList[0])
            if ndim2 > 0:
                if not isinstance(temperatureList[0][0], list):
                    raise ValueError("temperatureList is a not a 3D list")
                ndim3 = len(temperatureList[0][0])
                if (ndim3 > 0) and not isinstance(
                    temperatureList[0][0][0], Temperature
                ):
                    raise ValueError("temperatureList is not a 3D list of Temperature")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)
        eos.writeInt(ndim3)

        for thisList in temperatureList:
            for middleList in thisList:
                for thisTemperature in middleList:
                    thisTemperature.toBin(eos)

    @staticmethod
    def fromBin(eis):
        """
        Read the binary representation of an Temperature, in degrees Centigrade,
        from an EndianInput instance and use the read value to set a
        Temperature.

        return an Temperature
        """
        return Temperature(eis.readDouble())

    @staticmethod
    def from1DBin(eis):
        """
        Read a list of binary Temperature values, in degrees Centigrade, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        result = []
        for i in range(dim1):
            result.append(Temperature.fromBin(eis))

        return result

    @staticmethod
    def from2DBin(eis):
        """
        Read a 2D list of binary Temperature values, in degrees Centigrade, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        dim2 = eis.readInt()
        result = []
        for i in range(dim1):
            innerList = []
            for j in range(dim2):
                innerList.append(Temperature.fromBin(eis))
            result.append(innerList)

        return result

    @staticmethod
    def from3Dbin(eis):
        """
        Read a 3D list of binary Temperature values, in degrees Centigrade, from an
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
                    innerList.append(Temperature.fromBin(eis))
                middleList.append(innerList)
            result.append(middleList)

        return result

    def equals(self, otherTemperature):
        """
        Return True if and only if the specified other temperature is a
        Temperature and its value is equal to this temperature.
        param otherTemperature The other temperature to which this temperature
        is being compared.
        return True if and only if the specified other temperature is an
        Temperature and its value is equal to this temperature.
        """
        return isinstance(otherTemperature, Temperature) and (
            self._temperature == otherTemperature._temperature
        )

    def almostEquals(self, otherTemperature, toleranceTemperature):
        """
        Return True if and only if otherTemperature and toleranceTemperature are both Temperature
        instances are if the absolute value of the difference between this and otherTemperature
        is less than the absolute value of toleranceTemperature.
        """
        result = False
        if isinstance(otherTemperature, Temperature) and isinstance(
            toleranceTemperature, Temperature
        ):
            result = abs(self._temperature - otherTemperature._temperature) <= abs(
                toleranceTemperature._temperature
            )

        return result

    def isZero(self):
        """
        Return True if and only if this temperature is zero (0.0).
        """
        return self._temperature == 0.0

    def compareTo(self, otherTemperature):
        """
        Compare this Temperature to the specified otherTemperature, which must be
        a Temperature, returning -1, 0, or +1 if this temperature is less
        than, equal to, or greater than the specified other Temperature.
        """
        if not isinstance(otherTemperature, Temperature):
            raise ("Attempt to compare a Temperature to a non-Temperature.")

        result = 0
        if self._temperature < otherTemperature._temperature:
            result = -1
        if self._temperature > otherTemperature._temperature:
            result = 1

        return result

    def __eq__(self, otherTemperature):
        """
        Return True if and only if this Temperature is equal to the specified
        other Temperature.
        This is equivalent to the equals method.
        """
        return self.equals(otherTemperature)

    def __ne__(self, otherTemperature):
        """
        Return True if and only if this Temperature is not equal to the specified
        other Temperature.
        """
        return isinstance(otherTemperature, Temperature) and (
            self._temperature != otherTemperature._temperature
        )

    def __lt__(self, otherTemperature):
        """
        Return True if and only if this Temperature is less than the specified
        other Temperature.
        """
        return isinstance(otherTemperature, Temperature) and (
            self._temperature < otherTemperature._temperature
        )

    def __le__(self, otherTemperature):
        """
        Return True if and only if this Temperature is less than or equal to
        the specified other Temperature.
        """
        return isinstance(otherTemperature, Temperature) and (
            self._temperature <= otherTemperature._temperature
        )

    def __gt__(self, otherTemperature):
        """
        Return True if and only if this Temperature is greater than the specified
        other Temperature.
        """
        return isinstance(otherTemperature, Temperature) and (
            self._temperature > otherTemperature._temperature
        )

    def __ge__(self, otherTemperature):
        """
        Return True if and only if this Temperature is greater than or equal to
        the specified other Temperature.
        """
        return isinstance(otherTemperature, Temperature) and (
            self._temperature >= otherTemperature._temperature
        )

    def __add__(self, otherTemperature):
        """
        Add otherTemperature, which must be a Temperature, to this temperature, (this + x).
        param otherTemperature The Temperature to be added to this temperature.
        return This temperature after the addition.
        """
        if not isinstance(otherTemperature, Temperature):
            raise ValueError("Attempt to add a non-Temperature to a Temperature")

        self._temperature += otherTemperature._temperature
        return self

    def __sub__(self, otherTemperature):
        """
        Subtract otherTemperature which must be a Temperature, from this temperature, (this - x).
        param otherTemperature The Temperature to be subtracted from this temperature.
        return This temperature after the subtraction.
        """
        if not isinstance(otherTemperature, Temperature):
            raise ValueError("Attempt to subtract a non-Temperature from a Temperature")

        self._temperature -= otherTemperature._temperature
        return self

    def __mul__(self, factor):
        """
        Multiply this temperature by some factor, (this * factor).
        param factor The factor by which this temperature is to be multiplied.
        return This temperature after the multiplication.
        """
        self._temperature *= factor
        return self

    def __truediv__(self, factor):
        """
        Divide this temperature by some factor, (this / factor).
        param factor The factor by which this temperature is to be divided.
        return This temperature after the division.
        """
        self._temperature /= factor
        return self
