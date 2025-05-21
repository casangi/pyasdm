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
# File BaselineReferenceCode.py

# to keep track of the attributes added to this class for each value of this enumeration

_baselineReferenceCodeDict = {}

# the possible enumerations

_J2000 = 0  # mean equator, equinox J2000.0

_B1950 = 1  # mean equator, equinox B1950.0

_GALACTIC = 2  # galactic coordinates.

_SUPERGAL = 3  # supergalactic coordinates.

_ECLIPTIC = 4  # ecliptic for J2000.0

_JMEAN = 5  # mean equator.

_JTRUE = 6  # true equator.

_APP = 7  # apparent geocentric.

_BMEAN = 8  # mean equator.

_BTRUE = 9  # true equator.

_JNAT = 10  # geocentric natural frame.

_MECLIPTIC = 11  # ecliptic for mean equator.

_TECLIPTIC = 12  # ecliptic for true equator.

_TOPO = 13  # apparent geocentric

_MERCURY = 14  # from JPL DE table.

_VENUS = 15  #

_MARS = 16  #

_JUPITER = 17  #

_SATURN = 18  #

_NEPTUN = 19  #

_SUN = 20  #

_MOON = 21  #

_HADEC = 22  #

_AZEL = 23  #

_AZELGEO = 24  #

_AZELSW = 25  # topocentric Az/El (N => E).

_AZELNE = 26  # idem AZEL.

_ITRF = 27  # ITRF earth frame.


# their names in a dictionary
_baselineReferenceCodeNames = {}

_baselineReferenceCodeNames[_J2000] = "J2000"

_baselineReferenceCodeNames[_B1950] = "B1950"

_baselineReferenceCodeNames[_GALACTIC] = "GALACTIC"

_baselineReferenceCodeNames[_SUPERGAL] = "SUPERGAL"

_baselineReferenceCodeNames[_ECLIPTIC] = "ECLIPTIC"

_baselineReferenceCodeNames[_JMEAN] = "JMEAN"

_baselineReferenceCodeNames[_JTRUE] = "JTRUE"

_baselineReferenceCodeNames[_APP] = "APP"

_baselineReferenceCodeNames[_BMEAN] = "BMEAN"

_baselineReferenceCodeNames[_BTRUE] = "BTRUE"

_baselineReferenceCodeNames[_JNAT] = "JNAT"

_baselineReferenceCodeNames[_MECLIPTIC] = "MECLIPTIC"

_baselineReferenceCodeNames[_TECLIPTIC] = "TECLIPTIC"

_baselineReferenceCodeNames[_TOPO] = "TOPO"

_baselineReferenceCodeNames[_MERCURY] = "MERCURY"

_baselineReferenceCodeNames[_VENUS] = "VENUS"

_baselineReferenceCodeNames[_MARS] = "MARS"

_baselineReferenceCodeNames[_JUPITER] = "JUPITER"

_baselineReferenceCodeNames[_SATURN] = "SATURN"

_baselineReferenceCodeNames[_NEPTUN] = "NEPTUN"

_baselineReferenceCodeNames[_SUN] = "SUN"

_baselineReferenceCodeNames[_MOON] = "MOON"

_baselineReferenceCodeNames[_HADEC] = "HADEC"

_baselineReferenceCodeNames[_AZEL] = "AZEL"

_baselineReferenceCodeNames[_AZELGEO] = "AZELGEO"

_baselineReferenceCodeNames[_AZELSW] = "AZELSW"

_baselineReferenceCodeNames[_AZELNE] = "AZELNE"

_baselineReferenceCodeNames[_ITRF] = "ITRF"


class BaselineReferenceCode:
    """
    A class for the BaselineReferenceCode enumeration.
    """

    # The value of this BaselineReferenceCode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, baselineReferenceCode):
        # construct a BaselineReferenceCode from an integer, a string, or another BaselineReferenceCode
        # if baselineReferenceCode is a string, convert it to an instance of this class using literal
        if isinstance(baselineReferenceCode, BaselineReferenceCode):
            # copy constructor
            self._value = baselineReferenceCode.getValue()
            self._name = baselineReferenceCode.getName()
        elif isinstance(baselineReferenceCode, str):
            # convert it to an instance of this class using literal
            thisEnum = BaselineReferenceCode.literal(baselineReferenceCode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if baselineReferenceCode not in _baselineReferenceCodeNames:
                raise ValueError("unrecognized BaselineReferenceCode")
            self._value = baselineReferenceCode
            self._name = _baselineReferenceCodeNames[baselineReferenceCode]
            if self._name not in _baselineReferenceCodeDict:
                # add this BaselineReferenceCode as an attribute to this class using its name
                setattr(BaselineReferenceCode, self._name, self)
                _baselineReferenceCodeDict[self._name] = getattr(
                    BaselineReferenceCode, self._name
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
        Returns True if other is a BaselineReferenceCode and its value is the same as this one.
        """
        return isinstance(other, BaselineReferenceCode) and (
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
        the number of known enumerators in BaselineReferenceCode
        """
        return len(_baselineReferenceCodeNames)

    @staticmethod
    def name(baselineReferenceCode):
        """
        Returns the string form of baselineReferenceCode
        """
        return str(baselineReferenceCode)

    @staticmethod
    def names():
        """
        Return the list of all known BaselineReferenceCode enumeration names
        """
        return list(_baselineReferenceCodeNames.values())

    @staticmethod
    def newBaselineReferenceCode(name):
        """
        Equivalent to the literal method
        """
        return BaselineReferenceCode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the BaselineReferenceCode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(BaselineReferenceCode, name):
            raise ValueError("Unrecognized BaselineReferenceCode name")
        return BaselineReferenceCode(getattr(BaselineReferenceCode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a BaselineReferenceCode from an integration matching an enumeration.
        """
        return BaselineReferenceCode(i)


J2000 = BaselineReferenceCode(_J2000)

B1950 = BaselineReferenceCode(_B1950)

GALACTIC = BaselineReferenceCode(_GALACTIC)

SUPERGAL = BaselineReferenceCode(_SUPERGAL)

ECLIPTIC = BaselineReferenceCode(_ECLIPTIC)

JMEAN = BaselineReferenceCode(_JMEAN)

JTRUE = BaselineReferenceCode(_JTRUE)

APP = BaselineReferenceCode(_APP)

BMEAN = BaselineReferenceCode(_BMEAN)

BTRUE = BaselineReferenceCode(_BTRUE)

JNAT = BaselineReferenceCode(_JNAT)

MECLIPTIC = BaselineReferenceCode(_MECLIPTIC)

TECLIPTIC = BaselineReferenceCode(_TECLIPTIC)

TOPO = BaselineReferenceCode(_TOPO)

MERCURY = BaselineReferenceCode(_MERCURY)

VENUS = BaselineReferenceCode(_VENUS)

MARS = BaselineReferenceCode(_MARS)

JUPITER = BaselineReferenceCode(_JUPITER)

SATURN = BaselineReferenceCode(_SATURN)

NEPTUN = BaselineReferenceCode(_NEPTUN)

SUN = BaselineReferenceCode(_SUN)

MOON = BaselineReferenceCode(_MOON)

HADEC = BaselineReferenceCode(_HADEC)

AZEL = BaselineReferenceCode(_AZEL)

AZELGEO = BaselineReferenceCode(_AZELGEO)

AZELSW = BaselineReferenceCode(_AZELSW)

AZELNE = BaselineReferenceCode(_AZELNE)

ITRF = BaselineReferenceCode(_ITRF)
