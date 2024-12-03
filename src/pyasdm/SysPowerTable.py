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
# File SysPowerTable.py
#

import pyasdm.ASDM

from .SysPowerRow import SysPowerRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class SysPowerTable(Representable):
    """
        The SysPowerTable class is an Alma table.

         Role
         This table is intended to store power measurements based on a synchronous power detector as  used at the EVLA. While the table is intended to be general enough for use with other arrays, it is  deeply entwined with the EVLA data acquisition scheme. The units of \f$P_{diff}\f$ and \f$P_{sum}\f$ are such that the system temperature, \f$T_{sys}\f$, is :
    \f[
    T_{sys}=\frac{P_{sum}}{P_{diff}} . \frac{T_{cal}}{2}
    \f]
    where \f$T_{cal}\f$ is the temperature of the noise tube.


         Generated from model's revision -1, branch

         Attributes of SysPower

                      Key

        antennaId Tag

        spectralWindowId Tag

        feedId int

        timeInterval ArrayTimeInterval time interval over which the content of the row was measured.



                      Value (Mandatory)

        numReceptor int  The number of receptors.



                      Value (Optional)

        switchedPowerDifference float []   numReceptor  the switched power difference \f$P_{diff}\f$ defined by \f$P_{diff} = G*(P_{on}-P_{off})\f$.

        switchedPowerSum float []   numReceptor  the switched power sum \f$P_{sum}\f$ defined by \f$P_{sum}=G(P_{on} + P_{off})\f$.

        requantizerGain float []   numReceptor  refers to the gain inserted after the synchronous power detector. For WIDAR, it is the requantizer gain (\f$G\f$).


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "SysPower"

    # the list of field names that make up key 'key'.
    _key = ["antennaId", "spectralWindowId", "feedId", "timeInterval"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = False  # if True archive binary else archive XML
    _fileAsBin = False  # if True file binary else file XML

    # A list to store the SysPowerRow instances
    _privateRows = []

    # context is a dictionary where each key is a string resulting
    # from a call to the method Key and the value is a list of rows
    # maintained in time-order
    _context = {}

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    @staticmethod
    def Key(antennaId, spectralWindowId, feedId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        The parameter values are assumed to be the appropriate type for that parameter.
        """
        result = ""

        result += antennaId.toString() + "_"

        result += spectralWindowId.toString() + "_"

        result += feedId() + "_"

        return result

    def insertByStartTime(self, x, rowlist):
        """
        Insert a SysPowerRow in a list of SysPowerRow so that it's ordered by ascending start time.

        x is a SysPowerRow to be inserted.
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
                    raise DuplicateKey("DuplicateKey exception in ", "SysPowerTable")
            elif start.get() == rowlist[k1].timeInterval.getStart().get():
                if rowlist[k1].equalByRequiredValue(x):
                    # this row already exists at k1, nothing to insert or add, return that row
                    return rowlist[k1]
                else:
                    # the time matches, but the rest of the required parameters do not, duplicate keys
                    raise DuplicateKey("DuplicateKey exception in ", "SysPowerTable")
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
                raise DuplicateKey("DuplicateKey exception in ", "SysPowerTable")
        elif start.get() == rowlist[k1].timeInterval.getStart().get():
            if rowlist[k1].equalByRequiredValue(x):
                return rowlist[k1]
            else:
                # the time matches, but the rest of the required parameters do not, duplicate keys
                raise DuplicateKey("DuplicateKey exception in ", "SysPowerTable")

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
        Create a SysPowerTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("SysPowerTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("SysPowerTable")
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
        Returns "SysPowerTable" followed by the current size of the table
        between parenthesis.
        Example : SysPowerTable(12)
        """
        return "SysPowerTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = SysPowerRow(self)
        return thisRow

    def add(self, row):
        """
        Add a row.
        row the SysPowerRow to be added.

        return a SysPowerRow. If the table contains a SysPowerRow whose attributes (key and mandatory values) are equal to those in row
        then this returns that previously added SysPowerRow, otherwise row is returned.

        raises DuplicateKey when the table contains a SysPowerRow with a key equal to the key in row but having
        a value section different from the values in x.

        note: The row is inserted in the table in such a way that all the rows having the same value of
        ( antennaId, spectralWindowId, feedId ) are stored by ascending time.
        """

        # get the key for row
        k = self.Key(row.getAntennaId(), row.getSpectralWindowId(), row.getFeedId())

        if k not in self._context:
            # add a list to context for this key for this
            self._context[k] = []

        result = None
        try:
            result = self.insertByStartTime(x, self._context[k])
        except DuplicateKey as exc:
            raise  # this will simply reraise that exception

        return result

    def newRow(self, antennaId, spectralWindowId, feedId, timeInterval, numReceptor):
        """
        Create a new SysPowerRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = SysPowerRow(self)

        thisRow.setAntennaId(antennaId)

        thisRow.setSpectralWindowId(spectralWindowId)

        thisRow.setFeedId(feedId)

        thisRow.setTimeInterval(timeInterval)

        thisRow.setNumReceptor(numReceptor)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new SysPowerRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new SysPowerRow with default values for its attributes.
        """

        return SysPowerRow(self, row)

    # ====> Append a row to its table.

    def _checkAndAdd(self, newrow):
        """
        A method to append a row to its table, used by input conversion
        methods. Not intended for external use.
        Returns the added row.
        """

        thisKey = self.Key(
            newrow.getAntennaId(), newrow.getSpectralWindowId(), newrow.getFeedId()
        )

        if thisKey not in self._context:
            self._context[thisKey] = []

        return self.insertByStartTime(newrow, self._context[thisKey])

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as a list of SysPowerRow
        """
        return self._privateRows

    def getByContext(self, antennaId, spectralWindowId, feedId):
        """
        Return all the rows sorted by ascending startTime for a given context.
        The context is defined by the value of ( antennaId, spectralWindowId, feedId ).
        A None value is returned if the table contains no rows for the given
        ( antennaId, spectralWindowId, feedId ).
        """
        thisKey = SysPowerTable.Key(antennaId, spectralWindowId, feedId)

        result = None
        if thisKey in self._context:
            result = self._context(thisKey)

        return result

    def getRowByKey(self, antennaId, spectralWindowId, feedId, timeInterval):
        """
        Returns a SysPowerRow given a key.
        return the row having the key whose values are passed as parameters, or None
        if no row exists for that key.
        """

        keystr = self.Key(antennaId, spectralWindowId, feedId)

        if keystr not in context:
            return None

        contextRows = context[keystr]
        # Is the context list empty...impossible in principle !
        if len(contextRows) == 0:
            return None

        # only one element in the context list
        if len(contextRows) == 1:
            r = contextRows[0]
            if r.getTimeInterval().contains(timeInterval.getStart()):
                return r
            return None

        # Optimizations
        last = contextRows[-1]
        if timeInterval.getStart().get() >= (
            last.getTimeInterval().getStart().get()
            + last.getTimeInterval().getDuration().get()
        ):
            # the key is past the end of contextRows
            return None

        first = contextRows[0]
        if timeInterval.getStart().get() < first.getTimeInterval().getStart().get():
            # the key is before the start of contextRows
            return None

        # the key falls in the range of context and there's more than one row, find the row, if it exists in context
        # let's use dichotomy method
        k0 = 0
        k1 = len(contextRows) - 1
        while k0 != k1:
            # Is the start time contained in the time interval of row at k0
            r = contextRows[k0]
            if r.getTimeInterval().contains(timeInterval.getStart()):
                return r

            # Is the start time contained in the time interval of row at k1
            r = contextRows[k1]
            if r.getTimeInterval().contains(timeInterval.getStart()):
                return r

            # Are the rows at k0 and at k1 consecutive
            # Then we know for sure that there is no row containing the start of timeInterval.
            if k1 == (k0 + 1):
                return None

            # make sure indexing here is always done with integer and k0 and k1 remain integers
            r = contextRows[int((k0 + k1) / 2)]
            if timeInterval.getStart().get() <= r.getTimeInterval().getStart().get():
                k1 = int((k0 + k1) / 2)
            else:
                k0 = int((k0 + k1) / 2)

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for SysPower (SysPowerTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<SysPowerTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:syspwr="http://Alma/XASDM/SysPowerTable" xsi:schemaLocation="http://Alma/XASDM/SysPowerTable http://almaobservatory.org/XML/XASDM/4/SysPowerTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</SysPowerTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a SysPower (SysPowerTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of SysPowerTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "SysPowerTable":
            raise ConversionException(
                "XML is not from a the expected table", "SysPowerTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException("schemaVersion not found in XML", "SysPowerTable")
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "SysPowerTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "SysPowerTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "SysPowerTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "SysPowerTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "SysPowerTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "SysPowerTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "SysPowerTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "SysPowerTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "SysPowerTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a SysPowerTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "SysPowerTable",
            )

        if os.path.exists(os.path.join(directory, "SysPower.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "SysPower.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the SysPower table", "SysPowerTable"
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
        with open(os.path.join(directory, "SysPower.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("SysPower.xml is empty", "SysPowerTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'SysPower.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'SysPower.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (SysPower)"
                % directory,
                "SysPowerTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for SysPower")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "SysPower.xml")
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
