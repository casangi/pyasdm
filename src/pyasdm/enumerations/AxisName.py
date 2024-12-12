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
# File AxisName.py

# to keep track of the attributes added to this class for each value of this enumeration

_axisNameDict = {}

# the possible enumerations

_TIM = 0  # Time axis.

_BAL = 1  # Baseline axis.

_ANT = 2  # Antenna axis.

_BAB = 3  # Baseband axis.

_SPW = 4  # Spectral window  axis.

_SIB = 5  # Sideband axis.

_SUB = 6  # Subband axis.

_BIN = 7  # Bin axis.

_APC = 8  # Atmosphere phase correction axis.

_SPP = 9  # Spectral point axis.

_POL = 10  # Polarization axis (Stokes parameters).

_STO = 11  # Stokes parameter axis.

_HOL = 12  # Holography axis.


# their names in a dictionary
_axisNameNames = {}

_axisNameNames[_TIM] = "TIM"

_axisNameNames[_BAL] = "BAL"

_axisNameNames[_ANT] = "ANT"

_axisNameNames[_BAB] = "BAB"

_axisNameNames[_SPW] = "SPW"

_axisNameNames[_SIB] = "SIB"

_axisNameNames[_SUB] = "SUB"

_axisNameNames[_BIN] = "BIN"

_axisNameNames[_APC] = "APC"

_axisNameNames[_SPP] = "SPP"

_axisNameNames[_POL] = "POL"

_axisNameNames[_STO] = "STO"

_axisNameNames[_HOL] = "HOL"


class AxisName:
    """
    A class for the AxisName enumeration.
    """

    # The value of this AxisName, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, axisName):
        # construct a AxisName from an integer, a string, or another AxisName
        # if axisName is a string, convert it to an instance of this class using literal
        if isinstance(axisName, AxisName):
            # copy constructor
            self._value = axisName.getValue()
            self._name = axisName.getName()
        elif isinstance(axisName, str):
            # convert it to an instance of this class using literal
            thisEnum = AxisName.literal(axisName)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if axisName not in _axisNameNames:
                raise ValueError("unrecognized AxisName")
            self._value = axisName
            self._name = _axisNameNames[axisName]
            if self._name not in _axisNameDict:
                # add this AxisName as an attribute to this class using its name
                setattr(AxisName, self._name, self)
                _axisNameDict[self._name] = getattr(AxisName, self._name)

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
        the number of known enumerators in AxisName
        """
        return len(_axisNameNames)

    @staticmethod
    def name(axisName):
        """
        Returns the string form of the AxisName
        """
        return axisName.getName()

    @staticmethod
    def toString(axisName):
        """
        Equivalent to the name method
        """
        return AxisName.name(axisName)

    @staticmethod
    def names():
        """
        Return the list of all known AxisName enumeration names
        """
        return list(_axisNameNames.values())

    @staticmethod
    def newAxisName(name):
        """
        Equivalent to the literal method
        """
        return AxisName.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the AxisName enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(AxisName, name):
            raise ValueError("Unrecognized AxisName name")
        return AxisName(getattr(AxisName, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a AxisName from an integration matching an enumeration.
        """
        return AxisName(i)


TIM = AxisName(_TIM)

BAL = AxisName(_BAL)

ANT = AxisName(_ANT)

BAB = AxisName(_BAB)

SPW = AxisName(_SPW)

SIB = AxisName(_SIB)

SUB = AxisName(_SUB)

BIN = AxisName(_BIN)

APC = AxisName(_APC)

SPP = AxisName(_SPP)

POL = AxisName(_POL)

STO = AxisName(_STO)

HOL = AxisName(_HOL)
