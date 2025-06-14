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
# File EphemerisRow.py
#

import pyasdm.EphemerisTable

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


class EphemerisRow:
    """
    The EphemerisRow class is a row of a EphemerisTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a EphemerisRow.
        When row is None, create an empty row attached to table, which must be a EphemerisTable.
        When row is given, copy those values in to the new row. The row argument must be a EphemerisRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.EphemerisTable):
            raise ValueError("table must be a EphemerisTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._timeInterval = ArrayTimeInterval()

        self._ephemerisId = 0

        self._observerLocation = []  # this is a list of float []

        self._equinoxEquator = None

        self._numPolyDir = 0

        self._dir = []  # this is a list of float []  []

        self._numPolyDist = 0

        self._distance = []  # this is a list of float []

        self._timeOrigin = ArrayTime()

        self._origin = None

        self._numPolyRadVelExists = False

        self._numPolyRadVel = 0

        self._radVelExists = False

        self._radVel = []  # this is a list of float []

        if row is not None:
            if not isinstance(row, EphemerisRow):
                raise ValueError("row must be a EphemerisRow")

            # copy constructor

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._ephemerisId = row._ephemerisId

            # observerLocation is a  list , make a deep copy
            self._observerLocation = copy.deepcopy(row._observerLocation)

            self._equinoxEquator = row._equinoxEquator

            self._numPolyDir = row._numPolyDir

            # dir is a  list , make a deep copy
            self._dir = copy.deepcopy(row._dir)

            self._numPolyDist = row._numPolyDist

            # distance is a  list , make a deep copy
            self._distance = copy.deepcopy(row._distance)

            self._timeOrigin = ArrayTime(row._timeOrigin)

            self._origin = row._origin

            # by default set systematically numPolyRadVel's value to something not None

            if row._numPolyRadVelExists:

                self._numPolyRadVel = row._numPolyRadVel

                self._numPolyRadVelExists = True

            # by default set systematically radVel's value to something not None

            if row._radVelExists:

                # radVel is a list, make a deep copy
                self._radVel = copy.deepcopy(row._radVel)

                self._radVelExists = True

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

        result += Parser.valueToXML("ephemerisId", self._ephemerisId)

        result += Parser.listValueToXML("observerLocation", self._observerLocation)

        result += Parser.valueToXML("equinoxEquator", self._equinoxEquator)

        result += Parser.valueToXML("numPolyDir", self._numPolyDir)

        result += Parser.listValueToXML("dir", self._dir)

        result += Parser.valueToXML("numPolyDist", self._numPolyDist)

        result += Parser.listValueToXML("distance", self._distance)

        result += Parser.extendedValueToXML("timeOrigin", self._timeOrigin)

        result += Parser.valueToXML("origin", self._origin)

        if self._numPolyRadVelExists:

            result += Parser.valueToXML("numPolyRadVel", self._numPolyRadVel)

        if self._radVelExists:

            result += Parser.listValueToXML("radVel", self._radVel)

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
                "xmlrow is not a string or a minidom.Element", "EphemerisTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "EphemerisTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        ephemerisIdNode = rowdom.getElementsByTagName("ephemerisId")[0]

        self._ephemerisId = int(ephemerisIdNode.firstChild.data.strip())

        observerLocationNode = rowdom.getElementsByTagName("observerLocation")[0]

        observerLocationStr = observerLocationNode.firstChild.data.strip()

        self._observerLocation = Parser.stringListToLists(
            observerLocationStr, float, "Ephemeris", False
        )

        equinoxEquatorNode = rowdom.getElementsByTagName("equinoxEquator")[0]

        self._equinoxEquator = float(equinoxEquatorNode.firstChild.data.strip())

        numPolyDirNode = rowdom.getElementsByTagName("numPolyDir")[0]

        self._numPolyDir = int(numPolyDirNode.firstChild.data.strip())

        dirNode = rowdom.getElementsByTagName("dir")[0]

        dirStr = dirNode.firstChild.data.strip()

        self._dir = Parser.stringListToLists(dirStr, float, "Ephemeris", False)

        numPolyDistNode = rowdom.getElementsByTagName("numPolyDist")[0]

        self._numPolyDist = int(numPolyDistNode.firstChild.data.strip())

        distanceNode = rowdom.getElementsByTagName("distance")[0]

        distanceStr = distanceNode.firstChild.data.strip()

        self._distance = Parser.stringListToLists(
            distanceStr, float, "Ephemeris", False
        )

        timeOriginNode = rowdom.getElementsByTagName("timeOrigin")[0]

        self._timeOrigin = ArrayTime(timeOriginNode.firstChild.data.strip())

        originNode = rowdom.getElementsByTagName("origin")[0]

        self._origin = str(originNode.firstChild.data.strip())

        numPolyRadVelNode = rowdom.getElementsByTagName("numPolyRadVel")
        if len(numPolyRadVelNode) > 0:

            self._numPolyRadVel = int(numPolyRadVelNode[0].firstChild.data.strip())

            self._numPolyRadVelExists = True

        radVelNode = rowdom.getElementsByTagName("radVel")
        if len(radVelNode) > 0:

            radVelStr = radVelNode[0].firstChild.data.strip()

            self._radVel = Parser.stringListToLists(
                radVelStr, float, "Ephemeris", False
            )

            self._radVelExists = True

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._timeInterval.toBin(eos)

        eos.writeInt(self._ephemerisId)

        eos.writeInt(len(self._observerLocation))
        for i in range(len(self._observerLocation)):

            eos.writeFloat(self._observerLocation[i])

        eos.writeFloat(self._equinoxEquator)

        eos.writeInt(self._numPolyDir)

        # null array case, unsure if this is possible but this should work
        if self._dir is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            dir_dims = pyasdm.utils.getListDims(self._dir)
        # assumes it really is 2D
        eos.writeInt(dir_dims[0])
        eos.writeInt(dir_dims[1])
        for i in range(dir_dims[0]):
            for j in range(dir_dims[1]):
                eos.writeFloat(self._dir[i][j])

        eos.writeInt(self._numPolyDist)

        eos.writeInt(len(self._distance))
        for i in range(len(self._distance)):

            eos.writeFloat(self._distance[i])

        self._timeOrigin.toBin(eos)

        eos.writeStr(self._origin)

        eos.writeBool(self._numPolyRadVelExists)
        if self._numPolyRadVelExists:

            eos.writeInt(self._numPolyRadVel)

        eos.writeBool(self._radVelExists)
        if self._radVelExists:

            eos.writeInt(len(self._radVel))
            for i in range(len(self._radVel)):

                eos.writeFloat(self._radVel[i])

    @staticmethod
    def timeIntervalFromBin(row, eis):
        """
        Set the timeInterval in row from the EndianInput (eis) instance.
        """

        row._timeInterval = ArrayTimeInterval.fromBin(eis)

    @staticmethod
    def ephemerisIdFromBin(row, eis):
        """
        Set the ephemerisId in row from the EndianInput (eis) instance.
        """

        row._ephemerisId = eis.readInt()

    @staticmethod
    def observerLocationFromBin(row, eis):
        """
        Set the observerLocation in row from the EndianInput (eis) instance.
        """

        observerLocationDim1 = eis.readInt()
        thisList = []
        for i in range(observerLocationDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._observerLocation = thisList

    @staticmethod
    def equinoxEquatorFromBin(row, eis):
        """
        Set the equinoxEquator in row from the EndianInput (eis) instance.
        """

        row._equinoxEquator = eis.readFloat()

    @staticmethod
    def numPolyDirFromBin(row, eis):
        """
        Set the numPolyDir in row from the EndianInput (eis) instance.
        """

        row._numPolyDir = eis.readInt()

    @staticmethod
    def dirFromBin(row, eis):
        """
        Set the dir in row from the EndianInput (eis) instance.
        """

        dirDim1 = eis.readInt()
        dirDim2 = eis.readInt()
        thisList = []
        for i in range(dirDim1):
            thisList_j = []
            for j in range(dirDim2):
                thisValue = eis.readFloat()
                thisList_j.append(thisValue)
            thisList.append(thisList_j)
        row._dir = thisList

    @staticmethod
    def numPolyDistFromBin(row, eis):
        """
        Set the numPolyDist in row from the EndianInput (eis) instance.
        """

        row._numPolyDist = eis.readInt()

    @staticmethod
    def distanceFromBin(row, eis):
        """
        Set the distance in row from the EndianInput (eis) instance.
        """

        distanceDim1 = eis.readInt()
        thisList = []
        for i in range(distanceDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._distance = thisList

    @staticmethod
    def timeOriginFromBin(row, eis):
        """
        Set the timeOrigin in row from the EndianInput (eis) instance.
        """

        row._timeOrigin = ArrayTime.fromBin(eis)

    @staticmethod
    def originFromBin(row, eis):
        """
        Set the origin in row from the EndianInput (eis) instance.
        """

        row._origin = eis.readStr()

    @staticmethod
    def numPolyRadVelFromBin(row, eis):
        """
        Set the optional numPolyRadVel in row from the EndianInput (eis) instance.
        """
        row._numPolyRadVelExists = eis.readBool()
        if row._numPolyRadVelExists:

            row._numPolyRadVel = eis.readInt()

    @staticmethod
    def radVelFromBin(row, eis):
        """
        Set the optional radVel in row from the EndianInput (eis) instance.
        """
        row._radVelExists = eis.readBool()
        if row._radVelExists:

            radVelDim1 = eis.readInt()
            thisList = []
            for i in range(radVelDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._radVel = thisList

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["timeInterval"] = EphemerisRow.timeIntervalFromBin
        _fromBinMethods["ephemerisId"] = EphemerisRow.ephemerisIdFromBin
        _fromBinMethods["observerLocation"] = EphemerisRow.observerLocationFromBin
        _fromBinMethods["equinoxEquator"] = EphemerisRow.equinoxEquatorFromBin
        _fromBinMethods["numPolyDir"] = EphemerisRow.numPolyDirFromBin
        _fromBinMethods["dir"] = EphemerisRow.dirFromBin
        _fromBinMethods["numPolyDist"] = EphemerisRow.numPolyDistFromBin
        _fromBinMethods["distance"] = EphemerisRow.distanceFromBin
        _fromBinMethods["timeOrigin"] = EphemerisRow.timeOriginFromBin
        _fromBinMethods["origin"] = EphemerisRow.originFromBin

        _fromBinMethods["numPolyRadVel"] = EphemerisRow.numPolyRadVelFromBin
        _fromBinMethods["radVel"] = EphemerisRow.radVelFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = EphemerisRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Ephemeris",
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

    # ===> Attribute ephemerisId

    _ephemerisId = 0

    def getEphemerisId(self):
        """
        Get ephemerisId.
        return ephemerisId as int
        """

        return self._ephemerisId

    def setEphemerisId(self, ephemerisId):
        """
        Set ephemerisId with the specified int value.
        ephemerisId The int value to which ephemerisId is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the ephemerisId field, which is part of the key, after this row has been added to this table."
            )

        self._ephemerisId = int(ephemerisId)

    # ===> Attribute observerLocation

    _observerLocation = None  # this is a 1D list of float

    def getObserverLocation(self):
        """
        Get observerLocation.
        return observerLocation as float []
        """

        return copy.deepcopy(self._observerLocation)

    def setObserverLocation(self, observerLocation):
        """
        Set observerLocation with the specified float []  value.
        observerLocation The float []  value to which observerLocation is to be set.


        """

        # value must be a list
        if not isinstance(observerLocation, list):
            raise ValueError("The value of observerLocation must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(observerLocation)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of observerLocation is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(observerLocation, float):
                raise ValueError(
                    "type of the first value in observerLocation is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._observerLocation = copy.deepcopy(observerLocation)
        except Exception as exc:
            raise ValueError("Invalid observerLocation : " + str(exc))

    # ===> Attribute equinoxEquator

    _equinoxEquator = None

    def getEquinoxEquator(self):
        """
        Get equinoxEquator.
        return equinoxEquator as float
        """

        return self._equinoxEquator

    def setEquinoxEquator(self, equinoxEquator):
        """
        Set equinoxEquator with the specified float value.
        equinoxEquator The float value to which equinoxEquator is to be set.


        """

        self._equinoxEquator = float(equinoxEquator)

    # ===> Attribute numPolyDir

    _numPolyDir = 0

    def getNumPolyDir(self):
        """
        Get numPolyDir.
        return numPolyDir as int
        """

        return self._numPolyDir

    def setNumPolyDir(self, numPolyDir):
        """
        Set numPolyDir with the specified int value.
        numPolyDir The int value to which numPolyDir is to be set.


        """

        self._numPolyDir = int(numPolyDir)

    # ===> Attribute dir

    _dir = None  # this is a 2D list of float

    def getDir(self):
        """
        Get dir.
        return dir as float []  []
        """

        return copy.deepcopy(self._dir)

    def setDir(self, dir):
        """
        Set dir with the specified float []  []  value.
        dir The float []  []  value to which dir is to be set.


        """

        # value must be a list
        if not isinstance(dir, list):
            raise ValueError("The value of dir must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(dir)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of dir is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(dir, float):
                raise ValueError(
                    "type of the first value in dir is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._dir = copy.deepcopy(dir)
        except Exception as exc:
            raise ValueError("Invalid dir : " + str(exc))

    # ===> Attribute numPolyDist

    _numPolyDist = 0

    def getNumPolyDist(self):
        """
        Get numPolyDist.
        return numPolyDist as int
        """

        return self._numPolyDist

    def setNumPolyDist(self, numPolyDist):
        """
        Set numPolyDist with the specified int value.
        numPolyDist The int value to which numPolyDist is to be set.


        """

        self._numPolyDist = int(numPolyDist)

    # ===> Attribute distance

    _distance = None  # this is a 1D list of float

    def getDistance(self):
        """
        Get distance.
        return distance as float []
        """

        return copy.deepcopy(self._distance)

    def setDistance(self, distance):
        """
        Set distance with the specified float []  value.
        distance The float []  value to which distance is to be set.


        """

        # value must be a list
        if not isinstance(distance, list):
            raise ValueError("The value of distance must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(distance)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of distance is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(distance, float):
                raise ValueError(
                    "type of the first value in distance is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._distance = copy.deepcopy(distance)
        except Exception as exc:
            raise ValueError("Invalid distance : " + str(exc))

    # ===> Attribute timeOrigin

    _timeOrigin = ArrayTime()

    def getTimeOrigin(self):
        """
        Get timeOrigin.
        return timeOrigin as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._timeOrigin)

    def setTimeOrigin(self, timeOrigin):
        """
        Set timeOrigin with the specified ArrayTime value.
        timeOrigin The ArrayTime value to which timeOrigin is to be set.
        The value of timeOrigin can be anything allowed by the ArrayTime constructor.

        """

        self._timeOrigin = ArrayTime(timeOrigin)

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

    # ===> Attribute numPolyRadVel, which is optional
    _numPolyRadVelExists = False

    _numPolyRadVel = 0

    def isNumPolyRadVelExists(self):
        """
        The attribute numPolyRadVel is optional. Return True if this attribute exists.
        return True if and only if the numPolyRadVel attribute exists.
        """
        return self._numPolyRadVelExists

    def getNumPolyRadVel(self):
        """
        Get numPolyRadVel, which is optional.
        return numPolyRadVel as int
        raises ValueError If numPolyRadVel does not exist.
        """
        if not self._numPolyRadVelExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numPolyRadVel
                + " attribute in table Ephemeris does not exist!"
            )

        return self._numPolyRadVel

    def setNumPolyRadVel(self, numPolyRadVel):
        """
        Set numPolyRadVel with the specified int value.
        numPolyRadVel The int value to which numPolyRadVel is to be set.


        """

        self._numPolyRadVel = int(numPolyRadVel)

        self._numPolyRadVelExists = True

    def clearNumPolyRadVel(self):
        """
        Mark numPolyRadVel, which is an optional field, as non-existent.
        """
        self._numPolyRadVelExists = False

    # ===> Attribute radVel, which is optional
    _radVelExists = False

    _radVel = None  # this is a 1D list of float

    def isRadVelExists(self):
        """
        The attribute radVel is optional. Return True if this attribute exists.
        return True if and only if the radVel attribute exists.
        """
        return self._radVelExists

    def getRadVel(self):
        """
        Get radVel, which is optional.
        return radVel as float []
        raises ValueError If radVel does not exist.
        """
        if not self._radVelExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + radVel
                + " attribute in table Ephemeris does not exist!"
            )

        return copy.deepcopy(self._radVel)

    def setRadVel(self, radVel):
        """
        Set radVel with the specified float []  value.
        radVel The float []  value to which radVel is to be set.


        """

        # value must be a list
        if not isinstance(radVel, list):
            raise ValueError("The value of radVel must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(radVel)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of radVel is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(radVel, float):
                raise ValueError(
                    "type of the first value in radVel is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._radVel = copy.deepcopy(radVel)
        except Exception as exc:
            raise ValueError("Invalid radVel : " + str(exc))

        self._radVelExists = True

    def clearRadVel(self):
        """
        Mark radVel, which is an optional field, as non-existent.
        """
        self._radVelExists = False

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(
        self,
        timeInterval,
        ephemerisId,
        observerLocation,
        equinoxEquator,
        numPolyDir,
        dir,
        numPolyDist,
        distance,
        timeOrigin,
        origin,
    ):
        """
        Compare each attribute except the autoincrementable one of this EphemerisRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # ephemerisId is a int, compare using the == operator.
        if not (self._ephemerisId == ephemerisId):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._observerLocation) != len(observerLocation):
            return False
        for indx in range(len(observerLocation)):

            # observerLocation is a list of float, compare using == operator.
            if not (self._observerLocation[indx] == observerLocation[indx]):
                return False

        # equinoxEquator is a float, compare using the == operator.
        if not (self._equinoxEquator == equinoxEquator):
            return False

        # numPolyDir is a int, compare using the == operator.
        if not (self._numPolyDir == numPolyDir):
            return False

        # We compare two 2D arrays (lists).
        if dir is not None:
            if self._dir is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            dir_dims = pyasdm.utils.getListDims(dir)
            this_dir_dims = pyasdm.utils.getListDims(self._dir)
            if dir_dims != this_dir_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(dir_dims[0]):
                for j in range(dir_dims[1]):

                    # dir is an array of float, compare using == operator.
                    if not (self._dir[i][j] == dir[i][j]):
                        return False

        # numPolyDist is a int, compare using the == operator.
        if not (self._numPolyDist == numPolyDist):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._distance) != len(distance):
            return False
        for indx in range(len(distance)):

            # distance is a list of float, compare using == operator.
            if not (self._distance[indx] == distance[indx]):
                return False

        # timeOrigin is a ArrayTime, compare using the equals method.
        if not self._timeOrigin.equals(timeOrigin):
            return False

        # origin is a str, compare using the == operator.
        if not (self._origin == origin):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getObserverLocation(),
            otherRow.getEquinoxEquator(),
            otherRow.getNumPolyDir(),
            otherRow.getDir(),
            otherRow.getNumPolyDist(),
            otherRow.getDistance(),
            otherRow.getTimeOrigin(),
            otherRow.getOrigin(),
        )

    def compareRequiredValue(
        self,
        observerLocation,
        equinoxEquator,
        numPolyDir,
        dir,
        numPolyDist,
        distance,
        timeOrigin,
        origin,
    ):

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._observerLocation) != len(observerLocation):
            return False
        for indx in range(len(observerLocation)):

            # observerLocation is a list of float, compare using == operator.
            if not (self._observerLocation[indx] == observerLocation[indx]):
                return False

        # equinoxEquator is a float, compare using the == operator.
        if not (self._equinoxEquator == equinoxEquator):
            return False

        # numPolyDir is a int, compare using the == operator.
        if not (self._numPolyDir == numPolyDir):
            return False

        # We compare two 2D arrays (lists).
        if dir is not None:
            if self._dir is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            dir_dims = pyasdm.utils.getListDims(dir)
            this_dir_dims = pyasdm.utils.getListDims(self._dir)
            if dir_dims != this_dir_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(dir_dims[0]):
                for j in range(dir_dims[1]):

                    # dir is an array of float, compare using == operator.
                    if not (self._dir[i][j] == dir[i][j]):
                        return False

        # numPolyDist is a int, compare using the == operator.
        if not (self._numPolyDist == numPolyDist):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._distance) != len(distance):
            return False
        for indx in range(len(distance)):

            # distance is a list of float, compare using == operator.
            if not (self._distance[indx] == distance[indx]):
                return False

        # timeOrigin is a ArrayTime, compare using the equals method.
        if not self._timeOrigin.equals(timeOrigin):
            return False

        # origin is a str, compare using the == operator.
        if not (self._origin == origin):
            return False

        return True


# initialize the dictionary that maps fields to init methods
EphemerisRow.initFromBinMethods()
