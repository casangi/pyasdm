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
# File Representable.py

class Representable:
    """
    The Representable class is inherited by all Table classes which
    must have their own implementations of each of these functions.
    This class only exists in python so that each table is an
    instance of Representable.
    """

    def __init__(self):
        # nothing to do here
        pass

    def toXML(self):
        raise(ValueError("Representable.toXML is not implemented"))

    def fromXML(self, xmlString):
        raise(ValueError("Representable.fromXML is not implemented"))

    def toFITS(self):
        raise(ValueError("Representable.toFITS is not implemented"))

    def fromFITS(self, fitsBytes):
        raise(ValueError("Representable.fromFITS is not implemented"))

    def setEntity(self, thisEntity):
        raise(ValueError("Representable.setEntity is not implemented"))

    def getEntity(self):
        raise(ValueError("Representable.getEntity is not implemented"))

    def getName(self):
        raise(ValueError("Representable.getName is not implemented"))

    def size(self):
        raise(ValueError("Representable.size is not implemented"))



