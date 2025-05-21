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
# File PrimitiveDataType.py

# to keep track of the attributes added to this class for each value of this enumeration

_primitiveDataTypeDict = {}

# the possible enumerations

_INT16_TYPE = 0  # 2 bytes signed integer (short).

_INT32_TYPE = 1  # 4 bytes signed integer (int).

_INT64_TYPE = 2  # 8 bytes signed integer (long long).

_FLOAT32_TYPE = 3  # 4 bytes float (float).

_FLOAT64_TYPE = 4  # 8 bytes float (double).


# their names in a dictionary
_primitiveDataTypeNames = {}

_primitiveDataTypeNames[_INT16_TYPE] = "INT16_TYPE"

_primitiveDataTypeNames[_INT32_TYPE] = "INT32_TYPE"

_primitiveDataTypeNames[_INT64_TYPE] = "INT64_TYPE"

_primitiveDataTypeNames[_FLOAT32_TYPE] = "FLOAT32_TYPE"

_primitiveDataTypeNames[_FLOAT64_TYPE] = "FLOAT64_TYPE"


class PrimitiveDataType:
    """
    A class for the PrimitiveDataType enumeration.
    """

    # The value of this PrimitiveDataType, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, primitiveDataType):
        # construct a PrimitiveDataType from an integer, a string, or another PrimitiveDataType
        # if primitiveDataType is a string, convert it to an instance of this class using literal
        if isinstance(primitiveDataType, PrimitiveDataType):
            # copy constructor
            self._value = primitiveDataType.getValue()
            self._name = primitiveDataType.getName()
        elif isinstance(primitiveDataType, str):
            # convert it to an instance of this class using literal
            thisEnum = PrimitiveDataType.literal(primitiveDataType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if primitiveDataType not in _primitiveDataTypeNames:
                raise ValueError("unrecognized PrimitiveDataType")
            self._value = primitiveDataType
            self._name = _primitiveDataTypeNames[primitiveDataType]
            if self._name not in _primitiveDataTypeDict:
                # add this PrimitiveDataType as an attribute to this class using its name
                setattr(PrimitiveDataType, self._name, self)
                _primitiveDataTypeDict[self._name] = getattr(
                    PrimitiveDataType, self._name
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
        Returns True if other is a PrimitiveDataType and its value is the same as this one.
        """
        return isinstance(other, PrimitiveDataType) and (
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
        the number of known enumerators in PrimitiveDataType
        """
        return len(_primitiveDataTypeNames)

    @staticmethod
    def name(primitiveDataType):
        """
        Returns the string form of primitiveDataType
        """
        return str(primitiveDataType)

    @staticmethod
    def names():
        """
        Return the list of all known PrimitiveDataType enumeration names
        """
        return list(_primitiveDataTypeNames.values())

    @staticmethod
    def newPrimitiveDataType(name):
        """
        Equivalent to the literal method
        """
        return PrimitiveDataType.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the PrimitiveDataType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(PrimitiveDataType, name):
            raise ValueError("Unrecognized PrimitiveDataType name")
        return PrimitiveDataType(getattr(PrimitiveDataType, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a PrimitiveDataType from an integration matching an enumeration.
        """
        return PrimitiveDataType(i)


INT16_TYPE = PrimitiveDataType(_INT16_TYPE)

INT32_TYPE = PrimitiveDataType(_INT32_TYPE)

INT64_TYPE = PrimitiveDataType(_INT64_TYPE)

FLOAT32_TYPE = PrimitiveDataType(_FLOAT32_TYPE)

FLOAT64_TYPE = PrimitiveDataType(_FLOAT64_TYPE)
