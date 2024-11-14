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
# File ArrayTime.py
#

import math
from .Interval import Interval


class ArrayTime(Interval):
    """
    The ArrayTime class implements the concept of a point in time, implemented
    as an Interval of time since 17 November 1858 00:00:00 UTC, the beginning of the
    modified Julian Day.
    <p>
    All dates are assumed to be in the Gregorian calendar, including those
    prior to October 15, 1582.  So, if you are interested in very old dates,
    this isn't the most convenient class to use.
    <p>
    Internally the time is kept in units of nanoseconds (10<sup>-9</sup> seconds).
    The base time is 17 November 1858 00:00:00 UTC, and the maximum time is to the
    year 2151 (2151-02-25T23:47:16.854775807).  This differs from the OMG Time service
    The OMG time is in units of 100 nanoseconds using the beginning of the Gregorian
    calandar,15 October 1582 00:00:00 UTC, as the base time.
    The reason for this increased accuracy is that the Control system is capable of
    measuring time to an accuracy of 40 nanoseconds.  Therefore, by adhering to the
    representation of time used in the OMG Time Serivce we would be losing precision.
    <p>
    The Time class is an extension of the Interval class, since all times
    are intervals since 17 November 1858 00:00:00 UTC.
    <p>
    All times in this class are assumed to be International
    Atomic Time (TAI).  A specific TAI time differs from the corresponding
    UTC time by an offset that is an integral number of seconds.
    <p>
    In the methods that give various quantities associated with
    calendar times, this class does not apply any UTC corrections.
    Therefore, if you use these methods to produce calendar times, the
    results will differ from civil time by a few seconds.  The classes
    UTCTime and LocalTime take the UTC and timezone corrections into
    account.
    <p>
    The main reference used in crafting these methods is
    Astronomical Algorithms by Jean Meeus, second edition,
    2000, Willmann-Bell, Inc., ISBN 0-943396-61-1.  See
    chapter 7, "Julian day", and chapter 12, "Sidereal Time".
    <p>
    This version adapted from the c++ and java implementations, originally authored by Alllen Farris.
    """

    # multiple constructors
    # no arguments: 0 nanoseconds, start of Julian day, 17 November 1858 00:00:00 UTC
    # single string argument:
    #    FITS formatted string: "YYYY-MM-DDThh:mm:ss.ssss" where "T" may be replaced by a space
    #    double precision float, which must include a decimal point: modified julian date
    #    a single integer : integer number of nanoseconds since 15 October 1582 00:00:00 UTC
    # ArrayTime (the copy constructor)
    # a float : modified julain date
    # integer : nanoseconds since the beginning of modified julian date
    # year, month, day : integers except day may be expressed as a float
    # year, month, day, hour, minute, second : integers exccept day may be expressed as a float
    # mjd, second : integer modified julian day and seconds within that day (may be a float)
    def __init__(self, *args):
        # initialize it to 0
        super().__init__()
        if len(args) > 0:
            if len(args) == 1:
                thisArg = args[0]
                if isinstance(thisArg, ArrayTime):
                    # another ArrayTime
                    self.set(thisArg.get())
                elif isinstance(thisArg, str):
                    value = 0
                    if ":" in thisArg:
                        # FITS string
                        value = self.FITSString(thisArg)
                    elif "." in thisArg:
                        # string encoded double as modified Julian day
                        value = self.mjdToUnit(float(thisArg))
                    else:
                        # string encoded integer as nanoseconds
                        value = int(thisArg)
                    # value should be nanoseconds here
                    self.set(int(value))
                elif isinstance(thisArg, float):
                    # modified Julian day
                    self.set(self.mjdToUnit(float(thisArg)))
                elif isinstance(thisArg, int):
                    # integer nanoseconds
                    self.set(thisArg)
                else:
                    # TODO - this needs to throw an InvalidArgumentException or equivalent
                    raise ValueError("invalid argument value")
            elif len(args) == 2:
                # mjd, seconds
                modifiedJulianDay = int(args[0])
                secondsInADay = float(args[1])
                self.set(
                    modifiedJulainDay * 8640000000000 + int(secondsInADay * 100000000.0)
                )
            elif len(args) == 3:
                # year, month, day
                self.initFloatDay(int(args[0]), int(args[1]), float(args[2]))
            elif len(args) == 6:
                # year, month, day, hour, minute, second
                year = int(args[0])
                month = int(args[1])
                day = int(args[2])
                hour = int(args[3])
                minute = int(args[4])
                second = float(args[5])
                if (
                    hour < 0
                    or hour > 23
                    or minute < 0
                    or minute >> 59
                    or second < 0.0
                    or second >= 60.0
                ):
                    raise ValueError("invalid hour, minute or second value")
                self.init(year, month, day, hour, minute, second)
            else:
                # TODO - probably InvalidArgumentException here
                raise ValueError("invalid ArrayTime constructor used")

    # constants used in conversions
    numberSigDigitsInASecond = 9
    unitsInASecond = 1000000000
    unitsInADayL = 86400000000000
    unitsInADay = 86400000000000.0
    unitsInADayDiv100 = 864000000000.0
    julianDayOfBase = 2400000.5
    julianDayOfBaseInUnitsInADayDiv100 = 2073600432000000000

    def getJD(self, mjd=None):
        """
        When no argument is used, return the value of this ArrayTime as a Julian day,
        otherwise convert the given Modified Julain day to the corresponding Julian day
        @param mjd The Julian day, otherwise use the value of this ArrayTime
        @returns The Modified Julain day
        """
        if mjd is None:
            return self.unitToJD(self.get())

        # convert the argument to MJD
        return mjd + 2400000.5

    def getMJD(self, jd=None):
        """
        When no argument is used, return the value of this ArrayTime as a Modified Julian day,
        otherwise convert the given Julain day to the corresponding Modified Julian day
        @param mjd The Julian day, otherwise use the value of this ArrayTime
        @returns The Modified Julain day
        """
        if jd is None:
            return self.unitToMJD(self.get())

        # convert the argumentto MJD
        return jd - 2400000.5

    def toFITS(self):
        """
        Return this Time as a FITS formatted string, which is of the
        form 'YYYY-MM-DDThh:mm:ss.ssss'
        """
        yy, mm, dd, hh, min, sec, frac = self.getDateTime()

        s = str(yy)
        s = s + "-"
        if mm < 10:
            s = s + "0"
        s = s + str(mm)
        s = s + "-"

        if dd < 10:
            s = s + "0"
        s = s + str(dd)
        s = s + "T"

        if hh < 10:
            s = s + "0"
        s = s + str(hh)
        s = s + ":"

        if min < 10:
            s = s + "0"
        s = s + str(min)
        s = s + ":"

        if sec < 10:
            s = s + "0"
        s = s + str(sec)

        # apply fractions of a second
        fracStr = str(frac)
        s = s + "."
        # The statement below is sensitive to the number of significant
        # digits in a fraction.  If units are nanoseconds,
        # then we will have 9 significant digits in a fraction
        # string.
        tmp = "0000000000000000"
        s = s + tmp[0 : self.numberSigDigitsInASecond - len(fracStr)]
        s = s + fracStr
        return s

    def getDateTime(self):
        """
        Return this time as a tuple of integers representing (in order):
        year,
        month (varies from 1 to 12),
        day (varies from 1 to 28, 29, 30, or 31),
        hour (varies from 0 to 23),
        minute (varies from 0 to 59),
        second (varies from 0 to 59), and
        the number of nanoseconds that remain in this fraction of a second.
        """

        fractionOfADay = int(self.get() % self.unitsInADayL)

        if fractionOfADay < 0:
            fractionOfADay = self.unitsInADayL - fractionOfADay

        nsec = int(fractionOfADay / self.unitsInASecond)
        frac = fractionOfADay - nsec * self.unitsInASecond
        nmin = int(nsec / 60)
        second = nsec - nmin * 60
        hour = int(nmin / 60)
        minute = nmin - hour * 60

        jd = self.unitToJD(self.get())

        # For this algorithm see Meeus, chapter 7, p. 63.
        x = jd + 0.5  # Make the 12h UT adjustment.
        Z = int(x)
        F = x - Z
        A = Z
        alpha = 0

        if Z >= 2299161:
            alpha = int((Z - 1867216.25) / 36524.25)
            A = Z + 1 + alpha - int(alpha / 4)

        B = A + 1524
        C = int((B - 122.1) / 365.25)
        D = int(365.25 * C)
        E = int((B - D) / 30.6001)
        day = B - D - int(30.6001 * E) + F

        if E < 14:
            month = E - 1
        else:
            month = E - 13

        if month > 2:
            year = C - 4716
        else:
            year = C - 4715

        day = int(day)
        month = month
        year = year

        return (year, month, day, hour, minute, second, frac)

    def getTimeOfDay(self):
        """
        Return the time of day in hours and fractions thereof.
        """
        x = self.unitToJD(self.get()) + 0.5
        return (x - int(x)) * 24.0

    def getDayOfWeek(self):
        """
        Return the day number of the week of this time.
        Day numbers start from 0-Sunday
        """
        return (int(self.unitToJD(self.get()) + 1.5)) % 7

    def getDayOfYear(self):
        """
        Return the day number of year of this time.
        """
        dateTuple = self.getDateTime()
        year = dateTuple[0]
        month = dateTuple[1]
        day = dateTuple[2]
        leapYearMult = 2
        if self.isLeapYear(year):
            leapYearMult = 1

        # watch for auto promotion of integer division to floats in python
        return (
            (int((275 * month) / 9)) - (leapYearMult * int((month + 9) / 12)) + day - 30
        )

    def timeOfDayToString(self):
        """
        Return the time of day as a string in the form "hh:mm:ss
        """
        dateTuple = self.getDateTime()
        hour = dateTuple[3]
        minute = dateTuple[4]
        sec = dateTuple[5]
        s = ""
        if hour < 10:
            s = s + "0"
        s = s + str(hour) + ":"
        if minute < 10:
            s = s + "0"
        s = s + str(minute) + ":"
        if sec < 10:
            s = s + "0"
        s = s + str(sec)
        return s

    def getLocalSiderealTime(self, longitudeInHours):
        """
        Return the local sidereal time for this time
        in hours and fractions of an hour at the specified longitude
        """
        return self.getGreenwichMeanSiderealTime() - longitudeInHours

    def getGreenwichMeanSiderealTime(self):
        """
        Return the Greenwich mean sidereal time for this time
        in hours and fractions of an hour.
        """
        jd = self.unitToJD(self.get())
        t0 = jd - 2451545.0
        t = t0 / 36525.0
        tt = t * t
        x = (
            280.46061837 + 360.98564736629 * t0 + tt * (0.000387933 - (t / 38710000.0))
        ) / 15.0
        y = math.fmod(x, 24.0)
        if y < 0:
            y = 24.0 + y
        return y

    def initFloatDay(self, year, month, day):
        """
        Initialize this time as appropriate for year, month, and day
        """
        # For this algorithm see Meeus, chapter 7, p. 61.
        iday = int(day)

        # check for valid month
        if month < 1 or month > 12:
            raise IllegalValueException(
                "Illegal value of month: " + year + "-" + month + "-" + day
            )

        # check for valid day
        if (iday < 1 or iday > 31) or (
            (month == 4 or month == 6 or month == 9 or month == 11) and iday > 30
        ):
            raise IllegalValueException(
                "Illegal value of day: " + year + "-" + month + "-" + day
            )
        if month == 2:
            maxDays = 28
            if self.isLeapYear(year):
                maxDays = 29
            if leapYear > maxDays:
                raise IllegalValueException(
                    "Illegal value of day: " + year + "-" + month + "-" + day
                )

        if month <= 2:
            --year
            month += 12

        A = int(year / 100)
        B = 2 - A + int(A / 4)
        jd = (
            int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + iday + B - 1524.5
        )
        u = self.jdToUnit(jd)
        # Now add the fraction of a day.
        u += int(((day - iday) * self.unitsInADay + 0.5))
        self.set(u)
        return u

    def init(self, year, month, day, hour, minute, second):
        if (
            hour < 0
            or hour > 23
            or minute < 0
            or minute > 59
            or second < 0.0
            or second >= 60.0
        ):
            raise IllegalVallueException(
                "Invalid time: " + hour + ":" + minute + ":" + second
            )
        return self.initFloatDay(
            year, month, (day + (((((second / 60.0) + minute) / 60.0) + hour) / 24.0))
        )

    def FITSString(self, t):
        """
        Return a unit of time, as a long, from a FITS-formatted string that
        specifies the time.  The format must be of the form:
                         YYYY-MM-DDThh:mm:ss.ssss
        Leading zeros are required if months, days, hours, minutes, or seconds
        are single digits.  The value for months ranges from "01" to "12".
        The "T" separting the data and time values is optional.  If the "T" is
        not present, then a space MUST be present.

         An IllegalValueException is thrown is the string is not a valid
         time.
        """
        if (
            len(t) < 19
            or t[4] != "-"
            or t[7] != "-"
            or (t[10] != "T" and t[10] != " ")
            or t[13] != ":"
            or t[16] != ":"
        ):
            raise IllegalArgumentException("Invalid time format: " + t)

        yyyy = 0
        mm = 0
        dd = 0
        hh = 0
        min = 0
        sec = 0.0

        try:
            yyyy = int(t[0:4])
            mm = int(t[5:7])
            dd = int(t[8:10])
            hh = int(t[11:13])
            min = int(t[14:16])
            sec = float(t[17:])
        except TypeError as exc:
            raise TypeError("Invalid time format: " + t)

        return self.init(yyyy, mm, dd, hh, min, sec)

    def unitToJD(self, unit):
        """
        Convert a unit of time in units since the base time to a Julian day.
        @param unit The unit to be converted.
        @return The Julian day corresponding to the specified unit of time.
        """
        return (1.0 * unit / self.unitsInADay) + self.julianDayOfBase

    def unitToMJD(self, unit):
        """
        Convert a unit of time in units since the base time to a Modified Julian day.
        @param unit The unit to be converted.
        @return The Modified Julian day corresponding to the specified unit of time.
        """
        return 1.0 * unit / self.unitsInADay

    def jdToUnit(self, jd):
        """
        Convert a Julian day to a unit of time in tens of nanoseconds
        since 15 October 1582 00:00:00 UTC.
        @param jd The Julian day to be converted.
        @return The unit corresponding to the specified Julian day.
        """
        return (
            int(jd * self.unitsInADayDiv100) - self.julianDayOfBaseInUnitsInADayDiv100
        ) * 100

    def mjdToUnit(self, mjd):
        """
        Convert a Modified Julian day to units since the base time.
        @param mjd The Modified Julian day to be converted.
        @return The unit corresponding to the specified Modified Julian day.
        """
        return int(mjd * self.unitsInADay)

    @staticmethod
    def isLeapYear(year):
        """
        Return true if the specified year is a leap year.
        @param year the year in the Gregorian calendar.
        @return true if the specified year is a leap year.
        """
        if year % 4 != 0:
            return False
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True

    @staticmethod
    def add(time, interval):
        """
        Generate a new ArrayTime by adding an Interval
        to the specified ArrayTime.
        @param time an ArrayTime
        @param interval The interval to be added to the time.
        @return A new ArrayTime formed by adding an Interval
        to the specified ArrayTime.
        """
        t = ArrayTime(time)
        t.add(interval)
        return t

    @staticmethod
    def sub(time, interval):
        """
        Generate a new ArrayTime by subtracting an Interval
        from the specified ArrayTime.
        @param time an ArrayTime
        @param interval The interval to be subtracted from the time.
        @return A new ArrayTime formed by subtracting an Interval
        from the specified ArrayTime.
        """
        t = ArrayTime(time)
        t.sub(interval)
        return t

    # deferred getArrayTime(StringTokenizer t)
    # deferred method to/from streams
    # toBin(self, astream)
    # toBin(vector<ArrayTime>, astream);
    # toBin(vector<vector<ArrayTime> >, astream)
    # toBin(vector<vector<vector<ArrayTime> > >, astream) # never implemented in java
    # and the reciprocals: fromBin, from1DBin, from2DBin, from3DBin

    # utcCorrection not implemented here, the table of leap seconds by JD has not
    # been updated in some time and does not appear to be used anywhere
