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
# File DelayModelFixedParametersRow.py
#

import pyasdm.DelayModelFixedParametersTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from xml.dom import minidom

import copy


class DelayModelFixedParametersRow:
    """
    The DelayModelFixedParametersRow class is a row of a DelayModelFixedParametersTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a DelayModelFixedParametersRow.
        When row is None, create an empty row attached to table, which must be a DelayModelFixedParametersTable.
        When row is given, copy those values in to the new row. The row argument must be a DelayModelFixedParametersRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.DelayModelFixedParametersTable):
            raise ValueError("table must be a DelayModelFixedParametersTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._delayModelFixedParametersId = Tag()

        self._delayModelVersion = None

        self._gaussConstantExists = False

        self._gaussConstant = AngularRate()

        self._newtonianConstantExists = False

        self._newtonianConstant = None

        self._gravityExists = False

        self._gravity = None

        self._earthFlatteningExists = False

        self._earthFlattening = None

        self._earthRadiusExists = False

        self._earthRadius = Length()

        self._moonEarthMassRatioExists = False

        self._moonEarthMassRatio = None

        self._ephemerisEpochExists = False

        self._ephemerisEpoch = None

        self._earthTideLagExists = False

        self._earthTideLag = None

        self._earthGMExists = False

        self._earthGM = None

        self._moonGMExists = False

        self._moonGM = None

        self._sunGMExists = False

        self._sunGM = None

        self._loveNumberHExists = False

        self._loveNumberH = None

        self._loveNumberLExists = False

        self._loveNumberL = None

        self._precessionConstantExists = False

        self._precessionConstant = AngularRate()

        self._lightTime1AUExists = False

        self._lightTime1AU = None

        self._speedOfLightExists = False

        self._speedOfLight = Speed()

        self._delayModelFlagsExists = False

        self._delayModelFlags = None

        # extrinsic attributes

        self._execBlockId = Tag()

        if row is not None:
            if not isinstance(row, DelayModelFixedParametersRow):
                raise ValueError("row must be a DelayModelFixedParametersRow")

            # copy constructor

            self._delayModelFixedParametersId = Tag(row._delayModelFixedParametersId)

            self._delayModelVersion = row._delayModelVersion

            self._execBlockId = Tag(row._execBlockId)

            # by default set systematically gaussConstant's value to something not None

            if row._gaussConstantExists:

                self._gaussConstant = AngularRate(row._gaussConstant)

                self._gaussConstantExists = True

            # by default set systematically newtonianConstant's value to something not None

            if row._newtonianConstantExists:

                self._newtonianConstant = row._newtonianConstant

                self._newtonianConstantExists = True

            # by default set systematically gravity's value to something not None

            if row._gravityExists:

                self._gravity = row._gravity

                self._gravityExists = True

            # by default set systematically earthFlattening's value to something not None

            if row._earthFlatteningExists:

                self._earthFlattening = row._earthFlattening

                self._earthFlatteningExists = True

            # by default set systematically earthRadius's value to something not None

            if row._earthRadiusExists:

                self._earthRadius = Length(row._earthRadius)

                self._earthRadiusExists = True

            # by default set systematically moonEarthMassRatio's value to something not None

            if row._moonEarthMassRatioExists:

                self._moonEarthMassRatio = row._moonEarthMassRatio

                self._moonEarthMassRatioExists = True

            # by default set systematically ephemerisEpoch's value to something not None

            if row._ephemerisEpochExists:

                self._ephemerisEpoch = row._ephemerisEpoch

                self._ephemerisEpochExists = True

            # by default set systematically earthTideLag's value to something not None

            if row._earthTideLagExists:

                self._earthTideLag = row._earthTideLag

                self._earthTideLagExists = True

            # by default set systematically earthGM's value to something not None

            if row._earthGMExists:

                self._earthGM = row._earthGM

                self._earthGMExists = True

            # by default set systematically moonGM's value to something not None

            if row._moonGMExists:

                self._moonGM = row._moonGM

                self._moonGMExists = True

            # by default set systematically sunGM's value to something not None

            if row._sunGMExists:

                self._sunGM = row._sunGM

                self._sunGMExists = True

            # by default set systematically loveNumberH's value to something not None

            if row._loveNumberHExists:

                self._loveNumberH = row._loveNumberH

                self._loveNumberHExists = True

            # by default set systematically loveNumberL's value to something not None

            if row._loveNumberLExists:

                self._loveNumberL = row._loveNumberL

                self._loveNumberLExists = True

            # by default set systematically precessionConstant's value to something not None

            if row._precessionConstantExists:

                self._precessionConstant = AngularRate(row._precessionConstant)

                self._precessionConstantExists = True

            # by default set systematically lightTime1AU's value to something not None

            if row._lightTime1AUExists:

                self._lightTime1AU = row._lightTime1AU

                self._lightTime1AUExists = True

            # by default set systematically speedOfLight's value to something not None

            if row._speedOfLightExists:

                self._speedOfLight = Speed(row._speedOfLight)

                self._speedOfLightExists = True

            # by default set systematically delayModelFlags's value to something not None

            if row._delayModelFlagsExists:

                self._delayModelFlags = row._delayModelFlags

                self._delayModelFlagsExists = True

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

        result += Parser.extendedValueToXML(
            "delayModelFixedParametersId", self._delayModelFixedParametersId
        )

        result += Parser.valueToXML("delayModelVersion", self._delayModelVersion)

        if self._gaussConstantExists:

            result += Parser.extendedValueToXML("gaussConstant", self._gaussConstant)

        if self._newtonianConstantExists:

            result += Parser.valueToXML("newtonianConstant", self._newtonianConstant)

        if self._gravityExists:

            result += Parser.valueToXML("gravity", self._gravity)

        if self._earthFlatteningExists:

            result += Parser.valueToXML("earthFlattening", self._earthFlattening)

        if self._earthRadiusExists:

            result += Parser.extendedValueToXML("earthRadius", self._earthRadius)

        if self._moonEarthMassRatioExists:

            result += Parser.valueToXML("moonEarthMassRatio", self._moonEarthMassRatio)

        if self._ephemerisEpochExists:

            result += Parser.valueToXML("ephemerisEpoch", self._ephemerisEpoch)

        if self._earthTideLagExists:

            result += Parser.valueToXML("earthTideLag", self._earthTideLag)

        if self._earthGMExists:

            result += Parser.valueToXML("earthGM", self._earthGM)

        if self._moonGMExists:

            result += Parser.valueToXML("moonGM", self._moonGM)

        if self._sunGMExists:

            result += Parser.valueToXML("sunGM", self._sunGM)

        if self._loveNumberHExists:

            result += Parser.valueToXML("loveNumberH", self._loveNumberH)

        if self._loveNumberLExists:

            result += Parser.valueToXML("loveNumberL", self._loveNumberL)

        if self._precessionConstantExists:

            result += Parser.extendedValueToXML(
                "precessionConstant", self._precessionConstant
            )

        if self._lightTime1AUExists:

            result += Parser.valueToXML("lightTime1AU", self._lightTime1AU)

        if self._speedOfLightExists:

            result += Parser.extendedValueToXML("speedOfLight", self._speedOfLight)

        if self._delayModelFlagsExists:

            result += Parser.valueToXML("delayModelFlags", self._delayModelFlags)

        # extrinsic attributes

        result += Parser.extendedValueToXML("execBlockId", self._execBlockId)

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
                "xmlrow is not a string or a minidom.Element",
                "DelayModelFixedParametersTable",
            )

        if rowdom.nodeName != "row":
            raise ConversionException(
                "the argument is not a row", "DelayModelFixedParametersTable"
            )

        # intrinsic attribute values

        delayModelFixedParametersIdNode = rowdom.getElementsByTagName(
            "delayModelFixedParametersId"
        )[0]

        self._delayModelFixedParametersId = Tag(
            delayModelFixedParametersIdNode.firstChild.data.strip()
        )

        delayModelVersionNode = rowdom.getElementsByTagName("delayModelVersion")[0]

        self._delayModelVersion = str(delayModelVersionNode.firstChild.data.strip())

        gaussConstantNode = rowdom.getElementsByTagName("gaussConstant")
        if len(gaussConstantNode) > 0:

            self._gaussConstant = AngularRate(
                gaussConstantNode[0].firstChild.data.strip()
            )

            self._gaussConstantExists = True

        newtonianConstantNode = rowdom.getElementsByTagName("newtonianConstant")
        if len(newtonianConstantNode) > 0:

            self._newtonianConstant = float(
                newtonianConstantNode[0].firstChild.data.strip()
            )

            self._newtonianConstantExists = True

        gravityNode = rowdom.getElementsByTagName("gravity")
        if len(gravityNode) > 0:

            self._gravity = float(gravityNode[0].firstChild.data.strip())

            self._gravityExists = True

        earthFlatteningNode = rowdom.getElementsByTagName("earthFlattening")
        if len(earthFlatteningNode) > 0:

            self._earthFlattening = float(
                earthFlatteningNode[0].firstChild.data.strip()
            )

            self._earthFlatteningExists = True

        earthRadiusNode = rowdom.getElementsByTagName("earthRadius")
        if len(earthRadiusNode) > 0:

            self._earthRadius = Length(earthRadiusNode[0].firstChild.data.strip())

            self._earthRadiusExists = True

        moonEarthMassRatioNode = rowdom.getElementsByTagName("moonEarthMassRatio")
        if len(moonEarthMassRatioNode) > 0:

            self._moonEarthMassRatio = float(
                moonEarthMassRatioNode[0].firstChild.data.strip()
            )

            self._moonEarthMassRatioExists = True

        ephemerisEpochNode = rowdom.getElementsByTagName("ephemerisEpoch")
        if len(ephemerisEpochNode) > 0:

            self._ephemerisEpoch = str(ephemerisEpochNode[0].firstChild.data.strip())

            self._ephemerisEpochExists = True

        earthTideLagNode = rowdom.getElementsByTagName("earthTideLag")
        if len(earthTideLagNode) > 0:

            self._earthTideLag = float(earthTideLagNode[0].firstChild.data.strip())

            self._earthTideLagExists = True

        earthGMNode = rowdom.getElementsByTagName("earthGM")
        if len(earthGMNode) > 0:

            self._earthGM = float(earthGMNode[0].firstChild.data.strip())

            self._earthGMExists = True

        moonGMNode = rowdom.getElementsByTagName("moonGM")
        if len(moonGMNode) > 0:

            self._moonGM = float(moonGMNode[0].firstChild.data.strip())

            self._moonGMExists = True

        sunGMNode = rowdom.getElementsByTagName("sunGM")
        if len(sunGMNode) > 0:

            self._sunGM = float(sunGMNode[0].firstChild.data.strip())

            self._sunGMExists = True

        loveNumberHNode = rowdom.getElementsByTagName("loveNumberH")
        if len(loveNumberHNode) > 0:

            self._loveNumberH = float(loveNumberHNode[0].firstChild.data.strip())

            self._loveNumberHExists = True

        loveNumberLNode = rowdom.getElementsByTagName("loveNumberL")
        if len(loveNumberLNode) > 0:

            self._loveNumberL = float(loveNumberLNode[0].firstChild.data.strip())

            self._loveNumberLExists = True

        precessionConstantNode = rowdom.getElementsByTagName("precessionConstant")
        if len(precessionConstantNode) > 0:

            self._precessionConstant = AngularRate(
                precessionConstantNode[0].firstChild.data.strip()
            )

            self._precessionConstantExists = True

        lightTime1AUNode = rowdom.getElementsByTagName("lightTime1AU")
        if len(lightTime1AUNode) > 0:

            self._lightTime1AU = float(lightTime1AUNode[0].firstChild.data.strip())

            self._lightTime1AUExists = True

        speedOfLightNode = rowdom.getElementsByTagName("speedOfLight")
        if len(speedOfLightNode) > 0:

            self._speedOfLight = Speed(speedOfLightNode[0].firstChild.data.strip())

            self._speedOfLightExists = True

        delayModelFlagsNode = rowdom.getElementsByTagName("delayModelFlags")
        if len(delayModelFlagsNode) > 0:

            self._delayModelFlags = str(delayModelFlagsNode[0].firstChild.data.strip())

            self._delayModelFlagsExists = True

        # extrinsic attribute values

        execBlockIdNode = rowdom.getElementsByTagName("execBlockId")[0]

        self._execBlockId = Tag(execBlockIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._delayModelFixedParametersId.toBin(eos)

        eos.writeStr(self._delayModelVersion)

        self._execBlockId.toBin(eos)

        eos.writeBool(self._gaussConstantExists)
        if self._gaussConstantExists:

            self._gaussConstant.toBin(eos)

        eos.writeBool(self._newtonianConstantExists)
        if self._newtonianConstantExists:

            eos.writeFloat(self._newtonianConstant)

        eos.writeBool(self._gravityExists)
        if self._gravityExists:

            eos.writeFloat(self._gravity)

        eos.writeBool(self._earthFlatteningExists)
        if self._earthFlatteningExists:

            eos.writeFloat(self._earthFlattening)

        eos.writeBool(self._earthRadiusExists)
        if self._earthRadiusExists:

            self._earthRadius.toBin(eos)

        eos.writeBool(self._moonEarthMassRatioExists)
        if self._moonEarthMassRatioExists:

            eos.writeFloat(self._moonEarthMassRatio)

        eos.writeBool(self._ephemerisEpochExists)
        if self._ephemerisEpochExists:

            eos.writeStr(self._ephemerisEpoch)

        eos.writeBool(self._earthTideLagExists)
        if self._earthTideLagExists:

            eos.writeFloat(self._earthTideLag)

        eos.writeBool(self._earthGMExists)
        if self._earthGMExists:

            eos.writeFloat(self._earthGM)

        eos.writeBool(self._moonGMExists)
        if self._moonGMExists:

            eos.writeFloat(self._moonGM)

        eos.writeBool(self._sunGMExists)
        if self._sunGMExists:

            eos.writeFloat(self._sunGM)

        eos.writeBool(self._loveNumberHExists)
        if self._loveNumberHExists:

            eos.writeFloat(self._loveNumberH)

        eos.writeBool(self._loveNumberLExists)
        if self._loveNumberLExists:

            eos.writeFloat(self._loveNumberL)

        eos.writeBool(self._precessionConstantExists)
        if self._precessionConstantExists:

            self._precessionConstant.toBin(eos)

        eos.writeBool(self._lightTime1AUExists)
        if self._lightTime1AUExists:

            eos.writeFloat(self._lightTime1AU)

        eos.writeBool(self._speedOfLightExists)
        if self._speedOfLightExists:

            self._speedOfLight.toBin(eos)

        eos.writeBool(self._delayModelFlagsExists)
        if self._delayModelFlagsExists:

            eos.writeStr(self._delayModelFlags)

    @staticmethod
    def delayModelFixedParametersIdFromBin(row, eis):
        """
        Set the delayModelFixedParametersId in row from the EndianInput (eis) instance.
        """

        row._delayModelFixedParametersId = Tag.fromBin(eis)

    @staticmethod
    def delayModelVersionFromBin(row, eis):
        """
        Set the delayModelVersion in row from the EndianInput (eis) instance.
        """

        row._delayModelVersion = eis.readStr()

    @staticmethod
    def execBlockIdFromBin(row, eis):
        """
        Set the execBlockId in row from the EndianInput (eis) instance.
        """

        row._execBlockId = Tag.fromBin(eis)

    @staticmethod
    def gaussConstantFromBin(row, eis):
        """
        Set the optional gaussConstant in row from the EndianInput (eis) instance.
        """
        row._gaussConstantExists = eis.readBool()
        if row._gaussConstantExists:

            row._gaussConstant = AngularRate.fromBin(eis)

    @staticmethod
    def newtonianConstantFromBin(row, eis):
        """
        Set the optional newtonianConstant in row from the EndianInput (eis) instance.
        """
        row._newtonianConstantExists = eis.readBool()
        if row._newtonianConstantExists:

            row._newtonianConstant = eis.readFloat()

    @staticmethod
    def gravityFromBin(row, eis):
        """
        Set the optional gravity in row from the EndianInput (eis) instance.
        """
        row._gravityExists = eis.readBool()
        if row._gravityExists:

            row._gravity = eis.readFloat()

    @staticmethod
    def earthFlatteningFromBin(row, eis):
        """
        Set the optional earthFlattening in row from the EndianInput (eis) instance.
        """
        row._earthFlatteningExists = eis.readBool()
        if row._earthFlatteningExists:

            row._earthFlattening = eis.readFloat()

    @staticmethod
    def earthRadiusFromBin(row, eis):
        """
        Set the optional earthRadius in row from the EndianInput (eis) instance.
        """
        row._earthRadiusExists = eis.readBool()
        if row._earthRadiusExists:

            row._earthRadius = Length.fromBin(eis)

    @staticmethod
    def moonEarthMassRatioFromBin(row, eis):
        """
        Set the optional moonEarthMassRatio in row from the EndianInput (eis) instance.
        """
        row._moonEarthMassRatioExists = eis.readBool()
        if row._moonEarthMassRatioExists:

            row._moonEarthMassRatio = eis.readFloat()

    @staticmethod
    def ephemerisEpochFromBin(row, eis):
        """
        Set the optional ephemerisEpoch in row from the EndianInput (eis) instance.
        """
        row._ephemerisEpochExists = eis.readBool()
        if row._ephemerisEpochExists:

            row._ephemerisEpoch = eis.readStr()

    @staticmethod
    def earthTideLagFromBin(row, eis):
        """
        Set the optional earthTideLag in row from the EndianInput (eis) instance.
        """
        row._earthTideLagExists = eis.readBool()
        if row._earthTideLagExists:

            row._earthTideLag = eis.readFloat()

    @staticmethod
    def earthGMFromBin(row, eis):
        """
        Set the optional earthGM in row from the EndianInput (eis) instance.
        """
        row._earthGMExists = eis.readBool()
        if row._earthGMExists:

            row._earthGM = eis.readFloat()

    @staticmethod
    def moonGMFromBin(row, eis):
        """
        Set the optional moonGM in row from the EndianInput (eis) instance.
        """
        row._moonGMExists = eis.readBool()
        if row._moonGMExists:

            row._moonGM = eis.readFloat()

    @staticmethod
    def sunGMFromBin(row, eis):
        """
        Set the optional sunGM in row from the EndianInput (eis) instance.
        """
        row._sunGMExists = eis.readBool()
        if row._sunGMExists:

            row._sunGM = eis.readFloat()

    @staticmethod
    def loveNumberHFromBin(row, eis):
        """
        Set the optional loveNumberH in row from the EndianInput (eis) instance.
        """
        row._loveNumberHExists = eis.readBool()
        if row._loveNumberHExists:

            row._loveNumberH = eis.readFloat()

    @staticmethod
    def loveNumberLFromBin(row, eis):
        """
        Set the optional loveNumberL in row from the EndianInput (eis) instance.
        """
        row._loveNumberLExists = eis.readBool()
        if row._loveNumberLExists:

            row._loveNumberL = eis.readFloat()

    @staticmethod
    def precessionConstantFromBin(row, eis):
        """
        Set the optional precessionConstant in row from the EndianInput (eis) instance.
        """
        row._precessionConstantExists = eis.readBool()
        if row._precessionConstantExists:

            row._precessionConstant = AngularRate.fromBin(eis)

    @staticmethod
    def lightTime1AUFromBin(row, eis):
        """
        Set the optional lightTime1AU in row from the EndianInput (eis) instance.
        """
        row._lightTime1AUExists = eis.readBool()
        if row._lightTime1AUExists:

            row._lightTime1AU = eis.readFloat()

    @staticmethod
    def speedOfLightFromBin(row, eis):
        """
        Set the optional speedOfLight in row from the EndianInput (eis) instance.
        """
        row._speedOfLightExists = eis.readBool()
        if row._speedOfLightExists:

            row._speedOfLight = Speed.fromBin(eis)

    @staticmethod
    def delayModelFlagsFromBin(row, eis):
        """
        Set the optional delayModelFlags in row from the EndianInput (eis) instance.
        """
        row._delayModelFlagsExists = eis.readBool()
        if row._delayModelFlagsExists:

            row._delayModelFlags = eis.readStr()

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["delayModelFixedParametersId"] = (
            DelayModelFixedParametersRow.delayModelFixedParametersIdFromBin
        )
        _fromBinMethods["delayModelVersion"] = (
            DelayModelFixedParametersRow.delayModelVersionFromBin
        )
        _fromBinMethods["execBlockId"] = DelayModelFixedParametersRow.execBlockIdFromBin

        _fromBinMethods["gaussConstant"] = (
            DelayModelFixedParametersRow.gaussConstantFromBin
        )
        _fromBinMethods["newtonianConstant"] = (
            DelayModelFixedParametersRow.newtonianConstantFromBin
        )
        _fromBinMethods["gravity"] = DelayModelFixedParametersRow.gravityFromBin
        _fromBinMethods["earthFlattening"] = (
            DelayModelFixedParametersRow.earthFlatteningFromBin
        )
        _fromBinMethods["earthRadius"] = DelayModelFixedParametersRow.earthRadiusFromBin
        _fromBinMethods["moonEarthMassRatio"] = (
            DelayModelFixedParametersRow.moonEarthMassRatioFromBin
        )
        _fromBinMethods["ephemerisEpoch"] = (
            DelayModelFixedParametersRow.ephemerisEpochFromBin
        )
        _fromBinMethods["earthTideLag"] = (
            DelayModelFixedParametersRow.earthTideLagFromBin
        )
        _fromBinMethods["earthGM"] = DelayModelFixedParametersRow.earthGMFromBin
        _fromBinMethods["moonGM"] = DelayModelFixedParametersRow.moonGMFromBin
        _fromBinMethods["sunGM"] = DelayModelFixedParametersRow.sunGMFromBin
        _fromBinMethods["loveNumberH"] = DelayModelFixedParametersRow.loveNumberHFromBin
        _fromBinMethods["loveNumberL"] = DelayModelFixedParametersRow.loveNumberLFromBin
        _fromBinMethods["precessionConstant"] = (
            DelayModelFixedParametersRow.precessionConstantFromBin
        )
        _fromBinMethods["lightTime1AU"] = (
            DelayModelFixedParametersRow.lightTime1AUFromBin
        )
        _fromBinMethods["speedOfLight"] = (
            DelayModelFixedParametersRow.speedOfLightFromBin
        )
        _fromBinMethods["delayModelFlags"] = (
            DelayModelFixedParametersRow.delayModelFlagsFromBin
        )

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = DelayModelFixedParametersRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " DelayModelFixedParameters",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute delayModelFixedParametersId

    _delayModelFixedParametersId = Tag()

    def getDelayModelFixedParametersId(self):
        """
        Get delayModelFixedParametersId.
        return delayModelFixedParametersId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._delayModelFixedParametersId)

    def setDelayModelFixedParametersId(self, delayModelFixedParametersId):
        """
        Set delayModelFixedParametersId with the specified Tag value.
        delayModelFixedParametersId The Tag value to which delayModelFixedParametersId is to be set.
        The value of delayModelFixedParametersId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the delayModelFixedParametersId field, which is part of the key, after this row has been added to this table."
            )

        self._delayModelFixedParametersId = Tag(delayModelFixedParametersId)

    # ===> Attribute delayModelVersion

    _delayModelVersion = None

    def getDelayModelVersion(self):
        """
        Get delayModelVersion.
        return delayModelVersion as str
        """

        return self._delayModelVersion

    def setDelayModelVersion(self, delayModelVersion):
        """
        Set delayModelVersion with the specified str value.
        delayModelVersion The str value to which delayModelVersion is to be set.


        """

        self._delayModelVersion = str(delayModelVersion)

    # ===> Attribute gaussConstant, which is optional
    _gaussConstantExists = False

    _gaussConstant = AngularRate()

    def isGaussConstantExists(self):
        """
        The attribute gaussConstant is optional. Return True if this attribute exists.
        return True if and only if the gaussConstant attribute exists.
        """
        return self._gaussConstantExists

    def getGaussConstant(self):
        """
        Get gaussConstant, which is optional.
        return gaussConstant as AngularRate
        raises ValueError If gaussConstant does not exist.
        """
        if not self._gaussConstantExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + gaussConstant
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        # make sure it is a copy of AngularRate
        return AngularRate(self._gaussConstant)

    def setGaussConstant(self, gaussConstant):
        """
        Set gaussConstant with the specified AngularRate value.
        gaussConstant The AngularRate value to which gaussConstant is to be set.
        The value of gaussConstant can be anything allowed by the AngularRate constructor.

        """

        self._gaussConstant = AngularRate(gaussConstant)

        self._gaussConstantExists = True

    def clearGaussConstant(self):
        """
        Mark gaussConstant, which is an optional field, as non-existent.
        """
        self._gaussConstantExists = False

    # ===> Attribute newtonianConstant, which is optional
    _newtonianConstantExists = False

    _newtonianConstant = None

    def isNewtonianConstantExists(self):
        """
        The attribute newtonianConstant is optional. Return True if this attribute exists.
        return True if and only if the newtonianConstant attribute exists.
        """
        return self._newtonianConstantExists

    def getNewtonianConstant(self):
        """
        Get newtonianConstant, which is optional.
        return newtonianConstant as float
        raises ValueError If newtonianConstant does not exist.
        """
        if not self._newtonianConstantExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + newtonianConstant
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        return self._newtonianConstant

    def setNewtonianConstant(self, newtonianConstant):
        """
        Set newtonianConstant with the specified float value.
        newtonianConstant The float value to which newtonianConstant is to be set.


        """

        self._newtonianConstant = float(newtonianConstant)

        self._newtonianConstantExists = True

    def clearNewtonianConstant(self):
        """
        Mark newtonianConstant, which is an optional field, as non-existent.
        """
        self._newtonianConstantExists = False

    # ===> Attribute gravity, which is optional
    _gravityExists = False

    _gravity = None

    def isGravityExists(self):
        """
        The attribute gravity is optional. Return True if this attribute exists.
        return True if and only if the gravity attribute exists.
        """
        return self._gravityExists

    def getGravity(self):
        """
        Get gravity, which is optional.
        return gravity as float
        raises ValueError If gravity does not exist.
        """
        if not self._gravityExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + gravity
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        return self._gravity

    def setGravity(self, gravity):
        """
        Set gravity with the specified float value.
        gravity The float value to which gravity is to be set.


        """

        self._gravity = float(gravity)

        self._gravityExists = True

    def clearGravity(self):
        """
        Mark gravity, which is an optional field, as non-existent.
        """
        self._gravityExists = False

    # ===> Attribute earthFlattening, which is optional
    _earthFlatteningExists = False

    _earthFlattening = None

    def isEarthFlatteningExists(self):
        """
        The attribute earthFlattening is optional. Return True if this attribute exists.
        return True if and only if the earthFlattening attribute exists.
        """
        return self._earthFlatteningExists

    def getEarthFlattening(self):
        """
        Get earthFlattening, which is optional.
        return earthFlattening as float
        raises ValueError If earthFlattening does not exist.
        """
        if not self._earthFlatteningExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + earthFlattening
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        return self._earthFlattening

    def setEarthFlattening(self, earthFlattening):
        """
        Set earthFlattening with the specified float value.
        earthFlattening The float value to which earthFlattening is to be set.


        """

        self._earthFlattening = float(earthFlattening)

        self._earthFlatteningExists = True

    def clearEarthFlattening(self):
        """
        Mark earthFlattening, which is an optional field, as non-existent.
        """
        self._earthFlatteningExists = False

    # ===> Attribute earthRadius, which is optional
    _earthRadiusExists = False

    _earthRadius = Length()

    def isEarthRadiusExists(self):
        """
        The attribute earthRadius is optional. Return True if this attribute exists.
        return True if and only if the earthRadius attribute exists.
        """
        return self._earthRadiusExists

    def getEarthRadius(self):
        """
        Get earthRadius, which is optional.
        return earthRadius as Length
        raises ValueError If earthRadius does not exist.
        """
        if not self._earthRadiusExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + earthRadius
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        # make sure it is a copy of Length
        return Length(self._earthRadius)

    def setEarthRadius(self, earthRadius):
        """
        Set earthRadius with the specified Length value.
        earthRadius The Length value to which earthRadius is to be set.
        The value of earthRadius can be anything allowed by the Length constructor.

        """

        self._earthRadius = Length(earthRadius)

        self._earthRadiusExists = True

    def clearEarthRadius(self):
        """
        Mark earthRadius, which is an optional field, as non-existent.
        """
        self._earthRadiusExists = False

    # ===> Attribute moonEarthMassRatio, which is optional
    _moonEarthMassRatioExists = False

    _moonEarthMassRatio = None

    def isMoonEarthMassRatioExists(self):
        """
        The attribute moonEarthMassRatio is optional. Return True if this attribute exists.
        return True if and only if the moonEarthMassRatio attribute exists.
        """
        return self._moonEarthMassRatioExists

    def getMoonEarthMassRatio(self):
        """
        Get moonEarthMassRatio, which is optional.
        return moonEarthMassRatio as float
        raises ValueError If moonEarthMassRatio does not exist.
        """
        if not self._moonEarthMassRatioExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + moonEarthMassRatio
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        return self._moonEarthMassRatio

    def setMoonEarthMassRatio(self, moonEarthMassRatio):
        """
        Set moonEarthMassRatio with the specified float value.
        moonEarthMassRatio The float value to which moonEarthMassRatio is to be set.


        """

        self._moonEarthMassRatio = float(moonEarthMassRatio)

        self._moonEarthMassRatioExists = True

    def clearMoonEarthMassRatio(self):
        """
        Mark moonEarthMassRatio, which is an optional field, as non-existent.
        """
        self._moonEarthMassRatioExists = False

    # ===> Attribute ephemerisEpoch, which is optional
    _ephemerisEpochExists = False

    _ephemerisEpoch = None

    def isEphemerisEpochExists(self):
        """
        The attribute ephemerisEpoch is optional. Return True if this attribute exists.
        return True if and only if the ephemerisEpoch attribute exists.
        """
        return self._ephemerisEpochExists

    def getEphemerisEpoch(self):
        """
        Get ephemerisEpoch, which is optional.
        return ephemerisEpoch as str
        raises ValueError If ephemerisEpoch does not exist.
        """
        if not self._ephemerisEpochExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + ephemerisEpoch
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        return self._ephemerisEpoch

    def setEphemerisEpoch(self, ephemerisEpoch):
        """
        Set ephemerisEpoch with the specified str value.
        ephemerisEpoch The str value to which ephemerisEpoch is to be set.


        """

        self._ephemerisEpoch = str(ephemerisEpoch)

        self._ephemerisEpochExists = True

    def clearEphemerisEpoch(self):
        """
        Mark ephemerisEpoch, which is an optional field, as non-existent.
        """
        self._ephemerisEpochExists = False

    # ===> Attribute earthTideLag, which is optional
    _earthTideLagExists = False

    _earthTideLag = None

    def isEarthTideLagExists(self):
        """
        The attribute earthTideLag is optional. Return True if this attribute exists.
        return True if and only if the earthTideLag attribute exists.
        """
        return self._earthTideLagExists

    def getEarthTideLag(self):
        """
        Get earthTideLag, which is optional.
        return earthTideLag as float
        raises ValueError If earthTideLag does not exist.
        """
        if not self._earthTideLagExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + earthTideLag
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        return self._earthTideLag

    def setEarthTideLag(self, earthTideLag):
        """
        Set earthTideLag with the specified float value.
        earthTideLag The float value to which earthTideLag is to be set.


        """

        self._earthTideLag = float(earthTideLag)

        self._earthTideLagExists = True

    def clearEarthTideLag(self):
        """
        Mark earthTideLag, which is an optional field, as non-existent.
        """
        self._earthTideLagExists = False

    # ===> Attribute earthGM, which is optional
    _earthGMExists = False

    _earthGM = None

    def isEarthGMExists(self):
        """
        The attribute earthGM is optional. Return True if this attribute exists.
        return True if and only if the earthGM attribute exists.
        """
        return self._earthGMExists

    def getEarthGM(self):
        """
        Get earthGM, which is optional.
        return earthGM as float
        raises ValueError If earthGM does not exist.
        """
        if not self._earthGMExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + earthGM
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        return self._earthGM

    def setEarthGM(self, earthGM):
        """
        Set earthGM with the specified float value.
        earthGM The float value to which earthGM is to be set.


        """

        self._earthGM = float(earthGM)

        self._earthGMExists = True

    def clearEarthGM(self):
        """
        Mark earthGM, which is an optional field, as non-existent.
        """
        self._earthGMExists = False

    # ===> Attribute moonGM, which is optional
    _moonGMExists = False

    _moonGM = None

    def isMoonGMExists(self):
        """
        The attribute moonGM is optional. Return True if this attribute exists.
        return True if and only if the moonGM attribute exists.
        """
        return self._moonGMExists

    def getMoonGM(self):
        """
        Get moonGM, which is optional.
        return moonGM as float
        raises ValueError If moonGM does not exist.
        """
        if not self._moonGMExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + moonGM
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        return self._moonGM

    def setMoonGM(self, moonGM):
        """
        Set moonGM with the specified float value.
        moonGM The float value to which moonGM is to be set.


        """

        self._moonGM = float(moonGM)

        self._moonGMExists = True

    def clearMoonGM(self):
        """
        Mark moonGM, which is an optional field, as non-existent.
        """
        self._moonGMExists = False

    # ===> Attribute sunGM, which is optional
    _sunGMExists = False

    _sunGM = None

    def isSunGMExists(self):
        """
        The attribute sunGM is optional. Return True if this attribute exists.
        return True if and only if the sunGM attribute exists.
        """
        return self._sunGMExists

    def getSunGM(self):
        """
        Get sunGM, which is optional.
        return sunGM as float
        raises ValueError If sunGM does not exist.
        """
        if not self._sunGMExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sunGM
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        return self._sunGM

    def setSunGM(self, sunGM):
        """
        Set sunGM with the specified float value.
        sunGM The float value to which sunGM is to be set.


        """

        self._sunGM = float(sunGM)

        self._sunGMExists = True

    def clearSunGM(self):
        """
        Mark sunGM, which is an optional field, as non-existent.
        """
        self._sunGMExists = False

    # ===> Attribute loveNumberH, which is optional
    _loveNumberHExists = False

    _loveNumberH = None

    def isLoveNumberHExists(self):
        """
        The attribute loveNumberH is optional. Return True if this attribute exists.
        return True if and only if the loveNumberH attribute exists.
        """
        return self._loveNumberHExists

    def getLoveNumberH(self):
        """
        Get loveNumberH, which is optional.
        return loveNumberH as float
        raises ValueError If loveNumberH does not exist.
        """
        if not self._loveNumberHExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + loveNumberH
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        return self._loveNumberH

    def setLoveNumberH(self, loveNumberH):
        """
        Set loveNumberH with the specified float value.
        loveNumberH The float value to which loveNumberH is to be set.


        """

        self._loveNumberH = float(loveNumberH)

        self._loveNumberHExists = True

    def clearLoveNumberH(self):
        """
        Mark loveNumberH, which is an optional field, as non-existent.
        """
        self._loveNumberHExists = False

    # ===> Attribute loveNumberL, which is optional
    _loveNumberLExists = False

    _loveNumberL = None

    def isLoveNumberLExists(self):
        """
        The attribute loveNumberL is optional. Return True if this attribute exists.
        return True if and only if the loveNumberL attribute exists.
        """
        return self._loveNumberLExists

    def getLoveNumberL(self):
        """
        Get loveNumberL, which is optional.
        return loveNumberL as float
        raises ValueError If loveNumberL does not exist.
        """
        if not self._loveNumberLExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + loveNumberL
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        return self._loveNumberL

    def setLoveNumberL(self, loveNumberL):
        """
        Set loveNumberL with the specified float value.
        loveNumberL The float value to which loveNumberL is to be set.


        """

        self._loveNumberL = float(loveNumberL)

        self._loveNumberLExists = True

    def clearLoveNumberL(self):
        """
        Mark loveNumberL, which is an optional field, as non-existent.
        """
        self._loveNumberLExists = False

    # ===> Attribute precessionConstant, which is optional
    _precessionConstantExists = False

    _precessionConstant = AngularRate()

    def isPrecessionConstantExists(self):
        """
        The attribute precessionConstant is optional. Return True if this attribute exists.
        return True if and only if the precessionConstant attribute exists.
        """
        return self._precessionConstantExists

    def getPrecessionConstant(self):
        """
        Get precessionConstant, which is optional.
        return precessionConstant as AngularRate
        raises ValueError If precessionConstant does not exist.
        """
        if not self._precessionConstantExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + precessionConstant
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        # make sure it is a copy of AngularRate
        return AngularRate(self._precessionConstant)

    def setPrecessionConstant(self, precessionConstant):
        """
        Set precessionConstant with the specified AngularRate value.
        precessionConstant The AngularRate value to which precessionConstant is to be set.
        The value of precessionConstant can be anything allowed by the AngularRate constructor.

        """

        self._precessionConstant = AngularRate(precessionConstant)

        self._precessionConstantExists = True

    def clearPrecessionConstant(self):
        """
        Mark precessionConstant, which is an optional field, as non-existent.
        """
        self._precessionConstantExists = False

    # ===> Attribute lightTime1AU, which is optional
    _lightTime1AUExists = False

    _lightTime1AU = None

    def isLightTime1AUExists(self):
        """
        The attribute lightTime1AU is optional. Return True if this attribute exists.
        return True if and only if the lightTime1AU attribute exists.
        """
        return self._lightTime1AUExists

    def getLightTime1AU(self):
        """
        Get lightTime1AU, which is optional.
        return lightTime1AU as float
        raises ValueError If lightTime1AU does not exist.
        """
        if not self._lightTime1AUExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + lightTime1AU
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        return self._lightTime1AU

    def setLightTime1AU(self, lightTime1AU):
        """
        Set lightTime1AU with the specified float value.
        lightTime1AU The float value to which lightTime1AU is to be set.


        """

        self._lightTime1AU = float(lightTime1AU)

        self._lightTime1AUExists = True

    def clearLightTime1AU(self):
        """
        Mark lightTime1AU, which is an optional field, as non-existent.
        """
        self._lightTime1AUExists = False

    # ===> Attribute speedOfLight, which is optional
    _speedOfLightExists = False

    _speedOfLight = Speed()

    def isSpeedOfLightExists(self):
        """
        The attribute speedOfLight is optional. Return True if this attribute exists.
        return True if and only if the speedOfLight attribute exists.
        """
        return self._speedOfLightExists

    def getSpeedOfLight(self):
        """
        Get speedOfLight, which is optional.
        return speedOfLight as Speed
        raises ValueError If speedOfLight does not exist.
        """
        if not self._speedOfLightExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + speedOfLight
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        # make sure it is a copy of Speed
        return Speed(self._speedOfLight)

    def setSpeedOfLight(self, speedOfLight):
        """
        Set speedOfLight with the specified Speed value.
        speedOfLight The Speed value to which speedOfLight is to be set.
        The value of speedOfLight can be anything allowed by the Speed constructor.

        """

        self._speedOfLight = Speed(speedOfLight)

        self._speedOfLightExists = True

    def clearSpeedOfLight(self):
        """
        Mark speedOfLight, which is an optional field, as non-existent.
        """
        self._speedOfLightExists = False

    # ===> Attribute delayModelFlags, which is optional
    _delayModelFlagsExists = False

    _delayModelFlags = None

    def isDelayModelFlagsExists(self):
        """
        The attribute delayModelFlags is optional. Return True if this attribute exists.
        return True if and only if the delayModelFlags attribute exists.
        """
        return self._delayModelFlagsExists

    def getDelayModelFlags(self):
        """
        Get delayModelFlags, which is optional.
        return delayModelFlags as str
        raises ValueError If delayModelFlags does not exist.
        """
        if not self._delayModelFlagsExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + delayModelFlags
                + " attribute in table DelayModelFixedParameters does not exist!"
            )

        return self._delayModelFlags

    def setDelayModelFlags(self, delayModelFlags):
        """
        Set delayModelFlags with the specified str value.
        delayModelFlags The str value to which delayModelFlags is to be set.


        """

        self._delayModelFlags = str(delayModelFlags)

        self._delayModelFlagsExists = True

    def clearDelayModelFlags(self):
        """
        Mark delayModelFlags, which is an optional field, as non-existent.
        """
        self._delayModelFlagsExists = False

    # Extrinsic Table Attributes

    # ===> Attribute execBlockId

    _execBlockId = Tag()

    def getExecBlockId(self):
        """
        Get execBlockId.
        return execBlockId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._execBlockId)

    def setExecBlockId(self, execBlockId):
        """
        Set execBlockId with the specified Tag value.
        execBlockId The Tag value to which execBlockId is to be set.
        The value of execBlockId can be anything allowed by the Tag constructor.

        """

        self._execBlockId = Tag(execBlockId)

    # Links

    def getExecBlockUsingExecBlockId(self):
        """
        Returns the row in the ExecBlock table having ExecBlock.execBlockId == execBlockId

        """

        return self._table.getContainer().getExecBlock().getRowByKey(self._execBlockId)

    # comparison methods

    def compareNoAutoInc(self, delayModelVersion, execBlockId):
        """
        Compare each attribute except the autoincrementable one of this DelayModelFixedParametersRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # delayModelVersion is a str, compare using the == operator.
        if not (self._delayModelVersion == delayModelVersion):
            return False

        # execBlockId is a Tag, compare using the equals method.
        if not self._execBlockId.equals(execBlockId):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getDelayModelVersion(), otherRow.getExecBlockId()
        )

    def compareRequiredValue(self, delayModelVersion, execBlockId):

        # delayModelVersion is a str, compare using the == operator.
        if not (self._delayModelVersion == delayModelVersion):
            return False

        # execBlockId is a Tag, compare using the equals method.
        if not self._execBlockId.equals(execBlockId):
            return False

        return True


# initialize the dictionary that maps fields to init methods
DelayModelFixedParametersRow.initFromBinMethods()
