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
# File ReceiverTable.py
#

import pyasdm.ASDM

from .ReceiverRow import ReceiverRow

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


class ReceiverTable:
    """
    The ReceiverTable class is an Alma table.

    Role
    Receiver properties.

    Generated from model's revision -1, branch

    Attributes of Receiver

                 Key


    receiverId int (auto-incrementable)     Receiver identifier </TD>



    spectralWindowId Tag refers to a unique row in SpectralwindowTable. </TD>



    timeInterval ArrayTimeInterval time interval for which the content is valid. </TD>




                 Value (Mandatory)

    name  str  the name of the frontend.

    numLO (numLO) int  the number of frequencies of the local oscillator.

    frequencyBand  ReceiverBand  identifies the band of frequencies.

    freqLO  Frequency []   numLO  the frequencies of the local oscillator.

    receiverSideband  ReceiverSideband  the receiver sideband used.

    sidebandLO  NetSideband []   numLO  the sideband conversions.



    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # The name of this table.
    _tableName = "Receiver"

    # The list of field names that make up key 'key'.
    _key = ["receiverId", "spectralWindowId", "timeInterval"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # archive as bin not used by python implementation
    # _archiveAsBin = False # If True archive binary else archive XML
    _fileAsBin = False  # If True file binary else file XML

    # A data structure to store the ReceiverRow s.
    # In all cases we maintain a private list of ReceiverRow s.
    _privateRows = []

    # this table has a temporal key, an auto-incremetable key, and other key fields
    # context is a dictionary where the key is the key without the temporal and auto
    # incrementable fields.
    # the value is a list of lists, where the outer list is index by the auto-incrementable
    # key value and the inner list is the list of rows having that auto-incrementable
    # value.
    # Each list of rows is kept in temporal order
    _context = {}

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on freqLO during an add operation on the table
    _freqLOEqTolerance = Frequency(0.0)

    def setFreqLOEqTolerance(self, tolerance):
        """
        A setter for the tolerance on freqLO
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._freqLOEqTolerance = Frequency(tolerance)

    def getFreqLOEqTolerance(self):
        """
        A getter for the tolerance on freqLO
        Returns the tolerance as a  Frequency
        """
        return self._freqLOEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up key key
        as a list of strings.
        """
        return self._key

    def Key(self, spectralWindowId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        """
        result = ""

        result += spectralWindowId.toString() + "_"

        return result

    def insertByStartTime(self, x, rowlist):
        """
        Insert a ReceiverRow in a list of ReceiverRow so that it's ordered by ascending start time.

        x The ReceiverRow to be inserted.
        rowlist The list where x is to be inserted.

        The inserted row is returned. If x already exists in rowlist then it is not added and
        the row in rowlist is returned.

        If a row matching the value of the start time of timeInterval is
        found in rowlist but the other required parameters do not have the same value
        then a DuplicateKey exception is raised.
        """

        # get the ArrayTime value at the start of the ArrayTimeInterval found in x
        xTimeStart = x.getTimeInterval().getStart().get()

        # work out where to add x to rowlist
        if (len(rowlist) == 0) or (
            xTimeStart > (rowlist[-1].getTimeInterval().getStart().get())
        ):
            # it belongs at the end
            if len(rowlist) > 0:
                lastRow = rowlist[-1]
                # Modify the duration of lastRow if and only if the start time of x
                # is located strictly before the end time of last.
                if xTimeStart < (
                    lastRow.getTimeInterval().getStart().get()
                    + lastRow.getTimeInterval().getDuration().get()
                ):
                    lastRow.getTimeInterval().setDuration(
                        xTimeStart - lastRow.getTimeInterval().getStart().get()
                    )
            rowlist.append(x)
        elif xTimeStart < rowlist[0].getTimeInterval().getStart().get():
            # it belongs at the start
            firstRow = rowlist[0]
            # Modify the duration of x if and only if the start time of firstRow
            # is located strictly before the end time of x.
            if firstRow.getTimeInterval().getStart().get() < (
                xTimeStart + x.getTimeInterval().getDuration().get()
            ):
                x.getTimeInterval().setDuration(
                    firstRow.getTimeInterval().getStart().get() - xTimeStart
                )

            rowlist.insert(0, x)
        else:
            # x is inserted somewhere inside rowlist; let's use a dichotomoy
            # method to find the insertion index.

            k0 = 0
            k1 = len(rowlist) - 1

            while k0 != (k1 - 1):
                if xTimeStart == rowlist[k0].getTimeInterval().getStart().get():
                    if rowlist[k0].equalByRequiredValue(x):
                        # this row already exists at k0, nothing to insert or add, return that row
                        return rowlist[k0]
                    else:
                        # the start time matches, but the rest of the required parameters do not
                        raise DuplicateKey(
                            "DuplicateKey exception in ", "ReceiverTable"
                        )
                elif xTimeStart == rowlist[k1].getTimeInterval().getStart().get():
                    if rowlist[k1].equalByRequiredValue(x):
                        # this row already exists at k1, nothing to insert or add, return that row
                        return rowlist[k1]
                    else:
                        # the start time matches, but the rest of the required parameters do not
                        raise DuplicateKey(
                            "DuplicateKey exception in ", "ReceiverTable"
                        )
                else:
                    # make sure new index is an integer
                    newIndex = int((k0 + k1) / 2)
                    if (
                        xTimeStart
                        <= rowlist[newIndex].getTimeInterval().getStart().get()
                    ):
                        k1 = newIndex
                    else:
                        k0 = newIndex

            if xTimeStart == rowlist[k0].getTimeInterval().getStart().get():
                if rowlist[k0].equalByRequiredValue(x):
                    # this row already exists at k0, nothing to insert or add, return that row
                    return rowlist[k0]
                else:
                    # the start time matches, but the rest of the required paramters do not
                    raise DuplicateKey("DuplicateKey exception in ", "ReceiverTable")
            elif xTimeStart == rowlist[k1].getTimeInterval().getStart().get():
                if rowlist[k1].equalByRequiredValue(x):
                    # this row already exists at k1, nothing to insert or add, return that row
                    return rowlist[k1]
                else:
                    # the start time matches, but the rest of the required parameters do not
                    raise DuplicateKey("DuplicateKey exception in ", "ReceiverTable")

            # if it reaches here, it should be added, set the duration as appropriate for
            # insertion at k1, after k0, adjust duration of k0 as appropriate
            rowlist[k0].getTimeInterval().setDuration(
                xTimeStart - rowlist[k0].getTimeInterval().getStart().get()
            )
            x.getTimeInterval().setDuration(
                rowlist[k0 + 1].getTimeInterval().getStart().get() - xTimeStart
            )
            rowlist.insert(k1, x)

        # if it reaches here then x has already been addded to rowlist and it needs to be
        # appended to privateRows and marked as added internally before being returned
        self._privateRows.append(x)
        x.isAdded()
        return x

    def __init__(self, container):
        """
        Create a ReceiverTable attached to container.

        container must be a ASDM instance
        All tables must know the container
        """

        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("ReceiverTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("ReceiverTable")
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
            print("Receiver is not present in memory, setting from file")
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
        Returns "ReceiverTable" followed by the current size of the table
        between parenthesis.
        Example : ReceiverTable(12)
        """
        return "ReceiverTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = ReceiverRow(self)
        return thisRow

    def add(self, x):
        """
        Append a row to a ReceiverTable which has simply
        1) an autoincrementable attribute  (receiverId)
        2) a temporal attribute (timeInterval) in its key section.
        3) other attributes in the key section (defining a so called context).
        If there is already a row in the table whose key section non including is equal to x's one and
        whose value section is equal to x's one then return this row, otherwise add x to the collection
        of rows.
        """
        if not isinstance(x, ReceiverRow):
            raise ValueError("x must be a  ReceiverRow instance.")

        # Get the start time of the time interval of the row to be inserted (an ArrayTime)
        startTime = x.getTimeInterval().getStart()

        insertionId = 0

        # the key from the appropriate attributes
        keystr = self.Key(x.getSpectralWindowId())

        # Determine the insertion index for the row x, possibly returning a pointer to a row identical to x.
        if keystr in self._context:
            contextRows = self._context[keystr]
            # look through all of the auto-incrementable lists to see there is any
            # row that matches this time and other required values
            for autoIncList in range(len(contextRows)):
                for thisRow in autoIncList:
                    if startTime.eq(thisRow.getTimeInterval().getStart()):
                        if thisRow.compareRequiredValue(
                            x.getName(),
                            x.getNumLO(),
                            x.getFrequencyBand(),
                            x.getFreqLO(),
                            x.getReceiverSideband(),
                            x.getSidebandLO(),
                        ):
                            # We have found a ReceiverRow with the same value then return it.
                            return thisRow

                        # otherwise this has the same time but different other values so
                        # we must autoincrement receiverId and
                        # insert a new ReceiverRow with this autoincremented value.
                        # System.out.println("A row has been found with the same start time but different value , increment id")
                        insertionId = i + 1

                        # And directly goto next id value
                        break
        else:
            # There is not yet a context...
            # Create and initialize an entry in the context map for this combination....
            self._context[keystr] = []
            insertionId = 0

        x.setReceiverId(insertionId)

        contextRows = self._context[keystr]
        # make sure there are enough rows in contextRows to hold insertionId
        # probably this just adds one list to contextRows
        while len(contextRows) <= insertionId:
            contetRows.append([])

        # and insert this row into the list at insertionId so that list remains ordered in time
        result = self.insertByStartTime(x, contextRows[insertionId])
        return result

    def newRow(
        self,
        spectralWindowId,
        timeInterval,
        name,
        numLO,
        frequencyBand,
        freqLO,
        receiverSideband,
        sidebandLO,
    ):
        """
        Create a new ReceiverRow initialized to the specified values.

        The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = ReceiverRow(self)

        thisRow.setSpectralWindowId(spectralWindowId)

        thisRow.setTimeInterval(timeInterval)

        thisRow.setName(name)

        thisRow.setNumLO(numLO)

        thisRow.setFrequencyBand(frequencyBand)

        thisRow.setFreqLO(freqLO)

        thisRow.setReceiverSideband(receiverSideband)

        thisRow.setSidebandLO(sidebandLO)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new ReceiverRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new ReceiverRow with default values for its attributes.
        """

        return ReceiverRow(self, row)

    # ====> Append a row to its table.

    def checkAndAdd(self, x):
        """
        A method to append a row to its table, used by input conversion methods.
        Not indended for external use.

        If this table has an autoincrementable attribute then check if
        x verifies the rule of uniqueness and throw exception if not.

        This method is appropriate for an auto-incrementable attribute with a
        temporal field either with or without additional keywords.

        Append x to its table.
        x The row to be appended.
        returns  x.
        """
        # startTime is an ArrayTimeInterval
        startTime = x.getTimeInterval().getStart()

        if (
            self.lookup(
                x.getSpectralWindowId(),
                x.getTimeInterval(),
                x.getName(),
                x.getNumLO(),
                x.getFrequencyBand(),
                x.getFreqLO(),
                x.getReceiverSideband(),
                x.getSidebandLO(),
            )
            is not None
        ):
            raise UniquenessViolationException(
                "Uniqueness violation exception in table ReceiverTable"
            )

        if (
            self.getRowByKey(
                x.getReceiverId(), x.getSpectralWindowId(), x.getTimeInterval()
            )
            is not None
        ):
            raise DuplicateKey(
                "Duplicate key exception . ("
                + "receiverId="
                + x.getReceiverId()
                + " "
                + "spectralWindowId="
                + x.getSpectralWindowId()
                + " "
                + "timeInterval="
                + x.getTimeInterval()
                + " "
                + ") in ",
                "ReceiverTable.",
            )

        keystr = self.Key(x.getSpectralWindowId())

        i = x.getReceiverId()

        # make sure keystr is known to context and that there enough elements to retrieve
        # the list at element "i"
        if keystr not in self._context:
            self._context[keystr] = []
        while len(self._context[keystr]) <= i:
            self._context[keystr].append([])

        return self.insertByStartTime(x, self._context[keystr][i])

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows.
        return all rows as list of ReceiverRow
        """
        return self._privateRows

    def getRowByKey(self, receiverId, spectralWindowId, timeInterval):
        """
        Returns a ReceiverRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.
        """

        # the ArrayTime at the start of the requested time interval
        start = timeInterval.getStart()

        keystr = self.Key(spectralWindowId)
        if keystr not in self._context:
            return None

        id = int(receiverId)

        contextRows = self._context[keystr]
        # the first list is indexed by id so it must exist for this to find a row
        if id < len(contextRows):
            idRows = contextRows[id]
            for aRow in idRows:
                if aRow.getTimeInterval().equals(timeInterval):
                    return aRow

        # never found
        return None

    def getRowByReceiverId(self, receiverId):
        """
        Returns a list of rows whose key element receiverId
        is equal to the parameter receiverId.
        return a list of ReceiverRow. A returned list of size 0 means that no row has been found.
        receiverId is of type int and contains the value of
        the autoincrementable attribute that is looked up in the table.
        """
        result = []

        # any of the context strings could contain a list appropriate for the requested value
        for thisKeyValue in self._context.values():
            # if this has the requested value, that value can be used to index into this list
            if receiverId < len(thisKeyValue):
                # this value contains rows with the requested value
                # append all of them to the result
                result.extend(thisKeyValue[receiverId])

        return result

    def lookup(
        self,
        spectralWindowId,
        timeInterval,
        name,
        numLO,
        frequencyBand,
        freqLO,
        receiverSideband,
        sidebandLO,
    ):
        """
        Look up the table for a row whose all attributes  except the autoincrementable one
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.

        param spectralWindowId.

        param timeInterval.

        param name.

        param numLO.

        param frequencyBand.

        param freqLO.

        param receiverSideband.

        param sidebandLO.

        """
        keystr = self.Key(spectralWindowId)
        if keystr in self._context:
            # it may be found in any of the list of lists
            for thisKeyValueList in self._context.values():
                for thisList in thisKeyValueList:
                    for thisRow in thisList:
                        if thisRow.getTimeInterval().contains(
                            timeInterval
                        ) and thisRow.compareNoAutoInc(
                            spectralWindowId,
                            timeInterval,
                            name,
                            numLO,
                            frequencyBand,
                            freqLO,
                            receiverSideband,
                            sidebandLO,
                        ):
                            return thisRow

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
        to the schema defined for Receiver (ReceiverTable.xsd).

        returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<ReceiverTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:rcvr="http://Alma/XASDM/ReceiverTable" xsi:schemaLocation="http://Alma/XASDM/ReceiverTable http://almaobservatory.org/XML/XASDM/4/ReceiverTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</ReceiverTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a Receiver (ReceiverTable.xsd).
        """
        if not isinstance(xmlstr, str):
            raise ConversionException("xmlstr must be a string")

        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of "ReceiverTable".
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "ReceiverTable":
            raise ConversionException(
                "XML is not from the expected table", "ReceiverTable"
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
                "schemaVersion is not an integer", "ReceiverTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "ReceiverTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "ReceiverTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "ReceiverTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "ReceiverTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "ReceiverTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self.checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str(exc), "ReceiverTable") from None

                except UniquenessViolationException as exc:
                    msg = (
                        "UniquenessViolationException in row in ReceiverTable : %s"
                        % str(exc)
                    )

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "ReceiverTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "ReceiverTable")

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
        result += '<ReceiverTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:rcvr="http://Alma/XASDM/ReceiverTable" xsi:schemaLocation="http://Alma/XASDM/ReceiverTable http://almaobservatory.org/XML/XASDM/4/ReceiverTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += "<Entity entityId='"
        result += uidStr
        result += "' entityIdEncrypted='na' entityTypeName='ReceiverTable' schemaVersion='1' documentVersion='1'/>\n"
        result += "<ContainerEntity entityId='"
        result += containerUID
        result += "' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n"
        result += "<BulkStoreRef file_id='"
        result += withoutUID
        result += "' byteOrder='" + byteOrder.toString() + "' />\n"
        result += "<Attributes>\n"

        result += "<receiverId/>\n"
        result += "<spectralWindowId/>\n"
        result += "<timeInterval/>\n"
        result += "<name/>\n"
        result += "<numLO/>\n"
        result += "<frequencyBand/>\n"
        result += "<freqLO/>\n"
        result += "<receiverSideband/>\n"
        result += "<sidebandLO/>\n"

        result += "</Attributes>\n"
        result += "</ReceiverTable>\n"

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
                "Receiver",
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
                "Failed to detect the begining of the XML header.", "Receiver"
            )

        loc0 += len(xmlPartMIMEHeader)

        # Look for the string announcing the binary part.
        loc1 = headerBytes.find(binPartMIMEHeader, loc0)
        if loc1 < 0:
            byteStream.close()
            raise ConversionException(
                "Failed to detect the begining of the binary part.", "Receiver"
            )

        # extract the XML header as a string
        xmlHeader = headerBytes[loc0:loc1].decode()

        xmldom = minidom.parseString(xmlHeader)
        if not xmldom.hasChildNodes():
            byteStream.close()
            raise ConversionException("XML is not properly structured.", "Receiver")

        attributesSeq = []
        byteOrderStr = None
        versionStr = "-1"

        hdrdom = xmldom.firstChild
        if hdrdom.nodeName == "ASDMBinaryTable":
            # old style of binary data
            # assume Big_Endian and the default order of the elements
            byteOrderStr = "Big_Endian"

            attributesSeq.append("receiverId")

            attributesSeq.append("spectralWindowId")

            attributesSeq.append("timeInterval")

            attributesSeq.append("name")

            attributesSeq.append("numLO")

            attributesSeq.append("frequencyBand")

            attributesSeq.append("freqLO")

            attributesSeq.append("receiverSideband")

            attributesSeq.append("sidebandLO")

            versionStr = "2"

        else:
            # c++ and Java just assume it then must be a Receiver table
            # this is more insistant, just in case
            if hdrdom.nodeName != "ReceiverTable":
                byteStream.close()
                raise ConversionException(
                    "XML Header is not from the expected table.", "Receiver"
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
                    "THe XML header is missing all of the expected elements.",
                    "Receiver",
                )

            # loop through the child nodes, looking for BulkStoreRef and Attributes
            for hdrnode in hdrdom.childNodes:
                if hdrnode.nodeName == "BulkStoreRef":
                    if byteOrderStr is not None:
                        byteStream.close()
                        raise ConversionException(
                            "More than one BulkStoreRef element seen. Invalid XML header.",
                            "Receiver",
                        )
                    if not hdrnode.hasAttributes():
                        byteStream.close()
                        raise ConversionException(
                            "BulkStoreRef does not contain any attributes. Invalid XML header.",
                            "Receiver",
                        )
                    byteOrderAttr = hdrnode.attributes.getNamedItem("byteOrder")
                    if byteOrderAttr is None:
                        byteStream.close()
                        raise ConversionException(
                            "byteOrder attribute not found in BulkStoreRef element. Invalid XML header.",
                            "Receiver",
                        )
                    byteOrderStr = byteOrderAttr.value
                elif hdrnode.nodeName == "Attributes":
                    if len(attributesSeq) > 0:
                        byteStream.close()
                        raise ConversionException(
                            "More than one Attributes node seen. Invalid XML header.",
                            "Receiver",
                        )
                    if not hdrnode.hasChildNodes():
                        byteStream.close()
                        raise ConversionException(
                            "Attributes element has no child nodes. Invalid XML header.",
                            "Receiver",
                        )
                    for attrnode in hdrnode.childNodes:
                        if attrnode.nodeType == attrnode.ELEMENT_NODE:
                            attributesSeq.append(str(attrnode.nodeName))

        if byteOrderStr is None:
            byteStream.close()
            raise ConversionException(
                "BulkStoreRef element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "Receiver",
            )

        if len(attributesSeq) == 0:
            byteStream.close()
            raise ConversionException(
                "Attributes element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "Receiver",
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
                self.checkAndAdd(ReceiverRow.fromBin(eis, self, attributesSeq))
                print("row %s added, loc = %s" % (i, eis.tell()))
        except Exception as exc:
            byteStream.close()
            eis.close()
            raise ConversionException(
                "Error while reading binary data, the exception was " + str(exc),
                "Receiver",
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
        Reads and parses a file containing a representation of a ReceiverTable as those produced  by the toFile method.
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
                "ReceiverTable",
            )

        if os.path.exists(os.path.join(directory, "Receiver.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "Receiver.bin")):
            self.setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the Receiver table", "ReceiverTable"
            )

    def setFromMIMEFile(self, directory):
        """
        Set this table from a MIME file.
        Used internally by setFromFile. Not intended for external use.
        """
        # The java and c++ versions read all of the contents into a byte array.
        # This uses a buffered byte stream. Created here and then
        # handed off to the setFromMIME method, which is responsible for closing it.

        filename = os.path.join(directory, "Receiver.bin")
        byteStream = None
        try:
            byteStream = open(filename, "rb")
        except Exception as exc:
            raise ConversionException(
                "Error while opening " + filename + ". The exception was " + str(exc),
                "Receiver",
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
            with open(os.path.join(directory, "Receiver.xml")) as f:
                xmlstr = f.read()
        except Exception as exc:
            # reraise it as a ConversionException
            raise ConversionException(str(exc), "ReceiverTable") from None

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of its _fileAsBin data member a binary serialization
        of this (_fileAsBin==True) will be saved in a file "Receiver.bin" or
        an XML representation (_fileAsBin==False) will be saved in a file "Receiver.xml".
        The file is always written in a directory whose name is passed as a parameter.
        param directory The name of directory where the file containing the table's
        representation will be saved.
        raises ConversionException for any errors while writing that file.
        """
        if not isinstance(directory, str):
            raise ConversionException("directory must be a string")

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (Receiver)"
                % directory,
                "ReceiverTable",
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
                "ReceiverTable",
            ) from None

        if self._fileAsBin:
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)

            # Java defaults to Big_Endian
            # c++ defaults to Machine, go with c++
            byteOrder = ByteOrder()

            # first, just the short XML file
            xmlFilePath = os.path.join(directory, "Receiver.xml")
            if os.path.exists(xmlFilePath):
                try:
                    os.remove(xmlFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + xmlFilePath
                        + ", exception caught "
                        + str(exc),
                        "Receiver",
                    ) from None

            # used in both files
            mimeXMLpart = self.MIMEXMLPart(byteOrder)

            # this is all that is written to the XML file
            with open(xmlFilePath, "w") as xmlfile:
                xmlfile.write(mimeXMLpart)

            # now open the possibly much longer MIME file
            mimeFilePath = os.path.join(directory, "Receiver.bin")
            if os.path.exists(mimeFilePath):
                try:
                    os.remove(mimeFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + mimeFilePath
                        + ", exception caught "
                        + str(exc),
                        "Receiver",
                    ) from None

            # the details are all handled in toMIME
            self.toMIME(mimeFilePath, mimeXMLpart, byteOrder)
        else:
            # The table is totally exported in a XML file.
            filePath = os.path.join(directory, "Receiver.xml")
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
                        "ReceiverTable",
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
                    "Receiver",
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
