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
# File FieldRow.py
#

import pyasdm.FieldTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.DirectionReferenceCode import DirectionReferenceCode


from xml.dom import minidom

import copy


class FieldRow:
    """
    The FieldRow class is a row of a FieldTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a FieldRow.
        When row is None, create an empty row attached to table, which must be a FieldTable.
        When row is given, copy those values in to the new row. The row argument must be a FieldRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.FieldTable):
            raise ValueError("table must be a FieldTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._fieldId = Tag()

        self._fieldName = None

        self._numPoly = 0

        self._delayDir = []  # this is a list of Angle []  []

        self._phaseDir = []  # this is a list of Angle []  []

        self._referenceDir = []  # this is a list of Angle []  []

        self._timeExists = False

        self._time = ArrayTime()

        self._codeExists = False

        self._code = None

        self._directionCodeExists = False

        self._directionCode = DirectionReferenceCode.from_int(0)

        self._directionEquinoxExists = False

        self._directionEquinox = ArrayTime()

        self._assocNatureExists = False

        self._assocNature = None

        # extrinsic attributes

        self._assocFieldIdExists = False

        self._assocFieldId = Tag()

        self._ephemerisIdExists = False

        self._ephemerisId = 0

        self._sourceIdExists = False

        self._sourceId = 0

        if row is not None:
            if not isinstance(row, FieldRow):
                raise ValueError("row must be a FieldRow")

            # copy constructor

            self._fieldId = Tag(row._fieldId)

            self._fieldName = row._fieldName

            self._numPoly = row._numPoly

            # delayDir is a  list , make a deep copy
            self._delayDir = copy.deepcopy(row._delayDir)

            # phaseDir is a  list , make a deep copy
            self._phaseDir = copy.deepcopy(row._phaseDir)

            # referenceDir is a  list , make a deep copy
            self._referenceDir = copy.deepcopy(row._referenceDir)

            # by default set systematically time's value to something not None

            if row._timeExists:

                self._time = ArrayTime(row._time)

                self._timeExists = True

            # by default set systematically code's value to something not None

            if row._codeExists:

                self._code = row._code

                self._codeExists = True

            # by default set systematically directionCode's value to something not None

            self._directionCode = DirectionReferenceCode.from_int(0)

            if row._directionCodeExists:

                if row._directionCode is not None:
                    self._directionCode = row._directionCode

                self._directionCodeExists = True

            # by default set systematically directionEquinox's value to something not None

            if row._directionEquinoxExists:

                self._directionEquinox = ArrayTime(row._directionEquinox)

                self._directionEquinoxExists = True

            # by default set systematically assocNature's value to something not None

            if row._assocNatureExists:

                self._assocNature = row._assocNature

                self._assocNatureExists = True

            # by default set systematically ephemerisId's value to something not None

            if row._ephemerisIdExists:

                self._ephemerisId = row._ephemerisId

                self._ephemerisIdExists = True

            # by default set systematically sourceId's value to something not None

            if row._sourceIdExists:

                self._sourceId = row._sourceId

                self._sourceIdExists = True

            # by default set systematically assocFieldId's value to something not None

            if row._assocFieldIdExists:

                self._assocFieldId = Tag(row._assocFieldId)

                self._assocFieldIdExists = True

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

        result += Parser.extendedValueToXML("fieldId", self._fieldId)

        result += Parser.valueToXML("fieldName", self._fieldName)

        result += Parser.valueToXML("numPoly", self._numPoly)

        result += Parser.listExtendedValueToXML("delayDir", self._delayDir)

        result += Parser.listExtendedValueToXML("phaseDir", self._phaseDir)

        result += Parser.listExtendedValueToXML("referenceDir", self._referenceDir)

        if self._timeExists:

            result += Parser.extendedValueToXML("time", self._time)

        if self._codeExists:

            result += Parser.valueToXML("code", self._code)

        if self._directionCodeExists:

            result += Parser.valueToXML(
                "directionCode", DirectionReferenceCode.name(self._directionCode)
            )

        if self._directionEquinoxExists:

            result += Parser.extendedValueToXML(
                "directionEquinox", self._directionEquinox
            )

        if self._assocNatureExists:

            result += Parser.valueToXML("assocNature", self._assocNature)

        # extrinsic attributes

        if self._assocFieldIdExists:

            result += Parser.extendedValueToXML("assocFieldId", self._assocFieldId)

        if self._ephemerisIdExists:

            result += Parser.valueToXML("ephemerisId", self._ephemerisId)

        if self._sourceIdExists:

            result += Parser.valueToXML("sourceId", self._sourceId)

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
                "xmlrow is not a string or a minidom.Element", "FieldTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "FieldTable")

        # intrinsic attribute values

        fieldIdNode = rowdom.getElementsByTagName("fieldId")[0]

        self._fieldId = Tag(fieldIdNode.firstChild.data.strip())

        fieldNameNode = rowdom.getElementsByTagName("fieldName")[0]

        self._fieldName = str(fieldNameNode.firstChild.data.strip())

        numPolyNode = rowdom.getElementsByTagName("numPoly")[0]

        self._numPoly = int(numPolyNode.firstChild.data.strip())

        delayDirNode = rowdom.getElementsByTagName("delayDir")[0]

        delayDirStr = delayDirNode.firstChild.data.strip()

        self._delayDir = Parser.stringListToLists(delayDirStr, Angle, "Field", True)

        phaseDirNode = rowdom.getElementsByTagName("phaseDir")[0]

        phaseDirStr = phaseDirNode.firstChild.data.strip()

        self._phaseDir = Parser.stringListToLists(phaseDirStr, Angle, "Field", True)

        referenceDirNode = rowdom.getElementsByTagName("referenceDir")[0]

        referenceDirStr = referenceDirNode.firstChild.data.strip()

        self._referenceDir = Parser.stringListToLists(
            referenceDirStr, Angle, "Field", True
        )

        timeNode = rowdom.getElementsByTagName("time")
        if len(timeNode) > 0:

            self._time = ArrayTime(timeNode[0].firstChild.data.strip())

            self._timeExists = True

        codeNode = rowdom.getElementsByTagName("code")
        if len(codeNode) > 0:

            self._code = str(codeNode[0].firstChild.data.strip())

            self._codeExists = True

        directionCodeNode = rowdom.getElementsByTagName("directionCode")
        if len(directionCodeNode) > 0:

            self._directionCode = DirectionReferenceCode.newDirectionReferenceCode(
                directionCodeNode[0].firstChild.data.strip()
            )

            self._directionCodeExists = True

        directionEquinoxNode = rowdom.getElementsByTagName("directionEquinox")
        if len(directionEquinoxNode) > 0:

            self._directionEquinox = ArrayTime(
                directionEquinoxNode[0].firstChild.data.strip()
            )

            self._directionEquinoxExists = True

        assocNatureNode = rowdom.getElementsByTagName("assocNature")
        if len(assocNatureNode) > 0:

            self._assocNature = str(assocNatureNode[0].firstChild.data.strip())

            self._assocNatureExists = True

        # extrinsic attribute values

        assocFieldIdNode = rowdom.getElementsByTagName("assocFieldId")
        if len(assocFieldIdNode) > 0:

            self._assocFieldId = Tag(assocFieldIdNode[0].firstChild.data.strip())

            self._assocFieldIdExists = True

        ephemerisIdNode = rowdom.getElementsByTagName("ephemerisId")
        if len(ephemerisIdNode) > 0:

            self._ephemerisId = int(ephemerisIdNode[0].firstChild.data.strip())

            self._ephemerisIdExists = True

        sourceIdNode = rowdom.getElementsByTagName("sourceId")
        if len(sourceIdNode) > 0:

            self._sourceId = int(sourceIdNode[0].firstChild.data.strip())

            self._sourceIdExists = True

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._fieldId.toBin(eos)

        eos.writeStr(self._fieldName)

        eos.writeInt(self._numPoly)

        Angle.listToBin(self._delayDir, eos)

        Angle.listToBin(self._phaseDir, eos)

        Angle.listToBin(self._referenceDir, eos)

        eos.writeBool(self._timeExists)
        if self._timeExists:

            self._time.toBin(eos)

        eos.writeBool(self._codeExists)
        if self._codeExists:

            eos.writeStr(self._code)

        eos.writeBool(self._directionCodeExists)
        if self._directionCodeExists:

            eos.writeString(self._directionCode.toString())

        eos.writeBool(self._directionEquinoxExists)
        if self._directionEquinoxExists:

            self._directionEquinox.toBin(eos)

        eos.writeBool(self._assocNatureExists)
        if self._assocNatureExists:

            eos.writeStr(self._assocNature)

        eos.writeBool(self._ephemerisIdExists)
        if self._ephemerisIdExists:

            eos.writeInt(self._ephemerisId)

        eos.writeBool(self._sourceIdExists)
        if self._sourceIdExists:

            eos.writeInt(self._sourceId)

        eos.writeBool(self._assocFieldIdExists)
        if self._assocFieldIdExists:

            self._assocFieldId.toBin(eos)

    @staticmethod
    def fieldIdFromBin(row, eis):
        """
        Set the fieldId in row from the EndianInput (eis) instance.
        """

        row._fieldId = Tag.fromBin(eis)

    @staticmethod
    def fieldNameFromBin(row, eis):
        """
        Set the fieldName in row from the EndianInput (eis) instance.
        """

        row._fieldName = eis.readStr()

    @staticmethod
    def numPolyFromBin(row, eis):
        """
        Set the numPoly in row from the EndianInput (eis) instance.
        """

        row._numPoly = eis.readInt()

    @staticmethod
    def delayDirFromBin(row, eis):
        """
        Set the delayDir in row from the EndianInput (eis) instance.
        """

        row._delayDir = Angle.from2DBin(eis)

    @staticmethod
    def phaseDirFromBin(row, eis):
        """
        Set the phaseDir in row from the EndianInput (eis) instance.
        """

        row._phaseDir = Angle.from2DBin(eis)

    @staticmethod
    def referenceDirFromBin(row, eis):
        """
        Set the referenceDir in row from the EndianInput (eis) instance.
        """

        row._referenceDir = Angle.from2DBin(eis)

    @staticmethod
    def timeFromBin(row, eis):
        """
        Set the optional time in row from the EndianInput (eis) instance.
        """
        row._timeExists = eis.readBool()
        if row._timeExists:

            row._time = ArrayTime.fromBin(eis)

    @staticmethod
    def codeFromBin(row, eis):
        """
        Set the optional code in row from the EndianInput (eis) instance.
        """
        row._codeExists = eis.readBool()
        if row._codeExists:

            row._code = eis.readStr()

    @staticmethod
    def directionCodeFromBin(row, eis):
        """
        Set the optional directionCode in row from the EndianInput (eis) instance.
        """
        row._directionCodeExists = eis.readBool()
        if row._directionCodeExists:

            row._directionCode = DirectionReferenceCode.from_int(eis.readInt())

    @staticmethod
    def directionEquinoxFromBin(row, eis):
        """
        Set the optional directionEquinox in row from the EndianInput (eis) instance.
        """
        row._directionEquinoxExists = eis.readBool()
        if row._directionEquinoxExists:

            row._directionEquinox = ArrayTime.fromBin(eis)

    @staticmethod
    def assocNatureFromBin(row, eis):
        """
        Set the optional assocNature in row from the EndianInput (eis) instance.
        """
        row._assocNatureExists = eis.readBool()
        if row._assocNatureExists:

            row._assocNature = eis.readStr()

    @staticmethod
    def ephemerisIdFromBin(row, eis):
        """
        Set the optional ephemerisId in row from the EndianInput (eis) instance.
        """
        row._ephemerisIdExists = eis.readBool()
        if row._ephemerisIdExists:

            row._ephemerisId = eis.readInt()

    @staticmethod
    def sourceIdFromBin(row, eis):
        """
        Set the optional sourceId in row from the EndianInput (eis) instance.
        """
        row._sourceIdExists = eis.readBool()
        if row._sourceIdExists:

            row._sourceId = eis.readInt()

    @staticmethod
    def assocFieldIdFromBin(row, eis):
        """
        Set the optional assocFieldId in row from the EndianInput (eis) instance.
        """
        row._assocFieldIdExists = eis.readBool()
        if row._assocFieldIdExists:

            row._assocFieldId = Tag.fromBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["fieldId"] = FieldRow.fieldIdFromBin
        _fromBinMethods["fieldName"] = FieldRow.fieldNameFromBin
        _fromBinMethods["numPoly"] = FieldRow.numPolyFromBin
        _fromBinMethods["delayDir"] = FieldRow.delayDirFromBin
        _fromBinMethods["phaseDir"] = FieldRow.phaseDirFromBin
        _fromBinMethods["referenceDir"] = FieldRow.referenceDirFromBin

        _fromBinMethods["time"] = FieldRow.timeFromBin
        _fromBinMethods["code"] = FieldRow.codeFromBin
        _fromBinMethods["directionCode"] = FieldRow.directionCodeFromBin
        _fromBinMethods["directionEquinox"] = FieldRow.directionEquinoxFromBin
        _fromBinMethods["assocNature"] = FieldRow.assocNatureFromBin
        _fromBinMethods["ephemerisId"] = FieldRow.ephemerisIdFromBin
        _fromBinMethods["sourceId"] = FieldRow.sourceIdFromBin
        _fromBinMethods["assocFieldId"] = FieldRow.assocFieldIdFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = FieldRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Field",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute fieldId

    _fieldId = Tag()

    def getFieldId(self):
        """
        Get fieldId.
        return fieldId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._fieldId)

    def setFieldId(self, fieldId):
        """
        Set fieldId with the specified Tag value.
        fieldId The Tag value to which fieldId is to be set.
        The value of fieldId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the fieldId field, which is part of the key, after this row has been added to this table."
            )

        self._fieldId = Tag(fieldId)

    # ===> Attribute fieldName

    _fieldName = None

    def getFieldName(self):
        """
        Get fieldName.
        return fieldName as str
        """

        return self._fieldName

    def setFieldName(self, fieldName):
        """
        Set fieldName with the specified str value.
        fieldName The str value to which fieldName is to be set.


        """

        self._fieldName = str(fieldName)

    # ===> Attribute numPoly

    _numPoly = 0

    def getNumPoly(self):
        """
        Get numPoly.
        return numPoly as int
        """

        return self._numPoly

    def setNumPoly(self, numPoly):
        """
        Set numPoly with the specified int value.
        numPoly The int value to which numPoly is to be set.


        """

        self._numPoly = int(numPoly)

    # ===> Attribute delayDir

    _delayDir = None  # this is a 2D list of Angle

    def getDelayDir(self):
        """
        Get delayDir.
        return delayDir as Angle []  []
        """

        return copy.deepcopy(self._delayDir)

    def setDelayDir(self, delayDir):
        """
        Set delayDir with the specified Angle []  []  value.
        delayDir The Angle []  []  value to which delayDir is to be set.
        The value of delayDir can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(delayDir, list):
            raise ValueError("The value of delayDir must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(delayDir)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of delayDir is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(delayDir, Angle):
                raise ValueError(
                    "type of the first value in delayDir is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._delayDir = copy.deepcopy(delayDir)
        except Exception as exc:
            raise ValueError("Invalid delayDir : " + str(exc))

    # ===> Attribute phaseDir

    _phaseDir = None  # this is a 2D list of Angle

    def getPhaseDir(self):
        """
        Get phaseDir.
        return phaseDir as Angle []  []
        """

        return copy.deepcopy(self._phaseDir)

    def setPhaseDir(self, phaseDir):
        """
        Set phaseDir with the specified Angle []  []  value.
        phaseDir The Angle []  []  value to which phaseDir is to be set.
        The value of phaseDir can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(phaseDir, list):
            raise ValueError("The value of phaseDir must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(phaseDir)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of phaseDir is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(phaseDir, Angle):
                raise ValueError(
                    "type of the first value in phaseDir is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phaseDir = copy.deepcopy(phaseDir)
        except Exception as exc:
            raise ValueError("Invalid phaseDir : " + str(exc))

    # ===> Attribute referenceDir

    _referenceDir = None  # this is a 2D list of Angle

    def getReferenceDir(self):
        """
        Get referenceDir.
        return referenceDir as Angle []  []
        """

        return copy.deepcopy(self._referenceDir)

    def setReferenceDir(self, referenceDir):
        """
        Set referenceDir with the specified Angle []  []  value.
        referenceDir The Angle []  []  value to which referenceDir is to be set.
        The value of referenceDir can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(referenceDir, list):
            raise ValueError("The value of referenceDir must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(referenceDir)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of referenceDir is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(referenceDir, Angle):
                raise ValueError(
                    "type of the first value in referenceDir is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._referenceDir = copy.deepcopy(referenceDir)
        except Exception as exc:
            raise ValueError("Invalid referenceDir : " + str(exc))

    # ===> Attribute time, which is optional
    _timeExists = False

    _time = ArrayTime()

    def isTimeExists(self):
        """
        The attribute time is optional. Return True if this attribute exists.
        return True if and only if the time attribute exists.
        """
        return self._timeExists

    def getTime(self):
        """
        Get time, which is optional.
        return time as ArrayTime
        raises ValueError If time does not exist.
        """
        if not self._timeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + time
                + " attribute in table Field does not exist!"
            )

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._time)

    def setTime(self, time):
        """
        Set time with the specified ArrayTime value.
        time The ArrayTime value to which time is to be set.
        The value of time can be anything allowed by the ArrayTime constructor.

        """

        self._time = ArrayTime(time)

        self._timeExists = True

    def clearTime(self):
        """
        Mark time, which is an optional field, as non-existent.
        """
        self._timeExists = False

    # ===> Attribute code, which is optional
    _codeExists = False

    _code = None

    def isCodeExists(self):
        """
        The attribute code is optional. Return True if this attribute exists.
        return True if and only if the code attribute exists.
        """
        return self._codeExists

    def getCode(self):
        """
        Get code, which is optional.
        return code as str
        raises ValueError If code does not exist.
        """
        if not self._codeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + code
                + " attribute in table Field does not exist!"
            )

        return self._code

    def setCode(self, code):
        """
        Set code with the specified str value.
        code The str value to which code is to be set.


        """

        self._code = str(code)

        self._codeExists = True

    def clearCode(self):
        """
        Mark code, which is an optional field, as non-existent.
        """
        self._codeExists = False

    # ===> Attribute directionCode, which is optional
    _directionCodeExists = False

    _directionCode = DirectionReferenceCode.from_int(0)

    def isDirectionCodeExists(self):
        """
        The attribute directionCode is optional. Return True if this attribute exists.
        return True if and only if the directionCode attribute exists.
        """
        return self._directionCodeExists

    def getDirectionCode(self):
        """
        Get directionCode, which is optional.
        return directionCode as DirectionReferenceCode
        raises ValueError If directionCode does not exist.
        """
        if not self._directionCodeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + directionCode
                + " attribute in table Field does not exist!"
            )

        return self._directionCode

    def setDirectionCode(self, directionCode):
        """
        Set directionCode with the specified DirectionReferenceCode value.
        directionCode The DirectionReferenceCode value to which directionCode is to be set.


        """

        self._directionCode = DirectionReferenceCode(directionCode)

        self._directionCodeExists = True

    def clearDirectionCode(self):
        """
        Mark directionCode, which is an optional field, as non-existent.
        """
        self._directionCodeExists = False

    # ===> Attribute directionEquinox, which is optional
    _directionEquinoxExists = False

    _directionEquinox = ArrayTime()

    def isDirectionEquinoxExists(self):
        """
        The attribute directionEquinox is optional. Return True if this attribute exists.
        return True if and only if the directionEquinox attribute exists.
        """
        return self._directionEquinoxExists

    def getDirectionEquinox(self):
        """
        Get directionEquinox, which is optional.
        return directionEquinox as ArrayTime
        raises ValueError If directionEquinox does not exist.
        """
        if not self._directionEquinoxExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + directionEquinox
                + " attribute in table Field does not exist!"
            )

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._directionEquinox)

    def setDirectionEquinox(self, directionEquinox):
        """
        Set directionEquinox with the specified ArrayTime value.
        directionEquinox The ArrayTime value to which directionEquinox is to be set.
        The value of directionEquinox can be anything allowed by the ArrayTime constructor.

        """

        self._directionEquinox = ArrayTime(directionEquinox)

        self._directionEquinoxExists = True

    def clearDirectionEquinox(self):
        """
        Mark directionEquinox, which is an optional field, as non-existent.
        """
        self._directionEquinoxExists = False

    # ===> Attribute assocNature, which is optional
    _assocNatureExists = False

    _assocNature = None

    def isAssocNatureExists(self):
        """
        The attribute assocNature is optional. Return True if this attribute exists.
        return True if and only if the assocNature attribute exists.
        """
        return self._assocNatureExists

    def getAssocNature(self):
        """
        Get assocNature, which is optional.
        return assocNature as str
        raises ValueError If assocNature does not exist.
        """
        if not self._assocNatureExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + assocNature
                + " attribute in table Field does not exist!"
            )

        return self._assocNature

    def setAssocNature(self, assocNature):
        """
        Set assocNature with the specified str value.
        assocNature The str value to which assocNature is to be set.


        """

        self._assocNature = str(assocNature)

        self._assocNatureExists = True

    def clearAssocNature(self):
        """
        Mark assocNature, which is an optional field, as non-existent.
        """
        self._assocNatureExists = False

    # Extrinsic Table Attributes

    # ===> Attribute assocFieldId, which is optional
    _assocFieldIdExists = False

    _assocFieldId = Tag()

    def isAssocFieldIdExists(self):
        """
        The attribute assocFieldId is optional. Return True if this attribute exists.
        return True if and only if the assocFieldId attribute exists.
        """
        return self._assocFieldIdExists

    def getAssocFieldId(self):
        """
        Get assocFieldId, which is optional.
        return assocFieldId as Tag
        raises ValueError If assocFieldId does not exist.
        """
        if not self._assocFieldIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + assocFieldId
                + " attribute in table Field does not exist!"
            )

        # make sure it is a copy of Tag
        return Tag(self._assocFieldId)

    def setAssocFieldId(self, assocFieldId):
        """
        Set assocFieldId with the specified Tag value.
        assocFieldId The Tag value to which assocFieldId is to be set.
        The value of assocFieldId can be anything allowed by the Tag constructor.

        """

        self._assocFieldId = Tag(assocFieldId)

        self._assocFieldIdExists = True

    def clearAssocFieldId(self):
        """
        Mark assocFieldId, which is an optional field, as non-existent.
        """
        self._assocFieldIdExists = False

    # ===> Attribute ephemerisId, which is optional
    _ephemerisIdExists = False

    _ephemerisId = 0

    def isEphemerisIdExists(self):
        """
        The attribute ephemerisId is optional. Return True if this attribute exists.
        return True if and only if the ephemerisId attribute exists.
        """
        return self._ephemerisIdExists

    def getEphemerisId(self):
        """
        Get ephemerisId, which is optional.
        return ephemerisId as int
        raises ValueError If ephemerisId does not exist.
        """
        if not self._ephemerisIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + ephemerisId
                + " attribute in table Field does not exist!"
            )

        return self._ephemerisId

    def setEphemerisId(self, ephemerisId):
        """
        Set ephemerisId with the specified int value.
        ephemerisId The int value to which ephemerisId is to be set.


        """

        self._ephemerisId = int(ephemerisId)

        self._ephemerisIdExists = True

    def clearEphemerisId(self):
        """
        Mark ephemerisId, which is an optional field, as non-existent.
        """
        self._ephemerisIdExists = False

    # ===> Attribute sourceId, which is optional
    _sourceIdExists = False

    _sourceId = 0

    def isSourceIdExists(self):
        """
        The attribute sourceId is optional. Return True if this attribute exists.
        return True if and only if the sourceId attribute exists.
        """
        return self._sourceIdExists

    def getSourceId(self):
        """
        Get sourceId, which is optional.
        return sourceId as int
        raises ValueError If sourceId does not exist.
        """
        if not self._sourceIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sourceId
                + " attribute in table Field does not exist!"
            )

        return self._sourceId

    def setSourceId(self, sourceId):
        """
        Set sourceId with the specified int value.
        sourceId The int value to which sourceId is to be set.


        """

        self._sourceId = int(sourceId)

        self._sourceIdExists = True

    def clearSourceId(self):
        """
        Mark sourceId, which is an optional field, as non-existent.
        """
        self._sourceIdExists = False

    # Links

    # ===> Slice link from a row of Field table to a collection of row of Source table.
    def getSources(self):
        """
        Get the collection of rows in the Source table having sourceId == this.sourceId
        """

        if not self._sourceIdExists:
            raise InvalidAccessException()

        return self._table.getContainer().getSource().getRowBySourceId(self._sourceId)

    def getFieldUsingAssocFieldId(self):
        """
        Returns the row in the Field table having Field.assocFieldId == assocFieldId

        Raises ValueError if the optional assocFieldId does not exist for this row.

        """

        if not self._assocFieldIdExists:
            raise ValueError("assocFieldId does not exist for this row.")

        return self._table.getContainer().getField().getRowByKey(self._assocFieldId)

    # comparison methods

    def compareNoAutoInc(self, fieldName, numPoly, delayDir, phaseDir, referenceDir):
        """
        Compare each attribute except the autoincrementable one of this FieldRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # fieldName is a str, compare using the == operator.
        if not (self._fieldName == fieldName):
            return False

        # numPoly is a int, compare using the == operator.
        if not (self._numPoly == numPoly):
            return False

        # We compare two 2D arrays (lists).
        if delayDir is not None:
            if self._delayDir is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            delayDir_dims = pyasdm.utils.getListDims(delayDir)
            this_delayDir_dims = pyasdm.utils.getListDims(self._delayDir)
            if delayDir_dims != this_delayDir_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(delayDir_dims[0]):
                for j in range(delayDir_dims[1]):

                    # delayDir is a Angle, compare using the almostEquals method.
                    if not (
                        self._delayDir[i][j].almostEquals(
                            delayDir[i][j], self.getTable().getDelayDirEqTolerance()
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if phaseDir is not None:
            if self._phaseDir is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            phaseDir_dims = pyasdm.utils.getListDims(phaseDir)
            this_phaseDir_dims = pyasdm.utils.getListDims(self._phaseDir)
            if phaseDir_dims != this_phaseDir_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(phaseDir_dims[0]):
                for j in range(phaseDir_dims[1]):

                    # phaseDir is a Angle, compare using the almostEquals method.
                    if not (
                        self._phaseDir[i][j].almostEquals(
                            phaseDir[i][j], self.getTable().getPhaseDirEqTolerance()
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if referenceDir is not None:
            if self._referenceDir is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            referenceDir_dims = pyasdm.utils.getListDims(referenceDir)
            this_referenceDir_dims = pyasdm.utils.getListDims(self._referenceDir)
            if referenceDir_dims != this_referenceDir_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(referenceDir_dims[0]):
                for j in range(referenceDir_dims[1]):

                    # referenceDir is a Angle, compare using the almostEquals method.
                    if not (
                        self._referenceDir[i][j].almostEquals(
                            referenceDir[i][j],
                            self.getTable().getReferenceDirEqTolerance(),
                        )
                    ):
                        return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getFieldName(),
            otherRow.getNumPoly(),
            otherRow.getDelayDir(),
            otherRow.getPhaseDir(),
            otherRow.getReferenceDir(),
        )

    def compareRequiredValue(
        self, fieldName, numPoly, delayDir, phaseDir, referenceDir
    ):

        # fieldName is a str, compare using the == operator.
        if not (self._fieldName == fieldName):
            return False

        # numPoly is a int, compare using the == operator.
        if not (self._numPoly == numPoly):
            return False

        # We compare two 2D arrays (lists).
        if delayDir is not None:
            if self._delayDir is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            delayDir_dims = pyasdm.utils.getListDims(delayDir)
            this_delayDir_dims = pyasdm.utils.getListDims(self._delayDir)
            if delayDir_dims != this_delayDir_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(delayDir_dims[0]):
                for j in range(delayDir_dims[1]):

                    # delayDir is a Angle, compare using the almostEquals method.
                    if not (
                        self._delayDir[i][j].almostEquals(
                            delayDir[i][j], self.getTable().getDelayDirEqTolerance()
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if phaseDir is not None:
            if self._phaseDir is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            phaseDir_dims = pyasdm.utils.getListDims(phaseDir)
            this_phaseDir_dims = pyasdm.utils.getListDims(self._phaseDir)
            if phaseDir_dims != this_phaseDir_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(phaseDir_dims[0]):
                for j in range(phaseDir_dims[1]):

                    # phaseDir is a Angle, compare using the almostEquals method.
                    if not (
                        self._phaseDir[i][j].almostEquals(
                            phaseDir[i][j], self.getTable().getPhaseDirEqTolerance()
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if referenceDir is not None:
            if self._referenceDir is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            referenceDir_dims = pyasdm.utils.getListDims(referenceDir)
            this_referenceDir_dims = pyasdm.utils.getListDims(self._referenceDir)
            if referenceDir_dims != this_referenceDir_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(referenceDir_dims[0]):
                for j in range(referenceDir_dims[1]):

                    # referenceDir is a Angle, compare using the almostEquals method.
                    if not (
                        self._referenceDir[i][j].almostEquals(
                            referenceDir[i][j],
                            self.getTable().getReferenceDirEqTolerance(),
                        )
                    ):
                        return False

        return True


# initialize the dictionary that maps fields to init methods
FieldRow.initFromBinMethods()
