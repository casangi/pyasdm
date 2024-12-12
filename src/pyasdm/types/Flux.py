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

    def toString(self):
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

    def toBin(self):
        # it also needs a static method to send a list of flux items toBin
        # should also work for 2D, 3D lists
        raise RuntimeError("Flux.toBin is not yet implemented")

    def fromBin(self):
        raise RuntimeError("Flux.fromBin is not yet implemented")

    def from1DBin(self):
        raise RuntimeError("Flux.from1DBin is not yet implemented")

    def from2DBin(self):
        raise RuntimeError("Flux.from2DBin is not yet implemented")

    def from3DBin(self):
        raise RuntimeError("Flux.from2DBin is not yet implemented")

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

    def eq(self, otherFlux):
        """
        Return True if and only if this Flux is equal to the specified
        other Flux.
        This is equivalent to the equals method.
        """
        return self.equals(otherFlux)

    def ne(self, otherFlux):
        """
        Return True if and only if this Flux is not equal to the specified
        other Flux.
        """
        return isinstance(otherFlux, Flux) and (self._flux != otherFlux._flux)

    def lt(self, otherFlux):
        """
        Return True if and only if this Flux is less than the specified
        other Flux.
        """
        return isinstance(otherFlux, Flux) and (self._flux < otherFlux._flux)

    def le(self, otherFlux):
        """
        Return True if and only if this Flux is less than or equal to
        the specified other Flux.
        """
        return isinstance(otherFlux, Flux) and (self._flux <= otherFlux._flux)

    def gt(self, otherFlux):
        """
        Return True if and only if this Flux is greater than the specified
        other Flux.
        """
        return isinstance(otherFlux, Flux) and (self._flux > otherFlux._flux)

    def ge(self, otherFlux):
        """
        Return True if and only if this Flux is greater than or equal to
        the specified other Flux.
        """
        return isinstance(otherFlux, Flux) and (self._flux >= otherFlux._flux)

    def add(self, otherFlux):
        """
        Add otherFlux, which must be a Flux, to this flux, (this + x).
        param otherFlux The Flux to be added to this flux.
        return This flux after the addition.
        """
        if not isinstance(otherFlux, Flux):
            raise ValueError("Attempt to add a non-Flux to a Flux")

        self._flux += otherFlux._flux
        return self

    def sub(self, otherFlux):
        """
        Subtract otherFlux which must be a Flux, from this flux, (this - x).
        param otherFlux The Flux to be subtracted from this flux.
        return This flux after the subtraction.
        """
        if not isinstance(otherFlux, Flux):
            raise ValueError("Attempt to subtract a non-Flux from a Flux")

        self._flux -= otherFlux._flux
        return self

    def mult(self, factor):
        """
        Multiply this flux by some factor, (this * factor).
        param factor The factor by which this flux is to be multiplied.
        return This flux after the multiplication.
        """
        self._flux *= factor
        return self

    def div(self, factor):
        """
        Divide this flux by some factor, (this / factor).
        param factor The factor by which this flux is to be divided.
        return This flux after the division.
        """
        self._flux /= factor
        return self
