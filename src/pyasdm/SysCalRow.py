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
# File SysCalRow.py
#

import pyasdm.SysCalTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from xml.dom import minidom

import copy


class SysCalRow:
    """
    The SysCalRow class is a row of a SysCalTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a SysCalRow.
        When row is None, create an empty row attached to table, which must be a SysCalTable.
        When row is given, copy those values in to the new row. The row argument must be a SysCalRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.SysCalTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._timeInterval = ArrayTimeInterval()

        self._numReceptor = 0

        self._numChan = 0

        self._tcalFlagExists = False

        self._tcalFlag = None

        self._tcalSpectrumExists = False

        self._tcalSpectrum = []  # this is a list of Temperature []  []

        self._trxFlagExists = False

        self._trxFlag = None

        self._trxSpectrumExists = False

        self._trxSpectrum = []  # this is a list of Temperature []  []

        self._tskyFlagExists = False

        self._tskyFlag = None

        self._tskySpectrumExists = False

        self._tskySpectrum = []  # this is a list of Temperature []  []

        self._tsysFlagExists = False

        self._tsysFlag = None

        self._tsysSpectrumExists = False

        self._tsysSpectrum = []  # this is a list of Temperature []  []

        self._tantFlagExists = False

        self._tantFlag = None

        self._tantSpectrumExists = False

        self._tantSpectrum = []  # this is a list of float []  []

        self._tantTsysFlagExists = False

        self._tantTsysFlag = None

        self._tantTsysSpectrumExists = False

        self._tantTsysSpectrum = []  # this is a list of float []  []

        self._phaseDiffFlagExists = False

        self._phaseDiffFlag = None

        self._phaseDiffSpectrumExists = False

        self._phaseDiffSpectrum = []  # this is a list of float []  []

        # extrinsic attributes

        self._antennaId = Tag()

        self._feedId = 0

        self._spectralWindowId = Tag()

        if row is not None:
            if not isinstance(row, SysCalRow):
                raise ValueError("row must be a MainRow")

            # copy constructor

            self._antennaId = Tag(row._antennaId)

            self._spectralWindowId = Tag(row._spectralWindowId)

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._feedId = row._feedId

            self._numReceptor = row._numReceptor

            self._numChan = row._numChan

            # by default set systematically tcalFlag's value to something not None

            if row._tcalFlagExists:

                self._tcalFlag = row._tcalFlag

                self._tcalFlagExists = True

            # by default set systematically tcalSpectrum's value to something not None

            if row._tcalSpectrumExists:

                # tcalSpectrum is a list, make a deep copy
                self.tcalSpectrum = copy.deepcopy(row.tcalSpectrum)

                self._tcalSpectrumExists = True

            # by default set systematically trxFlag's value to something not None

            if row._trxFlagExists:

                self._trxFlag = row._trxFlag

                self._trxFlagExists = True

            # by default set systematically trxSpectrum's value to something not None

            if row._trxSpectrumExists:

                # trxSpectrum is a list, make a deep copy
                self.trxSpectrum = copy.deepcopy(row.trxSpectrum)

                self._trxSpectrumExists = True

            # by default set systematically tskyFlag's value to something not None

            if row._tskyFlagExists:

                self._tskyFlag = row._tskyFlag

                self._tskyFlagExists = True

            # by default set systematically tskySpectrum's value to something not None

            if row._tskySpectrumExists:

                # tskySpectrum is a list, make a deep copy
                self.tskySpectrum = copy.deepcopy(row.tskySpectrum)

                self._tskySpectrumExists = True

            # by default set systematically tsysFlag's value to something not None

            if row._tsysFlagExists:

                self._tsysFlag = row._tsysFlag

                self._tsysFlagExists = True

            # by default set systematically tsysSpectrum's value to something not None

            if row._tsysSpectrumExists:

                # tsysSpectrum is a list, make a deep copy
                self.tsysSpectrum = copy.deepcopy(row.tsysSpectrum)

                self._tsysSpectrumExists = True

            # by default set systematically tantFlag's value to something not None

            if row._tantFlagExists:

                self._tantFlag = row._tantFlag

                self._tantFlagExists = True

            # by default set systematically tantSpectrum's value to something not None

            if row._tantSpectrumExists:

                # tantSpectrum is a list, make a deep copy
                self.tantSpectrum = copy.deepcopy(row.tantSpectrum)

                self._tantSpectrumExists = True

            # by default set systematically tantTsysFlag's value to something not None

            if row._tantTsysFlagExists:

                self._tantTsysFlag = row._tantTsysFlag

                self._tantTsysFlagExists = True

            # by default set systematically tantTsysSpectrum's value to something not None

            if row._tantTsysSpectrumExists:

                # tantTsysSpectrum is a list, make a deep copy
                self.tantTsysSpectrum = copy.deepcopy(row.tantTsysSpectrum)

                self._tantTsysSpectrumExists = True

            # by default set systematically phaseDiffFlag's value to something not None

            if row._phaseDiffFlagExists:

                self._phaseDiffFlag = row._phaseDiffFlag

                self._phaseDiffFlagExists = True

            # by default set systematically phaseDiffSpectrum's value to something not None

            if row._phaseDiffSpectrumExists:

                # phaseDiffSpectrum is a list, make a deep copy
                self.phaseDiffSpectrum = copy.deepcopy(row.phaseDiffSpectrum)

                self._phaseDiffSpectrumExists = True

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

        result += Parser.valueToXML("numChan", self._numChan)

        if self._tcalFlagExists:

            result += Parser.valueToXML("tcalFlag", self._tcalFlag)

        if self._tcalSpectrumExists:

            result += Parser.listExtendedValueToXML("tcalSpectrum", self._tcalSpectrum)

        if self._trxFlagExists:

            result += Parser.valueToXML("trxFlag", self._trxFlag)

        if self._trxSpectrumExists:

            result += Parser.listExtendedValueToXML("trxSpectrum", self._trxSpectrum)

        if self._tskyFlagExists:

            result += Parser.valueToXML("tskyFlag", self._tskyFlag)

        if self._tskySpectrumExists:

            result += Parser.listExtendedValueToXML("tskySpectrum", self._tskySpectrum)

        if self._tsysFlagExists:

            result += Parser.valueToXML("tsysFlag", self._tsysFlag)

        if self._tsysSpectrumExists:

            result += Parser.listExtendedValueToXML("tsysSpectrum", self._tsysSpectrum)

        if self._tantFlagExists:

            result += Parser.valueToXML("tantFlag", self._tantFlag)

        if self._tantSpectrumExists:

            result += Parser.listValueToXML("tantSpectrum", self._tantSpectrum)

        if self._tantTsysFlagExists:

            result += Parser.valueToXML("tantTsysFlag", self._tantTsysFlag)

        if self._tantTsysSpectrumExists:

            result += Parser.listValueToXML("tantTsysSpectrum", self._tantTsysSpectrum)

        if self._phaseDiffFlagExists:

            result += Parser.valueToXML("phaseDiffFlag", self._phaseDiffFlag)

        if self._phaseDiffSpectrumExists:

            result += Parser.listValueToXML(
                "phaseDiffSpectrum", self._phaseDiffSpectrum
            )

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
                "xmlrow is not a string or a minidom.Element", "SysCalTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "SysCalTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        numChanNode = rowdom.getElementsByTagName("numChan")[0]

        self._numChan = int(numChanNode.firstChild.data.strip())

        tcalFlagNode = rowdom.getElementsByTagName("tcalFlag")
        if len(tcalFlagNode) > 0:

            self._tcalFlag = bool(tcalFlagNode[0].firstChild.data.strip())

            self._tcalFlagExists = True

        tcalSpectrumNode = rowdom.getElementsByTagName("tcalSpectrum")
        if len(tcalSpectrumNode) > 0:

            tcalSpectrumStr = tcalSpectrumNode[0].firstChild.data.strip()

            self._tcalSpectrum = Parser.stringListToLists(
                tcalSpectrumStr, Temperature, "SysCal", True
            )

            self._tcalSpectrumExists = True

        trxFlagNode = rowdom.getElementsByTagName("trxFlag")
        if len(trxFlagNode) > 0:

            self._trxFlag = bool(trxFlagNode[0].firstChild.data.strip())

            self._trxFlagExists = True

        trxSpectrumNode = rowdom.getElementsByTagName("trxSpectrum")
        if len(trxSpectrumNode) > 0:

            trxSpectrumStr = trxSpectrumNode[0].firstChild.data.strip()

            self._trxSpectrum = Parser.stringListToLists(
                trxSpectrumStr, Temperature, "SysCal", True
            )

            self._trxSpectrumExists = True

        tskyFlagNode = rowdom.getElementsByTagName("tskyFlag")
        if len(tskyFlagNode) > 0:

            self._tskyFlag = bool(tskyFlagNode[0].firstChild.data.strip())

            self._tskyFlagExists = True

        tskySpectrumNode = rowdom.getElementsByTagName("tskySpectrum")
        if len(tskySpectrumNode) > 0:

            tskySpectrumStr = tskySpectrumNode[0].firstChild.data.strip()

            self._tskySpectrum = Parser.stringListToLists(
                tskySpectrumStr, Temperature, "SysCal", True
            )

            self._tskySpectrumExists = True

        tsysFlagNode = rowdom.getElementsByTagName("tsysFlag")
        if len(tsysFlagNode) > 0:

            self._tsysFlag = bool(tsysFlagNode[0].firstChild.data.strip())

            self._tsysFlagExists = True

        tsysSpectrumNode = rowdom.getElementsByTagName("tsysSpectrum")
        if len(tsysSpectrumNode) > 0:

            tsysSpectrumStr = tsysSpectrumNode[0].firstChild.data.strip()

            self._tsysSpectrum = Parser.stringListToLists(
                tsysSpectrumStr, Temperature, "SysCal", True
            )

            self._tsysSpectrumExists = True

        tantFlagNode = rowdom.getElementsByTagName("tantFlag")
        if len(tantFlagNode) > 0:

            self._tantFlag = bool(tantFlagNode[0].firstChild.data.strip())

            self._tantFlagExists = True

        tantSpectrumNode = rowdom.getElementsByTagName("tantSpectrum")
        if len(tantSpectrumNode) > 0:

            tantSpectrumStr = tantSpectrumNode[0].firstChild.data.strip()

            self._tantSpectrum = Parser.stringListToLists(
                tantSpectrumStr, float, "SysCal", False
            )

            self._tantSpectrumExists = True

        tantTsysFlagNode = rowdom.getElementsByTagName("tantTsysFlag")
        if len(tantTsysFlagNode) > 0:

            self._tantTsysFlag = bool(tantTsysFlagNode[0].firstChild.data.strip())

            self._tantTsysFlagExists = True

        tantTsysSpectrumNode = rowdom.getElementsByTagName("tantTsysSpectrum")
        if len(tantTsysSpectrumNode) > 0:

            tantTsysSpectrumStr = tantTsysSpectrumNode[0].firstChild.data.strip()

            self._tantTsysSpectrum = Parser.stringListToLists(
                tantTsysSpectrumStr, float, "SysCal", False
            )

            self._tantTsysSpectrumExists = True

        phaseDiffFlagNode = rowdom.getElementsByTagName("phaseDiffFlag")
        if len(phaseDiffFlagNode) > 0:

            self._phaseDiffFlag = bool(phaseDiffFlagNode[0].firstChild.data.strip())

            self._phaseDiffFlagExists = True

        phaseDiffSpectrumNode = rowdom.getElementsByTagName("phaseDiffSpectrum")
        if len(phaseDiffSpectrumNode) > 0:

            phaseDiffSpectrumStr = phaseDiffSpectrumNode[0].firstChild.data.strip()

            self._phaseDiffSpectrum = Parser.stringListToLists(
                phaseDiffSpectrumStr, float, "SysCal", False
            )

            self._phaseDiffSpectrumExists = True

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

    # ===> Attribute tcalFlag, which is optional
    _tcalFlagExists = False

    _tcalFlag = None

    def isTcalFlagExists(self):
        """
        The attribute tcalFlag is optional. Return True if this attribute exists.
        return True if and only if the tcalFlag attribute exists.
        """
        return self._tcalFlagExists

    def getTcalFlag(self):
        """
        Get tcalFlag, which is optional.
        return tcalFlag as bool
        raises ValueError If tcalFlag does not exist.
        """
        if not self._tcalFlagExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tcalFlag
                + " attribute in table SysCal does not exist!"
            )

        return self._tcalFlag

    def setTcalFlag(self, tcalFlag):
        """
        Set tcalFlag with the specified bool value.
        tcalFlag The bool value to which tcalFlag is to be set.


        """

        self._tcalFlag = bool(tcalFlag)

        self._tcalFlagExists = True

    def clearTcalFlag(self):
        """
        Mark tcalFlag, which is an optional field, as non-existent.
        """
        self._tcalFlagExists = False

    # ===> Attribute tcalSpectrum, which is optional
    _tcalSpectrumExists = False

    _tcalSpectrum = None  # this is a 2D list of Temperature

    def isTcalSpectrumExists(self):
        """
        The attribute tcalSpectrum is optional. Return True if this attribute exists.
        return True if and only if the tcalSpectrum attribute exists.
        """
        return self._tcalSpectrumExists

    def getTcalSpectrum(self):
        """
        Get tcalSpectrum, which is optional.
        return tcalSpectrum as Temperature []  []
        raises ValueError If tcalSpectrum does not exist.
        """
        if not self._tcalSpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tcalSpectrum
                + " attribute in table SysCal does not exist!"
            )

        return copy.deepcopy(self._tcalSpectrum)

    def setTcalSpectrum(self, tcalSpectrum):
        """
        Set tcalSpectrum with the specified Temperature []  []  value.
        tcalSpectrum The Temperature []  []  value to which tcalSpectrum is to be set.
        The value of tcalSpectrum can be anything allowed by the Temperature []  []  constructor.

        """

        # value must be a list
        if not isinstance(tcalSpectrum, list):
            raise ValueError("The value of tcalSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tcalSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of tcalSpectrum is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(tcalSpectrum, Temperature):
                raise ValueError(
                    "type of the first value in tcalSpectrum is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tcalSpectrum = copy.deepcopy(tcalSpectrum)
        except Exception as exc:
            raise ValueError("Invalid tcalSpectrum : " + str(exc))

        self._tcalSpectrumExists = True

    def clearTcalSpectrum(self):
        """
        Mark tcalSpectrum, which is an optional field, as non-existent.
        """
        self._tcalSpectrumExists = False

    # ===> Attribute trxFlag, which is optional
    _trxFlagExists = False

    _trxFlag = None

    def isTrxFlagExists(self):
        """
        The attribute trxFlag is optional. Return True if this attribute exists.
        return True if and only if the trxFlag attribute exists.
        """
        return self._trxFlagExists

    def getTrxFlag(self):
        """
        Get trxFlag, which is optional.
        return trxFlag as bool
        raises ValueError If trxFlag does not exist.
        """
        if not self._trxFlagExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + trxFlag
                + " attribute in table SysCal does not exist!"
            )

        return self._trxFlag

    def setTrxFlag(self, trxFlag):
        """
        Set trxFlag with the specified bool value.
        trxFlag The bool value to which trxFlag is to be set.


        """

        self._trxFlag = bool(trxFlag)

        self._trxFlagExists = True

    def clearTrxFlag(self):
        """
        Mark trxFlag, which is an optional field, as non-existent.
        """
        self._trxFlagExists = False

    # ===> Attribute trxSpectrum, which is optional
    _trxSpectrumExists = False

    _trxSpectrum = None  # this is a 2D list of Temperature

    def isTrxSpectrumExists(self):
        """
        The attribute trxSpectrum is optional. Return True if this attribute exists.
        return True if and only if the trxSpectrum attribute exists.
        """
        return self._trxSpectrumExists

    def getTrxSpectrum(self):
        """
        Get trxSpectrum, which is optional.
        return trxSpectrum as Temperature []  []
        raises ValueError If trxSpectrum does not exist.
        """
        if not self._trxSpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + trxSpectrum
                + " attribute in table SysCal does not exist!"
            )

        return copy.deepcopy(self._trxSpectrum)

    def setTrxSpectrum(self, trxSpectrum):
        """
        Set trxSpectrum with the specified Temperature []  []  value.
        trxSpectrum The Temperature []  []  value to which trxSpectrum is to be set.
        The value of trxSpectrum can be anything allowed by the Temperature []  []  constructor.

        """

        # value must be a list
        if not isinstance(trxSpectrum, list):
            raise ValueError("The value of trxSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(trxSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of trxSpectrum is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(trxSpectrum, Temperature):
                raise ValueError(
                    "type of the first value in trxSpectrum is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._trxSpectrum = copy.deepcopy(trxSpectrum)
        except Exception as exc:
            raise ValueError("Invalid trxSpectrum : " + str(exc))

        self._trxSpectrumExists = True

    def clearTrxSpectrum(self):
        """
        Mark trxSpectrum, which is an optional field, as non-existent.
        """
        self._trxSpectrumExists = False

    # ===> Attribute tskyFlag, which is optional
    _tskyFlagExists = False

    _tskyFlag = None

    def isTskyFlagExists(self):
        """
        The attribute tskyFlag is optional. Return True if this attribute exists.
        return True if and only if the tskyFlag attribute exists.
        """
        return self._tskyFlagExists

    def getTskyFlag(self):
        """
        Get tskyFlag, which is optional.
        return tskyFlag as bool
        raises ValueError If tskyFlag does not exist.
        """
        if not self._tskyFlagExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tskyFlag
                + " attribute in table SysCal does not exist!"
            )

        return self._tskyFlag

    def setTskyFlag(self, tskyFlag):
        """
        Set tskyFlag with the specified bool value.
        tskyFlag The bool value to which tskyFlag is to be set.


        """

        self._tskyFlag = bool(tskyFlag)

        self._tskyFlagExists = True

    def clearTskyFlag(self):
        """
        Mark tskyFlag, which is an optional field, as non-existent.
        """
        self._tskyFlagExists = False

    # ===> Attribute tskySpectrum, which is optional
    _tskySpectrumExists = False

    _tskySpectrum = None  # this is a 2D list of Temperature

    def isTskySpectrumExists(self):
        """
        The attribute tskySpectrum is optional. Return True if this attribute exists.
        return True if and only if the tskySpectrum attribute exists.
        """
        return self._tskySpectrumExists

    def getTskySpectrum(self):
        """
        Get tskySpectrum, which is optional.
        return tskySpectrum as Temperature []  []
        raises ValueError If tskySpectrum does not exist.
        """
        if not self._tskySpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tskySpectrum
                + " attribute in table SysCal does not exist!"
            )

        return copy.deepcopy(self._tskySpectrum)

    def setTskySpectrum(self, tskySpectrum):
        """
        Set tskySpectrum with the specified Temperature []  []  value.
        tskySpectrum The Temperature []  []  value to which tskySpectrum is to be set.
        The value of tskySpectrum can be anything allowed by the Temperature []  []  constructor.

        """

        # value must be a list
        if not isinstance(tskySpectrum, list):
            raise ValueError("The value of tskySpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tskySpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of tskySpectrum is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(tskySpectrum, Temperature):
                raise ValueError(
                    "type of the first value in tskySpectrum is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tskySpectrum = copy.deepcopy(tskySpectrum)
        except Exception as exc:
            raise ValueError("Invalid tskySpectrum : " + str(exc))

        self._tskySpectrumExists = True

    def clearTskySpectrum(self):
        """
        Mark tskySpectrum, which is an optional field, as non-existent.
        """
        self._tskySpectrumExists = False

    # ===> Attribute tsysFlag, which is optional
    _tsysFlagExists = False

    _tsysFlag = None

    def isTsysFlagExists(self):
        """
        The attribute tsysFlag is optional. Return True if this attribute exists.
        return True if and only if the tsysFlag attribute exists.
        """
        return self._tsysFlagExists

    def getTsysFlag(self):
        """
        Get tsysFlag, which is optional.
        return tsysFlag as bool
        raises ValueError If tsysFlag does not exist.
        """
        if not self._tsysFlagExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tsysFlag
                + " attribute in table SysCal does not exist!"
            )

        return self._tsysFlag

    def setTsysFlag(self, tsysFlag):
        """
        Set tsysFlag with the specified bool value.
        tsysFlag The bool value to which tsysFlag is to be set.


        """

        self._tsysFlag = bool(tsysFlag)

        self._tsysFlagExists = True

    def clearTsysFlag(self):
        """
        Mark tsysFlag, which is an optional field, as non-existent.
        """
        self._tsysFlagExists = False

    # ===> Attribute tsysSpectrum, which is optional
    _tsysSpectrumExists = False

    _tsysSpectrum = None  # this is a 2D list of Temperature

    def isTsysSpectrumExists(self):
        """
        The attribute tsysSpectrum is optional. Return True if this attribute exists.
        return True if and only if the tsysSpectrum attribute exists.
        """
        return self._tsysSpectrumExists

    def getTsysSpectrum(self):
        """
        Get tsysSpectrum, which is optional.
        return tsysSpectrum as Temperature []  []
        raises ValueError If tsysSpectrum does not exist.
        """
        if not self._tsysSpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tsysSpectrum
                + " attribute in table SysCal does not exist!"
            )

        return copy.deepcopy(self._tsysSpectrum)

    def setTsysSpectrum(self, tsysSpectrum):
        """
        Set tsysSpectrum with the specified Temperature []  []  value.
        tsysSpectrum The Temperature []  []  value to which tsysSpectrum is to be set.
        The value of tsysSpectrum can be anything allowed by the Temperature []  []  constructor.

        """

        # value must be a list
        if not isinstance(tsysSpectrum, list):
            raise ValueError("The value of tsysSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tsysSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of tsysSpectrum is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(tsysSpectrum, Temperature):
                raise ValueError(
                    "type of the first value in tsysSpectrum is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tsysSpectrum = copy.deepcopy(tsysSpectrum)
        except Exception as exc:
            raise ValueError("Invalid tsysSpectrum : " + str(exc))

        self._tsysSpectrumExists = True

    def clearTsysSpectrum(self):
        """
        Mark tsysSpectrum, which is an optional field, as non-existent.
        """
        self._tsysSpectrumExists = False

    # ===> Attribute tantFlag, which is optional
    _tantFlagExists = False

    _tantFlag = None

    def isTantFlagExists(self):
        """
        The attribute tantFlag is optional. Return True if this attribute exists.
        return True if and only if the tantFlag attribute exists.
        """
        return self._tantFlagExists

    def getTantFlag(self):
        """
        Get tantFlag, which is optional.
        return tantFlag as bool
        raises ValueError If tantFlag does not exist.
        """
        if not self._tantFlagExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tantFlag
                + " attribute in table SysCal does not exist!"
            )

        return self._tantFlag

    def setTantFlag(self, tantFlag):
        """
        Set tantFlag with the specified bool value.
        tantFlag The bool value to which tantFlag is to be set.


        """

        self._tantFlag = bool(tantFlag)

        self._tantFlagExists = True

    def clearTantFlag(self):
        """
        Mark tantFlag, which is an optional field, as non-existent.
        """
        self._tantFlagExists = False

    # ===> Attribute tantSpectrum, which is optional
    _tantSpectrumExists = False

    _tantSpectrum = None  # this is a 2D list of float

    def isTantSpectrumExists(self):
        """
        The attribute tantSpectrum is optional. Return True if this attribute exists.
        return True if and only if the tantSpectrum attribute exists.
        """
        return self._tantSpectrumExists

    def getTantSpectrum(self):
        """
        Get tantSpectrum, which is optional.
        return tantSpectrum as float []  []
        raises ValueError If tantSpectrum does not exist.
        """
        if not self._tantSpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tantSpectrum
                + " attribute in table SysCal does not exist!"
            )

        return copy.deepcopy(self._tantSpectrum)

    def setTantSpectrum(self, tantSpectrum):
        """
        Set tantSpectrum with the specified float []  []  value.
        tantSpectrum The float []  []  value to which tantSpectrum is to be set.


        """

        # value must be a list
        if not isinstance(tantSpectrum, list):
            raise ValueError("The value of tantSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tantSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of tantSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(tantSpectrum, float):
                raise ValueError(
                    "type of the first value in tantSpectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tantSpectrum = copy.deepcopy(tantSpectrum)
        except Exception as exc:
            raise ValueError("Invalid tantSpectrum : " + str(exc))

        self._tantSpectrumExists = True

    def clearTantSpectrum(self):
        """
        Mark tantSpectrum, which is an optional field, as non-existent.
        """
        self._tantSpectrumExists = False

    # ===> Attribute tantTsysFlag, which is optional
    _tantTsysFlagExists = False

    _tantTsysFlag = None

    def isTantTsysFlagExists(self):
        """
        The attribute tantTsysFlag is optional. Return True if this attribute exists.
        return True if and only if the tantTsysFlag attribute exists.
        """
        return self._tantTsysFlagExists

    def getTantTsysFlag(self):
        """
        Get tantTsysFlag, which is optional.
        return tantTsysFlag as bool
        raises ValueError If tantTsysFlag does not exist.
        """
        if not self._tantTsysFlagExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tantTsysFlag
                + " attribute in table SysCal does not exist!"
            )

        return self._tantTsysFlag

    def setTantTsysFlag(self, tantTsysFlag):
        """
        Set tantTsysFlag with the specified bool value.
        tantTsysFlag The bool value to which tantTsysFlag is to be set.


        """

        self._tantTsysFlag = bool(tantTsysFlag)

        self._tantTsysFlagExists = True

    def clearTantTsysFlag(self):
        """
        Mark tantTsysFlag, which is an optional field, as non-existent.
        """
        self._tantTsysFlagExists = False

    # ===> Attribute tantTsysSpectrum, which is optional
    _tantTsysSpectrumExists = False

    _tantTsysSpectrum = None  # this is a 2D list of float

    def isTantTsysSpectrumExists(self):
        """
        The attribute tantTsysSpectrum is optional. Return True if this attribute exists.
        return True if and only if the tantTsysSpectrum attribute exists.
        """
        return self._tantTsysSpectrumExists

    def getTantTsysSpectrum(self):
        """
        Get tantTsysSpectrum, which is optional.
        return tantTsysSpectrum as float []  []
        raises ValueError If tantTsysSpectrum does not exist.
        """
        if not self._tantTsysSpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + tantTsysSpectrum
                + " attribute in table SysCal does not exist!"
            )

        return copy.deepcopy(self._tantTsysSpectrum)

    def setTantTsysSpectrum(self, tantTsysSpectrum):
        """
        Set tantTsysSpectrum with the specified float []  []  value.
        tantTsysSpectrum The float []  []  value to which tantTsysSpectrum is to be set.


        """

        # value must be a list
        if not isinstance(tantTsysSpectrum, list):
            raise ValueError("The value of tantTsysSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tantTsysSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of tantTsysSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(tantTsysSpectrum, float):
                raise ValueError(
                    "type of the first value in tantTsysSpectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tantTsysSpectrum = copy.deepcopy(tantTsysSpectrum)
        except Exception as exc:
            raise ValueError("Invalid tantTsysSpectrum : " + str(exc))

        self._tantTsysSpectrumExists = True

    def clearTantTsysSpectrum(self):
        """
        Mark tantTsysSpectrum, which is an optional field, as non-existent.
        """
        self._tantTsysSpectrumExists = False

    # ===> Attribute phaseDiffFlag, which is optional
    _phaseDiffFlagExists = False

    _phaseDiffFlag = None

    def isPhaseDiffFlagExists(self):
        """
        The attribute phaseDiffFlag is optional. Return True if this attribute exists.
        return True if and only if the phaseDiffFlag attribute exists.
        """
        return self._phaseDiffFlagExists

    def getPhaseDiffFlag(self):
        """
        Get phaseDiffFlag, which is optional.
        return phaseDiffFlag as bool
        raises ValueError If phaseDiffFlag does not exist.
        """
        if not self._phaseDiffFlagExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + phaseDiffFlag
                + " attribute in table SysCal does not exist!"
            )

        return self._phaseDiffFlag

    def setPhaseDiffFlag(self, phaseDiffFlag):
        """
        Set phaseDiffFlag with the specified bool value.
        phaseDiffFlag The bool value to which phaseDiffFlag is to be set.


        """

        self._phaseDiffFlag = bool(phaseDiffFlag)

        self._phaseDiffFlagExists = True

    def clearPhaseDiffFlag(self):
        """
        Mark phaseDiffFlag, which is an optional field, as non-existent.
        """
        self._phaseDiffFlagExists = False

    # ===> Attribute phaseDiffSpectrum, which is optional
    _phaseDiffSpectrumExists = False

    _phaseDiffSpectrum = None  # this is a 2D list of float

    def isPhaseDiffSpectrumExists(self):
        """
        The attribute phaseDiffSpectrum is optional. Return True if this attribute exists.
        return True if and only if the phaseDiffSpectrum attribute exists.
        """
        return self._phaseDiffSpectrumExists

    def getPhaseDiffSpectrum(self):
        """
        Get phaseDiffSpectrum, which is optional.
        return phaseDiffSpectrum as float []  []
        raises ValueError If phaseDiffSpectrum does not exist.
        """
        if not self._phaseDiffSpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + phaseDiffSpectrum
                + " attribute in table SysCal does not exist!"
            )

        return copy.deepcopy(self._phaseDiffSpectrum)

    def setPhaseDiffSpectrum(self, phaseDiffSpectrum):
        """
        Set phaseDiffSpectrum with the specified float []  []  value.
        phaseDiffSpectrum The float []  []  value to which phaseDiffSpectrum is to be set.


        """

        # value must be a list
        if not isinstance(phaseDiffSpectrum, list):
            raise ValueError("The value of phaseDiffSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(phaseDiffSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of phaseDiffSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(phaseDiffSpectrum, float):
                raise ValueError(
                    "type of the first value in phaseDiffSpectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phaseDiffSpectrum = copy.deepcopy(phaseDiffSpectrum)
        except Exception as exc:
            raise ValueError("Invalid phaseDiffSpectrum : " + str(exc))

        self._phaseDiffSpectrumExists = True

    def clearPhaseDiffSpectrum(self):
        """
        Mark phaseDiffSpectrum, which is an optional field, as non-existent.
        """
        self._phaseDiffSpectrumExists = False

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

    # ===> Slice link from a row of SysCal table to a collection of row of Feed table.
    def getFeeds(self):
        """
        Get the collection of rows in the Feed table having feedId == this.feedId
        """

        return self._table.getContainer().getFeed().getRowByFeedId(self._feedId)

    def getSpectralWindowUsingSpectralWindowId(self):
        """
        Returns the row in the SpectralWindow table having SpectralWindow.spectralWindowId == spectralWindowId

        """

        return (
            self._table.getContainer()
            .getSpectralWindow()
            .getRowByKey(self._spectralWindowId)
        )

    # comparison methods

    def compareNoAutoInc(
        self, antennaId, spectralWindowId, timeInterval, feedId, numReceptor, numChan
    ):
        """
        Compare each attribute except the autoincrementable one of this SysCalRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaId is a Tag, compare using the equals method.
        if not self._antennaId.equals(antennaId):
            return False

        # spectralWindowId is a Tag, compare using the equals method.
        if not self._spectralWindowId.equals(spectralWindowId):
            return False

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # feedId is a int, compare using the == operator.
        if not (self._feedId == feedId):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # numChan is a int, compare using the == operator.
        if not (self._numChan == numChan):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumReceptor(), otherRow.getNumChan()
        )

    def compareRequiredValue(self, numReceptor, numChan):

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # numChan is a int, compare using the == operator.
        if not (self._numChan == numChan):
            return False

        return True
