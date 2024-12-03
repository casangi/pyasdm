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
# File HistoryRow.py
#

import pyasdm.HistoryTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from xml.dom import minidom

import copy


class HistoryRow:
    """
    The HistoryRow class is a row of a HistoryTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a HistoryRow.
        When row is None, create an empty row attached to table, which must be a HistoryTable.
        When row is given, copy those values in to the new row. The row argument must be a HistoryRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.HistoryTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        if row is not None:
            if not isinstance(row, HistoryRow):
                raise ValueError("row must be a MainRow")

            self._execBlockId = Tag(row._execBlockId)

            self._time = ArrayTime(row._time)

            self._message = row._message

            self._priority = row._priority

            self._origin = row._origin

            self._objectId = row._objectId

            self._application = row._application

            self._cliCommand = row._cliCommand

            self._appParms = row._appParms

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

        result += Parser.extendedValueToXML("time", self._time)

        result += Parser.valueToXML("message", self._message)

        result += Parser.valueToXML("priority", self._priority)

        result += Parser.valueToXML("origin", self._origin)

        result += Parser.valueToXML("objectId", self._objectId)

        result += Parser.valueToXML("application", self._application)

        result += Parser.valueToXML("cliCommand", self._cliCommand)

        result += Parser.valueToXML("appParms", self._appParms)

        # extrinsic attributes

        result += Parser.extendedValueToXML("execBlockId", self._execBlockId)

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
                "xmlrow is not a string or a minidom.Element", "HistoryTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "HistoryTable")

        # intrinsic attribute values

        timeNode = rowdom.getElementsByTagName("time")[0]

        self._time = ArrayTime(timeNode.firstChild.data)

        messageNode = rowdom.getElementsByTagName("message")[0]

        self._message = str(messageNode.firstChild.data)

        priorityNode = rowdom.getElementsByTagName("priority")[0]

        self._priority = str(priorityNode.firstChild.data)

        originNode = rowdom.getElementsByTagName("origin")[0]

        self._origin = str(originNode.firstChild.data)

        objectIdNode = rowdom.getElementsByTagName("objectId")[0]

        self._objectId = str(objectIdNode.firstChild.data)

        applicationNode = rowdom.getElementsByTagName("application")[0]

        self._application = str(applicationNode.firstChild.data)

        cliCommandNode = rowdom.getElementsByTagName("cliCommand")[0]

        self._cliCommand = str(cliCommandNode.firstChild.data)

        appParmsNode = rowdom.getElementsByTagName("appParms")[0]

        self._appParms = str(appParmsNode.firstChild.data)

        # extrinsic attribute values

        execBlockIdNode = rowdom.getElementsByTagName("execBlockId")[0]

        self._execBlockId = Tag(execBlockIdNode.firstChild.data)

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

    # ===> Attribute time

    _time = ArrayTime()

    def getTime(self):
        """
        Get time.
        return time as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._time)

    def setTime(self, time):
        """
        Set time with the specified ArrayTime value.
        time The ArrayTime value to which time is to be set.
        The value of time can be anything allowed by the ArrayTime constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the time field, which is part of the key, after this row has been added to this table."
            )

        self._time = ArrayTime(time)

    # ===> Attribute message

    _message = None

    def getMessage(self):
        """
        Get message.
        return message as str
        """

        return self._message

    def setMessage(self, message):
        """
        Set message with the specified str value.
        message The str value to which message is to be set.


        """

        self._message = str(message)

    # ===> Attribute priority

    _priority = None

    def getPriority(self):
        """
        Get priority.
        return priority as str
        """

        return self._priority

    def setPriority(self, priority):
        """
        Set priority with the specified str value.
        priority The str value to which priority is to be set.


        """

        self._priority = str(priority)

    # ===> Attribute origin

    _origin = None

    def getOrigin(self):
        """
        Get origin.
        return origin as str
        """

        return self._origin

    def setOrigin(self, origin):
        """
        Set origin with the specified str value.
        origin The str value to which origin is to be set.


        """

        self._origin = str(origin)

    # ===> Attribute objectId

    _objectId = None

    def getObjectId(self):
        """
        Get objectId.
        return objectId as str
        """

        return self._objectId

    def setObjectId(self, objectId):
        """
        Set objectId with the specified str value.
        objectId The str value to which objectId is to be set.


        """

        self._objectId = str(objectId)

    # ===> Attribute application

    _application = None

    def getApplication(self):
        """
        Get application.
        return application as str
        """

        return self._application

    def setApplication(self, application):
        """
        Set application with the specified str value.
        application The str value to which application is to be set.


        """

        self._application = str(application)

    # ===> Attribute cliCommand

    _cliCommand = None

    def getCliCommand(self):
        """
        Get cliCommand.
        return cliCommand as str
        """

        return self._cliCommand

    def setCliCommand(self, cliCommand):
        """
        Set cliCommand with the specified str value.
        cliCommand The str value to which cliCommand is to be set.


        """

        self._cliCommand = str(cliCommand)

    # ===> Attribute appParms

    _appParms = None

    def getAppParms(self):
        """
        Get appParms.
        return appParms as str
        """

        return self._appParms

    def setAppParms(self, appParms):
        """
        Set appParms with the specified str value.
        appParms The str value to which appParms is to be set.


        """

        self._appParms = str(appParms)

    # Extrinsic Table Attributes

    # ===> Attribute execBlockId

    _execBlockId = Tag()

    def getExecBlockId(self):
        """
        Get execBlockId.
        return execBlockId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._execBlockId)

    def setExecBlockId(self, execBlockId):
        """
        Set execBlockId with the specified Tag value.
        execBlockId The Tag value to which execBlockId is to be set.
        The value of execBlockId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the execBlockId field, which is part of the key, after this row has been added to this table."
            )

        self._execBlockId = Tag(execBlockId)

    # Links

    def getExecBlockUsingExecBlockId(self):
        """
        Returns the row in the ExecBlock table having ExecBlock.execBlockId == execBlockId

        """

        return self._table.getContainer().getExecBlock().getRowByKey(self._execBlockId)

    # comparison methods

    def compareNoAutoInc(
        self,
        execBlockId,
        time,
        message,
        priority,
        origin,
        objectId,
        application,
        cliCommand,
        appParms,
    ):
        """
        Compare each attribute except the autoincrementable one of this HistoryRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # execBlockId is a Tag, compare using the equals method.
        if not self._execBlockId.equals(execBlockId):
            return False

        # time is a ArrayTime, compare using the equals method.
        if not self._time.equals(time):
            return False

        # message is a str, compare using the == operator.
        if not (self._message == message):
            return False

        # priority is a str, compare using the == operator.
        if not (self._priority == priority):
            return False

        # origin is a str, compare using the == operator.
        if not (self._origin == origin):
            return False

        # objectId is a str, compare using the == operator.
        if not (self._objectId == objectId):
            return False

        # application is a str, compare using the == operator.
        if not (self._application == application):
            return False

        # cliCommand is a str, compare using the == operator.
        if not (self._cliCommand == cliCommand):
            return False

        # appParms is a str, compare using the == operator.
        if not (self._appParms == appParms):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getMessage(),
            otherRow.getPriority(),
            otherRow.getOrigin(),
            otherRow.getObjectId(),
            otherRow.getApplication(),
            otherRow.getCliCommand(),
            otherRow.getAppParms(),
        )

    def compareRequiredValue(
        self, message, priority, origin, objectId, application, cliCommand, appParms
    ):

        # message is a str, compare using the == operator.
        if not (self._message == message):
            return False

        # priority is a str, compare using the == operator.
        if not (self._priority == priority):
            return False

        # origin is a str, compare using the == operator.
        if not (self._origin == origin):
            return False

        # objectId is a str, compare using the == operator.
        if not (self._objectId == objectId):
            return False

        # application is a str, compare using the == operator.
        if not (self._application == application):
            return False

        # cliCommand is a str, compare using the == operator.
        if not (self._cliCommand == cliCommand):
            return False

        # appParms is a str, compare using the == operator.
        if not (self._appParms == appParms):
            return False

        return True
