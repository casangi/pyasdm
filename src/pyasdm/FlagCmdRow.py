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
# Warning!
#  --------------------------------------------------------------------
# | This is generated code!  Do not modify this file.                  |
# | If you do, all changes will be lost when the file is re-generated. |
#  --------------------------------------------------------------------
#
# File FlagCmdRow.py
#

import pyasdm.FlagCmdTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from xml.dom import minidom

import copy


class FlagCmdRow:
    """
    The FlagCmdRow class is a row of a FlagCmdTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a FlagCmdRow.
        When row is None, create an empty row attached to table, which must be a FlagCmdTable.
        When row is given, copy those values in to the new row. The row argument must be a FlagCmdRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.FlagCmdTable):
            raise ValueError("table must be a FlagCmdTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._timeInterval = ArrayTimeInterval()

        self._type = None

        self._reason = None

        self._level = 0

        self._severity = 0

        self._applied = None

        self._command = None

        if row is not None:
            if not isinstance(row, FlagCmdRow):
                raise ValueError("row must be a FlagCmdRow")

            # copy constructor

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._type = row._type

            self._reason = row._reason

            self._level = row._level

            self._severity = row._severity

            self._applied = row._applied

            self._command = row._command

    def isAdded(self):
        self._hasBeenAdded = True

    def getTable(self):
        """
        Return the table to which this row belongs.
        """
        return self._table

    def toXML(self):
        """
        Return this row in the form of an XML string.
        """
        result = ""

        result += "<row> \n"

        # intrinsic attributes

        result += Parser.extendedValueToXML("timeInterval", self._timeInterval)

        result += Parser.valueToXML("type", self._type)

        result += Parser.valueToXML("reason", self._reason)

        result += Parser.valueToXML("level", self._level)

        result += Parser.valueToXML("severity", self._severity)

        result += Parser.valueToXML("applied", self._applied)

        result += Parser.valueToXML("command", self._command)

        # links, if any

        result += "</row>\n"
        return result

    def setFromXML(self, xmlrow):
        """
        Fill the values of this row from an XML string
        that was produced by the toXML() method.
        If xmlrow is a minidom.Element with a nodeName of row then
        it will be used as is. Anything else that is not a string
        is an error.
        """
        rowdom = None
        if isinstance(xmlrow, str):
            xmldom = minidom.parseString(xmlrow)
            rowdom = xmldom.firstChild
        elif isinstance(xmlrow, minidom.Element):
            rowdom = xmlrow
        else:
            raise ConversionException(
                "xmlrow is not a string or a minidom.Element", "FlagCmdTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "FlagCmdTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        typeNode = rowdom.getElementsByTagName("type")[0]

        self._type = str(typeNode.firstChild.data.strip())

        reasonNode = rowdom.getElementsByTagName("reason")[0]

        self._reason = str(reasonNode.firstChild.data.strip())

        levelNode = rowdom.getElementsByTagName("level")[0]

        self._level = int(levelNode.firstChild.data.strip())

        severityNode = rowdom.getElementsByTagName("severity")[0]

        self._severity = int(severityNode.firstChild.data.strip())

        appliedNode = rowdom.getElementsByTagName("applied")[0]

        self._applied = bool(appliedNode.firstChild.data.strip())

        commandNode = rowdom.getElementsByTagName("command")[0]

        self._command = str(commandNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._timeInterval.toBin(eos)

        eos.writeStr(self._type)

        eos.writeStr(self._reason)

        eos.writeInt(self._level)

        eos.writeInt(self._severity)

        eos.writeBool(self._applied)

        eos.writeStr(self._command)

    @staticmethod
    def timeIntervalFromBin(row, eis):
        """
        Set the timeInterval in row from the EndianInput (eis) instance.
        """

        row._timeInterval = ArrayTimeInterval.fromBin(eis)

    @staticmethod
    def typeFromBin(row, eis):
        """
        Set the type in row from the EndianInput (eis) instance.
        """

        row._type = eis.readStr()

    @staticmethod
    def reasonFromBin(row, eis):
        """
        Set the reason in row from the EndianInput (eis) instance.
        """

        row._reason = eis.readStr()

    @staticmethod
    def levelFromBin(row, eis):
        """
        Set the level in row from the EndianInput (eis) instance.
        """

        row._level = eis.readInt()

    @staticmethod
    def severityFromBin(row, eis):
        """
        Set the severity in row from the EndianInput (eis) instance.
        """

        row._severity = eis.readInt()

    @staticmethod
    def appliedFromBin(row, eis):
        """
        Set the applied in row from the EndianInput (eis) instance.
        """

        row._applied = eis.readBool()

    @staticmethod
    def commandFromBin(row, eis):
        """
        Set the command in row from the EndianInput (eis) instance.
        """

        row._command = eis.readStr()

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["timeInterval"] = FlagCmdRow.timeIntervalFromBin
        _fromBinMethods["type"] = FlagCmdRow.typeFromBin
        _fromBinMethods["reason"] = FlagCmdRow.reasonFromBin
        _fromBinMethods["level"] = FlagCmdRow.levelFromBin
        _fromBinMethods["severity"] = FlagCmdRow.severityFromBin
        _fromBinMethods["applied"] = FlagCmdRow.appliedFromBin
        _fromBinMethods["command"] = FlagCmdRow.commandFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = FlagCmdRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " FlagCmd",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute timeInterval

    _timeInterval = ArrayTimeInterval()

    def getTimeInterval(self):
        """
        Get timeInterval.
        return timeInterval as ArrayTimeInterval
        """

        # make sure it is a copy of ArrayTimeInterval
        return ArrayTimeInterval(self._timeInterval)

    def setTimeInterval(self, timeInterval):
        """
        Set timeInterval with the specified ArrayTimeInterval value.
        timeInterval The ArrayTimeInterval value to which timeInterval is to be set.
        The value of timeInterval can be anything allowed by the ArrayTimeInterval constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the timeInterval field, which is part of the key, after this row has been added to this table."
            )

        self._timeInterval = ArrayTimeInterval(timeInterval)

    # ===> Attribute type

    _type = None

    def getType(self):
        """
        Get type.
        return type as str
        """

        return self._type

    def setType(self, type):
        """
        Set type with the specified str value.
        type The str value to which type is to be set.


        """

        self._type = str(type)

    # ===> Attribute reason

    _reason = None

    def getReason(self):
        """
        Get reason.
        return reason as str
        """

        return self._reason

    def setReason(self, reason):
        """
        Set reason with the specified str value.
        reason The str value to which reason is to be set.


        """

        self._reason = str(reason)

    # ===> Attribute level

    _level = 0

    def getLevel(self):
        """
        Get level.
        return level as int
        """

        return self._level

    def setLevel(self, level):
        """
        Set level with the specified int value.
        level The int value to which level is to be set.


        """

        self._level = int(level)

    # ===> Attribute severity

    _severity = 0

    def getSeverity(self):
        """
        Get severity.
        return severity as int
        """

        return self._severity

    def setSeverity(self, severity):
        """
        Set severity with the specified int value.
        severity The int value to which severity is to be set.


        """

        self._severity = int(severity)

    # ===> Attribute applied

    _applied = None

    def getApplied(self):
        """
        Get applied.
        return applied as bool
        """

        return self._applied

    def setApplied(self, applied):
        """
        Set applied with the specified bool value.
        applied The bool value to which applied is to be set.


        """

        self._applied = bool(applied)

    # ===> Attribute command

    _command = None

    def getCommand(self):
        """
        Get command.
        return command as str
        """

        return self._command

    def setCommand(self, command):
        """
        Set command with the specified str value.
        command The str value to which command is to be set.


        """

        self._command = str(command)

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(
        self, timeInterval, type, reason, level, severity, applied, command
    ):
        """
        Compare each attribute except the autoincrementable one of this FlagCmdRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # type is a str, compare using the == operator.
        if not (self._type == type):
            return False

        # reason is a str, compare using the == operator.
        if not (self._reason == reason):
            return False

        # level is a int, compare using the == operator.
        if not (self._level == level):
            return False

        # severity is a int, compare using the == operator.
        if not (self._severity == severity):
            return False

        # applied is a bool, compare using the == operator.
        if not (self._applied == applied):
            return False

        # command is a str, compare using the == operator.
        if not (self._command == command):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getType(),
            otherRow.getReason(),
            otherRow.getLevel(),
            otherRow.getSeverity(),
            otherRow.getApplied(),
            otherRow.getCommand(),
        )

    def compareRequiredValue(self, type, reason, level, severity, applied, command):

        # type is a str, compare using the == operator.
        if not (self._type == type):
            return False

        # reason is a str, compare using the == operator.
        if not (self._reason == reason):
            return False

        # level is a int, compare using the == operator.
        if not (self._level == level):
            return False

        # severity is a int, compare using the == operator.
        if not (self._severity == severity):
            return False

        # applied is a bool, compare using the == operator.
        if not (self._applied == applied):
            return False

        # command is a str, compare using the == operator.
        if not (self._command == command):
            return False

        return True


# initialize the dictionary that maps fields to init methods
FlagCmdRow.initFromBinMethods()
