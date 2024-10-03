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
# File Parser.py

# this will eventually be generated code

class Parser:

    _pstr = "" # the string being parsed
    _pos = 0   # the current position in the string
    _beg = 0   # the beginning and end of a fragment
    _end = 0   #    in the string

    def __init__(self, s):
        # s must be a string
        if not isinstance(s,str):
            raise ValueError("s must be a string")
        self._pstr = s

    # is s in the string being parsed?
    def isStr(self, s):
        return (self._pstr.find(s) >= 0)

    # Get the portion of the string bounded by s1 and s2, inclusive.
    # The first matching index of s1 and s2 are used
    # Subsequenty uses search string at positions after this element
    # returns None if none found
    def getElement(self, s1, s2):
        self._beg = self._pstr.find(s1, self._pos)
        if (self._beg < 0):
            return(None)

        self._end = self._pstr.find(s2, self._beg+len(s1))
        if (self._end) < 0:
            return(None)
        self._pos = self._end + len(s2)
        return (self._pstr[self._beg:self._pos])

    # Get the portion of the string bounded by s1 and s2, exclusive
    # uses getElement and then the resulting internals to return the content
    # whitespace is removed from the start and end of the content
    def getElementContent(self, s1, s2):
        selement = self.getElement(s1,s2)
        if selement is None:
            return(None)
        return (self._pstr[(self._beg+len(s1)):self._end].strip())

    
