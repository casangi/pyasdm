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
# File EntityRef.py

# adapted from the original c++ and Java

from .PartId import PartId
from .EntityId import EntityId

from xml.dom import minidom

import pyasdm.utils


class EntityRef:
    """
    The EntityRef class is an identification of a persistent
    entity in the ALMA archive. It wasily maps onto an EntiyREfT
    object in ACS system entities.
    """

    _entityId = EntityId()
    _partId = None  # a PartId when not null
    _entityTypeName = None  # the entityTypeName string
    _instanceVersion = None  # the instanceVersion string

    def __init__(self, *args):
        """
        Construct an EntityRef.
        If args is empty, the default EntityRef whose internal parameters are null.
        If args is 1 it may be either a string (XML as produced by toXML) or
        another EntityRef (copy constructor).
        If there are 4 args they are, in order, entityId, partId,
        entityTypeName, and instanceVersion. All strings that express the
        4 components of an EntityRef.
        """
        _entityId = EntityId()
        _partId = None
        _entityTypeName = None
        _instanceVersion = None

        if len(args) == 0:
            # default, nothing to do
            pass
        elif len(args) == 1 and isinstance(args[0], str):
            self.setFromXML(args[0])
        elif len(args) == 1 and isinstance(args[0], EntityRef):
            otherRef = args[0]
            self._entityId = EntityId(otherRef._entityId)
            if otherRef._partId is None:
                # preserve it as unset
                self._partId = None
            else:
                self._partId = PartId(otherRef._partId)
            self._entityTypeName = otherRef._entityTypeName
            self._instanceVersion = otherRef._instanceVersion
        elif len(args) == 4:
            self._entityId = EntityId(args[0])
            self._partId = PartId(args[1])
            self._entityTypeName = str(args[2])
            self._instanceVersion = str(args[3])
        else:
            raise ValueError("unrecognized arguments to EntityRef constructor")

    def __str__(self):
        """
        Return the entityId as a string. Equivalent to toXML.
        """
        return self.toXML()

    def toBin(self, eos):
        """
        Write the binary representation of this into a DataOutput stream.
        """
        self._entityId.toBin(eos)
        self._partId.toBin(eos)
        eos.writeString(self._entityTypeName)
        eos.writeString(self._instanceVersion)

    @staticmethod
    def listToBin(entityRefList, eos):
        """
        Write a list of EntityRef to the EndianOutput.
        Only lists of 1D are supported.
        """
        if not isinstance(entityRefList, list):
            raise ValueError("entityRefList is not a list")

        listDims = pyasdm.utils.getListDims(entityRefList)
        if len(listDims) != 1:
            raise ValueError("only 1D lists of EntityRef are supported.")

        EntityRef.listTo1DBin(entityRefList, eos)

    @staticmethod
    def listTo1DBin(entityRefList, eos):
        """
        Write a 1D list of EntityRef to the EndianOutput
        """
        if not isinstance(entityRefList, list):
            raise ValueError("entityRefList is not a list")

        # ndim is always written, even for 0-element lists
        eos.writeInt(len(entityRefList))

        # only check the first value
        if (len(entityRefList) > 0) and not isinstance(entityRefList[0], EntityRef):
            raise (ValueError("entityRefList is not a list of EntityRef"))

        for thisEntityRef in entityRefList:
            thisEntityRef.toBin(eos)

    @staticmethod
    def fromBin(eis):
        """
        Read the binary representation of an EntityRef from an EndianInput
        instance and use the read values to set an EntityRef.

        return an EntityRef
        """
        # I don't trust the order that these might be evaluated if done in
        # the EntityRef constructor
        entityId = EntityId.fromBin(eis)
        partId = PartId.fromBin(eis)
        typeName = eis.readString()
        instanceVersion = eis.readString()
        return EntityRef(str(entityId), str(partId), typeName, instanceVersion)

    @staticmethod
    def from1DBin(eis):
        """
        Read a list of EntityRef from an EndianInput instance and return
        the resulting list.
        """
        dim1 = eis.readInt()
        result = []
        for i in range(dim1):
            result.append(EntityRef.fromBin(eis))

        return result

    def toXML(self):
        """
        Return the values of this EntityRef as an XML-formatted string.
        """
        # checks for valid values first
        msg = self.validXML()
        if msg is not None:
            raise RuntimeError(msg)

        result = ""
        result = '<EntityRef entityId="' + str(self._entityId)
        if self._partId is not None:
            result += '" partId="' + str(self._partId)
        result += '" entityTypeName="' + self._entityTypeName
        result += '" documentVersion="' + self._instanceVersion + '"/>'
        return result

    def setFromXML(self, xmlstr):
        """
        Set the values of this EntityRef from an XML formatted as produced by toXML
        """
        if not isinstance(xmlstr, str):
            raise ValueError(
                "EntityRef.setFromXML argument is not a string. type="
                + str(type(xmlstr))
            )
        try:
            xmldom = minidom.parseString(xmlstr)
            # requires that there's at least one EntityRef here and that the one that's desired is the first one
            entityRefEl = xmldom.getElementsByTagName("EntityRef")[0]
            self._entityId = EntityId(entityRefEl.getAttribute("entityId"))
            # partId may be missing if None
            partIdStr = entityRefEl.getAttribute("partId")
            if len(partIdStr) == 0:
                self._partId = None
            else:
                self._partId = PartId(partIdStr)

                self._entityTypeName = entityRefEl.getAttribute("entityTypeName")
                self._instanceVersion = entityRefEl.getAttribute("documentVersion")
        except Exception as exc:
            msg = "EntityRef.setFromXML() invalid EntityRef XML string." + str(exc)
            raise ValueError(msg) from None

        # and validate it
        msg = self.validXML()
        if msg is not None:
            raise ValueError(msg)

    def validXML(self):
        """
        Used internally to validate this EntityRef for conversion to or after
        conversion from an XML string
        If this is invalid a string message is returned, otherwise None is returned.
        """
        # null values, except for partId, are invalid in XML
        if (
            self._entityId.isNull()
            or len(self._entityTypeName) == 0
            or len(self._instanceVersion) == 0
        ):
            return "Null values detected in EntityRef " + str(self._entityId)

        # I think this isn't necessary the way these python classes work - caught elsewhere
        msg = EntityId.validate(str(self._entityId))
        if msg is not None:
            return msg

        # if partId is set, it must have the correct format
        if self._partId is not None:
            return PartId.validate(str(self._partId))

        return None

    def equals(self, other):
        """
        Returns True if and only if other is an EntityRef and it's values are all equal to this
        EntityRef.
        """

        if not isinstance(other, EntityRef):
            return False

        # if they're both null then they're equal, but if only one is they're not equal
        if self.isNull():
            if other.isNull():
                return True
            # only one is Null
            return False
        elif other.isNull():
            # only one is Null
            return False

        # a null EntityId has already been dealt with
        result = self._entityId.equals(other._entityId)

        # partId can be null, must be null in both
        if self._partId is None:
            result = result and (other._partId is None)
        else:
            # equals here will return False of other._partId is None
            result = result and self._partId.equals(other._partId)

        result = result and (self._entityTypeName == other._entityTypeName)
        result = result and (self._instanceVersion == other._instanceVersion)

        return result

    def isNull(self):
        """
        Returns True if and only if the entityId is Null
        """
        return self._entityId.isNull()

    # getters and setters
    def getEntityId(self):
        """
        Returns the entityId as a string
        """
        if self.isNull():
            return ""

        return str(self._entityId)

    def setEntityId(self, entityId):
        """
        Sets the entityId to this string, which must be a valid EntityId string
        """
        self._entityId = EntityId(entityId)

    def getPartId(self):
        """
        Returns the partId as a string. If unset, returns None
        """
        if self._partId is None:
            return None
        return str(self._partId)

    def setPartId(self, partId):
        """
        Sets the part to the given string
        """
        self._partId = PartId(partId)

    def getEntityTypeName(self):
        """
        returns the entityTypeName string
        """
        return self._entityTypeName

    def setEntityTypeName(self, entityTypeName):
        """
        sets the entityTypeName to the given string
        """
        self._entityTypeName = entityTypeName

    def getInstanceVersion(self):
        """
        returns the instanceVersion string
        """
        return self._instanceVersion

    def setInstanceVersion(self, instanceVersion):
        """
        sets the instanceVersion to the given string
        """
        self._instanceVersion = instranceVersion

    @staticmethod
    def getInstance(stringList):
        """
        This mirrors similar functions in the other types.
        This should not be used to construct an EntityRef because of the
        complexity of that object. It is included here in case
        the translation from java includes such a use. If used it
        will raise a RuntimeError.
        """
        raise RuntimeError("Entity.getEntityRef called, not supported in pyasdm.")
