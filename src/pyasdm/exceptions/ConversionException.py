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
# File ConversionException.py


class ConversionException(Exception):
    """
    The ConversionException class represents an exception when
    an error occurs in converting a table to its external
    representation or in restoring a table from one of its
    external representations.
    """

    def __init__(self, msg, tableName):
        """
        msg is a string giving the conversion error specifics.
        tableName is the name of the table being converted
        """
        fullmsg = "Cannot convert table " + tableName + ". " + msg
        super().__init__(fullmsg)
