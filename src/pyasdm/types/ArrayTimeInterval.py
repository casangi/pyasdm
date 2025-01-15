# ALMA - Atacama Large Millimeter Array
# (c) European Southern Observatory, 2024
# (c) Associated Universities Inc., 2024
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
# File ArrayTimeInterval.py
#

from .ArrayTime import ArrayTime
from .Interval import Interval

import pyasdm.utils

import math

# these needs to be somewhere that it can be set globally when the ASDM is loaded
# set using the static setters for these values

_readStartTimeDurationInXML = False
_readStartTimeDurationInBin = False


class ArrayTimeInterval:
    """
    Adapted from the c++ and java implementations.
    """

    _start = ArrayTime(0)
    _duration = Interval(0)

    # python doesn't have a maximum integer, but use this where it's needed here
    _max_duration = int(math.pow(2, 63)) - 1

    def __init__(self, start=None, duration=None):
        """
        Construct an ArrayTimeInterval.

        With no arguments, start and duration are set to 0.

        If start is an ArrayTimeInterval then this is the copy
        constructor and duration must be None.

        If start is an ArrayTime then duration can be unset (in which
        case the duration becomes the highest possible value given
        the start time. If duration is an Interval then both are used
        to set the ArrayTimeInterval. If duration is also an ArrayTime
        then duration is used as the end time of the interval. In that
        case if end (duration) is before start then the duration is
        set to 0 in the resuling ArrayTimeInterval.

        If start and duration are floats then start is a Modified Julian Date
        defining the start time and duration is the number of days defining
        the duration. If duration is None and start is a float then duration
        is set to the highest possible value given the start time.

        If start and duration are both integers then both are in nanoseconds
        giving the start and duration. If duration is not given and start is an
        integer then duration is set to the highest possible value given the
        start time.

        If start is a string then that string is parsed as if it was written
        to an XML field : two integers separated by a space giving the mid point
        and duration of the ArrayTimeInterval. It is an error to specify a duration
        in that case.
        """

        self._start = ArrayTime(0)
        self._duration = Interval(0)

        if start is None:
            if duration is not None:
                raise ("duration must be None when start is None")
            return

        if isinstance(start, ArrayTimeInterval):
            if duration is not None:
                raise ValueError(
                    "duration must be None if start is an ArrayTimeInterval"
                )
            # copy constructor
            self._start = ArrayTime(start.getStart())
            self._duration = Interval(start.getDuration())
            return

        # if start is a string then parse this as if it came from an XML output
        if isinstance(start, str):
            if duration is not None:
                raise ValueError("duration must be None if start is a string")
            vals = start.split()
            if len(vals) != 2:
                raise ValueError("start string does not contain exactly 2 values")
            try:
                l1 = int(vals[0])
                l2 = int(vals[1])

                # the Java code makes use of this, but it does not use that
                # when writing these values out, perhaps only old ASDMs use this
                if self.readStartTimeDurationInXML():
                    # use as is, start and duration
                    self._start = ArrayTime(l1)
                    self._duration = Interval(l2)
                else:
                    # midpoint and duration
                    self._start = ArrayTime(int(l1 - l2 / 2))
                    self._duration = Interval(l2)
            except Exception as exc:
                raise ValueError(
                    "there was a problem parsing the ArrayTimeInterval string. "
                    + str(exc)
                ) from None
            return

        if isinstance(start, ArrayTime):
            self._start = ArrayTime(start)
            if duration is None:
                # largest possible value given start
                self._duration = Interval(self._max_duration - self._start.get())
            elif isinstance(duration, Interval):
                self._duration = Interval(duration)
            elif isinstance(duration, ArrayTime):
                # duration is the end of the interval
                if duration_.ge(start_):
                    self._duration.set(duration.get() - self._start.get())
                else:
                    self._duration.set(0)
            else:
                raise ValueError(
                    "When start is an ArrayTime duration must be either None, Interval, or ArrayTime"
                )
        elif isinstance(start, float):
            self._start = ArrayTime(start)
            if duration is None:
                # largest possible value given start
                self._duration = Interval(self._max_duration - self._start.get())
            elif isinstance(duration, float):
                # duration is in days
                self._duration = Interval(int(ArrayTime.unitsInADay * duration))
            else:
                raise ValueError(
                    "When start is an float duration must be either None or float"
                )
        elif isinstance(start, int):
            self._start = ArrayTime(start)
            if duration is None:
                # largest possible value given start
                self._duration = Interval(self._max_duration - self._start.get())
            elif isinstance(duration, int):
                # duration in nanoseconds
                self._duration = Interval(duration)
            else:
                raise ValueError(
                    "When start is an int duration must be either None or int"
                )
        else:
            print("type of start : " + str(type(start)))
            print("start : " + str(start))
            raise ValueError(
                "unrecognized type for start, must be one of None, ArrayTimeInterval, ArrayTime, float or int"
            )

        # always make sure duration is less than the max value
        self._duration.set(min(self._duration.get(), self._max_duration))

    # Setters
    def setStart(self, start):
        """
        Set the start value of an ArrayTimeInterval.

        start can be an ArrayTime, a float (used as a Modified Julian Date) or an
        integer (used as nanoseconds).

        note the duration is left unchanged except that if necessary it's clipped to the highest possible
        value given the new start time.
        """
        if isinstance(start, ArrayTime):
            self._.start = ArrayTime(start)
        elif isinstance(float):
            self._start = ArrayTime(int(ArrayTime.unitsInADay * start))
        elif isinstance(int):
            self._start.set(start)
        else:
            raise ValueError("start must be an ArrayTime, float, or int")

        # make sure duration is less than the max value after setting start
        self._duration.set(
            min(self._duration.get(), (self._max_duration - self._start.get()))
        )

    def setDuration(self, duration):
        """
        Set the duration of an ArrayTimeInterval.

        duration man be an Interval defining the new duration, a float defining the duration in
        days, or an integer definining the duration in nanoseconds.

        note if necessary the duration is clipped to the highest possible value given the start time
        of this ArrayTimeInterval.
        """
        if isinstance(duration, Interval):
            self._duration.set(duration.get())
        elif isinstance(duration, float):
            self._duration.set(int(ArrayTime.unitsInADay * duration))
        elif isinstance(duration, int):
            self._duration.set(duration)

        # make sure duration is less than the max value using start
        self._duration.set(
            min(self._duration.get(), (self._max_duration - self._start.get()))
        )

    # Getters
    def getStart(self):
        """
        return the start time of this ArrayTimeInterval as an ArrayTime
        """
        return self._start

    def getMidPoint(self):
        """
        return the midpoint of this ArrayTimeInterval as an ArrayTIme.

        The midpoint is defind as start + duration / 2
        """
        return ArrayTime(int(self._start.get() + self._duration.get() / 2))

    def getStartInMJD(self):
        """
        return the start time of this ArrayTimeInterval as an MJD (float).
        """
        return self._start.getMJD()

    def getStartInNanoSeconds(self):
        """
        return the start time of this ArrayTimeInterval as a number of nanoseconds (int).
        """
        return self._start.get()

    def getDuration(self):
        """
        return the duration of this ArrayTimeInterval as an Interval.
        """
        return self._duration

    def getDurationInDays(self):
        """
        return the duration of this ArrayTimeInterval as a number of days (float).
        """
        return float(self._duration.get()) / ArrayTime.unitsInADay

    def getDurationInNanoSeconds(self):
        """
        return the duration of this ArrayTimeInterval as a number of nanoseconds (int)
        """
        return self._duration.get()

    # Checkers
    def equals(self, ati):
        """
        return True if and only if ati is an instance of ArrayTimeInterval and has the same
        start and duration values as this ArrayTimeInterval.
        """
        if not isinstance(ati, ArrayTimeInterval):
            return False
        return (ati.getStart().get() == self._start.get()) and (
            ati.getDuration().get() == self._duration.get()
        )

    def overlaps(self, ati):
        """
        Checks if this ArrayTimeInterval overlaps the one passed as a parameter.
        param ati the ArrayTimeInterval to be checked for overlapping.
        return True if and only if there is overlapping.
        """
        start1 = self._start.get()
        end1 = start1 + self._duration.get()

        start2 = ati.getStart().get()
        end2 = start2 + ati.getDuration().get()

        return (start2 <= start1 and end2 >= start1) or (
            start2 >= start1 and start2 <= end1
        )

    def containsArrayTimeInterval(self, ati):
        """
        Checks if this ArrayTimeInterval "contains" the one passed as a parameter.

        param ati the ArrayTimeInterval to be checked for the "contains" relationship.
        return True if and only if this contains ati.
        """
        start1 = self._start.get()
        end1 = start1 + self._duration.get()

        start2 = ati.getStart().get()
        end2 = start2 + ati.getDuration().get()

        return (start2 >= start1) and (end2 <= end1)

    def containsArrayTime(self, at):
        """
        Checks if this ArrayTimeInterval "contains" the ArrayTime passed as a parameter.

        param at the ArrayTime to be checked for the "contains" relationship.
        return True if and only if this contains at.
        """
        start1 = self._start.get()
        end1 = start1 + self._duration.get()

        atTime = at.get()
        return atTime >= start1 and atTime < end1

    def contains(self, atORati):
        """
        Checks if this ArrayTimeInterval "contains" either an ArrayTime or an
        ArrayTimeInterval.

        param atOrati is either an ArrayTime or an ArrayTimeInterval to be
        checked for the "contains" relationship.
        return True if and only if this contains at.
        """
        if isinstance(atORati, ArrayTime):
            return self.containsArrayTime(atORati)
        elif isinstance(atORati, ArrayTimeInterval):
            return self.containsArrayTimeInterval(atORati)
        else:
            raise ValueError(
                "contains argument must be an ArrayTime or an ArrayTimeInterval."
            )

    # Formatter
    def toString(self):
        result = "(start="
        result += str(self.getStart().toString())
        result += ",duration="
        result += str(self.getDuration().toString())
        result += ")"
        return result

    def toBin(self, eout):
        """
        Write the binary representation to an EndianOutput instance
        It successively writes midpoint and duration.
        """
        eout.writeLong(self.getMidPoint().get())
        eout.writeLong(self.getDuration().get())

    @staticmethod
    def listToBin(atiList, eos):
        """
        Write a list of ArrayTimeInterval to the EndianOutput.
        The list may have 1, 2 or 3 dimensions.
        """
        if not isinstance(atiList, list):
            raise ValueError("atiList is not a list")

        # this is used to determine the number of dimensions
        listDims = pyasdm.utils.getListDims(atiList)
        ndims = len(listDims)
        if ndims == 1:
            ArrayTimeInterval.listTo1DBin(atiList, eos)
        elif ndims == 2:
            ArrayTimeInterval.listTo2DBin(atiList, eos)
        elif ndims == 3:
            ArrayTimeInterval.listTo3DBin(atiList, eos)

        raise ValueError(
            "unsupport number of dimensions in atiList in ArrayTimeInterval.listToBin : "
            + str(ndims)
        )

    @staticmethod
    def listTo1DBin(atiList, eout):
        """
        Write the binary representation of a 1D list of ArrayTimeInterval instances to
        an EndianOutput instance.
        """
        if not isinstance(atiList, list):
            raise ValueError("atiList is not a list")

        # ndim is always written, even for 0-element lists
        eout.writeInt(len(atiList))

        # only check the first value
        if len(atiList) > 0 and not isinstance(atiList[0], ArrayTimeInterval):
            raise ValueError("atiList is not a list of ArrayTimeInterval")

        for thisAti in atiList:
            thisAti.toBin(eout)

    @staticmethod
    def listTo2DBin(atiList, eout):
        """
        Write the binary representation of a 2D list of ArrayTimeInterval instances to
        an EndianOutput instance.
        """
        if not isinstance(atiList, list):
            raise ValueError("atiList is not a list")

        ndim1 = len(atiList)
        ndim2 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(atiList[0], list):
                raise ValueError("atiList is not a 2D list")

            ndim2 = len(atiList[0])
            if ndim2 > 0 and not isinstance(atiList[0][0], ArrayTimeInterval):
                raise ValueError("atiList is not a 2D list of ArrayTimeInterval")

        # ndims are always written, even for 0-element lists
        eout.writeInt(ndim1)
        eout.writeInt(ndim2)

        for thisList in atiList:
            for thisAti in thisList:
                thisAti.toBin(eout)

    @staticmethod
    def listTo3DBin(atiList, eout):
        """
        Write the binary representation of a 3D list of ArrayTimeInterval instances to
        an EndianOutput instance.
        """
        if not isinstance(atiList, list):
            raise ValueError("atiList is not a list")

        ndim1 = len(atiList)
        ndim2 = 0
        ndim3 = 0

        if ndim1 > 0:
            # only check the first value in the outer list
            if not isinstance(atiList[0], list):
                raise ValueError("atiList is not a 3D list")

            ndim2 = len(atiList[0])

            if ndim2 > 0:
                # only check the first value in the middle list
                if not isinstance(atiList[0][0], list):
                    raise ValueError("atiList is a 3D list")

                ndim3 = len(atiList[0][0])
                if ndim3 > 0 and not isinstance(atiList[0][0][0], ArrayTimeInterval):
                    raise ValueError("atiList is not a 2D list of ArrayTimeInterval")

        # ndims are always written, even for 0-element lists
        eout.writeInt(ndim1)
        eout.writeInt(ndim2)
        eout.writeInt(ndim3)

        for thisList in atiList:
            for thisMidList in thisList:
                for thisAti in thisMidList:
                    thisAti.toBin(eout)

    @staticmethod
    def setReadStartTimeDurationInBin(torf):
        """
        Defines how the representation of an ArrayTimeInterval found in subsequent reads of
        a document containing table exported in binary must be interpreted. The interpretation depends on the value of the argument torf :
        torf == True means that it must be interpreted as (startTime, duration)
        torf == False means that it must be interpreted as (midPoint, duration)

        This sets a value found in this module outside of this class.

        param b a boolean value.
        """
        global _readStartTimeDurationInBin
        if not isinstance(torf, bool):
            raise ValueError("torf must be a bool")

        _readStartTimeDurationInBin = torf

    @staticmethod
    def readStartTimeDurationInBin():
        """
        Returns a boolean value whose meaning is defined as follows:
        True <=> the representation of ArrayTimeInterval object found in any binary table will be considered as (startTime, duration).
        False <=> the representation of ArrayTimeInterval object found in any binary table will be considered as (midPoint, duration).

        This returns a value found in this module outside of this class.
        """
        return _readStartTimeDurationInBin

    @staticmethod
    def setReadStartTimeDurationInXML(torf):
        """
        Defines how the representation of an ArrayTimeInterval found in subsequent reads of
        a document containing table exported in XML  must be interpreted. The interpretation depends on the value of the argument torf :
        torf == True means that it must be interpreted as (startTime, duration)
        torf == false means that it must be interpreted as (midPoint, duration)

        This sets a value found in this module outside of this class.

        param torf is a bool value.
        """
        global _readStartTimeDurationInXML
        if not isinstance(torf, bool):
            raise ValueError("torf must be a bool")

        _readStartTimeDurationInXML = torf

    @staticmethod
    def readStartTimeDurationInXML():
        """
        Returns a boolean value whose meaning is defined as follows:
        True <=> the representation of ArrayTimeInterval object found in any binary table will be considered as (startTime, duration).
        False <=> the representation of ArrayTimeInterval object found in any binary table will be considered as (midPoint, duration).

        This returns a value found in this module outside of this class.
        """
        return _readStartTimeDurationInXML

    @staticmethod
    def fromBin(eis):
        """
        Read the binary representation of an ArrayTimeInterval
        from an EndianInput instance and use the read values to set an
        ArrayTimeInterval.

        return an ArrayTimeInterval

        Remember that it reads two long integers (64 bits). The first one is considered as the midpoint of the interval
        and the second one is the duration. If readStartTimeDurationInBin() is True then the first integer
        is interpreted as the start time, not the midpoint, of the interval.0

        """
        l1 = eis.readLong()
        l2 = eis.readLong()
        if ArrayTimeInterval.readStartTimeDurationInBin():
            return ArrayTimeInterval(l1, l2)
        else:
            # ensure that the division here results in an integer
            return ArrayTimeInterval(int((l1 - l2) / 2), l2)

    # static method
    def from1DBin(ein):
        """
        Read the binary representations of a 1D array of ArrayTimeInterval
        from an EndianInput instance to set a 1D list of  ArrayTimeInterval.
        return a 1D list of ArrayTimeInterval
        """
        ndim = ein.readInt()
        result = []
        for i in range(ndim):
            result.append(ArrayTimeInterval.fromBin(ein))

        return result

    # static method
    def from2DBin(ein):
        """
        Read the binary representations of a 2D array of ArrayTimeInterval
        from an EndianInput instance to set a 2D list of  ArrayTimeInterval.
        return a 1D list of ArrayTimeInterval
        """
        ndim1 = ein.readInt()
        ndim2 = ein.readInt()
        result = []
        for i in range(ndim1):
            innerList = []
            for j in range(ndim2):
                innerList.append(ArrayTimeInterval.fromBin(ein))
            result.append(innerList)

        return result

    # static method
    def from3DBin(ein):
        """
        Read the binary representations of a 3D array of ArrayTimeInterval
        from an EndianInput instance to set a 3D list of  ArrayTimeInterval.
        return a 3D list of ArrayTimeInterval
        """
        ndim1 = ein.readInt()
        ndim2 = ein.readInt()
        ndim3 = ein.readInt()
        result = []
        for i in range(ndim1):
            middleList = []
            for j in range(ndim2):
                innerList = []
                for k in range(ndim3):
                    innerList.append(ArrayTimeInterval.fromBin(ein))
                middleList.append(innerList)
            result.append(middleList)

        return result

    @staticmethod
    def getInstance(stringList):
        """
        Retrieve two values from a list of strings and convert that to an ArrayTimeInterval

        This is used when parsing ArrayTimeInterval lists from an XML representation to
        eventually construct a list of ArrayTimeInterval instances. The values are expected
        to be integers representing nanoseconds with the first value being either the
        midpoint or start of an interval and the second value being the duration.
        readStartTimeDurationInXML() is used to determine how that first value is interepreted.

        Returns a tuple of (ArrayTimeInterval, stringList) where ArrayTimeInterval is the
        new ArrayTimeInterval created by this call and stringList is the remaining,
        unused, part of stringList after removing the first element.
        """
        if not isinstance(stringList, list):
            raise ValueError("stringList is not a list")

        # this will raise an error if there aren't enough elements on stringList
        intVal1 = int(stringList[0])
        intVal2 = int(stringList[1])

        if not ArrayTimeInterval.readStartTimeDurationInXML():
            # it's the midpoint, correct it to the start time, it must still be an integer
            intVal1 = intVal1 - int(intVal2 / 2)

        return (ArrayTimeInterval(intVal1, intVal2), stringList[2:])
