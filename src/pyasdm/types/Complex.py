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
# File Complex.py
#

import pyasdm.utils


class Complex:
    """
    The Complex class implements a complex number.

    This version adapted from the c++ and java implementations, originall authored by Allen Farris.
    """

    @staticmethod
    def sum(a, b):
        """
        Return a new complex number that is the sum of the two specified
        complex numbers, a +  b.
        param a The first complex of the pair.
        param b The second complex of the pair.
        return A new Complex number that is the sum of the two specified
        complex numbers, a +  b.
        """
        if not (isinstance(a, Complex) and isinstance(b, Complex)):
            raise ValueError("a and b must both be Complex instances")

        result = Complex(a)
        result.add(b)
        return result

    @staticmethod
    def subtract(a, b):
        """
        Return a new complex number that is the difference of the two specified
        complex numbers, a - b.
        param a The first complex of the pair.
        param b The second complex of the pair.
        return A new Complex number that is the difference of the specified
        complex numbers, a - b.
        """
        if not (isinstance(a, Complex) and isinstance(b, Complex)):
            raise ValueError("a and b must both be Complex instances")

        result = Complex(a)
        result.sub(b)
        return result

    @staticmethod
    def multiply(a, b):
        """
        Return a new complex number that is the product of the two specified
        complex numbers, a * b
        param a The first complex number of the pair.
        param b The second complex number of the pair.
        return A new Complex number that is the product of the two specified
        complex numbers, a * b
        """
        if not (isinstance(a, Complex) and isinstance(b, Complex)):
            raise ValueError("a and b must both be Complex instances")

        result = Complex(a)
        result.mult(b)
        return result

    @staticmethod
    def divide(a, b):
        """
        Return a new complex number that is "a / b".
        param a The first complex number of the pair.
        param b The second complex number of the pair.
        return a new Complex number that is "a / b".
        """
        if not (isinstance(a, Complex) and isinstance(b, Complex)):
            raise ValueError("a and b must both be Complex instances")

        result = Complex(a)
        result.div(b)
        return result

    @staticmethod
    def conjugate(a):
        """
        Return a new complex number that is the complex conjugate of the
        specified complex number.
        param a The complex number used to form its conjugate.
        return A new complex number that is the complex conjugate of a.
        """
        x = Complex(a)
        return x.conj()

    @staticmethod
    def getInstance(stringList):
        """
        Retrieve two values from a list of strings and convert that to a Complex.

        This is used when parsing Complex lists from an XML representation to
        eventually construct a list of Complex instances. The values are expected
        to be floats representing the real and imaginary parts of a complex number.

        Returns a tuple of (Complex, stringList) where Complex is the new Complex
        created by this call and stringList is the remaining, unused, part of
        stringList after removing the first two elements.
        """
        if not isinstance(stringList, list):
            raise ValueError("stringList is not a list")

        # this will raise an error if there aren't enough elements on stringList
        reVal = float(stringList[0])
        imVal = float(stringList[1])
        return (Complex(reVal, imVal), stringList[2:])

    # The real part of the complex number.
    _re = 0.0

    # The imaginary part of the complex number.
    _im = 0.0

    def __init__(self, re=None, im=None):
        """
        Create a Complex number. The default case initialzes this to zero.

        If re is a string the parse it of the form "x y" where x and y are
        strings representing float values (float(x) should return the float
        value equivalent to the string representation of x). In that case, the
        im value must be None. The float version of x and y are then the
        real and imaginary parts of the new Complex number, respectively.

        If re is a Complex number then this is the copy constructor and
        the im value must be None.

        For all other cases, re and im are first converted to float via
        float(re) and float(im) and are then used as the real and imaginary
        parts of the new Complex number. In that case re and im must both
        not be None.
        """
        if (re is None) and (im is None):
            self._re = 0.0
            self._im = 0.0
        elif isinstance(re, Complex):
            if im is not None:
                raise ValueError("im must be None when re is a Complex instance.")

            # this assumes they're already floats
            self._re = re._re
            self._im = re._im
        elif isinstance(re, str):
            if im is not None:
                raise ValueError("im must be None when re is a string")

            reParts = re.split()
            if len(reParts) != 2:
                raise ValueError("re string does not appear to have exactly 2 values")

            self._re = float(reParts[0])
            self._im = float(reParts[1])
        else:
            if (re is None) or (im is None):
                raise ValueError(
                    "re and im must both be specified if re is not a string or Complex"
                )

            self._re = float(re)
            self._im = float(im)

    def getReal(self):
        """
        Return the real part of this complex number.
        """
        return self._re

    def getImg(self):
        """
        Return the imaginary part of this complex number.
        """
        return self._im

    def setReal(self, re):
        """
        Set the real value of this complex number.
        The float operator is used to ensure that re is used as a float by this class.
        """
        self._re = float(re)

    def setImg(self, im):
        """
        Set the imaginary value of this complex number.
        The float operator is used to ensure that im is used as a float by this class.
        """
        self._im = float(im)

    def __str__(self):
        """
        Return the value of this complex number as a string of the form "x y",
        where x and y are strings representing the numbers.
        """
        return str(self._re) + " " + str(self._im)

    @staticmethod
    def rvalues(items):
        """
        return a list of floats equal to the real parts of the list of Complex objects
        passed in the items argument.
        items may also be a list of lists(2D array) of Complex objects. If the
        first item is a list then this method assumes that items is a list of lists
        and the return value is a list of lists of floats.
        The list of lists case is done by calling this method recursively and so it
        should work for higher orders of lists of lists. That use case is not tested.
        """
        result = []
        if isinstance(items[0], list):
            # this is a list of lists, assume they are all lists
            for item in items:
                thisResult = Complex.rvalues(item)
                result.append(thisResult)
        else:
            if not isinstance(items[0], Complex):
                raise ValueError("items must contain Complex instances")
            # only check the first item
            for item in items:
                result.append(item.getReal())
        return result

    @staticmethod
    def ivalues(items):
        """
        return a list of floats equal to the imaginary parts of the list of Complex objects
        passed in the items argument.
        items may also be a list of lists(2D array) of Complex objects. If the
        first item is a list then this method assumes that items is a list of lists
        and the return value is a list of lists of floats.
        The list of lists case is done by calling this method recursively and so it
        should work for higher orders of lists of lists. That use case is not tested.
        """
        result = []
        if isinstance(items[0], list):
            # this is a list of lists, assume they are all lists
            for item in items:
                thisResult = Complex.ivalues(item)
                result.append(thisResult)
        else:
            if not isinstance(items[0], Complex):
                raise ValueError("items must contain Complex instances")
            # only check the first item
            for item in items:
                result.append(item.getImg())
        return result

    def toBin(self, eos):
        """
        Write the binary representation of this into an EndianOutput
        """
        eos.writeDouble(self.getReal())
        eos.writeDouble(self.getImg())

    @staticmethod
    def listToBin(complexList, eos):
        """
        Write a list of Complex to the EndianOutput.
        The list may have 1, 2 or 3 dimensions.
        """
        if not isinstance(complexList, list):
            raise ValueError("complexList is not a list")

        # this is used to determine the number of dimensions
        listDims = pyasdm.utils.getListDims(complexList)
        ndims = len(listDims)
        if ndims == 1:
            Complex.listTo1DBin(complexList, eos)
        elif ndims == 2:
            Complex.listTo2DBin(complexList, eos)
        elif ndims == 3:
            Complex.listTo3DBin(complexList, eos)
        else:
            raise ValueError(
                "unsupport number of dimensions in complexList in Complex.listToBin : "
                + str(ndims)
            )

    @staticmethod
    def listTo1DBin(complexList, eos):
        """
        Write a 1D list of Complex to the EndianOutput
        """
        if not isinstance(complexList, list):
            raise ValueError("complexList is not a list")

        # ndim is always written, even for 0-element lists
        eos.writeInt(len(complexList))

        # only check the first value
        if (len(complexList) > 0) and not isinstance(complexList[0], Complex):
            raise (ValueError("complexList is not a list of Complex"))

        for thisComplex in complexList:
            thisComplex.toBin(eos)

    @staticmethod
    def listTo2DBin(complexList, eos):
        """
        Write a 2D list of Complex to the EndianOutput
        """
        if not isinstance(complexList, list):
            raise ValueError("complexList is not a list")

        ndim1 = len(complexList)
        ndim2 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(complexList[0], list):
                raise ValueError("complexList is not a 2D list")

            ndim2 = len(complexList[0])
            if ndim2 > 0 and not isinstance(complexList[0][0], Complex):
                raise ValueError("complexListis a not a 2D list of Complex")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)

        for thisList in complexList:
            for thisComplex in thisList:
                thisComplex.toBin(eos)

    @staticmethod
    def listTo3DBin(complexList, eos):
        """
        Write a 3D list of Complex to the EndianOutput
        """
        if not isinstance(complexList, list):
            raise ValueError("complexList is not a list")

        ndim1 = len(complexList)
        ndim2 = 0
        ndim3 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(complexList[0], list):
                raise ValueError("complexList is not a 3D list")

            ndim2 = len(complexList[0])
            if ndim2 > 0:
                if not isinstance(complexList[0][0], list):
                    raise ValueError("complexList is a not a 3D list")
                ndim3 = len(complexList[0][0])
                if (ndim3 > 0) and not isinstance(complexList[0][0][0], Complex):
                    raise ValueError("complexList is not a 3D list of Complex")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)
        eos.writeInt(ndim3)

        for thisList in complexList:
            for middleList in thisList:
                for thisComplex in middleList:
                    thisComplex.toBin(eos)

    @staticmethod
    def fromBin(eis):
        """
        Read the binary representation of a Complex value
        from an EndianInput instance and use the read value to set a Complex value.

        return a Complex
        """
        reVal = eos.readDouble()
        imVal = eos.readDouble()
        return Complex(reVal, imVal)

    @staticmethod
    def from1DBin(eis):
        """
        Read a list of binary Complex values from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        result = []
        for i in range(dim1):
            result.append(Complex.fromBin(eis))

        return result

    @staticmethod
    def from2DBin(eis):
        """
        Read a 2D list of binary Complex values from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        dim2 = eis.readInt()
        result = []
        for i in range(dim1):
            innerList = []
            for j in range(dim2):
                innerList.append(Complex.fromBin(eis))
            result.append(innerList)

        return result

    @staticmethod
    def from3DBin(eis):
        """
        Read a 2D list of binary Complex values from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        dim2 = eis.readInt()
        result = []
        for i in range(dim1):
            innerList = []
            for j in range(dim2):
                innerList.append(Complex.fromBin(eis))
            result.append(innerList)

        return result

    def equals(self, otherComplex):
        """
        Return True if and only if the specified other complex number is a
        Complex and its value is equal to this complex number.
        param otherComplex The other complex number to which this
        is being compared.
        return True if and only if the specified other complex number is a
        Complex and its value is equal to this complex number
        """
        result = isinstance(otherComplex, Complex)
        result = result and (self._re == otherComplex._re)
        result = result and (self._im == otherComplex._im)
        return result

    def isZero(self):
        """
        Return True if and only if this Complex number is zero.
        """
        return self._re == 0.0 and self._im == 0.0

    def compareTo(self, other):
        """
        Compare this Complex to the specified other complex number, which must be
        a Complex, returning -1, 0, or +1 if the magnitude of this complex
        number is less than, equal to, or greater than the magnitude of the
        specified other complex number.
        """
        if not isinstance(other, Complex):
            raise ("Attempt to compare a Complex to a non-Complex.")

        magThis = math.sqrt(self._re * self._re + self._im * self._im)
        magOther = math.sqrt(other._re * other._re + other._im * other._im)

        result = 0
        if magThis < magOther:
            result = -1
        elif magThis > magOther:
            result = 1

        return result

    def __eq__(self, other):
        """
        Return True if and only if this Complex is equal to the specified
        other Complex.
        This is equivalent to the equals method.
        """
        return self.equals(other)

    def __ne__(self, other):
        """
        Return True if and only if this Complex is not equal to the specified
        other Complex.
        """
        result = False
        if isinstance(other, Complex):
            result = (self._re != other._re) or (self._im != other._im)

        return result

    def __lt__(self, other):
        """
        Return True if and only if the magnitude of this Complex is less than that of
        the specified other Complex.
        """
        result = False
        if isinstance(other, Complex):
            result = self.compareTo(other) == -1
        return result

    def __le__(self, other):
        """
        Return True if and only if the magnitude of this Complex is less than or equal to
        that of the specified other Complex.
        """
        result = False
        if isinstance(other, Complex):
            n = self.compareTo(other)
            result = (n == -1) or (n == 0)
        return result

    def __gt__(self, other):
        """
        Return True if and only if the magnitude of this Complex is greater than that of
        the specified other Complex.
        """
        result = False
        if isinstance(other, Complex):
            result = self.compareTo(other) == 1
        return result

    def __ge__(self, other):
        """
        Return True if and only if the magnitude of this Complex is greater than or equal to
        that of the specified other Complex.
        """
        result = False
        if isinstance(other, Complex):
            n = self.compareTo(other)
            result = (n == 1) or (n == 0)
        return result

    def __add__(self, other):
        """
        Add other, which must be a Complex, to this complex number, (this + x).
        param other The Complex to be added to this complex number.
        return This complex number after the addition.
        """
        if not isinstance(other, Complex):
            raise ValueError("Attempt to add a non-Complex to a Complex")

        self._re += other._re
        self._im += other._im
        return self

    def __sub__(self, other):
        """
        Subtract other which must be a Complex, from this complex number, (this - x).
        param other The Complex to be subtracted from this complex number.
        return This complex number after the subtraction.
        """
        if not isinstance(other, Complex):
            raise ValueError("Attempt to subtract a non-Complex from a Complex")

        self._re -= other._re
        self._im -= other._im
        return self

    def __mul__(self, other):
        """
        Multiply this complex number by a specified other complex number, (this * other).
        param factor The complex number to be multiplied.
        return This complex number after the multiplication.
        """
        self._re = self._re * other._re + self._im * other._im
        self._im = self._re * other._im + self._im * other._re
        return self

    def __truediv__(self, other):
        """
        Divide this complex number by a specified complex number (this / x).
        param The complex number by which this number is divided.
        return This complex number after the division.
        """
        dem = other._re * other._re + other._im * other._im
        self._re = (self._re * other._re + self._im * other._im) / dem
        self._im = (self._im * other._re - self._re * other._im) / dem
        return self

    def conj(self):
        """
        Replace this complex number by it's complex conjugate.
        return this complex number
        """
        self._im = -self._im
        return self
