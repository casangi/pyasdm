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
# File CalDataRow.py
#

import pyasdm.CalDataTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.CalDataOrigin import CalDataOrigin


from pyasdm.enumerations.CalType import CalType


from pyasdm.enumerations.AssociatedCalNature import AssociatedCalNature


from pyasdm.enumerations.ScanIntent import ScanIntent


from xml.dom import minidom

import copy


class CalDataRow:
    """
    The CalDataRow class is a row of a CalDataTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalDataRow.
        When row is None, create an empty row attached to table, which must be a CalDataTable.
        When row is given, copy those values in to the new row. The row argument must be a CalDataRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalDataTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._calDataId = Tag()

        self._startTimeObserved = ArrayTime()

        self._endTimeObserved = ArrayTime()

        self._execBlockUID = EntityRef()

        self._calDataType = CalDataOrigin.from_int(0)

        self._calType = CalType.from_int(0)

        self._numScan = 0

        self._scanSet = []  # this is a list of int []

        self._assocCalDataIdExists = False

        self._assocCalDataId = Tag()

        self._assocCalNatureExists = False

        self._assocCalNature = AssociatedCalNature.from_int(0)

        self._fieldNameExists = False

        self._fieldName = []  # this is a list of str []

        self._sourceNameExists = False

        self._sourceName = []  # this is a list of str []

        self._sourceCodeExists = False

        self._sourceCode = []  # this is a list of str []

        self._scanIntentExists = False

        self._scanIntent = []  # this is a list of ScanIntent []

        if row is not None:
            if not isinstance(row, CalDataRow):
                raise ValueError("row must be a MainRow")

            # copy constructor

            self._calDataId = Tag(row._calDataId)

            self._startTimeObserved = ArrayTime(row._startTimeObserved)

            self._endTimeObserved = ArrayTime(row._endTimeObserved)

            self._execBlockUID = EntityRef(row._execBlockUID)

            # We force the attribute of the result to be not None
            if row._calDataType is None:
                self._calDataType = CalDataOrigin.from_int(0)
            else:
                self._calDataType = CalDataOrigin(row._calDataType)

            # We force the attribute of the result to be not None
            if row._calType is None:
                self._calType = CalType.from_int(0)
            else:
                self._calType = CalType(row._calType)

            self._numScan = row._numScan

            # scanSet is a  list , make a deep copy
            self._scanSet = copy.deepcopy(row._scanSet)

            # by default set systematically assocCalDataId's value to something not None

            if row._assocCalDataIdExists:

                self._assocCalDataId = Tag(row._assocCalDataId)

                self._assocCalDataIdExists = True

            # by default set systematically assocCalNature's value to something not None

            self.assocCalNature = AssociatedCalNature.from_int(0)

            if row._assocCalNatureExists:

                if row._assocCalNature is None:
                    self._assocCalNature = row._assocCalNature

                self._assocCalNatureExists = True

            # by default set systematically fieldName's value to something not None

            if row._fieldNameExists:

                # fieldName is a list, make a deep copy
                self.fieldName = copy.deepcopy(row.fieldName)

                self._fieldNameExists = True

            # by default set systematically sourceName's value to something not None

            if row._sourceNameExists:

                # sourceName is a list, make a deep copy
                self.sourceName = copy.deepcopy(row.sourceName)

                self._sourceNameExists = True

            # by default set systematically sourceCode's value to something not None

            if row._sourceCodeExists:

                # sourceCode is a list, make a deep copy
                self.sourceCode = copy.deepcopy(row.sourceCode)

                self._sourceCodeExists = True

            # by default set systematically scanIntent's value to something not None

            if row._scanIntentExists:

                # scanIntent is a list, make a deep copy
                self.scanIntent = copy.deepcopy(row.scanIntent)

                self._scanIntentExists = True

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

        result += Parser.extendedValueToXML("calDataId", self._calDataId)

        result += Parser.extendedValueToXML(
            "startTimeObserved", self._startTimeObserved
        )

        result += Parser.extendedValueToXML("endTimeObserved", self._endTimeObserved)

        result += Parser.extendedValueToXML("execBlockUID", self._execBlockUID)

        result += Parser.valueToXML(
            "calDataType", CalDataOrigin.name(self._calDataType)
        )

        result += Parser.valueToXML("calType", CalType.name(self._calType))

        result += Parser.valueToXML("numScan", self._numScan)

        result += Parser.listValueToXML("scanSet", self._scanSet)

        if self._assocCalDataIdExists:

            result += Parser.extendedValueToXML("assocCalDataId", self._assocCalDataId)

        if self._assocCalNatureExists:

            result += Parser.valueToXML(
                "assocCalNature", AssociatedCalNature.name(self._assocCalNature)
            )

        if self._fieldNameExists:

            result += Parser.listValueToXML("fieldName", self._fieldName)

        if self._sourceNameExists:

            result += Parser.listValueToXML("sourceName", self._sourceName)

        if self._sourceCodeExists:

            result += Parser.listValueToXML("sourceCode", self._sourceCode)

        if self._scanIntentExists:

            result += Parser.listEnumValueToXML("scanIntent", self._scanIntent)

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
                "xmlrow is not a string or a minidom.Element", "CalDataTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalDataTable")

        # intrinsic attribute values

        calDataIdNode = rowdom.getElementsByTagName("calDataId")[0]

        self._calDataId = Tag(calDataIdNode.firstChild.data.strip())

        startTimeObservedNode = rowdom.getElementsByTagName("startTimeObserved")[0]

        self._startTimeObserved = ArrayTime(
            startTimeObservedNode.firstChild.data.strip()
        )

        endTimeObservedNode = rowdom.getElementsByTagName("endTimeObserved")[0]

        self._endTimeObserved = ArrayTime(endTimeObservedNode.firstChild.data.strip())

        execBlockUIDNode = rowdom.getElementsByTagName("execBlockUID")[0]

        self._execBlockUID = EntityRef(execBlockUIDNode.toxml())

        calDataTypeNode = rowdom.getElementsByTagName("calDataType")[0]

        self._calDataType = CalDataOrigin.newCalDataOrigin(
            calDataTypeNode.firstChild.data.strip()
        )

        calTypeNode = rowdom.getElementsByTagName("calType")[0]

        self._calType = CalType.newCalType(calTypeNode.firstChild.data.strip())

        numScanNode = rowdom.getElementsByTagName("numScan")[0]

        self._numScan = int(numScanNode.firstChild.data.strip())

        scanSetNode = rowdom.getElementsByTagName("scanSet")[0]

        scanSetStr = scanSetNode.firstChild.data.strip()

        self._scanSet = Parser.stringListToLists(scanSetStr, int, "CalData", False)

        assocCalDataIdNode = rowdom.getElementsByTagName("assocCalDataId")
        if len(assocCalDataIdNode) > 0:

            self._assocCalDataId = Tag(assocCalDataIdNode[0].firstChild.data.strip())

            self._assocCalDataIdExists = True

        assocCalNatureNode = rowdom.getElementsByTagName("assocCalNature")
        if len(assocCalNatureNode) > 0:

            self._assocCalNature = AssociatedCalNature.newAssociatedCalNature(
                assocCalNatureNode[0].firstChild.data.strip()
            )

            self._assocCalNatureExists = True

        fieldNameNode = rowdom.getElementsByTagName("fieldName")
        if len(fieldNameNode) > 0:

            fieldNameStr = fieldNameNode[0].firstChild.data.strip()

            self._fieldName = Parser.stringListToLists(
                fieldNameStr, str, "CalData", False
            )

            self._fieldNameExists = True

        sourceNameNode = rowdom.getElementsByTagName("sourceName")
        if len(sourceNameNode) > 0:

            sourceNameStr = sourceNameNode[0].firstChild.data.strip()

            self._sourceName = Parser.stringListToLists(
                sourceNameStr, str, "CalData", False
            )

            self._sourceNameExists = True

        sourceCodeNode = rowdom.getElementsByTagName("sourceCode")
        if len(sourceCodeNode) > 0:

            sourceCodeStr = sourceCodeNode[0].firstChild.data.strip()

            self._sourceCode = Parser.stringListToLists(
                sourceCodeStr, str, "CalData", False
            )

            self._sourceCodeExists = True

        scanIntentNode = rowdom.getElementsByTagName("scanIntent")
        if len(scanIntentNode) > 0:

            scanIntentStr = scanIntentNode[0].firstChild.data.strip()
            self._scanIntent = Parser.stringListToLists(
                scanIntentStr, ScanIntent, "CalData", False
            )

            self._scanIntentExists = True

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

    # ===> Attribute calDataId

    _calDataId = Tag()

    def getCalDataId(self):
        """
        Get calDataId.
        return calDataId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._calDataId)

    def setCalDataId(self, calDataId):
        """
        Set calDataId with the specified Tag value.
        calDataId The Tag value to which calDataId is to be set.
        The value of calDataId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the calDataId field, which is part of the key, after this row has been added to this table."
            )

        self._calDataId = Tag(calDataId)

    # ===> Attribute startTimeObserved

    _startTimeObserved = ArrayTime()

    def getStartTimeObserved(self):
        """
        Get startTimeObserved.
        return startTimeObserved as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._startTimeObserved)

    def setStartTimeObserved(self, startTimeObserved):
        """
        Set startTimeObserved with the specified ArrayTime value.
        startTimeObserved The ArrayTime value to which startTimeObserved is to be set.
        The value of startTimeObserved can be anything allowed by the ArrayTime constructor.

        """

        self._startTimeObserved = ArrayTime(startTimeObserved)

    # ===> Attribute endTimeObserved

    _endTimeObserved = ArrayTime()

    def getEndTimeObserved(self):
        """
        Get endTimeObserved.
        return endTimeObserved as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._endTimeObserved)

    def setEndTimeObserved(self, endTimeObserved):
        """
        Set endTimeObserved with the specified ArrayTime value.
        endTimeObserved The ArrayTime value to which endTimeObserved is to be set.
        The value of endTimeObserved can be anything allowed by the ArrayTime constructor.

        """

        self._endTimeObserved = ArrayTime(endTimeObserved)

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

    # ===> Attribute calDataType

    _calDataType = CalDataOrigin.from_int(0)

    def getCalDataType(self):
        """
        Get calDataType.
        return calDataType as CalDataOrigin
        """

        return self._calDataType

    def setCalDataType(self, calDataType):
        """
        Set calDataType with the specified CalDataOrigin value.
        calDataType The CalDataOrigin value to which calDataType is to be set.


        """

        self._calDataType = CalDataOrigin(calDataType)

    # ===> Attribute calType

    _calType = CalType.from_int(0)

    def getCalType(self):
        """
        Get calType.
        return calType as CalType
        """

        return self._calType

    def setCalType(self, calType):
        """
        Set calType with the specified CalType value.
        calType The CalType value to which calType is to be set.


        """

        self._calType = CalType(calType)

    # ===> Attribute numScan

    _numScan = 0

    def getNumScan(self):
        """
        Get numScan.
        return numScan as int
        """

        return self._numScan

    def setNumScan(self, numScan):
        """
        Set numScan with the specified int value.
        numScan The int value to which numScan is to be set.


        """

        self._numScan = int(numScan)

    # ===> Attribute scanSet

    _scanSet = None  # this is a 1D list of int

    def getScanSet(self):
        """
        Get scanSet.
        return scanSet as int []
        """

        return copy.deepcopy(self._scanSet)

    def setScanSet(self, scanSet):
        """
        Set scanSet with the specified int []  value.
        scanSet The int []  value to which scanSet is to be set.


        """

        # value must be a list
        if not isinstance(scanSet, list):
            raise ValueError("The value of scanSet must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(scanSet)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of scanSet is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not Parser.checkListType(scanSet, int):
                raise ValueError(
                    "type of the first value in scanSet is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._scanSet = copy.deepcopy(scanSet)
        except Exception as exc:
            raise ValueError("Invalid scanSet : " + str(exc))

    # ===> Attribute assocCalDataId, which is optional
    _assocCalDataIdExists = False

    _assocCalDataId = Tag()

    def isAssocCalDataIdExists(self):
        """
        The attribute assocCalDataId is optional. Return True if this attribute exists.
        return True if and only if the assocCalDataId attribute exists.
        """
        return self._assocCalDataIdExists

    def getAssocCalDataId(self):
        """
        Get assocCalDataId, which is optional.
        return assocCalDataId as Tag
        raises ValueError If assocCalDataId does not exist.
        """
        if not self._assocCalDataIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + assocCalDataId
                + " attribute in table CalData does not exist!"
            )

        # make sure it is a copy of Tag
        return Tag(self._assocCalDataId)

    def setAssocCalDataId(self, assocCalDataId):
        """
        Set assocCalDataId with the specified Tag value.
        assocCalDataId The Tag value to which assocCalDataId is to be set.
        The value of assocCalDataId can be anything allowed by the Tag constructor.

        """

        self._assocCalDataId = Tag(assocCalDataId)

        self._assocCalDataIdExists = True

    def clearAssocCalDataId(self):
        """
        Mark assocCalDataId, which is an optional field, as non-existent.
        """
        self._assocCalDataIdExists = False

    # ===> Attribute assocCalNature, which is optional
    _assocCalNatureExists = False

    _assocCalNature = AssociatedCalNature.from_int(0)

    def isAssocCalNatureExists(self):
        """
        The attribute assocCalNature is optional. Return True if this attribute exists.
        return True if and only if the assocCalNature attribute exists.
        """
        return self._assocCalNatureExists

    def getAssocCalNature(self):
        """
        Get assocCalNature, which is optional.
        return assocCalNature as AssociatedCalNature
        raises ValueError If assocCalNature does not exist.
        """
        if not self._assocCalNatureExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + assocCalNature
                + " attribute in table CalData does not exist!"
            )

        return self._assocCalNature

    def setAssocCalNature(self, assocCalNature):
        """
        Set assocCalNature with the specified AssociatedCalNature value.
        assocCalNature The AssociatedCalNature value to which assocCalNature is to be set.


        """

        self._assocCalNature = AssociatedCalNature(assocCalNature)

        self._assocCalNatureExists = True

    def clearAssocCalNature(self):
        """
        Mark assocCalNature, which is an optional field, as non-existent.
        """
        self._assocCalNatureExists = False

    # ===> Attribute fieldName, which is optional
    _fieldNameExists = False

    _fieldName = None  # this is a 1D list of str

    def isFieldNameExists(self):
        """
        The attribute fieldName is optional. Return True if this attribute exists.
        return True if and only if the fieldName attribute exists.
        """
        return self._fieldNameExists

    def getFieldName(self):
        """
        Get fieldName, which is optional.
        return fieldName as str []
        raises ValueError If fieldName does not exist.
        """
        if not self._fieldNameExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + fieldName
                + " attribute in table CalData does not exist!"
            )

        return copy.deepcopy(self._fieldName)

    def setFieldName(self, fieldName):
        """
        Set fieldName with the specified str []  value.
        fieldName The str []  value to which fieldName is to be set.


        """

        # value must be a list
        if not isinstance(fieldName, list):
            raise ValueError("The value of fieldName must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(fieldName)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of fieldName is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not Parser.checkListType(fieldName, str):
                raise ValueError(
                    "type of the first value in fieldName is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._fieldName = copy.deepcopy(fieldName)
        except Exception as exc:
            raise ValueError("Invalid fieldName : " + str(exc))

        self._fieldNameExists = True

    def clearFieldName(self):
        """
        Mark fieldName, which is an optional field, as non-existent.
        """
        self._fieldNameExists = False

    # ===> Attribute sourceName, which is optional
    _sourceNameExists = False

    _sourceName = None  # this is a 1D list of str

    def isSourceNameExists(self):
        """
        The attribute sourceName is optional. Return True if this attribute exists.
        return True if and only if the sourceName attribute exists.
        """
        return self._sourceNameExists

    def getSourceName(self):
        """
        Get sourceName, which is optional.
        return sourceName as str []
        raises ValueError If sourceName does not exist.
        """
        if not self._sourceNameExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sourceName
                + " attribute in table CalData does not exist!"
            )

        return copy.deepcopy(self._sourceName)

    def setSourceName(self, sourceName):
        """
        Set sourceName with the specified str []  value.
        sourceName The str []  value to which sourceName is to be set.


        """

        # value must be a list
        if not isinstance(sourceName, list):
            raise ValueError("The value of sourceName must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(sourceName)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of sourceName is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not Parser.checkListType(sourceName, str):
                raise ValueError(
                    "type of the first value in sourceName is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._sourceName = copy.deepcopy(sourceName)
        except Exception as exc:
            raise ValueError("Invalid sourceName : " + str(exc))

        self._sourceNameExists = True

    def clearSourceName(self):
        """
        Mark sourceName, which is an optional field, as non-existent.
        """
        self._sourceNameExists = False

    # ===> Attribute sourceCode, which is optional
    _sourceCodeExists = False

    _sourceCode = None  # this is a 1D list of str

    def isSourceCodeExists(self):
        """
        The attribute sourceCode is optional. Return True if this attribute exists.
        return True if and only if the sourceCode attribute exists.
        """
        return self._sourceCodeExists

    def getSourceCode(self):
        """
        Get sourceCode, which is optional.
        return sourceCode as str []
        raises ValueError If sourceCode does not exist.
        """
        if not self._sourceCodeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sourceCode
                + " attribute in table CalData does not exist!"
            )

        return copy.deepcopy(self._sourceCode)

    def setSourceCode(self, sourceCode):
        """
        Set sourceCode with the specified str []  value.
        sourceCode The str []  value to which sourceCode is to be set.


        """

        # value must be a list
        if not isinstance(sourceCode, list):
            raise ValueError("The value of sourceCode must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(sourceCode)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of sourceCode is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not Parser.checkListType(sourceCode, str):
                raise ValueError(
                    "type of the first value in sourceCode is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._sourceCode = copy.deepcopy(sourceCode)
        except Exception as exc:
            raise ValueError("Invalid sourceCode : " + str(exc))

        self._sourceCodeExists = True

    def clearSourceCode(self):
        """
        Mark sourceCode, which is an optional field, as non-existent.
        """
        self._sourceCodeExists = False

    # ===> Attribute scanIntent, which is optional
    _scanIntentExists = False

    _scanIntent = None  # this is a 1D list of ScanIntent

    def isScanIntentExists(self):
        """
        The attribute scanIntent is optional. Return True if this attribute exists.
        return True if and only if the scanIntent attribute exists.
        """
        return self._scanIntentExists

    def getScanIntent(self):
        """
        Get scanIntent, which is optional.
        return scanIntent as ScanIntent []
        raises ValueError If scanIntent does not exist.
        """
        if not self._scanIntentExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + scanIntent
                + " attribute in table CalData does not exist!"
            )

        return copy.deepcopy(self._scanIntent)

    def setScanIntent(self, scanIntent):
        """
        Set scanIntent with the specified ScanIntent []  value.
        scanIntent The ScanIntent []  value to which scanIntent is to be set.


        """

        # value must be a list
        if not isinstance(scanIntent, list):
            raise ValueError("The value of scanIntent must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(scanIntent)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of scanIntent is not correct")

            # the type of the values in the list must be ScanIntent
            # note : this only checks the first value found
            if not Parser.checkListType(scanIntent, ScanIntent):
                raise ValueError(
                    "type of the first value in scanIntent is not ScanIntent as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._scanIntent = copy.deepcopy(scanIntent)
        except Exception as exc:
            raise ValueError("Invalid scanIntent : " + str(exc))

        self._scanIntentExists = True

    def clearScanIntent(self):
        """
        Mark scanIntent, which is an optional field, as non-existent.
        """
        self._scanIntentExists = False

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(
        self,
        startTimeObserved,
        endTimeObserved,
        execBlockUID,
        calDataType,
        calType,
        numScan,
        scanSet,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalDataRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # startTimeObserved is a ArrayTime, compare using the equals method.
        if not self._startTimeObserved.equals(startTimeObserved):
            return False

        # endTimeObserved is a ArrayTime, compare using the equals method.
        if not self._endTimeObserved.equals(endTimeObserved):
            return False

        # execBlockUID is a EntityRef, compare using the equals method.
        if not self._execBlockUID.equals(execBlockUID):
            return False

        # calDataType is a CalDataOrigin, compare using the == operator on the getValue() output
        if not (self._calDataType.getValue() == calDataType.getValue()):
            return False

        # calType is a CalType, compare using the == operator on the getValue() output
        if not (self._calType.getValue() == calType.getValue()):
            return False

        # numScan is a int, compare using the == operator.
        if not (self._numScan == numScan):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._scanSet) != len(scanSet):
            return False
        for indx in range(len(scanSet)):

            # scanSet is a list of int, compare using == operator.
            if not (self._scanSet[indx] == scanSet[indx]):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getStartTimeObserved(),
            otherRow.getEndTimeObserved(),
            otherRow.getExecBlockUID(),
            otherRow.getCalDataType(),
            otherRow.getCalType(),
            otherRow.getNumScan(),
            otherRow.getScanSet(),
        )

    def compareRequiredValue(
        self,
        startTimeObserved,
        endTimeObserved,
        execBlockUID,
        calDataType,
        calType,
        numScan,
        scanSet,
    ):

        # startTimeObserved is a ArrayTime, compare using the equals method.
        if not self._startTimeObserved.equals(startTimeObserved):
            return False

        # endTimeObserved is a ArrayTime, compare using the equals method.
        if not self._endTimeObserved.equals(endTimeObserved):
            return False

        # execBlockUID is a EntityRef, compare using the equals method.
        if not self._execBlockUID.equals(execBlockUID):
            return False

        # calDataType is a CalDataOrigin, compare using the == operator on the getValue() output
        if not (self._calDataType.getValue() == calDataType.getValue()):
            return False

        # calType is a CalType, compare using the == operator on the getValue() output
        if not (self._calType.getValue() == calType.getValue()):
            return False

        # numScan is a int, compare using the == operator.
        if not (self._numScan == numScan):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._scanSet) != len(scanSet):
            return False
        for indx in range(len(scanSet)):

            # scanSet is a list of int, compare using == operator.
            if not (self._scanSet[indx] == scanSet[indx]):
                return False

        return True
