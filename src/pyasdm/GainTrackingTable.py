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
# File GainTrackingTable.py
#

import pyasdm.ASDM

from .GainTrackingRow import GainTrackingRow

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


class GainTrackingTable:
    """
    The GainTrackingTable class is an ASDM table.

    Gain tracking information. Contains variable control parameters   affecting the signal coming from a receiver in an antenna.

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



        antennaId (Tag): refers to a unique row in AntennaTable. key.



        spectralWindowId (Tag): refers to a unique row in SpectralWindowTable. key.



        timeInterval (ArrayTimeInterval): time interval for which the row's content is valid. key.



        feedId (int): refers to a unique row in Feed Table key.





        numReceptor (int): the number of receptors.

        attenuator (float [] ): Array(numReceptor) the nominal value of the attenuator (one value per receptor).

        polarizationType (PolarizationType [] ): Array(numReceptor) describes the polarizations of the receptors (one value per receptor).




        samplingLevel (float): the sampling level. Optional.

        numAttFreq (int): the sizes of attSpectrum and attFreq. Optional.

        attFreq (float [] ): Array(numAttFreq) the attenuator frequencies. Optional.

        attSpectrum (Complex [] ): Array(numAttFreq) the attenuator's measured spectrum. Optional.


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
    _tableName = "GainTracking"

    # The list of field names that make up 'key'.
    _key = ["antennaId", "spectralWindowId", "timeInterval", "feedId"]

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

    # GainTrackingRow objects added from an XML file or using the add() method are kept here
    _rowList = []

    # binary table locations for rows added from a binary table file are kept here
    _rowLocList = []

    # this table has a temporal key attribute

    # the temporal key attribute values for all rows known to this table
    # (ArrayTimeInterval or ArrayTime) are kept here, in the order in which they were added.
    # The element number here is the same value used in getRow to retrieve that row.
    _rowTimesList = []

    # there are other key attributes and no auto-incrementable key attribute

    # The context dictionary contains lists of row numbers for each unique key string,
    # excluding the temporal key, and sorted by ascending order using the temporal
    # key attribute.  The values in each list correspond to row numbers that can be
    # used in getRow() as well as index into _rowTimesList.
    _context = {}

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    def getKeyName(self):
        """
        Return the list of field names that make up 'key'
        as a list of strings.
        """
        return self._key

    @staticmethod
    def Key(antennaId, spectralWindowId, feedId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        """
        result = ""

        result += str(antennaId) + "_"

        result += str(spectralWindowId) + "_"

        result += str(feedId) + "_"

        return result

    def insertByStartTime(self, x, rowIndexList):
        """
        Insert a GainTrackingRow in a list of GainTrackingRow so that it's ordered by ascending start time.

        x The GainTrackingRow to be inserted or a tuple of (rowStartLoc, timeInterval) where rowStartLoc
        is the starting location in self._eis where that row is found and timeInterval is the
        ArrayTimeInterval for that row at that location.
        rowIndexList The list where x is to be inserted.

        If the row is added, then the new row index (row number) for that row is returned. If x
        already exists in rowIndexList then it is not added and the row index found with the matching
        information in rowIndexList is returned.

        If a row matching the value of the start time of timeInterval is
        found in rowIndexList but the other required parameters do not have the same value
        then a DuplicateKey exception is raised.
        """

        # get the ArrayTime value at the start of the ArrayTimeInterval found in x

        rowStartLoc = None
        xTimeInterval = None
        xTimeStart = None
        addToRowLocList = False

        if isinstance(x, tuple):
            rowStartLoc, xTimeInterval = x
            addToRowLocList = True
            # this is the only sanity check here because this is an internal method
            # If it gets here then it's coming from a binary table file and there
            # can be no additional rows kept internally
            if self.size() != len(self._rowLocList):
                raise (
                    ValueError(
                        "GainTrackingTable internal error in insertByStartTime, attempting to insert a binary table row when there are already row objects kept internally, this should never happen"
                    )
                )
        else:
            xTimeInterval = x.getTimeInterval()

        xTimeStart = xTimeInterval.getStart().get()

        # work out where to add x to rowIndexList
        if (len(rowIndexList) == 0) or (
            xTimeStart > self._rowTimesList[rowIndexList[-1]].getStart().get()
        ):
            # it belongs at the end
            if len(rowIndexList) > 0:
                lastRowIndex = rowIndexList[-1]
                # Modify the duration of the row at lastRowIndex if and only if the start time of x
                # is located strictly before the end time of that row.
                lastTimeInterval = self._rowTimesList[lastRowIndex]
                if xTimeStart < (
                    lastTimeInterval.getStart().get()
                    + lastTimeInterval.getDuration().get()
                ):
                    # because these changes work through the reference that python maintains this
                    # change will change the value already in the list
                    lastTimeInterval.setDuration(
                        xTimeStart - lastTimeInterval.getStart().get()
                    )
            # this information will be appended to self._rowTimesList at the end,
            # that location is the row number for this newly added row
            rowIndexList.append(len(self._rowTimesList))
        elif xTimeStart < self._rowTimesList[rowIndexList[0]].getStart().get():
            # it belongs at the start
            firstRowIndex = rowIndexList[0]
            # Modify the duration of x if and only if the start time of the row at firstRowIndex
            # is located strictly before the end time of x.
            firstTimeInterval = self._rowTimesList[firstRowIndex]
            if firstTimeInterval.getStart().get() < (
                xTimeStart + xTimeInterval.getDuration().get()
            ):
                # because these changes work through the reference that python maintains this
                # change will change wherever xTimeInterval came from
                xTimeInterval.setDuration(
                    firstTimeInterval.getStart().get() - xTimeStart
                )
            # this information will be appended to self._rowTimesList at the end,
            # that location is the row number for this newly added row
            rowIndexList.insert(0, len(self._rowTimesList))
        else:
            # x is inserted somewhere inside rowIndexList; let's use a dichotomoy
            # method to find the insertion index.

            k0 = 0
            k1 = len(rowIndexList) - 1

            while k0 != (k1 - 1):
                k0TimeInterval = self._rowTimesList[rowIndexList[k0]]
                k1TimeInterval = self._rowTimesList[rowIndexList[k1]]
                if xTimeStart == k0TimeInterval.getStart().get():
                    # need to get both rows in hand here to compare
                    k0row = self.getRow(rowIndexList[k0])
                    if not isinstance(x, GainTrackingRow):
                        # get the row corresponding to rowStartLoc and store it in x
                        # so that this isn't done more than needed
                        x = self._getRowByLoc(rowStartLoc)
                    if k0row.equalByRequiredValue(x):
                        # this row already exists at k0, nothing to insert or add, return that row index
                        return rowIndexList[k0]
                    else:
                        # the start time matches, but the rest of the required parameters do not
                        raise DuplicateKey(
                            "DuplicateKey exception in ", "GainTrackingTable"
                        )
                elif xTimeStart == k1TimeInterval.getStart().get():
                    # need to get both rows in hand here to compare
                    k1row = self.getRow(rowIndexList[k1])
                    if not isinstance(x, GainTrackingRow):
                        # get the row corresponding to rowStartLoc and store it in x
                        # so that this isn't done more than needed
                        x = self._getRowByLoc(rowStartLoc)
                    if k1row.equalByRequiredValue(x):
                        # this row already exists at k1, nothing to insert or add, return that row index
                        return rowIndexList[k1]
                    else:
                        # the start time matches, but the rest of the required parameters do not
                        raise DuplicateKey(
                            "DuplicateKey exception in ", "GainTrackingTable"
                        )
                else:
                    # make sure new index is an integer
                    newIndex = int((k0 + k1) / 2)
                    if (
                        xTimeStart
                        <= self._rowTimesList[rowIndexList[newIndex]].getStart().get()
                    ):
                        k1 = newIndex
                    else:
                        k0 = newIndex

            if xTimeStart == self._rowTimesList[rowIndexList[k0]].getStart().get():
                # need to get both rows in hand here to compare
                k0row = self.getRow(rowIndexList[k0])
                if not isinstance(x, GainTrackingRow):
                    # get the row corresponding to rowStartLoc and store it in x
                    # so that this isn't done more than needed
                    x = self._getRowByLoc(rowStartLoc)
                if k0row.equalByRequiredValue(x):
                    # this row already exists at k0, nothing to insert or add, return that row index
                    return rowIndexList[k0]
                else:
                    # the start time matches, but the rest of the required paramters do not
                    raise DuplicateKey(
                        "DuplicateKey exception in ", "GainTrackingTable"
                    )
            elif xTimeStart == self._rowTimesList[rowIndexList[k1]].getStart().get():
                # need to get both rows here to compare
                k1row = self.getRow(rowIndexList[k1])
                if not isinstance(x, GainTrackingRow):
                    # get the row corresponding to rowStartLoc and store it in x
                    # so that this isn't done more than needed
                    x = self._getRowByLoc(rowStartLoc)
                if k1row.equalByRequiredValue(x):
                    # this row already exists at k1, nothing to insert or add, return that row index
                    return rowIndexList[k1]
                else:
                    # the start time matches, but the rest of the required parameters do not
                    raise DuplicateKey(
                        "DuplicateKey exception in ", "GainTrackingTable"
                    )

            # if it reaches here, it should be added, set the duration as appropriate for
            # insertion at k1, after k0, adjust duration of k0 as appropriate

            timeInterval0 = self._rowTimesList[rowIndexList[k0]]
            timeInterval1 = self._rowTimesList[rowIndexList[k0 + 1]]

            timeInterval0.setDuration(xTimeStart - timeInterval0.getStart().get())
            # use XTimeInterval but pull from x again if x is a row
            if isinstance(x, GainTrackingRow):
                xTimeInterval = x.getTimeInterval()
            xTimeInterval.setDuration(timeInterval1.getStart().get() - xTimeStart)

            # this information will be appended to self._rowTimesList at the end, that location is the row number for this newly added row
            rowIndexList.insert(k1, len(self._rowTimesList))

        # if it reaches here then the next element number of self._rowTimesList now appears in rowIndexList
        # The row location or the row itself need to be added to self._rowLocList or self._row as appropriate
        # and this time needs to be added to self._rowTimesList
        if addToRowLocList:
            self._rowLocList.append(rowStartLoc)
        else:
            self._rowList.append(x)
            x.isAdded()

        # in all cases, _rowTimesList gets xTimeInterval appended
        self._rowTimesList.append(xTimeInterval)

        # and return the element number of that newly added value
        return len(self._rowTimesList) - 1

    def __init__(self, container, checkRowUniqueness=False):
        """
        Create a GainTrackingTable attached to container.

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
                ValueError("GainTrackingTable constructor must use an ASDM instance")
            )

        self._container = container

        self._checkRowUniqueness = checkRowUniqueness

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("GainTrackingTable")
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

        self._rowTimesList = []
        self._context = {}

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
            # print("GainTracking is not present in memory, setting from file")
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
        Returns "GainTrackingTable" followed by the current size of the table
        between parenthesis.
        Example : GainTrackingTable(12)
        """
        return "GainTrackingTable(" + str(self.size()) + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = GainTrackingRow(self)
        return thisRow

    def add(self, x):
        """
        Add a row.
        x the GainTrackingRow to be added.

        return a GainTrackingRow. If the table contains a GainTrackingRow whose attributes (key and mandatory values) are equal to this in x
        then this returns that previously added GainTrackingRow, otherwise x is returned.

        raises  DuplicateKey when the table contains a GainTrackingRow with a key equal to the key in x but having
         a value section different from the values in x.
        """
        if not isinstance(x, GainTrackingRow):
            raise ValueError("x must be a  GainTrackingRow instance.")

        # get the key for x
        keystr = self.Key(x.getAntennaId(), x.getSpectralWindowId(), x.getFeedId())

        if keystr not in self._context:
            # add a list to context for this key
            self._context[keystr] = []

        result = None
        try:
            result = self.insertByStartTime(x, self._context[keystr])
        except DuplicateKey as exc:
            raise  # Simply reraise it

        # since insertByStartTime will have returned a location and add is expected to return a
        # row, return that row
        return self.getRow(result)

    def newRow(
        self,
        antennaId,
        spectralWindowId,
        timeInterval,
        feedId,
        numReceptor,
        attenuator,
        polarizationType,
    ):
        """
        Create a new GainTrackingRow initialized to the specified values.

        The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = GainTrackingRow(self)

        thisRow.setAntennaId(antennaId)

        thisRow.setSpectralWindowId(spectralWindowId)

        thisRow.setTimeInterval(timeInterval)

        thisRow.setFeedId(feedId)

        thisRow.setNumReceptor(numReceptor)

        thisRow.setAttenuator(attenuator)

        thisRow.setPolarizationType(polarizationType)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new GainTrackingRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new GainTrackingRow with default values for its attributes.
        """

        return GainTrackingRow(self, row)

    # ====> Append a row to its table.

    def checkAndAdd(self, x, skipUniquenessCheck=False):
        """
        A method to append a row to its table, used by input conversion methods.
        Not indended for external use.

        This method is appropriate for the case with an ArrayTimeInterval temporal key,
        no auto incrementable attribute, with other values in the key.

        The value of skipUniquenessCheck is not used in this version of checkAndAdd.

        Append x to its table.

        x The row to be appended or a tuple of (rowStartLocation, timeInterval, keystr) where
        rowStartLocation is the location self._eis where this row starts, timeInterval is the
        ArrayTimeInterval key value for this row and keystr is the Key() string appropriate for
        this row.
        returns  the index of the row that was inserted (the same rules used by insertByTime)
        """
        keystr = None
        if isinstance(x, tuple):
            rowStartLocation, timeInterval, keystr = x
            # change x to the tuple expected by insertByStartTime
            x = (rowStartLocation, timeInterval)
        else:
            keystr = self.Key(x.getAntennaId(), x.getSpectralWindowId(), x.getFeedId())

        if keystr not in self._context:
            self._context[keystr] = []

        return self.insertByStartTime(x, self._context[keystr])

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows.

        NOTE: if the rows are found in a binary table file then this may be an
        expensive operation since all of these rows will need to be read from disk and
        exist in memory at the same time. For a large table that may be enough to exhaust all
        resources. Use with caution.

        return all rows as a list of GainTrackingRow
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

            # adding a row can cause temporal key values to be adjusted, use the one found in self._rowTImesList to use the appropriate one
            # this is only needed for the binary rows as they are read from disk, rows already in memory will already have the correct temporal value
            # this MUST happen before isAdded is called
            result.setTimeInterval(self._rowTimesList[index])

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

    def getByContext(self, antennaId, spectralWindowId, feedId):
        """
        Returns all the rows sorted by ascending startTime for a given context.
        The context is defined by a value of ( antennaId, spectralWindowId, feedId ).

        NOTE: if hasBinary() is True then the rows found in the binary table file for that
        context are all read from the file and inserted into the list that is returned here
        and that may be an expensive operation if there are a large number of rows in this
        context.

        If hasBinary() is True then it will often be more efficient to use getListByContext to
        return the list of row numbers which can be retrieved invidually using getRow so that the
        individual rows need not be kept in memory.

        return a list  of GainTrackingRow. A None value is returned if the table contains
        no GainTrackingRow for the given ( antennaId, spectralWindowId, feedId ).
        """

        resultList = self.getListByContext(antennaId, spectralWindowId, feedId)
        result = None

        if resultList is not None:
            result = self.getRowList(resultList)

        return result

    def getListByContext(self, antennaId, spectralWindowId, feedId):
        """
        Returns a list of row numbers that share the same context, sorted by ascending startTime.
        The context is defined by a value of ( antennaId, spectralWindowId, feedId ).

        Note that if hasBinary is True then no row objects are constructed by this method.

        return a list of row numbers. A None value is returned if the table contains
        no  GainTrackingRow for the given ( antennaId, spectralWindowId, feedId ).
        """
        keystr = self.Key(antennaId, spectralWindowId, feedId)
        result = None

        if keystr in self._context:
            result = self._context[keystr]

        return result

    def getRowByKey(self, antennaId, spectralWindowId, timeInterval, feedId):
        """
        Returns a GainTrackingRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.
        """

        keystr = self.Key(antennaId, spectralWindowId, feedId)

        if keystr not in self._context:
            return None

        contextRowList = self._context[keystr]
        # Is the context list empty...impossible in principle !
        if len(contextRowList) == 0:
            return None

        # Only one element in the context list
        if len(contextRowList) == 1:
            thisRowTime = self._rowTimesList[contextRowList[0]]
            if thisRowTime.contains(timeInterval.getStart()):
                return self.getRow(contextRowList[0])
            return None

        # Optimizations
        lastRowTime = self._rowTimesList[contextRowList[-1]]
        if timeInterval.getStart().get() >= (
            lastRowTime.getStart().get() + lastRowTime.getDuration().get()
        ):
            # the requested timeInterval is after the last row in this context, it does not exist here
            return None

        firstRowTime = self._rowTimesList(contextRowsList[0])
        if timeInterval.getStart().get() < firstRowTime.getStart().get():
            # the requested timeInterval is before the start of this context, it does not exist here
            return None

        # the requested timeInterval falls within the range of this context, find the row
        # if it exists in this context
        # let's use dichotomy method
        k0 = 0
        k1 = len(contextRowList) - 1
        while k0 != k1:
            # Is the start time contained in the time interval of row at k0
            k0RowTime = self._rowTimesList[contextRowList[k0]]
            if k0RowTime.contains(timeInterval.getStart()):
                return self.getRow(contextRowList[k0])

            # Is the start time contained in the time interval of row at k1
            k1RowTime = self._rowTimesList[contextRowList[k1]]
            if k1RowTime.contains(timeInterval.getStart()):
                return self.getRow(contextRowList[k1])

            # Are the rows k0 and k1 consecutive
            # Then we know for sure that there is no row containing the start of timeInterval.
            if k1 == (k0 + 1):
                return None

            # ensure that the next row is also an integer
            nextRowIndx = int((k0 + k1) / 2)
            nextRowTime = self._rowTimesList[contextRowList[nextRowIndx]]
            if timeInterval.getStart().get() <= nextRowTime.getStart().get():
                k1 = nextRowIndx
            else:
                k0 = nextRowIndx

        # not found
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
            result = GainTrackingRow.fromBin(self._eis, self, self._attributesSeq)

            # remember this, in case the same row is requested again
            self._lastBinRow = result
            self._lastBinRowLoc = rowStartLoc

        return result

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for GainTracking (GainTrackingTable.xsd).

        returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '\n<GainTrackingTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:gntrk="http://Alma/XASDM/GainTrackingTable" xsi:schemaLocation="http://Alma/XASDM/GainTrackingTable http://almaobservatory.org/XML/XASDM/4/GainTrackingTable.xsd" schemaVersion="4" schemaRevision="-1">'
        result += "\n " + self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "\n <Container" + s[1:]

        # use self.getRow to handle binary table rows and xml rows in the correct order
        for rowNumber in range(self.size()):
            thisRow = self.getRow(rowNumber)
            result += "\n" + thisRow.toXML()
        result += "\n</GainTrackingTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a GainTracking (GainTrackingTable.xsd).
        """
        if not isinstance(xmlstr, str):
            raise ConversionException("xmlstr must be a string")

        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of "GainTrackingTable".
        if (
            not xmldom.hasChildNodes()
            or xmldom.firstChild.nodeName != "GainTrackingTable"
        ):
            raise ConversionException(
                "XML is not from the expected table", "GainTrackingTable"
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
                "schemaVersion is not an integer", "GainTrackingTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "GainTrackingTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "GainTrackingTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "GainTrackingTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "GainTrackingTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML",
                        "GainTrackingTable",
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)

                    self.checkAndAdd(row, (not self._checkRowUniqueness))
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str(exc), "GainTrackingTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "GainTrackingTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "GainTrackingTable")

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
        result += '<GainTrackingTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:gntrk="http://Alma/XASDM/GainTrackingTable" xsi:schemaLocation="http://Alma/XASDM/GainTrackingTable http://almaobservatory.org/XML/XASDM/4/GainTrackingTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += "<Entity entityId='"
        result += uidStr
        result += "' entityIdEncrypted='na' entityTypeName='GainTrackingTable' schemaVersion='1' documentVersion='1'/>\n"
        result += "<ContainerEntity entityId='"
        result += containerUID
        result += "' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n"
        result += "<BulkStoreRef file_id='"
        result += withoutUID
        result += "' byteOrder='" + str(byteOrder) + "' />\n"
        result += "<Attributes>\n"

        result += "<antennaId/>\n"
        result += "<spectralWindowId/>\n"
        result += "<timeInterval/>\n"
        result += "<feedId/>\n"
        result += "<numReceptor/>\n"
        result += "<attenuator/>\n"
        result += "<polarizationType/>\n"

        result += "<samplingLevel/>\n"
        result += "<numAttFreq/>\n"
        result += "<attFreq/>\n"
        result += "<attSpectrum/>\n"
        result += "</Attributes>\n"
        result += "</GainTrackingTable>\n"

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
                "GainTracking",
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
                    "Failed to detect the begining of the XML header.", "GainTracking"
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
                "Failed to detect the begining of the binary part.", "GainTracking"
            )

        # extract the XML header as a string
        xmlHeader = headerBytes[loc0:loc1].decode()

        xmldom = minidom.parseString(xmlHeader)
        if not xmldom.hasChildNodes():
            self._byteStream.close()
            raise ConversionException("XML is not properly structured.", "GainTracking")

        self._attributesSeq = []
        byteOrderStr = None
        versionStr = "-1"

        hdrdom = xmldom.firstChild
        if hdrdom.nodeName == "ASDMBinaryTable":
            # old style of binary data
            # assume Big_Endian and the default order of the elements
            byteOrderStr = "Big_Endian"

            self._attributesSeq.append("antennaId")

            self._attributesSeq.append("spectralWindowId")

            self._attributesSeq.append("timeInterval")

            self._attributesSeq.append("feedId")

            self._attributesSeq.append("numReceptor")

            self._attributesSeq.append("attenuator")

            self._attributesSeq.append("polarizationType")

            self._attributesSeq.append("samplingLevel")

            self._attributesSeq.append("numAttFreq")

            self._attributesSeq.append("attFreq")

            self._attributesSeq.append("attSpectrum")

            versionStr = "2"
        else:
            # c++ and Java just assume it then must be a GainTracking table
            # this is more insistant, just in case
            if hdrdom.nodeName != "GainTrackingTable":
                self._byteStream.close()
                raise ConversionException(
                    "XML Header is not from the expected table.", "GainTracking"
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
                    "GainTracking",
                )

            # loop through the child nodes, looking for BulkStoreRef and Attributes
            for hdrnode in hdrdom.childNodes:
                if hdrnode.nodeName == "BulkStoreRef":
                    if byteOrderStr is not None:
                        self._byteStream.close()
                        raise ConversionException(
                            "More than one BulkStoreRef element seen. Invalid XML header.",
                            "GainTracking",
                        )
                    if not hdrnode.hasAttributes():
                        self._byteStream.close()
                        raise ConversionException(
                            "BulkStoreRef does not contain any attributes. Invalid XML header.",
                            "GainTracking",
                        )
                    byteOrderAttr = hdrnode.attributes.getNamedItem("byteOrder")
                    if byteOrderAttr is None:
                        self._byteStream.close()
                        raise ConversionException(
                            "byteOrder attribute not found in BulkStoreRef element. Invalid XML header.",
                            "GainTracking",
                        )
                    byteOrderStr = byteOrderAttr.value
                elif hdrnode.nodeName == "Attributes":
                    if len(self._attributesSeq) > 0:
                        self._byteStream.close()
                        raise ConversionException(
                            "More than one Attributes node seen. Invalid XML header.",
                            "GainTracking",
                        )
                    if not hdrnode.hasChildNodes():
                        self._byteStream.close()
                        raise ConversionException(
                            "Attributes element has no child nodes. Invalid XML header.",
                            "GainTracking",
                        )
                    for attrnode in hdrnode.childNodes:
                        if attrnode.nodeType == attrnode.ELEMENT_NODE:
                            self._attributesSeq.append(str(attrnode.nodeName))

        if byteOrderStr is None:
            self._byteStream.close()
            raise ConversionException(
                "BulkStoreRef element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "GainTracking",
            )

        if len(self._attributesSeq) == 0:
            self._byteStream.close()
            raise ConversionException(
                "Attributes element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "GainTracking",
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
            numRows = self._container.getExpectedTableSize("GainTracking")

        # c++ reports an error when numRows is != -1 and does not agree with the value in the ASDM.xml
        # Java just uses numRows (but doesn't cover the case when numRows == -1)
        # do not check or report any difference here but cover the numRows==-1 case above

        # rows are not fully read here, just the starting location, the key information, and timeInterval
        self._lastBinRow = None
        self._lastBinRowLoc = -1
        try:
            for i in range(numRows):
                rowStart = self._eis.tell()

                # skip this row, getting only the information needed for checkAndAdd

                antennaId, spectralWindowId, timeInterval, feedId = (
                    GainTrackingRow.skipWithContextFromBin(
                        self._eis, self._attributesSeq
                    )
                )

                keystr = self.Key(antennaId, spectralWindowId, feedId)

                # temporal, no auto-incremental, other keys - 3 - ArrayTimeInterval (Pointing, etc) and 4 with ArrayTime(HistoryTotalPowwer)
                self.checkAndAdd(
                    (rowStart, timeInterval, keystr), (not self._checkRowUniqueness)
                )

        except DuplicateKey as exc:
            self._byteStream.close()
            self._eis.close()
            # reraise it as a ConversionException
            raise ConversionException(str(exc), "GainTrackingTable") from None
        except UniquenessViolationException as exc:
            self._byteStream.close()
            self._eis.close()
            msg = "UniquenessViolationException while adding row : %s" % str(exc)
            # raise a ConversionException using this msg
            raise ConversionException(msg, "GainTrackingTable") from None
        except Exception as exc:
            self._byteStream.close()
            self._eis.close()
            raise ConversionException(
                "Error while reading binary data, the exception was " + str(exc),
                "GainTrackingTable",
            ) from None

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a GainTrackingTable as those produced by the toFile method.
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
                "GainTrackingTable",
            )

        if not isinstance(directory, str):
            print("directory must be a string")

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "GainTrackingTable",
            )

        if os.path.exists(os.path.join(directory, "GainTracking.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "GainTracking.bin")):
            self.setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the GainTracking table", "GainTrackingTable"
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
                "GainTrackingTable",
            )

        filename = os.path.join(directory, "GainTracking.bin")
        self._byteStream = None
        try:
            self._byteStream = open(filename, "rb")
        except Exception as exc:
            raise ConversionException(
                "Error while opening " + filename + ". The exception was " + str(exc),
                "GainTrackingTable",
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
            with open(os.path.join(directory, "GainTracking.xml")) as f:
                xmlstr = f.read()
        except Exception as exc:
            # reraise it as a ConversionException
            raise ConversionException(str(exc), "GainTrackingTable") from None

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of its _fileAsBin data member a binary serialization
        of this (_fileAsBin==True) will be saved in a file "GainTracking.bin" or
        an XML representation (_fileAsBin==False) will be saved in a file "GainTracking.xml".
        The file is always written in a directory whose name is passed as a parameter.
        param directory The name of directory where the file containing the table's
        representation will be saved.
        raises ConversionException for any errors while writing that file.
        """
        if not isinstance(directory, str):
            raise ConversionException("directory must be a string")

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (GainTracking)"
                % directory,
                "GainTrackingTable",
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
                "GainTrackingTable",
            ) from None

        if self._fileAsBin:
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)

            # Java defaults to Big_Endian
            # c++ defaults to Machine, go with c++
            byteOrder = ByteOrder()

            # first, just the short XML file
            xmlFilePath = os.path.join(directory, "GainTracking.xml")
            if os.path.exists(xmlFilePath):
                try:
                    os.remove(xmlFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + xmlFilePath
                        + ", exception caught "
                        + str(exc),
                        "GainTracking",
                    ) from None

            # used in both files
            mimeXMLpart = self.MIMEXMLPart(byteOrder)

            # this is all that is written to the XML file
            with open(xmlFilePath, "w") as xmlfile:
                xmlfile.write(mimeXMLpart)

            # now open the possibly much longer MIME file
            mimeFilePath = os.path.join(directory, "GainTracking.bin")
            if os.path.exists(mimeFilePath):
                try:
                    os.remove(mimeFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + mimeFilePath
                        + ", exception caught "
                        + str(exc),
                        "GainTracking",
                    ) from None

            # the details are all handled in toMIME
            self.toMIME(mimeFilePath, mimeXMLpart, byteOrder)
        else:
            # The table is totally exported in a XML file.
            filePath = os.path.join(directory, "GainTracking.xml")
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
                        "GainTrackingTable",
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
                    "GainTracking",
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
