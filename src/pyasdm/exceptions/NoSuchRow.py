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
# File NoSuchRow.py


class NoSuchRow(Exception):
    """
    Generate an exception when an expected row cannot be found.
    """

    # at the moment this can only occur for Links (AntennaRow.py) and
    # the first argument is the link target table name and the second
    # argument is the calling table name. Both should be strings.
    # There is a 3rd bool argument in the c++ implementation for this case
    # but it's not used there and is omitted here
    def __init__(self, toTableName, fromTableName):
        fullmsg = f"The optional link to table {toTableName} in this row of table {fromTableName} does not exist!"
        super().__init__(fullmsg)
