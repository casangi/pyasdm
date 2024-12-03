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
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class ReceiverTable(Representable):
    """
    The ReceiverTable class is an Alma table.

     Role
     Receiver properties.

     Generated from model's revision -1, branch

     Attributes of Receiver

                  Key

    receiverId int Receiver identifier

    spectralWindowId Tag refers to a unique row in SpectralwindowTable.

    timeInterval ArrayTimeInterval time interval for which the content is valid.



                  Value (Mandatory)

    name str  the name of the frontend.

    numLO int  the number of frequencies of the local oscillator.

    frequencyBand ReceiverBand  identifies the band of frequencies.

    freqLO Frequency []   numLO  the frequencies of the local oscillator.

    receiverSideband ReceiverSideband  the receiver sideband used.

    sidebandLO NetSideband []   numLO  the sideband conversions.



    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "Receiver"

    # the list of field names that make up key 'key'.
    _key = ["receiverId", "spectralWindowId", "timeInterval"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = False  # if True archive binary else archive XML
    _fileAsBin = False  # if True file binary else file XML

    # A list to store the ReceiverRow instances
    _privateRows = []

    # context is dictionary of lists of rows where each key is a string resulting
    # from a call to the method Key and the value is list of rows sharing that key,
    # maintained sorted in time-order.
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
        self._freqLOEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on freqLO
    def getFreqLOEqTolerance(self):
        """
        A getter for the tolerance on freqLO
        """
        return self._freqLOEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    @staticmethod
    def Key(spectralWindowId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        The parameter values are assumed to be the appropriate type for that parameter.
        """
        result = ""

        result += spectralWindowId.toString() + "_"

        return result

    def insertByStartTime(self, x, rowlist):
        """
        Insert a ReceiverRow in a list of ReceiverRow so that it's ordered by ascending start time.

        x is a ReceiverRow to be inserted.
        rowlist is the list where to x is to be inserted.

        The inserted row is returned.
        """
        insertionIndex = 0

        # get the ArrayTime at the start of the interval found in x.
        start = x.timeInterval.getStart()

        # is the rowlist None
        if rowlist is None:
            rowlist = []
        # is rowlist empty
        if len(rowlist) == 0:
            rowlist.append(x)
            self._privateRows.append(x)
            x.isAdded()
            return x

        # case where x goes at the end of rowlist
        # the last row in the list
        last = rowlist[-1]

        if start.get() > last.timeInterval.getStart().get():
            # Modify the duration of last if and only if the start time of x
            # is located strictly before the end time of last.

            if start.get() < (
                last.timeInterval.getStart().get()
                + last.timeInterval.getDuration().get()
            ):
                last.timeInterval.setDuration(
                    start.get() - last.timeInterval.getStart().get()
                )

            rowlist.append(x)
            self._privateRows.append(x)
            x.isAdded()
            return x

        # case where x goes at the beginning of rowlist
        # the first row in the list
        first = rowlist[0]

        if start.get() < first.timeInterval.getStart().get():
            # Modify the duration of x if and only if the start time of first
            # is located strictly before the end time of x.

            if first.timeInterval.getStart().get() < (
                start.get() + x.timeInterval.getDuration().get()
            ):
                x.timeInterval.setDuration(
                    first.timeInterval.getStart().get() - start.get()
                )
            x.timeInterval.setDuration(
                first.timeInterval.getStart().get() - start.get()
            )
            rowlist.insert(0, x)
            self._privateRows.add(x)
            x.isAdded()
            return x

        # Case where x has to be inserted inside rowlist
        # let's use a dichotomy method to find the insertion index.

        k0 = 0
        k1 = len(rowlist) - 1

        while k0 != (k1 - 1):
            if start.get() == rowlist[k0].timeInterval.getStart().get():
                if rowlist[k0].equalByRequiredValue(x):
                    # this row already exists at k0, nothing to insert or add, return that row
                    return rowlist[k0]
                else:
                    # the time matches, but the rest of the required parameters do not, duplicate keys
                    raise DuplicateKey("DuplicateKey exception in ", "ReceiverTable")
            elif start.get() == rowlist[k1].timeInterval.getStart().get():
                if rowlist[k1].equalByRequiredValue(x):
                    # this row already exists at k1, nothing to insert or add, return that row
                    return rowlist[k1]
                else:
                    # the time matches, but the rest of the required parameters do not, duplicate keys
                    raise DuplicateKey("DuplicateKey exception in ", "ReceiverTable")
            else:
                # make sure integers are used throughout this step
                if (
                    start.get()
                    <= rowlist[int((k0 + k1) / 2)].timeInterval.getStart().get()
                ):
                    k1 = int((k0 + k1) / 2)
                else:
                    k0 = int((k0 + k1) / 2)

        if start.get() == rowlist[k0].timeInterval.getStart().get():
            if row.get[k0].equalByRequiredValue(x):
                # this row already exists at k0, nothing to insert or add, return that row
                return rowlist[k0]
            else:
                # the time matches, but the rest of the required parameters do not, duplicate keys
                raise DuplicateKey("DuplicateKey exception in ", "ReceiverTable")
        elif start.get() == rowlist[k1].timeInterval.getStart().get():
            if rowlist[k1].equalByRequiredValue(x):
                return rowlist[k1]
            else:
                # the time matches, but the rest of the required parameters do not, duplicate keys
                raise DuplicateKey("DuplicateKey exception in ", "ReceiverTable")

        rowlist[k0].timeInterval.setDuration(
            start.get() - rowlist[k0].timeInterval.getStart().get()
        )
        x.timeInterval.setDuration(
            rowlist[k0 + 1].timeInterval.getStart().get() - start.get()
        )
        row.insertElementAt(k1, x)
        self._privateRows.add(x)
        x.isAdded()
        return x

    def __init__(self, container):
        """
        Create a ReceiverTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
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
        # NOTE: if setFromFile throws an exception then presentInMemory will remain False
        # and loadInProgress will remain True, preventing another attempt at loading.
        # more complex solutions are then necessary to read that file and it's not worth
        # complicating this code here to handle a need to eventually try again to reload that file
        if not self._presentInMemory and not self._loadInProgress:
            self._loadInProgress = True
            self.setFromFile(self.getContainer().getDirectory())
            self._presentInMemory = True
            self._loadInProgress = False

    def getContainer(self):
        """
        Return the container to which this table belongs.
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

    def add(self, row):
        """
        Append a row to a ReceiverTable which has simply
        1) an autoincrementable attribute  (receiverId)
        2) a temporal attribute (timeInterval) in its key section.
        3) other attributes in the key section (defining a so called context).
        If there is already a row in the table whose key section non including is equal to x's one and
        whose value section is equal to x's one then return this row, otherwise add x to the collection
        of rows.
        """
        # Get the start time of the row to be inserted (an ArrayTime)
        startTime = x.getTimeInterval().getStart()

        insertionId = 0

        # The key from the appropriates attributes.
        keystr = Key(x.getSpectralWindowId())

        # Determine the insertion index for the row x, possibly returning a pointer to a row identical to x.
        contextRows = []
        if keystr in self._context:
            contextRows = self._context[keystr]
            for i in range(len(contextRows)):
                # print("Looking for a start time in i = " + i)
                # each element of contextRows is a list of rows
                v = contextRows[i]
                for j in range(len(v)):
                    r = v.get[j]
                    # print("starttime = "+startTime+" + str(r.startTime ="+r.getTimeInterval().getStart()))
                    if startTime.eq(r.getTimeInterval().getStart()):
                        if r.compareRequiredValue(
                            x.getName(),
                            x.getNumLO(),
                            x.getFrequencyBand(),
                            x.getFreqLO(),
                            x.getReceiverSideband(),
                            x.getSidebandLO(),
                        ):
                            # We have found a ReceiverRow with the same value. Return it.
                            # print("A row equal to x has been found, I return it")
                            return r

                        # Otherwise we must autoincrement receiverId and
                        # insert a new ReceiverRow with this autoincremented value.
                        # print("A row has been found with the same start time but different value , increment id")
                        insertionId = i + 1

                        # And directly goto next id value
                        break
                # System.out.println("No row with the same time than x, it will be inserted in row with id = 0")
        else:
            # There is not yet a context...
            # Create and initialize an entry in the context map for this combination....
            # print("Starting a new context")
            context[k] = contextRows
            insertionId = 0

        x.setReceiverId(insertionId)

        # because contextRows is a list from self._context, manipulating that list with list methods will
        # also manipulate the list in self._context - no copy is created
        while len(contextRows) <= insertionId:
            contextRows.append([])
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
        Create a new ReceiverRow. The new row is not added to this table, but it does know about it.
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

    def _checkAndAdd(self, newrow):
        """
        A method to append a row to its table, used by input conversion methods.
        Not intended for external use.

        If this table has an autoincrementable attribute then check if newrow verifies the rule of uniqueness and raise an exception if not.
        Check if newrow verifies the key uniqueness rule and throw an exception if not.
        Append newrow to its table.
        returns  newrow
        """
        startTime = newrow.getTimeInterval().getStart()

        if (
            self.lookup(
                newrow.getSpectralWindowId(),
                newrow.getTimeInterval(),
                newrow.getName(),
                newrow.getNumLO(),
                newrow.getFrequencyBand(),
                newrow.getFreqLO(),
                newrow.getReceiverSideband(),
                newrow.getSidebandLO(),
            )
            is not None
        ):
            raise UniquenessViolationException(
                "Uniqueness violation exception in table ReceiverTable"
            )

        if (
            self.getRowByKey(
                newrow.getReceiverId(),
                newrow.getSpectralWindowId(),
                newrow.getTimeInterval(),
            )
        ) is not None:
            raise DuplicateKey(
                "Duplicate key exception . ("
                + "receiverId="
                + newrow.getReceiverId()
                + " "
                + "spectralWindowId="
                + newrow.getSpectralWindowId()
                + " "
                + "timeInterval="
                + newrow.getTimeInterval()
                + " "
                + ") in ",
                "ReceiverTable.",
            )

        thisKey = self.Key(newrow.getSpectralWindowId())

        i = newrow.getReceiverId()

        # add this key to context if not there
        if thisKey not in self._context:
            self._context[thisKey] = []

        return self.insertByStartTime(newrow, self._context[thisKey])

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as a list of ReceiverRow
        """
        return self._privateRows

    def getRowByKey(self, receiverId, spectralWindowId, timeInterval):
        """
        Returns a ReceiverRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.
        """
        start = timeInterval.getStart()

        keystr = Key(spectralWindowId)
        if keystr in self._context:

            id = receiverId

            contextList = self._context[keystr]
            for aRow in contextList:
                if aRow.getTimeInterval().equals(timeInterval):
                    return aRow

        return None

    def getRowByReceiverId(self, receiverId):
        """
        Returns a list of all rows whose key element receiverId
        is equal to the parameter receiverId, which is a int.
        return an array of ReceiverRow. A returned array of size 0 means that no row has been found.
        param receiverId int contains the value of
        the autoincrementable attribute that is looked up in the table.
        """
        result = []
        for thisValue in self._context.values():
            # each value is a list of lists, with one list for each receiverId
            if receiverId < len(thisValue):
                # append all of the receiverId rows to result
                result.extend(thisValue[receiverId])

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
        keystr = Key(spectralWindowId)
        if keystr in self._context:
            for thisList in self._context[keystr]:
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

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for Receiver (ReceiverTable.xsd).

        Returns a string containing the XML representation.
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
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of ReceiverTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "ReceiverTable":
            raise ConversionException(
                "XML is not from a the expected table", "ReceiverTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException("schemaVersion not found in XML", "ReceiverTable")
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
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "ReceiverTable") from None

                except ValueError as exc:
                    # TBD when this turns up via template
                    msg = (
                        "UniquenessViolationException in row in ReceiverTable : %s"
                        % str(exc)
                    )

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "ReceiverTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "ReceiverTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a ReceiverTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "ReceiverTable",
            )

        if os.path.exists(os.path.join(directory, "Receiver.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "Receiver.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the Receiver table", "ReceiverTable"
            )

    def setFromMIMEFile(self, directory):
        print("setFromMIMEFile not implemented yet")

    def setFromXMLFile(self, directory):
        """
        This is the function used by setFromFile when the file is an XML file
        """

        # setFromFile has already established that this exists
        # read the entire file into a string
        xmlstr = None
        with open(os.path.join(directory, "Receiver.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("Receiver.xml is empty", "ReceiverTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'Receiver.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'Receiver.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (Receiver)"
                % directory,
                "ReceiverTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for Receiver")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "Receiver.xml")
            if os.path.exists(filePath):
                # try to delete it, this will raise an exception if the user does not have permission to do that
                os.remove(filePath)
            with open(filePath, "w") as f:
                f.write(self.toXML())
                f.close()

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
