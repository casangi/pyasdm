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

import math


class ArrayTimeInterval:
    """
    Adapted from the c++ and java implementations.
    """

    _start = ArrayTime(0)
    _duration = Interval(0)

    _readStartTimeDurationInXML_ = False
    _readStartTimeDurationInBin_ = False

    # python doesn't have a maximum integer, but use this where it's needed here
    _max_duration = int(math.pow(2, 63)) - 1

    def __init(self, start=None, duration=None):
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
            self._duration = Interval(duration.getDuration())

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
            sel._start = ArrayTime(start)
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
            raise ValueError(
                "unrecognized type for start, must be one of None, ArrayTimeInterval, ArrayTime, float or int"
            )

        # always make sure duration is less than the max value
        self._duration.set(math.min(self._duration.get(), self._max_duration))

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
            math.min(self._duration.get(), (self._max_duration - self._start.get()))
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
            math.min(self._duration.get(), (self._max_duration - self._start.get()))
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

    def contains(self, ati):
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

    def contains(self, at):
        """
        Checks if this ArrayTimeInterval "contains" the ArrayTime passed as a parameter.

        param at the ArrayTime to be checked for the "contains" relationship.
        return True if and only if this contains at.
        """
        start1 = self._start.get()
        end1 = start1 + self._duration.get()

        atTime = at.get()
        return atTime >= start1 and atTime < end1

    # Formatter
    def toString(self):
        result = "(start="
        result += str(self.getStart())
        result += ",duration="
        result += str(self.getDuration())
        result += ")"
        return result

    def toBin(self):
        """
        Write the binary representation
        It successively writes midpoint and duration.

        There needs to be a version that writes an list of ArrayTimeInterval out as binary.
        """
        raise RuntimeError("ArrayTimeInterval.toBin not yet implemented")

    def setReadStartTimeDurationInBin(self, torf):
        """
        Defines how the representation of an ArrayTimeInterval found in subsequent reads of
        a document containing table exported in binary must be interpreted. The interpretation depends on the value of the argument torf :
        torf == True means that it must be interpreted as (startTime, duration)
        torf == False means that it must be interpreted as (midPoint, duration)

        param b a boolean value.
        """
        if not isinstance(torf, bool):
            raise ValueError("torf must be a bool")

        self._readStartTimeDurationInBin = torf

    def readStartTimeDurationInBin(self):
        """
        Returns a boolean value whose meaning is defined as follows:
        True <=> the representation of ArrayTimeInterval object found in any binary table will be considered as (startTime, duration).
        False <=> the representation of ArrayTimeInterval object found in any binary table will be considered as (midPoint, duration).
        """
        return self._readStartTimeDurationInBin

    def setReadStartTimeDurationInXML(self, torf):
        """
        Defines how the representation of an ArrayTimeInterval found in subsequent reads of
        a document containing table exported in XML  must be interpreted. The interpretation depends on the value of the argument torf :
        torf == True means that it must be interpreted as (startTime, duration)
        torf == false means that it must be interpreted as (midPoint, duration)

        param torf is a bool value.
        """
        self._readStartTimeDurationInXML = torf

    def readStartTimeDurationInXML(self):
        """
        Returns a boolean value whose meaning is defined as follows:
        True <=> the representation of ArrayTimeInterval object found in any binary table will be considered as (startTime, duration).
        False <=> the representation of ArrayTimeInterval object found in any binary table will be considered as (midPoint, duration).
        """
        return self.readStartTimeDurationInXML

        def fromBin(self):
            """
            Read the binary representation of an ArrayTimeInterval
            and use the read value to set an  ArrayTimeInterval.

            return an ArrayTimeInterval

            Remember that it reads two long integers (64 bits). The first one is considered as the midpoint of the interval
            and the second one is the duration.

            """
            raise RuntimeError("fromBin is not yet implemented")

        def from1DBin(self):
            """
            Read the binary representation of a 1D array of  ArrayTimeInterval
            and use the read value to set a 1D list of  ArrayTimeInterval.
            return a 1D list of ArrayTimeInterval
            """
            raise RuntimeError("from1DBin is not yet implemented")
