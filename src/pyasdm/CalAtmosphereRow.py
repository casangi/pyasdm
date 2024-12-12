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
# File CalAtmosphereRow.py
#

import pyasdm.CalAtmosphereTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.ReceiverBand import ReceiverBand


from pyasdm.enumerations.BasebandName import BasebandName


from pyasdm.enumerations.PolarizationType import PolarizationType


from pyasdm.enumerations.SyscalMethod import SyscalMethod


from xml.dom import minidom

import copy


class CalAtmosphereRow:
    """
    The CalAtmosphereRow class is a row of a CalAtmosphereTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a CalAtmosphereRow.
        When row is None, create an empty row attached to table, which must be a CalAtmosphereTable.
        When row is given, copy those values in to the new row. The row argument must be a CalAtmosphereRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.CalAtmosphereTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._receiverBand = ReceiverBand.from_int(0)

        self._antennaName = None

        self._basebandName = BasebandName.from_int(0)

        self._startValidTime = ArrayTime()

        self._endValidTime = ArrayTime()

        self._numFreq = 0

        self._numLoad = 0

        self._numReceptor = 0

        self._forwardEffSpectrum = []  # this is a list of float []  []

        self._frequencyRange = []  # this is a list of Frequency []

        self._groundPressure = Pressure()

        self._groundRelHumidity = Humidity()

        self._frequencySpectrum = []  # this is a list of Frequency []

        self._groundTemperature = Temperature()

        self._polarizationTypes = []  # this is a list of PolarizationType []

        self._powerSkySpectrum = []  # this is a list of float []  []

        self._powerLoadSpectrum = []  # this is a list of float []  []  []

        self._syscalType = SyscalMethod.from_int(0)

        self._tAtmSpectrum = []  # this is a list of Temperature []  []

        self._tRecSpectrum = []  # this is a list of Temperature []  []

        self._tSysSpectrum = []  # this is a list of Temperature []  []

        self._tauSpectrum = []  # this is a list of float []  []

        self._tAtm = []  # this is a list of Temperature []

        self._tRec = []  # this is a list of Temperature []

        self._tSys = []  # this is a list of Temperature []

        self._tau = []  # this is a list of float []

        self._water = []  # this is a list of Length []

        self._waterError = []  # this is a list of Length []

        self._alphaSpectrumExists = False

        self._alphaSpectrum = []  # this is a list of float []  []

        self._forwardEfficiencyExists = False

        self._forwardEfficiency = []  # this is a list of float []

        self._forwardEfficiencyErrorExists = False

        self._forwardEfficiencyError = []  # this is a list of float []

        self._sbGainExists = False

        self._sbGain = []  # this is a list of float []

        self._sbGainErrorExists = False

        self._sbGainError = []  # this is a list of float []

        self._sbGainSpectrumExists = False

        self._sbGainSpectrum = []  # this is a list of float []  []

        # extrinsic attributes

        self._calDataId = Tag()

        self._calReductionId = Tag()

        if row is not None:
            if not isinstance(row, CalAtmosphereRow):
                raise ValueError("row must be a MainRow")

            # copy constructor

            self._antennaName = row._antennaName

            # We force the attribute of the result to be not None
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            # We force the attribute of the result to be not None
            if row._basebandName is None:
                self._basebandName = BasebandName.from_int(0)
            else:
                self._basebandName = BasebandName(row._basebandName)

            self._calDataId = Tag(row._calDataId)

            self._calReductionId = Tag(row._calReductionId)

            self._startValidTime = ArrayTime(row._startValidTime)

            self._endValidTime = ArrayTime(row._endValidTime)

            self._numFreq = row._numFreq

            self._numLoad = row._numLoad

            self._numReceptor = row._numReceptor

            # forwardEffSpectrum is a  list , make a deep copy
            self._forwardEffSpectrum = copy.deepcopy(row._forwardEffSpectrum)

            # frequencyRange is a  list , make a deep copy
            self._frequencyRange = copy.deepcopy(row._frequencyRange)

            self._groundPressure = Pressure(row._groundPressure)

            self._groundRelHumidity = Humidity(row._groundRelHumidity)

            # frequencySpectrum is a  list , make a deep copy
            self._frequencySpectrum = copy.deepcopy(row._frequencySpectrum)

            self._groundTemperature = Temperature(row._groundTemperature)

            # polarizationTypes is a  list , make a deep copy
            self._polarizationTypes = copy.deepcopy(row._polarizationTypes)

            # powerSkySpectrum is a  list , make a deep copy
            self._powerSkySpectrum = copy.deepcopy(row._powerSkySpectrum)

            # powerLoadSpectrum is a  list , make a deep copy
            self._powerLoadSpectrum = copy.deepcopy(row._powerLoadSpectrum)

            # We force the attribute of the result to be not None
            if row._syscalType is None:
                self._syscalType = SyscalMethod.from_int(0)
            else:
                self._syscalType = SyscalMethod(row._syscalType)

            # tAtmSpectrum is a  list , make a deep copy
            self._tAtmSpectrum = copy.deepcopy(row._tAtmSpectrum)

            # tRecSpectrum is a  list , make a deep copy
            self._tRecSpectrum = copy.deepcopy(row._tRecSpectrum)

            # tSysSpectrum is a  list , make a deep copy
            self._tSysSpectrum = copy.deepcopy(row._tSysSpectrum)

            # tauSpectrum is a  list , make a deep copy
            self._tauSpectrum = copy.deepcopy(row._tauSpectrum)

            # tAtm is a  list , make a deep copy
            self._tAtm = copy.deepcopy(row._tAtm)

            # tRec is a  list , make a deep copy
            self._tRec = copy.deepcopy(row._tRec)

            # tSys is a  list , make a deep copy
            self._tSys = copy.deepcopy(row._tSys)

            # tau is a  list , make a deep copy
            self._tau = copy.deepcopy(row._tau)

            # water is a  list , make a deep copy
            self._water = copy.deepcopy(row._water)

            # waterError is a  list , make a deep copy
            self._waterError = copy.deepcopy(row._waterError)

            # by default set systematically alphaSpectrum's value to something not None

            if row._alphaSpectrumExists:

                # alphaSpectrum is a list, make a deep copy
                self.alphaSpectrum = copy.deepcopy(row.alphaSpectrum)

                self._alphaSpectrumExists = True

            # by default set systematically forwardEfficiency's value to something not None

            if row._forwardEfficiencyExists:

                # forwardEfficiency is a list, make a deep copy
                self.forwardEfficiency = copy.deepcopy(row.forwardEfficiency)

                self._forwardEfficiencyExists = True

            # by default set systematically forwardEfficiencyError's value to something not None

            if row._forwardEfficiencyErrorExists:

                # forwardEfficiencyError is a list, make a deep copy
                self.forwardEfficiencyError = copy.deepcopy(row.forwardEfficiencyError)

                self._forwardEfficiencyErrorExists = True

            # by default set systematically sbGain's value to something not None

            if row._sbGainExists:

                # sbGain is a list, make a deep copy
                self.sbGain = copy.deepcopy(row.sbGain)

                self._sbGainExists = True

            # by default set systematically sbGainError's value to something not None

            if row._sbGainErrorExists:

                # sbGainError is a list, make a deep copy
                self.sbGainError = copy.deepcopy(row.sbGainError)

                self._sbGainErrorExists = True

            # by default set systematically sbGainSpectrum's value to something not None

            if row._sbGainSpectrumExists:

                # sbGainSpectrum is a list, make a deep copy
                self.sbGainSpectrum = copy.deepcopy(row.sbGainSpectrum)

                self._sbGainSpectrumExists = True

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

        result += Parser.valueToXML(
            "receiverBand", ReceiverBand.name(self._receiverBand)
        )

        result += Parser.valueToXML("antennaName", self._antennaName)

        result += Parser.valueToXML(
            "basebandName", BasebandName.name(self._basebandName)
        )

        result += Parser.extendedValueToXML("startValidTime", self._startValidTime)

        result += Parser.extendedValueToXML("endValidTime", self._endValidTime)

        result += Parser.valueToXML("numFreq", self._numFreq)

        result += Parser.valueToXML("numLoad", self._numLoad)

        result += Parser.valueToXML("numReceptor", self._numReceptor)

        result += Parser.listValueToXML("forwardEffSpectrum", self._forwardEffSpectrum)

        result += Parser.listExtendedValueToXML("frequencyRange", self._frequencyRange)

        result += Parser.extendedValueToXML("groundPressure", self._groundPressure)

        result += Parser.extendedValueToXML(
            "groundRelHumidity", self._groundRelHumidity
        )

        result += Parser.listExtendedValueToXML(
            "frequencySpectrum", self._frequencySpectrum
        )

        result += Parser.extendedValueToXML(
            "groundTemperature", self._groundTemperature
        )

        result += Parser.listEnumValueToXML(
            "polarizationTypes", self._polarizationTypes
        )

        result += Parser.listValueToXML("powerSkySpectrum", self._powerSkySpectrum)

        result += Parser.listValueToXML("powerLoadSpectrum", self._powerLoadSpectrum)

        result += Parser.valueToXML("syscalType", SyscalMethod.name(self._syscalType))

        result += Parser.listExtendedValueToXML("tAtmSpectrum", self._tAtmSpectrum)

        result += Parser.listExtendedValueToXML("tRecSpectrum", self._tRecSpectrum)

        result += Parser.listExtendedValueToXML("tSysSpectrum", self._tSysSpectrum)

        result += Parser.listValueToXML("tauSpectrum", self._tauSpectrum)

        result += Parser.listExtendedValueToXML("tAtm", self._tAtm)

        result += Parser.listExtendedValueToXML("tRec", self._tRec)

        result += Parser.listExtendedValueToXML("tSys", self._tSys)

        result += Parser.listValueToXML("tau", self._tau)

        result += Parser.listExtendedValueToXML("water", self._water)

        result += Parser.listExtendedValueToXML("waterError", self._waterError)

        if self._alphaSpectrumExists:

            result += Parser.listValueToXML("alphaSpectrum", self._alphaSpectrum)

        if self._forwardEfficiencyExists:

            result += Parser.listValueToXML(
                "forwardEfficiency", self._forwardEfficiency
            )

        if self._forwardEfficiencyErrorExists:

            result += Parser.listValueToXML(
                "forwardEfficiencyError", self._forwardEfficiencyError
            )

        if self._sbGainExists:

            result += Parser.listValueToXML("sbGain", self._sbGain)

        if self._sbGainErrorExists:

            result += Parser.listValueToXML("sbGainError", self._sbGainError)

        if self._sbGainSpectrumExists:

            result += Parser.listValueToXML("sbGainSpectrum", self._sbGainSpectrum)

        # extrinsic attributes

        result += Parser.extendedValueToXML("calDataId", self._calDataId)

        result += Parser.extendedValueToXML("calReductionId", self._calReductionId)

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
                "xmlrow is not a string or a minidom.Element", "CalAtmosphereTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "CalAtmosphereTable")

        # intrinsic attribute values

        receiverBandNode = rowdom.getElementsByTagName("receiverBand")[0]

        self._receiverBand = ReceiverBand.newReceiverBand(
            receiverBandNode.firstChild.data.strip()
        )

        antennaNameNode = rowdom.getElementsByTagName("antennaName")[0]

        self._antennaName = str(antennaNameNode.firstChild.data.strip())

        basebandNameNode = rowdom.getElementsByTagName("basebandName")[0]

        self._basebandName = BasebandName.newBasebandName(
            basebandNameNode.firstChild.data.strip()
        )

        startValidTimeNode = rowdom.getElementsByTagName("startValidTime")[0]

        self._startValidTime = ArrayTime(startValidTimeNode.firstChild.data.strip())

        endValidTimeNode = rowdom.getElementsByTagName("endValidTime")[0]

        self._endValidTime = ArrayTime(endValidTimeNode.firstChild.data.strip())

        numFreqNode = rowdom.getElementsByTagName("numFreq")[0]

        self._numFreq = int(numFreqNode.firstChild.data.strip())

        numLoadNode = rowdom.getElementsByTagName("numLoad")[0]

        self._numLoad = int(numLoadNode.firstChild.data.strip())

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")[0]

        self._numReceptor = int(numReceptorNode.firstChild.data.strip())

        forwardEffSpectrumNode = rowdom.getElementsByTagName("forwardEffSpectrum")[0]

        forwardEffSpectrumStr = forwardEffSpectrumNode.firstChild.data.strip()

        self._forwardEffSpectrum = Parser.stringListToLists(
            forwardEffSpectrumStr, float, "CalAtmosphere", False
        )

        frequencyRangeNode = rowdom.getElementsByTagName("frequencyRange")[0]

        frequencyRangeStr = frequencyRangeNode.firstChild.data.strip()

        self._frequencyRange = Parser.stringListToLists(
            frequencyRangeStr, Frequency, "CalAtmosphere", True
        )

        groundPressureNode = rowdom.getElementsByTagName("groundPressure")[0]

        self._groundPressure = Pressure(groundPressureNode.firstChild.data.strip())

        groundRelHumidityNode = rowdom.getElementsByTagName("groundRelHumidity")[0]

        self._groundRelHumidity = Humidity(
            groundRelHumidityNode.firstChild.data.strip()
        )

        frequencySpectrumNode = rowdom.getElementsByTagName("frequencySpectrum")[0]

        frequencySpectrumStr = frequencySpectrumNode.firstChild.data.strip()

        self._frequencySpectrum = Parser.stringListToLists(
            frequencySpectrumStr, Frequency, "CalAtmosphere", True
        )

        groundTemperatureNode = rowdom.getElementsByTagName("groundTemperature")[0]

        self._groundTemperature = Temperature(
            groundTemperatureNode.firstChild.data.strip()
        )

        polarizationTypesNode = rowdom.getElementsByTagName("polarizationTypes")[0]

        polarizationTypesStr = polarizationTypesNode.firstChild.data.strip()
        self._polarizationTypes = Parser.stringListToLists(
            polarizationTypesStr, PolarizationType, "CalAtmosphere", False
        )

        powerSkySpectrumNode = rowdom.getElementsByTagName("powerSkySpectrum")[0]

        powerSkySpectrumStr = powerSkySpectrumNode.firstChild.data.strip()

        self._powerSkySpectrum = Parser.stringListToLists(
            powerSkySpectrumStr, float, "CalAtmosphere", False
        )

        powerLoadSpectrumNode = rowdom.getElementsByTagName("powerLoadSpectrum")[0]

        powerLoadSpectrumStr = powerLoadSpectrumNode.firstChild.data.strip()

        self._powerLoadSpectrum = Parser.stringListToLists(
            powerLoadSpectrumStr, float, "CalAtmosphere", False
        )

        syscalTypeNode = rowdom.getElementsByTagName("syscalType")[0]

        self._syscalType = SyscalMethod.newSyscalMethod(
            syscalTypeNode.firstChild.data.strip()
        )

        tAtmSpectrumNode = rowdom.getElementsByTagName("tAtmSpectrum")[0]

        tAtmSpectrumStr = tAtmSpectrumNode.firstChild.data.strip()

        self._tAtmSpectrum = Parser.stringListToLists(
            tAtmSpectrumStr, Temperature, "CalAtmosphere", True
        )

        tRecSpectrumNode = rowdom.getElementsByTagName("tRecSpectrum")[0]

        tRecSpectrumStr = tRecSpectrumNode.firstChild.data.strip()

        self._tRecSpectrum = Parser.stringListToLists(
            tRecSpectrumStr, Temperature, "CalAtmosphere", True
        )

        tSysSpectrumNode = rowdom.getElementsByTagName("tSysSpectrum")[0]

        tSysSpectrumStr = tSysSpectrumNode.firstChild.data.strip()

        self._tSysSpectrum = Parser.stringListToLists(
            tSysSpectrumStr, Temperature, "CalAtmosphere", True
        )

        tauSpectrumNode = rowdom.getElementsByTagName("tauSpectrum")[0]

        tauSpectrumStr = tauSpectrumNode.firstChild.data.strip()

        self._tauSpectrum = Parser.stringListToLists(
            tauSpectrumStr, float, "CalAtmosphere", False
        )

        tAtmNode = rowdom.getElementsByTagName("tAtm")[0]

        tAtmStr = tAtmNode.firstChild.data.strip()

        self._tAtm = Parser.stringListToLists(
            tAtmStr, Temperature, "CalAtmosphere", True
        )

        tRecNode = rowdom.getElementsByTagName("tRec")[0]

        tRecStr = tRecNode.firstChild.data.strip()

        self._tRec = Parser.stringListToLists(
            tRecStr, Temperature, "CalAtmosphere", True
        )

        tSysNode = rowdom.getElementsByTagName("tSys")[0]

        tSysStr = tSysNode.firstChild.data.strip()

        self._tSys = Parser.stringListToLists(
            tSysStr, Temperature, "CalAtmosphere", True
        )

        tauNode = rowdom.getElementsByTagName("tau")[0]

        tauStr = tauNode.firstChild.data.strip()

        self._tau = Parser.stringListToLists(tauStr, float, "CalAtmosphere", False)

        waterNode = rowdom.getElementsByTagName("water")[0]

        waterStr = waterNode.firstChild.data.strip()

        self._water = Parser.stringListToLists(waterStr, Length, "CalAtmosphere", True)

        waterErrorNode = rowdom.getElementsByTagName("waterError")[0]

        waterErrorStr = waterErrorNode.firstChild.data.strip()

        self._waterError = Parser.stringListToLists(
            waterErrorStr, Length, "CalAtmosphere", True
        )

        alphaSpectrumNode = rowdom.getElementsByTagName("alphaSpectrum")
        if len(alphaSpectrumNode) > 0:

            alphaSpectrumStr = alphaSpectrumNode[0].firstChild.data.strip()

            self._alphaSpectrum = Parser.stringListToLists(
                alphaSpectrumStr, float, "CalAtmosphere", False
            )

            self._alphaSpectrumExists = True

        forwardEfficiencyNode = rowdom.getElementsByTagName("forwardEfficiency")
        if len(forwardEfficiencyNode) > 0:

            forwardEfficiencyStr = forwardEfficiencyNode[0].firstChild.data.strip()

            self._forwardEfficiency = Parser.stringListToLists(
                forwardEfficiencyStr, float, "CalAtmosphere", False
            )

            self._forwardEfficiencyExists = True

        forwardEfficiencyErrorNode = rowdom.getElementsByTagName(
            "forwardEfficiencyError"
        )
        if len(forwardEfficiencyErrorNode) > 0:

            forwardEfficiencyErrorStr = forwardEfficiencyErrorNode[
                0
            ].firstChild.data.strip()

            self._forwardEfficiencyError = Parser.stringListToLists(
                forwardEfficiencyErrorStr, float, "CalAtmosphere", False
            )

            self._forwardEfficiencyErrorExists = True

        sbGainNode = rowdom.getElementsByTagName("sbGain")
        if len(sbGainNode) > 0:

            sbGainStr = sbGainNode[0].firstChild.data.strip()

            self._sbGain = Parser.stringListToLists(
                sbGainStr, float, "CalAtmosphere", False
            )

            self._sbGainExists = True

        sbGainErrorNode = rowdom.getElementsByTagName("sbGainError")
        if len(sbGainErrorNode) > 0:

            sbGainErrorStr = sbGainErrorNode[0].firstChild.data.strip()

            self._sbGainError = Parser.stringListToLists(
                sbGainErrorStr, float, "CalAtmosphere", False
            )

            self._sbGainErrorExists = True

        sbGainSpectrumNode = rowdom.getElementsByTagName("sbGainSpectrum")
        if len(sbGainSpectrumNode) > 0:

            sbGainSpectrumStr = sbGainSpectrumNode[0].firstChild.data.strip()

            self._sbGainSpectrum = Parser.stringListToLists(
                sbGainSpectrumStr, float, "CalAtmosphere", False
            )

            self._sbGainSpectrumExists = True

        # extrinsic attribute values

        calDataIdNode = rowdom.getElementsByTagName("calDataId")[0]

        self._calDataId = Tag(calDataIdNode.firstChild.data.strip())

        calReductionIdNode = rowdom.getElementsByTagName("calReductionId")[0]

        self._calReductionId = Tag(calReductionIdNode.firstChild.data.strip())

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

    # ===> Attribute receiverBand

    _receiverBand = ReceiverBand.from_int(0)

    def getReceiverBand(self):
        """
        Get receiverBand.
        return receiverBand as ReceiverBand
        """

        return self._receiverBand

    def setReceiverBand(self, receiverBand):
        """
        Set receiverBand with the specified ReceiverBand value.
        receiverBand The ReceiverBand value to which receiverBand is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the receiverBand field, which is part of the key, after this row has been added to this table."
            )

        self._receiverBand = ReceiverBand(receiverBand)

    # ===> Attribute antennaName

    _antennaName = None

    def getAntennaName(self):
        """
        Get antennaName.
        return antennaName as str
        """

        return self._antennaName

    def setAntennaName(self, antennaName):
        """
        Set antennaName with the specified str value.
        antennaName The str value to which antennaName is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the antennaName field, which is part of the key, after this row has been added to this table."
            )

        self._antennaName = str(antennaName)

    # ===> Attribute basebandName

    _basebandName = BasebandName.from_int(0)

    def getBasebandName(self):
        """
        Get basebandName.
        return basebandName as BasebandName
        """

        return self._basebandName

    def setBasebandName(self, basebandName):
        """
        Set basebandName with the specified BasebandName value.
        basebandName The BasebandName value to which basebandName is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the basebandName field, which is part of the key, after this row has been added to this table."
            )

        self._basebandName = BasebandName(basebandName)

    # ===> Attribute startValidTime

    _startValidTime = ArrayTime()

    def getStartValidTime(self):
        """
        Get startValidTime.
        return startValidTime as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._startValidTime)

    def setStartValidTime(self, startValidTime):
        """
        Set startValidTime with the specified ArrayTime value.
        startValidTime The ArrayTime value to which startValidTime is to be set.
        The value of startValidTime can be anything allowed by the ArrayTime constructor.

        """

        self._startValidTime = ArrayTime(startValidTime)

    # ===> Attribute endValidTime

    _endValidTime = ArrayTime()

    def getEndValidTime(self):
        """
        Get endValidTime.
        return endValidTime as ArrayTime
        """

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._endValidTime)

    def setEndValidTime(self, endValidTime):
        """
        Set endValidTime with the specified ArrayTime value.
        endValidTime The ArrayTime value to which endValidTime is to be set.
        The value of endValidTime can be anything allowed by the ArrayTime constructor.

        """

        self._endValidTime = ArrayTime(endValidTime)

    # ===> Attribute numFreq

    _numFreq = 0

    def getNumFreq(self):
        """
        Get numFreq.
        return numFreq as int
        """

        return self._numFreq

    def setNumFreq(self, numFreq):
        """
        Set numFreq with the specified int value.
        numFreq The int value to which numFreq is to be set.


        """

        self._numFreq = int(numFreq)

    # ===> Attribute numLoad

    _numLoad = 0

    def getNumLoad(self):
        """
        Get numLoad.
        return numLoad as int
        """

        return self._numLoad

    def setNumLoad(self, numLoad):
        """
        Set numLoad with the specified int value.
        numLoad The int value to which numLoad is to be set.


        """

        self._numLoad = int(numLoad)

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

    # ===> Attribute forwardEffSpectrum

    _forwardEffSpectrum = None  # this is a 2D list of float

    def getForwardEffSpectrum(self):
        """
        Get forwardEffSpectrum.
        return forwardEffSpectrum as float []  []
        """

        return copy.deepcopy(self._forwardEffSpectrum)

    def setForwardEffSpectrum(self, forwardEffSpectrum):
        """
        Set forwardEffSpectrum with the specified float []  []  value.
        forwardEffSpectrum The float []  []  value to which forwardEffSpectrum is to be set.


        """

        # value must be a list
        if not isinstance(forwardEffSpectrum, list):
            raise ValueError("The value of forwardEffSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(forwardEffSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of forwardEffSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(forwardEffSpectrum, float):
                raise ValueError(
                    "type of the first value in forwardEffSpectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._forwardEffSpectrum = copy.deepcopy(forwardEffSpectrum)
        except Exception as exc:
            raise ValueError("Invalid forwardEffSpectrum : " + str(exc))

    # ===> Attribute frequencyRange

    _frequencyRange = None  # this is a 1D list of Frequency

    def getFrequencyRange(self):
        """
        Get frequencyRange.
        return frequencyRange as Frequency []
        """

        return copy.deepcopy(self._frequencyRange)

    def setFrequencyRange(self, frequencyRange):
        """
        Set frequencyRange with the specified Frequency []  value.
        frequencyRange The Frequency []  value to which frequencyRange is to be set.
        The value of frequencyRange can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(frequencyRange, list):
            raise ValueError("The value of frequencyRange must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(frequencyRange)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of frequencyRange is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(frequencyRange, Frequency):
                raise ValueError(
                    "type of the first value in frequencyRange is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._frequencyRange = copy.deepcopy(frequencyRange)
        except Exception as exc:
            raise ValueError("Invalid frequencyRange : " + str(exc))

    # ===> Attribute groundPressure

    _groundPressure = Pressure()

    def getGroundPressure(self):
        """
        Get groundPressure.
        return groundPressure as Pressure
        """

        # make sure it is a copy of Pressure
        return Pressure(self._groundPressure)

    def setGroundPressure(self, groundPressure):
        """
        Set groundPressure with the specified Pressure value.
        groundPressure The Pressure value to which groundPressure is to be set.
        The value of groundPressure can be anything allowed by the Pressure constructor.

        """

        self._groundPressure = Pressure(groundPressure)

    # ===> Attribute groundRelHumidity

    _groundRelHumidity = Humidity()

    def getGroundRelHumidity(self):
        """
        Get groundRelHumidity.
        return groundRelHumidity as Humidity
        """

        # make sure it is a copy of Humidity
        return Humidity(self._groundRelHumidity)

    def setGroundRelHumidity(self, groundRelHumidity):
        """
        Set groundRelHumidity with the specified Humidity value.
        groundRelHumidity The Humidity value to which groundRelHumidity is to be set.
        The value of groundRelHumidity can be anything allowed by the Humidity constructor.

        """

        self._groundRelHumidity = Humidity(groundRelHumidity)

    # ===> Attribute frequencySpectrum

    _frequencySpectrum = None  # this is a 1D list of Frequency

    def getFrequencySpectrum(self):
        """
        Get frequencySpectrum.
        return frequencySpectrum as Frequency []
        """

        return copy.deepcopy(self._frequencySpectrum)

    def setFrequencySpectrum(self, frequencySpectrum):
        """
        Set frequencySpectrum with the specified Frequency []  value.
        frequencySpectrum The Frequency []  value to which frequencySpectrum is to be set.
        The value of frequencySpectrum can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(frequencySpectrum, list):
            raise ValueError("The value of frequencySpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(frequencySpectrum)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of frequencySpectrum is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not Parser.checkListType(frequencySpectrum, Frequency):
                raise ValueError(
                    "type of the first value in frequencySpectrum is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._frequencySpectrum = copy.deepcopy(frequencySpectrum)
        except Exception as exc:
            raise ValueError("Invalid frequencySpectrum : " + str(exc))

    # ===> Attribute groundTemperature

    _groundTemperature = Temperature()

    def getGroundTemperature(self):
        """
        Get groundTemperature.
        return groundTemperature as Temperature
        """

        # make sure it is a copy of Temperature
        return Temperature(self._groundTemperature)

    def setGroundTemperature(self, groundTemperature):
        """
        Set groundTemperature with the specified Temperature value.
        groundTemperature The Temperature value to which groundTemperature is to be set.
        The value of groundTemperature can be anything allowed by the Temperature constructor.

        """

        self._groundTemperature = Temperature(groundTemperature)

    # ===> Attribute polarizationTypes

    _polarizationTypes = None  # this is a 1D list of PolarizationType

    def getPolarizationTypes(self):
        """
        Get polarizationTypes.
        return polarizationTypes as PolarizationType []
        """

        return copy.deepcopy(self._polarizationTypes)

    def setPolarizationTypes(self, polarizationTypes):
        """
        Set polarizationTypes with the specified PolarizationType []  value.
        polarizationTypes The PolarizationType []  value to which polarizationTypes is to be set.


        """

        # value must be a list
        if not isinstance(polarizationTypes, list):
            raise ValueError("The value of polarizationTypes must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(polarizationTypes)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of polarizationTypes is not correct")

            # the type of the values in the list must be PolarizationType
            # note : this only checks the first value found
            if not Parser.checkListType(polarizationTypes, PolarizationType):
                raise ValueError(
                    "type of the first value in polarizationTypes is not PolarizationType as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._polarizationTypes = copy.deepcopy(polarizationTypes)
        except Exception as exc:
            raise ValueError("Invalid polarizationTypes : " + str(exc))

    # ===> Attribute powerSkySpectrum

    _powerSkySpectrum = None  # this is a 2D list of float

    def getPowerSkySpectrum(self):
        """
        Get powerSkySpectrum.
        return powerSkySpectrum as float []  []
        """

        return copy.deepcopy(self._powerSkySpectrum)

    def setPowerSkySpectrum(self, powerSkySpectrum):
        """
        Set powerSkySpectrum with the specified float []  []  value.
        powerSkySpectrum The float []  []  value to which powerSkySpectrum is to be set.


        """

        # value must be a list
        if not isinstance(powerSkySpectrum, list):
            raise ValueError("The value of powerSkySpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(powerSkySpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of powerSkySpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(powerSkySpectrum, float):
                raise ValueError(
                    "type of the first value in powerSkySpectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._powerSkySpectrum = copy.deepcopy(powerSkySpectrum)
        except Exception as exc:
            raise ValueError("Invalid powerSkySpectrum : " + str(exc))

    # ===> Attribute powerLoadSpectrum

    _powerLoadSpectrum = None  # this is a 2D list of float

    def getPowerLoadSpectrum(self):
        """
        Get powerLoadSpectrum.
        return powerLoadSpectrum as float []  []  []
        """

        return copy.deepcopy(self._powerLoadSpectrum)

    def setPowerLoadSpectrum(self, powerLoadSpectrum):
        """
        Set powerLoadSpectrum with the specified float []  []  []  value.
        powerLoadSpectrum The float []  []  []  value to which powerLoadSpectrum is to be set.


        """

        # value must be a list
        if not isinstance(powerLoadSpectrum, list):
            raise ValueError("The value of powerLoadSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(powerLoadSpectrum)

            shapeOK = len(listDims) == 3

            if not shapeOK:
                raise ValueError("shape of powerLoadSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(powerLoadSpectrum, float):
                raise ValueError(
                    "type of the first value in powerLoadSpectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._powerLoadSpectrum = copy.deepcopy(powerLoadSpectrum)
        except Exception as exc:
            raise ValueError("Invalid powerLoadSpectrum : " + str(exc))

    # ===> Attribute syscalType

    _syscalType = SyscalMethod.from_int(0)

    def getSyscalType(self):
        """
        Get syscalType.
        return syscalType as SyscalMethod
        """

        return self._syscalType

    def setSyscalType(self, syscalType):
        """
        Set syscalType with the specified SyscalMethod value.
        syscalType The SyscalMethod value to which syscalType is to be set.


        """

        self._syscalType = SyscalMethod(syscalType)

    # ===> Attribute tAtmSpectrum

    _tAtmSpectrum = None  # this is a 2D list of Temperature

    def getTAtmSpectrum(self):
        """
        Get tAtmSpectrum.
        return tAtmSpectrum as Temperature []  []
        """

        return copy.deepcopy(self._tAtmSpectrum)

    def setTAtmSpectrum(self, tAtmSpectrum):
        """
        Set tAtmSpectrum with the specified Temperature []  []  value.
        tAtmSpectrum The Temperature []  []  value to which tAtmSpectrum is to be set.
        The value of tAtmSpectrum can be anything allowed by the Temperature []  []  constructor.

        """

        # value must be a list
        if not isinstance(tAtmSpectrum, list):
            raise ValueError("The value of tAtmSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tAtmSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of tAtmSpectrum is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(tAtmSpectrum, Temperature):
                raise ValueError(
                    "type of the first value in tAtmSpectrum is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tAtmSpectrum = copy.deepcopy(tAtmSpectrum)
        except Exception as exc:
            raise ValueError("Invalid tAtmSpectrum : " + str(exc))

    # ===> Attribute tRecSpectrum

    _tRecSpectrum = None  # this is a 2D list of Temperature

    def getTRecSpectrum(self):
        """
        Get tRecSpectrum.
        return tRecSpectrum as Temperature []  []
        """

        return copy.deepcopy(self._tRecSpectrum)

    def setTRecSpectrum(self, tRecSpectrum):
        """
        Set tRecSpectrum with the specified Temperature []  []  value.
        tRecSpectrum The Temperature []  []  value to which tRecSpectrum is to be set.
        The value of tRecSpectrum can be anything allowed by the Temperature []  []  constructor.

        """

        # value must be a list
        if not isinstance(tRecSpectrum, list):
            raise ValueError("The value of tRecSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tRecSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of tRecSpectrum is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(tRecSpectrum, Temperature):
                raise ValueError(
                    "type of the first value in tRecSpectrum is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tRecSpectrum = copy.deepcopy(tRecSpectrum)
        except Exception as exc:
            raise ValueError("Invalid tRecSpectrum : " + str(exc))

    # ===> Attribute tSysSpectrum

    _tSysSpectrum = None  # this is a 2D list of Temperature

    def getTSysSpectrum(self):
        """
        Get tSysSpectrum.
        return tSysSpectrum as Temperature []  []
        """

        return copy.deepcopy(self._tSysSpectrum)

    def setTSysSpectrum(self, tSysSpectrum):
        """
        Set tSysSpectrum with the specified Temperature []  []  value.
        tSysSpectrum The Temperature []  []  value to which tSysSpectrum is to be set.
        The value of tSysSpectrum can be anything allowed by the Temperature []  []  constructor.

        """

        # value must be a list
        if not isinstance(tSysSpectrum, list):
            raise ValueError("The value of tSysSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tSysSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of tSysSpectrum is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(tSysSpectrum, Temperature):
                raise ValueError(
                    "type of the first value in tSysSpectrum is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tSysSpectrum = copy.deepcopy(tSysSpectrum)
        except Exception as exc:
            raise ValueError("Invalid tSysSpectrum : " + str(exc))

    # ===> Attribute tauSpectrum

    _tauSpectrum = None  # this is a 2D list of float

    def getTauSpectrum(self):
        """
        Get tauSpectrum.
        return tauSpectrum as float []  []
        """

        return copy.deepcopy(self._tauSpectrum)

    def setTauSpectrum(self, tauSpectrum):
        """
        Set tauSpectrum with the specified float []  []  value.
        tauSpectrum The float []  []  value to which tauSpectrum is to be set.


        """

        # value must be a list
        if not isinstance(tauSpectrum, list):
            raise ValueError("The value of tauSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tauSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of tauSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(tauSpectrum, float):
                raise ValueError(
                    "type of the first value in tauSpectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tauSpectrum = copy.deepcopy(tauSpectrum)
        except Exception as exc:
            raise ValueError("Invalid tauSpectrum : " + str(exc))

    # ===> Attribute tAtm

    _tAtm = None  # this is a 1D list of Temperature

    def getTAtm(self):
        """
        Get tAtm.
        return tAtm as Temperature []
        """

        return copy.deepcopy(self._tAtm)

    def setTAtm(self, tAtm):
        """
        Set tAtm with the specified Temperature []  value.
        tAtm The Temperature []  value to which tAtm is to be set.
        The value of tAtm can be anything allowed by the Temperature []  constructor.

        """

        # value must be a list
        if not isinstance(tAtm, list):
            raise ValueError("The value of tAtm must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tAtm)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of tAtm is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(tAtm, Temperature):
                raise ValueError(
                    "type of the first value in tAtm is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tAtm = copy.deepcopy(tAtm)
        except Exception as exc:
            raise ValueError("Invalid tAtm : " + str(exc))

    # ===> Attribute tRec

    _tRec = None  # this is a 1D list of Temperature

    def getTRec(self):
        """
        Get tRec.
        return tRec as Temperature []
        """

        return copy.deepcopy(self._tRec)

    def setTRec(self, tRec):
        """
        Set tRec with the specified Temperature []  value.
        tRec The Temperature []  value to which tRec is to be set.
        The value of tRec can be anything allowed by the Temperature []  constructor.

        """

        # value must be a list
        if not isinstance(tRec, list):
            raise ValueError("The value of tRec must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tRec)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of tRec is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(tRec, Temperature):
                raise ValueError(
                    "type of the first value in tRec is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tRec = copy.deepcopy(tRec)
        except Exception as exc:
            raise ValueError("Invalid tRec : " + str(exc))

    # ===> Attribute tSys

    _tSys = None  # this is a 1D list of Temperature

    def getTSys(self):
        """
        Get tSys.
        return tSys as Temperature []
        """

        return copy.deepcopy(self._tSys)

    def setTSys(self, tSys):
        """
        Set tSys with the specified Temperature []  value.
        tSys The Temperature []  value to which tSys is to be set.
        The value of tSys can be anything allowed by the Temperature []  constructor.

        """

        # value must be a list
        if not isinstance(tSys, list):
            raise ValueError("The value of tSys must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tSys)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of tSys is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not Parser.checkListType(tSys, Temperature):
                raise ValueError(
                    "type of the first value in tSys is not Temperature as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tSys = copy.deepcopy(tSys)
        except Exception as exc:
            raise ValueError("Invalid tSys : " + str(exc))

    # ===> Attribute tau

    _tau = None  # this is a 1D list of float

    def getTau(self):
        """
        Get tau.
        return tau as float []
        """

        return copy.deepcopy(self._tau)

    def setTau(self, tau):
        """
        Set tau with the specified float []  value.
        tau The float []  value to which tau is to be set.


        """

        # value must be a list
        if not isinstance(tau, list):
            raise ValueError("The value of tau must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(tau)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of tau is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(tau, float):
                raise ValueError(
                    "type of the first value in tau is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._tau = copy.deepcopy(tau)
        except Exception as exc:
            raise ValueError("Invalid tau : " + str(exc))

    # ===> Attribute water

    _water = None  # this is a 1D list of Length

    def getWater(self):
        """
        Get water.
        return water as Length []
        """

        return copy.deepcopy(self._water)

    def setWater(self, water):
        """
        Set water with the specified Length []  value.
        water The Length []  value to which water is to be set.
        The value of water can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(water, list):
            raise ValueError("The value of water must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(water)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of water is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(water, Length):
                raise ValueError(
                    "type of the first value in water is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._water = copy.deepcopy(water)
        except Exception as exc:
            raise ValueError("Invalid water : " + str(exc))

    # ===> Attribute waterError

    _waterError = None  # this is a 1D list of Length

    def getWaterError(self):
        """
        Get waterError.
        return waterError as Length []
        """

        return copy.deepcopy(self._waterError)

    def setWaterError(self, waterError):
        """
        Set waterError with the specified Length []  value.
        waterError The Length []  value to which waterError is to be set.
        The value of waterError can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(waterError, list):
            raise ValueError("The value of waterError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(waterError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of waterError is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not Parser.checkListType(waterError, Length):
                raise ValueError(
                    "type of the first value in waterError is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._waterError = copy.deepcopy(waterError)
        except Exception as exc:
            raise ValueError("Invalid waterError : " + str(exc))

    # ===> Attribute alphaSpectrum, which is optional
    _alphaSpectrumExists = False

    _alphaSpectrum = None  # this is a 2D list of float

    def isAlphaSpectrumExists(self):
        """
        The attribute alphaSpectrum is optional. Return True if this attribute exists.
        return True if and only if the alphaSpectrum attribute exists.
        """
        return self._alphaSpectrumExists

    def getAlphaSpectrum(self):
        """
        Get alphaSpectrum, which is optional.
        return alphaSpectrum as float []  []
        raises ValueError If alphaSpectrum does not exist.
        """
        if not self._alphaSpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + alphaSpectrum
                + " attribute in table CalAtmosphere does not exist!"
            )

        return copy.deepcopy(self._alphaSpectrum)

    def setAlphaSpectrum(self, alphaSpectrum):
        """
        Set alphaSpectrum with the specified float []  []  value.
        alphaSpectrum The float []  []  value to which alphaSpectrum is to be set.


        """

        # value must be a list
        if not isinstance(alphaSpectrum, list):
            raise ValueError("The value of alphaSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(alphaSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of alphaSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(alphaSpectrum, float):
                raise ValueError(
                    "type of the first value in alphaSpectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._alphaSpectrum = copy.deepcopy(alphaSpectrum)
        except Exception as exc:
            raise ValueError("Invalid alphaSpectrum : " + str(exc))

        self._alphaSpectrumExists = True

    def clearAlphaSpectrum(self):
        """
        Mark alphaSpectrum, which is an optional field, as non-existent.
        """
        self._alphaSpectrumExists = False

    # ===> Attribute forwardEfficiency, which is optional
    _forwardEfficiencyExists = False

    _forwardEfficiency = None  # this is a 1D list of float

    def isForwardEfficiencyExists(self):
        """
        The attribute forwardEfficiency is optional. Return True if this attribute exists.
        return True if and only if the forwardEfficiency attribute exists.
        """
        return self._forwardEfficiencyExists

    def getForwardEfficiency(self):
        """
        Get forwardEfficiency, which is optional.
        return forwardEfficiency as float []
        raises ValueError If forwardEfficiency does not exist.
        """
        if not self._forwardEfficiencyExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + forwardEfficiency
                + " attribute in table CalAtmosphere does not exist!"
            )

        return copy.deepcopy(self._forwardEfficiency)

    def setForwardEfficiency(self, forwardEfficiency):
        """
        Set forwardEfficiency with the specified float []  value.
        forwardEfficiency The float []  value to which forwardEfficiency is to be set.


        """

        # value must be a list
        if not isinstance(forwardEfficiency, list):
            raise ValueError("The value of forwardEfficiency must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(forwardEfficiency)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of forwardEfficiency is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(forwardEfficiency, float):
                raise ValueError(
                    "type of the first value in forwardEfficiency is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._forwardEfficiency = copy.deepcopy(forwardEfficiency)
        except Exception as exc:
            raise ValueError("Invalid forwardEfficiency : " + str(exc))

        self._forwardEfficiencyExists = True

    def clearForwardEfficiency(self):
        """
        Mark forwardEfficiency, which is an optional field, as non-existent.
        """
        self._forwardEfficiencyExists = False

    # ===> Attribute forwardEfficiencyError, which is optional
    _forwardEfficiencyErrorExists = False

    _forwardEfficiencyError = None  # this is a 1D list of float

    def isForwardEfficiencyErrorExists(self):
        """
        The attribute forwardEfficiencyError is optional. Return True if this attribute exists.
        return True if and only if the forwardEfficiencyError attribute exists.
        """
        return self._forwardEfficiencyErrorExists

    def getForwardEfficiencyError(self):
        """
        Get forwardEfficiencyError, which is optional.
        return forwardEfficiencyError as float []
        raises ValueError If forwardEfficiencyError does not exist.
        """
        if not self._forwardEfficiencyErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + forwardEfficiencyError
                + " attribute in table CalAtmosphere does not exist!"
            )

        return copy.deepcopy(self._forwardEfficiencyError)

    def setForwardEfficiencyError(self, forwardEfficiencyError):
        """
        Set forwardEfficiencyError with the specified float []  value.
        forwardEfficiencyError The float []  value to which forwardEfficiencyError is to be set.


        """

        # value must be a list
        if not isinstance(forwardEfficiencyError, list):
            raise ValueError("The value of forwardEfficiencyError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(forwardEfficiencyError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of forwardEfficiencyError is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(forwardEfficiencyError, float):
                raise ValueError(
                    "type of the first value in forwardEfficiencyError is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._forwardEfficiencyError = copy.deepcopy(forwardEfficiencyError)
        except Exception as exc:
            raise ValueError("Invalid forwardEfficiencyError : " + str(exc))

        self._forwardEfficiencyErrorExists = True

    def clearForwardEfficiencyError(self):
        """
        Mark forwardEfficiencyError, which is an optional field, as non-existent.
        """
        self._forwardEfficiencyErrorExists = False

    # ===> Attribute sbGain, which is optional
    _sbGainExists = False

    _sbGain = None  # this is a 1D list of float

    def isSbGainExists(self):
        """
        The attribute sbGain is optional. Return True if this attribute exists.
        return True if and only if the sbGain attribute exists.
        """
        return self._sbGainExists

    def getSbGain(self):
        """
        Get sbGain, which is optional.
        return sbGain as float []
        raises ValueError If sbGain does not exist.
        """
        if not self._sbGainExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sbGain
                + " attribute in table CalAtmosphere does not exist!"
            )

        return copy.deepcopy(self._sbGain)

    def setSbGain(self, sbGain):
        """
        Set sbGain with the specified float []  value.
        sbGain The float []  value to which sbGain is to be set.


        """

        # value must be a list
        if not isinstance(sbGain, list):
            raise ValueError("The value of sbGain must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(sbGain)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of sbGain is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(sbGain, float):
                raise ValueError(
                    "type of the first value in sbGain is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._sbGain = copy.deepcopy(sbGain)
        except Exception as exc:
            raise ValueError("Invalid sbGain : " + str(exc))

        self._sbGainExists = True

    def clearSbGain(self):
        """
        Mark sbGain, which is an optional field, as non-existent.
        """
        self._sbGainExists = False

    # ===> Attribute sbGainError, which is optional
    _sbGainErrorExists = False

    _sbGainError = None  # this is a 1D list of float

    def isSbGainErrorExists(self):
        """
        The attribute sbGainError is optional. Return True if this attribute exists.
        return True if and only if the sbGainError attribute exists.
        """
        return self._sbGainErrorExists

    def getSbGainError(self):
        """
        Get sbGainError, which is optional.
        return sbGainError as float []
        raises ValueError If sbGainError does not exist.
        """
        if not self._sbGainErrorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sbGainError
                + " attribute in table CalAtmosphere does not exist!"
            )

        return copy.deepcopy(self._sbGainError)

    def setSbGainError(self, sbGainError):
        """
        Set sbGainError with the specified float []  value.
        sbGainError The float []  value to which sbGainError is to be set.


        """

        # value must be a list
        if not isinstance(sbGainError, list):
            raise ValueError("The value of sbGainError must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(sbGainError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of sbGainError is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(sbGainError, float):
                raise ValueError(
                    "type of the first value in sbGainError is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._sbGainError = copy.deepcopy(sbGainError)
        except Exception as exc:
            raise ValueError("Invalid sbGainError : " + str(exc))

        self._sbGainErrorExists = True

    def clearSbGainError(self):
        """
        Mark sbGainError, which is an optional field, as non-existent.
        """
        self._sbGainErrorExists = False

    # ===> Attribute sbGainSpectrum, which is optional
    _sbGainSpectrumExists = False

    _sbGainSpectrum = None  # this is a 2D list of float

    def isSbGainSpectrumExists(self):
        """
        The attribute sbGainSpectrum is optional. Return True if this attribute exists.
        return True if and only if the sbGainSpectrum attribute exists.
        """
        return self._sbGainSpectrumExists

    def getSbGainSpectrum(self):
        """
        Get sbGainSpectrum, which is optional.
        return sbGainSpectrum as float []  []
        raises ValueError If sbGainSpectrum does not exist.
        """
        if not self._sbGainSpectrumExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sbGainSpectrum
                + " attribute in table CalAtmosphere does not exist!"
            )

        return copy.deepcopy(self._sbGainSpectrum)

    def setSbGainSpectrum(self, sbGainSpectrum):
        """
        Set sbGainSpectrum with the specified float []  []  value.
        sbGainSpectrum The float []  []  value to which sbGainSpectrum is to be set.


        """

        # value must be a list
        if not isinstance(sbGainSpectrum, list):
            raise ValueError("The value of sbGainSpectrum must be a list")
        # check the shape
        try:
            listDims = Parser.getListDims(sbGainSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of sbGainSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not Parser.checkListType(sbGainSpectrum, float):
                raise ValueError(
                    "type of the first value in sbGainSpectrum is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._sbGainSpectrum = copy.deepcopy(sbGainSpectrum)
        except Exception as exc:
            raise ValueError("Invalid sbGainSpectrum : " + str(exc))

        self._sbGainSpectrumExists = True

    def clearSbGainSpectrum(self):
        """
        Mark sbGainSpectrum, which is an optional field, as non-existent.
        """
        self._sbGainSpectrumExists = False

    # Extrinsic Table Attributes

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

    # ===> Attribute calReductionId

    _calReductionId = Tag()

    def getCalReductionId(self):
        """
        Get calReductionId.
        return calReductionId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._calReductionId)

    def setCalReductionId(self, calReductionId):
        """
        Set calReductionId with the specified Tag value.
        calReductionId The Tag value to which calReductionId is to be set.
        The value of calReductionId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the calReductionId field, which is part of the key, after this row has been added to this table."
            )

        self._calReductionId = Tag(calReductionId)

    # Links

    def getCalReductionUsingCalReductionId(self):
        """
        Returns the row in the CalReduction table having CalReduction.calReductionId == calReductionId

        """

        return (
            self._table.getContainer()
            .getCalReduction()
            .getRowByKey(self._calReductionId)
        )

    def getCalDataUsingCalDataId(self):
        """
        Returns the row in the CalData table having CalData.calDataId == calDataId

        """

        return self._table.getContainer().getCalData().getRowByKey(self._calDataId)

    # comparison methods

    def compareNoAutoInc(
        self,
        antennaName,
        receiverBand,
        basebandName,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numFreq,
        numLoad,
        numReceptor,
        forwardEffSpectrum,
        frequencyRange,
        groundPressure,
        groundRelHumidity,
        frequencySpectrum,
        groundTemperature,
        polarizationTypes,
        powerSkySpectrum,
        powerLoadSpectrum,
        syscalType,
        tAtmSpectrum,
        tRecSpectrum,
        tSysSpectrum,
        tauSpectrum,
        tAtm,
        tRec,
        tSys,
        tau,
        water,
        waterError,
    ):
        """
        Compare each attribute except the autoincrementable one of this CalAtmosphereRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # antennaName is a str, compare using the == operator.
        if not (self._antennaName == antennaName):
            return False

        # receiverBand is a ReceiverBand, compare using the == operator on the getValue() output
        if not (self._receiverBand.getValue() == receiverBand.getValue()):
            return False

        # basebandName is a BasebandName, compare using the == operator on the getValue() output
        if not (self._basebandName.getValue() == basebandName.getValue()):
            return False

        # calDataId is a Tag, compare using the equals method.
        if not self._calDataId.equals(calDataId):
            return False

        # calReductionId is a Tag, compare using the equals method.
        if not self._calReductionId.equals(calReductionId):
            return False

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # numFreq is a int, compare using the == operator.
        if not (self._numFreq == numFreq):
            return False

        # numLoad is a int, compare using the == operator.
        if not (self._numLoad == numLoad):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 2D arrays (lists)
        if forwardEffSpectrum is not None:
            if self._forwardEffSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            forwardEffSpectrum_dims = Parser.getListDims(forwardEffSpectrum)
            this_forwardEffSpectrum_dims = Parser.getListDims(self._forwardEffSpectrum)
            if forwardEffSpectrum_dims != this_forwardEffSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(forwardEffSpectrum_dims[0]):
                for j in range(forwardEffSpectrum_dims[0]):

                    # forwardEffSpectrum is an array of float, compare using == operator.
                    if not (self._forwardEffSpectrum[i][j] == forwardEffSpectrum[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._frequencyRange) != len(frequencyRange):
            return False
        for indx in range(len(frequencyRange)):

            # frequencyRange is a list of Frequency, compare using the almostEquals method.
            if not self._frequencyRange[indx].almostEquals(
                frequencyRange[indx], self.getTable().getFrequencyRangeEqTolerance()
            ):
                return False

        # groundPressure is a Pressure, compare using the almostEquals method.
        if not self._groundPressure.almostEquals(
            groundPressure, self.getTable().getGroundPressureEqTolerance()
        ):
            return False

        # groundRelHumidity is a Humidity, compare using the almostEquals method.
        if not self._groundRelHumidity.almostEquals(
            groundRelHumidity, self.getTable().getGroundRelHumidityEqTolerance()
        ):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._frequencySpectrum) != len(frequencySpectrum):
            return False
        for indx in range(len(frequencySpectrum)):

            # frequencySpectrum is a list of Frequency, compare using the almostEquals method.
            if not self._frequencySpectrum[indx].almostEquals(
                frequencySpectrum[indx],
                self.getTable().getFrequencySpectrumEqTolerance(),
            ):
                return False

        # groundTemperature is a Temperature, compare using the almostEquals method.
        if not self._groundTemperature.almostEquals(
            groundTemperature, self.getTable().getGroundTemperatureEqTolerance()
        ):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationTypes) != len(polarizationTypes):
            return False
        for indx in range(len(polarizationTypes)):

            # polarizationTypes is a list of PolarizationType, compare using == operator.
            if not (self._polarizationTypes[indx] == polarizationTypes[indx]):
                return False

        # We compare two 2D arrays (lists)
        if powerSkySpectrum is not None:
            if self._powerSkySpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            powerSkySpectrum_dims = Parser.getListDims(powerSkySpectrum)
            this_powerSkySpectrum_dims = Parser.getListDims(self._powerSkySpectrum)
            if powerSkySpectrum_dims != this_powerSkySpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(powerSkySpectrum_dims[0]):
                for j in range(powerSkySpectrum_dims[0]):

                    # powerSkySpectrum is an array of float, compare using == operator.
                    if not (self._powerSkySpectrum[i][j] == powerSkySpectrum[i][j]):
                        return False

        # We compare two 3D arrays.
        # Compare firstly their dimensions and then their values.
        if powerLoadSpectrum is not None:
            if self._powerLoadSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            powerLoadSpectrum_dims = Parser.getListDims(powerLoadSpectrum)
            this_powerLoadSpectrum_dims = Parser.getListDims(self._powerLoadSpectrum)
            if powerLoadSpectrum_dims != this_powerLoadSpectrum_dims:
                return False
            # assumes they are both 3D arrays, the internal one should be
            for i in range(powerLoadSpectrum_dims[0]):
                for j in range(powerLoadSpectrum_dims[0]):
                    for k in range(powerLoadSpectrum_dims[0]):

                        # powerLoadSpectrum is an array of float, compare using == operator.
                        if not (
                            self._powerLoadSpectrum[i][j][k]
                            == powerLoadSpectrum[i][j][k]
                        ):
                            return False

        # syscalType is a SyscalMethod, compare using the == operator on the getValue() output
        if not (self._syscalType.getValue() == syscalType.getValue()):
            return False

        # We compare two 2D arrays (lists)
        if tAtmSpectrum is not None:
            if self._tAtmSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tAtmSpectrum_dims = Parser.getListDims(tAtmSpectrum)
            this_tAtmSpectrum_dims = Parser.getListDims(self._tAtmSpectrum)
            if tAtmSpectrum_dims != this_tAtmSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tAtmSpectrum_dims[0]):
                for j in range(tAtmSpectrum_dims[0]):

                    # tAtmSpectrum is a Temperature, compare using the almostEquals method.
                    if not (
                        self._tAtmSpectrum[i][j].almostEquals(
                            tAtmSpectrum[i][j],
                            this.getTable().getTAtmSpectrumEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists)
        if tRecSpectrum is not None:
            if self._tRecSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tRecSpectrum_dims = Parser.getListDims(tRecSpectrum)
            this_tRecSpectrum_dims = Parser.getListDims(self._tRecSpectrum)
            if tRecSpectrum_dims != this_tRecSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tRecSpectrum_dims[0]):
                for j in range(tRecSpectrum_dims[0]):

                    # tRecSpectrum is a Temperature, compare using the almostEquals method.
                    if not (
                        self._tRecSpectrum[i][j].almostEquals(
                            tRecSpectrum[i][j],
                            this.getTable().getTRecSpectrumEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists)
        if tSysSpectrum is not None:
            if self._tSysSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tSysSpectrum_dims = Parser.getListDims(tSysSpectrum)
            this_tSysSpectrum_dims = Parser.getListDims(self._tSysSpectrum)
            if tSysSpectrum_dims != this_tSysSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tSysSpectrum_dims[0]):
                for j in range(tSysSpectrum_dims[0]):

                    # tSysSpectrum is a Temperature, compare using the almostEquals method.
                    if not (
                        self._tSysSpectrum[i][j].almostEquals(
                            tSysSpectrum[i][j],
                            this.getTable().getTSysSpectrumEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists)
        if tauSpectrum is not None:
            if self._tauSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tauSpectrum_dims = Parser.getListDims(tauSpectrum)
            this_tauSpectrum_dims = Parser.getListDims(self._tauSpectrum)
            if tauSpectrum_dims != this_tauSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tauSpectrum_dims[0]):
                for j in range(tauSpectrum_dims[0]):

                    # tauSpectrum is an array of float, compare using == operator.
                    if not (self._tauSpectrum[i][j] == tauSpectrum[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._tAtm) != len(tAtm):
            return False
        for indx in range(len(tAtm)):

            # tAtm is a list of Temperature, compare using the almostEquals method.
            if not self._tAtm[indx].almostEquals(
                tAtm[indx], self.getTable().getTAtmEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._tRec) != len(tRec):
            return False
        for indx in range(len(tRec)):

            # tRec is a list of Temperature, compare using the almostEquals method.
            if not self._tRec[indx].almostEquals(
                tRec[indx], self.getTable().getTRecEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._tSys) != len(tSys):
            return False
        for indx in range(len(tSys)):

            # tSys is a list of Temperature, compare using the almostEquals method.
            if not self._tSys[indx].almostEquals(
                tSys[indx], self.getTable().getTSysEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._tau) != len(tau):
            return False
        for indx in range(len(tau)):

            # tau is a list of float, compare using == operator.
            if not (self._tau[indx] == tau[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._water) != len(water):
            return False
        for indx in range(len(water)):

            # water is a list of Length, compare using the almostEquals method.
            if not self._water[indx].almostEquals(
                water[indx], self.getTable().getWaterEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._waterError) != len(waterError):
            return False
        for indx in range(len(waterError)):

            # waterError is a list of Length, compare using the almostEquals method.
            if not self._waterError[indx].almostEquals(
                waterError[indx], self.getTable().getWaterErrorEqTolerance()
            ):
                return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getStartValidTime(),
            otherRow.getEndValidTime(),
            otherRow.getNumFreq(),
            otherRow.getNumLoad(),
            otherRow.getNumReceptor(),
            otherRow.getForwardEffSpectrum(),
            otherRow.getFrequencyRange(),
            otherRow.getGroundPressure(),
            otherRow.getGroundRelHumidity(),
            otherRow.getFrequencySpectrum(),
            otherRow.getGroundTemperature(),
            otherRow.getPolarizationTypes(),
            otherRow.getPowerSkySpectrum(),
            otherRow.getPowerLoadSpectrum(),
            otherRow.getSyscalType(),
            otherRow.getTAtmSpectrum(),
            otherRow.getTRecSpectrum(),
            otherRow.getTSysSpectrum(),
            otherRow.getTauSpectrum(),
            otherRow.getTAtm(),
            otherRow.getTRec(),
            otherRow.getTSys(),
            otherRow.getTau(),
            otherRow.getWater(),
            otherRow.getWaterError(),
        )

    def compareRequiredValue(
        self,
        startValidTime,
        endValidTime,
        numFreq,
        numLoad,
        numReceptor,
        forwardEffSpectrum,
        frequencyRange,
        groundPressure,
        groundRelHumidity,
        frequencySpectrum,
        groundTemperature,
        polarizationTypes,
        powerSkySpectrum,
        powerLoadSpectrum,
        syscalType,
        tAtmSpectrum,
        tRecSpectrum,
        tSysSpectrum,
        tauSpectrum,
        tAtm,
        tRec,
        tSys,
        tau,
        water,
        waterError,
    ):

        # startValidTime is a ArrayTime, compare using the equals method.
        if not self._startValidTime.equals(startValidTime):
            return False

        # endValidTime is a ArrayTime, compare using the equals method.
        if not self._endValidTime.equals(endValidTime):
            return False

        # numFreq is a int, compare using the == operator.
        if not (self._numFreq == numFreq):
            return False

        # numLoad is a int, compare using the == operator.
        if not (self._numLoad == numLoad):
            return False

        # numReceptor is a int, compare using the == operator.
        if not (self._numReceptor == numReceptor):
            return False

        # We compare two 2D arrays (lists)
        if forwardEffSpectrum is not None:
            if self._forwardEffSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            forwardEffSpectrum_dims = Parser.getListDims(forwardEffSpectrum)
            this_forwardEffSpectrum_dims = Parser.getListDims(self._forwardEffSpectrum)
            if forwardEffSpectrum_dims != this_forwardEffSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(forwardEffSpectrum_dims[0]):
                for j in range(forwardEffSpectrum_dims[0]):

                    # forwardEffSpectrum is an array of float, compare using == operator.
                    if not (self._forwardEffSpectrum[i][j] == forwardEffSpectrum[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._frequencyRange) != len(frequencyRange):
            return False
        for indx in range(len(frequencyRange)):

            # frequencyRange is a list of Frequency, compare using the almostEquals method.
            if not self._frequencyRange[indx].almostEquals(
                frequencyRange[indx], self.getTable().getFrequencyRangeEqTolerance()
            ):
                return False

        # groundPressure is a Pressure, compare using the almostEquals method.
        if not self._groundPressure.almostEquals(
            groundPressure, self.getTable().getGroundPressureEqTolerance()
        ):
            return False

        # groundRelHumidity is a Humidity, compare using the almostEquals method.
        if not self._groundRelHumidity.almostEquals(
            groundRelHumidity, self.getTable().getGroundRelHumidityEqTolerance()
        ):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._frequencySpectrum) != len(frequencySpectrum):
            return False
        for indx in range(len(frequencySpectrum)):

            # frequencySpectrum is a list of Frequency, compare using the almostEquals method.
            if not self._frequencySpectrum[indx].almostEquals(
                frequencySpectrum[indx],
                self.getTable().getFrequencySpectrumEqTolerance(),
            ):
                return False

        # groundTemperature is a Temperature, compare using the almostEquals method.
        if not self._groundTemperature.almostEquals(
            groundTemperature, self.getTable().getGroundTemperatureEqTolerance()
        ):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._polarizationTypes) != len(polarizationTypes):
            return False
        for indx in range(len(polarizationTypes)):

            # polarizationTypes is a list of PolarizationType, compare using == operator.
            if not (self._polarizationTypes[indx] == polarizationTypes[indx]):
                return False

        # We compare two 2D arrays (lists)
        if powerSkySpectrum is not None:
            if self._powerSkySpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            powerSkySpectrum_dims = Parser.getListDims(powerSkySpectrum)
            this_powerSkySpectrum_dims = Parser.getListDims(self._powerSkySpectrum)
            if powerSkySpectrum_dims != this_powerSkySpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(powerSkySpectrum_dims[0]):
                for j in range(powerSkySpectrum_dims[0]):

                    # powerSkySpectrum is an array of float, compare using == operator.
                    if not (self._powerSkySpectrum[i][j] == powerSkySpectrum[i][j]):
                        return False

        # We compare two 3D arrays.
        # Compare firstly their dimensions and then their values.
        if powerLoadSpectrum is not None:
            if self._powerLoadSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            powerLoadSpectrum_dims = Parser.getListDims(powerLoadSpectrum)
            this_powerLoadSpectrum_dims = Parser.getListDims(self._powerLoadSpectrum)
            if powerLoadSpectrum_dims != this_powerLoadSpectrum_dims:
                return False
            # assumes they are both 3D arrays, the internal one should be
            for i in range(powerLoadSpectrum_dims[0]):
                for j in range(powerLoadSpectrum_dims[0]):
                    for k in range(powerLoadSpectrum_dims[0]):

                        # powerLoadSpectrum is an array of float, compare using == operator.
                        if not (
                            self._powerLoadSpectrum[i][j][k]
                            == powerLoadSpectrum[i][j][k]
                        ):
                            return False

        # syscalType is a SyscalMethod, compare using the == operator on the getValue() output
        if not (self._syscalType.getValue() == syscalType.getValue()):
            return False

        # We compare two 2D arrays (lists)
        if tAtmSpectrum is not None:
            if self._tAtmSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tAtmSpectrum_dims = Parser.getListDims(tAtmSpectrum)
            this_tAtmSpectrum_dims = Parser.getListDims(self._tAtmSpectrum)
            if tAtmSpectrum_dims != this_tAtmSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tAtmSpectrum_dims[0]):
                for j in range(tAtmSpectrum_dims[0]):

                    # tAtmSpectrum is a Temperature, compare using the almostEquals method.
                    if not (
                        self._tAtmSpectrum[i][j].almostEquals(
                            tAtmSpectrum[i][j],
                            this.getTable().getTAtmSpectrumEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists)
        if tRecSpectrum is not None:
            if self._tRecSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tRecSpectrum_dims = Parser.getListDims(tRecSpectrum)
            this_tRecSpectrum_dims = Parser.getListDims(self._tRecSpectrum)
            if tRecSpectrum_dims != this_tRecSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tRecSpectrum_dims[0]):
                for j in range(tRecSpectrum_dims[0]):

                    # tRecSpectrum is a Temperature, compare using the almostEquals method.
                    if not (
                        self._tRecSpectrum[i][j].almostEquals(
                            tRecSpectrum[i][j],
                            this.getTable().getTRecSpectrumEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists)
        if tSysSpectrum is not None:
            if self._tSysSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tSysSpectrum_dims = Parser.getListDims(tSysSpectrum)
            this_tSysSpectrum_dims = Parser.getListDims(self._tSysSpectrum)
            if tSysSpectrum_dims != this_tSysSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tSysSpectrum_dims[0]):
                for j in range(tSysSpectrum_dims[0]):

                    # tSysSpectrum is a Temperature, compare using the almostEquals method.
                    if not (
                        self._tSysSpectrum[i][j].almostEquals(
                            tSysSpectrum[i][j],
                            this.getTable().getTSysSpectrumEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists)
        if tauSpectrum is not None:
            if self._tauSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tauSpectrum_dims = Parser.getListDims(tauSpectrum)
            this_tauSpectrum_dims = Parser.getListDims(self._tauSpectrum)
            if tauSpectrum_dims != this_tauSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tauSpectrum_dims[0]):
                for j in range(tauSpectrum_dims[0]):

                    # tauSpectrum is an array of float, compare using == operator.
                    if not (self._tauSpectrum[i][j] == tauSpectrum[i][j]):
                        return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._tAtm) != len(tAtm):
            return False
        for indx in range(len(tAtm)):

            # tAtm is a list of Temperature, compare using the almostEquals method.
            if not self._tAtm[indx].almostEquals(
                tAtm[indx], self.getTable().getTAtmEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._tRec) != len(tRec):
            return False
        for indx in range(len(tRec)):

            # tRec is a list of Temperature, compare using the almostEquals method.
            if not self._tRec[indx].almostEquals(
                tRec[indx], self.getTable().getTRecEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._tSys) != len(tSys):
            return False
        for indx in range(len(tSys)):

            # tSys is a list of Temperature, compare using the almostEquals method.
            if not self._tSys[indx].almostEquals(
                tSys[indx], self.getTable().getTSysEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._tau) != len(tau):
            return False
        for indx in range(len(tau)):

            # tau is a list of float, compare using == operator.
            if not (self._tau[indx] == tau[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._water) != len(water):
            return False
        for indx in range(len(water)):

            # water is a list of Length, compare using the almostEquals method.
            if not self._water[indx].almostEquals(
                water[indx], self.getTable().getWaterEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._waterError) != len(waterError):
            return False
        for indx in range(len(waterError)):

            # waterError is a list of Length, compare using the almostEquals method.
            if not self._waterError[indx].almostEquals(
                waterError[indx], self.getTable().getWaterErrorEqTolerance()
            ):
                return False

        return True
