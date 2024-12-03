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
# File AnnotationRow.py
#

import pyasdm.AnnotationTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.BasebandName import BasebandName


from xml.dom import minidom

import copy


class AnnotationRow:
    """
    The AnnotationRow class is a row of a AnnotationTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a AnnotationRow.
        When row is None, create an empty row attached to table, which must be a AnnotationTable.
        When row is given, copy those values in to the new row. The row argument must be a AnnotationRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.AnnotationTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # this is a list of BasebandName Enumeration, start off with it being empty
        self._basebandName = []

        if row is not None:
            if not isinstance(row, AnnotationRow):
                raise ValueError("row must be a MainRow")

            self._annotationId = Tag(row._annotationId)

            self._time = ArrayTime(row._time)

            self._issue = row._issue

            self._details = row._details

            # by default set systematically numAntenna's value to something not None

            if row._numAntennaExists:

                self._numAntenna = row._numAntenna

                self._numAntennaExists = True

            # by default set systematically basebandName's value to something not None

            if row._basebandNameExists:

                # basebandName is a list, make a deep copy
                self.basebandName = copy.deepcopy(row.basebandName)

                self._basebandNameExists = True

            # by default set systematically numBaseband's value to something not None

            if row._numBasebandExists:

                self._numBaseband = row._numBaseband

                self._numBasebandExists = True

            # by default set systematically interval's value to something not None

            if row._intervalExists:

                self._interval = Interval(row._interval)

                self._intervalExists = True

            # by default set systematically dValue's value to something not None

            if row._dValueExists:

                self._dValue = row._dValue

                self._dValueExists = True

            # by default set systematically vdValue's value to something not None

            if row._vdValueExists:

                # vdValue is a list, make a deep copy
                self.vdValue = copy.deepcopy(row.vdValue)

                self._vdValueExists = True

            # by default set systematically vvdValues's value to something not None

            if row._vvdValuesExists:

                # vvdValues is a list, make a deep copy
                self.vvdValues = copy.deepcopy(row.vvdValues)

                self._vvdValuesExists = True

            # by default set systematically llValue's value to something not None

            if row._llValueExists:

                self._llValue = row._llValue

                self._llValueExists = True

            # by default set systematically vllValue's value to something not None

            if row._vllValueExists:

                # vllValue is a list, make a deep copy
                self.vllValue = copy.deepcopy(row.vllValue)

                self._vllValueExists = True

            # by default set systematically vvllValue's value to something not None

            if row._vvllValueExists:

                # vvllValue is a list, make a deep copy
                self.vvllValue = copy.deepcopy(row.vvllValue)

                self._vvllValueExists = True

            # by default set systematically sValue's value to something not None

            if row._sValueExists:

                self._sValue = row._sValue

                self._sValueExists = True

            # by default set systematically antennaId's value to something not None

            if row._antennaIdExists:

                # antennaId is a list , let's populate self.antennaId element by element.
                if self._antennaId is None:
                    self._antennaId = []
                for i in range(len(row._antennaId)):

                    self._antennaId.append(Tag(row._antennaId[i]))

                self._antennaIdExists = True

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

        result += Parser.extendedValueToXML("annotationId", self._annotationId)

        result += Parser.extendedValueToXML("time", self._time)

        result += Parser.valueToXML("issue", self._issue)

        result += Parser.valueToXML("details", self._details)

        if self._numAntennaExists:

            result += Parser.valueToXML("numAntenna", self._numAntenna)

        if self._basebandNameExists:

            result += Parser.listEnumValueToXML("basebandName", self._basebandName)

        if self._numBasebandExists:

            result += Parser.valueToXML("numBaseband", self._numBaseband)

        if self._intervalExists:

            result += Parser.extendedValueToXML("interval", self._interval)

        if self._dValueExists:

            result += Parser.valueToXML("dValue", self._dValue)

        if self._vdValueExists:

            result += Parser.listValueToXML("vdValue", self._vdValue)

        if self._vvdValuesExists:

            result += Parser.listValueToXML("vvdValues", self._vvdValues)

        if self._llValueExists:

            result += Parser.valueToXML("llValue", self._llValue)

        if self._vllValueExists:

            result += Parser.listValueToXML("vllValue", self._vllValue)

        if self._vvllValueExists:

            result += Parser.listValueToXML("vvllValue", self._vvllValue)

        if self._sValueExists:

            result += Parser.valueToXML("sValue", self._sValue)

        # extrinsic attributes

        if self._antennaIdExists:

            result += Parser.listExtendedValueToXML("antennaId", self._antennaId)

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
                "xmlrow is not a string or a minidom.Element", "AnnotationTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "AnnotationTable")

        # intrinsic attribute values

        annotationIdNode = rowdom.getElementsByTagName("annotationId")[0]

        self._annotationId = Tag(annotationIdNode.firstChild.data)

        timeNode = rowdom.getElementsByTagName("time")[0]

        self._time = ArrayTime(timeNode.firstChild.data)

        issueNode = rowdom.getElementsByTagName("issue")[0]

        self._issue = str(issueNode.firstChild.data)

        detailsNode = rowdom.getElementsByTagName("details")[0]

        self._details = str(detailsNode.firstChild.data)

        numAntennaNode = rowdom.getElementsByTagName("numAntenna")
        if len(numAntennaNode) > 0:

            self._numAntenna = int(numAntennaNode[0].firstChild.data)

            self._numAntennaExists = True

        basebandNameNode = rowdom.getElementsByTagName("basebandName")
        if len(basebandNameNode) > 0:

            basebandNameStr = basebandNameNode[0].firstChild.data
            self._basebandName = Parser.stringListToLists(
                basebandNameStr, BasebandName, "Annotation"
            )

            self._basebandNameExists = True

        numBasebandNode = rowdom.getElementsByTagName("numBaseband")
        if len(numBasebandNode) > 0:

            self._numBaseband = int(numBasebandNode[0].firstChild.data)

            self._numBasebandExists = True

        intervalNode = rowdom.getElementsByTagName("interval")
        if len(intervalNode) > 0:

            self._interval = Interval(intervalNode[0].firstChild.data)

            self._intervalExists = True

        dValueNode = rowdom.getElementsByTagName("dValue")
        if len(dValueNode) > 0:

            self._dValue = double(dValueNode[0].firstChild.data)

            self._dValueExists = True

        vdValueNode = rowdom.getElementsByTagName("vdValue")
        if len(vdValueNode) > 0:

            vdValueStr = vdValueNode[0].firstChild.data
            self._vdValue = Parser.stringListToLists(vdValueStr, double, "Annotation")

            self._vdValueExists = True

        vvdValuesNode = rowdom.getElementsByTagName("vvdValues")
        if len(vvdValuesNode) > 0:

            vvdValuesStr = vvdValuesNode[0].firstChild.data
            self._vvdValues = Parser.stringListToLists(
                vvdValuesStr, double, "Annotation"
            )

            self._vvdValuesExists = True

        llValueNode = rowdom.getElementsByTagName("llValue")
        if len(llValueNode) > 0:

            self._llValue = int(llValueNode[0].firstChild.data)

            self._llValueExists = True

        vllValueNode = rowdom.getElementsByTagName("vllValue")
        if len(vllValueNode) > 0:

            vllValueStr = vllValueNode[0].firstChild.data
            self._vllValue = Parser.stringListToLists(vllValueStr, int, "Annotation")

            self._vllValueExists = True

        vvllValueNode = rowdom.getElementsByTagName("vvllValue")
        if len(vvllValueNode) > 0:

            vvllValueStr = vvllValueNode[0].firstChild.data
            self._vvllValue = Parser.stringListToLists(vvllValueStr, int, "Annotation")

            self._vvllValueExists = True

        sValueNode = rowdom.getElementsByTagName("sValue")
        if len(sValueNode) > 0:

            self._sValue = str(sValueNode[0].firstChild.data)

            self._sValueExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")
        if len(antennaIdNode) > 0:

            antennaIdStr = antennaIdNode[0].firstChild.data
            self._antennaId = Parser.stringListToLists(antennaIdStr, Tag, "Annotation")

            self._antennaIdExists = True

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

    # ===> Attribute annotationId

    _annotationId = Tag()

    def getAnnotationId(self):
        """
        Get annotationId.
        return annotationId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._annotationId)

    def setAnnotationId(self, annotationId):
        """
        Set annotationId with the specified Tag value.
        annotationId The Tag value to which annotationId is to be set.
        The value of annotationId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the annotationId field, which is part of the key, after this row has been added to this table."
            )

        self._annotationId = Tag(annotationId)

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

        """

        self._time = ArrayTime(time)

    # ===> Attribute issue

    _issue = None

    def getIssue(self):
        """
        Get issue.
        return issue as str
        """

        return self._issue

    def setIssue(self, issue):
        """
        Set issue with the specified str value.
        issue The str value to which issue is to be set.


        """

        self._issue = str(issue)

    # ===> Attribute details

    _details = None

    def getDetails(self):
        """
        Get details.
        return details as str
        """

        return self._details

    def setDetails(self, details):
        """
        Set details with the specified str value.
        details The str value to which details is to be set.


        """

        self._details = str(details)

    # ===> Attribute numAntenna, which is optional
    _numAntennaExists = False

    _numAntenna = 0

    def isNumAntennaExists(self):
        """
        The attribute numAntenna is optional. Return True if this attribute exists.
        return True if and only if the numAntenna attribute exists.
        """
        return self._numAntennaExists

    def getNumAntenna(self):
        """
        Get numAntenna, which is optional.
        return numAntenna as int
        raises ValueError If numAntenna does not exist.
        """
        if not self._numAntennaExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numAntenna
                + " attribute in table Annotation does not exist!"
            )

        return self._numAntenna

    def setNumAntenna(self, numAntenna):
        """
        Set numAntenna with the specified int value.
        numAntenna The int value to which numAntenna is to be set.


        """

        self._numAntenna = int(numAntenna)

        self._numAntennaExists = True

    def clearNumAntenna(self):
        """
        Mark numAntenna, which is an optional field, as non-existent.
        """
        self._numAntennaExists = False

    # ===> Attribute basebandName, which is optional
    _basebandNameExists = False

    _basebandName = None  # this is a 1D list of BasebandName

    def isBasebandNameExists(self):
        """
        The attribute basebandName is optional. Return True if this attribute exists.
        return True if and only if the basebandName attribute exists.
        """
        return self._basebandNameExists

    def getBasebandName(self):
        """
        Get basebandName, which is optional.
        return basebandName as BasebandName []
        raises ValueError If basebandName does not exist.
        """
        if not self._basebandNameExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + basebandName
                + " attribute in table Annotation does not exist!"
            )

        return copy.deepcopy(self._basebandName)

    def setBasebandName(self, basebandName):
        """
        Set basebandName with the specified BasebandName []  value.
        basebandName The BasebandName []  value to which basebandName is to be set.


        """

        # value must be a list
        if not isinstance(basebandName, list):
            raise ValueError("The value of basebandName must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(basebandName)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of basebandName is not correct")

            # the type of the values in the list must be BasebandName
            # note : this only checks the first value found
            if not Parser.checkListType(basebandName, BasebandName):
                raise ValueError(
                    "type of the first value in basebandName is not BasebandName as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._basebandName = copy.deepcopy(basebandName)
        except Exception as exc:
            raise ValueError("Invalid basebandName : " + str(exc))

        self._basebandNameExists = True

    def clearBasebandName(self):
        """
        Mark basebandName, which is an optional field, as non-existent.
        """
        self._basebandNameExists = False

    # ===> Attribute numBaseband, which is optional
    _numBasebandExists = False

    _numBaseband = 0

    def isNumBasebandExists(self):
        """
        The attribute numBaseband is optional. Return True if this attribute exists.
        return True if and only if the numBaseband attribute exists.
        """
        return self._numBasebandExists

    def getNumBaseband(self):
        """
        Get numBaseband, which is optional.
        return numBaseband as int
        raises ValueError If numBaseband does not exist.
        """
        if not self._numBasebandExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numBaseband
                + " attribute in table Annotation does not exist!"
            )

        return self._numBaseband

    def setNumBaseband(self, numBaseband):
        """
        Set numBaseband with the specified int value.
        numBaseband The int value to which numBaseband is to be set.


        """

        self._numBaseband = int(numBaseband)

        self._numBasebandExists = True

    def clearNumBaseband(self):
        """
        Mark numBaseband, which is an optional field, as non-existent.
        """
        self._numBasebandExists = False

    # ===> Attribute interval, which is optional
    _intervalExists = False

    _interval = Interval()

    def isIntervalExists(self):
        """
        The attribute interval is optional. Return True if this attribute exists.
        return True if and only if the interval attribute exists.
        """
        return self._intervalExists

    def getInterval(self):
        """
        Get interval, which is optional.
        return interval as Interval
        raises ValueError If interval does not exist.
        """
        if not self._intervalExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + interval
                + " attribute in table Annotation does not exist!"
            )

        # make sure it is a copy of Interval
        return Interval(self._interval)

    def setInterval(self, interval):
        """
        Set interval with the specified Interval value.
        interval The Interval value to which interval is to be set.
        The value of interval can be anything allowed by the Interval constructor.

        """

        self._interval = Interval(interval)

        self._intervalExists = True

    def clearInterval(self):
        """
        Mark interval, which is an optional field, as non-existent.
        """
        self._intervalExists = False

    # ===> Attribute dValue, which is optional
    _dValueExists = False

    _dValue = None

    def isDValueExists(self):
        """
        The attribute dValue is optional. Return True if this attribute exists.
        return True if and only if the dValue attribute exists.
        """
        return self._dValueExists

    def getDValue(self):
        """
        Get dValue, which is optional.
        return dValue as double
        raises ValueError If dValue does not exist.
        """
        if not self._dValueExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + dValue
                + " attribute in table Annotation does not exist!"
            )

        return self._dValue

    def setDValue(self, dValue):
        """
        Set dValue with the specified double value.
        dValue The double value to which dValue is to be set.


        """

        self._dValue = double(dValue)

        self._dValueExists = True

    def clearDValue(self):
        """
        Mark dValue, which is an optional field, as non-existent.
        """
        self._dValueExists = False

    # ===> Attribute vdValue, which is optional
    _vdValueExists = False

    _vdValue = None  # this is a 1D list of double

    def isVdValueExists(self):
        """
        The attribute vdValue is optional. Return True if this attribute exists.
        return True if and only if the vdValue attribute exists.
        """
        return self._vdValueExists

    def getVdValue(self):
        """
        Get vdValue, which is optional.
        return vdValue as double []
        raises ValueError If vdValue does not exist.
        """
        if not self._vdValueExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + vdValue
                + " attribute in table Annotation does not exist!"
            )

        return copy.deepcopy(self._vdValue)

    def setVdValue(self, vdValue):
        """
        Set vdValue with the specified double []  value.
        vdValue The double []  value to which vdValue is to be set.


        """

        # value must be a list
        if not isinstance(vdValue, list):
            raise ValueError("The value of vdValue must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(vdValue)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of vdValue is not correct")

            # the type of the values in the list must be double
            # note : this only checks the first value found
            if not Parser.checkListType(vdValue, double):
                raise ValueError(
                    "type of the first value in vdValue is not double as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._vdValue = copy.deepcopy(vdValue)
        except Exception as exc:
            raise ValueError("Invalid vdValue : " + str(exc))

        self._vdValueExists = True

    def clearVdValue(self):
        """
        Mark vdValue, which is an optional field, as non-existent.
        """
        self._vdValueExists = False

    # ===> Attribute vvdValues, which is optional
    _vvdValuesExists = False

    _vvdValues = None  # this is a 2D list of double

    def isVvdValuesExists(self):
        """
        The attribute vvdValues is optional. Return True if this attribute exists.
        return True if and only if the vvdValues attribute exists.
        """
        return self._vvdValuesExists

    def getVvdValues(self):
        """
        Get vvdValues, which is optional.
        return vvdValues as double []  []
        raises ValueError If vvdValues does not exist.
        """
        if not self._vvdValuesExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + vvdValues
                + " attribute in table Annotation does not exist!"
            )

        return copy.deepcopy(self._vvdValues)

    def setVvdValues(self, vvdValues):
        """
        Set vvdValues with the specified double []  []  value.
        vvdValues The double []  []  value to which vvdValues is to be set.


        """

        # value must be a list
        if not isinstance(vvdValues, list):
            raise ValueError("The value of vvdValues must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(vvdValues)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of vvdValues is not correct")

            # the type of the values in the list must be double
            # note : this only checks the first value found
            if not Parser.checkListType(vvdValues, double):
                raise ValueError(
                    "type of the first value in vvdValues is not double as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._vvdValues = copy.deepcopy(vvdValues)
        except Exception as exc:
            raise ValueError("Invalid vvdValues : " + str(exc))

        self._vvdValuesExists = True

    def clearVvdValues(self):
        """
        Mark vvdValues, which is an optional field, as non-existent.
        """
        self._vvdValuesExists = False

    # ===> Attribute llValue, which is optional
    _llValueExists = False

    _llValue = 0

    def isLlValueExists(self):
        """
        The attribute llValue is optional. Return True if this attribute exists.
        return True if and only if the llValue attribute exists.
        """
        return self._llValueExists

    def getLlValue(self):
        """
        Get llValue, which is optional.
        return llValue as int
        raises ValueError If llValue does not exist.
        """
        if not self._llValueExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + llValue
                + " attribute in table Annotation does not exist!"
            )

        return self._llValue

    def setLlValue(self, llValue):
        """
        Set llValue with the specified int value.
        llValue The int value to which llValue is to be set.


        """

        self._llValue = int(llValue)

        self._llValueExists = True

    def clearLlValue(self):
        """
        Mark llValue, which is an optional field, as non-existent.
        """
        self._llValueExists = False

    # ===> Attribute vllValue, which is optional
    _vllValueExists = False

    _vllValue = None  # this is a 1D list of int

    def isVllValueExists(self):
        """
        The attribute vllValue is optional. Return True if this attribute exists.
        return True if and only if the vllValue attribute exists.
        """
        return self._vllValueExists

    def getVllValue(self):
        """
        Get vllValue, which is optional.
        return vllValue as int []
        raises ValueError If vllValue does not exist.
        """
        if not self._vllValueExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + vllValue
                + " attribute in table Annotation does not exist!"
            )

        return copy.deepcopy(self._vllValue)

    def setVllValue(self, vllValue):
        """
        Set vllValue with the specified int []  value.
        vllValue The int []  value to which vllValue is to be set.


        """

        # value must be a list
        if not isinstance(vllValue, list):
            raise ValueError("The value of vllValue must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(vllValue)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of vllValue is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not Parser.checkListType(vllValue, int):
                raise ValueError(
                    "type of the first value in vllValue is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._vllValue = copy.deepcopy(vllValue)
        except Exception as exc:
            raise ValueError("Invalid vllValue : " + str(exc))

        self._vllValueExists = True

    def clearVllValue(self):
        """
        Mark vllValue, which is an optional field, as non-existent.
        """
        self._vllValueExists = False

    # ===> Attribute vvllValue, which is optional
    _vvllValueExists = False

    _vvllValue = None  # this is a 2D list of int

    def isVvllValueExists(self):
        """
        The attribute vvllValue is optional. Return True if this attribute exists.
        return True if and only if the vvllValue attribute exists.
        """
        return self._vvllValueExists

    def getVvllValue(self):
        """
        Get vvllValue, which is optional.
        return vvllValue as int []  []
        raises ValueError If vvllValue does not exist.
        """
        if not self._vvllValueExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + vvllValue
                + " attribute in table Annotation does not exist!"
            )

        return copy.deepcopy(self._vvllValue)

    def setVvllValue(self, vvllValue):
        """
        Set vvllValue with the specified int []  []  value.
        vvllValue The int []  []  value to which vvllValue is to be set.


        """

        # value must be a list
        if not isinstance(vvllValue, list):
            raise ValueError("The value of vvllValue must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(vvllValue)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of vvllValue is not correct")

            # the type of the values in the list must be int
            # note : this only checks the first value found
            if not Parser.checkListType(vvllValue, int):
                raise ValueError(
                    "type of the first value in vvllValue is not int as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._vvllValue = copy.deepcopy(vvllValue)
        except Exception as exc:
            raise ValueError("Invalid vvllValue : " + str(exc))

        self._vvllValueExists = True

    def clearVvllValue(self):
        """
        Mark vvllValue, which is an optional field, as non-existent.
        """
        self._vvllValueExists = False

    # ===> Attribute sValue, which is optional
    _sValueExists = False

    _sValue = None

    def isSValueExists(self):
        """
        The attribute sValue is optional. Return True if this attribute exists.
        return True if and only if the sValue attribute exists.
        """
        return self._sValueExists

    def getSValue(self):
        """
        Get sValue, which is optional.
        return sValue as str
        raises ValueError If sValue does not exist.
        """
        if not self._sValueExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sValue
                + " attribute in table Annotation does not exist!"
            )

        return self._sValue

    def setSValue(self, sValue):
        """
        Set sValue with the specified str value.
        sValue The str value to which sValue is to be set.


        """

        self._sValue = str(sValue)

        self._sValueExists = True

    def clearSValue(self):
        """
        Mark sValue, which is an optional field, as non-existent.
        """
        self._sValueExists = False

    # Extrinsic Table Attributes

    # ===> Attribute antennaId, which is optional
    _antennaIdExists = False

    _antennaId = []  # this is a list of Tag []

    def isAntennaIdExists(self):
        """
        The attribute antennaId is optional. Return True if this attribute exists.
        return True if and only if the antennaId attribute exists.
        """
        return self._antennaIdExists

    def getAntennaId(self):
        """
        Get antennaId, which is optional.
        return antennaId as Tag []
        raises ValueError If antennaId does not exist.
        """
        if not self._antennaIdExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + antennaId
                + " attribute in table Annotation does not exist!"
            )

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

        self._antennaIdExists = True

    def clearAntennaId(self):
        """
        Mark antennaId, which is an optional field, as non-existent.
        """
        self._antennaIdExists = False

    # Links

    def setOneAntennaId(self, index, antennaId):
        """
        Set antennaId[i] with the specified Tag value.
        index The index in antennaId where to set the Tag value.
        antennaId The Tag value to which antennaId[i] is to be set.
        Raises an exception if that value does not already exist in this row
        """
        if not self._antennaIdExists():
            raise ValueError(
                "The optional attribute, antennaId, does not exist in this row. This value can not be set using this method."
            )
        self._antennaId[index] = Tag(antennaId)

    # ===> hasmany link from a row of Annotation table to many rows of Antenna table.

    def addAntennaId(self, id):
        """
        Append a Tag to antennaId
        id the Tag to be appended to antennaId
        """
        if isinstance(id, list):
            for i in range(len(id)):
                self._antennaId.append(Tag(id[i]))
        else:
            self._antennaId.append(Tag(id))

        if not self._antennaIdExists:
            self._antennaIdExists = True

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

    # comparison methods

    def compareNoAutoInc(self, time, issue, details):
        """
        Compare each attribute except the autoincrementable one of this AnnotationRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # time is a ArrayTime, compare using the equals method.
        if not self._time.equals(time):
            return False

        # issue is a str, compare using the == operator.
        if not (self._issue == issue):
            return False

        # details is a str, compare using the == operator.
        if not (self._details == details):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getTime(), otherRow.getIssue(), otherRow.getDetails()
        )

    def compareRequiredValue(self, time, issue, details):

        # time is a ArrayTime, compare using the equals method.
        if not self._time.equals(time):
            return False

        # issue is a str, compare using the == operator.
        if not (self._issue == issue):
            return False

        # details is a str, compare using the == operator.
        if not (self._details == details):
            return False

        return True
