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
# File PolarizationRow.py
#

import pyasdm.PolarizationTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.StokesParameter import StokesParameter


from pyasdm.enumerations.PolarizationType import PolarizationType


from xml.dom import minidom

import copy


class PolarizationRow:
    """
    The PolarizationRow class is a row of a PolarizationTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a PolarizationRow.
        When row is None, create an empty row attached to table, which must be a PolarizationTable.
        When row is given, copy those values in to the new row. The row argument must be a PolarizationRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.PolarizationTable):
            raise ValueError("table must be a PolarizationTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._polarizationId = Tag()

        self._numCorr = 0

        self._corrType = []  # this is a list of StokesParameter []

        self._corrProduct = []  # this is a list of PolarizationType []  []

        if row is not None:
            if not isinstance(row, PolarizationRow):
                raise ValueError("row must be a PolarizationRow")

            # copy constructor

            self._polarizationId = Tag(row._polarizationId)

            self._numCorr = row._numCorr

            # corrType is a  list , make a deep copy
            self._corrType = copy.deepcopy(row._corrType)

            # corrProduct is a  list , make a deep copy
            self._corrProduct = copy.deepcopy(row._corrProduct)

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

        result += Parser.extendedValueToXML("polarizationId", self._polarizationId)

        result += Parser.valueToXML("numCorr", self._numCorr)

        result += Parser.listEnumValueToXML("corrType", self._corrType)

        result += Parser.listEnumValueToXML("corrProduct", self._corrProduct)

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
                "xmlrow is not a string or a minidom.Element", "PolarizationTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "PolarizationTable")

        # intrinsic attribute values

        polarizationIdNode = rowdom.getElementsByTagName("polarizationId")[0]

        self._polarizationId = Tag(polarizationIdNode.firstChild.data.strip())

        numCorrNode = rowdom.getElementsByTagName("numCorr")[0]

        self._numCorr = int(numCorrNode.firstChild.data.strip())

        corrTypeNode = rowdom.getElementsByTagName("corrType")[0]

        corrTypeStr = corrTypeNode.firstChild.data.strip()
        self._corrType = Parser.stringListToLists(
            corrTypeStr, StokesParameter, "Polarization", False
        )

        corrProductNode = rowdom.getElementsByTagName("corrProduct")[0]

        corrProductStr = corrProductNode.firstChild.data.strip()
        self._corrProduct = Parser.stringListToLists(
            corrProductStr, PolarizationType, "Polarization", False
        )

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._polarizationId.toBin(eos)

        eos.writeInt(self._numCorr)

        eos.writeInt(len(self._corrType))
        for i in range(len(self._corrType)):

            eos.writeString(str(self._corrType[i]))

        # null array case, unsure if this is possible but this should work
        if self._corrProduct is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            corrProduct_dims = pyasdm.utils.getListDims(self._corrProduct)
        # assumes it really is 2D
        eos.writeInt(corrProduct_dims[0])
        eos.writeInt(corrProduct_dims[1])
        for i in range(corrProduct_dims[0]):
            for j in range(corrProduct_dims[1]):
                eos.writeString(str(self._corrProduct[i][j]))

    @staticmethod
    def polarizationIdFromBin(row, eis):
        """
        Set the polarizationId in row from the EndianInput (eis) instance.
        """

        row._polarizationId = Tag.fromBin(eis)

    @staticmethod
    def numCorrFromBin(row, eis):
        """
        Set the numCorr in row from the EndianInput (eis) instance.
        """

        row._numCorr = eis.readInt()

    @staticmethod
    def corrTypeFromBin(row, eis):
        """
        Set the corrType in row from the EndianInput (eis) instance.
        """

        corrTypeDim1 = eis.readInt()
        thisList = []
        for i in range(corrTypeDim1):
            thisValue = StokesParameter.literal(eis.readString())
            thisList.append(thisValue)
        row._corrType = thisList

    @staticmethod
    def corrProductFromBin(row, eis):
        """
        Set the corrProduct in row from the EndianInput (eis) instance.
        """

        corrProductDim1 = eis.readInt()
        corrProductDim2 = eis.readInt()
        thisList = []
        for i in range(corrProductDim1):
            thisList_j = []
            for j in range(corrProductDim2):
                thisValue = PolarizationType.literal(eis.readString())
                thisList_j.append(thisValue)
            thisList.append(thisList_j)
        row._corrProduct = thisList

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["polarizationId"] = PolarizationRow.polarizationIdFromBin
        _fromBinMethods["numCorr"] = PolarizationRow.numCorrFromBin
        _fromBinMethods["corrType"] = PolarizationRow.corrTypeFromBin
        _fromBinMethods["corrProduct"] = PolarizationRow.corrProductFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = PolarizationRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Polarization",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute polarizationId

    _polarizationId = Tag()

    def getPolarizationId(self):
        """
        Get polarizationId.
        return polarizationId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._polarizationId)

    def setPolarizationId(self, polarizationId):
        """
        Set polarizationId with the specified Tag value.
        polarizationId The Tag value to which polarizationId is to be set.
        The value of polarizationId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the polarizationId field, which is part of the key, after this row has been added to this table."
            )

        self._polarizationId = Tag(polarizationId)

    # ===> Attribute numCorr

    _numCorr = 0

    def getNumCorr(self):
        """
        Get numCorr.
        return numCorr as int
        """

        return self._numCorr

    def setNumCorr(self, numCorr):
        """
        Set numCorr with the specified int value.
        numCorr The int value to which numCorr is to be set.


        """

        self._numCorr = int(numCorr)

    # ===> Attribute corrType

    _corrType = None  # this is a 1D list of StokesParameter

    def getCorrType(self):
        """
        Get corrType.
        return corrType as StokesParameter []
        """

        return copy.deepcopy(self._corrType)

    def setCorrType(self, corrType):
        """
        Set corrType with the specified StokesParameter []  value.
        corrType The StokesParameter []  value to which corrType is to be set.


        """

        # value must be a list
        if not isinstance(corrType, list):
            raise ValueError("The value of corrType must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(corrType)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of corrType is not correct")

            # the type of the values in the list must be StokesParameter
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(corrType, StokesParameter):
                raise ValueError(
                    "type of the first value in corrType is not StokesParameter as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._corrType = copy.deepcopy(corrType)
        except Exception as exc:
            raise ValueError("Invalid corrType : " + str(exc))

    # ===> Attribute corrProduct

    _corrProduct = None  # this is a 2D list of PolarizationType

    def getCorrProduct(self):
        """
        Get corrProduct.
        return corrProduct as PolarizationType []  []
        """

        return copy.deepcopy(self._corrProduct)

    def setCorrProduct(self, corrProduct):
        """
        Set corrProduct with the specified PolarizationType []  []  value.
        corrProduct The PolarizationType []  []  value to which corrProduct is to be set.


        """

        # value must be a list
        if not isinstance(corrProduct, list):
            raise ValueError("The value of corrProduct must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(corrProduct)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of corrProduct is not correct")

            # the type of the values in the list must be PolarizationType
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(corrProduct, PolarizationType):
                raise ValueError(
                    "type of the first value in corrProduct is not PolarizationType as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._corrProduct = copy.deepcopy(corrProduct)
        except Exception as exc:
            raise ValueError("Invalid corrProduct : " + str(exc))

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(self, numCorr, corrType, corrProduct):
        """
        Compare each attribute except the autoincrementable one of this PolarizationRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # numCorr is a int, compare using the == operator.
        if not (self._numCorr == numCorr):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._corrType) != len(corrType):
            return False
        for indx in range(len(corrType)):

            # corrType is a list of StokesParameter, compare using == operator.
            if not (self._corrType[indx] == corrType[indx]):
                return False

        # We compare two 2D arrays (lists).
        if corrProduct is not None:
            if self._corrProduct is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            corrProduct_dims = pyasdm.utils.getListDims(corrProduct)
            this_corrProduct_dims = pyasdm.utils.getListDims(self._corrProduct)
            if corrProduct_dims != this_corrProduct_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(corrProduct_dims[0]):
                for j in range(corrProduct_dims[1]):

                    # corrProduct is an array of PolarizationType, compare using == operator.
                    if not (self._corrProduct[i][j] == corrProduct[i][j]):
                        return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumCorr(), otherRow.getCorrType(), otherRow.getCorrProduct()
        )

    def compareRequiredValue(self, numCorr, corrType, corrProduct):

        # numCorr is a int, compare using the == operator.
        if not (self._numCorr == numCorr):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._corrType) != len(corrType):
            return False
        for indx in range(len(corrType)):

            # corrType is a list of StokesParameter, compare using == operator.
            if not (self._corrType[indx] == corrType[indx]):
                return False

        # We compare two 2D arrays (lists).
        if corrProduct is not None:
            if self._corrProduct is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            corrProduct_dims = pyasdm.utils.getListDims(corrProduct)
            this_corrProduct_dims = pyasdm.utils.getListDims(self._corrProduct)
            if corrProduct_dims != this_corrProduct_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(corrProduct_dims[0]):
                for j in range(corrProduct_dims[1]):

                    # corrProduct is an array of PolarizationType, compare using == operator.
                    if not (self._corrProduct[i][j] == corrProduct[i][j]):
                        return False

        return True


# initialize the dictionary that maps fields to init methods
PolarizationRow.initFromBinMethods()
