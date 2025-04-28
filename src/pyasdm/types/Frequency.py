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
# File Frequency.py
#

import pyasdm.utils

class Frequency:
    """
    The Frequency class implements a concept of a frequency in hertz.

    This version adapted from the c++ and java implementations, originall authored by Allen Farris.
    """

    # Hertz, Hz, an allowed unit of frequency.
    HERTZ = "Hz"

    # Kilohertz, kHz, an allowed unit of frequency.
    KILOHERTZ = "kHz"

    # Megahertz, MHz, an allowed unit of frequency.
    MEGAHERTZ = "MHz"

    # Gigahertz, GHz, an allowed unit of frequency.
    GIGAHERTZ = "GHz"

    # An list of strings containing the allowable units of frequency.
    AllowedUnits = [HERTZ, KILOHERTZ, MEGAHERTZ, GIGAHERTZ]

    @staticmethod
    def unit():
        """
        Return the canonical unit associated with this Frequency, hertz.
        return The unit associated with this Frequency.
        """
        return Frequency.HERTZ

    @staticmethod
    def sum(f1, f2):
        """
        Return a new Frequency that is the sum of the
        specified Frequencies, f1 +  f2.
        param f1 The first Frequency of the pair.
        param f2 The second Frequency of the pair.
        return A new Frequency that is the sum of the
        specified Frequencies, f1 +  f2.
        """
        if not (isinstance(f1, Frequency) and isinstance(f2, Frequency)):
            raise ValueError("f1 and f2 must both be Frequency instances")

        return Frequency(f1._frequency + f2._frequency)

    @staticmethod
    def subtract(f1, f2):
        """
        Return a new Frequency that is the difference of the
        specified frequencies, f1 - f2.
        param f1 The first Frequency of the pair.
        param f2 The second Frequency of the pair.
        return A new Frequency that is the difference of the
        specified frequencies, f1 - f2.
        """
        if not (isinstance(f1, Frequency) and isinstance(f2, Frequency)):
            raise ValueError("f1 and f2 must both be Frequency instances")

        return Frequency(f1._frequency - f2._frequency)

    @staticmethod
    def multiply(f, factor):
        """
        Return a new Frequency that is the product of a specified
        frequency and some specified factor, f * factor.
        param f The base frequency
        param factor The factor that is used to multiply the value.
        return A new Frequency that is the product of a specified
        frequency and some specified factor, f * factor.
        """
        if not isinstance(f, Frequency):
            raise ValueError("f must be a Frequency")

        return Frequency(f._frequency * factor)

    @staticmethod
    def divide(f, factor):
        """
        Return a new Frequency that is a specified frequency divided by a
        specified factor, f / factor.
        param f The base frequency
        param factor The factor that is used to divide the value.
        return A new Frequency that is the product of a specified
        frequency and some specified factor, f / factor.
        """
        if not isinstance(f, Frequency):
            raise ValueError("f must be a Frequency")

        return Frequency(f._frequency / factor)

    @staticmethod
    def getInstance(stringList):
        """
        Retrieve a value from a list of strings and convert that to a Frequency

        This is used when parsing Frequency lists from an XML representation to
        eventually construct a list of Frequency instances. The string values
        are float representation of a frequency in Hertz.

        Returns a tuple of (Frequency, stringList) where Frequency is the new Frequency
        created by this call and stringList is the remaining, unused, part of
        stringList after removing the first element.
        """
        if not isinstance(stringList, list):
            raise ValueError("stringList is not a list")

        # this will raise an error if there aren't any elements on stringList
        floatVal = float(stringList[0])
        return (Frequency(floatVal), stringList[1:])

    # The frequency in hertz.
    _frequency = 0.0

    def __init__(self, value=0.0, units=None):
        """
        Create a Frequency with an initial value and units.
        The default Frequency (no arguments) is zero (0.0) HERTZ
        The default units (non specified) is HERTZ
        The units must be one of HERTZ, KILOHERTZ, MEGAHERTZ, and GIGAHERTZ.
        Any value that is not a Frequency is valid so long as it can be
        converted to a float as float(value) (including a parseable string).
        If value is a Frequency instance then this is the copy constructor and any
        value of units other than None is illegal.
        """
        if isinstance(value, Frequency):
            if units is not None:
                raise ValueError("units can not be specified with value is Frequency")
            self._frequency = value._frequency
        else:
            self.set(value, units)

    def get(self, units=None):
        """
        Return the value of this frequency as a double in the specified units.
        When units is None (the default) the returned units are HERTZ.
        param units The units in which the value of this frequency is to be returned.
        return The value of this frequency as a double in the specified units.
        Recognized units are None (HERTZ), KILOHERTZ, MEGAHERTZ, and MILIMETERS
        """
        if units is None or units == self.HERTZ:
            return self._frequency
        if units == self.KILOHERTZ:
            return self._frequency / 1000.0
        if units == self.MEGAHERTZ:
            return self._frequency / 1000000.0
        if units == self.GIGAHERTZ:
            return self._frequency / 1000000000.0

        raise ValueError(str(units) + " is not an alllowable unit.")

    def set(self, value, units=None):
        """
        Set the value of this frequency to the given value in the specified units.
        Any value is valid so long as it can be converted into a float using float(value)
        (including a parseable string).
        The units is a string arguments that defaults to HERTZ as definied here.
        Recognized units are HERTZ, KILOHERTZ, MEGAHERTS, and GIGAHERTS (also definied here).
        """

        # make sure that this is a float (in case it's an int or a string, possibly
        # other types would work so long as this produces a float without an exception
        value = float(value)

        if units is None or units == self.HERTZ:
            self._frequency = value
        elif units == self.KILOHERTZ:
            self._frequency = value * 1000.0
        elif units == self.MEGAHERTZ:
            self._frequency = value * 1000000.0
        elif units == self.GIGAHERTZ:
            self._frequency = value * 1000000000.0
        else:
            raise ValueError(str(units) + " is not an alllowable unit.")

    def __str__(self):
        """
        Return the value of this frequency as a string in the default units of Hertz.
        """
        return str(self.get())

    @staticmethod
    def values(items):
        """
        return a list of floats containing the value of the list of Frequency objects
        passed in the items argument.
        items may also be a list of lists(2D array) of Frequency objects. If the
        first item is a list then this method assumes that items is a list of lists
        and the return value is a list of lists of floats.
        The list of lists case is done by calling this method recursively and so it
        should work for higher orders of lists of lists. That use case is not tested.
        """
        result = []
        if isinstance(items[0], list):
            # this is a list of lists, assume they are all lists
            for item in items:
                thisResult = Frequency.values(item)
                result.append(thisResult)
        else:
            if not isinstance(items[0], Frequency):
                raise ValueError("items must contain Frequency instances")
            # only check the first item
            for item in items:
                result.append(item.get())
        return result

    def toBin(self, eos):
        """
        Write this Frequency out, in Hertz, to a EndianOutput.
        """
        eos.writeDouble(self.get())

    @staticmethod
    def listToBin(frequencyList, eos):
        """
        Write a list of Frequency to the EndianOutput.
        The list may have 1, 2 or 3 dimensions.
        """
        if not isinstance(frequencyList, list):
            raise ValueError("frequencyList is not a list")

        # this is used to determine the number of dimensions
        listDims = pyasdm.utils.getListDims(frequencyList)
        ndims = len(listDims)
        if ndims == 1:
            Frequency.listTo1DBin(frequencyList, eos)
        elif ndims == 2:
            Frequency.listTo2DBin(frequencyList, eos)
        elif ndims == 3:
            Frequency.listTo3DBin(frequencyList, eos)
        else:
            raise ValueError(
                "unsupport number of dimensions in frequencyList in Frequency.listToBin : "
                + str(ndims)
            )

    @staticmethod
    def listTo1DBin(frequencyList, eos):
        """
        Write a 1D list of Frequency to the EndianOutput
        """
        if not isinstance(frequencyList, list):
            raise ValueError("frequencyList is not a list")

        # ndim is always written, even for 0-element lists
        eos.writeInt(len(frequencyList))

        # only check the first value
        if (len(frequencyList) > 0) and not isinstance(frequencyList[0], Frequency):
            raise (ValueError("frequencyList is not a list of Frequency"))

        for thisFrequency in frequencyList:
            thisFrequency.toBin(eos)

    @staticmethod
    def listTo2DBin(frequencyList, eos):
        """
        Write a 2D list of Frequency to the EndianOutput
        """
        if not isinstance(frequencyList, list):
            raise ValueError("frequencyList is not a list")

        ndim1 = len(frequencyList)
        ndim2 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(frequencyList[0], list):
                raise ValueError("frequencyList is not a 2D")

            ndim2 = len(frequencyList[0])
            if ndim2 > 0 and not isinstance(frequencyList[0][0], Frequency):
                raise ValueError("frequencyListis a not a 2D list of Frequency")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)

        for thisList in frequencyList:
            for thisFrequency in thisList:
                thisFrequency.toBin(eos)

    @staticmethod
    def listTo3DBin(frequencyList, eos):
        """
        Write a 3D list of Frequency to the EndianOutput
        """
        if not isinstance(frequencyList, list):
            raise ValueError("frequencyList is not a list")

        ndim1 = len(frequencyList)
        ndim2 = 0
        ndim3 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(frequencyList[0], list):
                raise ValueError("frequencyList is not a 3D list")

            ndim2 = len(frequencyList[0])
            if ndim2 > 0:
                if not isinstance(frequencyList[0][0], list):
                    raise ValueError("frequencyList is a not a 3D list")
                ndim3 = len(frequencyList[0][0])
                if (ndim3 > 0) and not isinstance(frequencyList[0][0][0], Frequency):
                    raise ValueError("frequencyList is not a 3D list of Frequency")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)
        eos.writeInt(ndim3)

        for thisList in frequencyList:
            for middleList in thisList:
                for thisFrequency in middleList:
                    thisFrequency.toBin(eos)

    @staticmethod
    def fromBin(eis):
        """
        Read the binary representation of an Frequency, in Hertz,
        from an EndianInput instance and use the read value to set a
        Frequency.

        return a Frequency
        """
        return Frequency(eis.readDouble())

    @staticmethod
    def from1DBin(eis):
        """
        Read a list of binary Frequency values, in Hertz, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        result = []
        for i in range(dim1):
            result.append(Frequency.fromBin(eis))

        return result

    @staticmethod
    def from2DBin(eis):
        """
        Read a 2D list of binary Frequency values, in Hertz, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        dim2 = eis.readInt()
        result = []
        for i in range(dim1):
            innerList = []
            for j in range(dim2):
                innerList.append(Frequency.fromBin(eis))
            result.append(innerList)

        return result

    @staticmethod
    def from3DBin(eis):
        """
        Read a 3D list of binary Frequency values, in Hertz, from an
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
                    innerList.append(Frequency.fromBin(eis))
                middleList.append(innerList)
            result.append(middleList)

        return result

    def equals(self, otherFrequency):
        """
        Return True if and only if the specified other frequency is a
        Frequency and its value is equal to this frequency.
        param otherFrequency The other frequency to which this frequency
        is being compared.
        return True if and only if the specified other frequency is an
        Frequency and its value is equal to this frequency.
        """
        return isinstance(otherFrequency, Frequency) and (
            self._frequency == otherFrequency._frequency
        )

    def almostEquals(self, otherFrequency, toleranceFrequency):
        """
        Return True if and only if otherFrequency and toleranceFrequency are both Frequency
        instances are if the absolute value of the difference between this and otherFrequency
        is less than the absolute value of toleranceFrequency.
        """
        result = False
        if isinstance(otherFrequency, Frequency) and isinstance(
            toleranceFrequency, Frequency
        ):
            result = abs(self._frequency - otherFrequency._frequency) <= abs(
                toleranceFrequency._frequency
            )

        return result

    def isZero(self):
        """
        Return True if and only if this frequency is zero (0.0).
        """
        return self._frequency == 0.0

    def compareTo(self, otherFrequency):
        """
        Compare this Frequency to the specified otherFrequencyt, which must be
        a Frequency, returning -1, 0, or +1 if this frequency is less
        than, equal to, or greater than the specified other Frequency.
        """
        if not isinstance(otherFrequency, Frequency):
            raise ("Attempt to compare a Frequency to a non-Frequency.")

        result = 0
        if self._frequency < otherFrequency._frequency:
            result = -1
        if self._frequency > otherFrequency._frequency:
            result = 1

        return result

    def __eq__(self, otherFrequency):
        """
        Return True if and only if this Frequency is equal to the specified
        other Frequency.
        This is equivalent to the equals method.
        """
        return self.equals(otherFrequency)

    def __ne__(self, otherFrequency):
        """
        Return True if and only if this Frequency is not equal to the specified
        other Frequency.
        """
        return isinstance(otherFrequency, Frequency) and (
            self._frequency != otherFrequency._frequency
        )

    def __lt__(self, otherFrequency):
        """
        Return True if and only if this Frequency is less than the specified
        other Frequency.
        """
        return isinstance(otherFrequency, Frequency) and (
            self._frequency < otherFrequency._frequency
        )

    def __le__(self, otherFrequency):
        """
        Return True if and only if this Frequency is less than or equal to
        the specified other Frequency.
        """
        return isinstance(otherFrequency, Frequency) and (
            self._frequency <= otherFrequency._frequency
        )

    def __gt__(self, otherFrequency):
        """
        Return True if and only if this Frequency is greater than the specified
        other Frequency.
        """
        return isinstance(otherFrequency, Frequency) and (
            self._frequency > otherFrequency._frequency
        )

    def __ge__(self, otherFrequency):
        """
        Return True if and only if this Frequency is greater than or equal to
        the specified other Frequency.
        """
        return isinstance(otherFrequency, Frequency) and (
            self._frequency >= otherFrequency._frequency
        )

    def __add__(self, otherFrequency):
        """
        Add otherFrequency, which must be a Frequency, to this frequency, (this + x).
        param otherFreqency The Frequency to be added to this frequency.
        return This frequency after the addition.
        """
        if not isinstance(otherFrequency, Frequency):
            raise ValueError("Attempt to add a non-Frequency to a Frequency")

        self._frequency += otherFrequency._frequency
        return self

    def __sub__(self, otherFrequency):
        """
        Subtract otherFrequency which must be a Frequency, from this frequency, (this - x).
        param otherFrequency The Frequency to be subtracted from this frequency.
        return This frequency after the subtraction.
        """
        if not isinstance(otherFrequency, Frequency):
            raise ValueError("Attempt to subtract a non-Frequency from a Frequency")

        self._frequency -= otherFrequency._frequency
        return self

    def __mul__(self, factor):
        """
        Multiply this frequency by some factor, (this * factor).
        param factor The factor by which this frequency is to be multiplied.
        return This frequency after the multiplication.
        """
        self._frequency *= factor
        return self

    def __truediv__(self, factor):
        """
        Divide this frequency by some factor, (this / factor).
        param factor The factor by which this frequency is to be divided.
        return This frequency after the division.
        """
        self._frequency /= factor
        return self
