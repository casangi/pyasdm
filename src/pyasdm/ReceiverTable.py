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

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey
from .exceptions.UniquenessViolationException import UniquenessViolationException

from xml.dom import minidom

import os


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
                    astRow.getTimeInterval().setDuration(
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

    def MIMEXMLPart(self):
        print("MIMEXMLPart not implemented for <ReceiverTable")
        return
        # the JAVA code looks like this
        # String UID = this.getEntity().getEntityId().toString();
        # String withoutUID = UID.substring(6);
        # String containerUID = this.getContainer().getEntity().getEntityId().toString();
        #
        # StringBuffer sb = new StringBuffer()
        # .append("<?xml version='1.0'  encoding='ISO-8859-1'?>")
        # .append("\n")
        # .append("<ReceiverTable xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:rcvr=\"http://Alma/XASDM/ReceiverTable\" xsi:schemaLocation=\"http://Alma/XASDM/ReceiverTable http://almaobservatory.org/XML/XASDM/4/ReceiverTable.xsd\" schemaVersion=\"4\" schemaRevision=\"-1\">\n")
        # .append("<Entity entityId='")
        # .append(UID)
        # .append("' entityIdEncrypted='na' entityTypeName='ReceiverTable' schemaVersion='1' documentVersion='1'/>\n")
        # .append("<ContainerEntity entityId='")
        # .append(containerUID)
        # .append("' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n")
        # .append("<BulkStoreRef file_id='")
        # .append(withoutUID)
        # .append("' byteOrder='Big_Endian' />\n")
        # .append("<Attributes>\n")

        # .append("<receiverId/>\n")
        # .append("<spectralWindowId/>\n")
        # .append("<timeInterval/>\n")
        # .append("<name/>\n")
        # .append("<numLO/>\n")
        # .append("<frequencyBand/>\n")
        # .append("<freqLO/>\n")
        # .append("<receiverSideband/>\n")
        # .append("<sidebandLO/>\n")

        # .append("</Attributes>\n")
        # .append("</ReceiverTable>\n");
        # return sb.toString();

    def toMIME(self):
        """
        Serialize this into a stream of bytes and encapsulates that stream into a MIME message.
        returns a string containing the MIME message.
        """
        print("toMIME not yet implemented for Receiver")
        return
        # the Java code looks like this - returns a Byte array
        # ByteArrayOutputStream bos = new ByteArrayOutputStream();
        # DataOutputStream dos = new DataOutputStream(bos);

        # String UID = this.getEntity().getEntityId().toString();
        # String execBlockUID = this.getContainer().getEntity().getEntityId().toString();
        # try {
        #     // The XML Header part.
        #     dos.writeBytes("MIME-Version: 1.0");
        #     dos.writeBytes("\n");
        #    dos
        #     .writeBytes("Content-Type: Multipart/Related; boundary='MIME_boundary'; type='text/xml'; start= '<header.xml>'");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-Description: Correlator");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("alma-uid:" + UID);
        #    dos.writeBytes("\n");
        #    dos.writeBytes("\n");
        #
        #    // The MIME XML part header.
        #    dos.writeBytes("--MIME_boundary");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-Type: text/xml; charset='ISO-8859-1'");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-Transfer-Encoding: 8bit");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-ID: <header.xml>");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("\n");
        #
        #    // The MIME XML part content.
        #    dos.writeBytes(MIMEXMLPart());
        #    // have updated their code to the new XML header.
        #    //
        #    //dos.writeBytes(oldMIMEXMLPart());
        #
        #    // The MIME binary part header
        #    dos.writeBytes("--MIME_boundary");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-Type: binary/octet-stream");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-ID: <content.bin>");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("\n");
        #
        #    // The binary part.
        #    entity.toBin(dos);
        #    container.getEntity().toBin(dos);
        #    dos.writeInt(size());

        #    for (ReceiverRow row: privateRows) row.toBin(dos);

        #    // The closing MIME boundary
        #    dos.writeBytes("\n--MIME_boundary--");
        #    dos.writeBytes("\n");

        # } catch (IOException e) {
        #    throw new ConversionException(
        #            "Error while reading binary data , the message was "
        #            + e.getMessage(), "Receiver");
        # }

        # return bos.toByteArray();

    # Java code looks like this
    # static private boolean binaryPartFound(DataInputStream dis, String s, int pos) throws IOException {
    #    int posl = pos;
    #    int count = 0;
    #    dis.mark(1000000);
    #    try {
    #        while (dis.readByte() != s.charAt(posl)){
    #            count ++;
    #        }
    #    }
    #    catch (EOFException e) {
    #        return false;
    #    }
    #
    #    if (posl == (s.length() - 1)) return true;
    #
    #    if (pos == 0) {
    #        posl++;
    #        return binaryPartFound(dis, s, posl);
    #    }
    #    else {
    #        if (count > 0) { dis.reset();  return binaryPartFound(dis, s, 0) ; }
    #        else {
    #            posl++;
    #            return binaryPartFound(dis, s, posl);
    #        }
    #    }
    # }

    # private String xmlHeaderPart (String s) throws ConversionException {
    #    String xmlPartMIMEHeader = "Content-ID: <header.xml>\n\n";
    #    String binPartMIMEHeader = "--MIME_boundary\nContent-Type: binary/octet-stream\nContent-ID: <content.bin>\n\n";
    #
    #    // Detect the XML header.
    #    int loc0 = s.indexOf(xmlPartMIMEHeader);
    #    if (loc0 == -1 ) throw new ConversionException("Failed to detect the beginning of the XML header", "Receiver");
    #
    #    loc0 += xmlPartMIMEHeader.length();
    #
    #    // Look for the string announcing the binary part.
    #    int loc1 = s.indexOf(binPartMIMEHeader, loc0);
    #    if (loc1 == -1) throw new ConversionException("Failed to detect the beginning of the binary part", "Receiver");
    #
    #    return s.substring(loc0, loc1).trim();
    # }

    # setFromMIME(byte[]   data) throws ConversionException {
    # *
    # Extracts the binary part of a MIME message and deserialize its content
    # to fill this with the result of the deserialization.
    # @param data the string containing the MIME message.
    # @throws ConversionException
    # /
    # ByteOrder byteOrder = null;
    # //
    # // Look for the part containing the XML header.
    # // Very empirically we assume that the first MIME part , the one which contains the
    # // XML header, always fits in the first 1000 bytes of the MIME message !!
    # //
    # String header = xmlHeaderPart(new String(data, 0, Math.min(10000, data.length)));
    # org.jdom.Document document = null;
    # SAXBuilder sxb = new SAXBuilder();
    #
    # // Firstly build a document out of the XML.
    # try {
    #    document = sxb.build(new ByteArrayInputStream(header.getBytes()));
    # }
    # catch (Exception e) {
    #     throw new ConversionException(e.getMessage(), "Receiver");
    # }
    #
    # //
    # // Let's define a default order for the sequence of attributes.
    # //
    # ArrayList<String> attributesSeq = new ArrayList<String> ();

    #     attributesSeq.add("receiverId"); attributesSeq.add("spectralWindowId"); attributesSeq.add("timeInterval"); attributesSeq.add("name"); attributesSeq.add("numLO"); attributesSeq.add("frequencyBand"); attributesSeq.add("freqLO"); attributesSeq.add("receiverSideband"); attributesSeq.add("sidebandLO");
    #

    # XPath xpath = null;
    # //
    # // And then look for the possible XML contents.
    # try {
    #     // Is it an "<ASDMBinaryTable ...." document (old) ?
    #    if (XPath.newInstance("/ASDMBinaryTable")
    #            .selectSingleNode(document) != null)
    #        byteOrder = ByteOrder.BIG_ENDIAN;
    #    else {
    #        // Then it must be a "<ReceiverTable ...." document
    #        // With a BulkStoreRef child element....
    #        XPath xpa = XPath.newInstance("/ReceiverTable/BulkStoreRef/@byteOrder");
    #        Object node = xpa.selectSingleNode(document.getRootElement());
    #        if (node == null)
    #            throw new ConversionException("No element found for the XPath expression '/ReceiverTable/BulkStoreRef/@byteOrder'. Invalid XML header '"+header+"'.", "Receiver");
    #
    #        // Yes ? then it must have a "BulkStoreRef" element with a
    #        // "byteOrder" attribute.
    #        String bo = xpa.valueOf(document.getRootElement());
    #        if (bo.equals("Little_Endian"))
    #            byteOrder = ByteOrder.LITTLE_ENDIAN;
    #        else if (bo.equals("Big_Endian"))
    #            byteOrder = ByteOrder.BIG_ENDIAN;
    #        else
    #            throw new ConversionException("No valid value retrieved for the node '/ReceiverTable/BulkStoreRef/@byteOrder'. Invalid XML header '"+header+"'.", "Receiver");
    #
    #        // And also it must have an Attributes element with children.
    #        xpa = XPath.newInstance("/ReceiverTable/Attributes#");
    #        List nodes = xpa.selectNodes(document.getRootElement());
    #        if (nodes==null || nodes.size()==0)
    #            throw new ConversionException("No element found for the XPath expression '/ReceiverTable/Attributes#'. Invalid XML header '"+header+"'.", "Receiver");
    #
    #        Iterator iter = nodes.iterator();
    #        attributesSeq.clear();
    #        int i = 0;
    #        while (iter.hasNext()){
    #            attributesSeq.add(((Element) iter.next()).getName());
    #            i += 1;
    #        }
    #    }
    # } catch (Exception e) {
    #    throw new ConversionException(e.getMessage(), "Receiver");
    # }

    # //
    # // Now that we know what is the byte order of the binary data
    # // Let's extract them from the second MIME part and parse them
    # //
    # ByteArrayInputStream bis = new ByteArrayInputStream(data);
    # DataInputStream dis = new DataInputStream(bis);
    # BODataInputStream bodis = new BODataInputStream(dis, byteOrder);
    #
    # String terminator = "Content-Type: binary/octet-stream\nContent-ID: <content.bin>\n\n";
    # entity = null;
    # try {
    #    if (binaryPartFound(dis, terminator, 0) == false) {
    #        throw new ConversionException ("Failed to detect the beginning of the binary part", "Receiver");
    #    }
    #
    #    entity = Entity.fromBin(bodis);
    #
    #    Entity containerEntity = Entity.fromBin(bodis);
    #
    #    int numRows = bodis.readInt();
    #    for (int i = 0; i < numRows; i++) {
    #    this.checkAndAdd(ReceiverRow.fromBin(bodis, this, attributesSeq.toArray(new String[0])));
    #    }
    # } catch (TagFormatException e) {
    #    throw new ConversionException( "Error while reading binary data , the message was "
    #        + e.getMessage(), "Receiver");
    # }catch (IOException e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "Receiver");
    # } catch (DuplicateKey e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "Receiver");
    # }catch (Exception e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "Receiver");
    # }
    # }

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
        Used internally by setFromFile. Not intented for external use.
        """
        print("setFromMIME file not yet implemented for ReceiverTable")
        return

        # java code looks like this
        # File file = new File(directory+"/Receiver.bin");
        #
        # byte[] bytes = null;
        #
        # try {
        #     InputStream is = new FileInputStream(file);
        #     long length = file.length();
        #     if (length > Integer.MAX_VALUE)
        #         throw new ConversionException ("File " + file.getName() + " is too large", "Receiver");
        #
        #    bytes = new byte[(int)length];
        #    int offset = 0;
        #    int numRead = 0;
        #
        #   while (offset < bytes.length && (numRead=is.read(bytes, offset, bytes.length-offset)) >= 0) {
        #       offset += numRead;
        #   }
        #
        #    if (offset < bytes.length) {
        #        throw new ConversionException("Could not completely read file "+file.getName(), "Receiver");
        #    }
        #    is.close();
        # }
        # catch (IOException e) {
        #    throw new ConversionException("Error while reading "+file.getName()+". The message was " + e.getMessage(),
        #    "Receiver");
        # }

        # setFromMIME(bytes);
        # // Changed 24 Sep, 2015 - The export policy cannot be changed by what has been observed at import time. M Caillat
        # // archiveAsBin = true;
        # // fileAsBin = true;

    # }

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
            # TBD: when fileAsBin is implemented this should be removed
            # this will at least preserve the case where fileAsBin was changed for
            # a table such that the archive has it in XML but the current rule is to
            # write it out as binary
            if self._fileAsBin:
                print(
                    "Receiver found as XML but it should be written as binary, which is not yet implemetned. Setting to write as XML to preserve this content."
                )
                self._fileAsBin = False

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
            print("fileAsBin not yet implemented for Receiver")
            # the Java code looks like this
            #
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)
            #
            # File xmlFile = new File(directory+"/Receiver.xml");
            # if (xmlFile.exists())
            #    if (!xmlFile.delete())
            #        throw new ConversionException("Problem while trying to delete a previous version of '"+xmlFile.toString()+"'", "Receiver");
            #
            # File binFile = new File(directory+"/Receiver.bin");
            # if (binFile.exists())
            #    if (!binFile.delete())
            #        throw new ConversionException("Problem while trying to delete a previous version of '"+binFile.toString()+"'", "Receiver");
            #
            # try {
            #    BufferedWriter out = new BufferedWriter(new FileWriter(xmlFile));
            #    out.write(MIMEXMLPart());
            #    out.close();
            #

            #  OutputStream osBin = new FileOutputStream(binFile);
            #  osBin.write(toMIME());
            #  osBin.close();

        # }
        # catch (FileNotFoundException e) {
        #     throw new ConversionException("Problem while writing the binary representation, the message was : " + e.getMessage(), "Receiver");
        # }
        # catch (IOException e) {
        #      throw new ConversionException("Problem while writing the binary representation, the message was : " + e.getMessage(), "Receiver");
        # }
        # }
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
