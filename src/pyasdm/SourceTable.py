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
    The SourceTable class is an Alma table.

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

    # The name of this table.
    _tableName = "Source"

    # The list of field names that make up key 'key'.
    _key = ["sourceId", "timeInterval", "spectralWindowId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # archive as bin not used by python implementation
    # _archiveAsBin = False # If True archive binary else archive XML
    _fileAsBin = False  # If True file binary else file XML

    # A data structure to store the SourceRow s.
    # In all cases we maintain a private list of SourceRow s.
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

        result += str(spectralWindowId) + "_"

        return result

    def insertByStartTime(self, x, rowlist):
        """
        Insert a SourceRow in a list of SourceRow so that it's ordered by ascending start time.

        x The SourceRow to be inserted.
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
                        raise DuplicateKey("DuplicateKey exception in ", "SourceTable")
                elif xTimeStart == rowlist[k1].getTimeInterval().getStart().get():
                    if rowlist[k1].equalByRequiredValue(x):
                        # this row already exists at k1, nothing to insert or add, return that row
                        return rowlist[k1]
                    else:
                        # the start time matches, but the rest of the required parameters do not
                        raise DuplicateKey("DuplicateKey exception in ", "SourceTable")
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
                    raise DuplicateKey("DuplicateKey exception in ", "SourceTable")
            elif xTimeStart == rowlist[k1].getTimeInterval().getStart().get():
                if rowlist[k1].equalByRequiredValue(x):
                    # this row already exists at k1, nothing to insert or add, return that row
                    return rowlist[k1]
                else:
                    # the start time matches, but the rest of the required parameters do not
                    raise DuplicateKey("DuplicateKey exception in ", "SourceTable")

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
        Create a SourceTable attached to container.

        container must be a ASDM instance
        All tables must know the container
        """

        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("SourceTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("SourceTable")
        self._entity.setEntityVersion("1")
        self._entity.setInstanceVersion("1")

        # the default table has no rows and so is presentInMemory
        self._presentInMemory = True
        self._loadInProgress = False

        self._privateRows = []

        self._context = {}

        self._version = 0

        self._name2id_dict = {}

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

    def __str__(self):
        """
        Returns "SourceTable" followed by the current size of the table
        between parenthesis.
        Example : SourceTable(12)
        """
        return "SourceTable(" + size() + ")"

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
        """

        if not isinstance(x, SourceRow):
            raise ValueError("add requires a SourceRow instance")

        # Get the start time of the row to be inserted.
        startTime = x.getTimeInterval().getStart()

        if not (x.getSourceName() in self._name2id_dict):
            nextId = len(self._name2id_dict)
            self._name2id_dict[x.getSourceName()] = nextId

        # print("Trying to add a new row with start time = "+str(startTime))

        insertionId = self.name2id_dict.get[x.getSourceName()]

        # sourceId is now known from the dictionary
        # context is a vector of vectors, sourceId index to the outer vector and
        # timeInterval for the inner vector

        kstr = self.Key(x.getSpectralWindowId())

        # Determine the insertion index for the row x, possibly returning a row identical to x.
        if keystr in self._context:
            if len[self._context] > insertionId:
                # this insertionId is known to _context, get the associated list of rows
                idList = self._context[keystr][insertionId]
                # search to see if that row is already known
                for r in idList:
                    if startTime.eq(r.getTimeInterval().getStart()):
                        if r.compareRequiredValue(
                            x.getCode(),
                            x.getDirection(),
                            x.getProperMotion(),
                            x.getSourceName(),
                        ):
                            # We have found a SourceRow with the same value then return it.
                            return r
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
                x.getTimeInterval(),
                x.getSpectralWindowId(),
                x.getCode(),
                x.getDirection(),
                x.getProperMotion(),
                x.getSourceName(),
            )
            is not None
        ):
            raise UniquenessViolationException(
                "Uniqueness violation exception in table SourceTable"
            )

        if (
            self.getRowByKey(
                x.getSourceId(), x.getTimeInterval(), x.getSpectralWindowId()
            )
            is not None
        ):
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

        keystr = self.Key(x.getSpectralWindowId())

        i = x.getSourceId()

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
        return all rows as list of SourceRow
        """
        return self._privateRows

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

        contextRows = self._context[keystr]
        # the first list is indexed by id so it must exist for this to find a row
        if id < len(contextRows):
            idRows = contextRows[id]
            for aRow in idRows:
                if aRow.getTimeInterval().equals(timeInterval):
                    return aRow

        # never found
        return None

    def getRowBySourceId(self, sourceId):
        """
        Returns a list of rows whose key element sourceId
        is equal to the parameter sourceId.
        return a list of SourceRow. A returned list of size 0 means that no row has been found.
        sourceId is of type int and contains the value of
        the autoincrementable attribute that is looked up in the table.
        """
        result = []

        # any of the context strings could contain a list appropriate for the requested value
        for thisKeyValue in self._context.values():
            # if this has the requested value, that value can be used to index into this list
            if sourceId < len(thisKeyValue):
                # this value contains rows with the requested value
                # append all of them to the result
                result.extend(thisKeyValue[sourceId])

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
                    for thisRow in thisList:
                        if thisRow.getTimeInterval().contains(
                            timeInterval
                        ) and thisRow.compareNoAutoInc(
                            timeInterval,
                            spectralWindowId,
                            code,
                            direction,
                            properMotion,
                            sourceName,
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
        to the schema defined for Source (SourceTable.xsd).

        returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<SourceTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:src="http://Alma/XASDM/SourceTable" xsi:schemaLocation="http://Alma/XASDM/SourceTable http://almaobservatory.org/XML/XASDM/4/SourceTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</SourceTable>"
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
                    self.checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str(exc), "SourceTable") from None

                except UniquenessViolationException as exc:
                    msg = (
                        "UniquenessViolationException in row in SourceTable : %s"
                        % str(exc)
                    )

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
                "Source",
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
                "Failed to detect the begining of the XML header.", "Source"
            )

        loc0 += len(xmlPartMIMEHeader)

        # Look for the string announcing the binary part.
        loc1 = headerBytes.find(binPartMIMEHeader, loc0)
        if loc1 < 0:
            byteStream.close()
            raise ConversionException(
                "Failed to detect the begining of the binary part.", "Source"
            )

        # extract the XML header as a string
        xmlHeader = headerBytes[loc0:loc1].decode()

        xmldom = minidom.parseString(xmlHeader)
        if not xmldom.hasChildNodes():
            byteStream.close()
            raise ConversionException("XML is not properly structured.", "Source")

        attributesSeq = []
        byteOrderStr = None
        versionStr = "-1"

        hdrdom = xmldom.firstChild
        if hdrdom.nodeName == "ASDMBinaryTable":
            # old style of binary data
            # assume Big_Endian and the default order of the elements
            byteOrderStr = "Big_Endian"

            attributesSeq.append("sourceId")

            attributesSeq.append("timeInterval")

            attributesSeq.append("spectralWindowId")

            attributesSeq.append("code")

            attributesSeq.append("direction")

            attributesSeq.append("properMotion")

            attributesSeq.append("sourceName")

            attributesSeq.append("directionCode")

            attributesSeq.append("directionEquinox")

            attributesSeq.append("calibrationGroup")

            attributesSeq.append("catalog")

            attributesSeq.append("deltaVel")

            attributesSeq.append("position")

            attributesSeq.append("numLines")

            attributesSeq.append("transition")

            attributesSeq.append("restFrequency")

            attributesSeq.append("sysVel")

            attributesSeq.append("rangeVel")

            attributesSeq.append("sourceModel")

            attributesSeq.append("frequencyRefCode")

            attributesSeq.append("numFreq")

            attributesSeq.append("numStokes")

            attributesSeq.append("frequency")

            attributesSeq.append("frequencyInterval")

            attributesSeq.append("stokesParameter")

            attributesSeq.append("flux")

            attributesSeq.append("fluxErr")

            attributesSeq.append("positionAngle")

            attributesSeq.append("positionAngleErr")

            attributesSeq.append("size")

            attributesSeq.append("sizeErr")

            attributesSeq.append("velRefCode")

            attributesSeq.append("dopplerVelocity")

            attributesSeq.append("dopplerReferenceSystem")

            attributesSeq.append("dopplerCalcType")

            attributesSeq.append("parallax")

            versionStr = "2"

        else:
            # c++ and Java just assume it then must be a Source table
            # this is more insistant, just in case
            if hdrdom.nodeName != "SourceTable":
                byteStream.close()
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
                byteStream.close()
                raise ConversionException(
                    "THe XML header is missing all of the expected elements.", "Source"
                )

            # loop through the child nodes, looking for BulkStoreRef and Attributes
            for hdrnode in hdrdom.childNodes:
                if hdrnode.nodeName == "BulkStoreRef":
                    if byteOrderStr is not None:
                        byteStream.close()
                        raise ConversionException(
                            "More than one BulkStoreRef element seen. Invalid XML header.",
                            "Source",
                        )
                    if not hdrnode.hasAttributes():
                        byteStream.close()
                        raise ConversionException(
                            "BulkStoreRef does not contain any attributes. Invalid XML header.",
                            "Source",
                        )
                    byteOrderAttr = hdrnode.attributes.getNamedItem("byteOrder")
                    if byteOrderAttr is None:
                        byteStream.close()
                        raise ConversionException(
                            "byteOrder attribute not found in BulkStoreRef element. Invalid XML header.",
                            "Source",
                        )
                    byteOrderStr = byteOrderAttr.value
                elif hdrnode.nodeName == "Attributes":
                    if len(attributesSeq) > 0:
                        byteStream.close()
                        raise ConversionException(
                            "More than one Attributes node seen. Invalid XML header.",
                            "Source",
                        )
                    if not hdrnode.hasChildNodes():
                        byteStream.close()
                        raise ConversionException(
                            "Attributes element has no child nodes. Invalid XML header.",
                            "Source",
                        )
                    for attrnode in hdrnode.childNodes:
                        if attrnode.nodeType == attrnode.ELEMENT_NODE:
                            attributesSeq.append(str(attrnode.nodeName))

        if byteOrderStr is None:
            byteStream.close()
            raise ConversionException(
                "BulkStoreRef element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "Source",
            )

        if len(attributesSeq) == 0:
            byteStream.close()
            raise ConversionException(
                "Attributes element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "Source",
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
                self.checkAndAdd(SourceRow.fromBin(eis, self, attributesSeq))
                # print("row %s added, loc = %s" % (i, eis.tell()))
        except Exception as exc:
            byteStream.close()
            eis.close()
            raise ConversionException(
                "Error while reading binary data, the exception was " + str(exc),
                "Source",
            ) from None

        # there is no harm in closing both
        # print("closing")
        eis.close()
        byteStream.close()
        # print("checking")
        # print("eis : %s" % eis.closed())
        # print("byteStream : %s" % byteStream.closed)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a SourceTable as those produced  by the toFile method.
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

        filename = os.path.join(directory, "Source.bin")
        byteStream = None
        try:
            byteStream = open(filename, "rb")
        except Exception as exc:
            raise ConversionException(
                "Error while opening " + filename + ". The exception was " + str(exc),
                "Source",
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
