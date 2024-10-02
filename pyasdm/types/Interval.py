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
# File Interval.py

# this file was adapted from the c++ implementation
# original author, Allen Farris
# IDL (ACS) dependencies are not implemented here



"""
   The Interval class implements a concept of an interval
   of time in units of nanoseconds.
"""
class Interval:

    # the interval, in nanoseconds, this should be an integer, it should not be used directly
    _value = 0;
        
    # intended for inernal use, used throughout this class
    # if value is an instance of Interval, returns value.value
    # if value is an integer, returns value
    # if value is a string, returns int(value)
    # else throws an exception  ** needs an exception here, is ValueError appropriate?
    @staticmethod
    def _getIntervalValue(value):
        if value is None:
            return 0;
        
        if isinstance(value,Interval):
            return value.value;
        elif type(value) is int:
            return value;
        elif type(value) is str:
            return int(value);
        else:
            raise ValueError("value is not an Interval, int, or str for _getIntervalValue")
        # it should never get here
        return None
        
    # create an interval of time, defaults to 0
    #
    # The value is the length of the interval, in nanoseconds
    #
    def __init__ (self, value=None):
        self.value = self._getIntervalValue(value);

    # the operators, they all work with either Interval, int, or str values

    # these operators change the value of this Interval using the argument and return this Interval
    
    # +=
    def __iadd__(self, other):
        self.value += self._getIntervalValue(other);
        return(self);

    # -=
    def __isub__(self, other):
        self.value -= self._getIntervalValue(other);
        return(self);

    # *=
    def __imul__(self, other):
        self.value *= self._getIntervalValue(other);
        return(self);

     # /=
    def __idoiv__(self, other):
        # note: this may lose precision because of the need for value and other to both be integers
        self.value /= self._getIntervalValue(other);
        # this may be unnecessary
        self.value = int(self.value)
        return(self);

    # binary operators, these return a new Interval and do not change self
    # +
    def __add__(self,other):
        return(Interval(self.value + self._getIntervalValue(other)));
    # =
    def __sub__(self,other):
        return(Interval(self.value - self._getIntervalValue(other)));
    # *
    def __mul__(self,other):
        return(Interval(self.value * self._getIntervalValue(other)));
    # /
    def __truediv__(self,other):
        # note - this may lose precision because of the need for this to be an integer
        return(Interval(int(self.value / self._getIntervalValue(other))));

    # comparison operators
    def __lt__(self,other):
        return(self.value < self._getIntervalValue(other));
    def __gt__(self,other):
        return(self.value > self._getIntervalValue(other));
    def __le__(self,other):
        return(self.value <= self._getIntervalValue(other));
    def __ge__(self,other):
        return(self.value <= self._getIntervalValue(other));
    def __eq__(self,other):
        return(self.value == self._getIntervalValue(other));
    def __ne__(self,other):
        return(self.value != self._getIntervalValue(other));

    # unary operators, they return a new Interval and do not change this Interval
    def __neg__(self):
        return(Interval(-self.value));
    def __pos__(self):
        return(Interval(self.value))

    # Return True if and only if other is an Interval and its value is equal to this interval
    def equals(self, other):
        if (not isinstance(other, Interval)):
            return False
        return(self.value == other.value);

    
    def isZero(self):
        return (self.value == 0);

    def toString(self):
        return (str(self.value));

    # equivalent to toString
    def string(self):
        return(self.toString());

    # get the value, always nanoseconds
    def get(self):
        return(self.value);

    # set the value, always nanoseconds
    def set(self, value):
        self.value = int(value);

    # the units are always "nanosec", derived classes may change or add to that
    def unit(self):
        return("nanosec");

    # set the value from a string, throws a ValueError when string isn't properly formatted
    def fromString(self, s):
        self.value = int(s);

    def copy(self):
        tmp = Interval();
        tmp.value = self.value;
        return(tmp);
