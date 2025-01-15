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
# File checkListType.py


def checkListType(thisList, atype):
    """
    Returns True if and only if thisList is a list and the type of
    the first non-list value found in thisList is an instance of atype
    or the length of that list is 0.
    """
    result = False
    if isinstance(thisList, list):
        if len(thisList) > 0:
            if isinstance(thisList[0], atype):
                return True
            if isinstance(thisList[0], list):
                return checkListType(thisList[0], atype)
        else:
            # zero length list is True
            return True
    # it's not a list, this means it's not the expected type
    # I think it can't get here recursively, only if called with a non-list argument
    return False
