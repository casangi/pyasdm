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
# File DelayModelFixedParametersTable.py
#

import pyasdm.ASDM

from .DelayModelFixedParametersRow import DelayModelFixedParametersRow

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


class DelayModelFixedParametersTable:
    """
    The DelayModelFixedParametersTable class is an ASDM table.



    Shown here are the fields found in each row.

    The key fields are shown first and used (together) to index a unique row. Key fields
    are all required and indicated by "Key." following the description.

    Other fields are required unless "optional" is shown for that field.

    The field description text here is as found in the model used to generate the code.

    Types may be an enumeration or extended pyasdm type. Fields that are python lists
    are indicated that by "[]" in the type and having the word "Array" at the start of
    description followed by the expected number of elements in that list in parentheses.
    Lists (arrays) may be multi-dimensional (lists of lists) and are indicated
    by [][] ... etc as needed to indicate the expected number of
    dimensions. Multi-dimenstional lists will show the expected number of elements
    for each dimension also in the parenthese after "Array".

    The use of "auto-incrementable" indicates that that field is auto-generated
    when the table is created and that field is set, as necessary, to create a
    unique key for the specific row being added, by incrementing that value from
    the previous highest value needed for the rest of the elements of the key on
    that row. Such a field can not be set independently, it is only set when
    the row is added to the table by that auto-increment mechanism.

    Attributes:



        delayModelFixedParametersId (Tag): identifies a unique row in the table. auto-incrementable, key.





        delayModelVersion (str):  should include the name of the software and its version.  Something like  "CALC v11" or "VDT v1.0" or "MODEST v2.1".

        execBlockId (Tag): refers to a unique row of the ExecBlock table.




        gaussConstant (AngularRate): the Gauss gravitational constant (should be of order  1.720209895.10^{-2} rad/d  but in SI units of  rad s^{-1} ).  Optional.

        newtonianConstant (float): the newtonian constant of gravitation (should be of order  6.67259.10^{-11} m^3  kg^{-1}  s^2 ).  Optional.

        gravity (float): the gravity acceleration in  m s^{-2} . Optional.

        earthFlattening (float): the ratio of equatorial to polar radii. Optional.

        earthRadius (Length): the earth equatorial radius in  m . Optional.

        moonEarthMassRatio (float):  Optional.

        ephemerisEpoch (str): should always be 'J2000'. Optional.

        earthTideLag (float):  Optional.

        earthGM (float): the earth gravitation constant in  m^3 s^{-2} . Optional.

        moonGM (float): the moon gravitation constant in  m^3 s^{-2} . Optional.

        sunGM (float): the sun gravitation constant in  m^3 s^{-2} . Optional.

        loveNumberH (float): the earth global Love number H. Optional.

        loveNumberL (float): the earth global Love number L. Optional.

        precessionConstant (AngularRate): the general precession constant in  arcsec \  s^{-1} . Optional.

        lightTime1AU (float): the light time for 1 AU in seconds. Optional.

        speedOfLight (Speed): the speed of light in  m s^{-1} .  Optional.

        delayModelFlags (str): the delay model switches. Optional.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # set to True to turn on uniqueness checking when an existing table is read from a file (XML
    # or bin). The default of False is appropriate in most cases since the ASDM already exists and
    # the appropriate uniqueness can be assumed if the ASDM comes from the online system at the
    # telescope. Checking for uniqueness as each row is read from the existing table can be time
    # consuming for large tables. When new rows are added using the add methods then the full
    # uniqueness check is always done.
    _checkRowUniqueness = False

    # The name of this table.
    _tableName = "DelayModelFixedParameters"

    # The list of field names that make up 'key'.
    _key = ["delayModelFixedParametersId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    _fileAsBin = False  # If True file binary else file XML

    # these values are only used when rows have been loaded from a binary table file
    _eis = None  # the EndianInput stream
    _byteStream = None  # the io.BufferedReader opened and used by _eis
    # the list of required and optional attributes found in this table
    _attributesSeq = []

    # these are used to avoid re-reading the row that was just read from a binary table file
    _lastBinRow = None  # the most recent row read
    _lastBinRowloc = -1  # the location in the binary table file of _lastBinRow

    # If loaded from a binary source, the binary table related lists are used
    # first when retrieving rows and then the _rowList for any additionall rows.
    # When the binary table lists are empty then all rows come from _rowList.
    # Rows added using the add() method are always added to _rowList.
    # Rows can only be added from one file and then only if no rows have previously been added.
    # For rows added from a binary table file, only enough information to populate these lists
    # is read and the starting location of reach row is kept here. Reading the full row requires
    # seeking to the starting location of that row and then reading the row.

    # DelayModelFixedParametersRow objects added from an XML file or using the add() method are kept here
    _rowList = []

    # binary table locations for rows added from a binary table file are kept here
    _rowLocList = []

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on gaussConstant during an add operation on the table
    _gaussConstantEqTolerance = AngularRate(0.0)

    def setGaussConstantEqTolerance(self, tolerance):
        """
        A setter for the tolerance on gaussConstant
        """
        if not isinstance(tolerance, AngularRate):
            print("tolerance must be a  AngularRate instance")

        self._gaussConstantEqTolerance = AngularRate(tolerance)

    def getGaussConstantEqTolerance(self):
        """
        A getter for the tolerance on gaussConstant
        Returns the tolerance as a  AngularRate
        """
        return self._gaussConstantEqTolerance

    # The tolerance which will be used on earthRadius during an add operation on the table
    _earthRadiusEqTolerance = Length(0.0)

    def setEarthRadiusEqTolerance(self, tolerance):
        """
        A setter for the tolerance on earthRadius
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._earthRadiusEqTolerance = Length(tolerance)

    def getEarthRadiusEqTolerance(self):
        """
        A getter for the tolerance on earthRadius
        Returns the tolerance as a  Length
        """
        return self._earthRadiusEqTolerance

    # The tolerance which will be used on precessionConstant during an add operation on the table
    _precessionConstantEqTolerance = AngularRate(0.0)

    def setPrecessionConstantEqTolerance(self, tolerance):
        """
        A setter for the tolerance on precessionConstant
        """
        if not isinstance(tolerance, AngularRate):
            print("tolerance must be a  AngularRate instance")

        self._precessionConstantEqTolerance = AngularRate(tolerance)

    def getPrecessionConstantEqTolerance(self):
        """
        A getter for the tolerance on precessionConstant
        Returns the tolerance as a  AngularRate
        """
        return self._precessionConstantEqTolerance

    # The tolerance which will be used on speedOfLight during an add operation on the table
    _speedOfLightEqTolerance = Speed(0.0)

    def setSpeedOfLightEqTolerance(self, tolerance):
        """
        A setter for the tolerance on speedOfLight
        """
        if not isinstance(tolerance, Speed):
            print("tolerance must be a  Speed instance")

        self._speedOfLightEqTolerance = Speed(tolerance)

    def getSpeedOfLightEqTolerance(self):
        """
        A getter for the tolerance on speedOfLight
        Returns the tolerance as a  Speed
        """
        return self._speedOfLightEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up 'key'
        as a list of strings.
        """
        return self._key

    def __init__(self, container, checkRowUniqueness=False):
        """
        Create a DelayModelFixedParametersTable attached to container.

        container must be a ASDM instance
        All tables must know the container

        The uniqueness check is off by default. Turn that on by setting
        checkRowUniqueness to True. When this is true the the uniquess check
        that normally happens with a row is added to the table is skipped when
        the full table is read from an existing copy (e.g. an XML or bin file).
        Checking that each row is unique can take a significant time for large
        tables. This check should be unnecessary for ASDMs created by the telescope.

        The checkRowUniqueness value has no effect when adding individual rows
        to a table using the add* methods.
        """

        if not isinstance(container, pyasdm.ASDM):
            raise (
                ValueError(
                    "DelayModelFixedParametersTable constructor must use an ASDM instance"
                )
            )

        self._container = container

        self._checkRowUniqueness = checkRowUniqueness

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("DelayModelFixedParametersTable")
        self._entity.setEntityVersion("1")
        self._entity.setInstanceVersion("1")

        # the default table has no rows and so is presentInMemory
        self._presentInMemory = True
        self._loadInProgress = False

        self._eis = None
        self._byteStream = None
        self._attributesSeq = []

        self._lastBinRow = None
        self._lastBinRowLoc = -1

        self._rowList = []
        self._rowLocList = []

        self._noAutoIncIds = {}

        self._version = 0

    def __del__(self):
        """
        close any opened files used for binary table reading
        """
        self.close()

    def close(self):
        """
        close any opened files used for binary table reading
        Note: once closed this object will be useless for reading any rows found
        in the binary table and there is no way to reset and reuse this instance
        """
        # closing one should close the other but there's no error in doing both so this is safest
        #  it's not an error to close it if it was previously closed
        if self._eis is not None:
            self._eis.close()

        if self._byteStream is not None:
            self._byteStream.close()

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
            # print("DelayModelFixedParameters is not present in memory, setting from file")
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

    def setCheckRowUniqueness(self, checkRowUniqueness):
        """
        Set the checkRowUniqueness state;

        checkRowUniqueness is a boolean that sets the state. False turns off
        the uniqueness check and True turns it on.

        The checkRowUniqueness value is only used when a table is read
        from disk (XML or bin). The single row add methods always check for
        the expected uniqueness.

        returns the value of the uniqueness check state (checkRowUniqueness)
        """
        self._checkRowUniqueness = checkRowUniqueness
        return self._checkRowUniqueness

    def getCheckRowUniqueness(self):
        """
        return the current uniqueness check state
        """
        return self._checkRowUniqueness

    def size(self):
        """
        Return the number of rows in the table.
        """
        return len(self._rowList) + len(self._rowLocList)

    def getName(self):
        """
        Return the name of this table.
        """
        return self._tableName

    def hasBinaryRows(self):
        # returns True if any of the rows present are tied to a binary table and not always
        # present in memory. Binary table rows are best retrieved individually using getRow()
        # or in a list (which should be short) using getRowList().
        # The get() method may be used to return all rows but for large binary table files that
        # may exhaust all of the resources available and should be used with caution.
        return len(self._rowLocList) > 0

    def __str__(self):
        """
        Returns "DelayModelFixedParametersTable" followed by the current size of the table
        between parenthesis.
        Example : DelayModelFixedParametersTable(12)
        """
        return "DelayModelFixedParametersTable(" + str(self.size()) + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = DelayModelFixedParametersRow(self)
        return thisRow

    def add(self, x):
        """
        Look up the table for a row whose noautoincrementable attributes are matching their
        homologues in x.  If a row is found that row else autoincrement x.delayModelFixedParametersId,
        add x to its table and returns x.

        returns a DelayModelFixedParametersRow.
        x. A row to be added.
        """
        if not isinstance(x, DelayModelFixedParametersRow):
            raise ValueError("x must be a  DelayModelFixedParametersRow instance.")

        aRow = self.lookup(x.getDelayModelVersion(), x.getExecBlockId())
        if aRow is not None:
            return aRow

        # Autoincrement delayModelFixedParametersId
        x.setDelayModelFixedParametersId(
            Tag(self.size(), TagType.DelayModelFixedParameters)
        )

        self._rowList.append(x)
        x.isAdded()
        return x

    def newRow(self, delayModelVersion, execBlockId):
        """
        Create a new DelayModelFixedParametersRow initialized to the specified values.

        The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = DelayModelFixedParametersRow(self)

        thisRow.setDelayModelVersion(delayModelVersion)

        thisRow.setExecBlockId(execBlockId)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new DelayModelFixedParametersRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new DelayModelFixedParametersRow with default values for its attributes.
        """

        return DelayModelFixedParametersRow(self, row)

    # ====> Append a row to its table.

    def checkAndAdd(self, x, skipUniquenessCheck=False):
        """
        A method to append a row to it's table, used by input conversion methods.
        Not indended for external use.

        If this table has an autoincrementable attribute then check if
        x verifies the rule of uniqueness and raise an exception if not.

        Append x to its table.


        x is the row to be appended or an integer giving the row start location in self._eis
        returns the index of the row that was added

        Note that if skipUniquenessCheck is False and x is a row start location then
        the row at that location is first read so that the lookup can be done using the full
        set of required attributes.

        """
        # remember where this is being added, in case the full row needs to be read into x
        rowStartLoc = None

        if isinstance(x, int):
            rowStartLoc = x

        # is this check being skipped
        if not skipUniquenessCheck:
            if isinstance(x, int):
                # the full row is needed in x
                x = self._getRowByLoc(rowStartLoc)
            if self.lookup(x.getDelayModelVersion(), x.getExecBlockId()) is not None:
                raise UniquenessViolationException(
                    "Uniqueness violation exception in table DelayModelFixedParametersTable"
                )

        # is this check being skipped
        if not skipUniquenessCheck:
            if isinstance(x, int):
                # the full row is needed in x
                x = self._getRowByLoc(rowStartLoc)
            if self.getRowByKey(x.getDelayModelFixedParametersId()) is not None:
                raise DuplicateKey(
                    "Duplicate key exception in ", "DelayModelFixedParametersTable"
                )

        # the row is now added and the index (rownumber) of the newly added row is returned.
        result = None
        if rowStartLoc is None:
            result = len(self._rowList)
            self._rowList.append(x)
            x.isAdded()
        else:
            result = len(self._rowLocList)
            self._rowLocList.append(rowStartLoc)

        return result

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows.

        NOTE: if the rows are found in a binary table file then this may be an
        expensive operation since all of these rows will need to be read from disk and
        exist in memory at the same time. For a large table that may be enough to exhaust all
        resources. Use with caution.

        return all rows as a list of DelayModelFixedParametersRow
        """
        result = []
        if len(self._rowLocList) > 0:
            # any binary rows come first and must be fetched individually
            for index in range(len(self.rowLocList)):
                # relies on getRow to set the added and temporal value if appropriate
                # the index is the row number since binary rows come first
                result.append(self.getRow(index))
            if len(self._rowList) > 0:
                result = result + self._rowList
        else:
            result = self._rowList

        return result

    def getRow(self, index):
        """
        Return the row indicated by index, which is a row number. Rows are numbered in the order
        they were added to the table. The index must be between 0 and (size()-1).

        raises a ValueError if index is out of range for this table.
        """
        if (index < 0) or (index >= self.size()):
            raise ValueError("index out of range")

        result = None
        # rows are found first in self._rowLocList then from self._rowList as needed
        if index < len(self._rowLocList):
            result = self._getRowByLoc(self._rowLocList[index])

            # this row has been added
            result.isAdded()
        else:
            rowListIndex = index - len(self._rowLocList)
            result = self._rowList[rowListIndex]

        return result

    def getRowList(self, indexList):
        """
        Return a list of rows using a list of row numbers in same order as the list.

        indexList is a list of row numbers (see getRow)
        returns a list of row instances in the same order as indexList
        raises a ValueError if an index is out of range for this table.
        """
        result = []
        for index in indexList:
            result.append(self.getRow(index))

        return result

    def getRowByKey(self, delayModelFixedParametersId):
        """
        Returns a DelayModelFixedParametersRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.
        Note that if the rows are found in a binary table file they will each be read until a
        match is found or the list of rows is exhausted. This may be slow in that case.

        param delayModelFixedParametersId.

        """
        for rowNumber in range(self.size()):
            thisRow = self.getRow(rowNumber)

            if not thisRow.getDelayModelFixedParametersId().equals(
                delayModelFixedParametersId
            ):
                continue

            return thisRow

        # no match found
        return None

    def lookup(self, delayModelVersion, execBlockId):
        """
        Look up the table for a row whose all attributes  except the autoincrementable one
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param delayModelVersion.

        param execBlockId.

        Note: for rows found in a binary table file this method will get each row in turn until a match
        is found.
        """
        for rowNumber in range(self.size()):
            thisRow = self.getRow(rowNumber)
            if thisRow.compareNoAutoInc(delayModelVersion, execBlockId):
                return thisRow

        return None

    def _getRowByLoc(self, rowStartLoc):
        """
        Used when attached to a binary table. For internal use.

        The retrieved row is kept internally in case the same row is requested before any
        other rows to avoid re-reading it.

        Note that when used by getRow the returned row will be marked as added and
        if this is a temporal table the temporal value in _rowTimesList will be used to set the temporal value in each row.
        That should only be done for row already added to this this table.

        Return a row using the binary table values that  start at rowStartLoc in self._eis.
        """
        result = None

        if rowStartLoc == self._lastBinRowLoc:
            # no need to re-read it
            result = self._lastBinRow
        else:
            loc = self._eis.seek(rowStartLoc)
            result = DelayModelFixedParametersRow.fromBin(
                self._eis, self, self._attributesSeq
            )

            # remember this, in case the same row is requested again
            self._lastBinRow = result
            self._lastBinRowLoc = rowStartLoc

        return result

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for DelayModelFixedParameters (DelayModelFixedParametersTable.xsd).

        returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '\n<DelayModelFixedParametersTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dmfp="http://Alma/XASDM/DelayModelFixedParametersTable" xsi:schemaLocation="http://Alma/XASDM/DelayModelFixedParametersTable http://almaobservatory.org/XML/XASDM/4/DelayModelFixedParametersTable.xsd" schemaVersion="4" schemaRevision="-1">'
        result += "\n " + self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "\n <Container" + s[1:]

        # use self.getRow to handle binary table rows and xml rows in the correct order
        for rowNumber in range(self.size()):
            thisRow = self.getRow(rowNumber)
            result += "\n" + thisRow.toXML()
        result += "\n</DelayModelFixedParametersTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a DelayModelFixedParameters (DelayModelFixedParametersTable.xsd).
        """
        if not isinstance(xmlstr, str):
            raise ConversionException("xmlstr must be a string")

        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of "DelayModelFixedParametersTable".
        if (
            not xmldom.hasChildNodes()
            or xmldom.firstChild.nodeName != "DelayModelFixedParametersTable"
        ):
            raise ConversionException(
                "XML is not from the expected table", "DelayModelFixedParametersTable"
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
                "schemaVersion is not an integer", "DelayModelFixedParametersTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements",
                "DelayModelFixedParametersTable",
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML",
                        "DelayModelFixedParametersTable",
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (
                    tabEntity.getEntityTypeName() == "DelayModelFixedParametersTable"
                ):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "DelayModelFixedParametersTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML",
                        "DelayModelFixedParametersTable",
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)

                    self.checkAndAdd(row, (not self._checkRowUniqueness))
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(
                        str(exc), "DelayModelFixedParametersTable"
                    ) from None

                except UniquenessViolationException as exc:
                    msg = "UniquenessViolationException while adding row : %s" % str(
                        exc
                    )
                    # raise a ConversionException using this msg
                    raise ConversionException(
                        msg, "DelayModelFixedParametersTable"
                    ) from None

        if tabEntity is None:
            raise ConversionException(
                "No Entity seen in XML", "DelayModelFixedParametersTable"
            )
        if not hasContainerEntity:
            raise ValueError(
                "No Container Entity seen in XL", "DelayModelFixedParametersTable"
            )

        self.setEntity(tabEntity)

    def MIMEXMLPart(self, byteOrder):
        """
        Used in both the small XML file as well as the bin file when writing out as binary.
        The byte order is set by byteOrder.
        """
        uidStr = str(self.getEntity().getEntityId())
        withoutUID = uidStr[6:]
        containerUID = str(self.getContainer().getEntity().getEntityId())

        result = ""
        result += "<?xml version='1.0'  encoding='ISO-8859-1'?>"
        result += "\n"
        result += '<DelayModelFixedParametersTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dmfp="http://Alma/XASDM/DelayModelFixedParametersTable" xsi:schemaLocation="http://Alma/XASDM/DelayModelFixedParametersTable http://almaobservatory.org/XML/XASDM/4/DelayModelFixedParametersTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += "<Entity entityId='"
        result += uidStr
        result += "' entityIdEncrypted='na' entityTypeName='DelayModelFixedParametersTable' schemaVersion='1' documentVersion='1'/>\n"
        result += "<ContainerEntity entityId='"
        result += containerUID
        result += "' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n"
        result += "<BulkStoreRef file_id='"
        result += withoutUID
        result += "' byteOrder='" + str(byteOrder) + "' />\n"
        result += "<Attributes>\n"

        result += "<delayModelFixedParametersId/>\n"
        result += "<delayModelVersion/>\n"
        result += "<execBlockId/>\n"

        result += "<gaussConstant/>\n"
        result += "<newtonianConstant/>\n"
        result += "<gravity/>\n"
        result += "<earthFlattening/>\n"
        result += "<earthRadius/>\n"
        result += "<moonEarthMassRatio/>\n"
        result += "<ephemerisEpoch/>\n"
        result += "<earthTideLag/>\n"
        result += "<earthGM/>\n"
        result += "<moonGM/>\n"
        result += "<sunGM/>\n"
        result += "<loveNumberH/>\n"
        result += "<loveNumberL/>\n"
        result += "<precessionConstant/>\n"
        result += "<lightTime1AU/>\n"
        result += "<speedOfLight/>\n"
        result += "<delayModelFlags/>\n"
        result += "</Attributes>\n"
        result += "</DelayModelFixedParametersTable>\n"

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

            uidStr = str(self.getEntity().getEntityId())

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
            eos.writeInt(self.size())

            # and all of the rows
            for thisRowNumber in range(self.size()):
                thisRow = self.getRow(thisRowNumber)
                thisRow.toBin(eos)

            # The closing MIME boundary
            outBuffer.write(bytes("\n--MIME_boundary--", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))

            # close the eos, also closes outBuffer, no penalty for doing that more than once
            eos.close()

    def setFromMIME(self):
        """
        Extracts the binary part of a MIME message and deserialize its content
        to fill this with the result of the deserialization.

        The previously opened io.BufferedReader is found at self._byteStream and
        contains the data to be extracted.
        """

        if not (
            isinstance(self._byteStream, io.BufferedReader)
            and self._byteStream.seekable()
        ):
            if self._byteStream is not None:
                self._byteStream.close()
            raise ConversionException(
                "opened byteStream is not the expected io.BufferedReader or it is not seekable, this should never happen.",
                "DelayModelFixedParameters",
            )

        xmlPartMIMEHeader = bytes(str("Content-ID: <header.xml>\n\n").encode())
        binPartMIMEHeader = bytes(
            str(
                "--MIME_boundary\nContent-Type: binary/octet-stream\nContent-ID: <content.bin>\n\n"
            ).encode()
        )
        # alternative seen in some bin tables (possibly only eVLA)
        xmlPartMIMEHeaderAlt = bytes(str("Content-ID: <header.xml>\r\n\r\n").encode())

        # follow the Java example and grab the first 10000 bytes, which will always contain the header
        headerBytes = self._byteStream.read(10000)

        # Detect the XML header.
        loc0 = headerBytes.find(xmlPartMIMEHeader)
        if loc0 < 0:
            # try the alternative
            loc0 = headerBytes.find(xmlPartMIMEHeaderAlt)
            if loc0 < 0:
                # nothing else to try
                self._byteStream.close()
                raise ConversionException(
                    "Failed to detect the begining of the XML header.",
                    "DelayModelFixedParameters",
                )
            else:
                loc0 += len(xmlPartMIMEHeaderAlt)
        else:
            loc0 += len(xmlPartMIMEHeader)

        # Look for the string announcing the binary part.
        loc1 = headerBytes.find(binPartMIMEHeader, loc0)
        if loc1 < 0:
            self._byteStream.close()
            raise ConversionException(
                "Failed to detect the begining of the binary part.",
                "DelayModelFixedParameters",
            )

        # extract the XML header as a string
        xmlHeader = headerBytes[loc0:loc1].decode()

        xmldom = minidom.parseString(xmlHeader)
        if not xmldom.hasChildNodes():
            self._byteStream.close()
            raise ConversionException(
                "XML is not properly structured.", "DelayModelFixedParameters"
            )

        self._attributesSeq = []
        byteOrderStr = None
        versionStr = "-1"

        hdrdom = xmldom.firstChild
        if hdrdom.nodeName == "ASDMBinaryTable":
            # old style of binary data
            # assume Big_Endian and the default order of the elements
            byteOrderStr = "Big_Endian"

            self._attributesSeq.append("delayModelFixedParametersId")

            self._attributesSeq.append("delayModelVersion")

            self._attributesSeq.append("execBlockId")

            self._attributesSeq.append("gaussConstant")

            self._attributesSeq.append("newtonianConstant")

            self._attributesSeq.append("gravity")

            self._attributesSeq.append("earthFlattening")

            self._attributesSeq.append("earthRadius")

            self._attributesSeq.append("moonEarthMassRatio")

            self._attributesSeq.append("ephemerisEpoch")

            self._attributesSeq.append("earthTideLag")

            self._attributesSeq.append("earthGM")

            self._attributesSeq.append("moonGM")

            self._attributesSeq.append("sunGM")

            self._attributesSeq.append("loveNumberH")

            self._attributesSeq.append("loveNumberL")

            self._attributesSeq.append("precessionConstant")

            self._attributesSeq.append("lightTime1AU")

            self._attributesSeq.append("speedOfLight")

            self._attributesSeq.append("delayModelFlags")

            versionStr = "2"
        else:
            # c++ and Java just assume it then must be a DelayModelFixedParameters table
            # this is more insistant, just in case
            if hdrdom.nodeName != "DelayModelFixedParametersTable":
                self._byteStream.close()
                raise ConversionException(
                    "XML Header is not from the expected table.",
                    "DelayModelFixedParameters",
                )

            # schemaVersion becomes versionStr
            if (
                hdrdom.hasAttributes()
                and hdrdom.attributes.getNamedItem("schemaVersion") is not None
            ):
                versionStr = hdrdom.attributes.getNamedItem("schemaVersion").value

            if not hdrdom.hasChildNodes():
                self._byteStream.close()
                raise ConversionException(
                    "THe XML header is missing all of the expected elements.",
                    "DelayModelFixedParameters",
                )

            # loop through the child nodes, looking for BulkStoreRef and Attributes
            for hdrnode in hdrdom.childNodes:
                if hdrnode.nodeName == "BulkStoreRef":
                    if byteOrderStr is not None:
                        self._byteStream.close()
                        raise ConversionException(
                            "More than one BulkStoreRef element seen. Invalid XML header.",
                            "DelayModelFixedParameters",
                        )
                    if not hdrnode.hasAttributes():
                        self._byteStream.close()
                        raise ConversionException(
                            "BulkStoreRef does not contain any attributes. Invalid XML header.",
                            "DelayModelFixedParameters",
                        )
                    byteOrderAttr = hdrnode.attributes.getNamedItem("byteOrder")
                    if byteOrderAttr is None:
                        self._byteStream.close()
                        raise ConversionException(
                            "byteOrder attribute not found in BulkStoreRef element. Invalid XML header.",
                            "DelayModelFixedParameters",
                        )
                    byteOrderStr = byteOrderAttr.value
                elif hdrnode.nodeName == "Attributes":
                    if len(self._attributesSeq) > 0:
                        self._byteStream.close()
                        raise ConversionException(
                            "More than one Attributes node seen. Invalid XML header.",
                            "DelayModelFixedParameters",
                        )
                    if not hdrnode.hasChildNodes():
                        self._byteStream.close()
                        raise ConversionException(
                            "Attributes element has no child nodes. Invalid XML header.",
                            "DelayModelFixedParameters",
                        )
                    for attrnode in hdrnode.childNodes:
                        if attrnode.nodeType == attrnode.ELEMENT_NODE:
                            self._attributesSeq.append(str(attrnode.nodeName))

        if byteOrderStr is None:
            self._byteStream.close()
            raise ConversionException(
                "BulkStoreRef element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "DelayModelFixedParameters",
            )

        if len(self._attributesSeq) == 0:
            self._byteStream.close()
            raise ConversionException(
                "Attributes element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "DelayModelFixedParameters",
            )

        byteOrder = ByteOrder(byteOrderStr)

        # seek to the start of the binary part
        self._byteStream.seek(loc1 + len(binPartMIMEHeader))

        # and create the class that manages that stream and returns values as requested
        self._eis = EndianInput(self._byteStream, byteOrder)

        self._entity = Entity.fromBin(self._eis)

        # containerEntity is not used, but it is next
        containerEntity = Entity.fromBin(self._eis)

        # the number of rows
        numRows = self._eis.readInt()
        if numRows == -1:
            # when this happens (used by eVLA, I believe) use the expected size from ASDM.xml
            numRows = self._container.getExpectedTableSize("DelayModelFixedParameters")

        # c++ reports an error when numRows is != -1 and does not agree with the value in the ASDM.xml
        # Java just uses numRows (but doesn't cover the case when numRows == -1)
        # do not check or report any difference here but cover the numRows==-1 case above

        # rows are not fully read here, just the starting location, the key information, and timeInterval
        self._lastBinRow = None
        self._lastBinRowLoc = -1
        try:
            for i in range(numRows):
                rowStart = self._eis.tell()

                # non temporal, rowstart (int), skip row
                DelayModelFixedParametersRow.skipBin(self._eis, self._attributesSeq)
                self.checkAndAdd(rowStart, (not self._checkRowUniqueness))

        except DuplicateKey as exc:
            self._byteStream.close()
            self._eis.close()
            # reraise it as a ConversionException
            raise ConversionException(
                str(exc), "DelayModelFixedParametersTable"
            ) from None
        except UniquenessViolationException as exc:
            self._byteStream.close()
            self._eis.close()
            msg = "UniquenessViolationException while adding row : %s" % str(exc)
            # raise a ConversionException using this msg
            raise ConversionException(msg, "DelayModelFixedParametersTable") from None
        except Exception as exc:
            self._byteStream.close()
            self._eis.close()
            raise ConversionException(
                "Error while reading binary data, the exception was " + str(exc),
                "DelayModelFixedParametersTable",
            ) from None

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a DelayModelFixedParametersTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        param directory The name of the directory containing the file te be read and parsed.

        raises ConversionException if any error occurs while reading the
        files in the directory or parsing them.

        raises ConversionException if some rows are already known or if an attempt was made to read from a
        binary table file and that resulted in an unexpected exception, leaving the object in a mixed state.
        """
        # check if this is allowed
        if (
            (self.size() > 0)
            or (self._eis is not None)
            or (self._byteStream is not None)
        ):
            raise ConversionException(
                "A table can not be set from a file once the size is > 0 or if an unexpected error happened while reading a binary table.",
                "DelayModelFixedParametersTable",
            )

        if not isinstance(directory, str):
            print("directory must be a string")

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "DelayModelFixedParametersTable",
            )

        if os.path.exists(os.path.join(directory, "DelayModelFixedParameters.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "DelayModelFixedParameters.bin")):
            self.setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the DelayModelFixedParameters table",
                "DelayModelFixedParametersTable",
            )

    def setFromMIMEFile(self, directory):
        """
        Set this table from a MIME file.
        Used internally by setFromFile. Not intended for external use.
        """
        # The java and c++ versions read all of the contents into a byte array.
        # This uses a buffered byte stream. Created here and then
        # handed off to the setFromMIME method, which is responsible for closing it.

        if self._byteStream is not None and not self._byteStream.closed:
            raise ConversionException(
                "The binary table file is already opened and can not be re-opened. This should never happen",
                "DelayModelFixedParametersTable",
            )

        filename = os.path.join(directory, "DelayModelFixedParameters.bin")
        self._byteStream = None
        try:
            self._byteStream = open(filename, "rb")
        except Exception as exc:
            raise ConversionException(
                "Error while opening " + filename + ". The exception was " + str(exc),
                "DelayModelFixedParametersTable",
            )

        self.setFromMIME()

    def setFromXMLFile(self, directory):
        """
        This is the function used by setFromFile when the file is an XML file
        Not intended for external use.
        """

        # setFromFile has already established that this exists
        # read the entire file into a string
        xmlstr = None
        try:
            with open(os.path.join(directory, "DelayModelFixedParameters.xml")) as f:
                xmlstr = f.read()
        except Exception as exc:
            # reraise it as a ConversionException
            raise ConversionException(
                str(exc), "DelayModelFixedParametersTable"
            ) from None

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of its _fileAsBin data member a binary serialization
        of this (_fileAsBin==True) will be saved in a file "DelayModelFixedParameters.bin" or
        an XML representation (_fileAsBin==False) will be saved in a file "DelayModelFixedParameters.xml".
        The file is always written in a directory whose name is passed as a parameter.
        param directory The name of directory where the file containing the table's
        representation will be saved.
        raises ConversionException for any errors while writing that file.
        """
        if not isinstance(directory, str):
            raise ConversionException("directory must be a string")

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (DelayModelFixedParameters)"
                % directory,
                "DelayModelFixedParametersTable",
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
                "DelayModelFixedParametersTable",
            ) from None

        if self._fileAsBin:
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)

            # Java defaults to Big_Endian
            # c++ defaults to Machine, go with c++
            byteOrder = ByteOrder()

            # first, just the short XML file
            xmlFilePath = os.path.join(directory, "DelayModelFixedParameters.xml")
            if os.path.exists(xmlFilePath):
                try:
                    os.remove(xmlFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + xmlFilePath
                        + ", exception caught "
                        + str(exc),
                        "DelayModelFixedParameters",
                    ) from None

            # used in both files
            mimeXMLpart = self.MIMEXMLPart(byteOrder)

            # this is all that is written to the XML file
            with open(xmlFilePath, "w") as xmlfile:
                xmlfile.write(mimeXMLpart)

            # now open the possibly much longer MIME file
            mimeFilePath = os.path.join(directory, "DelayModelFixedParameters.bin")
            if os.path.exists(mimeFilePath):
                try:
                    os.remove(mimeFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + mimeFilePath
                        + ", exception caught "
                        + str(exc),
                        "DelayModelFixedParameters",
                    ) from None

            # the details are all handled in toMIME
            self.toMIME(mimeFilePath, mimeXMLpart, byteOrder)
        else:
            # The table is totally exported in a XML file.
            filePath = os.path.join(directory, "DelayModelFixedParameters.xml")
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
                        "DelayModelFixedParametersTable",
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
                    "DelayModelFixedParameters",
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
