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
# File PostProcessingIntent.py

# to keep track of the attributes added to this class for each value of this enumeration

_postProcessingIntentDict = {}

# the possible enumerations

_CONTINUUM = 0  # continuum

_CUBE = 1  # cube

_CUBE_HANNING = 2  # cube hanning


# their names in a dictionary
_postProcessingIntentNames = {}

_postProcessingIntentNames[_CONTINUUM] = "CONTINUUM"

_postProcessingIntentNames[_CUBE] = "CUBE"

_postProcessingIntentNames[_CUBE_HANNING] = "CUBE_HANNING"


class PostProcessingIntent:
    """
    A class for the PostProcessingIntent enumeration.
    """

    # The value of this PostProcessingIntent, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, postProcessingIntent):
        # construct a PostProcessingIntent from an integer, a string, or another PostProcessingIntent
        # if postProcessingIntent is a string, convert it to an instance of this class using literal
        if isinstance(postProcessingIntent, PostProcessingIntent):
            # copy constructor
            self._value = postProcessingIntent.getValue()
            self._name = postProcessingIntent.getName()
        elif isinstance(postProcessingIntent, str):
            # convert it to an instance of this class using literal
            thisEnum = PostProcessingIntent.literal(postProcessingIntent)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if postProcessingIntent not in _postProcessingIntentNames:
                raise ValueError("unrecognized PostProcessingIntent")
            self._value = postProcessingIntent
            self._name = _postProcessingIntentNames[postProcessingIntent]
            if self._name not in _postProcessingIntentDict:
                # add this PostProcessingIntent as an attribute to this class using its name
                setattr(PostProcessingIntent, self._name, self)
                _postProcessingIntentDict[self._name] = getattr(
                    PostProcessingIntent, self._name
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
        Returns True if other is a PostProcessingIntent and its value is the same as this one.
        """
        return isinstance(other, PostProcessingIntent) and (
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
        the number of known enumerators in PostProcessingIntent
        """
        return len(_postProcessingIntentNames)

    @staticmethod
    def name(postProcessingIntent):
        """
        Returns the string form of postProcessingIntent
        """
        return str(postProcessingIntent)

    @staticmethod
    def names():
        """
        Return the list of all known PostProcessingIntent enumeration names
        """
        return list(_postProcessingIntentNames.values())

    @staticmethod
    def newPostProcessingIntent(name):
        """
        Equivalent to the literal method
        """
        return PostProcessingIntent.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the PostProcessingIntent enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(PostProcessingIntent, name):
            raise ValueError("Unrecognized PostProcessingIntent name")
        return PostProcessingIntent(getattr(PostProcessingIntent, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a PostProcessingIntent from an integration matching an enumeration.
        """
        return PostProcessingIntent(i)


CONTINUUM = PostProcessingIntent(_CONTINUUM)

CUBE = PostProcessingIntent(_CUBE)

CUBE_HANNING = PostProcessingIntent(_CUBE_HANNING)
