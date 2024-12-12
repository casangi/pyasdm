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
# File ProcessorSubType.py

# to keep track of the attributes added to this class for each value of this enumeration

_processorSubTypeDict = {}

# the possible enumerations

_ALMA_CORRELATOR_MODE = 0  # ALMA correlator.

_SQUARE_LAW_DETECTOR = 1  # Square law detector.

_HOLOGRAPHY = 2  # Holography.

_ALMA_RADIOMETER = 3  # ALMA radiometer.


# their names in a dictionary
_processorSubTypeNames = {}

_processorSubTypeNames[_ALMA_CORRELATOR_MODE] = "ALMA_CORRELATOR_MODE"

_processorSubTypeNames[_SQUARE_LAW_DETECTOR] = "SQUARE_LAW_DETECTOR"

_processorSubTypeNames[_HOLOGRAPHY] = "HOLOGRAPHY"

_processorSubTypeNames[_ALMA_RADIOMETER] = "ALMA_RADIOMETER"


class ProcessorSubType:
    """
    A class for the ProcessorSubType enumeration.
    """

    # The value of this ProcessorSubType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, processorSubType):
        # construct a ProcessorSubType from an integer, a string, or another ProcessorSubType
        # if processorSubType is a string, convert it to an instance of this class using literal
        if isinstance(processorSubType, ProcessorSubType):
            # copy constructor
            self._value = processorSubType.getValue()
            self._name = processorSubType.getName()
        elif isinstance(processorSubType, str):
            # convert it to an instance of this class using literal
            thisEnum = ProcessorSubType.literal(processorSubType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if processorSubType not in _processorSubTypeNames:
                raise ValueError("unrecognized ProcessorSubType")
            self._value = processorSubType
            self._name = _processorSubTypeNames[processorSubType]
            if self._name not in _processorSubTypeDict:
                # add this ProcessorSubType as an attribute to this class using its name
                setattr(ProcessorSubType, self._name, self)
                _processorSubTypeDict[self._name] = getattr(
                    ProcessorSubType, self._name
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
        the number of known enumerators in ProcessorSubType
        """
        return len(_processorSubTypeNames)

    @staticmethod
    def name(processorSubType):
        """
        Returns the string form of the ProcessorSubType
        """
        return processorSubType.getName()

    @staticmethod
    def toString(processorSubType):
        """
        Equivalent to the name method
        """
        return ProcessorSubType.name(processorSubType)

    @staticmethod
    def names():
        """
        Return the list of all known ProcessorSubType enumeration names
        """
        return list(_processorSubTypeNames.values())

    @staticmethod
    def newProcessorSubType(name):
        """
        Equivalent to the literal method
        """
        return ProcessorSubType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the ProcessorSubType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(ProcessorSubType, name):
            raise ValueError("Unrecognized ProcessorSubType name")
        return ProcessorSubType(getattr(ProcessorSubType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a ProcessorSubType from an integration matching an enumeration.
        """
        return ProcessorSubType(i)


ALMA_CORRELATOR_MODE = ProcessorSubType(_ALMA_CORRELATOR_MODE)

SQUARE_LAW_DETECTOR = ProcessorSubType(_SQUARE_LAW_DETECTOR)

HOLOGRAPHY = ProcessorSubType(_HOLOGRAPHY)

ALMA_RADIOMETER = ProcessorSubType(_ALMA_RADIOMETER)
