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
# File StokesParameter.py

# to keep track of the attributes added to this class for each value of this enumeration

_stokesParameterDict = {}

# the possible enumerations

_I = 0  #

_Q = 1  #

_U = 2  #

_V = 3  #

_RR = 4  #

_RL = 5  #

_LR = 6  #

_LL = 7  #

_XX = 8  # Linear correlation product

_XY = 9  #

_YX = 10  #

_YY = 11  #

_RX = 12  # Mixed correlation product

_RY = 13  # Mixed correlation product

_LX = 14  # Mixed LX product

_LY = 15  # Mixed LY correlation product

_XR = 16  # Mixed XR correlation product

_XL = 17  # Mixed XL correlation product

_YR = 18  # Mixed YR correlation product

_YL = 19  # Mixel YL correlation product

_PP = 20  #

_PQ = 21  #

_QP = 22  #

_QQ = 23  #

_RCIRCULAR = 24  #

_LCIRCULAR = 25  #

_LINEAR = 26  # single dish polarization type

_PTOTAL = 27  # Polarized intensity ((Q^2+U^2+V^2)^(1/2))

_PLINEAR = 28  # Linearly Polarized intensity ((Q^2+U^2)^(1/2))

_PFTOTAL = 29  # Polarization Fraction (Ptotal/I)

_PFLINEAR = 30  # Linear Polarization Fraction (Plinear/I)

_PANGLE = 31  # Linear Polarization Angle (0.5 arctan(U/Q)) (in radians)


# their names in a dictionary
_stokesParameterNames = {}

_stokesParameterNames[_I] = "I"

_stokesParameterNames[_Q] = "Q"

_stokesParameterNames[_U] = "U"

_stokesParameterNames[_V] = "V"

_stokesParameterNames[_RR] = "RR"

_stokesParameterNames[_RL] = "RL"

_stokesParameterNames[_LR] = "LR"

_stokesParameterNames[_LL] = "LL"

_stokesParameterNames[_XX] = "XX"

_stokesParameterNames[_XY] = "XY"

_stokesParameterNames[_YX] = "YX"

_stokesParameterNames[_YY] = "YY"

_stokesParameterNames[_RX] = "RX"

_stokesParameterNames[_RY] = "RY"

_stokesParameterNames[_LX] = "LX"

_stokesParameterNames[_LY] = "LY"

_stokesParameterNames[_XR] = "XR"

_stokesParameterNames[_XL] = "XL"

_stokesParameterNames[_YR] = "YR"

_stokesParameterNames[_YL] = "YL"

_stokesParameterNames[_PP] = "PP"

_stokesParameterNames[_PQ] = "PQ"

_stokesParameterNames[_QP] = "QP"

_stokesParameterNames[_QQ] = "QQ"

_stokesParameterNames[_RCIRCULAR] = "RCIRCULAR"

_stokesParameterNames[_LCIRCULAR] = "LCIRCULAR"

_stokesParameterNames[_LINEAR] = "LINEAR"

_stokesParameterNames[_PTOTAL] = "PTOTAL"

_stokesParameterNames[_PLINEAR] = "PLINEAR"

_stokesParameterNames[_PFTOTAL] = "PFTOTAL"

_stokesParameterNames[_PFLINEAR] = "PFLINEAR"

_stokesParameterNames[_PANGLE] = "PANGLE"


class StokesParameter:
    """
    A class for the StokesParameter enumeration.
    """

    # The value of this StokesParameter, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, stokesParameter):
        # construct a StokesParameter from an integer, a string, or another StokesParameter
        # if stokesParameter is a string, convert it to an instance of this class using literal
        if isinstance(stokesParameter, StokesParameter):
            # copy constructor
            self._value = stokesParameter.getValue()
            self._name = stokesParameter.getName()
        elif isinstance(stokesParameter, str):
            # convert it to an instance of this class using literal
            thisEnum = StokesParameter.literal(stokesParameter)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if stokesParameter not in _stokesParameterNames:
                raise ValueError("unrecognized StokesParameter")
            self._value = stokesParameter
            self._name = _stokesParameterNames[stokesParameter]
            if self._name not in _stokesParameterDict:
                # add this StokesParameter as an attribute to this class using its name
                setattr(StokesParameter, self._name, self)
                _stokesParameterDict[self._name] = getattr(StokesParameter, self._name)

    def getValue(self):
        return self._value

    def getName(self):
        return self._name

    # by convention with the other languages, these are all static methods
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
        the number of known enumerators in StokesParameter
        """
        return len(_stokesParameterNames)

    @staticmethod
    def name(stokesParameter):
        """
        Returns the string form of the StokesParameter
        """
        return stokesParameter.getName()

    @staticmethod
    def toString(stokesParameter):
        """
        Equivalent to the name method
        """
        return StokesParameter.name(stokesParameter)

    @staticmethod
    def names():
        """
        Return the list of all known StokesParameter enumeration names
        """
        return list(_stokesParameterNames.values())

    @staticmethod
    def newStokesParameter(name):
        """
        Equivalent to the literal method
        """
        return StokesParameter.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the StokesParameter enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(StokesParameter, name):
            raise ValueError("Unrecognized StokesParameter name")
        return StokesParameter(getattr(StokesParameter, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a StokesParameter from an integration matching an enumeration.
        """
        return StokesParameter(i)


I = StokesParameter(_I)

Q = StokesParameter(_Q)

U = StokesParameter(_U)

V = StokesParameter(_V)

RR = StokesParameter(_RR)

RL = StokesParameter(_RL)

LR = StokesParameter(_LR)

LL = StokesParameter(_LL)

XX = StokesParameter(_XX)

XY = StokesParameter(_XY)

YX = StokesParameter(_YX)

YY = StokesParameter(_YY)

RX = StokesParameter(_RX)

RY = StokesParameter(_RY)

LX = StokesParameter(_LX)

LY = StokesParameter(_LY)

XR = StokesParameter(_XR)

XL = StokesParameter(_XL)

YR = StokesParameter(_YR)

YL = StokesParameter(_YL)

PP = StokesParameter(_PP)

PQ = StokesParameter(_PQ)

QP = StokesParameter(_QP)

QQ = StokesParameter(_QQ)

RCIRCULAR = StokesParameter(_RCIRCULAR)

LCIRCULAR = StokesParameter(_LCIRCULAR)

LINEAR = StokesParameter(_LINEAR)

PTOTAL = StokesParameter(_PTOTAL)

PLINEAR = StokesParameter(_PLINEAR)

PFTOTAL = StokesParameter(_PFTOTAL)

PFLINEAR = StokesParameter(_PFLINEAR)

PANGLE = StokesParameter(_PANGLE)
