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
# File DetectorBandType.py

# to keep track of the attributes added to this class for each value of this enumeration

_detectorBandTypeDict = {}

# the possible enumerations

_BASEBAND = 0  # Detector in Baseband Processor

_DOWN_CONVERTER = 1  # Detector in Down - Converter

_HOLOGRAPHY_RECEIVER = 2  # Detector in Holography Receiver

_SUBBAND = 3  # Detector in subband (tunable digital filter).


# their names in a dictionary
_detectorBandTypeNames = {}

_detectorBandTypeNames[_BASEBAND] = "BASEBAND"

_detectorBandTypeNames[_DOWN_CONVERTER] = "DOWN_CONVERTER"

_detectorBandTypeNames[_HOLOGRAPHY_RECEIVER] = "HOLOGRAPHY_RECEIVER"

_detectorBandTypeNames[_SUBBAND] = "SUBBAND"


class DetectorBandType:
    """
    A class for the DetectorBandType enumeration.
    """

    # The value of this DetectorBandType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, detectorBandType):
        # construct a DetectorBandType from an integer, a string, or another DetectorBandType
        # if detectorBandType is a string, convert it to an instance of this class using literal
        if isinstance(detectorBandType, DetectorBandType):
            # copy constructor
            self._value = detectorBandType.getValue()
            self._name = detectorBandType.getName()
        elif isinstance(detectorBandType, str):
            # convert it to an instance of this class using literal
            thisEnum = DetectorBandType.literal(detectorBandType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if detectorBandType not in _detectorBandTypeNames:
                raise ValueError("unrecognized DetectorBandType")
            self._value = detectorBandType
            self._name = _detectorBandTypeNames[detectorBandType]
            if self._name not in _detectorBandTypeDict:
                # add this DetectorBandType as an attribute to this class using its name
                setattr(DetectorBandType, self._name, self)
                _detectorBandTypeDict[self._name] = getattr(
                    DetectorBandType, self._name
                )

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
        the number of known enumerators in DetectorBandType
        """
        return len(_detectorBandTypeNames)

    @staticmethod
    def name(detectorBandType):
        """
        Returns the string form of the DetectorBandType
        """
        return detectorBandType.getName()

    @staticmethod
    def toString(detectorBandType):
        """
        Equivalent to the name method
        """
        return DetectorBandType.name(detectorBandType)

    @staticmethod
    def names():
        """
        Return the list of all known DetectorBandType enumeration names
        """
        return list(_detectorBandTypeNames.values())

    @staticmethod
    def newDetectorBandType(name):
        """
        Equivalent to the literal method
        """
        return DetectorBandType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the DetectorBandType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(DetectorBandType, name):
            raise ValueError("Unrecognized DetectorBandType name")
        return DetectorBandType(getattr(DetectorBandType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a DetectorBandType from an integration matching an enumeration.
        """
        return DetectorBandType(i)


BASEBAND = DetectorBandType(_BASEBAND)

DOWN_CONVERTER = DetectorBandType(_DOWN_CONVERTER)

HOLOGRAPHY_RECEIVER = DetectorBandType(_HOLOGRAPHY_RECEIVER)

SUBBAND = DetectorBandType(_SUBBAND)
