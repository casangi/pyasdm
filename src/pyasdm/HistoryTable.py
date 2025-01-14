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
# Warning!
#  --------------------------------------------------------------------
# | This is generated code!  Do not modify this file.                  |
# | If you do, all changes will be lost when the file is re-generated. |
#  --------------------------------------------------------------------
#
# File HistoryTable.py
#

import pyasdm.ASDM

from .HistoryRow import HistoryRow

# All of the extended types are imported
from pyasdm.types import *

# for BIN input and output
from pyasdm.ByteOrder import ByteOrder
from pyasdm.EndianInput import EndianInput
from pyasdm.EndianOutput import EndianOutput

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey
from .exceptions.UniquenessViolationException import UniquenessViolationException

from xml.dom import minidom

import os
import io


class HistoryTable:
    """
    The HistoryTable class is an Alma table.

    Role
    History information.

    Generated from model's revision -1, branch

    Attributes of History

                 Key


    execBlockId Tag  </TD>



    time ArrayTime  </TD>




                 Value (Mandatory)

    message  str

    priority  str

    origin  str

    objectId  str

    application  str

    cliCommand  str

    appParms  str



    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # The name of this table.
    _tableName = "History"

    # The list of field names that make up key 'key'.
    _key = ["execBlockId", "time"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # archive as bin not used by python implementation
    # _archiveAsBin = False # If True archive binary else archive XML
    _fileAsBin = False  # If True file binary else file XML

    # A data structure to store the HistoryRow s.
    # In all cases we maintain a private list of HistoryRow s.
    _privateRows = []

    # this table has a temporal key with other key fields and no auto-incrementable key
    # context is a dictionary where the key is the key without the temporal field
    # and the value is a list of rows having those key values kept in temporal order
    _context = {}

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    def getKeyName(self):
        """
        Return the list of field names that make up key key
        as a list of strings.
        """
        return self._key

    def Key(self, execBlockId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        """
        result = ""

        result += execBlockId.toString() + "_"

        return result

    def insertByTime(self, x, rowlist):
        """
        Insert a HistoryRow in a list of HistoryRow so that it's ordered by ascending time.

        x The HistoryRow to be inserted.
        rowlist The list where x is to be inserted.

        The inserted row is returned. If x already exists in rowlist then it is not added and
        the row in rowlist is returned.

        If a row matching the the value of time is found in
        rowlist but the other required parameters do not have the same value then
        a DuplicateKey exception is raised.
        """

        # get the start time from the ArrayTime at time found in x
        xTime = x.getTime().get()

        # work out where to add x to rowlist
        if (len(rowlist) == 0) or (xTime > rowlist[-1].getTime().get()):
            # it belongs at the end
            rowlist.append(x)
        elif xTime < rowlist[0].getTime().get():
            # it belongs at the start
            rowlist.insert(0, x)
        else:
            # x is inserted somewhere inside rowlist; let's use a dichotomy
            # method to find the insertion index.

            k0 = 0
            k1 = len(rowlist) - 1

            while k0 != (k1 - 1):
                if xTime == rowlist[k0].getTime().get():
                    if rowlist[k0].equalByRequiredValue(x):
                        # this row already exists at k0, nothing to insert or add, return that row
                        return rowlist[k0]
                    else:
                        # the time matches, but the rest of the required parameters do not
                        raise DuplicateKey("DuplicateKey exception in ", "HistoryTable")
                elif xTime == rowlist[k1].getTime().get():
                    if rowlist[k1].equalByRequiredValue(x):
                        # this row already exists at k0, nothing to insert or add, return that row
                        return rowlist[k1]
                    else:
                        # the time matches, but the rest of the required parameters do not
                        raise DuplicateKey("DuplicateKey exception in ", "HistoryTable")
                else:
                    # make sure new index is an integer
                    newIndex = int((k0 + k1) / 2)
                    if xTime <= rowlist[newIndex].getTime().get():
                        k1 = newIndex
                    else:
                        k0 = newIndex

            if xTime == rowlist[k0].getTime().get():
                if rowlist[k0].equalByRequiredValue(x):
                    # this row already exists at k1, nothing to insert or add, return that row
                    return rowlist[k0]
                else:
                    # the time matches, but the rest of the required parameters do not
                    raise DuplicateKey("DuplicateKey exception in ", "HistoryTable")
            elif xTime == rowlist[k1].getTime().get():
                if rowlist[k1].equalByRequiredValue(x):
                    return rowlist[k1]
                else:
                    # the time matches, but the rest of the required parameters do not
                    raise DuplicateKey("DuplicateKey exception in ", "HistoryTable")

            # if it reaches here, it should be added at k1, after k0
            rowlist.insert(k1, x)

        # if it reaches here then x has already been added to rowlist and it needs to be
        # appended to privateRows and marked as added internally before being returned
        self._privateRows.append(x)
        x.isAdded()
        return x

    def __init__(self, container):
        """
        Create a HistoryTable attached to container.

        container must be a ASDM instance
        All tables must know the container
        """

        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("HistoryTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("HistoryTable")
        self._entity.setEntityVersion("1")
        self._entity.setInstanceVersion("1")

        # the default table has no rows and so is presentInMemory
        self._presentInMemory = True
        self._loadInProgress = False

        self._privateRows = []

        self._context = {}

        self._version = 0

    def setNotPresentInMemory(self):
        """
        Set the state to indicate it is not present in memory and needs to be loaded before being used.
        This is used by the container class when loaded from a file and this table is present with non-zero rows.
        Tables are loaded on demand when the get function in the container for that table is used.
        """
        self._presentInMemory = False

    def checkPresenceInMemory(self):
        """
        Check if the table is present in memory. If not, load the table from the file using the
        directory of the container.
        """
        # NOTE: if setFromFile raises an exception then presentInMemory will remain False
        # and loadInProgress will remain True, preventing another attempt at loading.
        # more complex solutions are then necessary to read that file and it's not worth
        # complicating this code here to handle a need to eventually try again to reload that file
        if not self._presentInMemory and not self._loadInProgress:
            print("History is not present in memory, setting from file")
            self._loadInProgress = True
            self.setFromFile(self.getContainer().getDirectory())
            self._presentInMemory = True
            self._loadInProgress = False

    def getContainer(self):
        """
        Return the container to which this table belongs.
        return a ASDM.
        """
        return self._container

    def size(self):
        """
        Return the number of rows in the table.
        """
        return len(self._privateRows)

    def getName(self):
        """
        Return the name of this table.
        """
        return self._tableName

    def toString(self):
        """
        Returns "HistoryTable" followed by the current size of the table
        between parenthesis.
        Example : HistoryTable(12)
        """
        return "HistoryTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = HistoryRow(self)
        return thisRow

    def add(self, x):
        """
        Add a row to this table.

        If this table contains a row whose attributes (key and mandatory values) are equal to
        this in the row to be added then this returns that previously added row, otherwise
        the row being added is returned.

        If this table contains a row with a key equal to that of the row to be added but
        having different value section from the row to be aded then a DuplicateKey exception
        is raised.

        The row is inserted in the table in such a way that all rows having the same
        value of ( execBlockId ) are stored by ascending time.
        """
        #
        # Is there already a context for this combination of not temporal
        # attributes ?

        if not isinstance(x, HistoryRow):
            raise ValueError("x must be a  HistoryRow instance.")

        keystr = self.Key(x.getExecBlockId())

        if not keystr in self._context:
            # There is not yet a context ...
            # Create and initialize an entry in the context dict for this combination....
            self._context[keystr] = []

        result = insertByTime(x, self._context[keystr])
        return result

    def newRow(
        self,
        execBlockId,
        time,
        message,
        priority,
        origin,
        objectId,
        application,
        cliCommand,
        appParms,
    ):
        """
        Create a new HistoryRow initialized to the specified values.

        The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = HistoryRow(self)

        thisRow.setExecBlockId(execBlockId)

        thisRow.setTime(time)

        thisRow.setMessage(message)

        thisRow.setPriority(priority)

        thisRow.setOrigin(origin)

        thisRow.setObjectId(objectId)

        thisRow.setApplication(application)

        thisRow.setCliCommand(cliCommand)

        thisRow.setAppParms(appParms)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new HistoryRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new HistoryRow with default values for its attributes.
        """

        return HistoryRow(self, row)

    # ====> Append a row to its table.

    def checkAndAdd(self, x):
        """
        A method to append a row to its table, used by input conversion methods.
        Not indended for external use.

        If this table has an autoincrementable attribute then check if
        x verifies the rule of uniqueness and throw exception if not.

        This method is appropriate for the case with a ArrayTime temporal key,
        no auto incrementable attribute, with other values in the key.

        Append x to its table.
        x The row to be appended.
        returns  x.
        """
        keystr = self.Key(x.getExecBlockId())

        if keystr not in self._context:
            self._context[keystr] = []

        return self.insertByTime(x, self._context[keystr])

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows.
        return all rows as a list of HistoryRow
        """
        return self._privateRows

    def getByContext(self, execBlockId):
        """
        Returns all the rows sorted by ascending startTime for a given context.
        The context is defined by a value of ( execBlockId ).

        return a list  of HistoryRow. A None value is returned if the table contains
        no HistoryRow for the given ( execBlockId ).
        """

        keystr = self.Key(execBlockId)

        result = None
        if keystr in self._context:
            result = self._context[keystr]

    def getRowByKey(self, execBlockId, time):
        """
        Returns a HistoryRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.
        """

        keystr = self.Key(execBlockId)

        if keystr not in self._context:
            return None

        contextRows = self._context[keystr]
        # Is the contextRows list empty ...impossible in principle !
        if len(contextRows) == 0:
            return None

        # Only one element in the contextRows
        if len(contextRows) == 1:
            r = contextRows[0]
            if time.get() == r.getTime().get():
                return r
            else:
                return None

        # Optimizations
        lastRow = contextRows[-1]
        if time.get() > lastRow.getTime().get():
            # requested time is after the last row in contextRows
            return None

        firstRow = contextRows[0]
        if time.get() < first.getTime().get():
            # requested time is before the first row in contextRows
            return None

        # More than one row
        # let's use a dichotomy method for the general case..
        k0 = 0
        k1 = len(contextRows) - 1
        while k0 != k1:
            r = contextRows[k0]
            if time.get() == r.getTime().get():
                return r

            r = contextRows[k1]
            if time.get() == r.getTime().get():
                return r

            # ensure that nextRowIndx is an integer
            nextRowIndx = int((k0 + k1) / 2)
            r = contextRows[nextRowIndx]
            if time.get() <= r.getTime().get():
                k1 = nextRowIndx
            else:
                k0 = nextRowIndx

        # if it reaches here it was not found
        return None

    def getRows(self):
        """
        get the rows, synonymous with the get method.
        """
        return self.get()

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for History (HistoryTable.xsd).

        returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<HistoryTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:histry="http://Alma/XASDM/HistoryTable" xsi:schemaLocation="http://Alma/XASDM/HistoryTable http://almaobservatory.org/XML/XASDM/4/HistoryTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</HistoryTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a History (HistoryTable.xsd).
        """
        if not isinstance(xmlstr, str):
            raise ConversionException("xmlstr must be a string")

        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of "HistoryTable".
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "HistoryTable":
            raise ConversionException(
                "XML is not from the expected table", "HistoryTable"
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which is not always there
        versionStr = "-1"
        if tabdom.hasAttributes() and (
            tabdom.attributes.getNamedItem("schemaVersion") is not None
        ):
            versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "HistoryTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "HistoryTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "HistoryTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "HistoryTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "HistoryTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "HistoryTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self.checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str(exc), "HistoryTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "HistoryTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "HistoryTable")

        self.setEntity(tabEntity)

    def MIMEXMLPart(self, byteOrder):
        """
        Used in both the small XML file as well as the bin file when writing out as binary.
        The byte order is set by byteOrder.
        """
        uidStr = self.getEntity().getEntityId().toString()
        withoutUID = uidStr[6:]
        containerUID = self.getContainer().getEntity().getEntityId().toString()

        result = ""
        result += "<?xml version='1.0'  encoding='ISO-8859-1'?>"
        result += "\n"
        result += '<HistoryTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:histry="http://Alma/XASDM/HistoryTable" xsi:schemaLocation="http://Alma/XASDM/HistoryTable http://almaobservatory.org/XML/XASDM/4/HistoryTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += "<Entity entityId='"
        result += uidStr
        result += "' entityIdEncrypted='na' entityTypeName='HistoryTable' schemaVersion='1' documentVersion='1'/>\n"
        result += "<ContainerEntity entityId='"
        result += containerUID
        result += "' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n"
        result += "<BulkStoreRef file_id='"
        result += withoutUID
        result += "' byteOrder='" + byteOrder.toString() + "' />\n"
        result += "<Attributes>\n"

        result += "<execBlockId/>\n"
        result += "<time/>\n"
        result += "<message/>\n"
        result += "<priority/>\n"
        result += "<origin/>\n"
        result += "<objectId/>\n"
        result += "<application/>\n"
        result += "<cliCommand/>\n"
        result += "<appParms/>\n"

        result += "</Attributes>\n"
        result += "</HistoryTable>\n"

        return result

    def toMIME(self, mimeFilePath, mimeXMLpart, byteOrder):
        """
        Write this out to mimeFilePath as a serialized MIME file with
        a leading XML part and a following binary part.

        The mimeXMLpart is a string that should have already been written
        to the corresponding small XML file (and is returned by the
        MIMEXMLPart method here). The byteOrder is a ByteOrder instance
        that gives the byte order to use when writing the binary data.
        That instance should have also been used to generate mimeXMLpart.
        """

        # mimeFilePath should have already been removed if it already existed.

        with open(mimeFilePath, "wb") as outBuffer:

            uidStr = self.getEntity().getEntityId().toString()

            # The XML Header part.
            outBuffer.write(bytes("MIME-Version: 1.0", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(
                bytes(
                    "Content-Type: Multipart/Related; boundary='MIME_boundary'; type='text/xml'; start= '<header.xml>'",
                    "utf-8",
                )
            )
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-Description: Correlator", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("alma-uid:" + uidStr, "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))

            # The MIME XML part header.
            outBuffer.write(bytes("--MIME_boundary", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(
                bytes("Content-Type: text/xml; charset='ISO-8859-1'", "utf-8")
            )
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-Transfer-Encoding: 8bit", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-ID: <header.xml>", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))

            # The MIME XML part content.
            outBuffer.write(bytes(mimeXMLpart, "utf-8"))

            # The MIME binary part header
            outBuffer.write(bytes("--MIME_boundary", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-Type: binary/octet-stream", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-ID: <content.bin>", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))

            # The binary part, needs an EndianOutput instance

            eos = EndianOutput(outBuffer, byteOrder)
            self.getEntity().toBin(eos)
            self.getContainer().getEntity().toBin(eos)
            eos.writeInt(len(self._privateRows))

            # and all of the rows
            for thisRow in self._privateRows:
                thisRow.toBin(eos)

            # The closing MIME boundary
            outBuffer.write(bytes("\n--MIME_boundary--", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))

            # close the eos, also closes outBuffer, no penalty for doing that more than once
            eos.close()

    def setFromMIME(self, byteStream):
        """
        Extracts the binary part of a MIME message and deserialize its content
        to fill this with the result of the deserialization.
        param byteStream the previously opened io.BufferedReader instance
        containing the data to be extracted.

        It is the responsibility of this method to close byteStream.
        """

        if not (isinstance(byteStream, io.BufferedReader) and byteStream.seekable()):
            byteStream.close()
            raise ConversionException(
                "opened byteStream is not the expected io.BufferedReader or it is not seekable, this should never happen.",
                "History",
            )

        xmlPartMIMEHeader = bytes(str("Content-ID: <header.xml>\n\n").encode())
        binPartMIMEHeader = bytes(
            str(
                "--MIME_boundary\nContent-Type: binary/octet-stream\nContent-ID: <content.bin>\n\n"
            ).encode()
        )

        # follow the Java example and grab the first 10000 bytes, which will always contain the header
        headerBytes = byteStream.read(10000)

        # Detect the XML header.
        loc0 = headerBytes.find(xmlPartMIMEHeader)
        # c++ code also looks for a string with an additional CRLF after each newline if the above fails, but Java
        # doesn't and even c++ doesn't follow that up when failing to find the binPartMIMEHeader, so go with the Java example
        if loc0 < 0:
            byteStream.close()
            raise ConversionException(
                "Failed to detect the begining of the XML header.", "History"
            )

        loc0 += len(xmlPartMIMEHeader)

        # Look for the string announcing the binary part.
        loc1 = headerBytes.find(binPartMIMEHeader, loc0)
        if loc1 < 0:
            byteStream.close()
            raise ConversionException(
                "Failed to detect the begining of the binary part.", "History"
            )

        # extract the XML header as a string
        xmlHeader = headerBytes[loc0:loc1].decode()

        xmldom = minidom.parseString(xmlHeader)
        if not xmldom.hasChildNodes():
            byteStream.close()
            raise ConversionException("XML is not properly structured.", "History")

        attributesSeq = []
        byteOrderStr = None
        versionStr = "-1"

        hdrdom = xmldom.firstChild
        if hdrdom.nodeName == "ASDMBinaryTable":
            # old style of binary data
            # assume Big_Endian and the default order of the elements
            byteOrderStr = "Big_Endian"

            attributesSeq.append("execBlockId")

            attributesSeq.append("time")

            attributesSeq.append("message")

            attributesSeq.append("priority")

            attributesSeq.append("origin")

            attributesSeq.append("objectId")

            attributesSeq.append("application")

            attributesSeq.append("cliCommand")

            attributesSeq.append("appParms")

            versionStr = "2"

        else:
            # c++ and Java just assume it then must be a History table
            # this is more insistant, just in case
            if hdrdom.nodeName != "HistoryTable":
                byteStream.close()
                raise ConversionException(
                    "XML Header is not from the expected table.", "History"
                )

            # schemaVersion becomes versionStr
            if (
                hdrdom.hasAttributes()
                and hdrdom.attributes.getNamedItem("schemaVersion") is not None
            ):
                versionStr = hdrdom.attributes.getNamedItem("schemaVersion").value

            if not hdrdom.hasChildNodes():
                byteStream.close()
                raise ConversionException(
                    "THe XML header is missing all of the expected elements.", "History"
                )

            # loop through the child nodes, looking for BulkStoreRef and Attributes
            for hdrnode in hdrdom.childNodes:
                if hdrnode.nodeName == "BulkStoreRef":
                    if byteOrderStr is not None:
                        byteStream.close()
                        raise ConversionException(
                            "More than one BulkStoreRef element seen. Invalid XML header.",
                            "History",
                        )
                    if not hdrnode.hasAttributes():
                        byteStream.close()
                        raise ConversionException(
                            "BulkStoreRef does not contain any attributes. Invalid XML header.",
                            "History",
                        )
                    byteOrderAttr = hdrnode.attributes.getNamedItem("byteOrder")
                    if byteOrderAttr is None:
                        byteStream.close()
                        raise ConversionException(
                            "byteOrder attribute not found in BulkStoreRef element. Invalid XML header.",
                            "History",
                        )
                    byteOrderStr = byteOrderAttr.value
                elif hdrnode.nodeName == "Attributes":
                    if len(attributesSeq) > 0:
                        byteStream.close()
                        raise ConversionException(
                            "More than one Attributes node seen. Invalid XML header.",
                            "History",
                        )
                    if not hdrnode.hasChildNodes():
                        byteStream.close()
                        raise ConversionException(
                            "Attributes element has no child nodes. Invalid XML header.",
                            "History",
                        )
                    for attrnode in hdrnode.childNodes:
                        if attrnode.nodeType == attrnode.ELEMENT_NODE:
                            attributesSeq.append(str(attrnode.nodeName))

        if byteOrderStr is None:
            byteStream.close()
            raise ConversionException(
                "BulkStoreRef element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "History",
            )

        if len(attributesSeq) == 0:
            byteStream.close()
            raise ConversionException(
                "Attributes element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "History",
            )

        byteOrder = ByteOrder(byteOrderStr)

        # seek to the start of the binary part
        byteStream.seek(loc1 + len(binPartMIMEHeader))

        # and create the class that manages that stream and returns values as requested
        eis = EndianInput(byteStream, byteOrder)

        self._entity = Entity.fromBin(eis)

        # containerEntity is not used, but it is next
        containerEntity = Entity.fromBin(eis)

        # the number of rows
        numRows = eis.readInt()

        # c++ checks numRows against what is reported in the ASDM for this table, this is what Java does
        try:
            for i in range(numRows):
                self.checkAndAdd(HistoryRow.fromBin(eis, self, attributesSeq))
                print("row %s added, loc = %s" % (i, eis.tell()))
        except Exception as exc:
            byteStream.close()
            eis.close()
            raise ConversionException(
                "Error while reading binary data, the exception was " + str(exc),
                "History",
            ) from None

        # there is no harm in closing both
        print("closing")
        eis.close()
        byteStream.close()
        print("checking")
        print("eis : %s" % eis.closed())
        print("byteStream : %s" % byteStream.closed)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a HistoryTable as those produced  by the toFile method.
        This table is populated with the result of the parsing.
        param directory The name of the directory containing the file te be read and parsed.
        raises ConversionException If any error occurs while reading the
        files in the directory or parsing them.
        """
        if not isinstance(directory, str):
            print("directory must be a string")

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "HistoryTable",
            )

        if os.path.exists(os.path.join(directory, "History.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "History.bin")):
            self.setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the History table", "HistoryTable"
            )

    def setFromMIMEFile(self, directory):
        """
        Set this table from a MIME file.
        Used internally by setFromFile. Not intended for external use.
        """
        # The java and c++ versions read all of the contents into a byte array.
        # This uses a buffered byte stream. Created here and then
        # handed off to the setFromMIME method, which is responsible for closing it.

        filename = os.path.join(directory, "History.bin")
        byteStream = None
        try:
            byteStream = open(filename, "rb")
        except Exception as exc:
            raise ConversionException(
                "Error while opening " + filename + ". The exception was " + str(exc),
                "History",
            )

        self.setFromMIME(byteStream)

    def setFromXMLFile(self, directory):
        """
        This is the function used by setFromFile when the file is an XML file
        Not intended for external use.
        """

        # setFromFile has already established that this exists
        # read the entire file into a string
        xmlstr = None
        try:
            with open(os.path.join(directory, "History.xml")) as f:
                xmlstr = f.read()
        except Exception as exc:
            # reraise it as a ConversionException
            raise ConversionException(str(exc), "HistoryTable") from None

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of its _fileAsBin data member a binary serialization
        of this (_fileAsBin==True) will be saved in a file "History.bin" or
        an XML representation (_fileAsBin==False) will be saved in a file "History.xml".
        The file is always written in a directory whose name is passed as a parameter.
        param directory The name of directory where the file containing the table's
        representation will be saved.
        raises ConversionException for any errors while writing that file.
        """
        if not isinstance(directory, str):
            raise ConversionException("directory must be a string")

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (History)"
                % directory,
                "HistoryTable",
            )

        # if not let's create it.
        try:
            if not os.path.exists(directory):
                # if it can't be created a FileNotFound exception is the most likely result
                os.mkdir(directory)
        except Exception as exc:
            # reraise any exception as a ConversionException
            raise ConversionException(
                "Could not create directory "
                + directory
                + " exception caught "
                + str(exc),
                "HistoryTable",
            ) from None

        if self._fileAsBin:
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)

            # Java defaults to Big_Endian
            # c++ defaults to Machine, go with c++
            byteOrder = ByteOrder()

            # first, just the short XML file
            xmlFilePath = os.path.join(directory, "History.xml")
            if os.path.exists(xmlFilePath):
                try:
                    os.remove(xmlFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + xmlFilePath
                        + ", exception caught "
                        + str(exc),
                        "History",
                    ) from None

            # used in both files
            mimeXMLpart = self.MIMEXMLPart(byteOrder)

            # this is all that is written to the XML file
            with open(xmlFilePath, "w") as xmlfile:
                xmlfile.write(mimeXMLpart)

            # now open the possibly much longer MIME file
            mimeFilePath = os.path.join(directory, "History.bin")
            if os.path.exists(mimeFilePath):
                try:
                    os.remove(mimeFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + mimeFilePath
                        + ", exception caught "
                        + str(exc),
                        "History",
                    ) from None

            # the details are all handled in toMIME
            self.toMIME(mimeFilePath, mimeXMLpart, byteOrder)
        else:
            # The table is totally exported in a XML file.
            filePath = os.path.join(directory, "History.xml")
            if os.path.exists(filePath):
                try:
                    # try to delete it, this will raise an exception if the user does not have permission to do that
                    os.remove(filePath)
                except Exception as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(
                        "Could not remove existing "
                        + filePath
                        + " exception caught "
                        + str(exc),
                        "HistoryTable",
                    ) from None

            try:
                with open(filePath, "w") as f:
                    f.write(self.toXML())
                    f.close()

                    # Java code uses a BufferedWriter to capture the output of toXML to the file
            except Exception as exc:
                # reraise it as a ConversionException
                raise ConversionException(
                    "Problem while writing the XML representation, the message was : "
                    + str(exc),
                    "History",
                ) from None

    def getEntity(self):
        """
        Returns the table's entity.
        """
        return self._entity

    def setEntity(self, e):
        """
        Set the table's entity
        The parameter, e, must be an Entity
        """
        if not isinstance(e, Entity):
            raise (ValueError("setEntity must use an Entity value"))

        self._entity = Entity(e)

    def getVersion(self):
        return self._version

    def setVersion(self, version):
        if not isinstance(version, int):
            raise ValueError("version must be an int")

        self._version = version
