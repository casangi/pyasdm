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
# File PartId.py

# adapted from the original c++ and Java


class PartId:

    # the string representation
    _id = ""

    @staticmethod
    def validate(idStr):
        """
        validate idStr, which must be a string or None
        If idStr has an invalid format or is not a string a string message is returned
        If idStr is valid, None is returned
        """
        if idStr is None:
            return None

        if not isinstance(idStr, str):
            return "provided id is not a string and can not be used as a PartID"

        if len(idStr) == 0:
            return None

        if (len(idStr)) != 9 or (idStr[0] != "X"):
            return "Invalid format for PartId: " + idStr

        # there's certainly a regex way to do this, but this is how Java and c++ do it so sticking with that
        for i in range(1, 9):
            thisChar = idStr[i]
            ok = (thisChar >= "0" and thisChar <= "9") or (
                thisChar >= "a" and thisChar <= "f"
            )
            if not ok:
                return "Invalid format for PartId: " + idStr

        return None

    def __init__(self, id=None):
        """
        Create a PartId from id.
        If id is None, a null PartId is created.
        If id is another PartID, make a copy.
        If id is a string, constrict a PartId from it after validating it has the expected format.
        Anything else or an invalid string results in a ValueError
        """
        _id = ""
        if id is None:
            # nothing more to do
            pass
        elif isinstance(id, PartId):
            self._id = id._id
        else:
            self.setId(id)

    def __str__(self):
        return self._id

    def toBin(self, eos):
        """
        Write the binary representation of this into an EndianOutput stream
        """
        eos.writeString(self._id)

    @staticmethod
    def fromBin(eis):
        """
        Read the binary representation of a PartId from an EndianInput stream
        and return the PartId
        """
        return PartId(eis.readString())

    def equals(self, other):
        return isinstance(other, PartId) and (other._id == self._id)

    def setId(self, idStr):
        """
        Set this PartId to the value in idStr.
        idStr can be None or a valid string.
        If string is invalid a ValueError will be raised
        """
        msg = PartId.validate(idStr)
        if msg != None:
            raise ValueError(msg)
        # make sure it's a string
        if idStr is None:
            idStr = ""
        self._id = idStr
