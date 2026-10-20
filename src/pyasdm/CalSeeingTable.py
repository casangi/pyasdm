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
# File CalSeeingTable.py
#

import pyasdm.ASDM

from .CalSeeingRow import CalSeeingRow

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


class CalSeeingTable:
    """
    The CalSeeingTable class is an Alma table.

    The seeing parameters deduced from TelCal calibrations.

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



        atmPhaseCorrection (AtmPhaseCorrection): describes how the atmospheric phase correction has been applied. key.



        calDataId (Tag): refers to a unique row in CalData Table. key.



        calReductionId (Tag): refers to a unique row in CalReduction Table. key.





        startValidTime (ArrayTime): the start time of result validity period.

        endValidTime (ArrayTime): the end time of result validity period.

        frequencyRange (Frequency [] ): Array(2) the range of frequencies over which this result is valid.

        integrationTime (Interval): the duration of averaging for the evaluation of the RMS.

        numBaseLengths (int): the number of baselines for which the the RMS phase data is evaluated.

        baselineLengths (Length [] ): Array(numBaseLengths) the lengths of the baselines (one value per baseline).

        phaseRMS (Angle [] ): Array(numBaseLengths) the RMS of phase fluctuations (one value per baseline).

        seeing (Angle): the seeing parameter, deduced for the LO1.

        seeingError (Angle): the uncertainty on the seeing parameter.




        exponent (float): the exponent of the spatial structure function. Optional.

        outerScale (Length): the outer scale. Optional.

        outerScaleRMS (Angle): the RMS of phase fluctuations at scale length outerScale. Optional.


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
    _tableName = "CalSeeing"

    # The list of field names that make up 'key'.
    _key = ["atmPhaseCorrection", "calDataId", "calReductionId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    _fileAsBin = True  # If True file binary else file XML

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
    # Rows added using the add() method are always added to _rowsList.
    # Rows can only be added from one file and then only if no rows have previously been added.
    # For rows added from a binary table file, only enough information to populate these lists
    # is read and the starting location of reach row is kept here. Reading the full row requires
    # seeking to the starting location of that row and then reading the row.

    # CalSeeingRow objects added from an XML file or using the add() method are kept here
    _rowList = []

    # binary table locations for rows added from a binary table file are kept here
    _rowLocList = []

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on frequencyRange during an add operation on the table
    _frequencyRangeEqTolerance = Frequency(0.0)

    def setFrequencyRangeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on frequencyRange
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._frequencyRangeEqTolerance = Frequency(tolerance)

    def getFrequencyRangeEqTolerance(self):
        """
        A getter for the tolerance on frequencyRange
        Returns the tolerance as a  Frequency
        """
        return self._frequencyRangeEqTolerance

    # The tolerance which will be used on baselineLengths during an add operation on the table
    _baselineLengthsEqTolerance = Length(0.0)

    def setBaselineLengthsEqTolerance(self, tolerance):
        """
        A setter for the tolerance on baselineLengths
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._baselineLengthsEqTolerance = Length(tolerance)

    def getBaselineLengthsEqTolerance(self):
        """
        A getter for the tolerance on baselineLengths
        Returns the tolerance as a  Length
        """
        return self._baselineLengthsEqTolerance

    # The tolerance which will be used on phaseRMS during an add operation on the table
    _phaseRMSEqTolerance = Angle(0.0)

    def setPhaseRMSEqTolerance(self, tolerance):
        """
        A setter for the tolerance on phaseRMS
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._phaseRMSEqTolerance = Angle(tolerance)

    def getPhaseRMSEqTolerance(self):
        """
        A getter for the tolerance on phaseRMS
        Returns the tolerance as a  Angle
        """
        return self._phaseRMSEqTolerance

    # The tolerance which will be used on seeing during an add operation on the table
    _seeingEqTolerance = Angle(0.0)

    def setSeeingEqTolerance(self, tolerance):
        """
        A setter for the tolerance on seeing
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._seeingEqTolerance = Angle(tolerance)

    def getSeeingEqTolerance(self):
        """
        A getter for the tolerance on seeing
        Returns the tolerance as a  Angle
        """
        return self._seeingEqTolerance

    # The tolerance which will be used on seeingError during an add operation on the table
    _seeingErrorEqTolerance = Angle(0.0)

    def setSeeingErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on seeingError
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._seeingErrorEqTolerance = Angle(tolerance)

    def getSeeingErrorEqTolerance(self):
        """
        A getter for the tolerance on seeingError
        Returns the tolerance as a  Angle
        """
        return self._seeingErrorEqTolerance

    # The tolerance which will be used on outerScale during an add operation on the table
    _outerScaleEqTolerance = Length(0.0)

    def setOuterScaleEqTolerance(self, tolerance):
        """
        A setter for the tolerance on outerScale
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._outerScaleEqTolerance = Length(tolerance)

    def getOuterScaleEqTolerance(self):
        """
        A getter for the tolerance on outerScale
        Returns the tolerance as a  Length
        """
        return self._outerScaleEqTolerance

    # The tolerance which will be used on outerScaleRMS during an add operation on the table
    _outerScaleRMSEqTolerance = Angle(0.0)

    def setOuterScaleRMSEqTolerance(self, tolerance):
        """
        A setter for the tolerance on outerScaleRMS
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._outerScaleRMSEqTolerance = Angle(tolerance)

    def getOuterScaleRMSEqTolerance(self):
        """
        A getter for the tolerance on outerScaleRMS
        Returns the tolerance as a  Angle
        """
        return self._outerScaleRMSEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up 'key'
        as a list of strings.
        """
        return self._key

    @staticmethod
    def Key(atmPhaseCorrection, calDataId, calReductionId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        """
        result = ""

        result += str(calDataId) + "_"

        result += str(calReductionId) + "_"

        return result

    def __init__(self, container, checkRowUniqueness=False):
        """
        Create a CalSeeingTable attached to container.

        container must be a ASDM instance
        All tables must know the container

        The uniqueness check is off by default. Turn that on by setting
        checkRowUniqueness to True. When this is true the the uniquess check
        that normally happens with a row is added to the table is skipped when
        the full table is read from an existing copy (e.g. and XML or bin file).
        Checking that each row is unique can take a significant time for large
        tables. This check should be unnecessary for ASDMs created by the telescope.

        The checkRowUniqueness value has no effect when adding individual rows
        to a table using the add* methods.
        """

        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("CalSeeingTable constructor must use a ASDM instance"))

        self._container = container

        self._checkRowUniqueness = checkRowUniqueness

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("CalSeeingTable")
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
            # print("CalSeeing is not present in memory, setting from file")
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
        Returns "CalSeeingTable" followed by the current size of the table
        between parenthesis.
        Example : CalSeeingTable(12)
        """
        return "CalSeeingTable(" + str(self.size()) + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = CalSeeingRow(self)
        return thisRow

    def add(self, x):
        """
        Add a row.
        raises a DuplicateKey Thrown if the new row has a key that is already in the table.
        If x is a list then this method is called recursively on each element of that list.
        In that case, None is always returned.
        returns the row that was added.
        """

        if isinstance(x, list):
            # add each row in the list, the type checking happens on each item
            for thisrow in x:
                self.add(thisrow)
            # return None for the list case only
            return None

        # the single row case
        if not isinstance(x, CalSeeingRow):
            raise ValueError("x must be a  CalSeeingRow instance.")

        if (
            self.getRowByKey(
                x.getAtmPhaseCorrection(), x.getCalDataId(), x.getCalReductionId()
            )
            is not None
        ):
            raise DuplicateKey(
                "["
                + x.getAtmPhaseCorrection()
                + "|"
                + x.getCalDataId()
                + "|"
                + x.getCalReductionId()
                + "]",
                "CalSeeing",
            )

        self._rowList.append(x)
        x.isAdded()
        return x

    def newRow(
        self,
        atmPhaseCorrection,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        frequencyRange,
        integrationTime,
        numBaseLengths,
        baselineLengths,
        phaseRMS,
        seeing,
        seeingError,
    ):
        """
        Create a new CalSeeingRow initialized to the specified values.

        The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = CalSeeingRow(self)

        thisRow.setAtmPhaseCorrection(atmPhaseCorrection)

        thisRow.setCalDataId(calDataId)

        thisRow.setCalReductionId(calReductionId)

        thisRow.setStartValidTime(startValidTime)

        thisRow.setEndValidTime(endValidTime)

        thisRow.setFrequencyRange(frequencyRange)

        thisRow.setIntegrationTime(integrationTime)

        thisRow.setNumBaseLengths(numBaseLengths)

        thisRow.setBaselineLengths(baselineLengths)

        thisRow.setPhaseRMS(phaseRMS)

        thisRow.setSeeing(seeing)

        thisRow.setSeeingError(seeingError)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new CalSeeingRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new CalSeeingRow with default values for its attributes.
        """

        return CalSeeingRow(self, row)

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
                x = self._getRowByLoc(rowStartLoc, isadded=False)
            if (
                self.getRowByKey(
                    x.getAtmPhaseCorrection(), x.getCalDataId(), x.getCalReductionId()
                )
                is not None
            ):
                raise DuplicateKey("Duplicate key exception in ", "CalSeeingTable")

        # when skipUniquenessCheck is True then this is all that happens, the rows are added
        # the index of the row being added is returned, set as appropriate
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

        return all rows as a list of CalSeeingRow
        """
        result = []
        if len(self._rowLocList) > 0:
            # any binary rows come first and must be fetched individually
            for rowLoc in self._rowLocList:
                result.append(self._getRowByLoc(rowLoc))
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

    def getRowByKey(self, atmPhaseCorrection, calDataId, calReductionId):
        """
        Returns a CalSeeingRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.
        Note that if the rows are found in a binary table file they will each be read until a
        match is found or the list of rows is exhausted. This may be slow in that case.

        param atmPhaseCorrection.

        param calDataId.

        param calReductionId.

        """
        for rowNumber in range(self.size()):
            thisRow = self.getRow(rowNumber)

            if thisRow.getAtmPhaseCorrection() != atmPhaseCorrection:
                continue

            if not thisRow.getCalDataId().equals(calDataId):
                continue

            if not thisRow.getCalReductionId().equals(calReductionId):
                continue

            return thisRow

        # no match found
        return None

    def lookup(
        self,
        atmPhaseCorrection,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        frequencyRange,
        integrationTime,
        numBaseLengths,
        baselineLengths,
        phaseRMS,
        seeing,
        seeingError,
    ):
        """
        Look up the table for a row whose all attributes
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param atmPhaseCorrection.

        param calDataId.

        param calReductionId.

        param startValidTime.

        param endValidTime.

        param frequencyRange.

        param integrationTime.

        param numBaseLengths.

        param baselineLengths.

        param phaseRMS.

        param seeing.

        param seeingError.

        Note: for rows found in a binary table file this method will get each row in turn until a match
        is found.
        """
        for rowNumber in range(self.size()):
            thisRow = self.getRow(rowNumber)
            if thisRow.compareNoAutoInc(
                atmPhaseCorrection,
                calDataId,
                calReductionId,
                startValidTime,
                endValidTime,
                frequencyRange,
                integrationTime,
                numBaseLengths,
                baselineLengths,
                phaseRMS,
                seeing,
                seeingError,
            ):
                return thisRow

        return None

    def _getRowByLoc(self, rowStartLoc, isadded=True):
        """
        Used when attached to a binary table. For internal use.

        If the row is in the process of being added then the row
        should not be marked as "added" yet and isadded is False. In all other cases the
        row has been added and that needs to be set when retrieving the row.

        The retrieved row is kept internally in case the same row is requested before any
        other rows to avoid re-reading it.

        Return a row using the binary table values that  start at rowStartLoc in self._eis.
        """
        result = None

        if rowStartLoc == self._lastBinRowLoc:
            # no need to re-read it
            result = self._lastBinRow
        else:
            loc = self._eis.seek(rowStartLoc)
            result = CalSeeingRow.fromBin(self._eis, self, self._attributesSeq)
            if isadded:
                result.isAdded()

            # remember this, in case the same row is requested again
            self._lastBinRow = result
            self._lastBinRowLoc = rowStartLoc

        return result

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for CalSeeing (CalSeeingTable.xsd).

        returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '\n<CalSeeingTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clsng="http://Alma/XASDM/CalSeeingTable" xsi:schemaLocation="http://Alma/XASDM/CalSeeingTable http://almaobservatory.org/XML/XASDM/4/CalSeeingTable.xsd" schemaVersion="4" schemaRevision="-1">'
        result += "\n " + self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "\n <Container" + s[1:]

        # use self.getRow to handle binary table rows and xml rows in the correct order
        for rowNumber in range(self.size()):
            thisRow = self.getRow(rowNumber)
            result += "\n" + thisRow.toXML()
        result += "\n</CalSeeingTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a CalSeeing (CalSeeingTable.xsd).
        """
        if not isinstance(xmlstr, str):
            raise ConversionException("xmlstr must be a string")

        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of "CalSeeingTable".
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "CalSeeingTable":
            raise ConversionException(
                "XML is not from the expected table", "CalSeeingTable"
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
                "schemaVersion is not an integer", "CalSeeingTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "CalSeeingTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "CalSeeingTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "CalSeeingTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "CalSeeingTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "CalSeeingTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self.checkAndAdd(row, (not self._checkRowUniqueness))
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str(exc), "CalSeeingTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalSeeingTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalSeeingTable")

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
        result += '<CalSeeingTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clsng="http://Alma/XASDM/CalSeeingTable" xsi:schemaLocation="http://Alma/XASDM/CalSeeingTable http://almaobservatory.org/XML/XASDM/4/CalSeeingTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += "<Entity entityId='"
        result += uidStr
        result += "' entityIdEncrypted='na' entityTypeName='CalSeeingTable' schemaVersion='1' documentVersion='1'/>\n"
        result += "<ContainerEntity entityId='"
        result += containerUID
        result += "' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n"
        result += "<BulkStoreRef file_id='"
        result += withoutUID
        result += "' byteOrder='" + str(byteOrder) + "' />\n"
        result += "<Attributes>\n"

        result += "<atmPhaseCorrection/>\n"
        result += "<calDataId/>\n"
        result += "<calReductionId/>\n"
        result += "<startValidTime/>\n"
        result += "<endValidTime/>\n"
        result += "<frequencyRange/>\n"
        result += "<integrationTime/>\n"
        result += "<numBaseLengths/>\n"
        result += "<baselineLengths/>\n"
        result += "<phaseRMS/>\n"
        result += "<seeing/>\n"
        result += "<seeingError/>\n"

        result += "<exponent/>\n"
        result += "<outerScale/>\n"
        result += "<outerScaleRMS/>\n"
        result += "</Attributes>\n"
        result += "</CalSeeingTable>\n"

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
                "CalSeeing",
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
                    "Failed to detect the begining of the XML header.", "CalSeeing"
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
                "Failed to detect the begining of the binary part.", "CalSeeing"
            )

        # extract the XML header as a string
        xmlHeader = headerBytes[loc0:loc1].decode()

        xmldom = minidom.parseString(xmlHeader)
        if not xmldom.hasChildNodes():
            self._byteStream.close()
            raise ConversionException("XML is not properly structured.", "CalSeeing")

        self._attributesSeq = []
        byteOrderStr = None
        versionStr = "-1"

        hdrdom = xmldom.firstChild
        if hdrdom.nodeName == "ASDMBinaryTable":
            # old style of binary data
            # assume Big_Endian and the default order of the elements
            byteOrderStr = "Big_Endian"

            self._attributesSeq.append("atmPhaseCorrection")

            self._attributesSeq.append("calDataId")

            self._attributesSeq.append("calReductionId")

            self._attributesSeq.append("startValidTime")

            self._attributesSeq.append("endValidTime")

            self._attributesSeq.append("frequencyRange")

            self._attributesSeq.append("integrationTime")

            self._attributesSeq.append("numBaseLengths")

            self._attributesSeq.append("baselineLengths")

            self._attributesSeq.append("phaseRMS")

            self._attributesSeq.append("seeing")

            self._attributesSeq.append("seeingError")

            self._attributesSeq.append("exponent")

            self._attributesSeq.append("outerScale")

            self._attributesSeq.append("outerScaleRMS")

            versionStr = "2"
        else:
            # c++ and Java just assume it then must be a CalSeeing table
            # this is more insistant, just in case
            if hdrdom.nodeName != "CalSeeingTable":
                self._byteStream.close()
                raise ConversionException(
                    "XML Header is not from the expected table.", "CalSeeing"
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
                    "CalSeeing",
                )

            # loop through the child nodes, looking for BulkStoreRef and Attributes
            for hdrnode in hdrdom.childNodes:
                if hdrnode.nodeName == "BulkStoreRef":
                    if byteOrderStr is not None:
                        self._byteStream.close()
                        raise ConversionException(
                            "More than one BulkStoreRef element seen. Invalid XML header.",
                            "CalSeeing",
                        )
                    if not hdrnode.hasAttributes():
                        self._byteStream.close()
                        raise ConversionException(
                            "BulkStoreRef does not contain any attributes. Invalid XML header.",
                            "CalSeeing",
                        )
                    byteOrderAttr = hdrnode.attributes.getNamedItem("byteOrder")
                    if byteOrderAttr is None:
                        self._byteStream.close()
                        raise ConversionException(
                            "byteOrder attribute not found in BulkStoreRef element. Invalid XML header.",
                            "CalSeeing",
                        )
                    byteOrderStr = byteOrderAttr.value
                elif hdrnode.nodeName == "Attributes":
                    if len(self._attributesSeq) > 0:
                        self._byteStream.close()
                        raise ConversionException(
                            "More than one Attributes node seen. Invalid XML header.",
                            "CalSeeing",
                        )
                    if not hdrnode.hasChildNodes():
                        self._byteStream.close()
                        raise ConversionException(
                            "Attributes element has no child nodes. Invalid XML header.",
                            "CalSeeing",
                        )
                    for attrnode in hdrnode.childNodes:
                        if attrnode.nodeType == attrnode.ELEMENT_NODE:
                            self._attributesSeq.append(str(attrnode.nodeName))

        if byteOrderStr is None:
            self._byteStream.close()
            raise ConversionException(
                "BulkStoreRef element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "CalSeeing",
            )

        if len(self._attributesSeq) == 0:
            self._byteStream.close()
            raise ConversionException(
                "Attributes element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "CalSeeing",
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
            numRows = self._container.getExpectedTableSize("CalSeeing")

        # c++ reports an error when numRows is != -1 and does not agree with the value in the ASDM.xml
        # Java just uses numRows (but doesn't cover the case when numRows == -1)
        # do not check or report any difference here but cover the numRows==-1 case above

        # rows are not fully read here, just the starting location, the key information, and timeInterval
        self._lastBinRow = None
        self._lastBinRowLoc = -1
        try:
            for i in range(numRows):
                rowStart = self._eis.tell()

                # non temporal - 1, rowstart (int), skip row
                CalSeeingRow.skipBin(self._eis, self._attributesSeq)
                self.checkAndAdd(rowStart, (not self._checkRowUniqueness))

        except DuplicateKey as exc:
            self._byteStream.close()
            self._eis.close()
            # reraise it as a ConversionException
            raise ConversionException(str(exc), "CalSeeingTable") from None
        except UniquenessViolationException as exc:
            self._byteStream.close()
            self._eis.close()
            msg = "UniquenessViolationException while adding row : %s" % str(exc)
            # raise a ConversionException using this msg
            raise ConversionException(msg, "CalSeeingTable") from None
        except Exception as exc:
            self._byteStream.close()
            self._eis.close()
            raise ConversionException(
                "Error while reading binary data, the exception was " + str(exc),
                "CalSeeingTable",
            ) from None

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalSeeingTable as those produced by the toFile method.
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
                "CalSeeingTable",
            )

        if not isinstance(directory, str):
            print("directory must be a string")

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "CalSeeingTable",
            )

        if os.path.exists(os.path.join(directory, "CalSeeing.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalSeeing.bin")):
            self.setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalSeeing table", "CalSeeingTable"
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
                "CalSeeingTable",
            )

        filename = os.path.join(directory, "CalSeeing.bin")
        self._byteStream = None
        try:
            self._byteStream = open(filename, "rb")
        except Exception as exc:
            raise ConversionException(
                "Error while opening " + filename + ". The exception was " + str(exc),
                "CalSeeingTable",
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
            with open(os.path.join(directory, "CalSeeing.xml")) as f:
                xmlstr = f.read()
        except Exception as exc:
            # reraise it as a ConversionException
            raise ConversionException(str(exc), "CalSeeingTable") from None

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of its _fileAsBin data member a binary serialization
        of this (_fileAsBin==True) will be saved in a file "CalSeeing.bin" or
        an XML representation (_fileAsBin==False) will be saved in a file "CalSeeing.xml".
        The file is always written in a directory whose name is passed as a parameter.
        param directory The name of directory where the file containing the table's
        representation will be saved.
        raises ConversionException for any errors while writing that file.
        """
        if not isinstance(directory, str):
            raise ConversionException("directory must be a string")

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalSeeing)"
                % directory,
                "CalSeeingTable",
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
                "CalSeeingTable",
            ) from None

        if self._fileAsBin:
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)

            # Java defaults to Big_Endian
            # c++ defaults to Machine, go with c++
            byteOrder = ByteOrder()

            # first, just the short XML file
            xmlFilePath = os.path.join(directory, "CalSeeing.xml")
            if os.path.exists(xmlFilePath):
                try:
                    os.remove(xmlFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + xmlFilePath
                        + ", exception caught "
                        + str(exc),
                        "CalSeeing",
                    ) from None

            # used in both files
            mimeXMLpart = self.MIMEXMLPart(byteOrder)

            # this is all that is written to the XML file
            with open(xmlFilePath, "w") as xmlfile:
                xmlfile.write(mimeXMLpart)

            # now open the possibly much longer MIME file
            mimeFilePath = os.path.join(directory, "CalSeeing.bin")
            if os.path.exists(mimeFilePath):
                try:
                    os.remove(mimeFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + mimeFilePath
                        + ", exception caught "
                        + str(exc),
                        "CalSeeing",
                    ) from None

            # the details are all handled in toMIME
            self.toMIME(mimeFilePath, mimeXMLpart, byteOrder)
        else:
            # The table is totally exported in a XML file.
            filePath = os.path.join(directory, "CalSeeing.xml")
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
                        "CalSeeingTable",
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
                    "CalSeeing",
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
