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
# File Speed.py
#


class Speed:
    """
    The Speed class implements a concept of an atmospheric speed in meters per second.

    This version adapted from the c++ and java implementations, originall authored by Allen Farris.
    """

    @staticmethod
    def sum(a, b):
        """
        Return a new Speed that is the sum of the
        specified Speeds, a +  b.
        param a The first Speed of the pair.
        param b The second Speed of the pair.
        return A new Speed that is the sum of the
        specified Speeds, a +  b.
        """
        if not (isinstance(a, Speed) and isinstance(b, Speed)):
            raise ValueError("a and b must both be Speed instances")

        return Speed(a._speed + b._speed)

    @staticmethod
    def subtract(a, b):
        """
        Return a new Speed that is the difference of the
        specified Speeds, a - b.
        param a The first Speed of the pair.
        param b The second Speed of the pair.
        return A new Speed that is the difference of the
        specified Speeds, a - b.
        """
        if not (isinstance(a, Speed) and isinstance(b, Speed)):
            raise ValueError("a and b must both be Speed instances")

        return Speed(a._speed - b._speed)

    @staticmethod
    def multiply(a, factor):
        """
        Return a new Speed that is the product of a specified
        speed and some specified factor, a * factor.
        param a The base speed
        param factor The factor that is used to multiply the value.
        return A new Speed that is the product of a specified
        speed and some specified factor, a * factor.
        """
        if not isinstance(a, Speed):
            raise ValueError("a must be a Speed")

        return Speed(a._speed * factor)

    @staticmethod
    def divide(a, factor):
        """
        Return a new Speed that is a specified speed divided by a
        specified factor, a / factor.
        param a The base speed
        param factor The factor that is used to divide the value.
        return A new Speed that is the product of a specified
        speed and some specified factor, a / factor.
        """
        if not isinstance(a, Speed):
            raise ValueError("a must be a Speed")

        return Speed(a._speed / factor)

    @staticmethod
    def getInstance(stringList):
        """
        Retrieve a value from a list of strings and convert that to a Speed

        This is used when parsing Speed lists from an XML representation to
        eventually construct a list of Speed instances. The string values
        are float representation of a speed in meters per second.

        Returns a tuple of (Speed, stringList) where Speed is the new Speed
        created by this call and stringList is the remaining, unused, part of
        stringList after removing the first element.
        """
        if not isinstance(stringList, list):
            raise ValueError("stringList is not a list")

        # this will raise an error if there aren't any elements on stringList
        floatVal = float(stringList[0])
        return (Speed(floatVal), stringList[1:])

    # The speed in meters per second.
    _speed = 0.0

    def __init__(self, speed=0.0):
        """
        Create a Speed with an initial value in meters per second.
        The default Speed (no arguments) is zero (0.0) meters per second.
        Any speed that is not a Speed is valid so long as it can be
        converted to a float as float(speed) (including a parseable string).
        If speed is a Speed instance then this is the copy constructor.
        """
        if isinstance(speed, Speed):
            self._speed = speed._speed
        else:
            self.set(speed)

    def get(self):
        """
        Return the value of this speed as a double in meters per second.
        """
        return self._speed

    def set(self, speed):
        """
        Set the value of this speed to the specified speed in meters per second.
        Any speed is valid so long as it can be converted into a float using float(speed)
        (including a parseable string).
        """
        self._speed = float(speed)

    def toString(self):
        """
        Return the value of this speed as a String in units of meters per second.
        """
        return str(self.get())

    @staticmethod
    def values(items):
        """
        return a list of floats containing the value of the list of Speed objects
        passed in the items argument.
        items may also be a list of lists(2D array) of Speed objects. If the
        first item is a list then this method assumes that items is a list of lists
        and the return value is a list of lists of floats.
        The list of lists case is done by calling this method recursively and so it
        should work for higher orders of lists of lists. That use case is not tested.
        """
        result = []
        if isinstance(items[0], list):
            # this is a list of lists, assume they are all lists
            for item in items:
                thisResult = Speed.values(item)
                result.append(thisResult)
        else:
            if not isinstance(items[0], Speed):
                raise ValueError("items must contain Speed instances")
            # only check the first item
            for item in items:
                result.append(item.get())
        return result

    def toBin(self):
        # it also needs a static method to send a list of speed items toBin
        # should also work for 2D, 3D lists
        raise RuntimeError("Speed.toBin is not yet implemented")

    def fromBin(self):
        raise RuntimeError("Speed.fromBin is not yet implemented")

    def from1DBin(self):
        raise RuntimeError("Speed.from1DBin is not yet implemented")

    def from2DBin(self):
        raise RuntimeError("Speed.from2DBin is not yet implemented")

    def from3DBin(self):
        raise RuntimeError("Speed.from2DBin is not yet implemented")

    def equals(self, otherSpeed):
        """
        Return True if and only if the specified other speed is a
        Speed and its value is equal to this speed.
        param otherSpeed The other speed to which this speed
        is being compared.
        return True if and only if the specified other speed is an
        Speed and its value is equal to this speed.
        """
        return isinstance(otherSpeed, Speed) and (self._speed == otherSpeed._speed)

    def almostEquals(self, otherSpeed, toleranceSpeed):
        """
        Return True if and only if otherSpeed and toleranceSpeed are both Speed
        instances are if the absolute value of the difference between this and otherSpeed
        is less than the absolute value of toleranceSpeed.
        """
        result = False
        if isinstance(otherSpeed, Speed) and isinstance(toleranceSpeed, Speed):
            result = abs(self._speed - otherSpeed._speed) <= abs(toleranceSpeed._speed)

        return result

    def isZero(self):
        """
        Return True if and only if this speed is zero (0.0).
        """
        return self._speed == 0.0

    def compareTo(self, otherSpeed):
        """
        Compare this Speed to the specified otherSpeedt, which must be
        a Speed, returning -1, 0, or +1 if this speed is less
        than, equal to, or greater than the specified other Speed.
        """
        if not isinstance(otherSpeed, Speed):
            raise ("Attempt to compare a Speed to a non-Speed.")

        result = 0
        if self._speed < otherSpeed._speed:
            result = -1
        if self._speed > otherSpeed._speed:
            result = 1

        return result

    def eq(self, otherSpeed):
        """
        Return True if and only if this Speed is equal to the specified
        other Speed.
        This is equivalent to the equals method.
        """
        return self.equals(otherSpeed)

    def ne(self, otherSpeed):
        """
        Return True if and only if this Speed is not equal to the specified
        other Speed.
        """
        return isinstance(otherSpeed, Speed) and (self._speed != otherSpeed._speed)

    def lt(self, otherSpeed):
        """
        Return True if and only if this Speed is less than the specified
        other Speed.
        """
        return isinstance(otherSpeed, Speed) and (self._speed < otherSpeed._speed)

    def le(self, otherSpeed):
        """
        Return True if and only if this Speed is less than or equal to
        the specified other Speed.
        """
        return isinstance(otherSpeed, Speed) and (self._speed <= otherSpeed._speed)

    def gt(self, otherSpeed):
        """
        Return True if and only if this Speed is greater than the specified
        other Speed.
        """
        return isinstance(otherSpeed, Speed) and (self._speed > otherSpeed._speed)

    def ge(self, otherSpeed):
        """
        Return True if and only if this Speed is greater than or equal to
        the specified other Speed.
        """
        return isinstance(otherSpeed, Speed) and (self._speed >= otherSpeed._speed)

    def add(self, otherSpeed):
        """
        Add otherSpeed, which must be a Speed, to this speed, (this + x).
        param otherSpeed The Speed to be added to this speed.
        return This speed after the addition.
        """
        if not isinstance(otherSpeed, Speed):
            raise ValueError("Attempt to add a non-Speed to a Speed")

        self._speed += otherSpeed._speed
        return self

    def sub(self, otherSpeed):
        """
        Subtract otherSpeed which must be a Speed, from this speed, (this - x).
        param otherSpeed The Speed to be subtracted from this speed.
        return This speed after the subtraction.
        """
        if not isinstance(otherSpeed, Speed):
            raise ValueError("Attempt to subtract a non-Speed from a Speed")

        self._speed -= otherSpeed._speed
        return self

    def mult(self, factor):
        """
        Multiply this speed by some factor, (this * factor).
        param factor The factor by which this speed is to be multiplied.
        return This speed after the multiplication.
        """
        self._speed *= factor
        return self

    def div(self, factor):
        """
        Divide this speed by some factor, (this / factor).
        param factor The factor by which this speed is to be divided.
        return This speed after the division.
        """
        self._speed /= factor
        return self
