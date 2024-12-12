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
# File CorrelatorName.py

# to keep track of the attributes added to this class for each value of this enumeration

_correlatorNameDict = {}

# the possible enumerations

_ALMA_ACA = 0  # ACA correlator

_ALMA_ACASPEC = 1  # ACA spectrometer

_ALMA_BASELINE = 2  #

_ALMA_BASELINE_ATF = 3  #

_ALMA_BASELINE_PROTO_OSF = 4  #

_HERSCHEL = 5  #

_IRAM_PDB = 6  #

_IRAM_30M_VESPA = 7  # Up to 18000 channels.

_IRAM_WILMA = 8  # 2 MHz, 18x930 MHz, HERA (wide)

_NRAO_VLA = 9  # VLA correlator.

_NRAO_WIDAR = 10  # EVLA correlator.


# their names in a dictionary
_correlatorNameNames = {}

_correlatorNameNames[_ALMA_ACA] = "ALMA_ACA"

_correlatorNameNames[_ALMA_ACASPEC] = "ALMA_ACASPEC"

_correlatorNameNames[_ALMA_BASELINE] = "ALMA_BASELINE"

_correlatorNameNames[_ALMA_BASELINE_ATF] = "ALMA_BASELINE_ATF"

_correlatorNameNames[_ALMA_BASELINE_PROTO_OSF] = "ALMA_BASELINE_PROTO_OSF"

_correlatorNameNames[_HERSCHEL] = "HERSCHEL"

_correlatorNameNames[_IRAM_PDB] = "IRAM_PDB"

_correlatorNameNames[_IRAM_30M_VESPA] = "IRAM_30M_VESPA"

_correlatorNameNames[_IRAM_WILMA] = "IRAM_WILMA"

_correlatorNameNames[_NRAO_VLA] = "NRAO_VLA"

_correlatorNameNames[_NRAO_WIDAR] = "NRAO_WIDAR"


class CorrelatorName:
    """
    A class for the CorrelatorName enumeration.
    """

    # The value of this CorrelatorName, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, correlatorName):
        # construct a CorrelatorName from an integer, a string, or another CorrelatorName
        # if correlatorName is a string, convert it to an instance of this class using literal
        if isinstance(correlatorName, CorrelatorName):
            # copy constructor
            self._value = correlatorName.getValue()
            self._name = correlatorName.getName()
        elif isinstance(correlatorName, str):
            # convert it to an instance of this class using literal
            thisEnum = CorrelatorName.literal(correlatorName)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if correlatorName not in _correlatorNameNames:
                raise ValueError("unrecognized CorrelatorName")
            self._value = correlatorName
            self._name = _correlatorNameNames[correlatorName]
            if self._name not in _correlatorNameDict:
                # add this CorrelatorName as an attribute to this class using its name
                setattr(CorrelatorName, self._name, self)
                _correlatorNameDict[self._name] = getattr(CorrelatorName, self._name)

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
        the number of known enumerators in CorrelatorName
        """
        return len(_correlatorNameNames)

    @staticmethod
    def name(correlatorName):
        """
        Returns the string form of the CorrelatorName
        """
        return correlatorName.getName()

    @staticmethod
    def toString(correlatorName):
        """
        Equivalent to the name method
        """
        return CorrelatorName.name(correlatorName)

    @staticmethod
    def names():
        """
        Return the list of all known CorrelatorName enumeration names
        """
        return list(_correlatorNameNames.values())

    @staticmethod
    def newCorrelatorName(name):
        """
        Equivalent to the literal method
        """
        return CorrelatorName.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the CorrelatorName enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(CorrelatorName, name):
            raise ValueError("Unrecognized CorrelatorName name")
        return CorrelatorName(getattr(CorrelatorName, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a CorrelatorName from an integration matching an enumeration.
        """
        return CorrelatorName(i)


ALMA_ACA = CorrelatorName(_ALMA_ACA)

ALMA_ACASPEC = CorrelatorName(_ALMA_ACASPEC)

ALMA_BASELINE = CorrelatorName(_ALMA_BASELINE)

ALMA_BASELINE_ATF = CorrelatorName(_ALMA_BASELINE_ATF)

ALMA_BASELINE_PROTO_OSF = CorrelatorName(_ALMA_BASELINE_PROTO_OSF)

HERSCHEL = CorrelatorName(_HERSCHEL)

IRAM_PDB = CorrelatorName(_IRAM_PDB)

IRAM_30M_VESPA = CorrelatorName(_IRAM_30M_VESPA)

IRAM_WILMA = CorrelatorName(_IRAM_WILMA)

NRAO_VLA = CorrelatorName(_NRAO_VLA)

NRAO_WIDAR = CorrelatorName(_NRAO_WIDAR)
