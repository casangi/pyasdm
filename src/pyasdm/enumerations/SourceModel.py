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
# File SourceModel.py

# to keep track of the attributes added to this class for each value of this enumeration

_sourceModelDict = {}

# the possible enumerations

_GAUSSIAN = 0  # Gaussian source

_POINT = 1  # Point Source

_DISK = 2  # Uniform Disk


# their names in a dictionary
_sourceModelNames = {}

_sourceModelNames[_GAUSSIAN] = "GAUSSIAN"

_sourceModelNames[_POINT] = "POINT"

_sourceModelNames[_DISK] = "DISK"


class SourceModel:
    """
    A class for the SourceModel enumeration.
    """

    # The value of this SourceModel, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, sourceModel):
        # construct a SourceModel from an integer, a string, or another SourceModel
        # if sourceModel is a string, convert it to an instance of this class using literal
        if isinstance(sourceModel, SourceModel):
            # copy constructor
            self._value = sourceModel.getValue()
            self._name = sourceModel.getName()
        elif isinstance(sourceModel, str):
            # convert it to an instance of this class using literal
            thisEnum = SourceModel.literal(sourceModel)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if sourceModel not in _sourceModelNames:
                raise ValueError("unrecognized SourceModel")
            self._value = sourceModel
            self._name = _sourceModelNames[sourceModel]
            if self._name not in _sourceModelDict:
                # add this SourceModel as an attribute to this class using its name
                setattr(SourceModel, self._name, self)
                _sourceModelDict[self._name] = getattr(SourceModel, self._name)

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
        Returns True if other is a SourceModel and its value is the same as this one.
        """
        return isinstance(other, SourceModel) and (other.getValue() == self.getValue())

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
        the number of known enumerators in SourceModel
        """
        return len(_sourceModelNames)

    @staticmethod
    def name(sourceModel):
        """
        Returns the string form of sourceModel
        """
        return str(sourceModel)

    @staticmethod
    def names():
        """
        Return the list of all known SourceModel enumeration names
        """
        return list(_sourceModelNames.values())

    @staticmethod
    def newSourceModel(name):
        """
        Equivalent to the literal method
        """
        return SourceModel.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the SourceModel enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(SourceModel, name):
            raise ValueError("Unrecognized SourceModel name")
        return SourceModel(getattr(SourceModel, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a SourceModel from an integration matching an enumeration.
        """
        return SourceModel(i)


GAUSSIAN = SourceModel(_GAUSSIAN)

POINT = SourceModel(_POINT)

DISK = SourceModel(_DISK)
