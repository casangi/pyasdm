# ALMA - Atacama Large Millimeter Array
# (c) European Southern Observatory, 2002
# (c) Associated Universities Inc., 2002
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
# /////////////////////////////////////////////////////////////////
# // WARNING!  DO NOT MODIFY THIS FILE!                          //
# //  ---------------------------------------------------------  //
# // | This is generated code!  Do not modify this file.       | //
# // | Any changes will be lost when the file is re-generated. | //
# //  ---------------------------------------------------------  //
# /////////////////////////////////////////////////////////////////
#
# File WindowFunction.py

# to keep track of the attributes added to this class for each value of this enumeration

_windowFunctionDict = {}

# the possible enumerations

_UNIFORM = 0  # No windowing

_HANNING = 1  # Raised cosine: \f$0.5*(1-cos(x))\f$ where \f$x = 2*\pi*i/(N-1)\f$

_HAMMING = 2  # The classic Hamming window is \f$W_M(x) = 0.54 - 0.46*\cos(x)\f$. This is generalized to \f$W_M(x) = \beta - (1-\beta)*\cos(x)\f$ where \f$\beta\f$ can take any value in the range \f$[0,1]\f$. \f$\beta=0.5\f$ corresponds to the Hanning window.

_BARTLETT = 3  # The Bartlett (triangular) window is \f$1 - |x/\pi|\f$, where \f$x = 2*\pi*i/(N-1)\f$.

_BLACKMANN = 4  # The window function is \f$W_B(x) = (0.5 - \beta) - 0.5*\cos(x_j) + \beta*\cos(2x_j)\f$, where \f$x_j=2*\pi*j/(N-1)\f$. The classic Blackman window is given by \f$\beta=0.08\f$.

_BLACKMANN_HARRIS = 5  # The BLACKMANN_HARRIS window is \f$1.0 - 1.36109*\cos(x) + 0.39381*\cos(2*x) - 0.032557*\cos(3*x)\f$, where \f$x = 2*\pi*i/(N-1)\f$.

_WELCH = 6  # The Welch window (parabolic) is \f$1 - (2*i/N)^2\f$.


# their names in a dictionary
_windowFunctionNames = {}

_windowFunctionNames[_UNIFORM] = "UNIFORM"

_windowFunctionNames[_HANNING] = "HANNING"

_windowFunctionNames[_HAMMING] = "HAMMING"

_windowFunctionNames[_BARTLETT] = "BARTLETT"

_windowFunctionNames[_BLACKMANN] = "BLACKMANN"

_windowFunctionNames[_BLACKMANN_HARRIS] = "BLACKMANN_HARRIS"

_windowFunctionNames[_WELCH] = "WELCH"


class WindowFunction:
    """
    A class for the WindowFunction enumeration.
    """

    # The value of this WindowFunction, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, windowFunction):
        # construct a WindowFunction from an integer, a string, or another WindowFunction
        # if windowFunction is a string, convert it to an instance of this class using literal
        if isinstance(windowFunction, WindowFunction):
            # copy constructor
            self._value = windowFunction.getValue()
            self._name = windowFunction.getName()
        elif isinstance(windowFunction, str):
            # convert it to an instance of this class using literal
            thisEnum = WindowFunction.literal(windowFunction)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if windowFunction not in _windowFunctionNames:
                raise ValueError("unrecognized WindowFunction")
            self._value = windowFunction
            self._name = _windowFunctionNames[windowFunction]
            if self._name not in _windowFunctionDict:
                # add this WindowFunction as an attribute to this class using its name
                setattr(WindowFunction, self._name, self)
                _windowFunctionDict[self._name] = getattr(WindowFunction, self._name)

    def getValue(self):
        """
        Return the integer value of this enumeration.
        """
        return self._value

    def getName(self):
        """
        Return the name of this enumeration.
        """
        return self._name

    def __str__(self):
        """
        Equivalent to getName()
        """
        return self.getName()

    def __eq__(self, other):
        """
        Returns True if other is a WindowFunction and its value is the same as this one.
        """
        return isinstance(other, WindowFunction) and (
            other.getValue() == self.getValue()
        )

    def __ne__(self, other):
        """
        Returns True if other is not equal to self
        """
        return not (self == other)

    # by convention with the code in java and c++, these are all static methods
    @staticmethod
    def revision():
        """
        revision as a string.
        """
        return "-1"

    @staticmethod
    def version():
        """
        the major version number as an int.
        """
        return 1

    @staticmethod
    def size():
        """
        the number of known enumerators in WindowFunction
        """
        return len(_windowFunctionNames)

    @staticmethod
    def name(windowFunction):
        """
        Returns the string form of windowFunction
        """
        return str(windowFunction)

    @staticmethod
    def names():
        """
        Return the list of all known WindowFunction enumeration names
        """
        return list(_windowFunctionNames.values())

    @staticmethod
    def newWindowFunction(name):
        """
        Equivalent to the literal method
        """
        return WindowFunction.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the WindowFunction enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(WindowFunction, name):
            raise ValueError("Unrecognized WindowFunction name")
        return WindowFunction(getattr(WindowFunction, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a WindowFunction from an integration matching an enumeration.
        """
        return WindowFunction(i)


UNIFORM = WindowFunction(_UNIFORM)

HANNING = WindowFunction(_HANNING)

HAMMING = WindowFunction(_HAMMING)

BARTLETT = WindowFunction(_BARTLETT)

BLACKMANN = WindowFunction(_BLACKMANN)

BLACKMANN_HARRIS = WindowFunction(_BLACKMANN_HARRIS)

WELCH = WindowFunction(_WELCH)
