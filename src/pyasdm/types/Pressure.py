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

    def toString(self):
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

    def toBin(self):
        # it also needs a static method to send a list of pressure items toBin
        # should also work for 2D, 3D lists
        raise RuntimeError("Pressure.toBin is not yet implemented")

    def fromBin(self):
        raise RuntimeError("Pressure.fromBin is not yet implemented")

    def from1DBin(self):
        raise RuntimeError("Pressure.from1DBin is not yet implemented")

    def from2DBin(self):
        raise RuntimeError("Pressure.from2DBin is not yet implemented")

    def from3DBin(self):
        raise RuntimeError("Pressure.from2DBin is not yet implemented")

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

    def eq(self, otherPressure):
        """
        Return True if and only if this Pressure is equal to the specified
        other Pressure.
        This is equivalent to the equals method.
        """
        return self.equals(otherPressure)

    def ne(self, otherPressure):
        """
        Return True if and only if this Pressure is not equal to the specified
        other Pressure.
        """
        return isinstance(otherPressure, Pressure) and (
            self._pressure != otherPressure._pressure
        )

    def lt(self, otherPressure):
        """
        Return True if and only if this Pressure is less than the specified
        other Pressure.
        """
        return isinstance(otherPressure, Pressure) and (
            self._pressure < otherPressure._pressure
        )

    def le(self, otherPressure):
        """
        Return True if and only if this Pressure is less than or equal to
        the specified other Pressure.
        """
        return isinstance(otherPressure, Pressure) and (
            self._pressure <= otherPressure._pressure
        )

    def gt(self, otherPressure):
        """
        Return True if and only if this Pressure is greater than the specified
        other Pressure.
        """
        return isinstance(otherPressure, Pressure) and (
            self._pressure > otherPressure._pressure
        )

    def ge(self, otherPressure):
        """
        Return True if and only if this Pressure is greater than or equal to
        the specified other Pressure.
        """
        return isinstance(otherPressure, Pressure) and (
            self._pressure >= otherPressure._pressure
        )

    def add(self, otherPressure):
        """
        Add otherPressure, which must be a Pressure, to this pressure, (this + x).
        param otherPressure The Pressure to be added to this pressure.
        return This pressure after the addition.
        """
        if not isinstance(otherPressure, Pressure):
            raise ValueError("Attempt to add a non-Pressure to a Pressure")

        self._pressure += otherPressure._pressure
        return self

    def sub(self, otherPressure):
        """
        Subtract otherPressure which must be a Pressure, from this pressure, (this - x).
        param otherPressure The Pressure to be subtracted from this pressure.
        return This pressure after the subtraction.
        """
        if not isinstance(otherPressure, Pressure):
            raise ValueError("Attempt to subtract a non-Pressure from a Pressure")

        self._pressure -= otherPressure._pressure
        return self

    def mult(self, factor):
        """
        Multiply this pressure by some factor, (this * factor).
        param factor The factor by which this pressure is to be multiplied.
        return This pressure after the multiplication.
        """
        self._pressure *= factor
        return self

    def div(self, factor):
        """
        Divide this pressure by some factor, (this / factor).
        param factor The factor by which this pressure is to be divided.
        return This pressure after the division.
        """
        self._pressure /= factor
        return self
