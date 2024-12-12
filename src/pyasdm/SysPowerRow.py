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
# File SysPowerRow.py
#

import pyasdm.SysPowerTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from xml.dom import minidom

import copy


class SysPowerRow:
    """
    The SysPowerRow class is a row of a SysPowerTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a SysPowerRow.
        When row is None, create an empty row attached to table, which must be a SysPowerTable.
        When row is given, copy those values in to the new row. The row argument must be a SysPowerRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.SysPowerTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._timeInterval = ArrayTimeInterval()

        self._numReceptor = 0

        self._switchedPowerDifferenceExists = False

        self._switchedPowerDifference = []  # this is a list of float []

        self._switchedPowerSumExists = False

        self._switchedPowerSum = []  # this is a list of float []

        self._requantizerGainExists = False

        self._requantizerGain = []  # this is a list of float []

        # extrinsic attributes

        self._antennaId = Tag()

        self._feedId = 0

        self._spectralWindowId = Tag()

        if row is not None:
            if not isinstance(row, SysPowerRow):
                raise ValueError("row must be a MainRow")

            # copy constructor

            self._antennaId = Tag(row._antennaId)

            self._spectralWindowId = Tag(row._spectralWindowId)

            self._feedId = row._feedId

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._numReceptor = row._numReceptor

            # by default set systematically switchedPowerDifference's value to something not None

            if row._switchedPowerDifferenceExists:

                # switchedPowerDifference is a list, make a deep copy
                self.switchedPowerDifference = copy.deepcopy(
                    row.switchedPowerDifference
                )

                self._switchedPowerDifferenceExists = True

            # by default set systematically switchedPowerSum's value to something not None

            if row._switchedPowerSumExists:

                # switchedPowerSum is a list, make a deep copy
                self.switchedPowerSum = copy.deepcopy(row.switchedPowerSum)

                self._switchedPowerSumExists = True

            # by default set systematically requantizerGain's value to something not None

            if row._requantizerGainExists:

                # requantizerGain is a list, make a deep copy
                self.requantizerGain = copy.deepcopy(row.requantizerGain)

                self._requantizerGainExists = True

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

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        if self._switchedPowerDifferenceExists:

            result += Parser.listValueToXML(
                "switchedPowerDifference", self._switchedPowerDifference
            )

        if self._switchedPowerSumExists:

            result += Parser.listValueToXML("switchedPowerSum", self._switchedPowerSum)

        if self._requantizerGainExists:

            result += Parser.listValueToXML("requantizerGain", self._requantizerGain)

        # extrinsic attributes

        result += Parser.extendedValueToXML("antennaId", self._antennaId)

        result += Parser.valueToXML("feedId", self._feedId)

        result += Parser.extendedValueToXML("spectralWindowId", self._spectralWindowId)

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
                "xmlrow is not a string or a minidom.Element", "SysPowerTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "SysPowerTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        switchedPowerDifferenceNode = rowdom.getElementsByTagName(
            "switchedPowerDifference"
        )
        if len(switchedPowerDifferenceNode) > 0:

            switchedPowerDifferenceStr = switchedPowerDifferenceNode[
                0
            ].firstChild.data.strip()

            self._switchedPowerDifference = Parser.stringListToLists(
                switchedPowerDifferenceStr, float, "SysPower", False
            )

            self._switchedPowerDifferenceExists = True

        switchedPowerSumNode = rowdom.getElementsByTagName("switchedPowerSum")
        if len(switchedPowerSumNode) > 0:

            switchedPowerSumStr = switchedPowerSumNode[0].firstChild.data.strip()

            self._switchedPowerSum = Parser.stringListToLists(
                switchedPowerSumStr, float, "SysPower", False
            )

            self._switchedPowerSumExists = True

        requantizerGainNode = rowdom.getElementsByTagName("requantizerGain")
        if len(requantizerGainNode) > 0:

            requantizerGainStr = requantizerGainNode[0].firstChild.data.strip()

            self._requantizerGain = Parser.stringListToLists(
                requantizerGainStr, float, "SysPower", False
            )

            self._requantizerGainExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        self._antennaId = Tag(antennaIdNode.firstChild.data.strip())

        feedIdNode = rowdom.getElementsByTagName("feedId")[0]

        self._feedId = int(feedIdNode.firstChild.data.strip())

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")[0]

        self._spectralWindowId = Tag(spectralWindowIdNode.firstChild.data.strip())

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

    # ===> Attribute numReceptor

    _numReceptor = 0

    def getNumReceptor(self):
        """
        Get numReceptor.
        return numReceptor as int
        """

        return self._numReceptor

    def setNumReceptor(self, numReceptor):
        """
        Set numReceptor with the specified int value.
        numReceptor The int value to which numReceptor is to be set.


        """

        self._numReceptor = int(numReceptor)

    # ===> Attribute switchedPowerDifference, which is optional
    _switchedPowerDifferenceExists = False

    _switchedPowerDifference = None  # this is a 1D list of float

    def isSwitchedPowerDifferenceExists(self):
        """
        The attribute switchedPowerDifference is optional. Return True if this attribute exists.
        return True if and only if the switchedPowerDifference attribute exists.
        """
        return self._switchedPowerDifferenceExists

    def getSwitchedPowerDifference(self):
        """
        Get switchedPowerDifference, which is optional.
        return switchedPowerDifference as float []
        raises ValueError If switchedPowerDifference does not exist.
        """
        if not self._switchedPowerDifferenceExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + switchedPowerDifference
                + " attribute in table SysPower does not exist!"
            )

        return copy.deepcopy(self._switchedPowerDifference)

    def setSwitchedPowerDifference(self, switchedPowerDifference):
        """
        Set switchedPowerDifference with the specified float []  value.
        switchedPowerDifference The float []  value to which switchedPowerDifference is to be set.


        """

        # value must be a list
        if not isinstance(switchedPowerDifference, list):
            raise ValueError("The value of switchedPowerDifference must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(switchedPowerDifference)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of switchedPowerDifference is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(switchedPowerDifference, float):
                raise ValueError(
                    "type of the first value in switchedPowerDifference is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._switchedPowerDifference = copy.deepcopy(switchedPowerDifference)
        except Exception as exc:
            raise ValueError("Invalid switchedPowerDifference : " + str(exc))

        self._switchedPowerDifferenceExists = True

    def clearSwitchedPowerDifference(self):
        """
        Mark switchedPowerDifference, which is an optional field, as non-existent.
        """
        self._switchedPowerDifferenceExists = False

    # ===> Attribute switchedPowerSum, which is optional
    _switchedPowerSumExists = False

    _switchedPowerSum = None  # this is a 1D list of float

    def isSwitchedPowerSumExists(self):
        """
        The attribute switchedPowerSum is optional. Return True if this attribute exists.
        return True if and only if the switchedPowerSum attribute exists.
        """
        return self._switchedPowerSumExists

    def getSwitchedPowerSum(self):
        """
        Get switchedPowerSum, which is optional.
        return switchedPowerSum as float []
        raises ValueError If switchedPowerSum does not exist.
        """
        if not self._switchedPowerSumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + switchedPowerSum
                + " attribute in table SysPower does not exist!"
            )

        return copy.deepcopy(self._switchedPowerSum)

    def setSwitchedPowerSum(self, switchedPowerSum):
        """
        Set switchedPowerSum with the specified float []  value.
        switchedPowerSum The float []  value to which switchedPowerSum is to be set.


        """

        # value must be a list
        if not isinstance(switchedPowerSum, list):
            raise ValueError("The value of switchedPowerSum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(switchedPowerSum)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of switchedPowerSum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(switchedPowerSum, float):
                raise ValueError(
                    "type of the first value in switchedPowerSum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._switchedPowerSum = copy.deepcopy(switchedPowerSum)
        except Exception as exc:
            raise ValueError("Invalid switchedPowerSum : " + str(exc))

        self._switchedPowerSumExists = True

    def clearSwitchedPowerSum(self):
        """
        Mark switchedPowerSum, which is an optional field, as non-existent.
        """
        self._switchedPowerSumExists = False

    # ===> Attribute requantizerGain, which is optional
    _requantizerGainExists = False

    _requantizerGain = None  # this is a 1D list of float

    def isRequantizerGainExists(self):
        """
        The attribute requantizerGain is optional. Return True if this attribute exists.
        return True if and only if the requantizerGain attribute exists.
        """
        return self._requantizerGainExists

    def getRequantizerGain(self):
        """
        Get requantizerGain, which is optional.
        return requantizerGain as float []
        raises ValueError If requantizerGain does not exist.
        """
        if not self._requantizerGainExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + requantizerGain
                + " attribute in table SysPower does not exist!"
            )

        return copy.deepcopy(self._requantizerGain)

    def setRequantizerGain(self, requantizerGain):
        """
        Set requantizerGain with the specified float []  value.
        requantizerGain The float []  value to which requantizerGain is to be set.


        """

        # value must be a list
        if not isinstance(requantizerGain, list):
            raise ValueError("The value of requantizerGain must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(requantizerGain)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of requantizerGain is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(requantizerGain, float):
                raise ValueError(
                    "type of the first value in requantizerGain is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._requantizerGain = copy.deepcopy(requantizerGain)
        except Exception as exc:
            raise ValueError("Invalid requantizerGain : " + str(exc))

        self._requantizerGainExists = True

    def clearRequantizerGain(self):
        """
        Mark requantizerGain, which is an optional field, as non-existent.
        """
        self._requantizerGainExists = False

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

    # ===> Attribute feedId

    _feedId = 0

    def getFeedId(self):
        """
        Get feedId.
        return feedId as int
        """

        return self._feedId

    def setFeedId(self, feedId):
        """
        Set feedId with the specified int value.
        feedId The int value to which feedId is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the feedId field, which is part of the key, after this row has been added to this table."
            )

        self._feedId = int(feedId)

    # ===> Attribute spectralWindowId

    _spectralWindowId = Tag()

    def getSpectralWindowId(self):
        """
        Get spectralWindowId.
        return spectralWindowId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._spectralWindowId)

    def setSpectralWindowId(self, spectralWindowId):
        """
        Set spectralWindowId with the specified Tag value.
        spectralWindowId The Tag value to which spectralWindowId is to be set.
        The value of spectralWindowId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the spectralWindowId field, which is part of the key, after this row has been added to this table."
            )

        self._spectralWindowId = Tag(spectralWindowId)

    # Links

    def getAntennaUsingAntennaId(self):
        """
        Returns the row in the Antenna table having Antenna.antennaId == antennaId

        """

        return self._table.getContainer().getAntenna().getRowByKey(self._antennaId)

    def getSpectralWindowUsingSpectralWindowId(self):
        """
        Returns the row in the SpectralWindow table having SpectralWindow.spectralWindowId == spectralWindowId

        """

        return (
            self._table.getContainer()
            .getSpectralWindow()
            .getRowByKey(self._spectralWindowId)
        )

    # ===> Slice link from a row of SysPower table to a collection of row of Feed table.
    def getFeeds(self):
        """
        Get the collection of rows in the Feed table having feedId == this.feedId
        """

        return self._table.getContainer().getFeed().getRowByFeedId(self._feedId)

    # comparison methods

    def compareNoAutoInc(
        self, antennaId, spectralWindowId, feedId, timeInterval, numReceptor
    ):
        """
        Compare each attribute except the autoincrementable one of this SysPowerRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaId is a Tag, compare using the equals method.
        if not self._antennaId.equals(antennaId):
            return False

        # spectralWindowId is a Tag, compare using the equals method.
        if not self._spectralWindowId.equals(spectralWindowId):
            return False

        # feedId is a int, compare using the == operator.
        if not (self._feedId == feedId):
            return False

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(otherRow.getNumReceptor())

    def compareRequiredValue(self, numReceptor):

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        return True
