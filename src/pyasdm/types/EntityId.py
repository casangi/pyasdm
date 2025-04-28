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
# File EntityId.py
#

import re

# regular expressions used to validate an EntityId string
_ALMAbasicUIDRegex = re.compile(
    "^[uU][iI][dD]://[0-9a-zA-Z]+(/[xX][0-9a-fA-F]+){2}(#\\w{1,}){0,}$"
)
_EVLAbasicUIDRegex = re.compile("^[uU][iI][dD]:///?evla/[0-9a-zA-Z]+/.+$")
# note that the Java implementation implies this re here:
# _EVLAbasicUIDRegex = re.compile("^[uU][iI][dD]:///?evla/(bdf|sdm)/.+$")
# the c++ version was chosen because CASA uses those classes regularly


class EntityId:
    """
    Adapted from the java and c++ implementations of this class.
    """

    # the value of the EntityId, a string
    _id = ""

    @staticmethod
    def validate(candidateId):
        """
        check that candidateId is a valid EntityId
        A valid EntityId must be a string and a match must be found using
        one of the two regular expressions in this class.
        If candidateId is valid then this function returns None, otherwise
        a message is returned that can be used to throw an exception
        for an invalid EntityId
        """
        if not isinstance(candidateId, str):
            return "The UID is not a string (not shown here)"

        if _ALMAbasicUIDRegex.match(candidateId) or _EVLAbasicUIDRegex.match(
            candidateId
        ):
            # this IS valid
            return None

        return "The UID '" + candidateId + "' is not well formed"

    def __init__(self, *args):
        """
        Initialize an EntityId.
        No arguments: a Null EntityId
        A single argument:
           An EntityId, copy the value to this one.
           A string, if valid, initialze this one with that string.
        If the argument is of the wrong type, an invalid string, or
        there is more than one argument then a ValueError is raised.
        """
        if len(args) > 1:
            raise ValueError("EntityId : too many arguments, zero or 1 expected")

        if len(args) == 0:
            # not necessary, but just in case
            self._id = ""
        else:
            # must be a single argument
            thisArg = args[0]
            if isinstance(thisArg, EntityId):
                self._id = thisArg._id
            elif isinstance(thisArg, str):
                msg = self.validate(thisArg)
                if msg is not None:
                    raise ValueError(msg)
                self._id = thisArg
            else:
                # invalid type
                raise ValueError("EntityId : argument must be an EntityId or str")

    def __str__(self):
        """
        returns the value
        """
        return self._id

    @staticmethod
    def fromBin(ein):
        """
        Create and return an EntityId from an EndianInput instance.
        """
        return EntityId(ein.readString())

    def toBin(self, eout):
        """
        Write this EntityId to an EndianOutput instance.
        """
        eout.writeString(self._id)

    def equals(self, id):
        """
        returns True if id is EntityId with a value equal to this EntityId, else False.
        """
        return isinstance(id, EntityId) and (self._id == id._id)

    def isNull(self):
        """
        return True if the value is an empty string, else False
        """
        return len(self._id) == 0

    @staticmethod
    def getInstance(stringList):
        """
        This mirrors similar functions in the other types.
        This should not be used to construct an EntityId because of the
        complexity of that object. It is included here in case
        the translation from java includes such a use. If used it
        will raise a RuntimeError.
        """
        raise RuntimeError("Entity.getEntityId called, not supported in pyasdm.")
