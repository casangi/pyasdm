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
# File ProcessorType.py

# to keep track of the attributes added to this class for each value of this enumeration

_processorTypeDict = {}

# the possible enumerations

_CORRELATOR = 0  # A digital correlator

_RADIOMETER = 1  # A radiometer

_SPECTROMETER = 2  # An (analogue) multi-channel spectrometer


# their names in a dictionary
_processorTypeNames = {}

_processorTypeNames[_CORRELATOR] = "CORRELATOR"

_processorTypeNames[_RADIOMETER] = "RADIOMETER"

_processorTypeNames[_SPECTROMETER] = "SPECTROMETER"


class ProcessorType:
    """
    A class for the ProcessorType enumeration.
    """

    # The value of this ProcessorType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, processorType):
        # construct a ProcessorType from an integer, a string, or another ProcessorType
        # if processorType is a string, convert it to an instance of this class using literal
        if isinstance(processorType, ProcessorType):
            # copy constructor
            self._value = processorType.getValue()
            self._name = processorType.getName()
        elif isinstance(processorType, str):
            # convert it to an instance of this class using literal
            thisEnum = ProcessorType.literal(processorType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if processorType not in _processorTypeNames:
                raise ValueError("unrecognized ProcessorType")
            self._value = processorType
            self._name = _processorTypeNames[processorType]
            if self._name not in _processorTypeDict:
                # add this ProcessorType as an attribute to this class using its name
                setattr(ProcessorType, self._name, self)
                _processorTypeDict[self._name] = getattr(ProcessorType, self._name)

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
        the number of known enumerators in ProcessorType
        """
        return len(_processorTypeNames)

    @staticmethod
    def name(processorType):
        """
        Returns the string form of the ProcessorType
        """
        return processorType.getName()

    @staticmethod
    def toString(processorType):
        """
        Equivalent to the name method
        """
        return ProcessorType.name(processorType)

    @staticmethod
    def names():
        """
        Return the list of all known ProcessorType enumeration names
        """
        return list(_processorTypeNames.values())

    @staticmethod
    def newProcessorType(name):
        """
        Equivalent to the literal method
        """
        return ProcessorType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the ProcessorType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(ProcessorType, name):
            raise ValueError("Unrecognized ProcessorType name")
        return ProcessorType(getattr(ProcessorType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a ProcessorType from an integration matching an enumeration.
        """
        return ProcessorType(i)


CORRELATOR = ProcessorType(_CORRELATOR)

RADIOMETER = ProcessorType(_RADIOMETER)

SPECTROMETER = ProcessorType(_SPECTROMETER)
