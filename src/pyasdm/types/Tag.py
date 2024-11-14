# ALMA - Atacama Large Millimeter Array
# (c) European Southern Observatory, 2024
# (c) Associated Universities Inc., 2024
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
# File Tag.py
#

from .TagType import TagType


class Tag:
    """
    The Tag class is an implementation of a unique index identifying
    a row of an ALMA table.

    Basically a Tag is defined by :

    a value which is an integer
    a type which is a pointer to a TagType

    modeled on java and c++ implementations, original author Allan Farris
    version 2 by Michel Caillat
    """

    _tag = "0"  # the tag, stored as a string
    _type = None  # the type, a TagType

    def __init__(self, *args):
        """
        Construct a Tag.
        No arguments: a null tag
        A single argument that is an integer: a NoType tag using that integer
        A single argument that is a Tag: the copy constructor
        A single argument that is a string: use parseTag, see the rules there
        Two arguments, an integer followed by a TagType
        Anything else is an error
        """
        if len(args) == 0:
            self._tag = "0"
            self._type = None
        elif len(args) == 1:
            thisArg = args[0]
            if isinstance(thisArg, int):
                self._tag = str(thisArg)
                self._type = TagType.NoType
            elif isinstance(thisArg, str):
                thisTag = Tag.parseTag(thisArg)
                self._tag = thisTag._tag
                self._type = thisTag._type
            elif isinstance(thisArg, Tag):
                self._tag = thisArg._tag
                self._type = thisArg._type
            else:
                raise ValueError(
                    "single Tag constructor argument is not an int or a Tag"
                )
        elif len(args) == 2:
            thisTag = args[0]
            thisType = args[1]
            if isinstance(thisTag, int) and isinstance(thisType, TagType):
                self._tag = str(thisTag)
                self._type = thisType
            else:
                raise ValueError(
                    "Tag constructor with two arguments must be an int with a TagType"
                )
        else:
            raise ValueError("Tag constructor takes 0, 1 or 2 arguments")

    @staticmethod
    def parseTag(s):
        """
        Convert the a string argument, s, into a Tag and return that Tag.
        The string must be a valid form: two strings joined by a single '_'.
        A zero-length string is valid and results in a null Tag.
        The first string must be known TagType and the second string must be an integer.
        If the TagType is "null" then this returns a null Tag and the contents of the second
        string is ignored.
        """
        if len(s) == 0 and isinstance(s, str):
            # if there's a zero length something else it will be caught by the split step
            return Tag()

        typeValue = s.split("_")
        if len(typeValue) != 2:
            raise ("Error: '" + s + "' cannot be parsed into a Tag")

        if typeValue[0] == "null":
            return Tag()

        type = TagType.getTagType(typeValue[0])
        if type is None:
            raise (
                "Error: '" + s + "' has an invalid Tag type part '" + typeValue[0] + "'"
            )

        value = 0
        try:
            value = int(typeValue[1])
        except ValueError as exc:
            raise ValueError(
                "Error: '"
                + s
                + "' has an invalid Tag value part '"
                + typeValue[1]
                + "'"
            ) from None

        return Tag(value, type)

    def toString(self):
        """
        Return the Tag as a string.
        The resulting string consists of the string representation of the type followed by an underscore
        followed by the string representation of the value. A null Tag is represented as "null_0".
        Examples: "Antenna_12", "SpectralWindow_0".
        """
        if self.isNull():
            return "null_0"
        return self._type.toString() + "_" + self._tag

    def getTagType(self):
        """
        Returns the type of this Tag. A returned value of None indicates that the Tag is null
        (i.e. isNull() is True)
        In all other cases the returned value is a TagType
        """
        return self._type

    def getTagValue(self):
        """
        Returns the value of this Tag.
        The returned value has no meaning if the Tag is null (it returns 0 in that case).
        """
        if self.isNull():
            return 0
        return int(self._tag)

    def getTag(self):
        """
        Returns the tag value as a string.
        If this is Null then the return value is "0"
        """
        return self._tag

    def equals(self, other):
        """
        Compares this with other using the == operator
        other must be a Tag.
        """
        result = False
        if isinstance(other, Tag):
            result = self == other
        return result

    # operators
    def __eq__(self, other):
        """
        Returns True if and only if the values and types of the two Tags are equal.
        """
        result = False
        if isinstance(other, Tag):
            if self.isNull() or other.isNull():
                # both must be null
                result = self.isNull() and other.isNull()
            else:
                # neither can be null
                if (not self.isNull()) and (not other.isNull()):
                    result = (self._tag == other._tag) and (
                        self._type.toString() == other._type.toString()
                    )
        return result

    def __ne__(self, other):
        """
        Returns True if the values and types of this tag are not equal to those of other, uses the eq operator.
        """
        return not (self == other)

    def __lt__(self, other):
        """
        Return if the value of this Tag is < the value of other. The types are ignored.
        Note that null Tags have a value of 0.
        """
        return self._tag < other._tag

    def __gt__(self, other):
        """
        Return if the value of this Tag is > the value of other. The types are ignored.
        Note that null Tags have a valueof 0.
        """
        return self._tag > other._tag

    def isNull(self):
        """
        Return True if this Tag is null, i.e. if it's TagType field is None
        """
        return self._type is None
