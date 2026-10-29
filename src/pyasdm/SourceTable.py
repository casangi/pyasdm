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
# File SourceTable.py
#

import pyasdm.ASDM

from .SourceRow import SourceRow

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


class SourceTable:
    """
    The SourceTable class is an ASDM table.

    Summary of astromomical source information.

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



        sourceId (int): identifies a collection of rows in the table. auto-incrementable, key.



        timeInterval (ArrayTimeInterval):  the time interval of validity of the row's content. key.



        spectralWindowId (Tag): refers to a unique row in SpectralWindowTable. key.





        code (str): indicates the nature of the source.

        direction (Angle [] ): Array(2) the direction of the source.

        properMotion (AngularRate [] ): Array(2) the proper motion of the source.

        sourceName (str): the name of the source.




        directionCode (DirectionReferenceCode): identifies the direction reference frame associated to direction. Optional.

        directionEquinox (ArrayTime): the equinox associated to the direction reference frame (if required). Optional.

        calibrationGroup (int): the calibration group number. Optional.

        catalog (str): the name of the catalog. Optional.

        deltaVel (Speed): the velocity resolution. Optional.

        position (Length [] ): Array(3) the position of the source. Optional.

        numLines (int): the number of line transitions. Optional.

        transition (str [] ): Array(numLines) the names of the transitions. Optional.

        restFrequency (Frequency [] ): Array(numLines) the rest frequencies (one value per transition line). Optional.

        sysVel (Speed [] ): Array(numLines) the systemic velocity. Optional.

        rangeVel (Speed [] ): Array(2) the velocity range. Optional.

        sourceModel (SourceModel): identifies the source model. Optional.

        frequencyRefCode (FrequencyReferenceCode): the frequency reference code. Optional.

        numFreq (int): the number of frequencies. Optional.

        numStokes (int): the number of Stokes parameters. Optional.

        frequency (Frequency [] ): Array(numFreq) the array of frequencies (one value per frequency). Optional.

        frequencyInterval (Frequency [] ): Array(numFreq) an array of frequency intervals (one value per interval). Optional.

        stokesParameter (StokesParameter [] ): Array(numStokes) the array of Stokes parameters (one value per parameter). Optional.

        flux (Flux []  [] ): Array(numFreq, numStokes) the array of flux densities expressed in Jansky (Jy). Optional.

        fluxErr (Flux []  [] ): Array(numFreq, numStokes) the array of uncertainties on flux densities. Optional.

        positionAngle (Angle [] ): Array(numFreq) the major axis position angles (one value per frequency). Optional.

        positionAngleErr (Angle [] ): Array(numFreq) the uncertainties on major axis position angles. Optional.

        size (Angle []  [] ): Array(numFreq, 2) the sizes of source (one pair of values per frequency). Optional.

        sizeErr (Angle []  [] ): Array(numFreq, 2) the uncertainties on the source sizes (one pair of value per frequency). Optional.

        velRefCode (RadialVelocityReferenceCode): the velocity reference code for velocities: sysVel, rangeVel, deltaVel. Optional.

        dopplerVelocity (Speed [] ): Array(numLines) the systemic velocity. Optional.

        dopplerReferenceSystem (RadialVelocityReferenceCode): the velocity reference code for velocities: sysVel, rangeVel, deltaVel. Optional.

        dopplerCalcType (DopplerReferenceCode): the velocity reference code for velocities: sysVel, rangeVel, deltaVel. Optional.

        parallax (Angle [] ): Array(numFreq) the sizes of source (one pair of values per frequency). Optional.


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
    _tableName = "Source"

    # The list of field names that make up 'key'.
    _key = ["sourceId", "timeInterval", "spectralWindowId"]

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

    # SourceRow objects added from an XML file or using the add() method are kept here
    _rowList = []

    # binary table locations for rows added from a binary table file are kept here
    _rowLocList = []

    # this table has a temporal key attribute

    # the temporal key attribute values for all rows known to this table
    # (ArrayTimeInterval or ArrayTime) are kept here, in the order in which they were added.
    # The element number here is the same value used in getRow to retrieve that row.
    _rowTimesList = []

    # there is an auto-incrementable key attribute along with other key attributes

    # the context dictionary contains list of lists of row numbers with one set of lists of list
    # for each unique key string excluding the temporal and auto-incrementable key attributes.
    # For each key string, there is one list of row numbers for each auto-incrementable key value for
    # that key string.
    # Each list of row numbers is kept sorted by the temporal key value in ascending order.
    # The row numbers can also be used to index _rowTimesList
    _context = {}

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on direction during an add operation on the table
    _directionEqTolerance = Angle(0.0)

    def setDirectionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on direction
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._directionEqTolerance = Angle(tolerance)

    def getDirectionEqTolerance(self):
        """
        A getter for the tolerance on direction
        Returns the tolerance as a  Angle
        """
        return self._directionEqTolerance

    # The tolerance which will be used on properMotion during an add operation on the table
    _properMotionEqTolerance = AngularRate(0.0)

    def setProperMotionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on properMotion
        """
        if not isinstance(tolerance, AngularRate):
            print("tolerance must be a  AngularRate instance")

        self._properMotionEqTolerance = AngularRate(tolerance)

    def getProperMotionEqTolerance(self):
        """
        A getter for the tolerance on properMotion
        Returns the tolerance as a  AngularRate
        """
        return self._properMotionEqTolerance

    # The tolerance which will be used on deltaVel during an add operation on the table
    _deltaVelEqTolerance = Speed(0.0)

    def setDeltaVelEqTolerance(self, tolerance):
        """
        A setter for the tolerance on deltaVel
        """
        if not isinstance(tolerance, Speed):
            print("tolerance must be a  Speed instance")

        self._deltaVelEqTolerance = Speed(tolerance)

    def getDeltaVelEqTolerance(self):
        """
        A getter for the tolerance on deltaVel
        Returns the tolerance as a  Speed
        """
        return self._deltaVelEqTolerance

    # The tolerance which will be used on position during an add operation on the table
    _positionEqTolerance = Length(0.0)

    def setPositionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on position
        """
        if not isinstance(tolerance, Length):
            print("tolerance must be a  Length instance")

        self._positionEqTolerance = Length(tolerance)

    def getPositionEqTolerance(self):
        """
        A getter for the tolerance on position
        Returns the tolerance as a  Length
        """
        return self._positionEqTolerance

    # The tolerance which will be used on restFrequency during an add operation on the table
    _restFrequencyEqTolerance = Frequency(0.0)

    def setRestFrequencyEqTolerance(self, tolerance):
        """
        A setter for the tolerance on restFrequency
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._restFrequencyEqTolerance = Frequency(tolerance)

    def getRestFrequencyEqTolerance(self):
        """
        A getter for the tolerance on restFrequency
        Returns the tolerance as a  Frequency
        """
        return self._restFrequencyEqTolerance

    # The tolerance which will be used on sysVel during an add operation on the table
    _sysVelEqTolerance = Speed(0.0)

    def setSysVelEqTolerance(self, tolerance):
        """
        A setter for the tolerance on sysVel
        """
        if not isinstance(tolerance, Speed):
            print("tolerance must be a  Speed instance")

        self._sysVelEqTolerance = Speed(tolerance)

    def getSysVelEqTolerance(self):
        """
        A getter for the tolerance on sysVel
        Returns the tolerance as a  Speed
        """
        return self._sysVelEqTolerance

    # The tolerance which will be used on rangeVel during an add operation on the table
    _rangeVelEqTolerance = Speed(0.0)

    def setRangeVelEqTolerance(self, tolerance):
        """
        A setter for the tolerance on rangeVel
        """
        if not isinstance(tolerance, Speed):
            print("tolerance must be a  Speed instance")

        self._rangeVelEqTolerance = Speed(tolerance)

    def getRangeVelEqTolerance(self):
        """
        A getter for the tolerance on rangeVel
        Returns the tolerance as a  Speed
        """
        return self._rangeVelEqTolerance

    # The tolerance which will be used on frequency during an add operation on the table
    _frequencyEqTolerance = Frequency(0.0)

    def setFrequencyEqTolerance(self, tolerance):
        """
        A setter for the tolerance on frequency
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._frequencyEqTolerance = Frequency(tolerance)

    def getFrequencyEqTolerance(self):
        """
        A getter for the tolerance on frequency
        Returns the tolerance as a  Frequency
        """
        return self._frequencyEqTolerance

    # The tolerance which will be used on frequencyInterval during an add operation on the table
    _frequencyIntervalEqTolerance = Frequency(0.0)

    def setFrequencyIntervalEqTolerance(self, tolerance):
        """
        A setter for the tolerance on frequencyInterval
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._frequencyIntervalEqTolerance = Frequency(tolerance)

    def getFrequencyIntervalEqTolerance(self):
        """
        A getter for the tolerance on frequencyInterval
        Returns the tolerance as a  Frequency
        """
        return self._frequencyIntervalEqTolerance

    # The tolerance which will be used on flux during an add operation on the table
    _fluxEqTolerance = Flux(0.0)

    def setFluxEqTolerance(self, tolerance):
        """
        A setter for the tolerance on flux
        """
        if not isinstance(tolerance, Flux):
            print("tolerance must be a  Flux instance")

        self._fluxEqTolerance = Flux(tolerance)

    def getFluxEqTolerance(self):
        """
        A getter for the tolerance on flux
        Returns the tolerance as a  Flux
        """
        return self._fluxEqTolerance

    # The tolerance which will be used on fluxErr during an add operation on the table
    _fluxErrEqTolerance = Flux(0.0)

    def setFluxErrEqTolerance(self, tolerance):
        """
        A setter for the tolerance on fluxErr
        """
        if not isinstance(tolerance, Flux):
            print("tolerance must be a  Flux instance")

        self._fluxErrEqTolerance = Flux(tolerance)

    def getFluxErrEqTolerance(self):
        """
        A getter for the tolerance on fluxErr
        Returns the tolerance as a  Flux
        """
        return self._fluxErrEqTolerance

    # The tolerance which will be used on positionAngle during an add operation on the table
    _positionAngleEqTolerance = Angle(0.0)

    def setPositionAngleEqTolerance(self, tolerance):
        """
        A setter for the tolerance on positionAngle
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._positionAngleEqTolerance = Angle(tolerance)

    def getPositionAngleEqTolerance(self):
        """
        A getter for the tolerance on positionAngle
        Returns the tolerance as a  Angle
        """
        return self._positionAngleEqTolerance

    # The tolerance which will be used on positionAngleErr during an add operation on the table
    _positionAngleErrEqTolerance = Angle(0.0)

    def setPositionAngleErrEqTolerance(self, tolerance):
        """
        A setter for the tolerance on positionAngleErr
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._positionAngleErrEqTolerance = Angle(tolerance)

    def getPositionAngleErrEqTolerance(self):
        """
        A getter for the tolerance on positionAngleErr
        Returns the tolerance as a  Angle
        """
        return self._positionAngleErrEqTolerance

    # The tolerance which will be used on size during an add operation on the table
    _sizeEqTolerance = Angle(0.0)

    def setSizeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on size
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._sizeEqTolerance = Angle(tolerance)

    def getSizeEqTolerance(self):
        """
        A getter for the tolerance on size
        Returns the tolerance as a  Angle
        """
        return self._sizeEqTolerance

    # The tolerance which will be used on sizeErr during an add operation on the table
    _sizeErrEqTolerance = Angle(0.0)

    def setSizeErrEqTolerance(self, tolerance):
        """
        A setter for the tolerance on sizeErr
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._sizeErrEqTolerance = Angle(tolerance)

    def getSizeErrEqTolerance(self):
        """
        A getter for the tolerance on sizeErr
        Returns the tolerance as a  Angle
        """
        return self._sizeErrEqTolerance

    # The tolerance which will be used on dopplerVelocity during an add operation on the table
    _dopplerVelocityEqTolerance = Speed(0.0)

    def setDopplerVelocityEqTolerance(self, tolerance):
        """
        A setter for the tolerance on dopplerVelocity
        """
        if not isinstance(tolerance, Speed):
            print("tolerance must be a  Speed instance")

        self._dopplerVelocityEqTolerance = Speed(tolerance)

    def getDopplerVelocityEqTolerance(self):
        """
        A getter for the tolerance on dopplerVelocity
        Returns the tolerance as a  Speed
        """
        return self._dopplerVelocityEqTolerance

    # The tolerance which will be used on parallax during an add operation on the table
    _parallaxEqTolerance = Angle(0.0)

    def setParallaxEqTolerance(self, tolerance):
        """
        A setter for the tolerance on parallax
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._parallaxEqTolerance = Angle(tolerance)

    def getParallaxEqTolerance(self):
        """
        A getter for the tolerance on parallax
        Returns the tolerance as a  Angle
        """
        return self._parallaxEqTolerance

    # Let's use a dictionary to implement the condition "one sourceName -> one sourceId"
    _name2id_dict = {}

    def getKeyName(self):
        """
        Return the list of field names that make up 'key'
        as a list of strings.
        """
        return self._key

    @staticmethod
    def Key(spectralWindowId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        """
        result = ""

        result += str(spectralWindowId) + "_"

        return result

    def insertByStartTime(self, x, rowIndexList):
        """
        Insert a SourceRow in a list of SourceRow so that it's ordered by ascending start time.

        x The SourceRow to be inserted or a tuple of (rowStartLoc, timeInterval) where rowStartLoc
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
                        "SourceTable internal error in insertByStartTime, attempting to insert a binary table row when there are already row objects kept internally, this should never happen"
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
                    if not isinstance(x, SourceRow):
                        # get the row corresponding to rowStartLoc and store it in x
                        # so that this isn't done more than needed
                        x = self._getRowByLoc(rowStartLoc)
                    if k0row.equalByRequiredValue(x):
                        # this row already exists at k0, nothing to insert or add, return that row index
                        return rowIndexList[k0]
                    else:
                        # the start time matches, but the rest of the required parameters do not
                        raise DuplicateKey("DuplicateKey exception in ", "SourceTable")
                elif xTimeStart == k1TimeInterval.getStart().get():
                    # need to get both rows in hand here to compare
                    k1row = self.getRow(rowIndexList[k1])
                    if not isinstance(x, SourceRow):
                        # get the row corresponding to rowStartLoc and store it in x
                        # so that this isn't done more than needed
                        x = self._getRowByLoc(rowStartLoc)
                    if k1row.equalByRequiredValue(x):
                        # this row already exists at k1, nothing to insert or add, return that row index
                        return rowIndexList[k1]
                    else:
                        # the start time matches, but the rest of the required parameters do not
                        raise DuplicateKey("DuplicateKey exception in ", "SourceTable")
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
                if not isinstance(x, SourceRow):
                    # get the row corresponding to rowStartLoc and store it in x
                    # so that this isn't done more than needed
                    x = self._getRowByLoc(rowStartLoc)
                if k0row.equalByRequiredValue(x):
                    # this row already exists at k0, nothing to insert or add, return that row index
                    return rowIndexList[k0]
                else:
                    # the start time matches, but the rest of the required paramters do not
                    raise DuplicateKey("DuplicateKey exception in ", "SourceTable")
            elif xTimeStart == self._rowTimesList[rowIndexList[k1]].getStart().get():
                # need to get both rows here to compare
                k1row = self.getRow(rowIndexList[k1])
                if not isinstance(x, SourceRow):
                    # get the row corresponding to rowStartLoc and store it in x
                    # so that this isn't done more than needed
                    x = self._getRowByLoc(rowStartLoc)
                if k1row.equalByRequiredValue(x):
                    # this row already exists at k1, nothing to insert or add, return that row index
                    return rowIndexList[k1]
                else:
                    # the start time matches, but the rest of the required parameters do not
                    raise DuplicateKey("DuplicateKey exception in ", "SourceTable")

            # if it reaches here, it should be added, set the duration as appropriate for
            # insertion at k1, after k0, adjust duration of k0 as appropriate

            timeInterval0 = self._rowTimesList[rowIndexList[k0]]
            timeInterval1 = self._rowTimesList[rowIndexList[k0 + 1]]

            timeInterval0.setDuration(xTimeStart - timeInterval0.getStart().get())
            # use XTimeInterval but pull from x again if x is a row
            if isinstance(x, SourceRow):
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
        Create a SourceTable attached to container.

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
            raise (ValueError("SourceTable constructor must use an ASDM instance"))

        self._container = container

        self._checkRowUniqueness = checkRowUniqueness

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("SourceTable")
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

        self._name2id_dict = {}

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
            # print("Source is not present in memory, setting from file")
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
        Returns "SourceTable" followed by the current size of the table
        between parenthesis.
        Example : SourceTable(12)
        """
        return "SourceTable(" + str(self.size()) + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = SourceRow(self)
        return thisRow

    def add(self, x):
        """
        Append a SourceRow to the SourceTable.

        x A SourceRow instance.
        returns a SourceRow which is x if a new row was added or a matching row if that row was previously added
        """

        if not isinstance(x, SourceRow):
            raise ValueError("add requires a SourceRow instance")

        # Get the start time of the row to be inserted.
        startTime = x.getTimeInterval().getStart()

        if not (x.getSourceName() in self._name2id_dict):
            nextId = len(self._name2id_dict)
            self._name2id_dict[x.getSourceName()] = nextId

        # print("Trying to add a new row with start time = "+str(startTime))

        insertionId = self._name2id_dict[x.getSourceName()]

        # sourceId is now known from the dictionary
        # context is a dictionary with list of lists
        # the key for the dictionary is the Key() value for this row and
        # the sourceId index is an index to the outer list for that Key's list of lists and
        # row indices are sorted by timeInterval for the inner list (each sourceId)
        # the values in the inner list are row numbers suitable for use in getRow
        # as well as an index to _rowTimesList

        keystr = self.Key(x.getSpectralWindowId())

        # Determine the insertion index for the row x, possibly returning a row identical to x.
        if keystr in self._context:
            if len(self._context[keystr]) > insertionId:
                # this insertionId is known to _context, get the associated list of rows
                rowIndexList = self._context[keystr][insertionId]
                # search to see if that row is already known
                for rowIndex in rowIndexList:
                    # any matches will first match the corresponding time in self._rowTimesList
                    if startTime.equals(self._rowTimesList[rowIndex].getStart()):
                        # get the row at rowIndex so that the full comparison can be done
                        thisRow = self.getRow(rowIndex)
                        if thisRow.compareRequiredValue(
                            x.getCode(),
                            x.getDirection(),
                            x.getProperMotion(),
                            x.getSourceName(),
                        ):
                            # We have found a SourceRow with the same value then return it.
                            return thisRow
                        else:
                            # java has the throw of a UniquenessViolationException commented out
                            # cpp doesn't even have it, so do nothing here
                            # possibly this just isn't possible given the use of the
                            # separate dict for determining insertionId
                            pass
        else:
            # There is not yet a context...
            # Create and initialize an entry in the context dictionary for this combination....
            self._context[keystr] = []

        x.setSourceId(insertionId)

        contextList = self._context[keystr]
        while len(contextList) <= insertionId:
            contextList.append([])

        result = self.insertByStartTime(x, contextList[insertionId])
        return result

    def newRow(
        self, timeInterval, spectralWindowId, code, direction, properMotion, sourceName
    ):
        """
        Create a new SourceRow initialized to the specified values.

        The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = SourceRow(self)

        thisRow.setTimeInterval(timeInterval)

        thisRow.setSpectralWindowId(spectralWindowId)

        thisRow.setCode(code)

        thisRow.setDirection(direction)

        thisRow.setProperMotion(properMotion)

        thisRow.setSourceName(sourceName)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new SourceRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new SourceRow with default values for its attributes.
        """

        return SourceRow(self, row)

    # ====> Append a row to its table.

    def checkAndAdd(self, x, skipUniquenessCheck=False):
        """
        A method to append a row to its table, used by input conversion methods.
        Not indended for external use.

        This method is appropriate for an auto-incrementable attribute with an
        ArrayTimeInterval key field either with or without additional keywords.

        When skipUniquenessCheck is False the row indicated by x is used to check
        to see if that row with that sourceId is already known
        to this table. If it is known then a DuplicateKey exception is raised. If the
        full row is needed for this step and x is a tuple then the row is read from the
        binary table file.

        Append x to its table.

        x The row to be appended or a tuple of
        (rowStartLocation, time, keyString,  sourceId)
        where rowStartLocation is a location in self._eis where the row can be found,
        time is the ArrayTimeInterval keyword value for that row, keyString
        is the Key() appropriate for that row, and the final argument is the
        auto incrementable attribute value for that row.
        returns the index of the row that was inserted (the same rules as insertByStartTime
        """

        keystr = None
        sourceId = None
        rowStartLoc = None
        xTimeInterval = None

        if isinstance(x, tuple):
            rowStartLoc, xTimeInterval, keystr, sourceId = x
            # the tuple expected by insertByStartTime
            x = (rowStartLoc, xTimeInterval)
        else:
            keystr = self.Key(x.getSpectralWindowId())

            sourceId = x.getSourceId()

        # make sure keystr is known to context
        if keystr not in self._context:
            self._context[keystr] = []
        else:
            # this is the only case where the uniqueness check might be needed
            if not skipUniquenessCheck:
                if xTimeInterval is None:
                    # then x must be a row instance and we need to get this
                    xTimeInterval = x.getTimeInterval()

                # is there a list for this sourceId
                if sourceId < len(self._context[keystr]):
                    # do any of these rows have the same timeInterval
                    for rowIndex in self._context[keystr][receiverId]:
                        if self._rowTimesList[rowIndex].equals(xTimeInterval):

                            # is this a duplicate key
                            thisRow = x
                            if rowLocation is not None:
                                thisRow = self._getRowByLoc(rowLocation)
                            otherRow = self.getRow(rowIndex)
                            if otherRow.equalByRequiredValue(thisRow):
                                raise UniquenessViolation(
                                    "Uniqueness violation exception", "SourceTable."
                                )

                        raise DuplicateKey(
                            "Duplicate key exception . ("
                            + "sourceId="
                            + x.getSourceId()
                            + " "
                            + "timeInterval="
                            + x.getTimeInterval()
                            + " "
                            + "spectralWindowId="
                            + x.getSpectralWindowId()
                            + " "
                            + ") in ",
                            "SourceTable.",
                        )

        # make sure that there are enough elements in this context for sourceId
        while len(self._context[keystr]) <= sourceId:
            self._context[keystr].append([])

        return self.insertByStartTime(x, self._context[keystr][sourceId])

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows.

        NOTE: if the rows are found in a binary table file then this may be an
        expensive operation since all of these rows will need to be read from disk and
        exist in memory at the same time. For a large table that may be enough to exhaust all
        resources. Use with caution.

        return all rows as a list of SourceRow
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

    def getRowByKey(self, sourceId, timeInterval, spectralWindowId):
        """
        Returns a SourceRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.
        """

        # the ArrayTime at the start of the requested time interval
        start = timeInterval.getStart()

        keystr = self.Key(spectralWindowId)
        if keystr not in self._context:
            return None

        id = int(sourceId)

        contextRowList = self._context[keystr]
        # the first list is indexed by id so it must exist for this to find a row
        if id < len(contextRowList):
            idRowList = contextRowList[id]
            for thisRowIndex in idRowList:
                if self._rowTimesList[thisRowIndex].equals(timeInterval):
                    return self.getRow(thisRowIndex)

        # never found
        return None

    def getRowListBySourceId(self, sourceId):
        """
        Returns a list of row numbers whose key element sourceId
        is equal to the parameter sourceId.
        return a list of indices that can be used in getRowList to get a list of rows or individually
        in getRow to get each row in turn. A returned list of size 0 means that no row has been found.
        sourceId is of type int and contains the value of
        the autoincrementable attribute that is looked up in the table.
        """
        result = []

        # any of the context strings could contain a list appropriate for the requested value
        for thisKeyList in self._context.values():
            # if this has the requested value, that value can be used to index into this list
            if sourceId < len(thisKeyList):
                # this value contains rows with the requested value
                # append all of them to the result
                result.extend(thisKeyList[sourceId])

        return result

    def getRowBySourceId(self, sourceIdySourceId):
        """
        Returns a list of rows whose key element sourceId
        is equal to the parameter sourceId.
        return a list of SourceRow. A returned list of size 0 means that no row has been found.
        sourceId is of type int and contains the value of
        the autoincrementable attribute that is looked up in the table.
        Note that for rows stored in a binary table file getting all of the rows in a list may be
        and expensive operation. The getRowListBySourceId can be used
        to get a list of row numbers that can then be used in individual calls to getRow so that all rows
        in the list need not be in memory at the same time.
        """
        resultList = self.getRowListBySourceId(SourceId)

        result = []
        if len(resultList) > 0:
            result = getRowList(resultList)

        return result

    def lookup(
        self, timeInterval, spectralWindowId, code, direction, properMotion, sourceName
    ):
        """
        Look up the table for a row whose all attributes  except the autoincrementable one
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.

        param timeInterval.

        param spectralWindowId.

        param code.

        param direction.

        param properMotion.

        param sourceName.

        """
        keystr = self.Key(spectralWindowId)
        if keystr in self._context:
            # it may be found in any of the list of lists
            for thisKeyValueList in self._context.values():
                for thisList in thisKeyValueList:
                    for thisRowIndex in thisList:
                        if self._rowTimesList[thisRowIndex].contains(timeInterval):
                            # a full comparison requires thie row
                            thisRow = self.getRow(thisRowIndex)
                            if thisRow.compareNoAutoInc(
                                timeInterval,
                                spectralWindowId,
                                code,
                                direction,
                                properMotion,
                                sourceName,
                            ):
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
            result = SourceRow.fromBin(self._eis, self, self._attributesSeq)

            # remember this, in case the same row is requested again
            self._lastBinRow = result
            self._lastBinRowLoc = rowStartLoc

        return result

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for Source (SourceTable.xsd).

        returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '\n<SourceTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:src="http://Alma/XASDM/SourceTable" xsi:schemaLocation="http://Alma/XASDM/SourceTable http://almaobservatory.org/XML/XASDM/4/SourceTable.xsd" schemaVersion="4" schemaRevision="-1">'
        result += "\n " + self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "\n <Container" + s[1:]

        # use self.getRow to handle binary table rows and xml rows in the correct order
        for rowNumber in range(self.size()):
            thisRow = self.getRow(rowNumber)
            result += "\n" + thisRow.toXML()
        result += "\n</SourceTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a Source (SourceTable.xsd).
        """
        if not isinstance(xmlstr, str):
            raise ConversionException("xmlstr must be a string")

        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of "SourceTable".
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "SourceTable":
            raise ConversionException(
                "XML is not from the expected table", "SourceTable"
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
                "schemaVersion is not an integer", "SourceTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "SourceTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "SourceTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "SourceTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "SourceTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "SourceTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)

                    # need to update self._name2id_dict if this source is not yet known
                    sourceName = row.getSourceName()
                    sourceId = row.getSourceId()
                    if sourceName not in self._name2id_dict:
                        self._name2id_dict[sourceName] = sourceId
                    else:
                        # make sure the ID in that dict matches the one in this row, else raise DuplicateKey
                        if self._name2id_dict[sourceName] != sourceId:
                            msg = "DuplicateKey while reading in rows from an XML table file for the SourceTable: "
                            msg += f"sourceName='{sourceName}' having sourceId={sourceId} is already known to this table with sourceId={self._name2id_dict[sourceName]}"

                    self.checkAndAdd(row, (not self._checkRowUniqueness))
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str(exc), "SourceTable") from None

                except UniquenessViolationException as exc:
                    msg = "UniquenessViolationException while adding row : %s" % str(
                        exc
                    )
                    # raise a ConversionException using this msg
                    raise ConversionException(msg, "SourceTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "SourceTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "SourceTable")

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
        result += '<SourceTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:src="http://Alma/XASDM/SourceTable" xsi:schemaLocation="http://Alma/XASDM/SourceTable http://almaobservatory.org/XML/XASDM/4/SourceTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += "<Entity entityId='"
        result += uidStr
        result += "' entityIdEncrypted='na' entityTypeName='SourceTable' schemaVersion='1' documentVersion='1'/>\n"
        result += "<ContainerEntity entityId='"
        result += containerUID
        result += "' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n"
        result += "<BulkStoreRef file_id='"
        result += withoutUID
        result += "' byteOrder='" + str(byteOrder) + "' />\n"
        result += "<Attributes>\n"

        result += "<sourceId/>\n"
        result += "<timeInterval/>\n"
        result += "<spectralWindowId/>\n"
        result += "<code/>\n"
        result += "<direction/>\n"
        result += "<properMotion/>\n"
        result += "<sourceName/>\n"

        result += "<directionCode/>\n"
        result += "<directionEquinox/>\n"
        result += "<calibrationGroup/>\n"
        result += "<catalog/>\n"
        result += "<deltaVel/>\n"
        result += "<position/>\n"
        result += "<numLines/>\n"
        result += "<transition/>\n"
        result += "<restFrequency/>\n"
        result += "<sysVel/>\n"
        result += "<rangeVel/>\n"
        result += "<sourceModel/>\n"
        result += "<frequencyRefCode/>\n"
        result += "<numFreq/>\n"
        result += "<numStokes/>\n"
        result += "<frequency/>\n"
        result += "<frequencyInterval/>\n"
        result += "<stokesParameter/>\n"
        result += "<flux/>\n"
        result += "<fluxErr/>\n"
        result += "<positionAngle/>\n"
        result += "<positionAngleErr/>\n"
        result += "<size/>\n"
        result += "<sizeErr/>\n"
        result += "<velRefCode/>\n"
        result += "<dopplerVelocity/>\n"
        result += "<dopplerReferenceSystem/>\n"
        result += "<dopplerCalcType/>\n"
        result += "<parallax/>\n"
        result += "</Attributes>\n"
        result += "</SourceTable>\n"

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
                "Source",
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
                    "Failed to detect the begining of the XML header.", "Source"
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
                "Failed to detect the begining of the binary part.", "Source"
            )

        # extract the XML header as a string
        xmlHeader = headerBytes[loc0:loc1].decode()

        xmldom = minidom.parseString(xmlHeader)
        if not xmldom.hasChildNodes():
            self._byteStream.close()
            raise ConversionException("XML is not properly structured.", "Source")

        self._attributesSeq = []
        byteOrderStr = None
        versionStr = "-1"

        hdrdom = xmldom.firstChild
        if hdrdom.nodeName == "ASDMBinaryTable":
            # old style of binary data
            # assume Big_Endian and the default order of the elements
            byteOrderStr = "Big_Endian"

            self._attributesSeq.append("sourceId")

            self._attributesSeq.append("timeInterval")

            self._attributesSeq.append("spectralWindowId")

            self._attributesSeq.append("code")

            self._attributesSeq.append("direction")

            self._attributesSeq.append("properMotion")

            self._attributesSeq.append("sourceName")

            self._attributesSeq.append("directionCode")

            self._attributesSeq.append("directionEquinox")

            self._attributesSeq.append("calibrationGroup")

            self._attributesSeq.append("catalog")

            self._attributesSeq.append("deltaVel")

            self._attributesSeq.append("position")

            self._attributesSeq.append("numLines")

            self._attributesSeq.append("transition")

            self._attributesSeq.append("restFrequency")

            self._attributesSeq.append("sysVel")

            self._attributesSeq.append("rangeVel")

            self._attributesSeq.append("sourceModel")

            self._attributesSeq.append("frequencyRefCode")

            self._attributesSeq.append("numFreq")

            self._attributesSeq.append("numStokes")

            self._attributesSeq.append("frequency")

            self._attributesSeq.append("frequencyInterval")

            self._attributesSeq.append("stokesParameter")

            self._attributesSeq.append("flux")

            self._attributesSeq.append("fluxErr")

            self._attributesSeq.append("positionAngle")

            self._attributesSeq.append("positionAngleErr")

            self._attributesSeq.append("size")

            self._attributesSeq.append("sizeErr")

            self._attributesSeq.append("velRefCode")

            self._attributesSeq.append("dopplerVelocity")

            self._attributesSeq.append("dopplerReferenceSystem")

            self._attributesSeq.append("dopplerCalcType")

            self._attributesSeq.append("parallax")

            versionStr = "2"
        else:
            # c++ and Java just assume it then must be a Source table
            # this is more insistant, just in case
            if hdrdom.nodeName != "SourceTable":
                self._byteStream.close()
                raise ConversionException(
                    "XML Header is not from the expected table.", "Source"
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
                    "THe XML header is missing all of the expected elements.", "Source"
                )

            # loop through the child nodes, looking for BulkStoreRef and Attributes
            for hdrnode in hdrdom.childNodes:
                if hdrnode.nodeName == "BulkStoreRef":
                    if byteOrderStr is not None:
                        self._byteStream.close()
                        raise ConversionException(
                            "More than one BulkStoreRef element seen. Invalid XML header.",
                            "Source",
                        )
                    if not hdrnode.hasAttributes():
                        self._byteStream.close()
                        raise ConversionException(
                            "BulkStoreRef does not contain any attributes. Invalid XML header.",
                            "Source",
                        )
                    byteOrderAttr = hdrnode.attributes.getNamedItem("byteOrder")
                    if byteOrderAttr is None:
                        self._byteStream.close()
                        raise ConversionException(
                            "byteOrder attribute not found in BulkStoreRef element. Invalid XML header.",
                            "Source",
                        )
                    byteOrderStr = byteOrderAttr.value
                elif hdrnode.nodeName == "Attributes":
                    if len(self._attributesSeq) > 0:
                        self._byteStream.close()
                        raise ConversionException(
                            "More than one Attributes node seen. Invalid XML header.",
                            "Source",
                        )
                    if not hdrnode.hasChildNodes():
                        self._byteStream.close()
                        raise ConversionException(
                            "Attributes element has no child nodes. Invalid XML header.",
                            "Source",
                        )
                    for attrnode in hdrnode.childNodes:
                        if attrnode.nodeType == attrnode.ELEMENT_NODE:
                            self._attributesSeq.append(str(attrnode.nodeName))

        if byteOrderStr is None:
            self._byteStream.close()
            raise ConversionException(
                "BulkStoreRef element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "Source",
            )

        if len(self._attributesSeq) == 0:
            self._byteStream.close()
            raise ConversionException(
                "Attributes element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "Source",
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
            numRows = self._container.getExpectedTableSize("Source")

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

                sourceId, timeInterval, spectralWindowId, sourceName = (
                    SourceRow.skipWithContextFromBin(self._eis, self._attributesSeq)
                )

                # need to update self._name2id_dict if this source is not yet known
                if not sourceName in self._name2id_dict:
                    self._name2id_dict[sourceName] = sourceId
                else:
                    # make sure the ID in that dict matches the one in this row, else raise DuplicateKey
                    if self._name2id_dict[sourceName] != sourceId:
                        raise DuplicateKey(
                            f"DuplicateKey while reading in rows from a binary table file for the SourceTable: sourceName='{sourceName}' having sourceId={sourceId} is already known to this table with sourceId={self._name2id_dict[sourceName]}"
                        )

                keystr = self.Key(spectralWindowId)

                # temporal, with auto-incremntal, other keys : 2 (Feed, Receiver, Source)
                self.checkAndAdd(
                    (rowStart, timeInterval, keystr, sourceId),
                    (not self._checkRowUniqueness),
                )

        except DuplicateKey as exc:
            self._byteStream.close()
            self._eis.close()
            # reraise it as a ConversionException
            raise ConversionException(str(exc), "SourceTable") from None
        except UniquenessViolationException as exc:
            self._byteStream.close()
            self._eis.close()
            msg = "UniquenessViolationException while adding row : %s" % str(exc)
            # raise a ConversionException using this msg
            raise ConversionException(msg, "SourceTable") from None
        except Exception as exc:
            self._byteStream.close()
            self._eis.close()
            raise ConversionException(
                "Error while reading binary data, the exception was " + str(exc),
                "SourceTable",
            ) from None

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a SourceTable as those produced by the toFile method.
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
                "SourceTable",
            )

        if not isinstance(directory, str):
            print("directory must be a string")

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "SourceTable",
            )

        if os.path.exists(os.path.join(directory, "Source.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "Source.bin")):
            self.setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the Source table", "SourceTable"
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
                "SourceTable",
            )

        filename = os.path.join(directory, "Source.bin")
        self._byteStream = None
        try:
            self._byteStream = open(filename, "rb")
        except Exception as exc:
            raise ConversionException(
                "Error while opening " + filename + ". The exception was " + str(exc),
                "SourceTable",
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
            with open(os.path.join(directory, "Source.xml")) as f:
                xmlstr = f.read()
        except Exception as exc:
            # reraise it as a ConversionException
            raise ConversionException(str(exc), "SourceTable") from None

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of its _fileAsBin data member a binary serialization
        of this (_fileAsBin==True) will be saved in a file "Source.bin" or
        an XML representation (_fileAsBin==False) will be saved in a file "Source.xml".
        The file is always written in a directory whose name is passed as a parameter.
        param directory The name of directory where the file containing the table's
        representation will be saved.
        raises ConversionException for any errors while writing that file.
        """
        if not isinstance(directory, str):
            raise ConversionException("directory must be a string")

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (Source)"
                % directory,
                "SourceTable",
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
                "SourceTable",
            ) from None

        if self._fileAsBin:
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)

            # Java defaults to Big_Endian
            # c++ defaults to Machine, go with c++
            byteOrder = ByteOrder()

            # first, just the short XML file
            xmlFilePath = os.path.join(directory, "Source.xml")
            if os.path.exists(xmlFilePath):
                try:
                    os.remove(xmlFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + xmlFilePath
                        + ", exception caught "
                        + str(exc),
                        "Source",
                    ) from None

            # used in both files
            mimeXMLpart = self.MIMEXMLPart(byteOrder)

            # this is all that is written to the XML file
            with open(xmlFilePath, "w") as xmlfile:
                xmlfile.write(mimeXMLpart)

            # now open the possibly much longer MIME file
            mimeFilePath = os.path.join(directory, "Source.bin")
            if os.path.exists(mimeFilePath):
                try:
                    os.remove(mimeFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + mimeFilePath
                        + ", exception caught "
                        + str(exc),
                        "Source",
                    ) from None

            # the details are all handled in toMIME
            self.toMIME(mimeFilePath, mimeXMLpart, byteOrder)
        else:
            # The table is totally exported in a XML file.
            filePath = os.path.join(directory, "Source.xml")
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
                        "SourceTable",
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
                    "Source",
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
