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

from .EntityId import EntityId

from xml.dom import minidom


class Entity:
    """
    The Entity class is an identification of a persistant
    entity in the ALMA archive. It easily maps onto an EntityT
    object in the ACS system entities.

    Adapted from the c++ and Java implementations of this class.
    """

    # TBD : use of StringTokenizer in getEntity

    # the internal representation of an Entity
    _entityId = EntityId()
    _entityIdEncrypted = ""
    _entityTypeName = ""
    _entityVersion = ""
    _instanceVersion = ""

    def __init__(self, *args):
        """
        Initialize an EntityId.
        No arguments: a Null EntityID and empty strings
        A string: interpret this as XML previously from a toString method
        EntityId, string, string, string, string : entityId, entityIdEncrypted, entityTypeName, entityVersion, instanceVersin
        Anything else raises a ValueError
        """
        if len(args) == 0:
            # should not be necessary given values set previously, but just in case
            self._entityId = EntityId()
            self._entityIdEncrypted = ""
            self._entityTypeName = ""
            self._entityVersion = ""
            self._instanceVersion = ""
        elif len(args) == 1:
            if isinstance(args[0], Entity):
                # copy constructor
                thisArg = args[0]
                self._entityId = thisArg._entityId
                self._entityIdEncrypted = thisArg._entityIdEncrypted
                self._entityTypeName = thisArg._entityTypeName
                self._entityVersion = thisArg._entityVersion
                self._instanceVersion = thisArg._instanceVersion
            else:
                # additional type checking happens in setFromXML
                self.setFromXML(args[0])
        elif len(args) == 5:
            # type checking happens in the set methods
            self.setEntityId(args[0])
            self.setEntityIdEncrypted(args[1])
            self.setEntityTypeName(args[2])
            self.setEntityVersion(args[3])
            self.setInstanceVersion(args[4])
        else:
            raise ValueError("Entity : invalid number of arguments, 0, 1 or 5 expected")

    def toString(self):
        """
        Synonymous with toXML
        """
        return self.toXML()

    def toXML(self):
        """
        Return the values of this Entity as an XML-formatted string.
        """
        msg = self._validXML()
        if msg is not None:
            raise RuntimeError("Entity.toXML : " + msg)
        s = '<Entity entityId="' + self._entityId.toString()
        s += '" entityIdEncrypted="' + self._entityIdEncrypted
        s += '" entityTypeName="' + self._entityTypeName
        s += '" schemaVersion="' + self._entityVersion
        s += '" documentVersion="' + self._instanceVersion
        s += '"/>'

        return s

    def setFromXML(self, xmlString):
        if not isinstance(xmlString, str):
            raise ValueError(
                "Entity.setFromXML argument is not a string. type="
                + str(type(xmlString))
            )
        try:
            xmlDom = minidom.parseString(xmlString)
            # this does not check if there's more than one Entity here
            entityEl = xmlDom.getElementsByTagName("Entity")[0]
            self._entityId = EntityId(entityEl.getAttribute("entityId"))
            self._entityIdEncrypted = entityEl.getAttribute("entityIdEncrypted")
            self._entityTypeName = entityEl.getAttribute("entityTypeName")
            self._entityVersion = entityEl.getAttribute("schemaVersion")
            self._instanceVersion = entityEl.getAttribute("documentVersion")
        except Exception as exc:
            msg = "Entity.setFromXML() invalid Entity XML string." + str(exc)
            raise ValueError(msg) from None

    def _validXML(self):
        """
        Internal method to check for a valid value for use in creating the XML string
        Returns a non-null string if there are errors in the values (null EntityID or
        empty string).
        """
        if (
            self._entityId.isNull()
            or (len(self._entityIdEncrypted) == 0)
            or (len(self._entityTypeName) == 0)
            or (len(self._entityVersion) == 0)
            or (len(self._instanceVersion) == 0)
        ):
            return "Null values detectect in Entity " + self._entityId.toString()

        # this check for a valid entityId and returns it
        return self._entityId.validate(self._entityId.toString())

    @staticmethod
    def fromBin(ein):
        """
        Create and return an Entity from an EndianInput instance.
        """
        # I don't trust the order that these might be evaluated if done in
        # the entity constructor

        idString = ein.readString()
        idEncrypted = ein.readString()
        idTypeName = ein.readString()
        version = ein.readString()
        instanceVers = ein.readString()
        entity = Entity(idString, idEncrypted, idTypeName, version, instanceVers)
        return entity

    def toBin(self, eout):
        """
        Write this Entity out to an EndianOutput instance.
        """
        self._entityId.toBin(eout)
        eout.writeString(self._entityIdEncrypted)
        eout.writeString(self._entityTypeName)
        eout.writeString(self._entityVersion)
        eout.writeString(self._instanceVersion)

    def equals(self, entity):
        """
        Returns True if entity is an Entity and it's values are equal to this Entity
        """
        if not isinstance(entity, Entity):
            return False

        return (
            self._entityId.equals(entity.getEntityId())
            and (self._entityIdEncrypted == entity._entityIdEncrypted)
            and (self._entityTypeName == entity._entityTypeName)
            and (self._entityVersion == entity._entityVersion)
            and (self._instanceVersion == entity._instanceVersion)
        )

    def isNull(self):
        """
        Return True if the entityId is null
        """
        return self._entityId.isNull()

    def getEntityId(self):
        return self._entityId

    def setEntityId(self, entityId):
        """
        Set the entityId, an EntityId or a valid string can be used.
        """
        self._entityId = EntityId(entityId)

    def getEntityIdEncrypted(self):
        return self._entityIdEncrypted

    def setEntityIdEncrypted(self, entityIdEncrypted):
        if not isinstance(entityIdEncrypted, str):
            raise ValueError("entityIdEncrypted is not a string")
        self._entityIdEncrypted = entityIdEncrypted

    def getEntityTypeName(self):
        return self._entityTypeName

    def setEntityTypeName(self, entityTypeName):
        if not isinstance(entityTypeName, str):
            raise ValueError("entityTypeName is not a string")
        self._entityTypeName = entityTypeName

    def getEntityVersion(self):
        return self._entityVersion

    def setEntityVersion(self, entityVersion):
        if not isinstance(entityVersion, str):
            raise ValueError("entityVersion is not a string")
        self._entityVersion = entityVersion

    def getInstanceVersion(self):
        return self._instanceVersion

    def setInstanceVersion(self, instanceVersion):
        if not isinstance(instanceVersion, str):
            raise ValueError("instanceVersion is not a string")
        self._instanceVersion = instanceVersion

    @staticmethod
    def getInstance(stringList):
        """
        This mirrors similar functions in the other types.
        This should not be used to construct an Entity because of the
        complexity of that object. It is included here in case
        the translation from java includes such a use. If used it
        will raise a RuntimeError.
        """
        raise RuntimeError("Entity.getEntity called, not supported in pyasdm.")
