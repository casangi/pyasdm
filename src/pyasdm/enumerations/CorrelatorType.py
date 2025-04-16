

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
# /////////////////////////////////////////////////////////////////
# // WARNING!  DO NOT MODIFY THIS FILE!                          //
# //  ---------------------------------------------------------  //
# // | This is generated code!  Do not modify this file.       | //
# // | Any changes will be lost when the file is re-generated. | //
# //  ---------------------------------------------------------  //
# /////////////////////////////////////////////////////////////////
#
# File CorrelatorType.py

# to keep track of the attributes added to this class for each value of this enumeration

_correlatorTypeDict = {}

# the possible enumerations

_FX = 0 # identifies a digital correlator of type FX.

_XF = 1 # identifies a digital correlator of type XF.

_FXF = 2 # identifies a correlator of type FXF.


# their names in a dictionary
_correlatorTypeNames = {}

_correlatorTypeNames[_FX] = 'FX';

_correlatorTypeNames[_XF] = 'XF';

_correlatorTypeNames[_FXF] = 'FXF';


class CorrelatorType:
    """
    A class for the CorrelatorType enumeration.
    """
    
    # The value of this CorrelatorType, one of the possible enumerations.
    _value = None
    
    # its name
    _name = None
    
    def __init__(self, correlatorType):
        # construct a CorrelatorType from an integer, a string, or another CorrelatorType
        # if correlatorType is a string, convert it to an instance of this class using literal
        if isinstance(correlatorType, CorrelatorType):
            # copy constructor
            self._value = correlatorType.getValue()
            self._name = correlatorType.getName()
        elif isinstance(correlatorType, str):
            # convert it to an instance of this class using literal
            thisEnum = CorrelatorType.literal(correlatorType)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if correlatorType not in _correlatorTypeNames:
                raise ValueError("unrecognized CorrelatorType")
            self._value = correlatorType
            self._name = _correlatorTypeNames[correlatorType]
            if self._name not in _correlatorTypeDict:
                # add this CorrelatorType as an attribute to this class using its name
                setattr(CorrelatorType, self._name, self)
                _correlatorTypeDict[self._name] = getattr(CorrelatorType, self._name)
                
    def getValue(self):
        return self._value
        
    def getName(self):
        return self._name
        
    # by convention with the other languages, these are all static methods
    @staticmethod
    def revision():
        """
        revision as a string.
        """
        return "-1"
        
    @staticmethod
    def version():
        """
        the major version number as an int.
        """
        return 1
        
    @staticmethod
    def size():
        """
        the number of known enumerators in CorrelatorType
        """
        return len(_correlatorTypeNames)
        
    @staticmethod
    def name(correlatorType):
        """
        Returns the string form of the CorrelatorType
        """
        return correlatorType.getName()
        
    @staticmethod
    def toString(correlatorType):
        """
        Equivalent to the name method
        """     	
        return CorrelatorType.name(correlatorType)
        
    @staticmethod
    def names():
        """
        Return the list of all known CorrelatorType enumeration names
        """
        return list(_correlatorTypeNames.values())
       
    @staticmethod
    def newCorrelatorType(name):
        """
        Equivalent to the literal method
        """
        return CorrelatorType.literal(name)
       
    @staticmethod
    def literal(name):
        """
        Return the CorrelatorType enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(CorrelatorType, name):
            raise ValueError("Unrecognized CorrelatorType name")
        return CorrelatorType(getattr(CorrelatorType, name).getValue())
       
    @staticmethod
    def from_int(i):
        """
        Return a CorrelatorType from an integration matching an enumeration.
        """
        return CorrelatorType(i)
       

FX = CorrelatorType(_FX)

XF = CorrelatorType(_XF)

FXF = CorrelatorType(_FXF)

