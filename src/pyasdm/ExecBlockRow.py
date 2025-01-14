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
# File ExecBlockRow.py
#

import pyasdm.ExecBlockTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from xml.dom import minidom

import copy


class ExecBlockRow:
    """
    The ExecBlockRow class is a row of a ExecBlockTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a ExecBlockRow.
        When row is None, create an empty row attached to table, which must be a ExecBlockTable.
        When row is given, copy those values in to the new row. The row argument must be a ExecBlockRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.ExecBlockTable):
            raise ValueError("table must be a ExecBlockTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._execBlockId = Tag()

        self._startTime = ArrayTime()

        self._endTime = ArrayTime()

        self._execBlockNum = 0

        self._execBlockUID = EntityRef()

        self._projectUID = EntityRef()

        self._configName = None

        self._telescopeName = None

        self._observerName = None

        self._numObservingLog = 0

        self._observingLog = []  # this is a list of str []

        self._sessionReference = EntityRef()

        self._baseRangeMin = Length()

        self._baseRangeMax = Length()

        self._baseRmsMinor = Length()

        self._baseRmsMajor = Length()

        self._basePa = Angle()

        self._aborted = None

        self._numAntenna = 0

        self._releaseDateExists = False

        self._releaseDate = ArrayTime()

        self._schedulerModeExists = False

        self._schedulerMode = None

        self._siteAltitudeExists = False

        self._siteAltitude = Length()

        self._siteLongitudeExists = False

        self._siteLongitude = Angle()

        self._siteLatitudeExists = False

        self._siteLatitude = Angle()

        self._observingScriptExists = False

        self._observingScript = None

        self._observingScriptUIDExists = False

        self._observingScriptUID = EntityRef()

        # extrinsic attributes

        self._antennaId = []  # this is a list of Tag []

        self._sBSummaryId = Tag()

        self._scaleIdExists = False

        self._scaleId = Tag()

        if row is not None:
            if not isinstance(row, ExecBlockRow):
                raise ValueError("row must be a ExecBlockRow")

            # copy constructor

            self._execBlockId = Tag(row._execBlockId)

            self._startTime = ArrayTime(row._startTime)

            self._endTime = ArrayTime(row._endTime)

            self._execBlockNum = row._execBlockNum

            self._execBlockUID = EntityRef(row._execBlockUID)

            self._projectUID = EntityRef(row._projectUID)

            self._configName = row._configName

            self._telescopeName = row._telescopeName

            self._observerName = row._observerName

            self._numObservingLog = row._numObservingLog

            # observingLog is a  list , make a deep copy
            self._observingLog = copy.deepcopy(row._observingLog)

            self._sessionReference = EntityRef(row._sessionReference)

            self._baseRangeMin = Length(row._baseRangeMin)

            self._baseRangeMax = Length(row._baseRangeMax)

            self._baseRmsMinor = Length(row._baseRmsMinor)

            self._baseRmsMajor = Length(row._baseRmsMajor)

            self._basePa = Angle(row._basePa)

            self._aborted = row._aborted

            self._numAntenna = row._numAntenna

            # antennaId is a list, let's populate self._antennaId element by element.
            if self._antennaId is None:
                self._antennaId = []

            for i in range(len(row._antennaId)):

                self._antennaId.append(Tag(row._antennaId[i]))

            self._sBSummaryId = Tag(row._sBSummaryId)

            # by default set systematically releaseDate's value to something not None

            if row._releaseDateExists:

                self._releaseDate = ArrayTime(row._releaseDate)

                self._releaseDateExists = True

            # by default set systematically schedulerMode's value to something not None

            if row._schedulerModeExists:

                self._schedulerMode = row._schedulerMode

                self._schedulerModeExists = True

            # by default set systematically siteAltitude's value to something not None

            if row._siteAltitudeExists:

                self._siteAltitude = Length(row._siteAltitude)

                self._siteAltitudeExists = True

            # by default set systematically siteLongitude's value to something not None

            if row._siteLongitudeExists:

                self._siteLongitude = Angle(row._siteLongitude)

                self._siteLongitudeExists = True

            # by default set systematically siteLatitude's value to something not None

            if row._siteLatitudeExists:

                self._siteLatitude = Angle(row._siteLatitude)

                self._siteLatitudeExists = True

            # by default set systematically observingScript's value to something not None

            if row._observingScriptExists:

                self._observingScript = row._observingScript

                self._observingScriptExists = True

            # by default set systematically observingScriptUID's value to something not None

            if row._observingScriptUIDExists:

                self._observingScriptUID = EntityRef(row._observingScriptUID)

                self._observingScriptUIDExists = True

            # by default set systematically scaleId's value to something not None

            if row._scaleIdExists:

                self._scaleId = Tag(row._scaleId)

                self._scaleIdExists = True

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

        result += Parser.extendedValueToXML("execBlockId", self._execBlockId)

        result += Parser.extendedValueToXML("startTime", self._startTime)

        result += Parser.extendedValueToXML("endTime", self._endTime)

        result += Parser.valueToXML("execBlockNum", self._execBlockNum)

        result += Parser.extendedValueToXML("execBlockUID", self._execBlockUID)

        result += Parser.extendedValueToXML("projectUID", self._projectUID)

        result += Parser.valueToXML("configName", self._configName)

        result += Parser.valueToXML("telescopeName", self._telescopeName)

        result += Parser.valueToXML("observerName", self._observerName)

        result += Parser.valueToXML("numObservingLog", self._numObservingLog)

        result += Parser.listValueToXML("observingLog", self._observingLog)

        result += Parser.extendedValueToXML("sessionReference", self._sessionReference)

        result += Parser.extendedValueToXML("baseRangeMin", self._baseRangeMin)

        result += Parser.extendedValueToXML("baseRangeMax", self._baseRangeMax)

        result += Parser.extendedValueToXML("baseRmsMinor", self._baseRmsMinor)

        result += Parser.extendedValueToXML("baseRmsMajor", self._baseRmsMajor)

        result += Parser.extendedValueToXML("basePa", self._basePa)

        result += Parser.valueToXML("aborted", self._aborted)

        result += Parser.valueToXML("numAntenna", self._numAntenna)

        if self._releaseDateExists:

            result += Parser.extendedValueToXML("releaseDate", self._releaseDate)

        if self._schedulerModeExists:

            result += Parser.valueToXML("schedulerMode", self._schedulerMode)

        if self._siteAltitudeExists:

            result += Parser.extendedValueToXML("siteAltitude", self._siteAltitude)

        if self._siteLongitudeExists:

            result += Parser.extendedValueToXML("siteLongitude", self._siteLongitude)

        if self._siteLatitudeExists:

            result += Parser.extendedValueToXML("siteLatitude", self._siteLatitude)

        if self._observingScriptExists:

            result += Parser.valueToXML("observingScript", self._observingScript)

        if self._observingScriptUIDExists:

            result += Parser.extendedValueToXML(
                "observingScriptUID", self._observingScriptUID
            )

        # extrinsic attributes

        result += Parser.listExtendedValueToXML("antennaId", self._antennaId)

        result += Parser.extendedValueToXML("sBSummaryId", self._sBSummaryId)

        if self._scaleIdExists:

            result += Parser.extendedValueToXML("scaleId", self._scaleId)

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
                "xmlrow is not a string or a minidom.Element", "ExecBlockTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "ExecBlockTable")

        # intrinsic attribute values

        execBlockIdNode = rowdom.getElementsByTagName("execBlockId")[0]

        self._execBlockId = Tag(execBlockIdNode.firstChild.data.strip())

        startTimeNode = rowdom.getElementsByTagName("startTime")[0]

        self._startTime = ArrayTime(startTimeNode.firstChild.data.strip())

        endTimeNode = rowdom.getElementsByTagName("endTime")[0]

        self._endTime = ArrayTime(endTimeNode.firstChild.data.strip())

        execBlockNumNode = rowdom.getElementsByTagName("execBlockNum")[0]

        self._execBlockNum = int(execBlockNumNode.firstChild.data.strip())

        execBlockUIDNode = rowdom.getElementsByTagName("execBlockUID")[0]

        self._execBlockUID = EntityRef(execBlockUIDNode.toxml())

        projectUIDNode = rowdom.getElementsByTagName("projectUID")[0]

        self._projectUID = EntityRef(projectUIDNode.toxml())

        configNameNode = rowdom.getElementsByTagName("configName")[0]

        self._configName = str(configNameNode.firstChild.data.strip())

        telescopeNameNode = rowdom.getElementsByTagName("telescopeName")[0]

        self._telescopeName = str(telescopeNameNode.firstChild.data.strip())

        observerNameNode = rowdom.getElementsByTagName("observerName")[0]

        self._observerName = str(observerNameNode.firstChild.data.strip())

        numObservingLogNode = rowdom.getElementsByTagName("numObservingLog")[0]

        self._numObservingLog = int(numObservingLogNode.firstChild.data.strip())

        observingLogNode = rowdom.getElementsByTagName("observingLog")[0]

        observingLogStr = observingLogNode.firstChild.data.strip()

        self._observingLog = Parser.stringListToLists(
            observingLogStr, str, "ExecBlock", False
        )

        sessionReferenceNode = rowdom.getElementsByTagName("sessionReference")[0]

        self._sessionReference = EntityRef(sessionReferenceNode.toxml())

        baseRangeMinNode = rowdom.getElementsByTagName("baseRangeMin")[0]

        self._baseRangeMin = Length(baseRangeMinNode.firstChild.data.strip())

        baseRangeMaxNode = rowdom.getElementsByTagName("baseRangeMax")[0]

        self._baseRangeMax = Length(baseRangeMaxNode.firstChild.data.strip())

        baseRmsMinorNode = rowdom.getElementsByTagName("baseRmsMinor")[0]

        self._baseRmsMinor = Length(baseRmsMinorNode.firstChild.data.strip())

        baseRmsMajorNode = rowdom.getElementsByTagName("baseRmsMajor")[0]

        self._baseRmsMajor = Length(baseRmsMajorNode.firstChild.data.strip())

        basePaNode = rowdom.getElementsByTagName("basePa")[0]

        self._basePa = Angle(basePaNode.firstChild.data.strip())

        abortedNode = rowdom.getElementsByTagName("aborted")[0]

        self._aborted = bool(abortedNode.firstChild.data.strip())

        numAntennaNode = rowdom.getElementsByTagName("numAntenna")[0]

        self._numAntenna = int(numAntennaNode.firstChild.data.strip())

        releaseDateNode = rowdom.getElementsByTagName("releaseDate")
        if len(releaseDateNode) > 0:

            self._releaseDate = ArrayTime(releaseDateNode[0].firstChild.data.strip())

            self._releaseDateExists = True

        schedulerModeNode = rowdom.getElementsByTagName("schedulerMode")
        if len(schedulerModeNode) > 0:

            self._schedulerMode = str(schedulerModeNode[0].firstChild.data.strip())

            self._schedulerModeExists = True

        siteAltitudeNode = rowdom.getElementsByTagName("siteAltitude")
        if len(siteAltitudeNode) > 0:

            self._siteAltitude = Length(siteAltitudeNode[0].firstChild.data.strip())

            self._siteAltitudeExists = True

        siteLongitudeNode = rowdom.getElementsByTagName("siteLongitude")
        if len(siteLongitudeNode) > 0:

            self._siteLongitude = Angle(siteLongitudeNode[0].firstChild.data.strip())

            self._siteLongitudeExists = True

        siteLatitudeNode = rowdom.getElementsByTagName("siteLatitude")
        if len(siteLatitudeNode) > 0:

            self._siteLatitude = Angle(siteLatitudeNode[0].firstChild.data.strip())

            self._siteLatitudeExists = True

        observingScriptNode = rowdom.getElementsByTagName("observingScript")
        if len(observingScriptNode) > 0:

            self._observingScript = str(observingScriptNode[0].firstChild.data.strip())

            self._observingScriptExists = True

        observingScriptUIDNode = rowdom.getElementsByTagName("observingScriptUID")
        if len(observingScriptUIDNode) > 0:

            self._observingScriptUID = EntityRef(
                observingScriptUIDNode[0].firstChild.data.strip()
            )

            self._observingScriptUIDExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        antennaIdStr = antennaIdNode.firstChild.data.strip()

        self._antennaId = Parser.stringListToLists(antennaIdStr, Tag, "ExecBlock", True)

        sBSummaryIdNode = rowdom.getElementsByTagName("sBSummaryId")[0]

        self._sBSummaryId = Tag(sBSummaryIdNode.firstChild.data.strip())

        scaleIdNode = rowdom.getElementsByTagName("scaleId")
        if len(scaleIdNode) > 0:

            self._scaleId = Tag(scaleIdNode[0].firstChild.data.strip())

            self._scaleIdExists = True

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._execBlockId.toBin(eos)

        self._startTime.toBin(eos)

        self._endTime.toBin(eos)

        eos.writeInt(self._execBlockNum)

        self._execBlockUID.toBin(eos)

        self._projectUID.toBin(eos)

        eos.writeStr(self._configName)

        eos.writeStr(self._telescopeName)

        eos.writeStr(self._observerName)

        eos.writeInt(self._numObservingLog)

        eos.writeInt(len(self._observingLog))
        for i in range(len(self._observingLog)):

            eos.writeStr(self._observingLog[i])

        self._sessionReference.toBin(eos)

        self._baseRangeMin.toBin(eos)

        self._baseRangeMax.toBin(eos)

        self._baseRmsMinor.toBin(eos)

        self._baseRmsMajor.toBin(eos)

        self._basePa.toBin(eos)

        eos.writeBool(self._aborted)

        eos.writeInt(self._numAntenna)

        Tag.listToBin(self._antennaId, eos)

        self._sBSummaryId.toBin(eos)

        eos.writeBool(self._releaseDateExists)
        if self._releaseDateExists:

            self._releaseDate.toBin(eos)

        eos.writeBool(self._schedulerModeExists)
        if self._schedulerModeExists:

            eos.writeStr(self._schedulerMode)

        eos.writeBool(self._siteAltitudeExists)
        if self._siteAltitudeExists:

            self._siteAltitude.toBin(eos)

        eos.writeBool(self._siteLongitudeExists)
        if self._siteLongitudeExists:

            self._siteLongitude.toBin(eos)

        eos.writeBool(self._siteLatitudeExists)
        if self._siteLatitudeExists:

            self._siteLatitude.toBin(eos)

        eos.writeBool(self._observingScriptExists)
        if self._observingScriptExists:

            eos.writeStr(self._observingScript)

        eos.writeBool(self._observingScriptUIDExists)
        if self._observingScriptUIDExists:

            self._observingScriptUID.toBin(eos)

        eos.writeBool(self._scaleIdExists)
        if self._scaleIdExists:

            self._scaleId.toBin(eos)

    @staticmethod
    def execBlockIdFromBin(row, eis):
        """
        Set the execBlockId in row from the EndianInput (eis) instance.
        """

        row._execBlockId = Tag.fromBin(eis)

    @staticmethod
    def startTimeFromBin(row, eis):
        """
        Set the startTime in row from the EndianInput (eis) instance.
        """

        row._startTime = ArrayTime.fromBin(eis)

    @staticmethod
    def endTimeFromBin(row, eis):
        """
        Set the endTime in row from the EndianInput (eis) instance.
        """

        row._endTime = ArrayTime.fromBin(eis)

    @staticmethod
    def execBlockNumFromBin(row, eis):
        """
        Set the execBlockNum in row from the EndianInput (eis) instance.
        """

        row._execBlockNum = eis.readInt()

    @staticmethod
    def execBlockUIDFromBin(row, eis):
        """
        Set the execBlockUID in row from the EndianInput (eis) instance.
        """

        row._execBlockUID = EntityRef.fromBin(eis)

    @staticmethod
    def projectUIDFromBin(row, eis):
        """
        Set the projectUID in row from the EndianInput (eis) instance.
        """

        row._projectUID = EntityRef.fromBin(eis)

    @staticmethod
    def configNameFromBin(row, eis):
        """
        Set the configName in row from the EndianInput (eis) instance.
        """

        row._configName = eis.readStr()

    @staticmethod
    def telescopeNameFromBin(row, eis):
        """
        Set the telescopeName in row from the EndianInput (eis) instance.
        """

        row._telescopeName = eis.readStr()

    @staticmethod
    def observerNameFromBin(row, eis):
        """
        Set the observerName in row from the EndianInput (eis) instance.
        """

        row._observerName = eis.readStr()

    @staticmethod
    def numObservingLogFromBin(row, eis):
        """
        Set the numObservingLog in row from the EndianInput (eis) instance.
        """

        row._numObservingLog = eis.readInt()

    @staticmethod
    def observingLogFromBin(row, eis):
        """
        Set the observingLog in row from the EndianInput (eis) instance.
        """

        observingLogDim1 = eis.readInt()
        thisList = []
        for i in range(observingLogDim1):
            thisValue = eis.readStr()
            thisList.append(thisValue)
        row._observingLog = thisList

    @staticmethod
    def sessionReferenceFromBin(row, eis):
        """
        Set the sessionReference in row from the EndianInput (eis) instance.
        """

        row._sessionReference = EntityRef.fromBin(eis)

    @staticmethod
    def baseRangeMinFromBin(row, eis):
        """
        Set the baseRangeMin in row from the EndianInput (eis) instance.
        """

        row._baseRangeMin = Length.fromBin(eis)

    @staticmethod
    def baseRangeMaxFromBin(row, eis):
        """
        Set the baseRangeMax in row from the EndianInput (eis) instance.
        """

        row._baseRangeMax = Length.fromBin(eis)

    @staticmethod
    def baseRmsMinorFromBin(row, eis):
        """
        Set the baseRmsMinor in row from the EndianInput (eis) instance.
        """

        row._baseRmsMinor = Length.fromBin(eis)

    @staticmethod
    def baseRmsMajorFromBin(row, eis):
        """
        Set the baseRmsMajor in row from the EndianInput (eis) instance.
        """

        row._baseRmsMajor = Length.fromBin(eis)

    @staticmethod
    def basePaFromBin(row, eis):
        """
        Set the basePa in row from the EndianInput (eis) instance.
        """

        row._basePa = Angle.fromBin(eis)

    @staticmethod
    def abortedFromBin(row, eis):
        """
        Set the aborted in row from the EndianInput (eis) instance.
        """

        row._aborted = eis.readBool()

    @staticmethod
    def numAntennaFromBin(row, eis):
        """
        Set the numAntenna in row from the EndianInput (eis) instance.
        """

        row._numAntenna = eis.readInt()

    @staticmethod
    def antennaIdFromBin(row, eis):
        """
        Set the antennaId in row from the EndianInput (eis) instance.
        """

        row._antennaId = Tag.from1DBin(eis)

    @staticmethod
    def sBSummaryIdFromBin(row, eis):
        """
        Set the sBSummaryId in row from the EndianInput (eis) instance.
        """

        row._sBSummaryId = Tag.fromBin(eis)

    @staticmethod
    def releaseDateFromBin(row, eis):
        """
        Set the optional releaseDate in row from the EndianInput (eis) instance.
        """
        row._releaseDateExists = eis.readBool()
        if row._releaseDateExists:

            row._releaseDate = ArrayTime.fromBin(eis)

    @staticmethod
    def schedulerModeFromBin(row, eis):
        """
        Set the optional schedulerMode in row from the EndianInput (eis) instance.
        """
        row._schedulerModeExists = eis.readBool()
        if row._schedulerModeExists:

            row._schedulerMode = eis.readStr()

    @staticmethod
    def siteAltitudeFromBin(row, eis):
        """
        Set the optional siteAltitude in row from the EndianInput (eis) instance.
        """
        row._siteAltitudeExists = eis.readBool()
        if row._siteAltitudeExists:

            row._siteAltitude = Length.fromBin(eis)

    @staticmethod
    def siteLongitudeFromBin(row, eis):
        """
        Set the optional siteLongitude in row from the EndianInput (eis) instance.
        """
        row._siteLongitudeExists = eis.readBool()
        if row._siteLongitudeExists:

            row._siteLongitude = Angle.fromBin(eis)

    @staticmethod
    def siteLatitudeFromBin(row, eis):
        """
        Set the optional siteLatitude in row from the EndianInput (eis) instance.
        """
        row._siteLatitudeExists = eis.readBool()
        if row._siteLatitudeExists:

            row._siteLatitude = Angle.fromBin(eis)

    @staticmethod
    def observingScriptFromBin(row, eis):
        """
        Set the optional observingScript in row from the EndianInput (eis) instance.
        """
        row._observingScriptExists = eis.readBool()
        if row._observingScriptExists:

            row._observingScript = eis.readStr()

    @staticmethod
    def observingScriptUIDFromBin(row, eis):
        """
        Set the optional observingScriptUID in row from the EndianInput (eis) instance.
        """
        row._observingScriptUIDExists = eis.readBool()
        if row._observingScriptUIDExists:

            row._observingScriptUID = EntityRef.fromBin(eis)

    @staticmethod
    def scaleIdFromBin(row, eis):
        """
        Set the optional scaleId in row from the EndianInput (eis) instance.
        """
        row._scaleIdExists = eis.readBool()
        if row._scaleIdExists:

            row._scaleId = Tag.fromBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["execBlockId"] = ExecBlockRow.execBlockIdFromBin
        _fromBinMethods["startTime"] = ExecBlockRow.startTimeFromBin
        _fromBinMethods["endTime"] = ExecBlockRow.endTimeFromBin
        _fromBinMethods["execBlockNum"] = ExecBlockRow.execBlockNumFromBin
        _fromBinMethods["execBlockUID"] = ExecBlockRow.execBlockUIDFromBin
        _fromBinMethods["projectUID"] = ExecBlockRow.projectUIDFromBin
        _fromBinMethods["configName"] = ExecBlockRow.configNameFromBin
        _fromBinMethods["telescopeName"] = ExecBlockRow.telescopeNameFromBin
        _fromBinMethods["observerName"] = ExecBlockRow.observerNameFromBin
        _fromBinMethods["numObservingLog"] = ExecBlockRow.numObservingLogFromBin
        _fromBinMethods["observingLog"] = ExecBlockRow.observingLogFromBin
        _fromBinMethods["sessionReference"] = ExecBlockRow.sessionReferenceFromBin
        _fromBinMethods["baseRangeMin"] = ExecBlockRow.baseRangeMinFromBin
        _fromBinMethods["baseRangeMax"] = ExecBlockRow.baseRangeMaxFromBin
        _fromBinMethods["baseRmsMinor"] = ExecBlockRow.baseRmsMinorFromBin
        _fromBinMethods["baseRmsMajor"] = ExecBlockRow.baseRmsMajorFromBin
        _fromBinMethods["basePa"] = ExecBlockRow.basePaFromBin
        _fromBinMethods["aborted"] = ExecBlockRow.abortedFromBin
        _fromBinMethods["numAntenna"] = ExecBlockRow.numAntennaFromBin
        _fromBinMethods["antennaId"] = ExecBlockRow.antennaIdFromBin
        _fromBinMethods["sBSummaryId"] = ExecBlockRow.sBSummaryIdFromBin

        _fromBinMethods["releaseDate"] = ExecBlockRow.releaseDateFromBin
        _fromBinMethods["schedulerMode"] = ExecBlockRow.schedulerModeFromBin
        _fromBinMethods["siteAltitude"] = ExecBlockRow.siteAltitudeFromBin
        _fromBinMethods["siteLongitude"] = ExecBlockRow.siteLongitudeFromBin
        _fromBinMethods["siteLatitude"] = ExecBlockRow.siteLatitudeFromBin
        _fromBinMethods["observingScript"] = ExecBlockRow.observingScriptFromBin
        _fromBinMethods["observingScriptUID"] = ExecBlockRow.observingScriptUIDFromBin
        _fromBinMethods["scaleId"] = ExecBlockRow.scaleIdFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = ExecBlockRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " ExecBlock",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

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

    # ===> Attribute startTime

    _startTime = ArrayTime()

    def getStartTime(self):
        """
        Get startTime.
        return startTime as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._startTime)

    def setStartTime(self, startTime):
        """
        Set startTime with the specified ArrayTime value.
        startTime The ArrayTime value to which startTime is to be set.
        The value of startTime can be anything allowed by the ArrayTime constructor.

        """

        self._startTime = ArrayTime(startTime)

    # ===> Attribute endTime

    _endTime = ArrayTime()

    def getEndTime(self):
        """
        Get endTime.
        return endTime as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._endTime)

    def setEndTime(self, endTime):
        """
        Set endTime with the specified ArrayTime value.
        endTime The ArrayTime value to which endTime is to be set.
        The value of endTime can be anything allowed by the ArrayTime constructor.

        """

        self._endTime = ArrayTime(endTime)

    # ===> Attribute execBlockNum

    _execBlockNum = 0

    def getExecBlockNum(self):
        """
        Get execBlockNum.
        return execBlockNum as int
        """

        return self._execBlockNum

    def setExecBlockNum(self, execBlockNum):
        """
        Set execBlockNum with the specified int value.
        execBlockNum The int value to which execBlockNum is to be set.


        """

        self._execBlockNum = int(execBlockNum)

    # ===> Attribute execBlockUID

    _execBlockUID = EntityRef()

    def getExecBlockUID(self):
        """
        Get execBlockUID.
        return execBlockUID as EntityRef
        """

        # make sure it is a copy of EntityRef
        return EntityRef(self._execBlockUID)

    def setExecBlockUID(self, execBlockUID):
        """
        Set execBlockUID with the specified EntityRef value.
        execBlockUID The EntityRef value to which execBlockUID is to be set.
        The value of execBlockUID can be anything allowed by the EntityRef constructor.

        """

        self._execBlockUID = EntityRef(execBlockUID)

    # ===> Attribute projectUID

    _projectUID = EntityRef()

    def getProjectUID(self):
        """
        Get projectUID.
        return projectUID as EntityRef
        """

        # make sure it is a copy of EntityRef
        return EntityRef(self._projectUID)

    def setProjectUID(self, projectUID):
        """
        Set projectUID with the specified EntityRef value.
        projectUID The EntityRef value to which projectUID is to be set.
        The value of projectUID can be anything allowed by the EntityRef constructor.

        """

        self._projectUID = EntityRef(projectUID)

    # ===> Attribute configName

    _configName = None

    def getConfigName(self):
        """
        Get configName.
        return configName as str
        """

        return self._configName

    def setConfigName(self, configName):
        """
        Set configName with the specified str value.
        configName The str value to which configName is to be set.


        """

        self._configName = str(configName)

    # ===> Attribute telescopeName

    _telescopeName = None

    def getTelescopeName(self):
        """
        Get telescopeName.
        return telescopeName as str
        """

        return self._telescopeName

    def setTelescopeName(self, telescopeName):
        """
        Set telescopeName with the specified str value.
        telescopeName The str value to which telescopeName is to be set.


        """

        self._telescopeName = str(telescopeName)

    # ===> Attribute observerName

    _observerName = None

    def getObserverName(self):
        """
        Get observerName.
        return observerName as str
        """

        return self._observerName

    def setObserverName(self, observerName):
        """
        Set observerName with the specified str value.
        observerName The str value to which observerName is to be set.


        """

        self._observerName = str(observerName)

    # ===> Attribute numObservingLog

    _numObservingLog = 0

    def getNumObservingLog(self):
        """
        Get numObservingLog.
        return numObservingLog as int
        """

        return self._numObservingLog

    def setNumObservingLog(self, numObservingLog):
        """
        Set numObservingLog with the specified int value.
        numObservingLog The int value to which numObservingLog is to be set.


        """

        self._numObservingLog = int(numObservingLog)

    # ===> Attribute observingLog

    _observingLog = None  # this is a 1D list of str

    def getObservingLog(self):
        """
        Get observingLog.
        return observingLog as str []
        """

        return copy.deepcopy(self._observingLog)

    def setObservingLog(self, observingLog):
        """
        Set observingLog with the specified str []  value.
        observingLog The str []  value to which observingLog is to be set.


        """

        # value must be a list
        if not isinstance(observingLog, list):
            raise ValueError("The value of observingLog must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(observingLog)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of observingLog is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not Parser.checkListType(observingLog, str):
                raise ValueError(
                    "type of the first value in observingLog is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._observingLog = copy.deepcopy(observingLog)
        except Exception as exc:
            raise ValueError("Invalid observingLog : " + str(exc))

    # ===> Attribute sessionReference

    _sessionReference = EntityRef()

    def getSessionReference(self):
        """
        Get sessionReference.
        return sessionReference as EntityRef
        """

        # make sure it is a copy of EntityRef
        return EntityRef(self._sessionReference)

    def setSessionReference(self, sessionReference):
        """
        Set sessionReference with the specified EntityRef value.
        sessionReference The EntityRef value to which sessionReference is to be set.
        The value of sessionReference can be anything allowed by the EntityRef constructor.

        """

        self._sessionReference = EntityRef(sessionReference)

    # ===> Attribute baseRangeMin

    _baseRangeMin = Length()

    def getBaseRangeMin(self):
        """
        Get baseRangeMin.
        return baseRangeMin as Length
        """

        # make sure it is a copy of Length
        return Length(self._baseRangeMin)

    def setBaseRangeMin(self, baseRangeMin):
        """
        Set baseRangeMin with the specified Length value.
        baseRangeMin The Length value to which baseRangeMin is to be set.
        The value of baseRangeMin can be anything allowed by the Length constructor.

        """

        self._baseRangeMin = Length(baseRangeMin)

    # ===> Attribute baseRangeMax

    _baseRangeMax = Length()

    def getBaseRangeMax(self):
        """
        Get baseRangeMax.
        return baseRangeMax as Length
        """

        # make sure it is a copy of Length
        return Length(self._baseRangeMax)

    def setBaseRangeMax(self, baseRangeMax):
        """
        Set baseRangeMax with the specified Length value.
        baseRangeMax The Length value to which baseRangeMax is to be set.
        The value of baseRangeMax can be anything allowed by the Length constructor.

        """

        self._baseRangeMax = Length(baseRangeMax)

    # ===> Attribute baseRmsMinor

    _baseRmsMinor = Length()

    def getBaseRmsMinor(self):
        """
        Get baseRmsMinor.
        return baseRmsMinor as Length
        """

        # make sure it is a copy of Length
        return Length(self._baseRmsMinor)

    def setBaseRmsMinor(self, baseRmsMinor):
        """
        Set baseRmsMinor with the specified Length value.
        baseRmsMinor The Length value to which baseRmsMinor is to be set.
        The value of baseRmsMinor can be anything allowed by the Length constructor.

        """

        self._baseRmsMinor = Length(baseRmsMinor)

    # ===> Attribute baseRmsMajor

    _baseRmsMajor = Length()

    def getBaseRmsMajor(self):
        """
        Get baseRmsMajor.
        return baseRmsMajor as Length
        """

        # make sure it is a copy of Length
        return Length(self._baseRmsMajor)

    def setBaseRmsMajor(self, baseRmsMajor):
        """
        Set baseRmsMajor with the specified Length value.
        baseRmsMajor The Length value to which baseRmsMajor is to be set.
        The value of baseRmsMajor can be anything allowed by the Length constructor.

        """

        self._baseRmsMajor = Length(baseRmsMajor)

    # ===> Attribute basePa

    _basePa = Angle()

    def getBasePa(self):
        """
        Get basePa.
        return basePa as Angle
        """

        # make sure it is a copy of Angle
        return Angle(self._basePa)

    def setBasePa(self, basePa):
        """
        Set basePa with the specified Angle value.
        basePa The Angle value to which basePa is to be set.
        The value of basePa can be anything allowed by the Angle constructor.

        """

        self._basePa = Angle(basePa)

    # ===> Attribute aborted

    _aborted = None

    def getAborted(self):
        """
        Get aborted.
        return aborted as bool
        """

        return self._aborted

    def setAborted(self, aborted):
        """
        Set aborted with the specified bool value.
        aborted The bool value to which aborted is to be set.


        """

        self._aborted = bool(aborted)

    # ===> Attribute numAntenna

    _numAntenna = 0

    def getNumAntenna(self):
        """
        Get numAntenna.
        return numAntenna as int
        """

        return self._numAntenna

    def setNumAntenna(self, numAntenna):
        """
        Set numAntenna with the specified int value.
        numAntenna The int value to which numAntenna is to be set.


        """

        self._numAntenna = int(numAntenna)

    # ===> Attribute releaseDate, which is optional
    _releaseDateExists = False

    _releaseDate = ArrayTime()

    def isReleaseDateExists(self):
        """
        The attribute releaseDate is optional. Return True if this attribute exists.
        return True if and only if the releaseDate attribute exists.
        """
        return self._releaseDateExists

    def getReleaseDate(self):
        """
        Get releaseDate, which is optional.
        return releaseDate as ArrayTime
        raises ValueError If releaseDate does not exist.
        """
        if not self._releaseDateExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + releaseDate
                + " attribute in table ExecBlock does not exist!"
            )

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._releaseDate)

    def setReleaseDate(self, releaseDate):
        """
        Set releaseDate with the specified ArrayTime value.
        releaseDate The ArrayTime value to which releaseDate is to be set.
        The value of releaseDate can be anything allowed by the ArrayTime constructor.

        """

        self._releaseDate = ArrayTime(releaseDate)

        self._releaseDateExists = True

    def clearReleaseDate(self):
        """
        Mark releaseDate, which is an optional field, as non-existent.
        """
        self._releaseDateExists = False

    # ===> Attribute schedulerMode, which is optional
    _schedulerModeExists = False

    _schedulerMode = None

    def isSchedulerModeExists(self):
        """
        The attribute schedulerMode is optional. Return True if this attribute exists.
        return True if and only if the schedulerMode attribute exists.
        """
        return self._schedulerModeExists

    def getSchedulerMode(self):
        """
        Get schedulerMode, which is optional.
        return schedulerMode as str
        raises ValueError If schedulerMode does not exist.
        """
        if not self._schedulerModeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + schedulerMode
                + " attribute in table ExecBlock does not exist!"
            )

        return self._schedulerMode

    def setSchedulerMode(self, schedulerMode):
        """
        Set schedulerMode with the specified str value.
        schedulerMode The str value to which schedulerMode is to be set.


        """

        self._schedulerMode = str(schedulerMode)

        self._schedulerModeExists = True

    def clearSchedulerMode(self):
        """
        Mark schedulerMode, which is an optional field, as non-existent.
        """
        self._schedulerModeExists = False

    # ===> Attribute siteAltitude, which is optional
    _siteAltitudeExists = False

    _siteAltitude = Length()

    def isSiteAltitudeExists(self):
        """
        The attribute siteAltitude is optional. Return True if this attribute exists.
        return True if and only if the siteAltitude attribute exists.
        """
        return self._siteAltitudeExists

    def getSiteAltitude(self):
        """
        Get siteAltitude, which is optional.
        return siteAltitude as Length
        raises ValueError If siteAltitude does not exist.
        """
        if not self._siteAltitudeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + siteAltitude
                + " attribute in table ExecBlock does not exist!"
            )

        # make sure it is a copy of Length
        return Length(self._siteAltitude)

    def setSiteAltitude(self, siteAltitude):
        """
        Set siteAltitude with the specified Length value.
        siteAltitude The Length value to which siteAltitude is to be set.
        The value of siteAltitude can be anything allowed by the Length constructor.

        """

        self._siteAltitude = Length(siteAltitude)

        self._siteAltitudeExists = True

    def clearSiteAltitude(self):
        """
        Mark siteAltitude, which is an optional field, as non-existent.
        """
        self._siteAltitudeExists = False

    # ===> Attribute siteLongitude, which is optional
    _siteLongitudeExists = False

    _siteLongitude = Angle()

    def isSiteLongitudeExists(self):
        """
        The attribute siteLongitude is optional. Return True if this attribute exists.
        return True if and only if the siteLongitude attribute exists.
        """
        return self._siteLongitudeExists

    def getSiteLongitude(self):
        """
        Get siteLongitude, which is optional.
        return siteLongitude as Angle
        raises ValueError If siteLongitude does not exist.
        """
        if not self._siteLongitudeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + siteLongitude
                + " attribute in table ExecBlock does not exist!"
            )

        # make sure it is a copy of Angle
        return Angle(self._siteLongitude)

    def setSiteLongitude(self, siteLongitude):
        """
        Set siteLongitude with the specified Angle value.
        siteLongitude The Angle value to which siteLongitude is to be set.
        The value of siteLongitude can be anything allowed by the Angle constructor.

        """

        self._siteLongitude = Angle(siteLongitude)

        self._siteLongitudeExists = True

    def clearSiteLongitude(self):
        """
        Mark siteLongitude, which is an optional field, as non-existent.
        """
        self._siteLongitudeExists = False

    # ===> Attribute siteLatitude, which is optional
    _siteLatitudeExists = False

    _siteLatitude = Angle()

    def isSiteLatitudeExists(self):
        """
        The attribute siteLatitude is optional. Return True if this attribute exists.
        return True if and only if the siteLatitude attribute exists.
        """
        return self._siteLatitudeExists

    def getSiteLatitude(self):
        """
        Get siteLatitude, which is optional.
        return siteLatitude as Angle
        raises ValueError If siteLatitude does not exist.
        """
        if not self._siteLatitudeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + siteLatitude
                + " attribute in table ExecBlock does not exist!"
            )

        # make sure it is a copy of Angle
        return Angle(self._siteLatitude)

    def setSiteLatitude(self, siteLatitude):
        """
        Set siteLatitude with the specified Angle value.
        siteLatitude The Angle value to which siteLatitude is to be set.
        The value of siteLatitude can be anything allowed by the Angle constructor.

        """

        self._siteLatitude = Angle(siteLatitude)

        self._siteLatitudeExists = True

    def clearSiteLatitude(self):
        """
        Mark siteLatitude, which is an optional field, as non-existent.
        """
        self._siteLatitudeExists = False

    # ===> Attribute observingScript, which is optional
    _observingScriptExists = False

    _observingScript = None

    def isObservingScriptExists(self):
        """
        The attribute observingScript is optional. Return True if this attribute exists.
        return True if and only if the observingScript attribute exists.
        """
        return self._observingScriptExists

    def getObservingScript(self):
        """
        Get observingScript, which is optional.
        return observingScript as str
        raises ValueError If observingScript does not exist.
        """
        if not self._observingScriptExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + observingScript
                + " attribute in table ExecBlock does not exist!"
            )

        return self._observingScript

    def setObservingScript(self, observingScript):
        """
        Set observingScript with the specified str value.
        observingScript The str value to which observingScript is to be set.


        """

        self._observingScript = str(observingScript)

        self._observingScriptExists = True

    def clearObservingScript(self):
        """
        Mark observingScript, which is an optional field, as non-existent.
        """
        self._observingScriptExists = False

    # ===> Attribute observingScriptUID, which is optional
    _observingScriptUIDExists = False

    _observingScriptUID = EntityRef()

    def isObservingScriptUIDExists(self):
        """
        The attribute observingScriptUID is optional. Return True if this attribute exists.
        return True if and only if the observingScriptUID attribute exists.
        """
        return self._observingScriptUIDExists

    def getObservingScriptUID(self):
        """
        Get observingScriptUID, which is optional.
        return observingScriptUID as EntityRef
        raises ValueError If observingScriptUID does not exist.
        """
        if not self._observingScriptUIDExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + observingScriptUID
                + " attribute in table ExecBlock does not exist!"
            )

        # make sure it is a copy of EntityRef
        return EntityRef(self._observingScriptUID)

    def setObservingScriptUID(self, observingScriptUID):
        """
        Set observingScriptUID with the specified EntityRef value.
        observingScriptUID The EntityRef value to which observingScriptUID is to be set.
        The value of observingScriptUID can be anything allowed by the EntityRef constructor.

        """

        self._observingScriptUID = EntityRef(observingScriptUID)

        self._observingScriptUIDExists = True

    def clearObservingScriptUID(self):
        """
        Mark observingScriptUID, which is an optional field, as non-existent.
        """
        self._observingScriptUIDExists = False

    # Extrinsic Table Attributes

    # ===> Attribute antennaId

    _antennaId = []  # this is a list of Tag []

    def getAntennaId(self):
        """
        Get antennaId.
        return antennaId as Tag []
        """

        return copy.deepcopy(self._antennaId)

    def setAntennaId(self, antennaId):
        """
        Set antennaId with the specified Tag []  value.
        antennaId The Tag []  value to which antennaId is to be set.
        The value of antennaId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(antennaId, list):
            raise ValueError("The value of antennaId must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(antennaId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of antennaId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not Parser.checkListType(antennaId, Tag):
                raise ValueError(
                    "type of the first value in antennaId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._antennaId = copy.deepcopy(antennaId)
        except Exception as exc:
            raise ValueError("Invalid antennaId : " + str(exc))

    # ===> Attribute sBSummaryId

    _sBSummaryId = Tag()

    def getSBSummaryId(self):
        """
        Get sBSummaryId.
        return sBSummaryId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._sBSummaryId)

    def setSBSummaryId(self, sBSummaryId):
        """
        Set sBSummaryId with the specified Tag value.
        sBSummaryId The Tag value to which sBSummaryId is to be set.
        The value of sBSummaryId can be anything allowed by the Tag constructor.

        """

        self._sBSummaryId = Tag(sBSummaryId)

    # ===> Attribute scaleId, which is optional
    _scaleIdExists = False

    _scaleId = Tag()

    def isScaleIdExists(self):
        """
        The attribute scaleId is optional. Return True if this attribute exists.
        return True if and only if the scaleId attribute exists.
        """
        return self._scaleIdExists

    def getScaleId(self):
        """
        Get scaleId, which is optional.
        return scaleId as Tag
        raises ValueError If scaleId does not exist.
        """
        if not self._scaleIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + scaleId
                + " attribute in table ExecBlock does not exist!"
            )

        # make sure it is a copy of Tag
        return Tag(self._scaleId)

    def setScaleId(self, scaleId):
        """
        Set scaleId with the specified Tag value.
        scaleId The Tag value to which scaleId is to be set.
        The value of scaleId can be anything allowed by the Tag constructor.

        """

        self._scaleId = Tag(scaleId)

        self._scaleIdExists = True

    def clearScaleId(self):
        """
        Mark scaleId, which is an optional field, as non-existent.
        """
        self._scaleIdExists = False

    # Links

    def setOneAntennaId(self, index, antennaId):
        """
        Set antennaId[index] with the specified Tag value.
        index The index in antennaId where to set the Tag value.
        antennaId The Tag value to which antennaId[index] is to be set.

        """

        self._antennaId[index] = Tag(antennaId)

    # ===> hasmany link from a row of ExecBlock table to many rows of Antenna table.

    def addAntennaId(self, id):
        """
        Append a Tag to antennaId
        id the Tag to be appended to antennaId
        """
        if isinstance(id, list):
            for thisValue in id:
                self._antennaId.append(Tag(thisValue))
        else:
            self._antennaId.append(Tag(id))

    def getOneAntennaId(self, i):
        """
        Returns the Tag stored in antennaId at position i.
        """
        return self._antennaId[i]

    def getAntennaUsingAntennaId(self, i):
        """
        Returns the AntennaRow linked to this row via the Tag stored in antennaId
        at position i.
        """

        return self._table.getContainer().getAntenna().getRowByKey(self._antennaId[i])

    def getAntennasUsingAntennaId(self):
        """
        Returns the array of AntennaRow linked to this row via the Tags stored in antennaId
        """
        result = []
        for thisItem in self._antennaId:
            result.append(self._table.getContainer().getAntenna().getRowByKey(thisItem))

        return result

    def getSBSummaryUsingSBSummaryId(self):
        """
        Returns the row in the SBSummary table having SBSummary.sBSummaryId == sBSummaryId

        """

        return self._table.getContainer().getSBSummary().getRowByKey(self._sBSummaryId)

    def getScaleUsingScaleId(self):
        """
        Returns the row in the Scale table having Scale.scaleId == scaleId

        Raises ValueError if the optional scaleId does not exist for this row.

        """

        if not self._scaleIdExists:
            raise ValueError("scaleId does not exist for this row.")

        return self._table.getContainer().getScale().getRowByKey(self._scaleId)

    # comparison methods

    def compareNoAutoInc(
        self,
        startTime,
        endTime,
        execBlockNum,
        execBlockUID,
        projectUID,
        configName,
        telescopeName,
        observerName,
        numObservingLog,
        observingLog,
        sessionReference,
        baseRangeMin,
        baseRangeMax,
        baseRmsMinor,
        baseRmsMajor,
        basePa,
        aborted,
        numAntenna,
        antennaId,
        sBSummaryId,
    ):
        """
        Compare each attribute except the autoincrementable one of this ExecBlockRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # startTime is a ArrayTime, compare using the equals method.
        if not self._startTime.equals(startTime):
            return False

        # endTime is a ArrayTime, compare using the equals method.
        if not self._endTime.equals(endTime):
            return False

        # execBlockNum is a int, compare using the == operator.
        if not (self._execBlockNum == execBlockNum):
            return False

        # execBlockUID is a EntityRef, compare using the equals method.
        if not self._execBlockUID.equals(execBlockUID):
            return False

        # projectUID is a EntityRef, compare using the equals method.
        if not self._projectUID.equals(projectUID):
            return False

        # configName is a str, compare using the == operator.
        if not (self._configName == configName):
            return False

        # telescopeName is a str, compare using the == operator.
        if not (self._telescopeName == telescopeName):
            return False

        # observerName is a str, compare using the == operator.
        if not (self._observerName == observerName):
            return False

        # numObservingLog is a int, compare using the == operator.
        if not (self._numObservingLog == numObservingLog):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._observingLog) != len(observingLog):
            return False
        for indx in range(len(observingLog)):

            # observingLog is a list of str, compare using == operator.
            if not (self._observingLog[indx] == observingLog[indx]):
                return False

        # sessionReference is a EntityRef, compare using the equals method.
        if not self._sessionReference.equals(sessionReference):
            return False

        # baseRangeMin is a Length, compare using the almostEquals method.
        if not self._baseRangeMin.almostEquals(
            baseRangeMin, self.getTable().getBaseRangeMinEqTolerance()
        ):
            return False

        # baseRangeMax is a Length, compare using the almostEquals method.
        if not self._baseRangeMax.almostEquals(
            baseRangeMax, self.getTable().getBaseRangeMaxEqTolerance()
        ):
            return False

        # baseRmsMinor is a Length, compare using the almostEquals method.
        if not self._baseRmsMinor.almostEquals(
            baseRmsMinor, self.getTable().getBaseRmsMinorEqTolerance()
        ):
            return False

        # baseRmsMajor is a Length, compare using the almostEquals method.
        if not self._baseRmsMajor.almostEquals(
            baseRmsMajor, self.getTable().getBaseRmsMajorEqTolerance()
        ):
            return False

        # basePa is a Angle, compare using the almostEquals method.
        if not self._basePa.almostEquals(
            basePa, self.getTable().getBasePaEqTolerance()
        ):
            return False

        # aborted is a bool, compare using the == operator.
        if not (self._aborted == aborted):
            return False

        # numAntenna is a int, compare using the == operator.
        if not (self._numAntenna == numAntenna):
            return False

        # antennaId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._antennaId) != len(antennaId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._antennaId)):
            if not (self._antennaId[indx].equals(antennaId[indx])):
                return False

        # sBSummaryId is a Tag, compare using the equals method.
        if not self._sBSummaryId.equals(sBSummaryId):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getStartTime(),
            otherRow.getEndTime(),
            otherRow.getExecBlockNum(),
            otherRow.getExecBlockUID(),
            otherRow.getProjectUID(),
            otherRow.getConfigName(),
            otherRow.getTelescopeName(),
            otherRow.getObserverName(),
            otherRow.getNumObservingLog(),
            otherRow.getObservingLog(),
            otherRow.getSessionReference(),
            otherRow.getBaseRangeMin(),
            otherRow.getBaseRangeMax(),
            otherRow.getBaseRmsMinor(),
            otherRow.getBaseRmsMajor(),
            otherRow.getBasePa(),
            otherRow.getAborted(),
            otherRow.getNumAntenna(),
            otherRow.getAntennaId(),
            otherRow.getSBSummaryId(),
        )

    def compareRequiredValue(
        self,
        startTime,
        endTime,
        execBlockNum,
        execBlockUID,
        projectUID,
        configName,
        telescopeName,
        observerName,
        numObservingLog,
        observingLog,
        sessionReference,
        baseRangeMin,
        baseRangeMax,
        baseRmsMinor,
        baseRmsMajor,
        basePa,
        aborted,
        numAntenna,
        antennaId,
        sBSummaryId,
    ):

        # startTime is a ArrayTime, compare using the equals method.
        if not self._startTime.equals(startTime):
            return False

        # endTime is a ArrayTime, compare using the equals method.
        if not self._endTime.equals(endTime):
            return False

        # execBlockNum is a int, compare using the == operator.
        if not (self._execBlockNum == execBlockNum):
            return False

        # execBlockUID is a EntityRef, compare using the equals method.
        if not self._execBlockUID.equals(execBlockUID):
            return False

        # projectUID is a EntityRef, compare using the equals method.
        if not self._projectUID.equals(projectUID):
            return False

        # configName is a str, compare using the == operator.
        if not (self._configName == configName):
            return False

        # telescopeName is a str, compare using the == operator.
        if not (self._telescopeName == telescopeName):
            return False

        # observerName is a str, compare using the == operator.
        if not (self._observerName == observerName):
            return False

        # numObservingLog is a int, compare using the == operator.
        if not (self._numObservingLog == numObservingLog):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._observingLog) != len(observingLog):
            return False
        for indx in range(len(observingLog)):

            # observingLog is a list of str, compare using == operator.
            if not (self._observingLog[indx] == observingLog[indx]):
                return False

        # sessionReference is a EntityRef, compare using the equals method.
        if not self._sessionReference.equals(sessionReference):
            return False

        # baseRangeMin is a Length, compare using the almostEquals method.
        if not self._baseRangeMin.almostEquals(
            baseRangeMin, self.getTable().getBaseRangeMinEqTolerance()
        ):
            return False

        # baseRangeMax is a Length, compare using the almostEquals method.
        if not self._baseRangeMax.almostEquals(
            baseRangeMax, self.getTable().getBaseRangeMaxEqTolerance()
        ):
            return False

        # baseRmsMinor is a Length, compare using the almostEquals method.
        if not self._baseRmsMinor.almostEquals(
            baseRmsMinor, self.getTable().getBaseRmsMinorEqTolerance()
        ):
            return False

        # baseRmsMajor is a Length, compare using the almostEquals method.
        if not self._baseRmsMajor.almostEquals(
            baseRmsMajor, self.getTable().getBaseRmsMajorEqTolerance()
        ):
            return False

        # basePa is a Angle, compare using the almostEquals method.
        if not self._basePa.almostEquals(
            basePa, self.getTable().getBasePaEqTolerance()
        ):
            return False

        # aborted is a bool, compare using the == operator.
        if not (self._aborted == aborted):
            return False

        # numAntenna is a int, compare using the == operator.
        if not (self._numAntenna == numAntenna):
            return False

        # antennaId is an extrinsic attribute which is a list of Tag.
        # the lists must have the same length
        if len(self._antennaId) != len(antennaId):
            return False

        # compare each element using the equals method.
        for indx in range(len(self._antennaId)):
            if not (self._antennaId[indx].equals(antennaId[indx])):
                return False

        # sBSummaryId is a Tag, compare using the equals method.
        if not self._sBSummaryId.equals(sBSummaryId):
            return False

        return True


# initialize the dictionary that maps fields to init methods
ExecBlockRow.initFromBinMethods()
