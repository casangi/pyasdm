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
# File RadialVelocityReferenceCode.py

# to keep track of the attributes added to this class for each value of this enumeration

_radialVelocityReferenceCodeDict = {}

# the possible enumerations

_LSRD = 0  # dynamic local standard of rest.

_LSRK = 1  # kinematic local standard of rest.

_GALACTO = 2  # galactocentric frequency.

_BARY = 3  # barycentric frequency.

_GEO = 4  # geocentric frequency.

_TOPO = 5  # topocentric frequency.


# their names in a dictionary
_radialVelocityReferenceCodeNames = {}

_radialVelocityReferenceCodeNames[_LSRD] = "LSRD"

_radialVelocityReferenceCodeNames[_LSRK] = "LSRK"

_radialVelocityReferenceCodeNames[_GALACTO] = "GALACTO"

_radialVelocityReferenceCodeNames[_BARY] = "BARY"

_radialVelocityReferenceCodeNames[_GEO] = "GEO"

_radialVelocityReferenceCodeNames[_TOPO] = "TOPO"


class RadialVelocityReferenceCode:
    """
    A class for the RadialVelocityReferenceCode enumeration.
    """

    # The value of this RadialVelocityReferenceCode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, radialVelocityReferenceCode):
        # construct a RadialVelocityReferenceCode from an integer, a string, or another RadialVelocityReferenceCode
        # if radialVelocityReferenceCode is a string, convert it to an instance of this class using literal
        if isinstance(radialVelocityReferenceCode, RadialVelocityReferenceCode):
            # copy constructor
            self._value = radialVelocityReferenceCode.getValue()
            self._name = radialVelocityReferenceCode.getName()
        elif isinstance(radialVelocityReferenceCode, str):
            # convert it to an instance of this class using literal
            thisEnum = RadialVelocityReferenceCode.literal(radialVelocityReferenceCode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if radialVelocityReferenceCode not in _radialVelocityReferenceCodeNames:
                raise ValueError("unrecognized RadialVelocityReferenceCode")
            self._value = radialVelocityReferenceCode
            self._name = _radialVelocityReferenceCodeNames[radialVelocityReferenceCode]
            if self._name not in _radialVelocityReferenceCodeDict:
                # add this RadialVelocityReferenceCode as an attribute to this class using its name
                setattr(RadialVelocityReferenceCode, self._name, self)
                _radialVelocityReferenceCodeDict[self._name] = getattr(
                    RadialVelocityReferenceCode, self._name
                )

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
        Returns True if other is a RadialVelocityReferenceCode and its value is the same as this one.
        """
        return isinstance(other, RadialVelocityReferenceCode) and (
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
        the number of known enumerators in RadialVelocityReferenceCode
        """
        return len(_radialVelocityReferenceCodeNames)

    @staticmethod
    def name(radialVelocityReferenceCode):
        """
        Returns the string form of radialVelocityReferenceCode
        """
        return str(radialVelocityReferenceCode)

    @staticmethod
    def names():
        """
        Return the list of all known RadialVelocityReferenceCode enumeration names
        """
        return list(_radialVelocityReferenceCodeNames.values())

    @staticmethod
    def newRadialVelocityReferenceCode(name):
        """
        Equivalent to the literal method
        """
        return RadialVelocityReferenceCode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the RadialVelocityReferenceCode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(RadialVelocityReferenceCode, name):
            raise ValueError("Unrecognized RadialVelocityReferenceCode name")
        return RadialVelocityReferenceCode(
            getattr(RadialVelocityReferenceCode, name).getValue()
        )

    @staticmethod
    def from_int(i):
        """
        Return a RadialVelocityReferenceCode from an integration matching an enumeration.
        """
        return RadialVelocityReferenceCode(i)


LSRD = RadialVelocityReferenceCode(_LSRD)

LSRK = RadialVelocityReferenceCode(_LSRK)

GALACTO = RadialVelocityReferenceCode(_GALACTO)

BARY = RadialVelocityReferenceCode(_BARY)

GEO = RadialVelocityReferenceCode(_GEO)

TOPO = RadialVelocityReferenceCode(_TOPO)
