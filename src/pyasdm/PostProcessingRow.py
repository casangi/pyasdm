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
# File PostProcessingRow.py
#

import pyasdm.PostProcessingTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.PostProcessingIntent import PostProcessingIntent


from xml.dom import minidom

import copy


class PostProcessingRow:
    """
    The PostProcessingRow class is a row of a PostProcessingTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a PostProcessingRow.
        When row is None, create an empty row attached to table, which must be a PostProcessingTable.
        When row is given, copy those values in to the new row. The row argument must be a PostProcessingRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.PostProcessingTable):
            raise ValueError("table must be a PostProcessingTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._postProcessingId = Tag()

        self._intent = PostProcessingIntent.from_int(0)

        self._descriptionExists = False

        self._description = None

        self._numSpectralWindowExists = False

        self._numSpectralWindow = 0

        self._numScanExists = False

        self._numScan = 0

        self._scanNumberExists = False

        self._scanNumber = []  # this is a list of int []

        self._calibrationStrategyExists = False

        self._calibrationStrategy = None

        # extrinsic attributes

        self._execBlockIdExists = False

        self._execBlockId = []  # this is a list of Tag []

        self._spectralWindowIdExists = False

        self._spectralWindowId = []  # this is a list of Tag []

        if row is not None:
            if not isinstance(row, PostProcessingRow):
                raise ValueError("row must be a PostProcessingRow")

            # copy constructor

            self._postProcessingId = Tag(row._postProcessingId)

            # We force the attribute of the result to be not None
            if row._intent is None:
                self._intent = PostProcessingIntent.from_int(0)
            else:
                self._intent = PostProcessingIntent(row._intent)

            # by default set systematically description's value to something not None

            if row._descriptionExists:

                self._description = row._description

                self._descriptionExists = True

            # by default set systematically numSpectralWindow's value to something not None

            if row._numSpectralWindowExists:

                self._numSpectralWindow = row._numSpectralWindow

                self._numSpectralWindowExists = True

            # by default set systematically numScan's value to something not None

            if row._numScanExists:

                self._numScan = row._numScan

                self._numScanExists = True

            # by default set systematically scanNumber's value to something not None

            if row._scanNumberExists:

                # scanNumber is a list, make a deep copy
                self._scanNumber = copy.deepcopy(row._scanNumber)

                self._scanNumberExists = True

            # by default set systematically calibrationStrategy's value to something not None

            if row._calibrationStrategyExists:

                self._calibrationStrategy = row._calibrationStrategy

                self._calibrationStrategyExists = True

            # by default set systematically spectralWindowId's value to something not None

            if row._spectralWindowIdExists:

                # spectralWindowId is a list, let's populate self._spectralWindowId element by element.
                if self._spectralWindowId is None:
                    self._spectralWindowId = []
                for i in range(len(row._spectralWindowId)):

                    self._spectralWindowId.append(Tag(row._spectralWindowId[i]))

                self._spectralWindowIdExists = True

            # by default set systematically execBlockId's value to something not None

            if row._execBlockIdExists:

                # execBlockId is a list, let's populate self._execBlockId element by element.
                if self._execBlockId is None:
                    self._execBlockId = []
                for i in range(len(row._execBlockId)):

                    self._execBlockId.append(Tag(row._execBlockId[i]))

                self._execBlockIdExists = True

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

        result += Parser.extendedValueToXML("postProcessingId", self._postProcessingId)

        result += Parser.valueToXML("intent", PostProcessingIntent.name(self._intent))

        if self._descriptionExists:

            result += Parser.valueToXML("description", self._description)

        if self._numSpectralWindowExists:

            result += Parser.valueToXML("numSpectralWindow", self._numSpectralWindow)

        if self._numScanExists:

            result += Parser.valueToXML("numScan", self._numScan)

        if self._scanNumberExists:

            result += Parser.listValueToXML("scanNumber", self._scanNumber)

        if self._calibrationStrategyExists:

            result += Parser.valueToXML(
                "calibrationStrategy", self._calibrationStrategy
            )

        # extrinsic attributes

        if self._execBlockIdExists:

            result += Parser.listExtendedValueToXML("execBlockId", self._execBlockId)

        if self._spectralWindowIdExists:

            result += Parser.listExtendedValueToXML(
                "spectralWindowId", self._spectralWindowId
            )

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
                "xmlrow is not a string or a minidom.Element", "PostProcessingTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException(
                "the argument is not a row", "PostProcessingTable"
            )

        # intrinsic attribute values

        postProcessingIdNode = rowdom.getElementsByTagName("postProcessingId")[0]

        self._postProcessingId = Tag(postProcessingIdNode.firstChild.data.strip())

        intentNode = rowdom.getElementsByTagName("intent")[0]

        self._intent = PostProcessingIntent.newPostProcessingIntent(
            intentNode.firstChild.data.strip()
        )

        descriptionNode = rowdom.getElementsByTagName("description")
        if len(descriptionNode) > 0:

            self._description = str(descriptionNode[0].firstChild.data.strip())

            self._descriptionExists = True

        numSpectralWindowNode = rowdom.getElementsByTagName("numSpectralWindow")
        if len(numSpectralWindowNode) > 0:

            self._numSpectralWindow = int(
                numSpectralWindowNode[0].firstChild.data.strip()
            )

            self._numSpectralWindowExists = True

        numScanNode = rowdom.getElementsByTagName("numScan")
        if len(numScanNode) > 0:

            self._numScan = int(numScanNode[0].firstChild.data.strip())

            self._numScanExists = True

        scanNumberNode = rowdom.getElementsByTagName("scanNumber")
        if len(scanNumberNode) > 0:

            scanNumberStr = scanNumberNode[0].firstChild.data.strip()

            self._scanNumber = Parser.stringListToLists(
                scanNumberStr, int, "PostProcessing", False
            )

            self._scanNumberExists = True

        calibrationStrategyNode = rowdom.getElementsByTagName("calibrationStrategy")
        if len(calibrationStrategyNode) > 0:

            self._calibrationStrategy = str(
                calibrationStrategyNode[0].firstChild.data.strip()
            )

            self._calibrationStrategyExists = True

        # extrinsic attribute values

        execBlockIdNode = rowdom.getElementsByTagName("execBlockId")
        if len(execBlockIdNode) > 0:

            execBlockIdStr = execBlockIdNode[0].firstChild.data.strip()

            self._execBlockId = Parser.stringListToLists(
                execBlockIdStr, Tag, "PostProcessing", True
            )

            self._execBlockIdExists = True

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")
        if len(spectralWindowIdNode) > 0:

            spectralWindowIdStr = spectralWindowIdNode[0].firstChild.data.strip()

            self._spectralWindowId = Parser.stringListToLists(
                spectralWindowIdStr, Tag, "PostProcessing", True
            )

            self._spectralWindowIdExists = True

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._postProcessingId.toBin(eos)

        eos.writeString(str(self._intent))

        eos.writeBool(self._descriptionExists)
        if self._descriptionExists:

            eos.writeStr(self._description)

        eos.writeBool(self._numSpectralWindowExists)
        if self._numSpectralWindowExists:

            eos.writeInt(self._numSpectralWindow)

        eos.writeBool(self._numScanExists)
        if self._numScanExists:

            eos.writeInt(self._numScan)

        eos.writeBool(self._scanNumberExists)
        if self._scanNumberExists:

            eos.writeInt(len(self._scanNumber))
            for i in range(len(self._scanNumber)):

                eos.writeInt(self._scanNumber[i])

        eos.writeBool(self._calibrationStrategyExists)
        if self._calibrationStrategyExists:

            eos.writeStr(self._calibrationStrategy)

        eos.writeBool(self._spectralWindowIdExists)
        if self._spectralWindowIdExists:

            Tag.listToBin(self._spectralWindowId, eos)

        eos.writeBool(self._execBlockIdExists)
        if self._execBlockIdExists:

            Tag.listToBin(self._execBlockId, eos)

    @staticmethod
    def postProcessingIdFromBin(row, eis):
        """
        Set the postProcessingId in row from the EndianInput (eis) instance.
        """

        row._postProcessingId = Tag.fromBin(eis)

    @staticmethod
    def intentFromBin(row, eis):
        """
        Set the intent in row from the EndianInput (eis) instance.
        """

        row._intent = PostProcessingIntent.literal(eis.readString())

    @staticmethod
    def descriptionFromBin(row, eis):
        """
        Set the optional description in row from the EndianInput (eis) instance.
        """
        row._descriptionExists = eis.readBool()
        if row._descriptionExists:

            row._description = eis.readStr()

    @staticmethod
    def numSpectralWindowFromBin(row, eis):
        """
        Set the optional numSpectralWindow in row from the EndianInput (eis) instance.
        """
        row._numSpectralWindowExists = eis.readBool()
        if row._numSpectralWindowExists:

            row._numSpectralWindow = eis.readInt()

    @staticmethod
    def numScanFromBin(row, eis):
        """
        Set the optional numScan in row from the EndianInput (eis) instance.
        """
        row._numScanExists = eis.readBool()
        if row._numScanExists:

            row._numScan = eis.readInt()

    @staticmethod
    def scanNumberFromBin(row, eis):
        """
        Set the optional scanNumber in row from the EndianInput (eis) instance.
        """
        row._scanNumberExists = eis.readBool()
        if row._scanNumberExists:

            scanNumberDim1 = eis.readInt()
            thisList = []
            for i in range(scanNumberDim1):
                thisValue = eis.readInt()
                thisList.append(thisValue)
            row._scanNumber = thisList

    @staticmethod
    def calibrationStrategyFromBin(row, eis):
        """
        Set the optional calibrationStrategy in row from the EndianInput (eis) instance.
        """
        row._calibrationStrategyExists = eis.readBool()
        if row._calibrationStrategyExists:

            row._calibrationStrategy = eis.readStr()

    @staticmethod
    def spectralWindowIdFromBin(row, eis):
        """
        Set the optional spectralWindowId in row from the EndianInput (eis) instance.
        """
        row._spectralWindowIdExists = eis.readBool()
        if row._spectralWindowIdExists:

            row._spectralWindowId = Tag.from1DBin(eis)

    @staticmethod
    def execBlockIdFromBin(row, eis):
        """
        Set the optional execBlockId in row from the EndianInput (eis) instance.
        """
        row._execBlockIdExists = eis.readBool()
        if row._execBlockIdExists:

            row._execBlockId = Tag.from1DBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["postProcessingId"] = PostProcessingRow.postProcessingIdFromBin
        _fromBinMethods["intent"] = PostProcessingRow.intentFromBin

        _fromBinMethods["description"] = PostProcessingRow.descriptionFromBin
        _fromBinMethods["numSpectralWindow"] = (
            PostProcessingRow.numSpectralWindowFromBin
        )
        _fromBinMethods["numScan"] = PostProcessingRow.numScanFromBin
        _fromBinMethods["scanNumber"] = PostProcessingRow.scanNumberFromBin
        _fromBinMethods["calibrationStrategy"] = (
            PostProcessingRow.calibrationStrategyFromBin
        )
        _fromBinMethods["spectralWindowId"] = PostProcessingRow.spectralWindowIdFromBin
        _fromBinMethods["execBlockId"] = PostProcessingRow.execBlockIdFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = PostProcessingRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " PostProcessing",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute postProcessingId

    _postProcessingId = Tag()

    def getPostProcessingId(self):
        """
        Get postProcessingId.
        return postProcessingId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._postProcessingId)

    def setPostProcessingId(self, postProcessingId):
        """
        Set postProcessingId with the specified Tag value.
        postProcessingId The Tag value to which postProcessingId is to be set.
        The value of postProcessingId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the postProcessingId field, which is part of the key, after this row has been added to this table."
            )

        self._postProcessingId = Tag(postProcessingId)

    # ===> Attribute intent

    _intent = PostProcessingIntent.from_int(0)

    def getIntent(self):
        """
        Get intent.
        return intent as PostProcessingIntent
        """

        return self._intent

    def setIntent(self, intent):
        """
        Set intent with the specified PostProcessingIntent value.
        intent The PostProcessingIntent value to which intent is to be set.


        """

        self._intent = PostProcessingIntent(intent)

    # ===> Attribute description, which is optional
    _descriptionExists = False

    _description = None

    def isDescriptionExists(self):
        """
        The attribute description is optional. Return True if this attribute exists.
        return True if and only if the description attribute exists.
        """
        return self._descriptionExists

    def getDescription(self):
        """
        Get description, which is optional.
        return description as str
        raises ValueError If description does not exist.
        """
        if not self._descriptionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + description
                + " attribute in table PostProcessing does not exist!"
            )

        return self._description

    def setDescription(self, description):
        """
        Set description with the specified str value.
        description The str value to which description is to be set.


        """

        self._description = str(description)

        self._descriptionExists = True

    def clearDescription(self):
        """
        Mark description, which is an optional field, as non-existent.
        """
        self._descriptionExists = False

    # ===> Attribute numSpectralWindow, which is optional
    _numSpectralWindowExists = False

    _numSpectralWindow = 0

    def isNumSpectralWindowExists(self):
        """
        The attribute numSpectralWindow is optional. Return True if this attribute exists.
        return True if and only if the numSpectralWindow attribute exists.
        """
        return self._numSpectralWindowExists

    def getNumSpectralWindow(self):
        """
        Get numSpectralWindow, which is optional.
        return numSpectralWindow as int
        raises ValueError If numSpectralWindow does not exist.
        """
        if not self._numSpectralWindowExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numSpectralWindow
                + " attribute in table PostProcessing does not exist!"
            )

        return self._numSpectralWindow

    def setNumSpectralWindow(self, numSpectralWindow):
        """
        Set numSpectralWindow with the specified int value.
        numSpectralWindow The int value to which numSpectralWindow is to be set.


        """

        self._numSpectralWindow = int(numSpectralWindow)

        self._numSpectralWindowExists = True

    def clearNumSpectralWindow(self):
        """
        Mark numSpectralWindow, which is an optional field, as non-existent.
        """
        self._numSpectralWindowExists = False

    # ===> Attribute numScan, which is optional
    _numScanExists = False

    _numScan = 0

    def isNumScanExists(self):
        """
        The attribute numScan is optional. Return True if this attribute exists.
        return True if and only if the numScan attribute exists.
        """
        return self._numScanExists

    def getNumScan(self):
        """
        Get numScan, which is optional.
        return numScan as int
        raises ValueError If numScan does not exist.
        """
        if not self._numScanExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numScan
                + " attribute in table PostProcessing does not exist!"
            )

        return self._numScan

    def setNumScan(self, numScan):
        """
        Set numScan with the specified int value.
        numScan The int value to which numScan is to be set.


        """

        self._numScan = int(numScan)

        self._numScanExists = True

    def clearNumScan(self):
        """
        Mark numScan, which is an optional field, as non-existent.
        """
        self._numScanExists = False

    # ===> Attribute scanNumber, which is optional
    _scanNumberExists = False

    _scanNumber = None  # this is a 1D list of int

    def isScanNumberExists(self):
        """
        The attribute scanNumber is optional. Return True if this attribute exists.
        return True if and only if the scanNumber attribute exists.
        """
        return self._scanNumberExists

    def getScanNumber(self):
        """
        Get scanNumber, which is optional.
        return scanNumber as int []
        raises ValueError If scanNumber does not exist.
        """
        if not self._scanNumberExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + scanNumber
                + " attribute in table PostProcessing does not exist!"
            )

        return copy.deepcopy(self._scanNumber)

    def setScanNumber(self, scanNumber):
        """
        Set scanNumber with the specified int []  value.
        scanNumber The int []  value to which scanNumber is to be set.


        """

        # value must be a list
        if not isinstance(scanNumber, list):
            raise ValueError("The value of scanNumber must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(scanNumber)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of scanNumber is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(scanNumber, int):
                raise ValueError(
                    "type of the first value in scanNumber is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._scanNumber = copy.deepcopy(scanNumber)
        except Exception as exc:
            raise ValueError("Invalid scanNumber : " + str(exc))

        self._scanNumberExists = True

    def clearScanNumber(self):
        """
        Mark scanNumber, which is an optional field, as non-existent.
        """
        self._scanNumberExists = False

    # ===> Attribute calibrationStrategy, which is optional
    _calibrationStrategyExists = False

    _calibrationStrategy = None

    def isCalibrationStrategyExists(self):
        """
        The attribute calibrationStrategy is optional. Return True if this attribute exists.
        return True if and only if the calibrationStrategy attribute exists.
        """
        return self._calibrationStrategyExists

    def getCalibrationStrategy(self):
        """
        Get calibrationStrategy, which is optional.
        return calibrationStrategy as str
        raises ValueError If calibrationStrategy does not exist.
        """
        if not self._calibrationStrategyExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + calibrationStrategy
                + " attribute in table PostProcessing does not exist!"
            )

        return self._calibrationStrategy

    def setCalibrationStrategy(self, calibrationStrategy):
        """
        Set calibrationStrategy with the specified str value.
        calibrationStrategy The str value to which calibrationStrategy is to be set.


        """

        self._calibrationStrategy = str(calibrationStrategy)

        self._calibrationStrategyExists = True

    def clearCalibrationStrategy(self):
        """
        Mark calibrationStrategy, which is an optional field, as non-existent.
        """
        self._calibrationStrategyExists = False

    # Extrinsic Table Attributes

    # ===> Attribute execBlockId, which is optional
    _execBlockIdExists = False

    _execBlockId = []  # this is a list of Tag []

    def isExecBlockIdExists(self):
        """
        The attribute execBlockId is optional. Return True if this attribute exists.
        return True if and only if the execBlockId attribute exists.
        """
        return self._execBlockIdExists

    def getExecBlockId(self):
        """
        Get execBlockId, which is optional.
        return execBlockId as Tag []
        raises ValueError If execBlockId does not exist.
        """
        if not self._execBlockIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + execBlockId
                + " attribute in table PostProcessing does not exist!"
            )

        return copy.deepcopy(self._execBlockId)

    def setExecBlockId(self, execBlockId):
        """
        Set execBlockId with the specified Tag []  value.
        execBlockId The Tag []  value to which execBlockId is to be set.
        The value of execBlockId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(execBlockId, list):
            raise ValueError("The value of execBlockId must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(execBlockId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of execBlockId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(execBlockId, Tag):
                raise ValueError(
                    "type of the first value in execBlockId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._execBlockId = copy.deepcopy(execBlockId)
        except Exception as exc:
            raise ValueError("Invalid execBlockId : " + str(exc))

        self._execBlockIdExists = True

    def clearExecBlockId(self):
        """
        Mark execBlockId, which is an optional field, as non-existent.
        """
        self._execBlockIdExists = False

    # ===> Attribute spectralWindowId, which is optional
    _spectralWindowIdExists = False

    _spectralWindowId = []  # this is a list of Tag []

    def isSpectralWindowIdExists(self):
        """
        The attribute spectralWindowId is optional. Return True if this attribute exists.
        return True if and only if the spectralWindowId attribute exists.
        """
        return self._spectralWindowIdExists

    def getSpectralWindowId(self):
        """
        Get spectralWindowId, which is optional.
        return spectralWindowId as Tag []
        raises ValueError If spectralWindowId does not exist.
        """
        if not self._spectralWindowIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + spectralWindowId
                + " attribute in table PostProcessing does not exist!"
            )

        return copy.deepcopy(self._spectralWindowId)

    def setSpectralWindowId(self, spectralWindowId):
        """
        Set spectralWindowId with the specified Tag []  value.
        spectralWindowId The Tag []  value to which spectralWindowId is to be set.
        The value of spectralWindowId can be anything allowed by the Tag []  constructor.

        """

        # value must be a list
        if not isinstance(spectralWindowId, list):
            raise ValueError("The value of spectralWindowId must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(spectralWindowId)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of spectralWindowId is not correct")

            # the type of the values in the list must be Tag
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(spectralWindowId, Tag):
                raise ValueError(
                    "type of the first value in spectralWindowId is not Tag as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._spectralWindowId = copy.deepcopy(spectralWindowId)
        except Exception as exc:
            raise ValueError("Invalid spectralWindowId : " + str(exc))

        self._spectralWindowIdExists = True

    def clearSpectralWindowId(self):
        """
        Mark spectralWindowId, which is an optional field, as non-existent.
        """
        self._spectralWindowIdExists = False

    # Links

    def setOneSpectralWindowId(self, index, spectralWindowId):
        """
        Set spectralWindowId[index] with the specified Tag value.
        index The index in spectralWindowId where to set the Tag value.
        spectralWindowId The Tag value to which spectralWindowId[index] is to be set.
        Raises an exception if that value does not already exist in this row
        """
        if not self._spectralWindowIdExists():
            raise ValueError(
                "The optional attribute, spectralWindowId, does not exist in this row. This value can not be set using this method."
            )
        self._spectralWindowId[index] = Tag(spectralWindowId)

    # ===> hasmany link from a row of PostProcessing table to many rows of SpectralWindow table.

    def addSpectralWindowId(self, id):
        """
        Append a Tag to spectralWindowId
        id the Tag to be appended to spectralWindowId
        """
        if isinstance(id, list):
            for thisValue in id:
                self._spectralWindowId.append(Tag(thisValue))
        else:
            self._spectralWindowId.append(Tag(id))

        if not self._spectralWindowIdExists:
            self._spectralWindowIdExists = True

    def getOneSpectralWindowId(self, i):
        """
        Returns the Tag stored in spectralWindowId at position i.
        """
        return self._spectralWindowId[i]

    def getSpectralWindowUsingSpectralWindowId(self, i):
        """
        Returns the SpectralWindowRow linked to this row via the Tag stored in spectralWindowId
        at position i.
        """

        return (
            self._table.getContainer()
            .getSpectralWindow()
            .getRowByKey(self._spectralWindowId[i])
        )

    def getSpectralWindowsUsingSpectralWindowId(self):
        """
        Returns the array of SpectralWindowRow linked to this row via the Tags stored in spectralWindowId
        """
        result = []
        for thisItem in self._spectralWindowId:
            result.append(
                self._table.getContainer().getSpectralWindow().getRowByKey(thisItem)
            )

        return result

    def setOneExecBlockId(self, index, execBlockId):
        """
        Set execBlockId[index] with the specified Tag value.
        index The index in execBlockId where to set the Tag value.
        execBlockId The Tag value to which execBlockId[index] is to be set.
        Raises an exception if that value does not already exist in this row
        """
        if not self._execBlockIdExists():
            raise ValueError(
                "The optional attribute, execBlockId, does not exist in this row. This value can not be set using this method."
            )
        self._execBlockId[index] = Tag(execBlockId)

    # ===> hasmany link from a row of PostProcessing table to many rows of ExecBlock table.

    def addExecBlockId(self, id):
        """
        Append a Tag to execBlockId
        id the Tag to be appended to execBlockId
        """
        if isinstance(id, list):
            for thisValue in id:
                self._execBlockId.append(Tag(thisValue))
        else:
            self._execBlockId.append(Tag(id))

        if not self._execBlockIdExists:
            self._execBlockIdExists = True

    def getOneExecBlockId(self, i):
        """
        Returns the Tag stored in execBlockId at position i.
        """
        return self._execBlockId[i]

    def getExecBlockUsingExecBlockId(self, i):
        """
        Returns the ExecBlockRow linked to this row via the Tag stored in execBlockId
        at position i.
        """

        return (
            self._table.getContainer().getExecBlock().getRowByKey(self._execBlockId[i])
        )

    def getExecBlocksUsingExecBlockId(self):
        """
        Returns the array of ExecBlockRow linked to this row via the Tags stored in execBlockId
        """
        result = []
        for thisItem in self._execBlockId:
            result.append(
                self._table.getContainer().getExecBlock().getRowByKey(thisItem)
            )

        return result

    # comparison methods

    def compareNoAutoInc(self, intent):
        """
        Compare each attribute except the autoincrementable one of this PostProcessingRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # intent is a PostProcessingIntent, compare using the == operator on the getValue() output
        if not (self._intent.getValue() == intent.getValue()):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(otherRow.getIntent())

    def compareRequiredValue(self, intent):

        # intent is a PostProcessingIntent, compare using the == operator on the getValue() output
        if not (self._intent.getValue() == intent.getValue()):
            return False

        return True


# initialize the dictionary that maps fields to init methods
PostProcessingRow.initFromBinMethods()
