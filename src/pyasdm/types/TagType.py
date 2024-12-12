
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
# Warning!
#  -------------------------------------------------------------------- 
# | This is generated code!  Do not modify this file.                  |
# | If you do, all changes will be lost when the file is re-generated. |
#  --------------------------------------------------------------------
#
# File TagType.py
#

_tagTypeDict = {}

class TagType:
    """
    A class to represent the type of a Tag, i.e. the ASDM class a Tag refers to.
    The known types from the model are all available as attributes of this class.
    e.g. TagType.DataDescription is a TagType with a value of "DataDescription"
    """
    
    # the value of this TagType
    _name = None

    def __init__(self,name):
        """
        Initialize the TagType with name, which must be a string.
        If name is not already known, an attribute using that name is
       	added to the TagType class.
       	"""
       	if not isinstance(name, str):
       	    raise ValueError("TagType name must be a string")
       	self._name = name
       	if not name in _tagTypeDict:
       	    setattr(TagType,name,self)
       	    _tagTypeDict[name] = getattr(TagType,name)
	
    def toString(self):
        """
        Returns the string representation of this TagType.
        """
        return (self._name)

    @staticmethod
    def getTagType(name):
        """
        Returns a TagType given a string.
        Returns the TagType associated with the string given as the parameter. E.g. getTagType("Holography")
        returns TagType.Holography. Returns None if no Tag is associated to the given string.
        """
        if name in _tagTypeDict:
            return (_tagTypeDict[name])
        return None
        
# The known types, these are all available as attributes of the TagType class

# The TagType for a no typed Tag
NoType = TagType("NoType")

	

	
# The TagType for a AlmaRadiometer Tag.
AlmaRadiometer = TagType("AlmaRadiometer")
	

	
# The TagType for a Annotation Tag.
Annotation = TagType("Annotation")
	

	
# The TagType for a Antenna Tag.
Antenna = TagType("Antenna")
	

	

	

	

	

	

	

	
# The TagType for a CalData Tag.
CalData = TagType("CalData")
	

	

	

	

	

	

	

	

	

	

	

	

	

	
# The TagType for a CalReduction Tag.
CalReduction = TagType("CalReduction")
	

	

	

	
# The TagType for a ConfigDescription Tag.
ConfigDescription = TagType("ConfigDescription")
	

	
# The TagType for a CorrelatorMode Tag.
CorrelatorMode = TagType("CorrelatorMode")
	

	
# The TagType for a DataDescription Tag.
DataDescription = TagType("DataDescription")
	

	

	
# The TagType for a DelayModelFixedParameters Tag.
DelayModelFixedParameters = TagType("DelayModelFixedParameters")
	

	
# The TagType for a DelayModelVariableParameters Tag.
DelayModelVariableParameters = TagType("DelayModelVariableParameters")
	

	
# The TagType for a Doppler Tag.
Doppler = TagType("Doppler")
	

	

	
# The TagType for a ExecBlock Tag.
ExecBlock = TagType("ExecBlock")
	

	
# The TagType for a Feed Tag.
Feed = TagType("Feed")
	

	
# The TagType for a Field Tag.
Field = TagType("Field")
	

	
# The TagType for a Flag Tag.
Flag = TagType("Flag")
	

	

	

	
# The TagType for a FocusModel Tag.
FocusModel = TagType("FocusModel")
	

	

	

	

	
# The TagType for a Holography Tag.
Holography = TagType("Holography")
	

	
# The TagType for a Observation Tag.
Observation = TagType("Observation")
	

	

	
# The TagType for a PointingModel Tag.
PointingModel = TagType("PointingModel")
	

	
# The TagType for a Polarization Tag.
Polarization = TagType("Polarization")
	

	
# The TagType for a Processor Tag.
Processor = TagType("Processor")
	

	
# The TagType for a Pulsar Tag.
Pulsar = TagType("Pulsar")
	

	
# The TagType for a Receiver Tag.
Receiver = TagType("Receiver")
	

	
# The TagType for a SBSummary Tag.
SBSummary = TagType("SBSummary")
	

	
# The TagType for a Scale Tag.
Scale = TagType("Scale")
	

	

	

	
# The TagType for a Source Tag.
Source = TagType("Source")
	

	
# The TagType for a SpectralWindow Tag.
SpectralWindow = TagType("SpectralWindow")
	

	
# The TagType for a SquareLawDetector Tag.
SquareLawDetector = TagType("SquareLawDetector")
	

	
# The TagType for a State Tag.
State = TagType("State")
	

	
# The TagType for a Station Tag.
Station = TagType("Station")
	

	

	
# The TagType for a SwitchCycle Tag.
SwitchCycle = TagType("SwitchCycle")
	

	

	

	

	

	

	

