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
# File DirectionReferenceCode.py

# to keep track of the attributes added to this class for each value of this enumeration

_directionReferenceCodeDict = {}

# the possible enumerations

_J2000 = 0  # mean equator and equinox at J2000.0

_JMEAN = 1  # mean equator and equinox at frame epoch.

_JTRUE = 2  # true equator and equinox at frame epoch.

_APP = 3  # apparent geocentric position.

_B1950 = 4  # mean epoch and ecliptic at B1950.0.

_B1950_VLA = 5  #

_BMEAN = 6  # mean equator and equinox at frame epoch.

_BTRUE = 7  # true equator and equinox at frame epoch.

_GALACTIC = 8  # galactic coordinates.

_HADEC = 9  # topocentric HA and declination.

_AZELSW = 10  # topocentric Azimuth and Elevation (N through E).

_AZELSWGEO = 11  #

_AZELNE = 12  # idem AZEL

_AZELNEGEO = 13  #

_JNAT = 14  # geocentric natural frame.

_ECLIPTIC = 15  # ecliptic for J2000.0 equator, equinox.

_MECLIPTIC = 16  # ecliptic for mean equator of date.

_TECLIPTIC = 17  # ecliptic for true equatorof date.

_SUPERGAL = 18  # supergalactic coordinates.

_ITRF = 19  # coordinates wrt ITRF earth frame.

_TOPO = 20  # apparent topocentric position.

_ICRS = 21  #

_MERCURY = 22  # from JPL DE table.

_VENUS = 23  #

_MARS = 24  #

_JUPITER = 25  #

_SATURN = 26  #

_URANUS = 27  #

_NEPTUNE = 28  #

_PLUTO = 29  #

_SUN = 30  #

_MOON = 31  #


# their names in a dictionary
_directionReferenceCodeNames = {}

_directionReferenceCodeNames[_J2000] = "J2000"

_directionReferenceCodeNames[_JMEAN] = "JMEAN"

_directionReferenceCodeNames[_JTRUE] = "JTRUE"

_directionReferenceCodeNames[_APP] = "APP"

_directionReferenceCodeNames[_B1950] = "B1950"

_directionReferenceCodeNames[_B1950_VLA] = "B1950_VLA"

_directionReferenceCodeNames[_BMEAN] = "BMEAN"

_directionReferenceCodeNames[_BTRUE] = "BTRUE"

_directionReferenceCodeNames[_GALACTIC] = "GALACTIC"

_directionReferenceCodeNames[_HADEC] = "HADEC"

_directionReferenceCodeNames[_AZELSW] = "AZELSW"

_directionReferenceCodeNames[_AZELSWGEO] = "AZELSWGEO"

_directionReferenceCodeNames[_AZELNE] = "AZELNE"

_directionReferenceCodeNames[_AZELNEGEO] = "AZELNEGEO"

_directionReferenceCodeNames[_JNAT] = "JNAT"

_directionReferenceCodeNames[_ECLIPTIC] = "ECLIPTIC"

_directionReferenceCodeNames[_MECLIPTIC] = "MECLIPTIC"

_directionReferenceCodeNames[_TECLIPTIC] = "TECLIPTIC"

_directionReferenceCodeNames[_SUPERGAL] = "SUPERGAL"

_directionReferenceCodeNames[_ITRF] = "ITRF"

_directionReferenceCodeNames[_TOPO] = "TOPO"

_directionReferenceCodeNames[_ICRS] = "ICRS"

_directionReferenceCodeNames[_MERCURY] = "MERCURY"

_directionReferenceCodeNames[_VENUS] = "VENUS"

_directionReferenceCodeNames[_MARS] = "MARS"

_directionReferenceCodeNames[_JUPITER] = "JUPITER"

_directionReferenceCodeNames[_SATURN] = "SATURN"

_directionReferenceCodeNames[_URANUS] = "URANUS"

_directionReferenceCodeNames[_NEPTUNE] = "NEPTUNE"

_directionReferenceCodeNames[_PLUTO] = "PLUTO"

_directionReferenceCodeNames[_SUN] = "SUN"

_directionReferenceCodeNames[_MOON] = "MOON"


class DirectionReferenceCode:
    """
    A class for the DirectionReferenceCode enumeration.
    """

    # The value of this DirectionReferenceCode, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, directionReferenceCode):
        # construct a DirectionReferenceCode from an integer, a string, or another DirectionReferenceCode
        # if directionReferenceCode is a string, convert it to an instance of this class using literal
        if isinstance(directionReferenceCode, DirectionReferenceCode):
            # copy constructor
            self._value = directionReferenceCode.getValue()
            self._name = directionReferenceCode.getName()
        elif isinstance(directionReferenceCode, str):
            # convert it to an instance of this class using literal
            thisEnum = DirectionReferenceCode.literal(directionReferenceCode)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if directionReferenceCode not in _directionReferenceCodeNames:
                raise ValueError("unrecognized DirectionReferenceCode")
            self._value = directionReferenceCode
            self._name = _directionReferenceCodeNames[directionReferenceCode]
            if self._name not in _directionReferenceCodeDict:
                # add this DirectionReferenceCode as an attribute to this class using its name
                setattr(DirectionReferenceCode, self._name, self)
                _directionReferenceCodeDict[self._name] = getattr(
                    DirectionReferenceCode, self._name
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
        Returns True if other is a DirectionReferenceCode and its value is the same as this one.
        """
        return isinstance(other, DirectionReferenceCode) and (
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
        the number of known enumerators in DirectionReferenceCode
        """
        return len(_directionReferenceCodeNames)

    @staticmethod
    def name(directionReferenceCode):
        """
        Returns the string form of directionReferenceCode
        """
        return str(directionReferenceCode)

    @staticmethod
    def names():
        """
        Return the list of all known DirectionReferenceCode enumeration names
        """
        return list(_directionReferenceCodeNames.values())

    @staticmethod
    def newDirectionReferenceCode(name):
        """
        Equivalent to the literal method
        """
        return DirectionReferenceCode.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the DirectionReferenceCode enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(DirectionReferenceCode, name):
            raise ValueError("Unrecognized DirectionReferenceCode name")
        return DirectionReferenceCode(getattr(DirectionReferenceCode, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a DirectionReferenceCode from an integration matching an enumeration.
        """
        return DirectionReferenceCode(i)


J2000 = DirectionReferenceCode(_J2000)

JMEAN = DirectionReferenceCode(_JMEAN)

JTRUE = DirectionReferenceCode(_JTRUE)

APP = DirectionReferenceCode(_APP)

B1950 = DirectionReferenceCode(_B1950)

B1950_VLA = DirectionReferenceCode(_B1950_VLA)

BMEAN = DirectionReferenceCode(_BMEAN)

BTRUE = DirectionReferenceCode(_BTRUE)

GALACTIC = DirectionReferenceCode(_GALACTIC)

HADEC = DirectionReferenceCode(_HADEC)

AZELSW = DirectionReferenceCode(_AZELSW)

AZELSWGEO = DirectionReferenceCode(_AZELSWGEO)

AZELNE = DirectionReferenceCode(_AZELNE)

AZELNEGEO = DirectionReferenceCode(_AZELNEGEO)

JNAT = DirectionReferenceCode(_JNAT)

ECLIPTIC = DirectionReferenceCode(_ECLIPTIC)

MECLIPTIC = DirectionReferenceCode(_MECLIPTIC)

TECLIPTIC = DirectionReferenceCode(_TECLIPTIC)

SUPERGAL = DirectionReferenceCode(_SUPERGAL)

ITRF = DirectionReferenceCode(_ITRF)

TOPO = DirectionReferenceCode(_TOPO)

ICRS = DirectionReferenceCode(_ICRS)

MERCURY = DirectionReferenceCode(_MERCURY)

VENUS = DirectionReferenceCode(_VENUS)

MARS = DirectionReferenceCode(_MARS)

JUPITER = DirectionReferenceCode(_JUPITER)

SATURN = DirectionReferenceCode(_SATURN)

URANUS = DirectionReferenceCode(_URANUS)

NEPTUNE = DirectionReferenceCode(_NEPTUNE)

PLUTO = DirectionReferenceCode(_PLUTO)

SUN = DirectionReferenceCode(_SUN)

MOON = DirectionReferenceCode(_MOON)
