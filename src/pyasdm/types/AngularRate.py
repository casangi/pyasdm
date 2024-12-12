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
# File AngularRate.py
#


class AngularRate:
    """
    The AngularRate class implements a concept of a angular speed in radians per second.

    This version adapted from the c++ and java implementations, originall authored by Allen Farris.
    """

    @staticmethod
    def sum(a, b):
        """
        Return a new AngularRate that is the sum of the
        specified AngularRates, a +  b.
        param a The first AngularRate of the pair.
        param b The second AngularRate of the pair.
        return A new AngularRate that is the sum of the
        specified AngularRates, a +  b.
        """
        if not (isinstance(a, AngularRate) and isinstance(b, AngularRate)):
            raise ValueError("a and b must both be AngularRate instances")

        return AngularRate(a._rate + b._rate)

    @staticmethod
    def subtract(a, b):
        """
        Return a new AngularRate that is the difference of the
        specified AngularRate, a - b.
        param a The first AngularRate of the pair.
        param b The second AngularRate of the pair.
        return A new AngularRate that is the difference of the
        specified AngularRates, a - b.
        """
        if not (isinstance(a, AngularRate) and isinstance(b, AngularRate)):
            raise ValueError("a and b must both be AngularRate instances")

        return AngularRate(a._rate - b._rate)

    @staticmethod
    def multiply(a, factor):
        """
        Return a new AngularRate that is the product of a specified
        angular rate and some specified factor, a * factor.
        param a The base angular rate
        param factor The factor that is used to multiply the value.
        return A new AngularRate that is the product of a specified
        angular rate and some specified factor, a * factor.
        """
        if not isinstance(a, AngularRate):
            raise ValueError("a must be a AngularRate")

        return AngularRate(a._rate * factor)

    @staticmethod
    def divide(a, factor):
        """
        Return a new AngularRate that is a specified angular rate divided by a
        specified factor, a / factor.
        param a The base angular rate
        param factor The factor that is used to divide the value.
        return A new AngularRate that is the product of a specified
        angular rate and some specified factor, a / factor.
        """
        if not isinstance(a, AngularRate):
            raise ValueError("a must be a AngularRate")

        return AngularRate(a._rate / factor)

    @staticmethod
    def getInstance(stringList):
        """
        Retrieve a value from a list of strings and convert that to an AngularRate

        This is used when parsing AngularRate lists from an XML representation to
        eventually construct a list of AngularRate instances. The string values
        are float representation of an angular rate in radians per second.

        Returns a tuple of (AngularRate, stringList) where AngularRate is the new AngularRate
        created by this call and stringList is the remaining, unused, part of
        stringList after removing the first element.
        """
        if not isinstance(stringList, list):
            raise ValueError("stringList is not a list")

        # this will raise an error if there aren't any elements on stringList
        floatVal = float(stringList[0])
        return (AngularRate(floatVal), stringList[1:])

    # The angular rate in radians per second
    _rate = 0.0

    def __init__(self, rate=0.0):
        """
        Create a AngularRate with an initial angular rate in radians per second.
        The default AngularRate (no arguments) is zero (0.0) radians per second.
        Any rate that is not a AngularRate is valid so long as it can be
        converted to a float as float(rate) (including a parseable string).
        If rate is a AngularRate instance then this is the copy constructor.
        """
        if isinstance(rate, AngularRate):
            self._rate = rate._rate
        else:
            self.set(rate)

    def get(self):
        """
        Return the value of this rate as a double in hectopascals.
        """
        return self._rate

    def set(self, rate):
        """
        Set the value of this angular rate to the specified angular rate in radians per second.
        Any rate is valid so long as it can be converted into a float using float(rate)
        (including a parseable string).
        """
        self._rate = float(rate)

    def toString(self):
        """
        Return the value of this angular rate as a String in units of radians per second.
        """
        return str(self.get())

    @staticmethod
    def values(items):
        """
        return a list of floats containing the value of the list of AngularRate objects
        passed in the items argument.
        items may also be a list of lists(2D array) of AngularRate objects. If the
        first item is a list then this method assumes that items is a list of lists
        and the return value is a list of lists of floats.
        The list of lists case is done by calling this method recursively and so it
        should work for higher orders of lists of lists. That use case is not tested.
        """
        result = []
        if isinstance(items[0], list):
            # this is a list of lists, assume they are all lists
            for item in items:
                thisResult = AngularRate.values(item)
                result.append(thisResult)
        else:
            if not isinstance(items[0], AngularRate):
                raise ValueError("items must contain AngularRate instances")
            # only check the first item
            for item in items:
                result.append(item.get())
        return result

    def toBin(self):
        # it also needs a static method to send a list of rate items toBin
        # should also work for 2D, 3D lists
        raise RuntimeError("AngularRate.toBin is not yet implemented")

    def fromBin(self):
        raise RuntimeError("AngularRate.fromBin is not yet implemented")

    def from1DBin(self):
        raise RuntimeError("AngularRate.from1DBin is not yet implemented")

    def from2DBin(self):
        raise RuntimeError("AngularRate.from2DBin is not yet implemented")

    def from3DBin(self):
        raise RuntimeError("AngularRate.from2DBin is not yet implemented")

    def equals(self, otherAngularRate):
        """
        Return True if and only if the specified other angular rate is a
        AngularRate and its value is equal to this angular rate.
        param otherAngularRate The other angular rate to which this angular rate
        is being compared.
        return True if and only if the specified other angular rate is an
        AngularRate and its value is equal to this angular rate.
        """
        return isinstance(otherAngularRate, AngularRate) and (
            self._rate == otherAngularRate._rate
        )

    def almostEquals(self, otherAngularRate, toleranceAngularRate):
        """
        Return True if and only if otherAngularRate and toleranceAngularRate are both AngularRate
        instances are the absolute value of the difference between this and otherAngularRate
        is less than the absolute value of toleranceAngularRate.
        """
        result = False
        if isinstance(otherAngularRate, AngularRate) and isinstance(
            toleranceAngularRate, AngularRate
        ):
            result = abs(self._rate - otherAngularRate._rate) <= abs(
                toleranceAngularRate._rate
            )

        return result

    def isZero(self):
        """
        Return True if and only if this angular rate is zero (0.0).
        """
        return self._rate == 0.0

    def compareTo(self, otherAngularRate):
        """
        Compare this AngularRate to the specified otherAngularRate, which must be
        a AngularRate, returning -1, 0, or +1 if this rate is less
        than, equal to, or greater than the specified other AngularRate.
        """
        if not isinstance(otherAngularRate, AngularRate):
            raise ("Attempt to compare a AngularRate to a non-AngularRate.")

        result = 0
        if self._rate < otherAngularRate._rate:
            result = -1
        if self._rate > otherAngularRate._rate:
            result = 1

        return result

    def eq(self, otherAngularRate):
        """
        Return True if and only if this AngularRate is equal to the specified
        other AngularRate.
        This is equivalent to the equals method.
        """
        return self.equals(otherAngularRate)

    def ne(self, otherAngularRate):
        """
        Return True if and only if this AngularRate is not equal to the specified
        other AngularRate.
        """
        return isinstance(otherAngularRate, AngularRate) and (
            self._rate != otherAngularRate._rate
        )

    def lt(self, otherAngularRate):
        """
        Return True if and only if this AngularRate is less than the specified
        other AngularRate.
        """
        return isinstance(otherAngularRate, AngularRate) and (
            self._rate < otherAngularRate._rate
        )

    def le(self, otherAngularRate):
        """
        Return True if and only if this AngularRate is less than or equal to
        the specified other AngularRate.
        """
        return isinstance(otherAngularRate, AngularRate) and (
            self._rate <= otherAngularRate._rate
        )

    def gt(self, otherAngularRate):
        """
        Return True if and only if this AngularRate is greater than the specified
        other AngularRate.
        """
        return isinstance(otherAngularRate, AngularRate) and (
            self._rate > otherAngularRate._rate
        )

    def ge(self, otherAngularRate):
        """
        Return True if and only if this AngularRate is greater than or equal to
        the specified other AngularRate.
        """
        return isinstance(otherAngularRate, AngularRate) and (
            self._rate >= otherAngularRate._rate
        )

    def add(self, otherAngularRate):
        """
        Add otherAngularRate, which must be a AngularRate, to this angular rate, (this + x).
        param otherAngularRate The AngularRate to be added to this rate.
        return This angular rate after the addition.
        """
        if not isinstance(otherAngularRate, AngularRate):
            raise ValueError("Attempt to add a non-AngularRate to a AngularRate")

        self._rate += otherAngularRate._rate
        return self

    def sub(self, otherAngularRate):
        """
        Subtract otherAngularRate which must be a AngularRate, from this angular rate, (this - x).
        param otherAngularRate The AngularRate to be subtracted from this angular rate.
        return This angular rate after the subtraction.
        """
        if not isinstance(otherAngularRate, AngularRate):
            raise ValueError("Attempt to subtract a non-AngularRate from a AngularRate")

        self._rate -= otherAngularRate._rate
        return self

    def mult(self, factor):
        """
        Multiply this angular rate by some factor, (this * factor).
        param factor The factor by which this angular rate is to be multiplied.
        return This angular rate after the multiplication.
        """
        self._rate *= factor
        return self

    def div(self, factor):
        """
        Divide this angular rate by some factor, (this / factor).
        param factor The factor by which this angular rate is to be divided.
        return This angular rate after the division.
        """
        self._rate /= factor
        return self
