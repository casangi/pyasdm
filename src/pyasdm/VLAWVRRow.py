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
# File VLAWVRRow.py
#

import pyasdm.VLAWVRTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from xml.dom import minidom

import copy


class VLAWVRRow:
    """
    The VLAWVRRow class is a row of a VLAWVRTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a VLAWVRRow.
        When row is None, create an empty row attached to table, which must be a VLAWVRTable.
        When row is given, copy those values in to the new row. The row argument must be a VLAWVRRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.VLAWVRTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        if row is not None:
            if not isinstance(row, VLAWVRRow):
                raise ValueError("row must be a MainRow")

            self._antennaId = Tag(row._antennaId)

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._numChan = row._numChan

            # hiValues is a  list , make a deep copy
            self._hiValues = copy.deepcopy(row._hiValues)

            # loValues is a  list , make a deep copy
            self._loValues = copy.deepcopy(row._loValues)

            # by default set systematically chanFreqCenter's value to something not None

            if row._chanFreqCenterExists:

                # chanFreqCenter is a list, make a deep copy
                self.chanFreqCenter = copy.deepcopy(row.chanFreqCenter)

                self._chanFreqCenterExists = True

            # by default set systematically chanWidth's value to something not None

            if row._chanWidthExists:

                # chanWidth is a list, make a deep copy
                self.chanWidth = copy.deepcopy(row.chanWidth)

                self._chanWidthExists = True

            # by default set systematically wvrId's value to something not None

            if row._wvrIdExists:

                self._wvrId = row._wvrId

                self._wvrIdExists = True

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

        result += Parser.valueToXML("numChan", self._numChan)

        result += Parser.listValueToXML("hiValues", self._hiValues)

        result += Parser.listValueToXML("loValues", self._loValues)

        if self._chanFreqCenterExists:

            result += Parser.listExtendedValueToXML(
                "chanFreqCenter", self._chanFreqCenter
            )

        if self._chanWidthExists:

            result += Parser.listExtendedValueToXML("chanWidth", self._chanWidth)

        if self._wvrIdExists:

            result += Parser.valueToXML("wvrId", self._wvrId)

        # extrinsic attributes

        result += Parser.extendedValueToXML("antennaId", self._antennaId)

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
                "xmlrow is not a string or a minidom.Element", "VLAWVRTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "VLAWVRTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data)

        numChanNode = rowdom.getElementsByTagName("numChan")[0]

        self._numChan = int(numChanNode.firstChild.data)

        hiValuesNode = rowdom.getElementsByTagName("hiValues")[0]

        hiValuesStr = hiValuesNode.firstChild.data
        self._hiValues = Parser.stringListToLists(hiValuesStr, float, "VLAWVR")

        loValuesNode = rowdom.getElementsByTagName("loValues")[0]

        loValuesStr = loValuesNode.firstChild.data
        self._loValues = Parser.stringListToLists(loValuesStr, float, "VLAWVR")

        chanFreqCenterNode = rowdom.getElementsByTagName("chanFreqCenter")
        if len(chanFreqCenterNode) > 0:

            chanFreqCenterStr = chanFreqCenterNode[0].firstChild.data
            self._chanFreqCenter = Parser.stringListToLists(
                chanFreqCenterStr, Frequency, "VLAWVR"
            )

            self._chanFreqCenterExists = True

        chanWidthNode = rowdom.getElementsByTagName("chanWidth")
        if len(chanWidthNode) > 0:

            chanWidthStr = chanWidthNode[0].firstChild.data
            self._chanWidth = Parser.stringListToLists(
                chanWidthStr, Frequency, "VLAWVR"
            )

            self._chanWidthExists = True

        wvrIdNode = rowdom.getElementsByTagName("wvrId")
        if len(wvrIdNode) > 0:

            self._wvrId = str(wvrIdNode[0].firstChild.data)

            self._wvrIdExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        self._antennaId = Tag(antennaIdNode.firstChild.data)

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

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

    # ===> Attribute numChan

    _numChan = 0

    def getNumChan(self):
        """
        Get numChan.
        return numChan as int
        """

        return self._numChan

    def setNumChan(self, numChan):
        """
        Set numChan with the specified int value.
        numChan The int value to which numChan is to be set.


        """

        self._numChan = int(numChan)

    # ===> Attribute hiValues

    _hiValues = None  # this is a 1D list of float

    def getHiValues(self):
        """
        Get hiValues.
        return hiValues as float []
        """

        return copy.deepcopy(self._hiValues)

    def setHiValues(self, hiValues):
        """
        Set hiValues with the specified float []  value.
        hiValues The float []  value to which hiValues is to be set.


        """

        # value must be a list
        if not isinstance(hiValues, list):
            raise ValueError("The value of hiValues must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(hiValues)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of hiValues is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(hiValues, float):
                raise ValueError(
                    "type of the first value in hiValues is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._hiValues = copy.deepcopy(hiValues)
        except Exception as exc:
            raise ValueError("Invalid hiValues : " + str(exc))

    # ===> Attribute loValues

    _loValues = None  # this is a 1D list of float

    def getLoValues(self):
        """
        Get loValues.
        return loValues as float []
        """

        return copy.deepcopy(self._loValues)

    def setLoValues(self, loValues):
        """
        Set loValues with the specified float []  value.
        loValues The float []  value to which loValues is to be set.


        """

        # value must be a list
        if not isinstance(loValues, list):
            raise ValueError("The value of loValues must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(loValues)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of loValues is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(loValues, float):
                raise ValueError(
                    "type of the first value in loValues is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._loValues = copy.deepcopy(loValues)
        except Exception as exc:
            raise ValueError("Invalid loValues : " + str(exc))

    # ===> Attribute chanFreqCenter, which is optional
    _chanFreqCenterExists = False

    _chanFreqCenter = None  # this is a 1D list of Frequency

    def isChanFreqCenterExists(self):
        """
        The attribute chanFreqCenter is optional. Return True if this attribute exists.
        return True if and only if the chanFreqCenter attribute exists.
        """
        return self._chanFreqCenterExists

    def getChanFreqCenter(self):
        """
        Get chanFreqCenter, which is optional.
        return chanFreqCenter as Frequency []
        raises ValueError If chanFreqCenter does not exist.
        """
        if not self._chanFreqCenterExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + chanFreqCenter
                + " attribute in table VLAWVR does not exist!"
            )

        return copy.deepcopy(self._chanFreqCenter)

    def setChanFreqCenter(self, chanFreqCenter):
        """
        Set chanFreqCenter with the specified Frequency []  value.
        chanFreqCenter The Frequency []  value to which chanFreqCenter is to be set.
        The value of chanFreqCenter can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(chanFreqCenter, list):
            raise ValueError("The value of chanFreqCenter must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(chanFreqCenter)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of chanFreqCenter is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(chanFreqCenter, Frequency):
                raise ValueError(
                    "type of the first value in chanFreqCenter is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._chanFreqCenter = copy.deepcopy(chanFreqCenter)
        except Exception as exc:
            raise ValueError("Invalid chanFreqCenter : " + str(exc))

        self._chanFreqCenterExists = True

    def clearChanFreqCenter(self):
        """
        Mark chanFreqCenter, which is an optional field, as non-existent.
        """
        self._chanFreqCenterExists = False

    # ===> Attribute chanWidth, which is optional
    _chanWidthExists = False

    _chanWidth = None  # this is a 1D list of Frequency

    def isChanWidthExists(self):
        """
        The attribute chanWidth is optional. Return True if this attribute exists.
        return True if and only if the chanWidth attribute exists.
        """
        return self._chanWidthExists

    def getChanWidth(self):
        """
        Get chanWidth, which is optional.
        return chanWidth as Frequency []
        raises ValueError If chanWidth does not exist.
        """
        if not self._chanWidthExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + chanWidth
                + " attribute in table VLAWVR does not exist!"
            )

        return copy.deepcopy(self._chanWidth)

    def setChanWidth(self, chanWidth):
        """
        Set chanWidth with the specified Frequency []  value.
        chanWidth The Frequency []  value to which chanWidth is to be set.
        The value of chanWidth can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(chanWidth, list):
            raise ValueError("The value of chanWidth must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(chanWidth)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of chanWidth is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(chanWidth, Frequency):
                raise ValueError(
                    "type of the first value in chanWidth is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._chanWidth = copy.deepcopy(chanWidth)
        except Exception as exc:
            raise ValueError("Invalid chanWidth : " + str(exc))

        self._chanWidthExists = True

    def clearChanWidth(self):
        """
        Mark chanWidth, which is an optional field, as non-existent.
        """
        self._chanWidthExists = False

    # ===> Attribute wvrId, which is optional
    _wvrIdExists = False

    _wvrId = None

    def isWvrIdExists(self):
        """
        The attribute wvrId is optional. Return True if this attribute exists.
        return True if and only if the wvrId attribute exists.
        """
        return self._wvrIdExists

    def getWvrId(self):
        """
        Get wvrId, which is optional.
        return wvrId as str
        raises ValueError If wvrId does not exist.
        """
        if not self._wvrIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + wvrId
                + " attribute in table VLAWVR does not exist!"
            )

        return self._wvrId

    def setWvrId(self, wvrId):
        """
        Set wvrId with the specified str value.
        wvrId The str value to which wvrId is to be set.


        """

        self._wvrId = str(wvrId)

        self._wvrIdExists = True

    def clearWvrId(self):
        """
        Mark wvrId, which is an optional field, as non-existent.
        """
        self._wvrIdExists = False

    # Extrinsic Table Attributes

    # ===> Attribute antennaId

    _antennaId = Tag()

    def getAntennaId(self):
        """
        Get antennaId.
        return antennaId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._antennaId)

    def setAntennaId(self, antennaId):
        """
        Set antennaId with the specified Tag value.
        antennaId The Tag value to which antennaId is to be set.
        The value of antennaId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the antennaId field, which is part of the key, after this row has been added to this table."
            )

        self._antennaId = Tag(antennaId)

    # Links

    def getAntennaUsingAntennaId(self):
        """
        Returns the row in the Antenna table having Antenna.antennaId == antennaId

        """

        return self._table.getContainer().getAntenna().getRowByKey(self._antennaId)

    # comparison methods

    def compareNoAutoInc(self, antennaId, timeInterval, numChan, hiValues, loValues):
        """
        Compare each attribute except the autoincrementable one of this VLAWVRRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaId is a Tag, compare using the equals method.
        if not self._antennaId.equals(antennaId):
            return False

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # numChan is a int, compare using the == operator.
        if not (self._numChan == numChan):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._hiValues) != len(hiValues):
            return False
        for indx in range(len(hiValues)):

            # hiValues is a list of float, compare using == operator.
            if not (self._hiValues[indx] == hiValues[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._loValues) != len(loValues):
            return False
        for indx in range(len(loValues)):

            # loValues is a list of float, compare using == operator.
            if not (self._loValues[indx] == loValues[indx]):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumChan(), otherRow.getHiValues(), otherRow.getLoValues()
        )

    def compareRequiredValue(self, numChan, hiValues, loValues):

        # numChan is a int, compare using the == operator.
        if not (self._numChan == numChan):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._hiValues) != len(hiValues):
            return False
        for indx in range(len(hiValues)):

            # hiValues is a list of float, compare using == operator.
            if not (self._hiValues[indx] == hiValues[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._loValues) != len(loValues):
            return False
        for indx in range(len(loValues)):

            # loValues is a list of float, compare using == operator.
            if not (self._loValues[indx] == loValues[indx]):
                return False

        return True
