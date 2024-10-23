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
# File MainRow.py

# this will eventually be generated code

import pyasdm.MainTable

from pyasdm.enumerations.TimeSampling import TimeSampling
from pyasdm.types.ArrayTime import ArrayTime
from pyasdm.types.Interval import Interval
from pyasdm.types.Tag import Tag
from pyasdm.types.EntityRef import EntityRef

from xml.dom import minidom

class MainRow:
    """
    The MainRow class is a row of a MainTable.
    """

    # every row belongs to a table
    _table = None

    # a row has not been added to its table until this is true
    _hasBeenAdded = False

    # attributes with their default initializations
    _time = ArrayTime()
    _numAntenna = 0
    _timeSampling = TimeSampling.from_int(0)
    _interval = Interval()
    _numIntegration = 0
    _scanNumber = 0
    _subscanNumber = 0
    _dataSize = 0
    _dataUID = EntityRef()
    _configDescriptionId = Tag()
    _execBlockId = Tag()
    _fieldId = Tag()
    _stateId = []   # this is a list of Tags that should have length _numAntenna

    def __init__(self, table, row = None):
        # When row is None, create an empty row attached to table, which must be a MainTable
        # when row is give, copy those values to this row, row must be a MainRow if given
        # in both cases the row is not yet added to the given table

        if not isinstance(table, pyasdm.MainTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # the default initialization is present in the class description

        if row is not None:
            if not isinstance(row, MainRow):
                raise ValueError("row must be a MainRow")

            self._time = ArrayTime(row._time)
            self._configDescriptionId = Tag(row._configDescriptionId)
            self._fieldId = Tag(row._fieldId)
            self._numAntenna = row._numAntenna
            if row._timeSampling == None:
                self._timeSampling = TimeSampling.from_int(0)
            else:
                self._timeSampling = TimeSampling(row._timeSampling)
            self._interval = Interval(row._interval)
            self._numIntegration = row._numIntegration
            self._scanNumber = row._scanNumber
            self._subscanNumber = row._subscanNumber
            self._dataSize = row._dataSize
            self._dataUID = EntityRef(row._dataUID)
            for i in range(len(row._stateId)):
                self._stateId.append(Tag(row._stateId[i]))
            self._execBlockId = Tag(row._execBlockId)

    def isAdded(self):
        """
        Has this row been added to it's table?
        """
        return self._hasBeenAdded

    def getTable(self):
        """
        Return the table to which this row belongs.
        """
        return self._table

    @staticmethod
    def _nameStringToXML(name, strval):
        """
        Internal method to produce and XML using the name and a string value.
        <name>strval</name>
        The returned value has a trailing space so that it can be used to add
        these strings together without worrying about spacing.
        """
        return ("<%s> %s </%s> " % (name,strval,name))

    def toXML(self):
        """
        Return this row in the form of an XML string.
        """
        result = ""

        result += "<row> \n"

        result += MainRow._nameStringToXML("time",self._time.toString())
        result += MainRow._nameStringToXML("numAntenna",str(self._numAntenna))
        result += MainRow._nameStringToXML("timeSampling",TimeSampling.name(self._timeSampling))
        result += MainRow._nameStringToXML("interval",self._interval.toString())
        result += MainRow._nameStringToXML("numIntegration",str(self._numIntegration))
        result += MainRow._nameStringToXML("scanNumber",str(self._scanNumber))
        result += MainRow._nameStringToXML("subscanNumber",str(self._subscanNumber))
        result += MainRow._nameStringToXML("dataSize",str(self._dataSize))
        result += MainRow._nameStringToXML("dataUID",self._dataUID.toString())
        result += MainRow._nameStringToXML("configDescriptionId",self._configDescriptionId.toString())
        result += MainRow._nameStringToXML("execBlockId",self._execBlockId.toString())
        result += MainRow._nameStringToXML("fieldId",self._fieldId.toString())

        # stateId is a list of Tags
        result += "<stateId> "
        # 1 dimension and length of the list
        result += "1 %s " % len(self._stateId)
        for thisStateId in self._stateId:
            result += thisStateId.toString() + " "
        result += " </stateId> "

        result += "</row>\n"
        return(result)        
        
    def setFromXML(self,xmlrow):
        """
        Fill the values of this row from an XML string
        that was produced by the toXML method.
        If xmlrow is an minidom.Element with a nodeName of row then
        it will be used as is. Anything else that is not a string
        is an error
        """
        rowdom = None
        if isinstance(xmlrow, str):
            xmldom = minidom.parseString(xmlrow)
            rowdom = xmldom.firstChild
        elif isinstance(xmlrow, minidom.Element):
            rowdom = xmlrow
        else:
            raise ValueError("xmlrow is not a string or a minidom.Element")

        if rowdom.nodeName != "row":
            raise ValueError("the argument is not a row")

        # look for the possible attributes, set to default if not found

        # required attributes - if they are missing then this will raise an excception

        # time
        timeNode = rowdom.getElementsByTagName("time")[0]
        self._time = ArrayTime(timeNode.firstChild.data)

        # numAntenna
        numAntennaNode = rowdom.getElementsByTagName("numAntenna")[0]
        self._numAntenna = int(numAntennaNode.firstChild.data)

        # timeSampling
        timeSamplingNode = rowdom.getElementsByTagName("timeSampling")[0]
        self._timeSampling = TimeSampling.newTimeSampling(timeSamplingNode.firstChild.data)

        # interval
        intervalNode = rowdom.getElementsByTagName("interval")[0]
        self._interval = Interval(intervalNode.firstChild.data)

        # numIntegration
        numIntegrationNode = rowdom.getElementsByTagName("numIntegration")[0]
        self._numIntegration = int(numIntegrationNode.firstChild.data)

        # scanNumber
        scanNumberNode = rowdom.getElementsByTagName("scanNumber")[0]
        self._scanNumber = int(scanNumberNode.firstChild.data)
       
        # subscanNumber
        subscanNumberNode = rowdom.getElementsByTagName("subscanNumber")[0]
        self._subscanNumber = int(subscanNumberNode.firstChild.data)
       
        # dataSize
        dataSizeNode = rowdom.getElementsByTagName("dataSize")[0]
        self._dataSize = int(dataSizeNode.firstChild.data)

        # dataUID
        dataUIDNode = rowdom.getElementsByTagName("dataUID")[0]
        self._dataUID = EntityRef(dataUIDNode.toxml())

        # the second argument of Parser.getTag is there so that the exceptions here can indicate the table name
        
        # configDescriptionId
        configDescriptionIdNode = rowdom.getElementsByTagName("configDescriptionId")[0]
        self._configDescriptionId = Tag.parseTag(configDescriptionIdNode.firstChild.data)
        
        # execBlockId
        execBlockIdNode = rowdom.getElementsByTagName("execBlockId")[0]
        self._execBlockId = Tag.parseTag(execBlockIdNode.firstChild.data)

        # fieldId
        fieldIdNode = rowdom.getElementsByTagName("fieldId")[0]
        self._fieldId = Tag.parseTag(fieldIdNode.firstChild.data)

        # stateId
        stateIdNode = rowdom.getElementsByTagName("stateId")[0]
        stateIdStr = stateIdNode.firstChild.data
        stateIdList = stateIdStr.split()
        # first 2 elements are the dimension, which must be 1, and the number of elements
        if len(stateIdList) < 2:
            raise(ValueError("invalid stateId value"))
        if stateIdList[0] != "1":
            raise ValueError("stateId does not start with a '1'")
        nState = int(stateIdList[1])
        if ((nState+2) > len(stateIdList)):
            raise ValueError("not enough stateId values found in stateId attribute field")
        self._stateId = []
        for i in range(nState):
            self._stateId.append(Tag.parseTag(stateIdList[i+2]))

    def toBin(self):
        print("not yet implemented")

    # getters and setters for the attributes

    # intrisic table attributes

    # time
    
    def getTime(self):
        """
        Get time as an ArrayTime
        """
        # make sure it's a copy of the ArrayTime
        return ArrayTime(self._time)

    def setTime(self, time):
        """
        set time with the specified ArrayTime value (value can be anything allowed by the ArrayTime constructor)
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
            raise ValueError("Attempt to change the time field, which is part of the key, after this row has been added to this table.")

        self._time = ArrayTime(time)

    # numAntenna
    
    def getNumAntenna(self):
        """
        Get numAntenna as int
        """
        return self._numAntenna

    def setNumAntenna(self, numAntenna):
        """
        set numAntenna with the specified integer value, numAntenna is converted to an int, possibly truncating the value
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
            # Java code suppresses this exception at all times, only the key attributes trigger this
            if (False):
                raise ValueError("Attempt to change the numAntenna field, which is a mandatory attribute, after this row has been added to this table.")

        self._numAntenna = int(numAntenna)

    def getTimeSampling(self):
        """
        Get timeSampling as TimeSampling
        """
        return self._timeSampling

    def setTimeSampling(self, timeSampling):
        """
        set timeSampling with the specified TimeSampling value (value can be anything allowed by the TimeSampling constructor)
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
            # Java code suppresses this exception at all times, only the key attributes trigger this
            if (False):
                raise ValueError("Attempt to change the timeSampling field, which is a mandatory attribute, after this row has been added to this table.")

        self._timeSampling = TimeSampling(timeSampling)

    # interval
    
    def getInterval(self):
        """
        Get interval as an Interval
        """
        # make sure it's a copy of the Interval
        return Interval(self._interval)

    def setInterval(self, interval):
        """
        set interval with the specified Interval value (value can be anything allowed by the Interval constructor)
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
            # Java code suppresses this exception at all times, only the key attributes trigger this
            if (False):
                raise ValueError("Attempt to change the interval field, which is part of the key, after this row has been added to this table.")

        self._interval = Interval(interval)


    # numIntegration
    
    def getNumIntegration(self):
        """
        Get numIntegration as int
        """
        return self._numIntegration

    def setNumIntegration(self, numIntegration):
        """
        set numIntegration with the specified integer value, numIntegration is converted to an int, possibly truncating the value
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
            # Java code suppresses this exception at all times, only the key attributes trigger this
            if (False):
                raise ValueError("Attempt to change the numIntegration field, which is a mandatory attribute, after this row has been added to this table.")

        self._numIntegration = int(numIntegration)
        
    # scanNumber
    
    def getScanNumber(self):
        """
        Get scanNumber as int
        """
        return self._scanNumber

    def setScanNumber(self, scanNumber):
        """
        set scanNumber with the specified integer value, scanNumber is converted to an int, possibly truncating the value
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
            # Java code suppresses this exception at all times, only the key attributes trigger this
            if (False):
                raise ValueError("Attempt to change the scanNumber field, which is a mandatory attribute, after this row has been added to this table.")

        self._scanNumber = int(scanNumber)

    # subscanNumber
    
    def getSubscanNumber(self):
        """
        Get subscanNumber as int
        """
        return self._subscanNumber

    def setSubscanNumber(self, subscanNumber):
        """
        set subscanNumber with the specified integer value, subscanNumber is converted to an int, possibly truncating the value
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
            # Java code suppresses this exception at all times, only the key attributes trigger this
            if (False):
                raise ValueError("Attempt to change the subscanNumber field, which is a mandatory attribute, after this row has been added to this table.")

        self._subscanNumber = int(subscanNumber)

    # dataSize
    
    def getDataSize(self):
        """
        Get dataSize as int
        """
        return self._dataSize

    def setDataSize(self, dataSize):
        """
        set dataSize with the specified integer value, dataSize is converted to an int, possibly truncating the value
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
            # Java code suppresses this exception at all times, only the key attributes trigger this
            if (False):
                raise ValueError("Attempt to change the dataSize field, which is a mandatory attribute, after this row has been added to this table.")

        self._dataSize = int(dataSize)

    # dataUID
    
    def getDataUID(self):
        """
        Get dataUID as EntityRef
        """
        return self._dataUID

    def setDataUID(self, dataUID):
        """
        set dataUID with the specified EntityRef value (dataUID can be any argument valid for the EntityRef constructor)
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
            # Java code suppresses this exception at all times, only the key attributes trigger this
            if (False):
                raise ValueError("Attempt to change the dataUID field, which is a mandatory attribute, after this row has been added to this table.")

        self._dataUID = EntityRef(dataUID)

    # configDescriptionId

    def getConfigDescriptionId(self):
        """
        Get configDescriptionId as Tag
        """
        # make sure it's a copy of the Tag
        return Tag(self._configDescriptionId)

    def setConfigDescriptionId(self, configDescriptionId):
        """
        set configDescriptionId with the specified Tag value (value can be anything allowed by the Tag constructor)
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
            raise ValueError("Attempt to change the configDescriptionId field, which is part of the key, after this row has been added to this table.")

        self._configDescriptionId = Tag(configDescriptionId)

    # execBlockId

    def getExecBlockId(self):
        """
        Get execBlockId as Tag
        """
        # make sure it's a copy of the Tag
        return Tag(self._execBlockId)

    def setExecBlockId(self, execBlockId):
        """
        set execBlockId with the specified Tag value (value can be anything allowed by the Tag constructor)
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
           # Java code suppresses this exception at all times, only the key attributes trigger this
            if (False):
                raise ValueError("Attempt to change the execBlockId field, which is a mandatory attribute, after this row has been added to this table.")

        self._execBlockId = Tag(execBlockId)

        
    # fieldId

    def getFieldId(self):
        """
        Get fieldId as Tag
        """
        # make sure it's a copy of the Tag
        return Tag(self._fieldId)

    def setFieldId(self, fieldId):
        """
        set fieldId with the specified Tag value (value can be anything allowed by the Tag constructor)
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
            raise ValueError("Attempt to change the fieldId field, which is part of the key, after this row has been added to this table.")

        self._fieldId = Tag(fieldId)

        
    # stateId
    def getStateId(self, i=None):
        """
        Get stateId as a list of Tag objects
        When i is specified, return just that element as a Tag
        """
        result = None
        if i is not None:
            result = Tag(self._stateId[i])
        else:
            result = []
            for i in range(len(self._stateId)):
                result.append(Tag(self._stateId[i]))
                
        return result

    def setStateId(self, stateId):
        """
        set stateId with the specified list of Tag values (each value can be anything allowed by the Tag constructor)
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
           # Java code suppresses this exception at all times, only the key attributes trigger this
            if (False):
                raise ValueError("Attempt to change the stateId, which is a mandatory attribute, after this row has been added to this table.")

        self._stateId = []
        for i in range(len(stateId)):
            self._stateId.append(Tag(stateId[i]))

    # links
    def getConfigDescriptionUsingConfigDescriptionId(self):
        """
        Returns the row in hte ConfigDescription table having ConfigDescription.configDescriptionId == configDescriptionId
        """
        return self._table.getContainer().getConfigDescription().getRowByKey(self._configDescriptionId)

    def getFieldUsingFieldId(self):
        """
        Returns the row in the Field table having Field.fieldId == fieldId
        """
        return self._table.getContainer().getField().getRowByKey(self._fieldId)

    # set a specified stateId
    def setStateid(self, index, stateId):
        """
        Set stateId[i] with the specified stateId value, which must be interpreted as a Tag by the Tag constructor.
        stateId[i] must already exist
        Throws an exception if an attempt is made to change this field after it has been added to the table.
        """
        if (self._hasBeenAdded):
           # Java code suppresses this exception at all times, only the key attributes trigger this
            if (False):
                raise ValueError("Attempt to change the stateId field, which is a mandatory attribute, after this row has been added to this table.")

        self._stateId[index] = Tag(stateId)

    # hasmany link from a row of Main table to many rows of State table.

    def addStateId(self,stateId):
        """
        Append stateId as a Tag or list of Tags to the stateId
        """
        if isinstance(stateId, list):
            for i in range(len(stateId)):
                self._stateId.append(Tag(stateId[i]))
        else:
            self._stateId.append(Tag(stateId))

    def getStateUsingStateId(self, i):
        """
        Returns the StateRow linked to this row via the Tag stored in the indicated stateId
        """
        return self._table.getContainer().getState().getRowByKey(self._stateId[i])

    def getStatesUsingStateId(self):
        """
        Returns the array of StateRows linked to this row via the Tags stored in stateId
        """
        stateRows = []
        for thisStateId in self._stateId:
            stateRows.append(self._table.getContainer().getState().getRowByKey(thisStateId))

    def getExecBlockUsingExecBlockId(self):
        """
        Returns the row in the ExecBlock table having ExecBlock.execBlockId == execBlockId
        """
        return self._table.getContainer().getExecBlock().getRowByKey(self._execBlockId)

    # comparison methods
    def compareNoAutoInc(self, time, configDescriptionId, fieldId, numAntenna, TimeSampling,
                         interval, numIntegration, scanNumber, subscanNumber, dataSize,
                         dataUID, stateId, execBlockId):
        """
        Compare each attribute except the autoincrementable one of this MainRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # time is a ArrayTime, compare using the equals method
        if (not (this._time.equals(time))):
            return False

        # configDescriptionId is a Tag, compare using the equals method.
        if (not (this._configDescriptionId.equals(configDescriptionId))):
            return False

        # fieldId is a Tag, compare using the equals method.
        if (not (this._fieldid.equals(fieldId))):
            return False

        # numAntenna is a int, compare using the == operator.
        if (not (this._numAntenna == numAntenna)):
            return False

        # timeSampling is aTimeSampling, compare using the == on the getValue() member
        if (not (this._timeSampling.getValue() == timeSampling.getValue())):
            return False

        # interval is a Interval, compare using the equals method.
        if (not (this._interval.equals(interval))):
            return False

        # numIntegration is a int, compare using the == operator
        if (not (this._numIntegration == numIntegration)):
            return False

        # scanNumber is a int, compare using the == operator
        if (not (this._scanNumber == scanNumber)):
            return False

        # subscanNumber is a int, compare using the == operator
        if (not (this._subscanNumber == subscanNumber)):
            return False

        # dataSize is a int, compare using the == operator
        if (not (this._dataSize == dataSize)):
            return False

        # dataUID is a EntityRef, compare using the equals method
        if (not (this._dataUID.equals(dataUID))):
            return False

        # stateId is an extrinsic attribute which is a list of Tag
        # the lists must have the same length
        if (not (len(this._stateId) == len(stateId))):
            return False

        # compare each element using the equals method
        for indx in range(len(this._stateId)):
            if (not (this._stateId[indx].equals(stateId[indx]))):
                return False

        # execBlockId is a Tag, compare using the equals method.
        if (not (this._execBlockId.equals(execBlockId))):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        return compareRequiredValue(
            otherRow.getNumAntenna(),
            otherRow.getTimeSampling(),
            otherRow.getInterval(),
            otherRow.getNumIntegration(),
            otherRow.getScanNumber(),
            otherRow.getSubscanNumber(),
            otherRow.getDataSize(),
            otherRow.getStateId(),
            otherRow.getExecBlock()
            )

    def compareRequiredValue(self, numAntenna, timeSampling, interval, numIntegration,
                             scanNumber, subscanNumber, dataSize, dataUID, stateId, execBlockId):

        # numAntenna is a int, compare using the == operator
        if (not (this._numAntenna == numAntenna)):
            return False

        # timeSampling is a TimeSampling, compare using the == on the getValue() member.
        if (not (this._timeSampling.getValue() == timeSampling.getValue())):
            return False

        # interval is a Interval, compare using the equals method
        if (not (this._interval.equals(interval))):
            return False

        # numIntegration is a int, compare using the == operator
        if (not (this._numIntegration == numIntegration)):
            return False

        # scanNumber is a int, compare using the == operator
        if (not (this._scanNumber == scanNumber)):
            return False

        # subscanNumber is a int, compare using the == operator
        if (not (this._subscanNumber == subscanNumber)):
            return False

        # dataSize is a int, compare using the == operator
        if (not (this._dataSize == dataSize)):
            return False

        # dataUID is a EntityRef, compare using the equals method
        if (not (this._dataUID.equals(dataUID))):
            return False

        # stateId is an extrinsic attribute which is a list of Tag
        # the lists must have the same length
        if (not (len(this._stateId) == len(stateId))):
            return False
        # compare each element using the equals method
        for indx in range(len(this._stateId)):
            if (not (this._stateId[indx].equals(stateId[indx]))):
                return False

        # execBlock is a Tag, compare using the equals method.
        if (not (this._execBlockId.equals(execBlockId))):
            return False

        return True


        
