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
# File Flux.py
#

import pyasdm.utils


class Flux:
    """
    The Flux class implements a concept of a flux in Janskys.

    This version adapted from the c++ and java implementations, originally authored by Allen Farris.
    """

    @staticmethod
    def sum(a, b):
        """
        Return a new Flux that is the sum of the
        specified Janskys, a +  b.
        param a The first Flux of the pair.
        param b The second Flux of the pair.
        return A new Flux that is the sum of the
        specified Janskys, a +  b.
        """
        if not (isinstance(a, Flux) and isinstance(b, Flux)):
            raise ValueError("a and b must both be Flux instances")

        return Flux(a._flux + b._flux)

    @staticmethod
    def subtract(a, b):
        """
        Return a new Flux that is the difference of the
        specified Janskys, a - b.
        param a The first Flux of the pair.
        param b The second Flux of the pair.
        return A new Flux that is the difference of the
        specified Janskys, a - b.
        """
        if not (isinstance(a, Flux) and isinstance(b, Flux)):
            raise ValueError("a and b must both be Flux instances")

        return Flux(a._flux - b._flux)

    @staticmethod
    def multiply(a, factor):
        """
        Return a new Flux that is the product of a specified
        flux and some specified factor, a * factor.
        param a The base flux
        param factor The factor that is used to multiply the value.
        return A new Flux that is the product of a specified
        flux and some specified factor, a * factor.
        """
        if not isinstance(a, Flux):
            raise ValueError("a must be a Flux")

        return Flux(a._flux * factor)

    @staticmethod
    def divide(a, factor):
        """
        Return a new Flux that is a specified flux divided by a
        specified factor, a / factor.
        param a The base flux
        param factor The factor that is used to divide the value.
        return A new Flux that is the product of a specified
        flux and some specified factor, a / factor.
        """
        if not isinstance(a, Flux):
            raise ValueError("a must be a Flux")

        return Flux(a._flux / factor)

    @staticmethod
    def getInstance(stringList):
        """
        Retrieve a value from a list of strings and convert that to a Flux.

        This is used when parsing Flux lists from an XML representation to
        eventually construct a list of Flux instances. The string values
        are float representation of flux in Janskys.

        Returns a tuple of (Flux, stringList) where Flux is the new Flux
        created by this call and stringList is the remaining, unused, part of
        stringList after removing the first element.
        """
        if not isinstance(stringList, list):
            raise ValueError("stringList is not a list")

        # this will raise an error if there aren't any elements on stringList
        floatVal = float(stringList[0])
        return (Flux(floatVal), stringList[1:])

    # The flux in Janskys.
    _flux = 0.0

    def __init__(self, flux=0.0):
        """
        Create a Flux with an initial value in Janskys.
        The default Flux (no arguments) is zero (0.0) Janskys.
        Any flux that is not a Flux is valid so long as it can be
        converted to a float as float(flux) (including a parseable string).
        If flux is a Flux instance then this is the copy constructor.
        """
        if isinstance(flux, Flux):
            self._flux = flux._flux
        else:
            self.set(flux)

    def get(self):
        """
        Return the value of this flux as a double in Janskys.
        """
        return self._flux

    def set(self, flux):
        """
        Set the value of this flux to the specified flux in Janskys.
        Any flux is valid so long as it can be converted into a float using float(flux)
        (including a parseable string).
        """
        self._flux = float(flux)

    def __str__(self):
        """
        Return the value of this flux as a String in units of Janskys.
        """
        return str(self.get())

    @staticmethod
    def values(items):
        """
        return a list of floats containing the value of the list of Flux objects
        passed in the items argument.
        items may also be a list of lists(2D array) of Flux objects. If the
        first item is a list then this method assumes that items is a list of lists
        and the return value is a list of lists of floats.
        The list of lists case is done by calling this method recursively and so it
        should work for higher orders of lists of lists. That use case is not tested.
        """
        result = []
        if isinstance(items[0], list):
            # this is a list of lists, assume they are all lists
            for item in items:
                thisResult = Flux.values(item)
                result.append(thisResult)
        else:
            if not isinstance(items[0], Flux):
                raise ValueError("items must contain Flux instances")
            # only check the first item
            for item in items:
                result.append(item.get())
        return result

    def toBin(self, eos):
        """
        Write this Flux out, in Janskys, to a EndianOutput.
        """
        eos.writeDouble(self.get())

    @staticmethod
    def listToBin(fluxList, eos):
        """
        Write a list of Flux to the EndianOutput.
        The list may have 1, 2 or 3 dimensions.
        """
        if not isinstance(fluxList, list):
            raise ValueError("fluxList is not a list")

        # this is used to determine the number of dimensions
        listDims = pyasdm.utils.getListDims(fluxList)
        ndims = len(listDims)
        if ndims == 1:
            Flux.listTo1DBin(fluxList, eos)
        elif ndims == 2:
            Flux.listTo2DBin(fluxList, eos)
        elif ndims == 3:
            Flux.listTo3DBin(fluxList, eos)
        else:
            raise ValueError(
                "unsupport number of dimensions in fluxList in Flux.listToBin : "
                + str(ndims)
            )

    @staticmethod
    def listTo1DBin(fluxList, eos):
        """
        Write a 1D list of Flux to the EndianOutput
        """
        if not isinstance(fluxList, list):
            raise ValueError("fluxList is not a list")

        # ndim is always written, even for 0-element lists
        eos.writeInt(len(fluxList))

        # only check the first value
        if (len(fluxList) > 0) and not isinstance(fluxList[0], Flux):
            raise (ValueError("fluxList is not a list of Flux"))

        for thisFlux in fluxList:
            thisFlux.toBin(eos)

    @staticmethod
    def listTo2DBin(fluxList, eos):
        """
        Write a 2D list of Flux to the EndianOutput
        """
        if not isinstance(fluxList, list):
            raise ValueError("fluxList is not a list")

        ndim1 = len(fluxList)
        ndim2 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(fluxList[0], list):
                raise ValueError("fluxList is not a 2D")

            ndim2 = len(fluxList[0])
            if ndim2 > 0 and not isinstance(fluxList[0][0], Flux):
                raise ValueError("fluxListis a not a 2D list of Flux")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)

        for thisList in fluxList:
            for thisFlux in thisList:
                thisFlux.toBin(eos)

    @staticmethod
    def listTo3DBin(fluxList, eos):
        """
        Write a 3D list of Flux to the EndianOutput
        """
        if not isinstance(fluxList, list):
            raise ValueError("fluxList is not a list")

        ndim1 = len(fluxList)
        ndim2 = 0
        ndim3 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(fluxList[0], list):
                raise ValueError("fluxList is not a 3D list")

            ndim2 = len(fluxList[0])
            if ndim2 > 0:
                if not isinstance(fluxList[0][0], list):
                    raise ValueError("fluxList is a not a 3D list")
                ndim3 = len(fluxList[0][0])
                if (ndim3 > 0) and not isinstance(fluxList[0][0][0], Flux):
                    raise ValueError("fluxList is not a 3D list of Flux")

        # ndims are always written
        eos.writeInt(ndim1)
        eos.writeInt(ndim2)
        eos.writeInt(ndim3)

        for thisList in fluxList:
            for middleList in thisList:
                for thisFlux in middleList:
                    thisFlux.toBin(eos)

    @staticmethod
    def fromBin(eis):
        """
        Read the binary representation of an Flux, in Janskys,
        from an EndianInput instance and use the read value to set a
        Flux.

        return a Flux
        """
        return Flux(eis.readDouble())

    @staticmethod
    def from1DBin(eis):
        """
        Read a list of binary Flux values, in Janskys, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        result = []
        for i in range(dim1):
            result.append(Flux.fromBin(eis))

        return result

    @staticmethod
    def from2DBin(eis):
        """
        Read a 2D list of binary Flux values, in Janskys, from an
        EndianInput instance and return the resulting list.
        """
        dim1 = eis.readInt()
        dim2 = eis.readInt()
        result = []
        for i in range(dim1):
            innerList = []
            for j in range(dim2):
                innerList.append(Flux.fromBin(eis))
            result.append(innerList)

        return result

    @staticmethod
    def from3DBin(eis):
        """
        Read a 3D list of binary Flux values, in Janskys, from an
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
                    innerList.append(Flux.fromBin(eis))
                middleList.append(innerList)
            result.append(middleList)

        return result

    def equals(self, otherFlux):
        """
        Return True if and only if the specified other flux is a
        Flux and its value is equal to this flux.
        param otherFlux The other flux to which this flux
        is being compared.
        return True if and only if the specified other flux is an
        Flux and its value is equal to this flux.
        """
        return isinstance(otherFlux, Flux) and (self._flux == otherFlux._flux)

    def almostEquals(self, otherFlux, toleranceFlux):
        """
        Return True if and only if otherFlux and toleranceFlux are both Flux
        instances are if the absolute value of the difference between this and otherFlux
        is less than the absolute value of toleranceFlux.
        """
        result = False
        if isinstance(otherFlux, Flux) and isinstance(toleranceFlux, Flux):
            result = abs(self._flux - otherFlux._flux) <= abs(toleranceFlux._flux)

        return result

    def isZero(self):
        """
        Return True if and only if this flux is zero (0.0).
        """
        return self._flux == 0.0

    def compareTo(self, otherFlux):
        """
        Compare this Flux to the specified otherFlux, which must be
        a Flux, returning -1, 0, or +1 if this flux is less
        than, equal to, or greater than the specified other Flux.
        """
        if not isinstance(otherFlux, Flux):
            raise ("Attempt to compare a Flux to a non-Flux.")

        result = 0
        if self._flux < otherFlux._flux:
            result = -1
        if self._flux > otherFlux._flux:
            result = 1

        return result

    def __eq__(self, otherFlux):
        """
        Return True if and only if this Flux is equal to the specified
        other Flux.
        This is equivalent to the equals method.
        """
        return self.equals(otherFlux)

    def __ne__(self, otherFlux):
        """
        Return True if and only if this Flux is not equal to the specified
        other Flux.
        """
        return isinstance(otherFlux, Flux) and (self._flux != otherFlux._flux)

    def __lt__(self, otherFlux):
        """
        Return True if and only if this Flux is less than the specified
        other Flux.
        """
        return isinstance(otherFlux, Flux) and (self._flux < otherFlux._flux)

    def __le__(self, otherFlux):
        """
        Return True if and only if this Flux is less than or equal to
        the specified other Flux.
        """
        return isinstance(otherFlux, Flux) and (self._flux <= otherFlux._flux)

    def __gt__(self, otherFlux):
        """
        Return True if and only if this Flux is greater than the specified
        other Flux.
        """
        return isinstance(otherFlux, Flux) and (self._flux > otherFlux._flux)

    def __ge__(self, otherFlux):
        """
        Return True if and only if this Flux is greater than or equal to
        the specified other Flux.
        """
        return isinstance(otherFlux, Flux) and (self._flux >= otherFlux._flux)

    def __add__(self, otherFlux):
        """
        Add otherFlux, which must be a Flux, to this flux, (this + x).
        param otherFlux The Flux to be added to this flux.
        return This flux after the addition.
        """
        if not isinstance(otherFlux, Flux):
            raise ValueError("Attempt to add a non-Flux to a Flux")

        self._flux += otherFlux._flux
        return self

    def __sub__(self, otherFlux):
        """
        Subtract otherFlux which must be a Flux, from this flux, (this - x).
        param otherFlux The Flux to be subtracted from this flux.
        return This flux after the subtraction.
        """
        if not isinstance(otherFlux, Flux):
            raise ValueError("Attempt to subtract a non-Flux from a Flux")

        self._flux -= otherFlux._flux
        return self

    def __mul__(self, factor):
        """
        Multiply this flux by some factor, (this * factor).
        param factor The factor by which this flux is to be multiplied.
        return This flux after the multiplication.
        """
        self._flux *= factor
        return self

    def __truediv__(self, factor):
        """
        Divide this flux by some factor, (this / factor).
        param factor The factor by which this flux is to be divided.
        return This flux after the division.
        """
        self._flux /= factor
        return self
