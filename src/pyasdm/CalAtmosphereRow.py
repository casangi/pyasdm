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

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


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
            raise ValueError("table must be a CalAtmosphereTable")

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
                raise ValueError("row must be a CalAtmosphereRow")

            # copy constructor

            self._antennaName = row._antennaName

            # We force the attribute of the result to be not None.
            if row._receiverBand is None:
                self._receiverBand = ReceiverBand.from_int(0)
            else:
                self._receiverBand = ReceiverBand(row._receiverBand)

            # We force the attribute of the result to be not None.
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
                self._alphaSpectrum = copy.deepcopy(row._alphaSpectrum)

                self._alphaSpectrumExists = True

            # by default set systematically forwardEfficiency's value to something not None

            if row._forwardEfficiencyExists:

                # forwardEfficiency is a list, make a deep copy
                self._forwardEfficiency = copy.deepcopy(row._forwardEfficiency)

                self._forwardEfficiencyExists = True

            # by default set systematically forwardEfficiencyError's value to something not None

            if row._forwardEfficiencyErrorExists:

                # forwardEfficiencyError is a list, make a deep copy
                self._forwardEfficiencyError = copy.deepcopy(
                    row._forwardEfficiencyError
                )

                self._forwardEfficiencyErrorExists = True

            # by default set systematically sbGain's value to something not None

            if row._sbGainExists:

                # sbGain is a list, make a deep copy
                self._sbGain = copy.deepcopy(row._sbGain)

                self._sbGainExists = True

            # by default set systematically sbGainError's value to something not None

            if row._sbGainErrorExists:

                # sbGainError is a list, make a deep copy
                self._sbGainError = copy.deepcopy(row._sbGainError)

                self._sbGainErrorExists = True

            # by default set systematically sbGainSpectrum's value to something not None

            if row._sbGainSpectrumExists:

                # sbGainSpectrum is a list, make a deep copy
                self._sbGainSpectrum = copy.deepcopy(row._sbGainSpectrum)

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

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        eos.writeStr(self._antennaName)

        eos.writeString(str(self._receiverBand))

        eos.writeString(str(self._basebandName))

        self._calDataId.toBin(eos)

        self._calReductionId.toBin(eos)

        self._startValidTime.toBin(eos)

        self._endValidTime.toBin(eos)

        eos.writeInt(self._numFreq)

        eos.writeInt(self._numLoad)

        eos.writeInt(self._numReceptor)

        # null array case, unsure if this is possible but this should work
        if self._forwardEffSpectrum is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            forwardEffSpectrum_dims = pyasdm.utils.getListDims(self._forwardEffSpectrum)
        # assumes it really is 2D
        eos.writeInt(forwardEffSpectrum_dims[0])
        eos.writeInt(forwardEffSpectrum_dims[1])
        for i in range(forwardEffSpectrum_dims[0]):
            for j in range(forwardEffSpectrum_dims[1]):
                eos.writeFloat(self._forwardEffSpectrum[i][j])

        Frequency.listToBin(self._frequencyRange, eos)

        self._groundPressure.toBin(eos)

        self._groundRelHumidity.toBin(eos)

        Frequency.listToBin(self._frequencySpectrum, eos)

        self._groundTemperature.toBin(eos)

        eos.writeInt(len(self._polarizationTypes))
        for i in range(len(self._polarizationTypes)):

            eos.writeString(str(self._polarizationTypes[i]))

        # null array case, unsure if this is possible but this should work
        if self._powerSkySpectrum is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            powerSkySpectrum_dims = pyasdm.utils.getListDims(self._powerSkySpectrum)
        # assumes it really is 2D
        eos.writeInt(powerSkySpectrum_dims[0])
        eos.writeInt(powerSkySpectrum_dims[1])
        for i in range(powerSkySpectrum_dims[0]):
            for j in range(powerSkySpectrum_dims[1]):
                eos.writeFloat(self._powerSkySpectrum[i][j])

        # null array case, unsure if this is possible but this should work
        if self._powerLoadSpectrum is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            powerLoadSpectrum_dims = pyasdm.utils.getListDims(self._powerLoadSpectrum)
        # assumes it really is 3D
        eos.writeInt(powerLoadSpectrum_dims[0])
        eos.writeInt(powerLoadSpectrum_dims[1])
        eos.writeInt(powerLoadSpectrum_dims[2])
        for i in range(powerLoadSpectrum_dims[0]):
            for j in range(powerLoadSpectrum_dims[1]):
                for k in range(powerLoadSpectrum_dims[2]):
                    eos.writeFloat(self._powerLoadSpectrum[i][j][k])

        eos.writeString(str(self._syscalType))

        Temperature.listToBin(self._tAtmSpectrum, eos)

        Temperature.listToBin(self._tRecSpectrum, eos)

        Temperature.listToBin(self._tSysSpectrum, eos)

        # null array case, unsure if this is possible but this should work
        if self._tauSpectrum is None:
            eos.writeInt(0)
            eos.writeInt(0)
        else:
            tauSpectrum_dims = pyasdm.utils.getListDims(self._tauSpectrum)
        # assumes it really is 2D
        eos.writeInt(tauSpectrum_dims[0])
        eos.writeInt(tauSpectrum_dims[1])
        for i in range(tauSpectrum_dims[0]):
            for j in range(tauSpectrum_dims[1]):
                eos.writeFloat(self._tauSpectrum[i][j])

        Temperature.listToBin(self._tAtm, eos)

        Temperature.listToBin(self._tRec, eos)

        Temperature.listToBin(self._tSys, eos)

        eos.writeInt(len(self._tau))
        for i in range(len(self._tau)):

            eos.writeFloat(self._tau[i])

        Length.listToBin(self._water, eos)

        Length.listToBin(self._waterError, eos)

        eos.writeBool(self._alphaSpectrumExists)
        if self._alphaSpectrumExists:

            # null array case, unsure if this is possible but this should work
            if self._alphaSpectrum is None:
                eos.writeInt(0)
                eos.writeInt(0)
            else:
                alphaSpectrum_dims = pyasdm.utils.getListDims(self._alphaSpectrum)
            # assumes it really is 2D
            eos.writeInt(alphaSpectrum_dims[0])
            eos.writeInt(alphaSpectrum_dims[1])
            for i in range(alphaSpectrum_dims[0]):
                for j in range(alphaSpectrum_dims[1]):
                    eos.writeFloat(self._alphaSpectrum[i][j])

        eos.writeBool(self._forwardEfficiencyExists)
        if self._forwardEfficiencyExists:

            eos.writeInt(len(self._forwardEfficiency))
            for i in range(len(self._forwardEfficiency)):

                eos.writeFloat(self._forwardEfficiency[i])

        eos.writeBool(self._forwardEfficiencyErrorExists)
        if self._forwardEfficiencyErrorExists:

            eos.writeInt(len(self._forwardEfficiencyError))
            for i in range(len(self._forwardEfficiencyError)):

                eos.writeFloat(self._forwardEfficiencyError[i])

        eos.writeBool(self._sbGainExists)
        if self._sbGainExists:

            eos.writeInt(len(self._sbGain))
            for i in range(len(self._sbGain)):

                eos.writeFloat(self._sbGain[i])

        eos.writeBool(self._sbGainErrorExists)
        if self._sbGainErrorExists:

            eos.writeInt(len(self._sbGainError))
            for i in range(len(self._sbGainError)):

                eos.writeFloat(self._sbGainError[i])

        eos.writeBool(self._sbGainSpectrumExists)
        if self._sbGainSpectrumExists:

            # null array case, unsure if this is possible but this should work
            if self._sbGainSpectrum is None:
                eos.writeInt(0)
                eos.writeInt(0)
            else:
                sbGainSpectrum_dims = pyasdm.utils.getListDims(self._sbGainSpectrum)
            # assumes it really is 2D
            eos.writeInt(sbGainSpectrum_dims[0])
            eos.writeInt(sbGainSpectrum_dims[1])
            for i in range(sbGainSpectrum_dims[0]):
                for j in range(sbGainSpectrum_dims[1]):
                    eos.writeFloat(self._sbGainSpectrum[i][j])

    @staticmethod
    def antennaNameFromBin(row, eis):
        """
        Set the antennaName in row from the EndianInput (eis) instance.
        """

        row._antennaName = eis.readStr()

    @staticmethod
    def receiverBandFromBin(row, eis):
        """
        Set the receiverBand in row from the EndianInput (eis) instance.
        """

        row._receiverBand = ReceiverBand.literal(eis.readString())

    @staticmethod
    def basebandNameFromBin(row, eis):
        """
        Set the basebandName in row from the EndianInput (eis) instance.
        """

        row._basebandName = BasebandName.literal(eis.readString())

    @staticmethod
    def calDataIdFromBin(row, eis):
        """
        Set the calDataId in row from the EndianInput (eis) instance.
        """

        row._calDataId = Tag.fromBin(eis)

    @staticmethod
    def calReductionIdFromBin(row, eis):
        """
        Set the calReductionId in row from the EndianInput (eis) instance.
        """

        row._calReductionId = Tag.fromBin(eis)

    @staticmethod
    def startValidTimeFromBin(row, eis):
        """
        Set the startValidTime in row from the EndianInput (eis) instance.
        """

        row._startValidTime = ArrayTime.fromBin(eis)

    @staticmethod
    def endValidTimeFromBin(row, eis):
        """
        Set the endValidTime in row from the EndianInput (eis) instance.
        """

        row._endValidTime = ArrayTime.fromBin(eis)

    @staticmethod
    def numFreqFromBin(row, eis):
        """
        Set the numFreq in row from the EndianInput (eis) instance.
        """

        row._numFreq = eis.readInt()

    @staticmethod
    def numLoadFromBin(row, eis):
        """
        Set the numLoad in row from the EndianInput (eis) instance.
        """

        row._numLoad = eis.readInt()

    @staticmethod
    def numReceptorFromBin(row, eis):
        """
        Set the numReceptor in row from the EndianInput (eis) instance.
        """

        row._numReceptor = eis.readInt()

    @staticmethod
    def forwardEffSpectrumFromBin(row, eis):
        """
        Set the forwardEffSpectrum in row from the EndianInput (eis) instance.
        """

        forwardEffSpectrumDim1 = eis.readInt()
        forwardEffSpectrumDim2 = eis.readInt()
        thisList = []
        for i in range(forwardEffSpectrumDim1):
            thisList_j = []
            for j in range(forwardEffSpectrumDim2):
                thisValue = eis.readFloat()
                thisList_j.append(thisValue)
            thisList.append(thisList_j)
        row._forwardEffSpectrum = thisList

    @staticmethod
    def frequencyRangeFromBin(row, eis):
        """
        Set the frequencyRange in row from the EndianInput (eis) instance.
        """

        row._frequencyRange = Frequency.from1DBin(eis)

    @staticmethod
    def groundPressureFromBin(row, eis):
        """
        Set the groundPressure in row from the EndianInput (eis) instance.
        """

        row._groundPressure = Pressure.fromBin(eis)

    @staticmethod
    def groundRelHumidityFromBin(row, eis):
        """
        Set the groundRelHumidity in row from the EndianInput (eis) instance.
        """

        row._groundRelHumidity = Humidity.fromBin(eis)

    @staticmethod
    def frequencySpectrumFromBin(row, eis):
        """
        Set the frequencySpectrum in row from the EndianInput (eis) instance.
        """

        row._frequencySpectrum = Frequency.from1DBin(eis)

    @staticmethod
    def groundTemperatureFromBin(row, eis):
        """
        Set the groundTemperature in row from the EndianInput (eis) instance.
        """

        row._groundTemperature = Temperature.fromBin(eis)

    @staticmethod
    def polarizationTypesFromBin(row, eis):
        """
        Set the polarizationTypes in row from the EndianInput (eis) instance.
        """

        polarizationTypesDim1 = eis.readInt()
        thisList = []
        for i in range(polarizationTypesDim1):
            thisValue = PolarizationType.literal(eis.readString())
            thisList.append(thisValue)
        row._polarizationTypes = thisList

    @staticmethod
    def powerSkySpectrumFromBin(row, eis):
        """
        Set the powerSkySpectrum in row from the EndianInput (eis) instance.
        """

        powerSkySpectrumDim1 = eis.readInt()
        powerSkySpectrumDim2 = eis.readInt()
        thisList = []
        for i in range(powerSkySpectrumDim1):
            thisList_j = []
            for j in range(powerSkySpectrumDim2):
                thisValue = eis.readFloat()
                thisList_j.append(thisValue)
            thisList.append(thisList_j)
        row._powerSkySpectrum = thisList

    @staticmethod
    def powerLoadSpectrumFromBin(row, eis):
        """
        Set the powerLoadSpectrum in row from the EndianInput (eis) instance.
        """

        powerLoadSpectrumDim1 = eis.readInt()
        powerLoadSpectrumDim2 = eis.readInt()
        powerLoadSpectrumDim3 = eis.readInt()
        thisList = []
        for i in range(powerLoadSpectrumDim1):
            thisList_j = []
            for j in range(powerLoadSpectrumDim2):
                thisList_k = []
                for k in range(powerLoadSpectrumDim3):
                    thisValue = eis.readFloat()
                    thisList_k.append(thisValue)
                thisList_j.append(thisList_k)
            thisList.append(thisList_j)
        row._powerLoadSpectrum = thisList

    @staticmethod
    def syscalTypeFromBin(row, eis):
        """
        Set the syscalType in row from the EndianInput (eis) instance.
        """

        row._syscalType = SyscalMethod.literal(eis.readString())

    @staticmethod
    def tAtmSpectrumFromBin(row, eis):
        """
        Set the tAtmSpectrum in row from the EndianInput (eis) instance.
        """

        row._tAtmSpectrum = Temperature.from2DBin(eis)

    @staticmethod
    def tRecSpectrumFromBin(row, eis):
        """
        Set the tRecSpectrum in row from the EndianInput (eis) instance.
        """

        row._tRecSpectrum = Temperature.from2DBin(eis)

    @staticmethod
    def tSysSpectrumFromBin(row, eis):
        """
        Set the tSysSpectrum in row from the EndianInput (eis) instance.
        """

        row._tSysSpectrum = Temperature.from2DBin(eis)

    @staticmethod
    def tauSpectrumFromBin(row, eis):
        """
        Set the tauSpectrum in row from the EndianInput (eis) instance.
        """

        tauSpectrumDim1 = eis.readInt()
        tauSpectrumDim2 = eis.readInt()
        thisList = []
        for i in range(tauSpectrumDim1):
            thisList_j = []
            for j in range(tauSpectrumDim2):
                thisValue = eis.readFloat()
                thisList_j.append(thisValue)
            thisList.append(thisList_j)
        row._tauSpectrum = thisList

    @staticmethod
    def tAtmFromBin(row, eis):
        """
        Set the tAtm in row from the EndianInput (eis) instance.
        """

        row._tAtm = Temperature.from1DBin(eis)

    @staticmethod
    def tRecFromBin(row, eis):
        """
        Set the tRec in row from the EndianInput (eis) instance.
        """

        row._tRec = Temperature.from1DBin(eis)

    @staticmethod
    def tSysFromBin(row, eis):
        """
        Set the tSys in row from the EndianInput (eis) instance.
        """

        row._tSys = Temperature.from1DBin(eis)

    @staticmethod
    def tauFromBin(row, eis):
        """
        Set the tau in row from the EndianInput (eis) instance.
        """

        tauDim1 = eis.readInt()
        thisList = []
        for i in range(tauDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._tau = thisList

    @staticmethod
    def waterFromBin(row, eis):
        """
        Set the water in row from the EndianInput (eis) instance.
        """

        row._water = Length.from1DBin(eis)

    @staticmethod
    def waterErrorFromBin(row, eis):
        """
        Set the waterError in row from the EndianInput (eis) instance.
        """

        row._waterError = Length.from1DBin(eis)

    @staticmethod
    def alphaSpectrumFromBin(row, eis):
        """
        Set the optional alphaSpectrum in row from the EndianInput (eis) instance.
        """
        row._alphaSpectrumExists = eis.readBool()
        if row._alphaSpectrumExists:

            alphaSpectrumDim1 = eis.readInt()
            alphaSpectrumDim2 = eis.readInt()
            thisList = []
            for i in range(alphaSpectrumDim1):
                thisList_j = []
                for j in range(alphaSpectrumDim2):
                    thisValue = eis.readFloat()
                    thisList_j.append(thisValue)
                thisList.append(thisList_j)
            row._alphaSpectrum = thisList

    @staticmethod
    def forwardEfficiencyFromBin(row, eis):
        """
        Set the optional forwardEfficiency in row from the EndianInput (eis) instance.
        """
        row._forwardEfficiencyExists = eis.readBool()
        if row._forwardEfficiencyExists:

            forwardEfficiencyDim1 = eis.readInt()
            thisList = []
            for i in range(forwardEfficiencyDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._forwardEfficiency = thisList

    @staticmethod
    def forwardEfficiencyErrorFromBin(row, eis):
        """
        Set the optional forwardEfficiencyError in row from the EndianInput (eis) instance.
        """
        row._forwardEfficiencyErrorExists = eis.readBool()
        if row._forwardEfficiencyErrorExists:

            forwardEfficiencyErrorDim1 = eis.readInt()
            thisList = []
            for i in range(forwardEfficiencyErrorDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._forwardEfficiencyError = thisList

    @staticmethod
    def sbGainFromBin(row, eis):
        """
        Set the optional sbGain in row from the EndianInput (eis) instance.
        """
        row._sbGainExists = eis.readBool()
        if row._sbGainExists:

            sbGainDim1 = eis.readInt()
            thisList = []
            for i in range(sbGainDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._sbGain = thisList

    @staticmethod
    def sbGainErrorFromBin(row, eis):
        """
        Set the optional sbGainError in row from the EndianInput (eis) instance.
        """
        row._sbGainErrorExists = eis.readBool()
        if row._sbGainErrorExists:

            sbGainErrorDim1 = eis.readInt()
            thisList = []
            for i in range(sbGainErrorDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._sbGainError = thisList

    @staticmethod
    def sbGainSpectrumFromBin(row, eis):
        """
        Set the optional sbGainSpectrum in row from the EndianInput (eis) instance.
        """
        row._sbGainSpectrumExists = eis.readBool()
        if row._sbGainSpectrumExists:

            sbGainSpectrumDim1 = eis.readInt()
            sbGainSpectrumDim2 = eis.readInt()
            thisList = []
            for i in range(sbGainSpectrumDim1):
                thisList_j = []
                for j in range(sbGainSpectrumDim2):
                    thisValue = eis.readFloat()
                    thisList_j.append(thisValue)
                thisList.append(thisList_j)
            row._sbGainSpectrum = thisList

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaName"] = CalAtmosphereRow.antennaNameFromBin
        _fromBinMethods["receiverBand"] = CalAtmosphereRow.receiverBandFromBin
        _fromBinMethods["basebandName"] = CalAtmosphereRow.basebandNameFromBin
        _fromBinMethods["calDataId"] = CalAtmosphereRow.calDataIdFromBin
        _fromBinMethods["calReductionId"] = CalAtmosphereRow.calReductionIdFromBin
        _fromBinMethods["startValidTime"] = CalAtmosphereRow.startValidTimeFromBin
        _fromBinMethods["endValidTime"] = CalAtmosphereRow.endValidTimeFromBin
        _fromBinMethods["numFreq"] = CalAtmosphereRow.numFreqFromBin
        _fromBinMethods["numLoad"] = CalAtmosphereRow.numLoadFromBin
        _fromBinMethods["numReceptor"] = CalAtmosphereRow.numReceptorFromBin
        _fromBinMethods["forwardEffSpectrum"] = (
            CalAtmosphereRow.forwardEffSpectrumFromBin
        )
        _fromBinMethods["frequencyRange"] = CalAtmosphereRow.frequencyRangeFromBin
        _fromBinMethods["groundPressure"] = CalAtmosphereRow.groundPressureFromBin
        _fromBinMethods["groundRelHumidity"] = CalAtmosphereRow.groundRelHumidityFromBin
        _fromBinMethods["frequencySpectrum"] = CalAtmosphereRow.frequencySpectrumFromBin
        _fromBinMethods["groundTemperature"] = CalAtmosphereRow.groundTemperatureFromBin
        _fromBinMethods["polarizationTypes"] = CalAtmosphereRow.polarizationTypesFromBin
        _fromBinMethods["powerSkySpectrum"] = CalAtmosphereRow.powerSkySpectrumFromBin
        _fromBinMethods["powerLoadSpectrum"] = CalAtmosphereRow.powerLoadSpectrumFromBin
        _fromBinMethods["syscalType"] = CalAtmosphereRow.syscalTypeFromBin
        _fromBinMethods["tAtmSpectrum"] = CalAtmosphereRow.tAtmSpectrumFromBin
        _fromBinMethods["tRecSpectrum"] = CalAtmosphereRow.tRecSpectrumFromBin
        _fromBinMethods["tSysSpectrum"] = CalAtmosphereRow.tSysSpectrumFromBin
        _fromBinMethods["tauSpectrum"] = CalAtmosphereRow.tauSpectrumFromBin
        _fromBinMethods["tAtm"] = CalAtmosphereRow.tAtmFromBin
        _fromBinMethods["tRec"] = CalAtmosphereRow.tRecFromBin
        _fromBinMethods["tSys"] = CalAtmosphereRow.tSysFromBin
        _fromBinMethods["tau"] = CalAtmosphereRow.tauFromBin
        _fromBinMethods["water"] = CalAtmosphereRow.waterFromBin
        _fromBinMethods["waterError"] = CalAtmosphereRow.waterErrorFromBin

        _fromBinMethods["alphaSpectrum"] = CalAtmosphereRow.alphaSpectrumFromBin
        _fromBinMethods["forwardEfficiency"] = CalAtmosphereRow.forwardEfficiencyFromBin
        _fromBinMethods["forwardEfficiencyError"] = (
            CalAtmosphereRow.forwardEfficiencyErrorFromBin
        )
        _fromBinMethods["sbGain"] = CalAtmosphereRow.sbGainFromBin
        _fromBinMethods["sbGainError"] = CalAtmosphereRow.sbGainErrorFromBin
        _fromBinMethods["sbGainSpectrum"] = CalAtmosphereRow.sbGainSpectrumFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = CalAtmosphereRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " CalAtmosphere",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

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
            listDims = pyasdm.utils.getListDims(forwardEffSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of forwardEffSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(forwardEffSpectrum, float):
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
            listDims = pyasdm.utils.getListDims(frequencyRange)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of frequencyRange is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(frequencyRange, Frequency):
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
            listDims = pyasdm.utils.getListDims(frequencySpectrum)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of frequencySpectrum is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(frequencySpectrum, Frequency):
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
            listDims = pyasdm.utils.getListDims(polarizationTypes)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of polarizationTypes is not correct")

            # the type of the values in the list must be PolarizationType
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(polarizationTypes, PolarizationType):
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
            listDims = pyasdm.utils.getListDims(powerSkySpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of powerSkySpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(powerSkySpectrum, float):
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
            listDims = pyasdm.utils.getListDims(powerLoadSpectrum)

            shapeOK = len(listDims) == 3

            if not shapeOK:
                raise ValueError("shape of powerLoadSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(powerLoadSpectrum, float):
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
            listDims = pyasdm.utils.getListDims(tAtmSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of tAtmSpectrum is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(tAtmSpectrum, Temperature):
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
            listDims = pyasdm.utils.getListDims(tRecSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of tRecSpectrum is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(tRecSpectrum, Temperature):
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
            listDims = pyasdm.utils.getListDims(tSysSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of tSysSpectrum is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(tSysSpectrum, Temperature):
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
            listDims = pyasdm.utils.getListDims(tauSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of tauSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(tauSpectrum, float):
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
            listDims = pyasdm.utils.getListDims(tAtm)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of tAtm is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(tAtm, Temperature):
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
            listDims = pyasdm.utils.getListDims(tRec)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of tRec is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(tRec, Temperature):
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
            listDims = pyasdm.utils.getListDims(tSys)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of tSys is not correct")

            # the type of the values in the list must be Temperature
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(tSys, Temperature):
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
            listDims = pyasdm.utils.getListDims(tau)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of tau is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(tau, float):
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
            listDims = pyasdm.utils.getListDims(water)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of water is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(water, Length):
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
            listDims = pyasdm.utils.getListDims(waterError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of waterError is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(waterError, Length):
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
            listDims = pyasdm.utils.getListDims(alphaSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of alphaSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(alphaSpectrum, float):
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
            listDims = pyasdm.utils.getListDims(forwardEfficiency)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of forwardEfficiency is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(forwardEfficiency, float):
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
            listDims = pyasdm.utils.getListDims(forwardEfficiencyError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of forwardEfficiencyError is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(forwardEfficiencyError, float):
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
            listDims = pyasdm.utils.getListDims(sbGain)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of sbGain is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(sbGain, float):
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
            listDims = pyasdm.utils.getListDims(sbGainError)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of sbGainError is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(sbGainError, float):
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
            listDims = pyasdm.utils.getListDims(sbGainSpectrum)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of sbGainSpectrum is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(sbGainSpectrum, float):
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

        # We compare two 2D arrays (lists).
        if forwardEffSpectrum is not None:
            if self._forwardEffSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            forwardEffSpectrum_dims = pyasdm.utils.getListDims(forwardEffSpectrum)
            this_forwardEffSpectrum_dims = pyasdm.utils.getListDims(
                self._forwardEffSpectrum
            )
            if forwardEffSpectrum_dims != this_forwardEffSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(forwardEffSpectrum_dims[0]):
                for j in range(forwardEffSpectrum_dims[1]):

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

        # We compare two 2D arrays (lists).
        if powerSkySpectrum is not None:
            if self._powerSkySpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            powerSkySpectrum_dims = pyasdm.utils.getListDims(powerSkySpectrum)
            this_powerSkySpectrum_dims = pyasdm.utils.getListDims(
                self._powerSkySpectrum
            )
            if powerSkySpectrum_dims != this_powerSkySpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(powerSkySpectrum_dims[0]):
                for j in range(powerSkySpectrum_dims[1]):

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
            powerLoadSpectrum_dims = pyasdm.utils.getListDims(powerLoadSpectrum)
            this_powerLoadSpectrum_dims = pyasdm.utils.getListDims(
                self._powerLoadSpectrum
            )
            if powerLoadSpectrum_dims != this_powerLoadSpectrum_dims:
                return False
            # assumes they are both 3D arrays, the internal one should be
            for i in range(powerLoadSpectrum_dims[0]):
                for j in range(powerLoadSpectrum_dims[1]):
                    for k in range(powerLoadSpectrum_dims[2]):

                        # powerLoadSpectrum is an array of float, compare using == operator.
                        if not (
                            self._powerLoadSpectrum[i][j][k]
                            == powerLoadSpectrum[i][j][k]
                        ):
                            return False

        # syscalType is a SyscalMethod, compare using the == operator on the getValue() output
        if not (self._syscalType.getValue() == syscalType.getValue()):
            return False

        # We compare two 2D arrays (lists).
        if tAtmSpectrum is not None:
            if self._tAtmSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tAtmSpectrum_dims = pyasdm.utils.getListDims(tAtmSpectrum)
            this_tAtmSpectrum_dims = pyasdm.utils.getListDims(self._tAtmSpectrum)
            if tAtmSpectrum_dims != this_tAtmSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tAtmSpectrum_dims[0]):
                for j in range(tAtmSpectrum_dims[1]):

                    # tAtmSpectrum is a Temperature, compare using the almostEquals method.
                    if not (
                        self._tAtmSpectrum[i][j].almostEquals(
                            tAtmSpectrum[i][j],
                            self.getTable().getTAtmSpectrumEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if tRecSpectrum is not None:
            if self._tRecSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tRecSpectrum_dims = pyasdm.utils.getListDims(tRecSpectrum)
            this_tRecSpectrum_dims = pyasdm.utils.getListDims(self._tRecSpectrum)
            if tRecSpectrum_dims != this_tRecSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tRecSpectrum_dims[0]):
                for j in range(tRecSpectrum_dims[1]):

                    # tRecSpectrum is a Temperature, compare using the almostEquals method.
                    if not (
                        self._tRecSpectrum[i][j].almostEquals(
                            tRecSpectrum[i][j],
                            self.getTable().getTRecSpectrumEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if tSysSpectrum is not None:
            if self._tSysSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tSysSpectrum_dims = pyasdm.utils.getListDims(tSysSpectrum)
            this_tSysSpectrum_dims = pyasdm.utils.getListDims(self._tSysSpectrum)
            if tSysSpectrum_dims != this_tSysSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tSysSpectrum_dims[0]):
                for j in range(tSysSpectrum_dims[1]):

                    # tSysSpectrum is a Temperature, compare using the almostEquals method.
                    if not (
                        self._tSysSpectrum[i][j].almostEquals(
                            tSysSpectrum[i][j],
                            self.getTable().getTSysSpectrumEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if tauSpectrum is not None:
            if self._tauSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tauSpectrum_dims = pyasdm.utils.getListDims(tauSpectrum)
            this_tauSpectrum_dims = pyasdm.utils.getListDims(self._tauSpectrum)
            if tauSpectrum_dims != this_tauSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tauSpectrum_dims[0]):
                for j in range(tauSpectrum_dims[1]):

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

        # We compare two 2D arrays (lists).
        if forwardEffSpectrum is not None:
            if self._forwardEffSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            forwardEffSpectrum_dims = pyasdm.utils.getListDims(forwardEffSpectrum)
            this_forwardEffSpectrum_dims = pyasdm.utils.getListDims(
                self._forwardEffSpectrum
            )
            if forwardEffSpectrum_dims != this_forwardEffSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(forwardEffSpectrum_dims[0]):
                for j in range(forwardEffSpectrum_dims[1]):

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

        # We compare two 2D arrays (lists).
        if powerSkySpectrum is not None:
            if self._powerSkySpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            powerSkySpectrum_dims = pyasdm.utils.getListDims(powerSkySpectrum)
            this_powerSkySpectrum_dims = pyasdm.utils.getListDims(
                self._powerSkySpectrum
            )
            if powerSkySpectrum_dims != this_powerSkySpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(powerSkySpectrum_dims[0]):
                for j in range(powerSkySpectrum_dims[1]):

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
            powerLoadSpectrum_dims = pyasdm.utils.getListDims(powerLoadSpectrum)
            this_powerLoadSpectrum_dims = pyasdm.utils.getListDims(
                self._powerLoadSpectrum
            )
            if powerLoadSpectrum_dims != this_powerLoadSpectrum_dims:
                return False
            # assumes they are both 3D arrays, the internal one should be
            for i in range(powerLoadSpectrum_dims[0]):
                for j in range(powerLoadSpectrum_dims[1]):
                    for k in range(powerLoadSpectrum_dims[2]):

                        # powerLoadSpectrum is an array of float, compare using == operator.
                        if not (
                            self._powerLoadSpectrum[i][j][k]
                            == powerLoadSpectrum[i][j][k]
                        ):
                            return False

        # syscalType is a SyscalMethod, compare using the == operator on the getValue() output
        if not (self._syscalType.getValue() == syscalType.getValue()):
            return False

        # We compare two 2D arrays (lists).
        if tAtmSpectrum is not None:
            if self._tAtmSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tAtmSpectrum_dims = pyasdm.utils.getListDims(tAtmSpectrum)
            this_tAtmSpectrum_dims = pyasdm.utils.getListDims(self._tAtmSpectrum)
            if tAtmSpectrum_dims != this_tAtmSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tAtmSpectrum_dims[0]):
                for j in range(tAtmSpectrum_dims[1]):

                    # tAtmSpectrum is a Temperature, compare using the almostEquals method.
                    if not (
                        self._tAtmSpectrum[i][j].almostEquals(
                            tAtmSpectrum[i][j],
                            self.getTable().getTAtmSpectrumEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if tRecSpectrum is not None:
            if self._tRecSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tRecSpectrum_dims = pyasdm.utils.getListDims(tRecSpectrum)
            this_tRecSpectrum_dims = pyasdm.utils.getListDims(self._tRecSpectrum)
            if tRecSpectrum_dims != this_tRecSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tRecSpectrum_dims[0]):
                for j in range(tRecSpectrum_dims[1]):

                    # tRecSpectrum is a Temperature, compare using the almostEquals method.
                    if not (
                        self._tRecSpectrum[i][j].almostEquals(
                            tRecSpectrum[i][j],
                            self.getTable().getTRecSpectrumEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if tSysSpectrum is not None:
            if self._tSysSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tSysSpectrum_dims = pyasdm.utils.getListDims(tSysSpectrum)
            this_tSysSpectrum_dims = pyasdm.utils.getListDims(self._tSysSpectrum)
            if tSysSpectrum_dims != this_tSysSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tSysSpectrum_dims[0]):
                for j in range(tSysSpectrum_dims[1]):

                    # tSysSpectrum is a Temperature, compare using the almostEquals method.
                    if not (
                        self._tSysSpectrum[i][j].almostEquals(
                            tSysSpectrum[i][j],
                            self.getTable().getTSysSpectrumEqTolerance(),
                        )
                    ):
                        return False

        # We compare two 2D arrays (lists).
        if tauSpectrum is not None:
            if self._tauSpectrum is None:
                return False
            # both lists are not None, assume they are at least lists at this point
            # Compare first their dimensions and then their values.
            tauSpectrum_dims = pyasdm.utils.getListDims(tauSpectrum)
            this_tauSpectrum_dims = pyasdm.utils.getListDims(self._tauSpectrum)
            if tauSpectrum_dims != this_tauSpectrum_dims:
                return False
            # assumes they are both 2D arrays, the internal one should be

            for i in range(tauSpectrum_dims[0]):
                for j in range(tauSpectrum_dims[1]):

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


# initialize the dictionary that maps fields to init methods
CalAtmosphereRow.initFromBinMethods()
