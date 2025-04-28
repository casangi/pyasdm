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
# File SourceRow.py
#

import pyasdm.SourceTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.DirectionReferenceCode import DirectionReferenceCode


from pyasdm.enumerations.SourceModel import SourceModel


from pyasdm.enumerations.FrequencyReferenceCode import FrequencyReferenceCode


from pyasdm.enumerations.StokesParameter import StokesParameter


from pyasdm.enumerations.RadialVelocityReferenceCode import RadialVelocityReferenceCode


from pyasdm.enumerations.RadialVelocityReferenceCode import RadialVelocityReferenceCode


from pyasdm.enumerations.DopplerReferenceCode import DopplerReferenceCode


from xml.dom import minidom

import copy


class SourceRow:
    """
    The SourceRow class is a row of a SourceTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a SourceRow.
        When row is None, create an empty row attached to table, which must be a SourceTable.
        When row is given, copy those values in to the new row. The row argument must be a SourceRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.SourceTable):
            raise ValueError("table must be a SourceTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._sourceId = 0

        self._timeInterval = ArrayTimeInterval()

        self._code = None

        self._direction = []  # this is a list of Angle []

        self._properMotion = []  # this is a list of AngularRate []

        self._sourceName = None

        self._directionCodeExists = False

        self._directionCode = DirectionReferenceCode.from_int(0)

        self._directionEquinoxExists = False

        self._directionEquinox = ArrayTime()

        self._calibrationGroupExists = False

        self._calibrationGroup = 0

        self._catalogExists = False

        self._catalog = None

        self._deltaVelExists = False

        self._deltaVel = Speed()

        self._positionExists = False

        self._position = []  # this is a list of Length []

        self._numLinesExists = False

        self._numLines = 0

        self._transitionExists = False

        self._transition = []  # this is a list of str []

        self._restFrequencyExists = False

        self._restFrequency = []  # this is a list of Frequency []

        self._sysVelExists = False

        self._sysVel = []  # this is a list of Speed []

        self._rangeVelExists = False

        self._rangeVel = []  # this is a list of Speed []

        self._sourceModelExists = False

        self._sourceModel = SourceModel.from_int(0)

        self._frequencyRefCodeExists = False

        self._frequencyRefCode = FrequencyReferenceCode.from_int(0)

        self._numFreqExists = False

        self._numFreq = 0

        self._numStokesExists = False

        self._numStokes = 0

        self._frequencyExists = False

        self._frequency = []  # this is a list of Frequency []

        self._frequencyIntervalExists = False

        self._frequencyInterval = []  # this is a list of Frequency []

        self._stokesParameterExists = False

        self._stokesParameter = []  # this is a list of StokesParameter []

        self._fluxExists = False

        self._flux = []  # this is a list of Flux []  []

        self._fluxErrExists = False

        self._fluxErr = []  # this is a list of Flux []  []

        self._positionAngleExists = False

        self._positionAngle = []  # this is a list of Angle []

        self._positionAngleErrExists = False

        self._positionAngleErr = []  # this is a list of Angle []

        self._sizeExists = False

        self._size = []  # this is a list of Angle []  []

        self._sizeErrExists = False

        self._sizeErr = []  # this is a list of Angle []  []

        self._velRefCodeExists = False

        self._velRefCode = RadialVelocityReferenceCode.from_int(0)

        self._dopplerVelocityExists = False

        self._dopplerVelocity = []  # this is a list of Speed []

        self._dopplerReferenceSystemExists = False

        self._dopplerReferenceSystem = RadialVelocityReferenceCode.from_int(0)

        self._dopplerCalcTypeExists = False

        self._dopplerCalcType = DopplerReferenceCode.from_int(0)

        self._parallaxExists = False

        self._parallax = []  # this is a list of Angle []

        # extrinsic attributes

        self._spectralWindowId = Tag()

        if row is not None:
            if not isinstance(row, SourceRow):
                raise ValueError("row must be a SourceRow")

            # copy constructor

            self._sourceId = row._sourceId

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._spectralWindowId = Tag(row._spectralWindowId)

            self._code = row._code

            # direction is a  list , make a deep copy
            self._direction = copy.deepcopy(row._direction)

            # properMotion is a  list , make a deep copy
            self._properMotion = copy.deepcopy(row._properMotion)

            self._sourceName = row._sourceName

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

            # by default set systematically calibrationGroup's value to something not None

            if row._calibrationGroupExists:

                self._calibrationGroup = row._calibrationGroup

                self._calibrationGroupExists = True

            # by default set systematically catalog's value to something not None

            if row._catalogExists:

                self._catalog = row._catalog

                self._catalogExists = True

            # by default set systematically deltaVel's value to something not None

            if row._deltaVelExists:

                self._deltaVel = Speed(row._deltaVel)

                self._deltaVelExists = True

            # by default set systematically position's value to something not None

            if row._positionExists:

                # position is a list, make a deep copy
                self._position = copy.deepcopy(row._position)

                self._positionExists = True

            # by default set systematically numLines's value to something not None

            if row._numLinesExists:

                self._numLines = row._numLines

                self._numLinesExists = True

            # by default set systematically transition's value to something not None

            if row._transitionExists:

                # transition is a list, make a deep copy
                self._transition = copy.deepcopy(row._transition)

                self._transitionExists = True

            # by default set systematically restFrequency's value to something not None

            if row._restFrequencyExists:

                # restFrequency is a list, make a deep copy
                self._restFrequency = copy.deepcopy(row._restFrequency)

                self._restFrequencyExists = True

            # by default set systematically sysVel's value to something not None

            if row._sysVelExists:

                # sysVel is a list, make a deep copy
                self._sysVel = copy.deepcopy(row._sysVel)

                self._sysVelExists = True

            # by default set systematically rangeVel's value to something not None

            if row._rangeVelExists:

                # rangeVel is a list, make a deep copy
                self._rangeVel = copy.deepcopy(row._rangeVel)

                self._rangeVelExists = True

            # by default set systematically sourceModel's value to something not None

            self._sourceModel = SourceModel.from_int(0)

            if row._sourceModelExists:

                if row._sourceModel is not None:
                    self._sourceModel = row._sourceModel

                self._sourceModelExists = True

            # by default set systematically frequencyRefCode's value to something not None

            self._frequencyRefCode = FrequencyReferenceCode.from_int(0)

            if row._frequencyRefCodeExists:

                if row._frequencyRefCode is not None:
                    self._frequencyRefCode = row._frequencyRefCode

                self._frequencyRefCodeExists = True

            # by default set systematically numFreq's value to something not None

            if row._numFreqExists:

                self._numFreq = row._numFreq

                self._numFreqExists = True

            # by default set systematically numStokes's value to something not None

            if row._numStokesExists:

                self._numStokes = row._numStokes

                self._numStokesExists = True

            # by default set systematically frequency's value to something not None

            if row._frequencyExists:

                # frequency is a list, make a deep copy
                self._frequency = copy.deepcopy(row._frequency)

                self._frequencyExists = True

            # by default set systematically frequencyInterval's value to something not None

            if row._frequencyIntervalExists:

                # frequencyInterval is a list, make a deep copy
                self._frequencyInterval = copy.deepcopy(row._frequencyInterval)

                self._frequencyIntervalExists = True

            # by default set systematically stokesParameter's value to something not None

            if row._stokesParameterExists:

                # stokesParameter is a list, make a deep copy
                self._stokesParameter = copy.deepcopy(row._stokesParameter)

                self._stokesParameterExists = True

            # by default set systematically flux's value to something not None

            if row._fluxExists:

                # flux is a list, make a deep copy
                self._flux = copy.deepcopy(row._flux)

                self._fluxExists = True

            # by default set systematically fluxErr's value to something not None

            if row._fluxErrExists:

                # fluxErr is a list, make a deep copy
                self._fluxErr = copy.deepcopy(row._fluxErr)

                self._fluxErrExists = True

            # by default set systematically positionAngle's value to something not None

            if row._positionAngleExists:

                # positionAngle is a list, make a deep copy
                self._positionAngle = copy.deepcopy(row._positionAngle)

                self._positionAngleExists = True

            # by default set systematically positionAngleErr's value to something not None

            if row._positionAngleErrExists:

                # positionAngleErr is a list, make a deep copy
                self._positionAngleErr = copy.deepcopy(row._positionAngleErr)

                self._positionAngleErrExists = True

            # by default set systematically size's value to something not None

            if row._sizeExists:

                # size is a list, make a deep copy
                self._size = copy.deepcopy(row._size)

                self._sizeExists = True

            # by default set systematically sizeErr's value to something not None

            if row._sizeErrExists:

                # sizeErr is a list, make a deep copy
                self._sizeErr = copy.deepcopy(row._sizeErr)

                self._sizeErrExists = True

            # by default set systematically velRefCode's value to something not None

            self._velRefCode = RadialVelocityReferenceCode.from_int(0)

            if row._velRefCodeExists:

                if row._velRefCode is not None:
                    self._velRefCode = row._velRefCode

                self._velRefCodeExists = True

            # by default set systematically dopplerVelocity's value to something not None

            if row._dopplerVelocityExists:

                # dopplerVelocity is a list, make a deep copy
                self._dopplerVelocity = copy.deepcopy(row._dopplerVelocity)

                self._dopplerVelocityExists = True

            # by default set systematically dopplerReferenceSystem's value to something not None

            self._dopplerReferenceSystem = RadialVelocityReferenceCode.from_int(0)

            if row._dopplerReferenceSystemExists:

                if row._dopplerReferenceSystem is not None:
                    self._dopplerReferenceSystem = row._dopplerReferenceSystem

                self._dopplerReferenceSystemExists = True

            # by default set systematically dopplerCalcType's value to something not None

            self._dopplerCalcType = DopplerReferenceCode.from_int(0)

            if row._dopplerCalcTypeExists:

                if row._dopplerCalcType is not None:
                    self._dopplerCalcType = row._dopplerCalcType

                self._dopplerCalcTypeExists = True

            # by default set systematically parallax's value to something not None

            if row._parallaxExists:

                # parallax is a list, make a deep copy
                self._parallax = copy.deepcopy(row._parallax)

                self._parallaxExists = True

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

        result += Parser.valueToXML("sourceId", self._sourceId)

        result += Parser.extendedValueToXML("timeInterval", self._timeInterval)

        result += Parser.valueToXML("code", self._code)

        result += Parser.listExtendedValueToXML("direction", self._direction)

        result += Parser.listExtendedValueToXML("properMotion", self._properMotion)

        result += Parser.valueToXML("sourceName", self._sourceName)

        if self._directionCodeExists:

            result += Parser.valueToXML(
                "directionCode", DirectionReferenceCode.name(self._directionCode)
            )

        if self._directionEquinoxExists:

            result += Parser.extendedValueToXML(
                "directionEquinox", self._directionEquinox
            )

        if self._calibrationGroupExists:

            result += Parser.valueToXML("calibrationGroup", self._calibrationGroup)

        if self._catalogExists:

            result += Parser.valueToXML("catalog", self._catalog)

        if self._deltaVelExists:

            result += Parser.extendedValueToXML("deltaVel", self._deltaVel)

        if self._positionExists:

            result += Parser.listExtendedValueToXML("position", self._position)

        if self._numLinesExists:

            result += Parser.valueToXML("numLines", self._numLines)

        if self._transitionExists:

            result += Parser.listValueToXML("transition", self._transition)

        if self._restFrequencyExists:

            result += Parser.listExtendedValueToXML(
                "restFrequency", self._restFrequency
            )

        if self._sysVelExists:

            result += Parser.listExtendedValueToXML("sysVel", self._sysVel)

        if self._rangeVelExists:

            result += Parser.listExtendedValueToXML("rangeVel", self._rangeVel)

        if self._sourceModelExists:

            result += Parser.valueToXML(
                "sourceModel", SourceModel.name(self._sourceModel)
            )

        if self._frequencyRefCodeExists:

            result += Parser.valueToXML(
                "frequencyRefCode", FrequencyReferenceCode.name(self._frequencyRefCode)
            )

        if self._numFreqExists:

            result += Parser.valueToXML("numFreq", self._numFreq)

        if self._numStokesExists:

            result += Parser.valueToXML("numStokes", self._numStokes)

        if self._frequencyExists:

            result += Parser.listExtendedValueToXML("frequency", self._frequency)

        if self._frequencyIntervalExists:

            result += Parser.listExtendedValueToXML(
                "frequencyInterval", self._frequencyInterval
            )

        if self._stokesParameterExists:

            result += Parser.listEnumValueToXML(
                "stokesParameter", self._stokesParameter
            )

        if self._fluxExists:

            result += Parser.listExtendedValueToXML("flux", self._flux)

        if self._fluxErrExists:

            result += Parser.listExtendedValueToXML("fluxErr", self._fluxErr)

        if self._positionAngleExists:

            result += Parser.listExtendedValueToXML(
                "positionAngle", self._positionAngle
            )

        if self._positionAngleErrExists:

            result += Parser.listExtendedValueToXML(
                "positionAngleErr", self._positionAngleErr
            )

        if self._sizeExists:

            result += Parser.listExtendedValueToXML("size", self._size)

        if self._sizeErrExists:

            result += Parser.listExtendedValueToXML("sizeErr", self._sizeErr)

        if self._velRefCodeExists:

            result += Parser.valueToXML(
                "velRefCode", RadialVelocityReferenceCode.name(self._velRefCode)
            )

        if self._dopplerVelocityExists:

            result += Parser.listExtendedValueToXML(
                "dopplerVelocity", self._dopplerVelocity
            )

        if self._dopplerReferenceSystemExists:

            result += Parser.valueToXML(
                "dopplerReferenceSystem",
                RadialVelocityReferenceCode.name(self._dopplerReferenceSystem),
            )

        if self._dopplerCalcTypeExists:

            result += Parser.valueToXML(
                "dopplerCalcType", DopplerReferenceCode.name(self._dopplerCalcType)
            )

        if self._parallaxExists:

            result += Parser.listExtendedValueToXML("parallax", self._parallax)

        # extrinsic attributes

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
                "xmlrow is not a string or a minidom.Element", "SourceTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "SourceTable")

        # intrinsic attribute values

        sourceIdNode = rowdom.getElementsByTagName("sourceId")[0]

        self._sourceId = int(sourceIdNode.firstChild.data.strip())

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        codeNode = rowdom.getElementsByTagName("code")[0]

        self._code = str(codeNode.firstChild.data.strip())

        directionNode = rowdom.getElementsByTagName("direction")[0]

        directionStr = directionNode.firstChild.data.strip()

        self._direction = Parser.stringListToLists(directionStr, Angle, "Source", True)

        properMotionNode = rowdom.getElementsByTagName("properMotion")[0]

        properMotionStr = properMotionNode.firstChild.data.strip()

        self._properMotion = Parser.stringListToLists(
            properMotionStr, AngularRate, "Source", True
        )

        sourceNameNode = rowdom.getElementsByTagName("sourceName")[0]

        self._sourceName = str(sourceNameNode.firstChild.data.strip())

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

        calibrationGroupNode = rowdom.getElementsByTagName("calibrationGroup")
        if len(calibrationGroupNode) > 0:

            self._calibrationGroup = int(
                calibrationGroupNode[0].firstChild.data.strip()
            )

            self._calibrationGroupExists = True

        catalogNode = rowdom.getElementsByTagName("catalog")
        if len(catalogNode) > 0:

            self._catalog = str(catalogNode[0].firstChild.data.strip())

            self._catalogExists = True

        deltaVelNode = rowdom.getElementsByTagName("deltaVel")
        if len(deltaVelNode) > 0:

            self._deltaVel = Speed(deltaVelNode[0].firstChild.data.strip())

            self._deltaVelExists = True

        positionNode = rowdom.getElementsByTagName("position")
        if len(positionNode) > 0:

            positionStr = positionNode[0].firstChild.data.strip()

            self._position = Parser.stringListToLists(
                positionStr, Length, "Source", True
            )

            self._positionExists = True

        numLinesNode = rowdom.getElementsByTagName("numLines")
        if len(numLinesNode) > 0:

            self._numLines = int(numLinesNode[0].firstChild.data.strip())

            self._numLinesExists = True

        transitionNode = rowdom.getElementsByTagName("transition")
        if len(transitionNode) > 0:

            transitionStr = transitionNode[0].firstChild.data.strip()

            self._transition = Parser.stringListToLists(
                transitionStr, str, "Source", False
            )

            self._transitionExists = True

        restFrequencyNode = rowdom.getElementsByTagName("restFrequency")
        if len(restFrequencyNode) > 0:

            restFrequencyStr = restFrequencyNode[0].firstChild.data.strip()

            self._restFrequency = Parser.stringListToLists(
                restFrequencyStr, Frequency, "Source", True
            )

            self._restFrequencyExists = True

        sysVelNode = rowdom.getElementsByTagName("sysVel")
        if len(sysVelNode) > 0:

            sysVelStr = sysVelNode[0].firstChild.data.strip()

            self._sysVel = Parser.stringListToLists(sysVelStr, Speed, "Source", True)

            self._sysVelExists = True

        rangeVelNode = rowdom.getElementsByTagName("rangeVel")
        if len(rangeVelNode) > 0:

            rangeVelStr = rangeVelNode[0].firstChild.data.strip()

            self._rangeVel = Parser.stringListToLists(
                rangeVelStr, Speed, "Source", True
            )

            self._rangeVelExists = True

        sourceModelNode = rowdom.getElementsByTagName("sourceModel")
        if len(sourceModelNode) > 0:

            self._sourceModel = SourceModel.newSourceModel(
                sourceModelNode[0].firstChild.data.strip()
            )

            self._sourceModelExists = True

        frequencyRefCodeNode = rowdom.getElementsByTagName("frequencyRefCode")
        if len(frequencyRefCodeNode) > 0:

            self._frequencyRefCode = FrequencyReferenceCode.newFrequencyReferenceCode(
                frequencyRefCodeNode[0].firstChild.data.strip()
            )

            self._frequencyRefCodeExists = True

        numFreqNode = rowdom.getElementsByTagName("numFreq")
        if len(numFreqNode) > 0:

            self._numFreq = int(numFreqNode[0].firstChild.data.strip())

            self._numFreqExists = True

        numStokesNode = rowdom.getElementsByTagName("numStokes")
        if len(numStokesNode) > 0:

            self._numStokes = int(numStokesNode[0].firstChild.data.strip())

            self._numStokesExists = True

        frequencyNode = rowdom.getElementsByTagName("frequency")
        if len(frequencyNode) > 0:

            frequencyStr = frequencyNode[0].firstChild.data.strip()

            self._frequency = Parser.stringListToLists(
                frequencyStr, Frequency, "Source", True
            )

            self._frequencyExists = True

        frequencyIntervalNode = rowdom.getElementsByTagName("frequencyInterval")
        if len(frequencyIntervalNode) > 0:

            frequencyIntervalStr = frequencyIntervalNode[0].firstChild.data.strip()

            self._frequencyInterval = Parser.stringListToLists(
                frequencyIntervalStr, Frequency, "Source", True
            )

            self._frequencyIntervalExists = True

        stokesParameterNode = rowdom.getElementsByTagName("stokesParameter")
        if len(stokesParameterNode) > 0:

            stokesParameterStr = stokesParameterNode[0].firstChild.data.strip()
            self._stokesParameter = Parser.stringListToLists(
                stokesParameterStr, StokesParameter, "Source", False
            )

            self._stokesParameterExists = True

        fluxNode = rowdom.getElementsByTagName("flux")
        if len(fluxNode) > 0:

            fluxStr = fluxNode[0].firstChild.data.strip()

            self._flux = Parser.stringListToLists(fluxStr, Flux, "Source", True)

            self._fluxExists = True

        fluxErrNode = rowdom.getElementsByTagName("fluxErr")
        if len(fluxErrNode) > 0:

            fluxErrStr = fluxErrNode[0].firstChild.data.strip()

            self._fluxErr = Parser.stringListToLists(fluxErrStr, Flux, "Source", True)

            self._fluxErrExists = True

        positionAngleNode = rowdom.getElementsByTagName("positionAngle")
        if len(positionAngleNode) > 0:

            positionAngleStr = positionAngleNode[0].firstChild.data.strip()

            self._positionAngle = Parser.stringListToLists(
                positionAngleStr, Angle, "Source", True
            )

            self._positionAngleExists = True

        positionAngleErrNode = rowdom.getElementsByTagName("positionAngleErr")
        if len(positionAngleErrNode) > 0:

            positionAngleErrStr = positionAngleErrNode[0].firstChild.data.strip()

            self._positionAngleErr = Parser.stringListToLists(
                positionAngleErrStr, Angle, "Source", True
            )

            self._positionAngleErrExists = True

        sizeNode = rowdom.getElementsByTagName("size")
        if len(sizeNode) > 0:

            sizeStr = sizeNode[0].firstChild.data.strip()

            self._size = Parser.stringListToLists(sizeStr, Angle, "Source", True)

            self._sizeExists = True

        sizeErrNode = rowdom.getElementsByTagName("sizeErr")
        if len(sizeErrNode) > 0:

            sizeErrStr = sizeErrNode[0].firstChild.data.strip()

            self._sizeErr = Parser.stringListToLists(sizeErrStr, Angle, "Source", True)

            self._sizeErrExists = True

        velRefCodeNode = rowdom.getElementsByTagName("velRefCode")
        if len(velRefCodeNode) > 0:

            self._velRefCode = (
                RadialVelocityReferenceCode.newRadialVelocityReferenceCode(
                    velRefCodeNode[0].firstChild.data.strip()
                )
            )

            self._velRefCodeExists = True

        dopplerVelocityNode = rowdom.getElementsByTagName("dopplerVelocity")
        if len(dopplerVelocityNode) > 0:

            dopplerVelocityStr = dopplerVelocityNode[0].firstChild.data.strip()

            self._dopplerVelocity = Parser.stringListToLists(
                dopplerVelocityStr, Speed, "Source", True
            )

            self._dopplerVelocityExists = True

        dopplerReferenceSystemNode = rowdom.getElementsByTagName(
            "dopplerReferenceSystem"
        )
        if len(dopplerReferenceSystemNode) > 0:

            self._dopplerReferenceSystem = (
                RadialVelocityReferenceCode.newRadialVelocityReferenceCode(
                    dopplerReferenceSystemNode[0].firstChild.data.strip()
                )
            )

            self._dopplerReferenceSystemExists = True

        dopplerCalcTypeNode = rowdom.getElementsByTagName("dopplerCalcType")
        if len(dopplerCalcTypeNode) > 0:

            self._dopplerCalcType = DopplerReferenceCode.newDopplerReferenceCode(
                dopplerCalcTypeNode[0].firstChild.data.strip()
            )

            self._dopplerCalcTypeExists = True

        parallaxNode = rowdom.getElementsByTagName("parallax")
        if len(parallaxNode) > 0:

            parallaxStr = parallaxNode[0].firstChild.data.strip()

            self._parallax = Parser.stringListToLists(
                parallaxStr, Angle, "Source", True
            )

            self._parallaxExists = True

        # extrinsic attribute values

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")[0]

        self._spectralWindowId = Tag(spectralWindowIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        eos.writeInt(self._sourceId)

        self._timeInterval.toBin(eos)

        self._spectralWindowId.toBin(eos)

        eos.writeStr(self._code)

        Angle.listToBin(self._direction, eos)

        AngularRate.listToBin(self._properMotion, eos)

        eos.writeStr(self._sourceName)

        eos.writeBool(self._directionCodeExists)
        if self._directionCodeExists:

            eos.writeString(str(self._directionCode))

        eos.writeBool(self._directionEquinoxExists)
        if self._directionEquinoxExists:

            self._directionEquinox.toBin(eos)

        eos.writeBool(self._calibrationGroupExists)
        if self._calibrationGroupExists:

            eos.writeInt(self._calibrationGroup)

        eos.writeBool(self._catalogExists)
        if self._catalogExists:

            eos.writeStr(self._catalog)

        eos.writeBool(self._deltaVelExists)
        if self._deltaVelExists:

            self._deltaVel.toBin(eos)

        eos.writeBool(self._positionExists)
        if self._positionExists:

            Length.listToBin(self._position, eos)

        eos.writeBool(self._numLinesExists)
        if self._numLinesExists:

            eos.writeInt(self._numLines)

        eos.writeBool(self._transitionExists)
        if self._transitionExists:

            eos.writeInt(len(self._transition))
            for i in range(len(self._transition)):

                eos.writeStr(self._transition[i])

        eos.writeBool(self._restFrequencyExists)
        if self._restFrequencyExists:

            Frequency.listToBin(self._restFrequency, eos)

        eos.writeBool(self._sysVelExists)
        if self._sysVelExists:

            Speed.listToBin(self._sysVel, eos)

        eos.writeBool(self._rangeVelExists)
        if self._rangeVelExists:

            Speed.listToBin(self._rangeVel, eos)

        eos.writeBool(self._sourceModelExists)
        if self._sourceModelExists:

            eos.writeString(str(self._sourceModel))

        eos.writeBool(self._frequencyRefCodeExists)
        if self._frequencyRefCodeExists:

            eos.writeString(str(self._frequencyRefCode))

        eos.writeBool(self._numFreqExists)
        if self._numFreqExists:

            eos.writeInt(self._numFreq)

        eos.writeBool(self._numStokesExists)
        if self._numStokesExists:

            eos.writeInt(self._numStokes)

        eos.writeBool(self._frequencyExists)
        if self._frequencyExists:

            Frequency.listToBin(self._frequency, eos)

        eos.writeBool(self._frequencyIntervalExists)
        if self._frequencyIntervalExists:

            Frequency.listToBin(self._frequencyInterval, eos)

        eos.writeBool(self._stokesParameterExists)
        if self._stokesParameterExists:

            eos.writeInt(len(self._stokesParameter))
            for i in range(len(self._stokesParameter)):

                eos.writeString(str(self._stokesParameter[i]))

        eos.writeBool(self._fluxExists)
        if self._fluxExists:

            Flux.listToBin(self._flux, eos)

        eos.writeBool(self._fluxErrExists)
        if self._fluxErrExists:

            Flux.listToBin(self._fluxErr, eos)

        eos.writeBool(self._positionAngleExists)
        if self._positionAngleExists:

            Angle.listToBin(self._positionAngle, eos)

        eos.writeBool(self._positionAngleErrExists)
        if self._positionAngleErrExists:

            Angle.listToBin(self._positionAngleErr, eos)

        eos.writeBool(self._sizeExists)
        if self._sizeExists:

            Angle.listToBin(self._size, eos)

        eos.writeBool(self._sizeErrExists)
        if self._sizeErrExists:

            Angle.listToBin(self._sizeErr, eos)

        eos.writeBool(self._velRefCodeExists)
        if self._velRefCodeExists:

            eos.writeString(str(self._velRefCode))

        eos.writeBool(self._dopplerVelocityExists)
        if self._dopplerVelocityExists:

            Speed.listToBin(self._dopplerVelocity, eos)

        eos.writeBool(self._dopplerReferenceSystemExists)
        if self._dopplerReferenceSystemExists:

            eos.writeString(str(self._dopplerReferenceSystem))

        eos.writeBool(self._dopplerCalcTypeExists)
        if self._dopplerCalcTypeExists:

            eos.writeString(str(self._dopplerCalcType))

        eos.writeBool(self._parallaxExists)
        if self._parallaxExists:

            Angle.listToBin(self._parallax, eos)

    @staticmethod
    def sourceIdFromBin(row, eis):
        """
        Set the sourceId in row from the EndianInput (eis) instance.
        """

        row._sourceId = eis.readInt()

    @staticmethod
    def timeIntervalFromBin(row, eis):
        """
        Set the timeInterval in row from the EndianInput (eis) instance.
        """

        row._timeInterval = ArrayTimeInterval.fromBin(eis)

    @staticmethod
    def spectralWindowIdFromBin(row, eis):
        """
        Set the spectralWindowId in row from the EndianInput (eis) instance.
        """

        row._spectralWindowId = Tag.fromBin(eis)

    @staticmethod
    def codeFromBin(row, eis):
        """
        Set the code in row from the EndianInput (eis) instance.
        """

        row._code = eis.readStr()

    @staticmethod
    def directionFromBin(row, eis):
        """
        Set the direction in row from the EndianInput (eis) instance.
        """

        row._direction = Angle.from1DBin(eis)

    @staticmethod
    def properMotionFromBin(row, eis):
        """
        Set the properMotion in row from the EndianInput (eis) instance.
        """

        row._properMotion = AngularRate.from1DBin(eis)

    @staticmethod
    def sourceNameFromBin(row, eis):
        """
        Set the sourceName in row from the EndianInput (eis) instance.
        """

        row._sourceName = eis.readStr()

    @staticmethod
    def directionCodeFromBin(row, eis):
        """
        Set the optional directionCode in row from the EndianInput (eis) instance.
        """
        row._directionCodeExists = eis.readBool()
        if row._directionCodeExists:

            row._directionCode = DirectionReferenceCode.literal(eis.readString())

    @staticmethod
    def directionEquinoxFromBin(row, eis):
        """
        Set the optional directionEquinox in row from the EndianInput (eis) instance.
        """
        row._directionEquinoxExists = eis.readBool()
        if row._directionEquinoxExists:

            row._directionEquinox = ArrayTime.fromBin(eis)

    @staticmethod
    def calibrationGroupFromBin(row, eis):
        """
        Set the optional calibrationGroup in row from the EndianInput (eis) instance.
        """
        row._calibrationGroupExists = eis.readBool()
        if row._calibrationGroupExists:

            row._calibrationGroup = eis.readInt()

    @staticmethod
    def catalogFromBin(row, eis):
        """
        Set the optional catalog in row from the EndianInput (eis) instance.
        """
        row._catalogExists = eis.readBool()
        if row._catalogExists:

            row._catalog = eis.readStr()

    @staticmethod
    def deltaVelFromBin(row, eis):
        """
        Set the optional deltaVel in row from the EndianInput (eis) instance.
        """
        row._deltaVelExists = eis.readBool()
        if row._deltaVelExists:

            row._deltaVel = Speed.fromBin(eis)

    @staticmethod
    def positionFromBin(row, eis):
        """
        Set the optional position in row from the EndianInput (eis) instance.
        """
        row._positionExists = eis.readBool()
        if row._positionExists:

            row._position = Length.from1DBin(eis)

    @staticmethod
    def numLinesFromBin(row, eis):
        """
        Set the optional numLines in row from the EndianInput (eis) instance.
        """
        row._numLinesExists = eis.readBool()
        if row._numLinesExists:

            row._numLines = eis.readInt()

    @staticmethod
    def transitionFromBin(row, eis):
        """
        Set the optional transition in row from the EndianInput (eis) instance.
        """
        row._transitionExists = eis.readBool()
        if row._transitionExists:

            transitionDim1 = eis.readInt()
            thisList = []
            for i in range(transitionDim1):
                thisValue = eis.readStr()
                thisList.append(thisValue)
            row._transition = thisList

    @staticmethod
    def restFrequencyFromBin(row, eis):
        """
        Set the optional restFrequency in row from the EndianInput (eis) instance.
        """
        row._restFrequencyExists = eis.readBool()
        if row._restFrequencyExists:

            row._restFrequency = Frequency.from1DBin(eis)

    @staticmethod
    def sysVelFromBin(row, eis):
        """
        Set the optional sysVel in row from the EndianInput (eis) instance.
        """
        row._sysVelExists = eis.readBool()
        if row._sysVelExists:

            row._sysVel = Speed.from1DBin(eis)

    @staticmethod
    def rangeVelFromBin(row, eis):
        """
        Set the optional rangeVel in row from the EndianInput (eis) instance.
        """
        row._rangeVelExists = eis.readBool()
        if row._rangeVelExists:

            row._rangeVel = Speed.from1DBin(eis)

    @staticmethod
    def sourceModelFromBin(row, eis):
        """
        Set the optional sourceModel in row from the EndianInput (eis) instance.
        """
        row._sourceModelExists = eis.readBool()
        if row._sourceModelExists:

            row._sourceModel = SourceModel.literal(eis.readString())

    @staticmethod
    def frequencyRefCodeFromBin(row, eis):
        """
        Set the optional frequencyRefCode in row from the EndianInput (eis) instance.
        """
        row._frequencyRefCodeExists = eis.readBool()
        if row._frequencyRefCodeExists:

            row._frequencyRefCode = FrequencyReferenceCode.literal(eis.readString())

    @staticmethod
    def numFreqFromBin(row, eis):
        """
        Set the optional numFreq in row from the EndianInput (eis) instance.
        """
        row._numFreqExists = eis.readBool()
        if row._numFreqExists:

            row._numFreq = eis.readInt()

    @staticmethod
    def numStokesFromBin(row, eis):
        """
        Set the optional numStokes in row from the EndianInput (eis) instance.
        """
        row._numStokesExists = eis.readBool()
        if row._numStokesExists:

            row._numStokes = eis.readInt()

    @staticmethod
    def frequencyFromBin(row, eis):
        """
        Set the optional frequency in row from the EndianInput (eis) instance.
        """
        row._frequencyExists = eis.readBool()
        if row._frequencyExists:

            row._frequency = Frequency.from1DBin(eis)

    @staticmethod
    def frequencyIntervalFromBin(row, eis):
        """
        Set the optional frequencyInterval in row from the EndianInput (eis) instance.
        """
        row._frequencyIntervalExists = eis.readBool()
        if row._frequencyIntervalExists:

            row._frequencyInterval = Frequency.from1DBin(eis)

    @staticmethod
    def stokesParameterFromBin(row, eis):
        """
        Set the optional stokesParameter in row from the EndianInput (eis) instance.
        """
        row._stokesParameterExists = eis.readBool()
        if row._stokesParameterExists:

            stokesParameterDim1 = eis.readInt()
            thisList = []
            for i in range(stokesParameterDim1):
                thisValue = StokesParameter.literal(eis.readString())
                thisList.append(thisValue)
            row._stokesParameter = thisList

    @staticmethod
    def fluxFromBin(row, eis):
        """
        Set the optional flux in row from the EndianInput (eis) instance.
        """
        row._fluxExists = eis.readBool()
        if row._fluxExists:

            row._flux = Flux.from2DBin(eis)

    @staticmethod
    def fluxErrFromBin(row, eis):
        """
        Set the optional fluxErr in row from the EndianInput (eis) instance.
        """
        row._fluxErrExists = eis.readBool()
        if row._fluxErrExists:

            row._fluxErr = Flux.from2DBin(eis)

    @staticmethod
    def positionAngleFromBin(row, eis):
        """
        Set the optional positionAngle in row from the EndianInput (eis) instance.
        """
        row._positionAngleExists = eis.readBool()
        if row._positionAngleExists:

            row._positionAngle = Angle.from1DBin(eis)

    @staticmethod
    def positionAngleErrFromBin(row, eis):
        """
        Set the optional positionAngleErr in row from the EndianInput (eis) instance.
        """
        row._positionAngleErrExists = eis.readBool()
        if row._positionAngleErrExists:

            row._positionAngleErr = Angle.from1DBin(eis)

    @staticmethod
    def sizeFromBin(row, eis):
        """
        Set the optional size in row from the EndianInput (eis) instance.
        """
        row._sizeExists = eis.readBool()
        if row._sizeExists:

            row._size = Angle.from2DBin(eis)

    @staticmethod
    def sizeErrFromBin(row, eis):
        """
        Set the optional sizeErr in row from the EndianInput (eis) instance.
        """
        row._sizeErrExists = eis.readBool()
        if row._sizeErrExists:

            row._sizeErr = Angle.from2DBin(eis)

    @staticmethod
    def velRefCodeFromBin(row, eis):
        """
        Set the optional velRefCode in row from the EndianInput (eis) instance.
        """
        row._velRefCodeExists = eis.readBool()
        if row._velRefCodeExists:

            row._velRefCode = RadialVelocityReferenceCode.literal(eis.readString())

    @staticmethod
    def dopplerVelocityFromBin(row, eis):
        """
        Set the optional dopplerVelocity in row from the EndianInput (eis) instance.
        """
        row._dopplerVelocityExists = eis.readBool()
        if row._dopplerVelocityExists:

            row._dopplerVelocity = Speed.from1DBin(eis)

    @staticmethod
    def dopplerReferenceSystemFromBin(row, eis):
        """
        Set the optional dopplerReferenceSystem in row from the EndianInput (eis) instance.
        """
        row._dopplerReferenceSystemExists = eis.readBool()
        if row._dopplerReferenceSystemExists:

            row._dopplerReferenceSystem = RadialVelocityReferenceCode.literal(
                eis.readString()
            )

    @staticmethod
    def dopplerCalcTypeFromBin(row, eis):
        """
        Set the optional dopplerCalcType in row from the EndianInput (eis) instance.
        """
        row._dopplerCalcTypeExists = eis.readBool()
        if row._dopplerCalcTypeExists:

            row._dopplerCalcType = DopplerReferenceCode.literal(eis.readString())

    @staticmethod
    def parallaxFromBin(row, eis):
        """
        Set the optional parallax in row from the EndianInput (eis) instance.
        """
        row._parallaxExists = eis.readBool()
        if row._parallaxExists:

            row._parallax = Angle.from1DBin(eis)

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["sourceId"] = SourceRow.sourceIdFromBin
        _fromBinMethods["timeInterval"] = SourceRow.timeIntervalFromBin
        _fromBinMethods["spectralWindowId"] = SourceRow.spectralWindowIdFromBin
        _fromBinMethods["code"] = SourceRow.codeFromBin
        _fromBinMethods["direction"] = SourceRow.directionFromBin
        _fromBinMethods["properMotion"] = SourceRow.properMotionFromBin
        _fromBinMethods["sourceName"] = SourceRow.sourceNameFromBin

        _fromBinMethods["directionCode"] = SourceRow.directionCodeFromBin
        _fromBinMethods["directionEquinox"] = SourceRow.directionEquinoxFromBin
        _fromBinMethods["calibrationGroup"] = SourceRow.calibrationGroupFromBin
        _fromBinMethods["catalog"] = SourceRow.catalogFromBin
        _fromBinMethods["deltaVel"] = SourceRow.deltaVelFromBin
        _fromBinMethods["position"] = SourceRow.positionFromBin
        _fromBinMethods["numLines"] = SourceRow.numLinesFromBin
        _fromBinMethods["transition"] = SourceRow.transitionFromBin
        _fromBinMethods["restFrequency"] = SourceRow.restFrequencyFromBin
        _fromBinMethods["sysVel"] = SourceRow.sysVelFromBin
        _fromBinMethods["rangeVel"] = SourceRow.rangeVelFromBin
        _fromBinMethods["sourceModel"] = SourceRow.sourceModelFromBin
        _fromBinMethods["frequencyRefCode"] = SourceRow.frequencyRefCodeFromBin
        _fromBinMethods["numFreq"] = SourceRow.numFreqFromBin
        _fromBinMethods["numStokes"] = SourceRow.numStokesFromBin
        _fromBinMethods["frequency"] = SourceRow.frequencyFromBin
        _fromBinMethods["frequencyInterval"] = SourceRow.frequencyIntervalFromBin
        _fromBinMethods["stokesParameter"] = SourceRow.stokesParameterFromBin
        _fromBinMethods["flux"] = SourceRow.fluxFromBin
        _fromBinMethods["fluxErr"] = SourceRow.fluxErrFromBin
        _fromBinMethods["positionAngle"] = SourceRow.positionAngleFromBin
        _fromBinMethods["positionAngleErr"] = SourceRow.positionAngleErrFromBin
        _fromBinMethods["size"] = SourceRow.sizeFromBin
        _fromBinMethods["sizeErr"] = SourceRow.sizeErrFromBin
        _fromBinMethods["velRefCode"] = SourceRow.velRefCodeFromBin
        _fromBinMethods["dopplerVelocity"] = SourceRow.dopplerVelocityFromBin
        _fromBinMethods["dopplerReferenceSystem"] = (
            SourceRow.dopplerReferenceSystemFromBin
        )
        _fromBinMethods["dopplerCalcType"] = SourceRow.dopplerCalcTypeFromBin
        _fromBinMethods["parallax"] = SourceRow.parallaxFromBin

    @staticmethod
    def fromBin(eis, table, attributesSeq):
        """
        Given an EndianInput instance by the table (which must be a Pointing instance) and
        the list of attributes to be found in eis, in order, this constructs a row by
        pulling off values from that EndianInput in the expected order.

        The new row object is returned.
        """
        global _fromBinMethods

        row = SourceRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " Source",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

    # ===> Attribute sourceId

    _sourceId = 0

    def getSourceId(self):
        """
        Get sourceId.
        return sourceId as int
        """

        return self._sourceId

    def setSourceId(self, sourceId):
        """
        Set sourceId with the specified int value.
        sourceId The int value to which sourceId is to be set.


        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the sourceId field, which is part of the key, after this row has been added to this table."
            )

        self._sourceId = int(sourceId)

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

    # ===> Attribute code

    _code = None

    def getCode(self):
        """
        Get code.
        return code as str
        """

        return self._code

    def setCode(self, code):
        """
        Set code with the specified str value.
        code The str value to which code is to be set.


        """

        self._code = str(code)

    # ===> Attribute direction

    _direction = None  # this is a 1D list of Angle

    def getDirection(self):
        """
        Get direction.
        return direction as Angle []
        """

        return copy.deepcopy(self._direction)

    def setDirection(self, direction):
        """
        Set direction with the specified Angle []  value.
        direction The Angle []  value to which direction is to be set.
        The value of direction can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(direction, list):
            raise ValueError("The value of direction must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(direction)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of direction is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(direction, Angle):
                raise ValueError(
                    "type of the first value in direction is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._direction = copy.deepcopy(direction)
        except Exception as exc:
            raise ValueError("Invalid direction : " + str(exc))

    # ===> Attribute properMotion

    _properMotion = None  # this is a 1D list of AngularRate

    def getProperMotion(self):
        """
        Get properMotion.
        return properMotion as AngularRate []
        """

        return copy.deepcopy(self._properMotion)

    def setProperMotion(self, properMotion):
        """
        Set properMotion with the specified AngularRate []  value.
        properMotion The AngularRate []  value to which properMotion is to be set.
        The value of properMotion can be anything allowed by the AngularRate []  constructor.

        """

        # value must be a list
        if not isinstance(properMotion, list):
            raise ValueError("The value of properMotion must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(properMotion)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of properMotion is not correct")

            # the type of the values in the list must be AngularRate
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(properMotion, AngularRate):
                raise ValueError(
                    "type of the first value in properMotion is not AngularRate as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._properMotion = copy.deepcopy(properMotion)
        except Exception as exc:
            raise ValueError("Invalid properMotion : " + str(exc))

    # ===> Attribute sourceName

    _sourceName = None

    def getSourceName(self):
        """
        Get sourceName.
        return sourceName as str
        """

        return self._sourceName

    def setSourceName(self, sourceName):
        """
        Set sourceName with the specified str value.
        sourceName The str value to which sourceName is to be set.


        """

        self._sourceName = str(sourceName)

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
                + " attribute in table Source does not exist!"
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
                + " attribute in table Source does not exist!"
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

    # ===> Attribute calibrationGroup, which is optional
    _calibrationGroupExists = False

    _calibrationGroup = 0

    def isCalibrationGroupExists(self):
        """
        The attribute calibrationGroup is optional. Return True if this attribute exists.
        return True if and only if the calibrationGroup attribute exists.
        """
        return self._calibrationGroupExists

    def getCalibrationGroup(self):
        """
        Get calibrationGroup, which is optional.
        return calibrationGroup as int
        raises ValueError If calibrationGroup does not exist.
        """
        if not self._calibrationGroupExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + calibrationGroup
                + " attribute in table Source does not exist!"
            )

        return self._calibrationGroup

    def setCalibrationGroup(self, calibrationGroup):
        """
        Set calibrationGroup with the specified int value.
        calibrationGroup The int value to which calibrationGroup is to be set.


        """

        self._calibrationGroup = int(calibrationGroup)

        self._calibrationGroupExists = True

    def clearCalibrationGroup(self):
        """
        Mark calibrationGroup, which is an optional field, as non-existent.
        """
        self._calibrationGroupExists = False

    # ===> Attribute catalog, which is optional
    _catalogExists = False

    _catalog = None

    def isCatalogExists(self):
        """
        The attribute catalog is optional. Return True if this attribute exists.
        return True if and only if the catalog attribute exists.
        """
        return self._catalogExists

    def getCatalog(self):
        """
        Get catalog, which is optional.
        return catalog as str
        raises ValueError If catalog does not exist.
        """
        if not self._catalogExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + catalog
                + " attribute in table Source does not exist!"
            )

        return self._catalog

    def setCatalog(self, catalog):
        """
        Set catalog with the specified str value.
        catalog The str value to which catalog is to be set.


        """

        self._catalog = str(catalog)

        self._catalogExists = True

    def clearCatalog(self):
        """
        Mark catalog, which is an optional field, as non-existent.
        """
        self._catalogExists = False

    # ===> Attribute deltaVel, which is optional
    _deltaVelExists = False

    _deltaVel = Speed()

    def isDeltaVelExists(self):
        """
        The attribute deltaVel is optional. Return True if this attribute exists.
        return True if and only if the deltaVel attribute exists.
        """
        return self._deltaVelExists

    def getDeltaVel(self):
        """
        Get deltaVel, which is optional.
        return deltaVel as Speed
        raises ValueError If deltaVel does not exist.
        """
        if not self._deltaVelExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + deltaVel
                + " attribute in table Source does not exist!"
            )

        # make sure it is a copy of Speed
        return Speed(self._deltaVel)

    def setDeltaVel(self, deltaVel):
        """
        Set deltaVel with the specified Speed value.
        deltaVel The Speed value to which deltaVel is to be set.
        The value of deltaVel can be anything allowed by the Speed constructor.

        """

        self._deltaVel = Speed(deltaVel)

        self._deltaVelExists = True

    def clearDeltaVel(self):
        """
        Mark deltaVel, which is an optional field, as non-existent.
        """
        self._deltaVelExists = False

    # ===> Attribute position, which is optional
    _positionExists = False

    _position = None  # this is a 1D list of Length

    def isPositionExists(self):
        """
        The attribute position is optional. Return True if this attribute exists.
        return True if and only if the position attribute exists.
        """
        return self._positionExists

    def getPosition(self):
        """
        Get position, which is optional.
        return position as Length []
        raises ValueError If position does not exist.
        """
        if not self._positionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + position
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._position)

    def setPosition(self, position):
        """
        Set position with the specified Length []  value.
        position The Length []  value to which position is to be set.
        The value of position can be anything allowed by the Length []  constructor.

        """

        # value must be a list
        if not isinstance(position, list):
            raise ValueError("The value of position must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(position)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of position is not correct")

            # the type of the values in the list must be Length
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(position, Length):
                raise ValueError(
                    "type of the first value in position is not Length as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._position = copy.deepcopy(position)
        except Exception as exc:
            raise ValueError("Invalid position : " + str(exc))

        self._positionExists = True

    def clearPosition(self):
        """
        Mark position, which is an optional field, as non-existent.
        """
        self._positionExists = False

    # ===> Attribute numLines, which is optional
    _numLinesExists = False

    _numLines = 0

    def isNumLinesExists(self):
        """
        The attribute numLines is optional. Return True if this attribute exists.
        return True if and only if the numLines attribute exists.
        """
        return self._numLinesExists

    def getNumLines(self):
        """
        Get numLines, which is optional.
        return numLines as int
        raises ValueError If numLines does not exist.
        """
        if not self._numLinesExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numLines
                + " attribute in table Source does not exist!"
            )

        return self._numLines

    def setNumLines(self, numLines):
        """
        Set numLines with the specified int value.
        numLines The int value to which numLines is to be set.


        """

        self._numLines = int(numLines)

        self._numLinesExists = True

    def clearNumLines(self):
        """
        Mark numLines, which is an optional field, as non-existent.
        """
        self._numLinesExists = False

    # ===> Attribute transition, which is optional
    _transitionExists = False

    _transition = None  # this is a 1D list of str

    def isTransitionExists(self):
        """
        The attribute transition is optional. Return True if this attribute exists.
        return True if and only if the transition attribute exists.
        """
        return self._transitionExists

    def getTransition(self):
        """
        Get transition, which is optional.
        return transition as str []
        raises ValueError If transition does not exist.
        """
        if not self._transitionExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + transition
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._transition)

    def setTransition(self, transition):
        """
        Set transition with the specified str []  value.
        transition The str []  value to which transition is to be set.


        """

        # value must be a list
        if not isinstance(transition, list):
            raise ValueError("The value of transition must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(transition)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of transition is not correct")

            # the type of the values in the list must be str
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(transition, str):
                raise ValueError(
                    "type of the first value in transition is not str as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._transition = copy.deepcopy(transition)
        except Exception as exc:
            raise ValueError("Invalid transition : " + str(exc))

        self._transitionExists = True

    def clearTransition(self):
        """
        Mark transition, which is an optional field, as non-existent.
        """
        self._transitionExists = False

    # ===> Attribute restFrequency, which is optional
    _restFrequencyExists = False

    _restFrequency = None  # this is a 1D list of Frequency

    def isRestFrequencyExists(self):
        """
        The attribute restFrequency is optional. Return True if this attribute exists.
        return True if and only if the restFrequency attribute exists.
        """
        return self._restFrequencyExists

    def getRestFrequency(self):
        """
        Get restFrequency, which is optional.
        return restFrequency as Frequency []
        raises ValueError If restFrequency does not exist.
        """
        if not self._restFrequencyExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + restFrequency
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._restFrequency)

    def setRestFrequency(self, restFrequency):
        """
        Set restFrequency with the specified Frequency []  value.
        restFrequency The Frequency []  value to which restFrequency is to be set.
        The value of restFrequency can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(restFrequency, list):
            raise ValueError("The value of restFrequency must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(restFrequency)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of restFrequency is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(restFrequency, Frequency):
                raise ValueError(
                    "type of the first value in restFrequency is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._restFrequency = copy.deepcopy(restFrequency)
        except Exception as exc:
            raise ValueError("Invalid restFrequency : " + str(exc))

        self._restFrequencyExists = True

    def clearRestFrequency(self):
        """
        Mark restFrequency, which is an optional field, as non-existent.
        """
        self._restFrequencyExists = False

    # ===> Attribute sysVel, which is optional
    _sysVelExists = False

    _sysVel = None  # this is a 1D list of Speed

    def isSysVelExists(self):
        """
        The attribute sysVel is optional. Return True if this attribute exists.
        return True if and only if the sysVel attribute exists.
        """
        return self._sysVelExists

    def getSysVel(self):
        """
        Get sysVel, which is optional.
        return sysVel as Speed []
        raises ValueError If sysVel does not exist.
        """
        if not self._sysVelExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sysVel
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._sysVel)

    def setSysVel(self, sysVel):
        """
        Set sysVel with the specified Speed []  value.
        sysVel The Speed []  value to which sysVel is to be set.
        The value of sysVel can be anything allowed by the Speed []  constructor.

        """

        # value must be a list
        if not isinstance(sysVel, list):
            raise ValueError("The value of sysVel must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(sysVel)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of sysVel is not correct")

            # the type of the values in the list must be Speed
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(sysVel, Speed):
                raise ValueError(
                    "type of the first value in sysVel is not Speed as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._sysVel = copy.deepcopy(sysVel)
        except Exception as exc:
            raise ValueError("Invalid sysVel : " + str(exc))

        self._sysVelExists = True

    def clearSysVel(self):
        """
        Mark sysVel, which is an optional field, as non-existent.
        """
        self._sysVelExists = False

    # ===> Attribute rangeVel, which is optional
    _rangeVelExists = False

    _rangeVel = None  # this is a 1D list of Speed

    def isRangeVelExists(self):
        """
        The attribute rangeVel is optional. Return True if this attribute exists.
        return True if and only if the rangeVel attribute exists.
        """
        return self._rangeVelExists

    def getRangeVel(self):
        """
        Get rangeVel, which is optional.
        return rangeVel as Speed []
        raises ValueError If rangeVel does not exist.
        """
        if not self._rangeVelExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + rangeVel
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._rangeVel)

    def setRangeVel(self, rangeVel):
        """
        Set rangeVel with the specified Speed []  value.
        rangeVel The Speed []  value to which rangeVel is to be set.
        The value of rangeVel can be anything allowed by the Speed []  constructor.

        """

        # value must be a list
        if not isinstance(rangeVel, list):
            raise ValueError("The value of rangeVel must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(rangeVel)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of rangeVel is not correct")

            # the type of the values in the list must be Speed
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(rangeVel, Speed):
                raise ValueError(
                    "type of the first value in rangeVel is not Speed as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._rangeVel = copy.deepcopy(rangeVel)
        except Exception as exc:
            raise ValueError("Invalid rangeVel : " + str(exc))

        self._rangeVelExists = True

    def clearRangeVel(self):
        """
        Mark rangeVel, which is an optional field, as non-existent.
        """
        self._rangeVelExists = False

    # ===> Attribute sourceModel, which is optional
    _sourceModelExists = False

    _sourceModel = SourceModel.from_int(0)

    def isSourceModelExists(self):
        """
        The attribute sourceModel is optional. Return True if this attribute exists.
        return True if and only if the sourceModel attribute exists.
        """
        return self._sourceModelExists

    def getSourceModel(self):
        """
        Get sourceModel, which is optional.
        return sourceModel as SourceModel
        raises ValueError If sourceModel does not exist.
        """
        if not self._sourceModelExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sourceModel
                + " attribute in table Source does not exist!"
            )

        return self._sourceModel

    def setSourceModel(self, sourceModel):
        """
        Set sourceModel with the specified SourceModel value.
        sourceModel The SourceModel value to which sourceModel is to be set.


        """

        self._sourceModel = SourceModel(sourceModel)

        self._sourceModelExists = True

    def clearSourceModel(self):
        """
        Mark sourceModel, which is an optional field, as non-existent.
        """
        self._sourceModelExists = False

    # ===> Attribute frequencyRefCode, which is optional
    _frequencyRefCodeExists = False

    _frequencyRefCode = FrequencyReferenceCode.from_int(0)

    def isFrequencyRefCodeExists(self):
        """
        The attribute frequencyRefCode is optional. Return True if this attribute exists.
        return True if and only if the frequencyRefCode attribute exists.
        """
        return self._frequencyRefCodeExists

    def getFrequencyRefCode(self):
        """
        Get frequencyRefCode, which is optional.
        return frequencyRefCode as FrequencyReferenceCode
        raises ValueError If frequencyRefCode does not exist.
        """
        if not self._frequencyRefCodeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + frequencyRefCode
                + " attribute in table Source does not exist!"
            )

        return self._frequencyRefCode

    def setFrequencyRefCode(self, frequencyRefCode):
        """
        Set frequencyRefCode with the specified FrequencyReferenceCode value.
        frequencyRefCode The FrequencyReferenceCode value to which frequencyRefCode is to be set.


        """

        self._frequencyRefCode = FrequencyReferenceCode(frequencyRefCode)

        self._frequencyRefCodeExists = True

    def clearFrequencyRefCode(self):
        """
        Mark frequencyRefCode, which is an optional field, as non-existent.
        """
        self._frequencyRefCodeExists = False

    # ===> Attribute numFreq, which is optional
    _numFreqExists = False

    _numFreq = 0

    def isNumFreqExists(self):
        """
        The attribute numFreq is optional. Return True if this attribute exists.
        return True if and only if the numFreq attribute exists.
        """
        return self._numFreqExists

    def getNumFreq(self):
        """
        Get numFreq, which is optional.
        return numFreq as int
        raises ValueError If numFreq does not exist.
        """
        if not self._numFreqExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numFreq
                + " attribute in table Source does not exist!"
            )

        return self._numFreq

    def setNumFreq(self, numFreq):
        """
        Set numFreq with the specified int value.
        numFreq The int value to which numFreq is to be set.


        """

        self._numFreq = int(numFreq)

        self._numFreqExists = True

    def clearNumFreq(self):
        """
        Mark numFreq, which is an optional field, as non-existent.
        """
        self._numFreqExists = False

    # ===> Attribute numStokes, which is optional
    _numStokesExists = False

    _numStokes = 0

    def isNumStokesExists(self):
        """
        The attribute numStokes is optional. Return True if this attribute exists.
        return True if and only if the numStokes attribute exists.
        """
        return self._numStokesExists

    def getNumStokes(self):
        """
        Get numStokes, which is optional.
        return numStokes as int
        raises ValueError If numStokes does not exist.
        """
        if not self._numStokesExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numStokes
                + " attribute in table Source does not exist!"
            )

        return self._numStokes

    def setNumStokes(self, numStokes):
        """
        Set numStokes with the specified int value.
        numStokes The int value to which numStokes is to be set.


        """

        self._numStokes = int(numStokes)

        self._numStokesExists = True

    def clearNumStokes(self):
        """
        Mark numStokes, which is an optional field, as non-existent.
        """
        self._numStokesExists = False

    # ===> Attribute frequency, which is optional
    _frequencyExists = False

    _frequency = None  # this is a 1D list of Frequency

    def isFrequencyExists(self):
        """
        The attribute frequency is optional. Return True if this attribute exists.
        return True if and only if the frequency attribute exists.
        """
        return self._frequencyExists

    def getFrequency(self):
        """
        Get frequency, which is optional.
        return frequency as Frequency []
        raises ValueError If frequency does not exist.
        """
        if not self._frequencyExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + frequency
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._frequency)

    def setFrequency(self, frequency):
        """
        Set frequency with the specified Frequency []  value.
        frequency The Frequency []  value to which frequency is to be set.
        The value of frequency can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(frequency, list):
            raise ValueError("The value of frequency must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(frequency)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of frequency is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(frequency, Frequency):
                raise ValueError(
                    "type of the first value in frequency is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._frequency = copy.deepcopy(frequency)
        except Exception as exc:
            raise ValueError("Invalid frequency : " + str(exc))

        self._frequencyExists = True

    def clearFrequency(self):
        """
        Mark frequency, which is an optional field, as non-existent.
        """
        self._frequencyExists = False

    # ===> Attribute frequencyInterval, which is optional
    _frequencyIntervalExists = False

    _frequencyInterval = None  # this is a 1D list of Frequency

    def isFrequencyIntervalExists(self):
        """
        The attribute frequencyInterval is optional. Return True if this attribute exists.
        return True if and only if the frequencyInterval attribute exists.
        """
        return self._frequencyIntervalExists

    def getFrequencyInterval(self):
        """
        Get frequencyInterval, which is optional.
        return frequencyInterval as Frequency []
        raises ValueError If frequencyInterval does not exist.
        """
        if not self._frequencyIntervalExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + frequencyInterval
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._frequencyInterval)

    def setFrequencyInterval(self, frequencyInterval):
        """
        Set frequencyInterval with the specified Frequency []  value.
        frequencyInterval The Frequency []  value to which frequencyInterval is to be set.
        The value of frequencyInterval can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(frequencyInterval, list):
            raise ValueError("The value of frequencyInterval must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(frequencyInterval)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of frequencyInterval is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(frequencyInterval, Frequency):
                raise ValueError(
                    "type of the first value in frequencyInterval is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._frequencyInterval = copy.deepcopy(frequencyInterval)
        except Exception as exc:
            raise ValueError("Invalid frequencyInterval : " + str(exc))

        self._frequencyIntervalExists = True

    def clearFrequencyInterval(self):
        """
        Mark frequencyInterval, which is an optional field, as non-existent.
        """
        self._frequencyIntervalExists = False

    # ===> Attribute stokesParameter, which is optional
    _stokesParameterExists = False

    _stokesParameter = None  # this is a 1D list of StokesParameter

    def isStokesParameterExists(self):
        """
        The attribute stokesParameter is optional. Return True if this attribute exists.
        return True if and only if the stokesParameter attribute exists.
        """
        return self._stokesParameterExists

    def getStokesParameter(self):
        """
        Get stokesParameter, which is optional.
        return stokesParameter as StokesParameter []
        raises ValueError If stokesParameter does not exist.
        """
        if not self._stokesParameterExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + stokesParameter
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._stokesParameter)

    def setStokesParameter(self, stokesParameter):
        """
        Set stokesParameter with the specified StokesParameter []  value.
        stokesParameter The StokesParameter []  value to which stokesParameter is to be set.


        """

        # value must be a list
        if not isinstance(stokesParameter, list):
            raise ValueError("The value of stokesParameter must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(stokesParameter)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of stokesParameter is not correct")

            # the type of the values in the list must be StokesParameter
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(stokesParameter, StokesParameter):
                raise ValueError(
                    "type of the first value in stokesParameter is not StokesParameter as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._stokesParameter = copy.deepcopy(stokesParameter)
        except Exception as exc:
            raise ValueError("Invalid stokesParameter : " + str(exc))

        self._stokesParameterExists = True

    def clearStokesParameter(self):
        """
        Mark stokesParameter, which is an optional field, as non-existent.
        """
        self._stokesParameterExists = False

    # ===> Attribute flux, which is optional
    _fluxExists = False

    _flux = None  # this is a 2D list of Flux

    def isFluxExists(self):
        """
        The attribute flux is optional. Return True if this attribute exists.
        return True if and only if the flux attribute exists.
        """
        return self._fluxExists

    def getFlux(self):
        """
        Get flux, which is optional.
        return flux as Flux []  []
        raises ValueError If flux does not exist.
        """
        if not self._fluxExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + flux
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._flux)

    def setFlux(self, flux):
        """
        Set flux with the specified Flux []  []  value.
        flux The Flux []  []  value to which flux is to be set.
        The value of flux can be anything allowed by the Flux []  []  constructor.

        """

        # value must be a list
        if not isinstance(flux, list):
            raise ValueError("The value of flux must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(flux)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of flux is not correct")

            # the type of the values in the list must be Flux
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(flux, Flux):
                raise ValueError(
                    "type of the first value in flux is not Flux as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._flux = copy.deepcopy(flux)
        except Exception as exc:
            raise ValueError("Invalid flux : " + str(exc))

        self._fluxExists = True

    def clearFlux(self):
        """
        Mark flux, which is an optional field, as non-existent.
        """
        self._fluxExists = False

    # ===> Attribute fluxErr, which is optional
    _fluxErrExists = False

    _fluxErr = None  # this is a 2D list of Flux

    def isFluxErrExists(self):
        """
        The attribute fluxErr is optional. Return True if this attribute exists.
        return True if and only if the fluxErr attribute exists.
        """
        return self._fluxErrExists

    def getFluxErr(self):
        """
        Get fluxErr, which is optional.
        return fluxErr as Flux []  []
        raises ValueError If fluxErr does not exist.
        """
        if not self._fluxErrExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + fluxErr
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._fluxErr)

    def setFluxErr(self, fluxErr):
        """
        Set fluxErr with the specified Flux []  []  value.
        fluxErr The Flux []  []  value to which fluxErr is to be set.
        The value of fluxErr can be anything allowed by the Flux []  []  constructor.

        """

        # value must be a list
        if not isinstance(fluxErr, list):
            raise ValueError("The value of fluxErr must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(fluxErr)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of fluxErr is not correct")

            # the type of the values in the list must be Flux
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(fluxErr, Flux):
                raise ValueError(
                    "type of the first value in fluxErr is not Flux as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._fluxErr = copy.deepcopy(fluxErr)
        except Exception as exc:
            raise ValueError("Invalid fluxErr : " + str(exc))

        self._fluxErrExists = True

    def clearFluxErr(self):
        """
        Mark fluxErr, which is an optional field, as non-existent.
        """
        self._fluxErrExists = False

    # ===> Attribute positionAngle, which is optional
    _positionAngleExists = False

    _positionAngle = None  # this is a 1D list of Angle

    def isPositionAngleExists(self):
        """
        The attribute positionAngle is optional. Return True if this attribute exists.
        return True if and only if the positionAngle attribute exists.
        """
        return self._positionAngleExists

    def getPositionAngle(self):
        """
        Get positionAngle, which is optional.
        return positionAngle as Angle []
        raises ValueError If positionAngle does not exist.
        """
        if not self._positionAngleExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + positionAngle
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._positionAngle)

    def setPositionAngle(self, positionAngle):
        """
        Set positionAngle with the specified Angle []  value.
        positionAngle The Angle []  value to which positionAngle is to be set.
        The value of positionAngle can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(positionAngle, list):
            raise ValueError("The value of positionAngle must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(positionAngle)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of positionAngle is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(positionAngle, Angle):
                raise ValueError(
                    "type of the first value in positionAngle is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._positionAngle = copy.deepcopy(positionAngle)
        except Exception as exc:
            raise ValueError("Invalid positionAngle : " + str(exc))

        self._positionAngleExists = True

    def clearPositionAngle(self):
        """
        Mark positionAngle, which is an optional field, as non-existent.
        """
        self._positionAngleExists = False

    # ===> Attribute positionAngleErr, which is optional
    _positionAngleErrExists = False

    _positionAngleErr = None  # this is a 1D list of Angle

    def isPositionAngleErrExists(self):
        """
        The attribute positionAngleErr is optional. Return True if this attribute exists.
        return True if and only if the positionAngleErr attribute exists.
        """
        return self._positionAngleErrExists

    def getPositionAngleErr(self):
        """
        Get positionAngleErr, which is optional.
        return positionAngleErr as Angle []
        raises ValueError If positionAngleErr does not exist.
        """
        if not self._positionAngleErrExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + positionAngleErr
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._positionAngleErr)

    def setPositionAngleErr(self, positionAngleErr):
        """
        Set positionAngleErr with the specified Angle []  value.
        positionAngleErr The Angle []  value to which positionAngleErr is to be set.
        The value of positionAngleErr can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(positionAngleErr, list):
            raise ValueError("The value of positionAngleErr must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(positionAngleErr)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of positionAngleErr is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(positionAngleErr, Angle):
                raise ValueError(
                    "type of the first value in positionAngleErr is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._positionAngleErr = copy.deepcopy(positionAngleErr)
        except Exception as exc:
            raise ValueError("Invalid positionAngleErr : " + str(exc))

        self._positionAngleErrExists = True

    def clearPositionAngleErr(self):
        """
        Mark positionAngleErr, which is an optional field, as non-existent.
        """
        self._positionAngleErrExists = False

    # ===> Attribute size, which is optional
    _sizeExists = False

    _size = None  # this is a 2D list of Angle

    def isSizeExists(self):
        """
        The attribute size is optional. Return True if this attribute exists.
        return True if and only if the size attribute exists.
        """
        return self._sizeExists

    def getSize(self):
        """
        Get size, which is optional.
        return size as Angle []  []
        raises ValueError If size does not exist.
        """
        if not self._sizeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + size
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._size)

    def setSize(self, size):
        """
        Set size with the specified Angle []  []  value.
        size The Angle []  []  value to which size is to be set.
        The value of size can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(size, list):
            raise ValueError("The value of size must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(size)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of size is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(size, Angle):
                raise ValueError(
                    "type of the first value in size is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._size = copy.deepcopy(size)
        except Exception as exc:
            raise ValueError("Invalid size : " + str(exc))

        self._sizeExists = True

    def clearSize(self):
        """
        Mark size, which is an optional field, as non-existent.
        """
        self._sizeExists = False

    # ===> Attribute sizeErr, which is optional
    _sizeErrExists = False

    _sizeErr = None  # this is a 2D list of Angle

    def isSizeErrExists(self):
        """
        The attribute sizeErr is optional. Return True if this attribute exists.
        return True if and only if the sizeErr attribute exists.
        """
        return self._sizeErrExists

    def getSizeErr(self):
        """
        Get sizeErr, which is optional.
        return sizeErr as Angle []  []
        raises ValueError If sizeErr does not exist.
        """
        if not self._sizeErrExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + sizeErr
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._sizeErr)

    def setSizeErr(self, sizeErr):
        """
        Set sizeErr with the specified Angle []  []  value.
        sizeErr The Angle []  []  value to which sizeErr is to be set.
        The value of sizeErr can be anything allowed by the Angle []  []  constructor.

        """

        # value must be a list
        if not isinstance(sizeErr, list):
            raise ValueError("The value of sizeErr must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(sizeErr)

            shapeOK = len(listDims) == 2

            if not shapeOK:
                raise ValueError("shape of sizeErr is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(sizeErr, Angle):
                raise ValueError(
                    "type of the first value in sizeErr is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._sizeErr = copy.deepcopy(sizeErr)
        except Exception as exc:
            raise ValueError("Invalid sizeErr : " + str(exc))

        self._sizeErrExists = True

    def clearSizeErr(self):
        """
        Mark sizeErr, which is an optional field, as non-existent.
        """
        self._sizeErrExists = False

    # ===> Attribute velRefCode, which is optional
    _velRefCodeExists = False

    _velRefCode = RadialVelocityReferenceCode.from_int(0)

    def isVelRefCodeExists(self):
        """
        The attribute velRefCode is optional. Return True if this attribute exists.
        return True if and only if the velRefCode attribute exists.
        """
        return self._velRefCodeExists

    def getVelRefCode(self):
        """
        Get velRefCode, which is optional.
        return velRefCode as RadialVelocityReferenceCode
        raises ValueError If velRefCode does not exist.
        """
        if not self._velRefCodeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + velRefCode
                + " attribute in table Source does not exist!"
            )

        return self._velRefCode

    def setVelRefCode(self, velRefCode):
        """
        Set velRefCode with the specified RadialVelocityReferenceCode value.
        velRefCode The RadialVelocityReferenceCode value to which velRefCode is to be set.


        """

        self._velRefCode = RadialVelocityReferenceCode(velRefCode)

        self._velRefCodeExists = True

    def clearVelRefCode(self):
        """
        Mark velRefCode, which is an optional field, as non-existent.
        """
        self._velRefCodeExists = False

    # ===> Attribute dopplerVelocity, which is optional
    _dopplerVelocityExists = False

    _dopplerVelocity = None  # this is a 1D list of Speed

    def isDopplerVelocityExists(self):
        """
        The attribute dopplerVelocity is optional. Return True if this attribute exists.
        return True if and only if the dopplerVelocity attribute exists.
        """
        return self._dopplerVelocityExists

    def getDopplerVelocity(self):
        """
        Get dopplerVelocity, which is optional.
        return dopplerVelocity as Speed []
        raises ValueError If dopplerVelocity does not exist.
        """
        if not self._dopplerVelocityExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + dopplerVelocity
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._dopplerVelocity)

    def setDopplerVelocity(self, dopplerVelocity):
        """
        Set dopplerVelocity with the specified Speed []  value.
        dopplerVelocity The Speed []  value to which dopplerVelocity is to be set.
        The value of dopplerVelocity can be anything allowed by the Speed []  constructor.

        """

        # value must be a list
        if not isinstance(dopplerVelocity, list):
            raise ValueError("The value of dopplerVelocity must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(dopplerVelocity)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of dopplerVelocity is not correct")

            # the type of the values in the list must be Speed
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(dopplerVelocity, Speed):
                raise ValueError(
                    "type of the first value in dopplerVelocity is not Speed as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._dopplerVelocity = copy.deepcopy(dopplerVelocity)
        except Exception as exc:
            raise ValueError("Invalid dopplerVelocity : " + str(exc))

        self._dopplerVelocityExists = True

    def clearDopplerVelocity(self):
        """
        Mark dopplerVelocity, which is an optional field, as non-existent.
        """
        self._dopplerVelocityExists = False

    # ===> Attribute dopplerReferenceSystem, which is optional
    _dopplerReferenceSystemExists = False

    _dopplerReferenceSystem = RadialVelocityReferenceCode.from_int(0)

    def isDopplerReferenceSystemExists(self):
        """
        The attribute dopplerReferenceSystem is optional. Return True if this attribute exists.
        return True if and only if the dopplerReferenceSystem attribute exists.
        """
        return self._dopplerReferenceSystemExists

    def getDopplerReferenceSystem(self):
        """
        Get dopplerReferenceSystem, which is optional.
        return dopplerReferenceSystem as RadialVelocityReferenceCode
        raises ValueError If dopplerReferenceSystem does not exist.
        """
        if not self._dopplerReferenceSystemExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + dopplerReferenceSystem
                + " attribute in table Source does not exist!"
            )

        return self._dopplerReferenceSystem

    def setDopplerReferenceSystem(self, dopplerReferenceSystem):
        """
        Set dopplerReferenceSystem with the specified RadialVelocityReferenceCode value.
        dopplerReferenceSystem The RadialVelocityReferenceCode value to which dopplerReferenceSystem is to be set.


        """

        self._dopplerReferenceSystem = RadialVelocityReferenceCode(
            dopplerReferenceSystem
        )

        self._dopplerReferenceSystemExists = True

    def clearDopplerReferenceSystem(self):
        """
        Mark dopplerReferenceSystem, which is an optional field, as non-existent.
        """
        self._dopplerReferenceSystemExists = False

    # ===> Attribute dopplerCalcType, which is optional
    _dopplerCalcTypeExists = False

    _dopplerCalcType = DopplerReferenceCode.from_int(0)

    def isDopplerCalcTypeExists(self):
        """
        The attribute dopplerCalcType is optional. Return True if this attribute exists.
        return True if and only if the dopplerCalcType attribute exists.
        """
        return self._dopplerCalcTypeExists

    def getDopplerCalcType(self):
        """
        Get dopplerCalcType, which is optional.
        return dopplerCalcType as DopplerReferenceCode
        raises ValueError If dopplerCalcType does not exist.
        """
        if not self._dopplerCalcTypeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + dopplerCalcType
                + " attribute in table Source does not exist!"
            )

        return self._dopplerCalcType

    def setDopplerCalcType(self, dopplerCalcType):
        """
        Set dopplerCalcType with the specified DopplerReferenceCode value.
        dopplerCalcType The DopplerReferenceCode value to which dopplerCalcType is to be set.


        """

        self._dopplerCalcType = DopplerReferenceCode(dopplerCalcType)

        self._dopplerCalcTypeExists = True

    def clearDopplerCalcType(self):
        """
        Mark dopplerCalcType, which is an optional field, as non-existent.
        """
        self._dopplerCalcTypeExists = False

    # ===> Attribute parallax, which is optional
    _parallaxExists = False

    _parallax = None  # this is a 1D list of Angle

    def isParallaxExists(self):
        """
        The attribute parallax is optional. Return True if this attribute exists.
        return True if and only if the parallax attribute exists.
        """
        return self._parallaxExists

    def getParallax(self):
        """
        Get parallax, which is optional.
        return parallax as Angle []
        raises ValueError If parallax does not exist.
        """
        if not self._parallaxExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + parallax
                + " attribute in table Source does not exist!"
            )

        return copy.deepcopy(self._parallax)

    def setParallax(self, parallax):
        """
        Set parallax with the specified Angle []  value.
        parallax The Angle []  value to which parallax is to be set.
        The value of parallax can be anything allowed by the Angle []  constructor.

        """

        # value must be a list
        if not isinstance(parallax, list):
            raise ValueError("The value of parallax must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(parallax)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of parallax is not correct")

            # the type of the values in the list must be Angle
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(parallax, Angle):
                raise ValueError(
                    "type of the first value in parallax is not Angle as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._parallax = copy.deepcopy(parallax)
        except Exception as exc:
            raise ValueError("Invalid parallax : " + str(exc))

        self._parallaxExists = True

    def clearParallax(self):
        """
        Mark parallax, which is an optional field, as non-existent.
        """
        self._parallaxExists = False

    # Extrinsic Table Attributes

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
        self, timeInterval, spectralWindowId, code, direction, properMotion, sourceName
    ):
        """
        Compare each attribute except the autoincrementable one of this SourceRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # timeInterval is a ArrayTimeInterval, compare using the equals method.
        if not self._timeInterval.equals(timeInterval):
            return False

        # spectralWindowId is a Tag, compare using the equals method.
        if not self._spectralWindowId.equals(spectralWindowId):
            return False

        # code is a str, compare using the == operator.
        if not (self._code == code):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._direction) != len(direction):
            return False
        for indx in range(len(direction)):

            # direction is a list of Angle, compare using the almostEquals method.
            if not self._direction[indx].almostEquals(
                direction[indx], self.getTable().getDirectionEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._properMotion) != len(properMotion):
            return False
        for indx in range(len(properMotion)):

            # properMotion is a list of AngularRate, compare using the almostEquals method.
            if not self._properMotion[indx].almostEquals(
                properMotion[indx], self.getTable().getProperMotionEqTolerance()
            ):
                return False

        # sourceName is a str, compare using the == operator.
        if not (self._sourceName == sourceName):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getCode(),
            otherRow.getDirection(),
            otherRow.getProperMotion(),
            otherRow.getSourceName(),
        )

    def compareRequiredValue(self, code, direction, properMotion, sourceName):

        # code is a str, compare using the == operator.
        if not (self._code == code):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._direction) != len(direction):
            return False
        for indx in range(len(direction)):

            # direction is a list of Angle, compare using the almostEquals method.
            if not self._direction[indx].almostEquals(
                direction[indx], self.getTable().getDirectionEqTolerance()
            ):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._properMotion) != len(properMotion):
            return False
        for indx in range(len(properMotion)):

            # properMotion is a list of AngularRate, compare using the almostEquals method.
            if not self._properMotion[indx].almostEquals(
                properMotion[indx], self.getTable().getProperMotionEqTolerance()
            ):
                return False

        # sourceName is a str, compare using the == operator.
        if not (self._sourceName == sourceName):
            return False

        return True


# initialize the dictionary that maps fields to init methods
SourceRow.initFromBinMethods()
