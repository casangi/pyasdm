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
# File AssociatedFieldNature.py

# to keep track of the attributes added to this class for each value of this enumeration

_associatedFieldNatureDict = {}

# the possible enumerations

_ON = 0  # The associated field is used as ON source data

_OFF = 1  # The associated field is used as OFF source data

_PHASE_REFERENCE = 2  # The associated field is used as Phase reference data


# their names in a dictionary
_associatedFieldNatureNames = {}

_associatedFieldNatureNames[_ON] = "ON"

_associatedFieldNatureNames[_OFF] = "OFF"

_associatedFieldNatureNames[_PHASE_REFERENCE] = "PHASE_REFERENCE"


class AssociatedFieldNature:
    """
    A class for the AssociatedFieldNature enumeration.
    """

    # The value of this AssociatedFieldNature, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, associatedFieldNature):
        # construct a AssociatedFieldNature from an integer, a string, or another AssociatedFieldNature
        # if associatedFieldNature is a string, convert it to an instance of this class using literal
        if isinstance(associatedFieldNature, AssociatedFieldNature):
            # copy constructor
            self._value = associatedFieldNature.getValue()
            self._name = associatedFieldNature.getName()
        elif isinstance(associatedFieldNature, str):
            # convert it to an instance of this class using literal
            thisEnum = AssociatedFieldNature.literal(associatedFieldNature)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if associatedFieldNature not in _associatedFieldNatureNames:
                raise ValueError("unrecognized AssociatedFieldNature")
            self._value = associatedFieldNature
            self._name = _associatedFieldNatureNames[associatedFieldNature]
            if self._name not in _associatedFieldNatureDict:
                # add this AssociatedFieldNature as an attribute to this class using its name
                setattr(AssociatedFieldNature, self._name, self)
                _associatedFieldNatureDict[self._name] = getattr(
                    AssociatedFieldNature, self._name
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
        Returns True if other is a AssociatedFieldNature and its value is the same as this one.
        """
        return isinstance(other, AssociatedFieldNature) and (
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
        the number of known enumerators in AssociatedFieldNature
        """
        return len(_associatedFieldNatureNames)

    @staticmethod
    def name(associatedFieldNature):
        """
        Returns the string form of associatedFieldNature
        """
        return str(associatedFieldNature)

    @staticmethod
    def names():
        """
        Return the list of all known AssociatedFieldNature enumeration names
        """
        return list(_associatedFieldNatureNames.values())

    @staticmethod
    def newAssociatedFieldNature(name):
        """
        Equivalent to the literal method
        """
        return AssociatedFieldNature.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the AssociatedFieldNature enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(AssociatedFieldNature, name):
            raise ValueError("Unrecognized AssociatedFieldNature name")
        return AssociatedFieldNature(getattr(AssociatedFieldNature, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a AssociatedFieldNature from an integration matching an enumeration.
        """
        return AssociatedFieldNature(i)


ON = AssociatedFieldNature(_ON)

OFF = AssociatedFieldNature(_OFF)

PHASE_REFERENCE = AssociatedFieldNature(_PHASE_REFERENCE)
