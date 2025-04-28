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
# File Angle.py
#

import math
import pyasdm.utils


class Angle:
    """
    The Angle class implements a concept of an angle in radians.

    This version adapted from the c++ and java implementation originally authored by Allen Farris
    """

    # The factor by which to multiply an angle in radians to convert it to degrees.
    radToDeg = 180.0 / math.pi

    # The factor by which to mulitply an angle in radians to convert it to hours.
    radToHour = 12.0 / math.pi

    # The factor by which to multiply an angle in radians to convert it to arcseconds.
    radToArcsecond = (3600.0 * 180.0) / math.pi

    # The factor by which to multiply an angle in degress to convert it to radians.
    degToRad = math.pi / 180.0

    # The factor by which to multiple an angle in hours to convert it to radians.
    hourToRad = math.pi / 12.0

    # The factor by which to multiple an angle in arcseconds to convert it to radians.
    arcsecondToRad = math.pi / (3600.0 * 180.0)

    # Radian, rad, an allowed unit of angle.
    RADIAN = "rad"

    # Degree, deg, an allowed unit of angle.
    DEGREE = "deg"

    # Hour, hr, an allowed unit of angle.
    HOUR = "hr"

    # Arcsecond, arcsec, an allowed unit of angle.
    ARCSECOND = "arcsec"

    # A list of strings containing the allowable units of Angle.
    AllowedUnits = [RADIAN, DEGREE, HOUR, ARCSECOND]

    @staticmethod
    def unit():
        """
        Return the canonical unit associated with this Angle, radian.
        The unit associated with this Angle, always returns RADIAN.
        """
        return Angle.RADIAN

    @staticmethod
    def add(a1, a2):
        """
        Return a new Angle that is the sum of the
        specified angles, a1 +  a2.
        a1 The first Angle of the pair.
        a2 The second Angle of the pair.
        return A new Angle that is the sum of the specified angles, a1 +  a2.
        """
        if not (isinstance(a1, Angle) and isinstance(a2, Angle)):
            raise ValueError("a1 and a2 must both be Angle instances")

        return Angle(a1._angle + a2._angle)

    @staticmethod
    def subtract(a1, a2):
        """
        Return a new Angle that is the difference of the
        specified angles, a1 - a2.
        a1 The first Angle of the pair.
        a2 The second Angle of the pair.
        return A new Angle that is the difference of the specified angles, a1 - a2.
        """
        if not (isinstance(a1, Angle) and isinstance(a2, Angle)):
            raise ValueError("a1 and a2 must both be Angle instances")

        return Angle(a1._angle - a2._angle)

    @staticmethod
    def multiply(a, factor):
        """
        Return a new Angle that is the product of a specified
        angle and some specified factor, a * factor.
        a The base angle
        factor The factor that is used to multiply the value.
        return A new Angle that is the product of a specified angle
        and some specified factor, a * factor.
        """
        if not isinstance(a, Angle):
            raise ValueError("a must be an Angle")

        return Angle(a._angle * factor)

    @staticmethod
    def divide(a, factor):
        """
        Return a new Angle that is a specified angle divided by a
        specified factor, a / factor.
        a The base angle
        factor The factor that is used to divide the value.
        return A new Angle that is the quotient of a specified
        angle and some specified factor, a / factor.
        """
        if not isinstance(a, Angle):
            raise ValueError("a must be an Angle")

        return Angle(a._angle / factor)

    @staticmethod
    def getInstance(stringList):
        """
        Retrieve a value from a list of strings and convert that to an Angle.

        This is used when parsing Angle lists from an XML representation to
        eventually construct a list of Angle instances. The strings are
        float representations of the angle in radians.

        Returns a tuple of (Angle, stringList) where Angle is the new Angle
        created by this call and stringList is the remaining, unused, part of
        stringList after removing the first element.
        """
        if not isinstance(stringList, list):
            raise ValueError("stringList is not a list")

        # this will raise an error if there aren't any elements on stringList
        floatVal = float(stringList[0])
        return (Angle(floatVal), stringList[1:])

    # the angle in radians
    _angle = 0.0

    def __init__(self, value=0.0, units=None):
        """
        Create an Angle with an initial value and units.
        The default Angle (no arguments) is zero (0.0) radians.
        The default units (none specified) is RADIAN.
        The units must be one of the 4 recognized units: RADIAN,
        DEGREE, HOUR, and ARCSECOND.
        Any value that is not an Angle is valid so long as it can
        be converted to a float as float(value) (including a parseable string).
        If value is an Angle instance then this is the copy constructor
        and any value of units other than None is illegal.
        """
        if isinstance(value, Angle):
            if units is not None:
                raise ValueError("units can not be specied when value is an Angle")
            self._angle = value._angle

        else:
            self.set(value, units)

    def get(self, units=None):
        """
        Return the value of this angle in the specified units.
        When units is None (the default) the returned units are RADIAN.
        Recognized units are None (RADIAN), RADIAN, DEGREE, HOUR, and ARCSECOND.
        """
        if units is None or units == self.RADIAN:
            return self._angle
        if units == self.DEGREE:
            return self._angle * self.radToDeg
        if units == self.HOUR:
            return self._angle * self.radToHour
        if units == self.ARCSECOND:
            return self._angle * self.radToArcsecond

        raise ValueError(str(units) + " is not an allowable unit.")

    def set(self, value, units=None):
        """
        Set the value of this angle to the specified value in the specified units.
        Any value is valid so long as it can be converted into a float using float(value)
        (including a parseable string).
        The units default to RADIAN.
        Recognized units are RADIAN, DEGREE, HOUR, and ARCSECOND.
        """

        # make sure that this is a float even if value is an int or a string
        # other types might work, too
        value = float(value)

        if units is None or units == self.RADIAN:
            self._angle = value
        elif units == self.DEGREE:
            self._angle = value * self.degToRad
        elif units == self.HOUR:
            self._angle = value * self.hourToRad
        elif units == self.ARCSECOND:
            self._angle = value * self.arcsecondToRad
        else:
            raise ValueError(str(units) + " is not an allowable unit.")

    def __str__(self):
        """
        Print the value of this angle in the units of RADIAN.
        """
        return str(self.get())

    @staticmethod
    def values(items):
        """
        return a list of floats containing the value of the list of Angle objects
        passed in the items argument.
        items may also be a list of lists (2D array) of Angle objects. If the first
        item is a list then this method assumes that items is a list of list and the
        return value is a list of lists of floats.
        The list of lists case is done by calling this method recursively and so should
        work for higher levels of lists of lists. That use case is not tested.
        """
        result = []
        if isinstance(items[0], list):
            # this is a list of lists, assume they are all lists
            for item in items:
                thisResult = Angle.values(item)
                result.append(thisResult)
        else:
            # assume this is a list of Angle objects
            for item in items:
                result.append(item.get())
        return result

    def toBin(self, eos):
        """
        Write this Angle out, in radians, to a EndianOutput.
        """
        eos.writeDouble(self.get())

    @staticmethod
    def listToBin(angleList, eos):
        """
        Write a list of Angle to the EndianOutput.
        The list may have 1, 2 or 3 dimensions.
        """
        if not isinstance(angleList, list):
            raise ValueError("angleList is not a list")

        # this is used to determine the number of dimensions
        listDims = pyasdm.utils.getListDims(angleList)
        ndims = len(listDims)
        if ndims == 1:
            Angle.listTo1DBin(angleList, eos)
        elif ndims == 2:
            Angle.listTo2DBin(angleList, eos)
        elif ndims == 3:
            Angle.listTo3DBin(angleList, eos)
        else:
            raise ValueError(
                "unsupport number of dimensions in angleList in Angle.listToBin : "
                + str(ndims)
            )

    @staticmethod
    def listTo1DBin(angleList, eos):
        """
        Write a 1D list of Angle to the EndianOutput
        """
        if not isinstance(angleList, list):
            raise ValueError("angleList is not a list")

        # ndim is always written, even for 0-element lists
        eos.writeInt(len(angleList))

        # only check the first value
        if (len(angleList) > 0) and not isinstance(angleList[0], Angle):
            raise (ValueError("angleList is not a list of Angle"))

        for thisAngle in angleList:
            thisAngle.toBin(eos)

    @staticmethod
    def listTo2DBin(angleList, eos):
        """
        Write a 2D list of Angle to the EndianOutput
        """
        if not isinstance(angleList, list):
            raise ValueError("angleList is not a list")

        ndim1 = len(angleList)
        ndim2 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(angleList[0], list):
                raise ValueError("angleList is not a 2D")

            ndim2 = len(angleList[0])
            if ndim2 > 0 and not isinstance(angleList[0][0], Angle):
                raise ValueError("angleListis a not a 2D list of Angle")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)

        for thisList in angleList:
            for thisAngle in thisList:
                thisAngle.toBin(eos)

    @staticmethod
    def listTo3DBin(angleList, eos):
        """
        Write a 3D list of Angle to the EndianOutput
        """
        if not isinstance(angleList, list):
            raise ValueError("angleList is not a list")

        ndim1 = len(angleList)
        ndim2 = 0
        ndim3 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(angleList[0], list):
                raise ValueError("angleList is not a 3D list")

            ndim2 = len(angleList[0])
            if ndim2 > 0:
                if not isinstance(angleList[0][0], list):
                    raise ValueError("angleList is a not a 3D list")
                ndim3 = len(angleList[0][0])
                if (ndim3 > 0) and not isinstance(angleList[0][0][0], Angle):
                    raise ValueError("angleList is not a 3D list of Angle")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)
        eos.writeInt(ndim3)

        for thisList in angleList:
            for middleList in thisList:
                for thisAngle in middleList:
                    thisAngle.toBin(eos)

    @staticmethod
    def fromBin(eis):
        """
        Read the binary representation of an Angle, in radians,
        from an EndianInput instance and use the read value to set an
        Angle.

        return an Angle
        """
        return Angle(eis.readDouble())

    @staticmethod
    def from1DBin(eis):
        """
        Read a list of binary Angle values, in radians, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        result = []
        for i in range(dim1):
            result.append(Angle.fromBin(eis))

        return result

    @staticmethod
    def from2DBin(eis):
        """
        Read a 2D list of binary Angle values, in radians, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        dim2 = eis.readInt()
        result = []
        for i in range(dim1):
            innerList = []
            for j in range(dim2):
                innerList.append(Angle.fromBin(eis))
            result.append(innerList)

        return result

    @staticmethod
    def from3Dbin(eis):
        """
        Read a 3D list of binary Angle values, in radians, from an
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
                    innerList.append(Angle.fromBin(eis))
                middleList.append(innerList)
            result.append(middleList)

        return result

    def equals(self, otherAngle):
        """
        Returns True if and only if the specified other angle has
        a value that is equal to this angle.
        """
        return isinstance(otherAngle, Angle) and (self._angle == otherAngle._angle)

    def almostEquals(self, otherAngle, toleranceAngle):
        """
        Returns True if and only if otherAngle and toleranceAngle are both Angles
        and if the distance (absolute value of the difference) between this Angle
        and otherAngle is less than the absolute value of toleranceAngle.
        """
        result = False
        if isinstance(otherAngle, Angle) and isinstance(toleranceAngle, Angle):
            result = abs(self._angle - otherAngle._angle) <= abs(toleranceAngle._angle)

        return result

    def isZero(self):
        """
        Return True if and only if this angle is zero (0.0).
        """
        return self._angle == 0.0

    def compareTo(self, otherAngle):
        """
        Compare this Angle to the specified otherAngle, which must be an Angle.
        Returning -1, 0, or +1 if this Angle is less than, equal to, or greater
        than the other Angle.
        """
        if not isinstance(otherAngle, Angle):
            raise ValueError("otherAngle must be an Angle")

        result = 0
        if self._angle < otherAngle._angle:
            result = -1
        elif self._angle > otherAngle._angle:
            result = 1

        return result

    def __eq__(self, otherAngle):
        """
        Returns True if and only if this Angle is equal to the otherAngle.
        This is equivalent to the equals method.
        """
        return self.equals(otherAngle)

    def __ne__(self, otherAngle):
        """
        Returns True if and only if this Angle is not equal to otherAngle
        """
        return isinstance(otherAngle, Angle) and (self._angle != otherAngle._angle)

    def __lt__(self, otherAngle):
        """
        Returns True if and only if this Angle is less than otherAngle
        """
        return isinstance(otherAngle, Angle) and (self._angle < otherAngle._angle)

    def __le__(self, otherAngle):
        """
        Returns True if and only if this Angle is less than or equal to otherAngle
        """
        return isinstance(otherAngle, Angle) and (self._angle <= otherAngle._angle)

    def __gt__(self, otherAngle):
        """
        Returns True if and only if this angle is greater than otherAngle
        """
        return isinstance(otherAngle, Angle) and (self._angle > otherAngle._angle)

    def __ge__(self, otherAngle):
        """
        Returns True if and only if this angle is greater than or equal to otherAngle
        """
        return isinstance(otherAngle, Angle) and (self._angle >= otherAngle._angle)

    def __mul__(self, factor):
        """
        Multiply this angle by some factor, (this * factor).
        Return this angle after multiplication.
        """
        self._angle *= factor
        return self

    def __truediv__(self, factor):
        """
        Divide this angle by some factor, (this / factor)
        Return this angle after division.
        """
        self._angle /= factor
        return self

    def sin(self):
        """
        Return the trigonometric sine of this angle.
        """
        return math.sin(self._angle)

    def cos(self):
        """
        Return the trigonometric cosine of this angle.
        """
        return math.cos(self._angle)

    def tan(self):
        """
        Return the trigonometric tangent of this angle.
        """
        return math.tan(self._angle)

    def asin(self):
        """
        Return the arc sine of this angle, in the range of -<i>pi</i>/2 through <i>pi</i>/2.
        """
        return math.asin(self._angle)

    def acos(self):
        """
        Return the arc cosine of this angle, in the range of 0.0 through <i>pi</i>.
        """
        return math.acos(self._angle)

    def atan(self):
        """
        Return the arc tangent of this angle, in the range of -<i>pi</i>/2 through <i>pi</i>/2.
        """
        return math.atan(self._angle)
