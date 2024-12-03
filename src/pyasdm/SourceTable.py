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
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class SourceTable(Representable):
    """
    The SourceTable class is an Alma table.

     Role
     Summary of astromomical source information.

     Generated from model's revision -1, branch

     Attributes of Source

                  Key

    sourceId int identifies a collection of rows in the table.

    timeInterval ArrayTimeInterval  the time interval of validity of the row's content.

    spectralWindowId Tag refers to a unique row in SpectralWindowTable.



                  Value (Mandatory)

    code str  indicates the nature of the source.

    direction Angle []   2  the direction of the source.

    properMotion AngularRate []   2  the proper motion of the source.

    sourceName str  the name of the source.



                  Value (Optional)

    directionCode DirectionReferenceCode  identifies the direction reference frame associated to direction.

    directionEquinox ArrayTime  the equinox associated to the direction reference frame (if required).

    calibrationGroup int  the calibration group number.

    catalog str  the name of the catalog.

    deltaVel Speed  the velocity resolution.

    position Length []   3  the position of the source.

    numLines int  the number of line transitions.

    transition str []   numLines  the names of the transitions.

    restFrequency Frequency []   numLines  the rest frequencies (one value per transition line).

    sysVel Speed []   numLines  the systemic velocity.

    rangeVel Speed []   2  the velocity range.

    sourceModel SourceModel  identifies the source model.

    frequencyRefCode FrequencyReferenceCode  the frequency reference code.

    numFreq int  the number of frequencies.

    numStokes int  the number of Stokes parameters.

    frequency Frequency []   numFreq  the array of frequencies (one value per frequency).

    frequencyInterval Frequency []   numFreq  an array of frequency intervals (one value per interval).

    stokesParameter StokesParameter []   numStokes  the array of Stokes parameters (one value per parameter).

    flux Flux []  []   numFreq, numStokes  the array of flux densities expressed in Jansky (Jy).

    fluxErr Flux []  []   numFreq, numStokes  the array of uncertainties on flux densities.

    positionAngle Angle []   numFreq  the major axis position angles (one value per frequency).

    positionAngleErr Angle []   numFreq  the uncertainties on major axis position angles.

    size Angle []  []   numFreq, 2  the sizes of source (one pair of values per frequency).

    sizeErr Angle []  []   numFreq, 2  the uncertainties on the source sizes (one pair of value per frequency).

    velRefCode RadialVelocityReferenceCode  the velocity reference code for velocities: sysVel, rangeVel, deltaVel.

    dopplerVelocity Speed []   numLines  the systemic velocity.

    dopplerReferenceSystem RadialVelocityReferenceCode  the velocity reference code for velocities: sysVel, rangeVel, deltaVel.

    dopplerCalcType DopplerReferenceCode  the velocity reference code for velocities: sysVel, rangeVel, deltaVel.

    parallax Angle []   numFreq  the sizes of source (one pair of values per frequency).


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "Source"

    # the list of field names that make up key 'key'.
    _key = ["sourceId", "timeInterval", "spectralWindowId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = False  # if True archive binary else archive XML
    _fileAsBin = False  # if True file binary else file XML

    # A list to store the SourceRow instances
    _privateRows = []

    # context is dictionary of lists of rows where each key is a string resulting
    # from a call to the method Key and the value is list of rows sharing that key,
    # maintained sorted in time-order.
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
        self._directionEqTolerance = Angle(tolerance)

    # A getter for the tolerance on direction
    def getDirectionEqTolerance(self):
        """
        A getter for the tolerance on direction
        """
        return self._directionEqTolerance

    # The tolerance which will be used on properMotion during an add operation on the table
    _properMotionEqTolerance = AngularRate(0.0)

    def setProperMotionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on properMotion
        """
        self._properMotionEqTolerance = AngularRate(tolerance)

    # A getter for the tolerance on properMotion
    def getProperMotionEqTolerance(self):
        """
        A getter for the tolerance on properMotion
        """
        return self._properMotionEqTolerance

    # The tolerance which will be used on deltaVel during an add operation on the table
    _deltaVelEqTolerance = Speed(0.0)

    def setDeltaVelEqTolerance(self, tolerance):
        """
        A setter for the tolerance on deltaVel
        """
        self._deltaVelEqTolerance = Speed(tolerance)

    # A getter for the tolerance on deltaVel
    def getDeltaVelEqTolerance(self):
        """
        A getter for the tolerance on deltaVel
        """
        return self._deltaVelEqTolerance

    # The tolerance which will be used on position during an add operation on the table
    _positionEqTolerance = Length(0.0)

    def setPositionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on position
        """
        self._positionEqTolerance = Length(tolerance)

    # A getter for the tolerance on position
    def getPositionEqTolerance(self):
        """
        A getter for the tolerance on position
        """
        return self._positionEqTolerance

    # The tolerance which will be used on restFrequency during an add operation on the table
    _restFrequencyEqTolerance = Frequency(0.0)

    def setRestFrequencyEqTolerance(self, tolerance):
        """
        A setter for the tolerance on restFrequency
        """
        self._restFrequencyEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on restFrequency
    def getRestFrequencyEqTolerance(self):
        """
        A getter for the tolerance on restFrequency
        """
        return self._restFrequencyEqTolerance

    # The tolerance which will be used on sysVel during an add operation on the table
    _sysVelEqTolerance = Speed(0.0)

    def setSysVelEqTolerance(self, tolerance):
        """
        A setter for the tolerance on sysVel
        """
        self._sysVelEqTolerance = Speed(tolerance)

    # A getter for the tolerance on sysVel
    def getSysVelEqTolerance(self):
        """
        A getter for the tolerance on sysVel
        """
        return self._sysVelEqTolerance

    # The tolerance which will be used on rangeVel during an add operation on the table
    _rangeVelEqTolerance = Speed(0.0)

    def setRangeVelEqTolerance(self, tolerance):
        """
        A setter for the tolerance on rangeVel
        """
        self._rangeVelEqTolerance = Speed(tolerance)

    # A getter for the tolerance on rangeVel
    def getRangeVelEqTolerance(self):
        """
        A getter for the tolerance on rangeVel
        """
        return self._rangeVelEqTolerance

    # The tolerance which will be used on frequency during an add operation on the table
    _frequencyEqTolerance = Frequency(0.0)

    def setFrequencyEqTolerance(self, tolerance):
        """
        A setter for the tolerance on frequency
        """
        self._frequencyEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on frequency
    def getFrequencyEqTolerance(self):
        """
        A getter for the tolerance on frequency
        """
        return self._frequencyEqTolerance

    # The tolerance which will be used on frequencyInterval during an add operation on the table
    _frequencyIntervalEqTolerance = Frequency(0.0)

    def setFrequencyIntervalEqTolerance(self, tolerance):
        """
        A setter for the tolerance on frequencyInterval
        """
        self._frequencyIntervalEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on frequencyInterval
    def getFrequencyIntervalEqTolerance(self):
        """
        A getter for the tolerance on frequencyInterval
        """
        return self._frequencyIntervalEqTolerance

    # The tolerance which will be used on flux during an add operation on the table
    _fluxEqTolerance = Flux(0.0)

    def setFluxEqTolerance(self, tolerance):
        """
        A setter for the tolerance on flux
        """
        self._fluxEqTolerance = Flux(tolerance)

    # A getter for the tolerance on flux
    def getFluxEqTolerance(self):
        """
        A getter for the tolerance on flux
        """
        return self._fluxEqTolerance

    # The tolerance which will be used on fluxErr during an add operation on the table
    _fluxErrEqTolerance = Flux(0.0)

    def setFluxErrEqTolerance(self, tolerance):
        """
        A setter for the tolerance on fluxErr
        """
        self._fluxErrEqTolerance = Flux(tolerance)

    # A getter for the tolerance on fluxErr
    def getFluxErrEqTolerance(self):
        """
        A getter for the tolerance on fluxErr
        """
        return self._fluxErrEqTolerance

    # The tolerance which will be used on positionAngle during an add operation on the table
    _positionAngleEqTolerance = Angle(0.0)

    def setPositionAngleEqTolerance(self, tolerance):
        """
        A setter for the tolerance on positionAngle
        """
        self._positionAngleEqTolerance = Angle(tolerance)

    # A getter for the tolerance on positionAngle
    def getPositionAngleEqTolerance(self):
        """
        A getter for the tolerance on positionAngle
        """
        return self._positionAngleEqTolerance

    # The tolerance which will be used on positionAngleErr during an add operation on the table
    _positionAngleErrEqTolerance = Angle(0.0)

    def setPositionAngleErrEqTolerance(self, tolerance):
        """
        A setter for the tolerance on positionAngleErr
        """
        self._positionAngleErrEqTolerance = Angle(tolerance)

    # A getter for the tolerance on positionAngleErr
    def getPositionAngleErrEqTolerance(self):
        """
        A getter for the tolerance on positionAngleErr
        """
        return self._positionAngleErrEqTolerance

    # The tolerance which will be used on size during an add operation on the table
    _sizeEqTolerance = Angle(0.0)

    def setSizeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on size
        """
        self._sizeEqTolerance = Angle(tolerance)

    # A getter for the tolerance on size
    def getSizeEqTolerance(self):
        """
        A getter for the tolerance on size
        """
        return self._sizeEqTolerance

    # The tolerance which will be used on sizeErr during an add operation on the table
    _sizeErrEqTolerance = Angle(0.0)

    def setSizeErrEqTolerance(self, tolerance):
        """
        A setter for the tolerance on sizeErr
        """
        self._sizeErrEqTolerance = Angle(tolerance)

    # A getter for the tolerance on sizeErr
    def getSizeErrEqTolerance(self):
        """
        A getter for the tolerance on sizeErr
        """
        return self._sizeErrEqTolerance

    # The tolerance which will be used on dopplerVelocity during an add operation on the table
    _dopplerVelocityEqTolerance = Speed(0.0)

    def setDopplerVelocityEqTolerance(self, tolerance):
        """
        A setter for the tolerance on dopplerVelocity
        """
        self._dopplerVelocityEqTolerance = Speed(tolerance)

    # A getter for the tolerance on dopplerVelocity
    def getDopplerVelocityEqTolerance(self):
        """
        A getter for the tolerance on dopplerVelocity
        """
        return self._dopplerVelocityEqTolerance

    # The tolerance which will be used on parallax during an add operation on the table
    _parallaxEqTolerance = Angle(0.0)

    def setParallaxEqTolerance(self, tolerance):
        """
        A setter for the tolerance on parallax
        """
        self._parallaxEqTolerance = Angle(tolerance)

    # A getter for the tolerance on parallax
    def getParallaxEqTolerance(self):
        """
        A getter for the tolerance on parallax
        """
        return self._parallaxEqTolerance

    # Let's use a dictionary to implement the condition "one sourceName -> one sourceId"
    _name2id_dict = {}

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
        Insert a SourceRow in a list of SourceRow so that it's ordered by ascending start time.

        x is a SourceRow to be inserted.
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
                    raise DuplicateKey("DuplicateKey exception in ", "SourceTable")
            elif start.get() == rowlist[k1].timeInterval.getStart().get():
                if rowlist[k1].equalByRequiredValue(x):
                    # this row already exists at k1, nothing to insert or add, return that row
                    return rowlist[k1]
                else:
                    # the time matches, but the rest of the required parameters do not, duplicate keys
                    raise DuplicateKey("DuplicateKey exception in ", "SourceTable")
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
                raise DuplicateKey("DuplicateKey exception in ", "SourceTable")
        elif start.get() == rowlist[k1].timeInterval.getStart().get():
            if rowlist[k1].equalByRequiredValue(x):
                return rowlist[k1]
            else:
                # the time matches, but the rest of the required parameters do not, duplicate keys
                raise DuplicateKey("DuplicateKey exception in ", "SourceTable")

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
        Create a SourceTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
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
        # Get the start time of the row to be inserted.
        startTime = x.getTimeInterval().getStart()

        if not (x.getSourceName() in self._name2id_dict):
            nextId = len(self._name2id_dict)
            name2id_dict[x.getSourceName()] = nextId

        # print("Trying to add a new row with start time = "+startTime)

        insertionId = name2id_dict[x.getSourceName()]

        # Determine the entry in the context from the appropriates attributes.
        keystr = Key(x.getSpectralWindowId())

        # Determine the insertion index for the row x, possibly returning a row identical to x.
        if keystr in self._context:
            if len(self._context[keystr]) > insertionId:
                idList = context[keystr][insertionId]
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
                            # no idea why the java code doesn't throw a UniquenessViolationException here, but it's commented out
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
        Create a new SourceRow. The new row is not added to this table, but it does know about it.
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
                newrow.getTimeInterval(),
                newrow.getSpectralWindowId(),
                newrow.getCode(),
                newrow.getDirection(),
                newrow.getProperMotion(),
                newrow.getSourceName(),
            )
            is not None
        ):
            raise UniquenessViolationException(
                "Uniqueness violation exception in table SourceTable"
            )

        if (
            self.getRowByKey(
                newrow.getSourceId(),
                newrow.getTimeInterval(),
                newrow.getSpectralWindowId(),
            )
        ) is not None:
            raise DuplicateKey(
                "Duplicate key exception . ("
                + "sourceId="
                + newrow.getSourceId()
                + " "
                + "timeInterval="
                + newrow.getTimeInterval()
                + " "
                + "spectralWindowId="
                + newrow.getSpectralWindowId()
                + " "
                + ") in ",
                "SourceTable.",
            )

        thisKey = self.Key(newrow.getSpectralWindowId())

        i = newrow.getSourceId()

        # add this key to context if not there
        if thisKey not in self._context:
            self._context[thisKey] = []

        return self.insertByStartTime(newrow, self._context[thisKey])

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as a list of SourceRow
        """
        return self._privateRows

    def getRowByKey(self, sourceId, timeInterval, spectralWindowId):
        """
        Returns a SourceRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.
        """
        start = timeInterval.getStart()

        keystr = Key(spectralWindowId)
        if keystr in self._context:

            id = sourceId

            contextList = self._context[keystr]
            for aRow in contextList:
                if aRow.getTimeInterval().equals(timeInterval):
                    return aRow

        return None

    def getRowBySourceId(self, sourceId):
        """
        Returns a list of all rows whose key element sourceId
        is equal to the parameter sourceId, which is a int.
        return an array of SourceRow. A returned array of size 0 means that no row has been found.
        param sourceId int contains the value of
        the autoincrementable attribute that is looked up in the table.
        """
        result = []
        for thisValue in self._context.values():
            # each value is a list of lists, with one list for each sourceId
            if sourceId < len(thisValue):
                # append all of the sourceId rows to result
                result.extend(thisValue[sourceId])

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
        keystr = Key(spectralWindowId)
        if keystr in self._context:
            for thisList in self._context[keystr]:
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

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for Source (SourceTable.xsd).

        Returns a string containing the XML representation.
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
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of SourceTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "SourceTable":
            raise ConversionException(
                "XML is not from a the expected table", "SourceTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException("schemaVersion not found in XML", "SourceTable")
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
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "SourceTable") from None

                except ValueError as exc:
                    # TBD when this turns up via template
                    msg = (
                        "UniquenessViolationException in row in SourceTable : %s"
                        % str(exc)
                    )

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "SourceTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "SourceTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a SourceTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "SourceTable",
            )

        if os.path.exists(os.path.join(directory, "Source.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "Source.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the Source table", "SourceTable"
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
        with open(os.path.join(directory, "Source.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("Source.xml is empty", "SourceTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'Source.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'Source.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (Source)"
                % directory,
                "SourceTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for Source")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "Source.xml")
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
