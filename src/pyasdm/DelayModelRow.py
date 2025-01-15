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
# File DelayModelRow.py
#

import pyasdm.DelayModelTable

from .Parser import Parser

import pyasdm.utils

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *

# this will contain all of the static methods used to get each element of the row
# from an EndianInput instance
_fromBinMethods = {}


from pyasdm.enumerations.PolarizationType import PolarizationType


from xml.dom import minidom

import copy


class DelayModelRow:
    """
    The DelayModelRow class is a row of a DelayModelTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a DelayModelRow.
        When row is None, create an empty row attached to table, which must be a DelayModelTable.
        When row is given, copy those values in to the new row. The row argument must be a DelayModelRow.

        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.DelayModelTable):
            raise ValueError("table must be a DelayModelTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize attribute values

        # intrinsic attributes

        self._timeInterval = ArrayTimeInterval()

        self._numPoly = 0

        self._phaseDelay = []  # this is a list of float []

        self._phaseDelayRate = []  # this is a list of float []

        self._groupDelay = []  # this is a list of float []

        self._groupDelayRate = []  # this is a list of float []

        self._timeOriginExists = False

        self._timeOrigin = ArrayTime()

        self._atmosphericGroupDelayExists = False

        self._atmosphericGroupDelay = None

        self._atmosphericGroupDelayRateExists = False

        self._atmosphericGroupDelayRate = None

        self._geometricDelayExists = False

        self._geometricDelay = None

        self._geometricDelayRateExists = False

        self._geometricDelayRate = None

        self._numLOExists = False

        self._numLO = 0

        self._LOOffsetExists = False

        self._LOOffset = []  # this is a list of Frequency []

        self._LOOffsetRateExists = False

        self._LOOffsetRate = []  # this is a list of Frequency []

        self._dispersiveDelayExists = False

        self._dispersiveDelay = None

        self._dispersiveDelayRateExists = False

        self._dispersiveDelayRate = None

        self._atmosphericDryDelayExists = False

        self._atmosphericDryDelay = None

        self._atmosphericWetDelayExists = False

        self._atmosphericWetDelay = None

        self._padDelayExists = False

        self._padDelay = None

        self._antennaDelayExists = False

        self._antennaDelay = None

        self._numReceptorExists = False

        self._numReceptor = 0

        self._polarizationTypeExists = False

        self._polarizationType = []  # this is a list of PolarizationType []

        self._electronicDelayExists = False

        self._electronicDelay = []  # this is a list of float []

        self._electronicDelayRateExists = False

        self._electronicDelayRate = []  # this is a list of float []

        self._receiverDelayExists = False

        self._receiverDelay = []  # this is a list of float []

        self._IFDelayExists = False

        self._IFDelay = []  # this is a list of float []

        self._LODelayExists = False

        self._LODelay = []  # this is a list of float []

        self._crossPolarizationDelayExists = False

        self._crossPolarizationDelay = None

        # extrinsic attributes

        self._antennaId = Tag()

        self._fieldId = Tag()

        self._spectralWindowId = Tag()

        if row is not None:
            if not isinstance(row, DelayModelRow):
                raise ValueError("row must be a DelayModelRow")

            # copy constructor

            self._antennaId = Tag(row._antennaId)

            self._spectralWindowId = Tag(row._spectralWindowId)

            self._timeInterval = ArrayTimeInterval(row._timeInterval)

            self._numPoly = row._numPoly

            # phaseDelay is a  list , make a deep copy
            self._phaseDelay = copy.deepcopy(row._phaseDelay)

            # phaseDelayRate is a  list , make a deep copy
            self._phaseDelayRate = copy.deepcopy(row._phaseDelayRate)

            # groupDelay is a  list , make a deep copy
            self._groupDelay = copy.deepcopy(row._groupDelay)

            # groupDelayRate is a  list , make a deep copy
            self._groupDelayRate = copy.deepcopy(row._groupDelayRate)

            self._fieldId = Tag(row._fieldId)

            # by default set systematically timeOrigin's value to something not None

            if row._timeOriginExists:

                self._timeOrigin = ArrayTime(row._timeOrigin)

                self._timeOriginExists = True

            # by default set systematically atmosphericGroupDelay's value to something not None

            if row._atmosphericGroupDelayExists:

                self._atmosphericGroupDelay = row._atmosphericGroupDelay

                self._atmosphericGroupDelayExists = True

            # by default set systematically atmosphericGroupDelayRate's value to something not None

            if row._atmosphericGroupDelayRateExists:

                self._atmosphericGroupDelayRate = row._atmosphericGroupDelayRate

                self._atmosphericGroupDelayRateExists = True

            # by default set systematically geometricDelay's value to something not None

            if row._geometricDelayExists:

                self._geometricDelay = row._geometricDelay

                self._geometricDelayExists = True

            # by default set systematically geometricDelayRate's value to something not None

            if row._geometricDelayRateExists:

                self._geometricDelayRate = row._geometricDelayRate

                self._geometricDelayRateExists = True

            # by default set systematically numLO's value to something not None

            if row._numLOExists:

                self._numLO = row._numLO

                self._numLOExists = True

            # by default set systematically LOOffset's value to something not None

            if row._LOOffsetExists:

                # LOOffset is a list, make a deep copy
                self.LOOffset = copy.deepcopy(row.LOOffset)

                self._LOOffsetExists = True

            # by default set systematically LOOffsetRate's value to something not None

            if row._LOOffsetRateExists:

                # LOOffsetRate is a list, make a deep copy
                self.LOOffsetRate = copy.deepcopy(row.LOOffsetRate)

                self._LOOffsetRateExists = True

            # by default set systematically dispersiveDelay's value to something not None

            if row._dispersiveDelayExists:

                self._dispersiveDelay = row._dispersiveDelay

                self._dispersiveDelayExists = True

            # by default set systematically dispersiveDelayRate's value to something not None

            if row._dispersiveDelayRateExists:

                self._dispersiveDelayRate = row._dispersiveDelayRate

                self._dispersiveDelayRateExists = True

            # by default set systematically atmosphericDryDelay's value to something not None

            if row._atmosphericDryDelayExists:

                self._atmosphericDryDelay = row._atmosphericDryDelay

                self._atmosphericDryDelayExists = True

            # by default set systematically atmosphericWetDelay's value to something not None

            if row._atmosphericWetDelayExists:

                self._atmosphericWetDelay = row._atmosphericWetDelay

                self._atmosphericWetDelayExists = True

            # by default set systematically padDelay's value to something not None

            if row._padDelayExists:

                self._padDelay = row._padDelay

                self._padDelayExists = True

            # by default set systematically antennaDelay's value to something not None

            if row._antennaDelayExists:

                self._antennaDelay = row._antennaDelay

                self._antennaDelayExists = True

            # by default set systematically numReceptor's value to something not None

            if row._numReceptorExists:

                self._numReceptor = row._numReceptor

                self._numReceptorExists = True

            # by default set systematically polarizationType's value to something not None

            if row._polarizationTypeExists:

                # polarizationType is a list, make a deep copy
                self.polarizationType = copy.deepcopy(row.polarizationType)

                self._polarizationTypeExists = True

            # by default set systematically electronicDelay's value to something not None

            if row._electronicDelayExists:

                # electronicDelay is a list, make a deep copy
                self.electronicDelay = copy.deepcopy(row.electronicDelay)

                self._electronicDelayExists = True

            # by default set systematically electronicDelayRate's value to something not None

            if row._electronicDelayRateExists:

                # electronicDelayRate is a list, make a deep copy
                self.electronicDelayRate = copy.deepcopy(row.electronicDelayRate)

                self._electronicDelayRateExists = True

            # by default set systematically receiverDelay's value to something not None

            if row._receiverDelayExists:

                # receiverDelay is a list, make a deep copy
                self.receiverDelay = copy.deepcopy(row.receiverDelay)

                self._receiverDelayExists = True

            # by default set systematically IFDelay's value to something not None

            if row._IFDelayExists:

                # IFDelay is a list, make a deep copy
                self.IFDelay = copy.deepcopy(row.IFDelay)

                self._IFDelayExists = True

            # by default set systematically LODelay's value to something not None

            if row._LODelayExists:

                # LODelay is a list, make a deep copy
                self.LODelay = copy.deepcopy(row.LODelay)

                self._LODelayExists = True

            # by default set systematically crossPolarizationDelay's value to something not None

            if row._crossPolarizationDelayExists:

                self._crossPolarizationDelay = row._crossPolarizationDelay

                self._crossPolarizationDelayExists = True

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

        result += Parser.valueToXML("numPoly", self._numPoly)

        result += Parser.listValueToXML("phaseDelay", self._phaseDelay)

        result += Parser.listValueToXML("phaseDelayRate", self._phaseDelayRate)

        result += Parser.listValueToXML("groupDelay", self._groupDelay)

        result += Parser.listValueToXML("groupDelayRate", self._groupDelayRate)

        if self._timeOriginExists:

            result += Parser.extendedValueToXML("timeOrigin", self._timeOrigin)

        if self._atmosphericGroupDelayExists:

            result += Parser.valueToXML(
                "atmosphericGroupDelay", self._atmosphericGroupDelay
            )

        if self._atmosphericGroupDelayRateExists:

            result += Parser.valueToXML(
                "atmosphericGroupDelayRate", self._atmosphericGroupDelayRate
            )

        if self._geometricDelayExists:

            result += Parser.valueToXML("geometricDelay", self._geometricDelay)

        if self._geometricDelayRateExists:

            result += Parser.valueToXML("geometricDelayRate", self._geometricDelayRate)

        if self._numLOExists:

            result += Parser.valueToXML("numLO", self._numLO)

        if self._LOOffsetExists:

            result += Parser.listExtendedValueToXML("LOOffset", self._LOOffset)

        if self._LOOffsetRateExists:

            result += Parser.listExtendedValueToXML("LOOffsetRate", self._LOOffsetRate)

        if self._dispersiveDelayExists:

            result += Parser.valueToXML("dispersiveDelay", self._dispersiveDelay)

        if self._dispersiveDelayRateExists:

            result += Parser.valueToXML(
                "dispersiveDelayRate", self._dispersiveDelayRate
            )

        if self._atmosphericDryDelayExists:

            result += Parser.valueToXML(
                "atmosphericDryDelay", self._atmosphericDryDelay
            )

        if self._atmosphericWetDelayExists:

            result += Parser.valueToXML(
                "atmosphericWetDelay", self._atmosphericWetDelay
            )

        if self._padDelayExists:

            result += Parser.valueToXML("padDelay", self._padDelay)

        if self._antennaDelayExists:

            result += Parser.valueToXML("antennaDelay", self._antennaDelay)

        if self._numReceptorExists:

            result += Parser.valueToXML("numReceptor", self._numReceptor)

        if self._polarizationTypeExists:

            result += Parser.listEnumValueToXML(
                "polarizationType", self._polarizationType
            )

        if self._electronicDelayExists:

            result += Parser.listValueToXML("electronicDelay", self._electronicDelay)

        if self._electronicDelayRateExists:

            result += Parser.listValueToXML(
                "electronicDelayRate", self._electronicDelayRate
            )

        if self._receiverDelayExists:

            result += Parser.listValueToXML("receiverDelay", self._receiverDelay)

        if self._IFDelayExists:

            result += Parser.listValueToXML("IFDelay", self._IFDelay)

        if self._LODelayExists:

            result += Parser.listValueToXML("LODelay", self._LODelay)

        if self._crossPolarizationDelayExists:

            result += Parser.valueToXML(
                "crossPolarizationDelay", self._crossPolarizationDelay
            )

        # extrinsic attributes

        result += Parser.extendedValueToXML("antennaId", self._antennaId)

        result += Parser.extendedValueToXML("fieldId", self._fieldId)

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
                "xmlrow is not a string or a minidom.Element", "DelayModelTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "DelayModelTable")

        # intrinsic attribute values

        timeIntervalNode = rowdom.getElementsByTagName("timeInterval")[0]

        self._timeInterval = ArrayTimeInterval(timeIntervalNode.firstChild.data.strip())

        numPolyNode = rowdom.getElementsByTagName("numPoly")[0]

        self._numPoly = int(numPolyNode.firstChild.data.strip())

        phaseDelayNode = rowdom.getElementsByTagName("phaseDelay")[0]

        phaseDelayStr = phaseDelayNode.firstChild.data.strip()

        self._phaseDelay = Parser.stringListToLists(
            phaseDelayStr, float, "DelayModel", False
        )

        phaseDelayRateNode = rowdom.getElementsByTagName("phaseDelayRate")[0]

        phaseDelayRateStr = phaseDelayRateNode.firstChild.data.strip()

        self._phaseDelayRate = Parser.stringListToLists(
            phaseDelayRateStr, float, "DelayModel", False
        )

        groupDelayNode = rowdom.getElementsByTagName("groupDelay")[0]

        groupDelayStr = groupDelayNode.firstChild.data.strip()

        self._groupDelay = Parser.stringListToLists(
            groupDelayStr, float, "DelayModel", False
        )

        groupDelayRateNode = rowdom.getElementsByTagName("groupDelayRate")[0]

        groupDelayRateStr = groupDelayRateNode.firstChild.data.strip()

        self._groupDelayRate = Parser.stringListToLists(
            groupDelayRateStr, float, "DelayModel", False
        )

        timeOriginNode = rowdom.getElementsByTagName("timeOrigin")
        if len(timeOriginNode) > 0:

            self._timeOrigin = ArrayTime(timeOriginNode[0].firstChild.data.strip())

            self._timeOriginExists = True

        atmosphericGroupDelayNode = rowdom.getElementsByTagName("atmosphericGroupDelay")
        if len(atmosphericGroupDelayNode) > 0:

            self._atmosphericGroupDelay = float(
                atmosphericGroupDelayNode[0].firstChild.data.strip()
            )

            self._atmosphericGroupDelayExists = True

        atmosphericGroupDelayRateNode = rowdom.getElementsByTagName(
            "atmosphericGroupDelayRate"
        )
        if len(atmosphericGroupDelayRateNode) > 0:

            self._atmosphericGroupDelayRate = float(
                atmosphericGroupDelayRateNode[0].firstChild.data.strip()
            )

            self._atmosphericGroupDelayRateExists = True

        geometricDelayNode = rowdom.getElementsByTagName("geometricDelay")
        if len(geometricDelayNode) > 0:

            self._geometricDelay = float(geometricDelayNode[0].firstChild.data.strip())

            self._geometricDelayExists = True

        geometricDelayRateNode = rowdom.getElementsByTagName("geometricDelayRate")
        if len(geometricDelayRateNode) > 0:

            self._geometricDelayRate = float(
                geometricDelayRateNode[0].firstChild.data.strip()
            )

            self._geometricDelayRateExists = True

        numLONode = rowdom.getElementsByTagName("numLO")
        if len(numLONode) > 0:

            self._numLO = int(numLONode[0].firstChild.data.strip())

            self._numLOExists = True

        LOOffsetNode = rowdom.getElementsByTagName("LOOffset")
        if len(LOOffsetNode) > 0:

            LOOffsetStr = LOOffsetNode[0].firstChild.data.strip()

            self._LOOffset = Parser.stringListToLists(
                LOOffsetStr, Frequency, "DelayModel", True
            )

            self._LOOffsetExists = True

        LOOffsetRateNode = rowdom.getElementsByTagName("LOOffsetRate")
        if len(LOOffsetRateNode) > 0:

            LOOffsetRateStr = LOOffsetRateNode[0].firstChild.data.strip()

            self._LOOffsetRate = Parser.stringListToLists(
                LOOffsetRateStr, Frequency, "DelayModel", True
            )

            self._LOOffsetRateExists = True

        dispersiveDelayNode = rowdom.getElementsByTagName("dispersiveDelay")
        if len(dispersiveDelayNode) > 0:

            self._dispersiveDelay = float(
                dispersiveDelayNode[0].firstChild.data.strip()
            )

            self._dispersiveDelayExists = True

        dispersiveDelayRateNode = rowdom.getElementsByTagName("dispersiveDelayRate")
        if len(dispersiveDelayRateNode) > 0:

            self._dispersiveDelayRate = float(
                dispersiveDelayRateNode[0].firstChild.data.strip()
            )

            self._dispersiveDelayRateExists = True

        atmosphericDryDelayNode = rowdom.getElementsByTagName("atmosphericDryDelay")
        if len(atmosphericDryDelayNode) > 0:

            self._atmosphericDryDelay = float(
                atmosphericDryDelayNode[0].firstChild.data.strip()
            )

            self._atmosphericDryDelayExists = True

        atmosphericWetDelayNode = rowdom.getElementsByTagName("atmosphericWetDelay")
        if len(atmosphericWetDelayNode) > 0:

            self._atmosphericWetDelay = float(
                atmosphericWetDelayNode[0].firstChild.data.strip()
            )

            self._atmosphericWetDelayExists = True

        padDelayNode = rowdom.getElementsByTagName("padDelay")
        if len(padDelayNode) > 0:

            self._padDelay = float(padDelayNode[0].firstChild.data.strip())

            self._padDelayExists = True

        antennaDelayNode = rowdom.getElementsByTagName("antennaDelay")
        if len(antennaDelayNode) > 0:

            self._antennaDelay = float(antennaDelayNode[0].firstChild.data.strip())

            self._antennaDelayExists = True

        numReceptorNode = rowdom.getElementsByTagName("numReceptor")
        if len(numReceptorNode) > 0:

            self._numReceptor = int(numReceptorNode[0].firstChild.data.strip())

            self._numReceptorExists = True

        polarizationTypeNode = rowdom.getElementsByTagName("polarizationType")
        if len(polarizationTypeNode) > 0:

            polarizationTypeStr = polarizationTypeNode[0].firstChild.data.strip()
            self._polarizationType = Parser.stringListToLists(
                polarizationTypeStr, PolarizationType, "DelayModel", False
            )

            self._polarizationTypeExists = True

        electronicDelayNode = rowdom.getElementsByTagName("electronicDelay")
        if len(electronicDelayNode) > 0:

            electronicDelayStr = electronicDelayNode[0].firstChild.data.strip()

            self._electronicDelay = Parser.stringListToLists(
                electronicDelayStr, float, "DelayModel", False
            )

            self._electronicDelayExists = True

        electronicDelayRateNode = rowdom.getElementsByTagName("electronicDelayRate")
        if len(electronicDelayRateNode) > 0:

            electronicDelayRateStr = electronicDelayRateNode[0].firstChild.data.strip()

            self._electronicDelayRate = Parser.stringListToLists(
                electronicDelayRateStr, float, "DelayModel", False
            )

            self._electronicDelayRateExists = True

        receiverDelayNode = rowdom.getElementsByTagName("receiverDelay")
        if len(receiverDelayNode) > 0:

            receiverDelayStr = receiverDelayNode[0].firstChild.data.strip()

            self._receiverDelay = Parser.stringListToLists(
                receiverDelayStr, float, "DelayModel", False
            )

            self._receiverDelayExists = True

        IFDelayNode = rowdom.getElementsByTagName("IFDelay")
        if len(IFDelayNode) > 0:

            IFDelayStr = IFDelayNode[0].firstChild.data.strip()

            self._IFDelay = Parser.stringListToLists(
                IFDelayStr, float, "DelayModel", False
            )

            self._IFDelayExists = True

        LODelayNode = rowdom.getElementsByTagName("LODelay")
        if len(LODelayNode) > 0:

            LODelayStr = LODelayNode[0].firstChild.data.strip()

            self._LODelay = Parser.stringListToLists(
                LODelayStr, float, "DelayModel", False
            )

            self._LODelayExists = True

        crossPolarizationDelayNode = rowdom.getElementsByTagName(
            "crossPolarizationDelay"
        )
        if len(crossPolarizationDelayNode) > 0:

            self._crossPolarizationDelay = float(
                crossPolarizationDelayNode[0].firstChild.data.strip()
            )

            self._crossPolarizationDelayExists = True

        # extrinsic attribute values

        antennaIdNode = rowdom.getElementsByTagName("antennaId")[0]

        self._antennaId = Tag(antennaIdNode.firstChild.data.strip())

        fieldIdNode = rowdom.getElementsByTagName("fieldId")[0]

        self._fieldId = Tag(fieldIdNode.firstChild.data.strip())

        spectralWindowIdNode = rowdom.getElementsByTagName("spectralWindowId")[0]

        self._spectralWindowId = Tag(spectralWindowIdNode.firstChild.data.strip())

        # from link values, if any

    def toBin(self, eos):
        """
        Write this row out to the EndianOutput instance, eos.
        """

        self._antennaId.toBin(eos)

        self._spectralWindowId.toBin(eos)

        self._timeInterval.toBin(eos)

        eos.writeInt(self._numPoly)

        eos.writeInt(len(self._phaseDelay))
        for i in range(len(self._phaseDelay)):

            eos.writeFloat(self._phaseDelay[i])

        eos.writeInt(len(self._phaseDelayRate))
        for i in range(len(self._phaseDelayRate)):

            eos.writeFloat(self._phaseDelayRate[i])

        eos.writeInt(len(self._groupDelay))
        for i in range(len(self._groupDelay)):

            eos.writeFloat(self._groupDelay[i])

        eos.writeInt(len(self._groupDelayRate))
        for i in range(len(self._groupDelayRate)):

            eos.writeFloat(self._groupDelayRate[i])

        self._fieldId.toBin(eos)

        eos.writeBool(self._timeOriginExists)
        if self._timeOriginExists:

            self._timeOrigin.toBin(eos)

        eos.writeBool(self._atmosphericGroupDelayExists)
        if self._atmosphericGroupDelayExists:

            eos.writeFloat(self._atmosphericGroupDelay)

        eos.writeBool(self._atmosphericGroupDelayRateExists)
        if self._atmosphericGroupDelayRateExists:

            eos.writeFloat(self._atmosphericGroupDelayRate)

        eos.writeBool(self._geometricDelayExists)
        if self._geometricDelayExists:

            eos.writeFloat(self._geometricDelay)

        eos.writeBool(self._geometricDelayRateExists)
        if self._geometricDelayRateExists:

            eos.writeFloat(self._geometricDelayRate)

        eos.writeBool(self._numLOExists)
        if self._numLOExists:

            eos.writeInt(self._numLO)

        eos.writeBool(self._LOOffsetExists)
        if self._LOOffsetExists:

            Frequency.listToBin(self._LOOffset, eos)

        eos.writeBool(self._LOOffsetRateExists)
        if self._LOOffsetRateExists:

            Frequency.listToBin(self._LOOffsetRate, eos)

        eos.writeBool(self._dispersiveDelayExists)
        if self._dispersiveDelayExists:

            eos.writeFloat(self._dispersiveDelay)

        eos.writeBool(self._dispersiveDelayRateExists)
        if self._dispersiveDelayRateExists:

            eos.writeFloat(self._dispersiveDelayRate)

        eos.writeBool(self._atmosphericDryDelayExists)
        if self._atmosphericDryDelayExists:

            eos.writeFloat(self._atmosphericDryDelay)

        eos.writeBool(self._atmosphericWetDelayExists)
        if self._atmosphericWetDelayExists:

            eos.writeFloat(self._atmosphericWetDelay)

        eos.writeBool(self._padDelayExists)
        if self._padDelayExists:

            eos.writeFloat(self._padDelay)

        eos.writeBool(self._antennaDelayExists)
        if self._antennaDelayExists:

            eos.writeFloat(self._antennaDelay)

        eos.writeBool(self._numReceptorExists)
        if self._numReceptorExists:

            eos.writeInt(self._numReceptor)

        eos.writeBool(self._polarizationTypeExists)
        if self._polarizationTypeExists:

            eos.writeInt(len(self._polarizationType))
            for i in range(len(self._polarizationType)):

                eos.writeString(self._polarizationType[i].toString())

        eos.writeBool(self._electronicDelayExists)
        if self._electronicDelayExists:

            eos.writeInt(len(self._electronicDelay))
            for i in range(len(self._electronicDelay)):

                eos.writeFloat(self._electronicDelay[i])

        eos.writeBool(self._electronicDelayRateExists)
        if self._electronicDelayRateExists:

            eos.writeInt(len(self._electronicDelayRate))
            for i in range(len(self._electronicDelayRate)):

                eos.writeFloat(self._electronicDelayRate[i])

        eos.writeBool(self._receiverDelayExists)
        if self._receiverDelayExists:

            eos.writeInt(len(self._receiverDelay))
            for i in range(len(self._receiverDelay)):

                eos.writeFloat(self._receiverDelay[i])

        eos.writeBool(self._IFDelayExists)
        if self._IFDelayExists:

            eos.writeInt(len(self._IFDelay))
            for i in range(len(self._IFDelay)):

                eos.writeFloat(self._IFDelay[i])

        eos.writeBool(self._LODelayExists)
        if self._LODelayExists:

            eos.writeInt(len(self._LODelay))
            for i in range(len(self._LODelay)):

                eos.writeFloat(self._LODelay[i])

        eos.writeBool(self._crossPolarizationDelayExists)
        if self._crossPolarizationDelayExists:

            eos.writeFloat(self._crossPolarizationDelay)

    @staticmethod
    def antennaIdFromBin(row, eis):
        """
        Set the antennaId in row from the EndianInput (eis) instance.
        """

        row._antennaId = Tag.fromBin(eis)

    @staticmethod
    def spectralWindowIdFromBin(row, eis):
        """
        Set the spectralWindowId in row from the EndianInput (eis) instance.
        """

        row._spectralWindowId = Tag.fromBin(eis)

    @staticmethod
    def timeIntervalFromBin(row, eis):
        """
        Set the timeInterval in row from the EndianInput (eis) instance.
        """

        row._timeInterval = ArrayTimeInterval.fromBin(eis)

    @staticmethod
    def numPolyFromBin(row, eis):
        """
        Set the numPoly in row from the EndianInput (eis) instance.
        """

        row._numPoly = eis.readInt()

    @staticmethod
    def phaseDelayFromBin(row, eis):
        """
        Set the phaseDelay in row from the EndianInput (eis) instance.
        """

        phaseDelayDim1 = eis.readInt()
        thisList = []
        for i in range(phaseDelayDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._phaseDelay = thisList

    @staticmethod
    def phaseDelayRateFromBin(row, eis):
        """
        Set the phaseDelayRate in row from the EndianInput (eis) instance.
        """

        phaseDelayRateDim1 = eis.readInt()
        thisList = []
        for i in range(phaseDelayRateDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._phaseDelayRate = thisList

    @staticmethod
    def groupDelayFromBin(row, eis):
        """
        Set the groupDelay in row from the EndianInput (eis) instance.
        """

        groupDelayDim1 = eis.readInt()
        thisList = []
        for i in range(groupDelayDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._groupDelay = thisList

    @staticmethod
    def groupDelayRateFromBin(row, eis):
        """
        Set the groupDelayRate in row from the EndianInput (eis) instance.
        """

        groupDelayRateDim1 = eis.readInt()
        thisList = []
        for i in range(groupDelayRateDim1):
            thisValue = eis.readFloat()
            thisList.append(thisValue)
        row._groupDelayRate = thisList

    @staticmethod
    def fieldIdFromBin(row, eis):
        """
        Set the fieldId in row from the EndianInput (eis) instance.
        """

        row._fieldId = Tag.fromBin(eis)

    @staticmethod
    def timeOriginFromBin(row, eis):
        """
        Set the optional timeOrigin in row from the EndianInput (eis) instance.
        """
        row._timeOriginExists = eis.readBool()
        if row._timeOriginExists:

            row._timeOrigin = ArrayTime.fromBin(eis)

    @staticmethod
    def atmosphericGroupDelayFromBin(row, eis):
        """
        Set the optional atmosphericGroupDelay in row from the EndianInput (eis) instance.
        """
        row._atmosphericGroupDelayExists = eis.readBool()
        if row._atmosphericGroupDelayExists:

            row._atmosphericGroupDelay = eis.readFloat()

    @staticmethod
    def atmosphericGroupDelayRateFromBin(row, eis):
        """
        Set the optional atmosphericGroupDelayRate in row from the EndianInput (eis) instance.
        """
        row._atmosphericGroupDelayRateExists = eis.readBool()
        if row._atmosphericGroupDelayRateExists:

            row._atmosphericGroupDelayRate = eis.readFloat()

    @staticmethod
    def geometricDelayFromBin(row, eis):
        """
        Set the optional geometricDelay in row from the EndianInput (eis) instance.
        """
        row._geometricDelayExists = eis.readBool()
        if row._geometricDelayExists:

            row._geometricDelay = eis.readFloat()

    @staticmethod
    def geometricDelayRateFromBin(row, eis):
        """
        Set the optional geometricDelayRate in row from the EndianInput (eis) instance.
        """
        row._geometricDelayRateExists = eis.readBool()
        if row._geometricDelayRateExists:

            row._geometricDelayRate = eis.readFloat()

    @staticmethod
    def numLOFromBin(row, eis):
        """
        Set the optional numLO in row from the EndianInput (eis) instance.
        """
        row._numLOExists = eis.readBool()
        if row._numLOExists:

            row._numLO = eis.readInt()

    @staticmethod
    def LOOffsetFromBin(row, eis):
        """
        Set the optional LOOffset in row from the EndianInput (eis) instance.
        """
        row._LOOffsetExists = eis.readBool()
        if row._LOOffsetExists:

            row._LOOffset = Frequency.from1DBin(eis)

    @staticmethod
    def LOOffsetRateFromBin(row, eis):
        """
        Set the optional LOOffsetRate in row from the EndianInput (eis) instance.
        """
        row._LOOffsetRateExists = eis.readBool()
        if row._LOOffsetRateExists:

            row._LOOffsetRate = Frequency.from1DBin(eis)

    @staticmethod
    def dispersiveDelayFromBin(row, eis):
        """
        Set the optional dispersiveDelay in row from the EndianInput (eis) instance.
        """
        row._dispersiveDelayExists = eis.readBool()
        if row._dispersiveDelayExists:

            row._dispersiveDelay = eis.readFloat()

    @staticmethod
    def dispersiveDelayRateFromBin(row, eis):
        """
        Set the optional dispersiveDelayRate in row from the EndianInput (eis) instance.
        """
        row._dispersiveDelayRateExists = eis.readBool()
        if row._dispersiveDelayRateExists:

            row._dispersiveDelayRate = eis.readFloat()

    @staticmethod
    def atmosphericDryDelayFromBin(row, eis):
        """
        Set the optional atmosphericDryDelay in row from the EndianInput (eis) instance.
        """
        row._atmosphericDryDelayExists = eis.readBool()
        if row._atmosphericDryDelayExists:

            row._atmosphericDryDelay = eis.readFloat()

    @staticmethod
    def atmosphericWetDelayFromBin(row, eis):
        """
        Set the optional atmosphericWetDelay in row from the EndianInput (eis) instance.
        """
        row._atmosphericWetDelayExists = eis.readBool()
        if row._atmosphericWetDelayExists:

            row._atmosphericWetDelay = eis.readFloat()

    @staticmethod
    def padDelayFromBin(row, eis):
        """
        Set the optional padDelay in row from the EndianInput (eis) instance.
        """
        row._padDelayExists = eis.readBool()
        if row._padDelayExists:

            row._padDelay = eis.readFloat()

    @staticmethod
    def antennaDelayFromBin(row, eis):
        """
        Set the optional antennaDelay in row from the EndianInput (eis) instance.
        """
        row._antennaDelayExists = eis.readBool()
        if row._antennaDelayExists:

            row._antennaDelay = eis.readFloat()

    @staticmethod
    def numReceptorFromBin(row, eis):
        """
        Set the optional numReceptor in row from the EndianInput (eis) instance.
        """
        row._numReceptorExists = eis.readBool()
        if row._numReceptorExists:

            row._numReceptor = eis.readInt()

    @staticmethod
    def polarizationTypeFromBin(row, eis):
        """
        Set the optional polarizationType in row from the EndianInput (eis) instance.
        """
        row._polarizationTypeExists = eis.readBool()
        if row._polarizationTypeExists:

            polarizationTypeDim1 = eis.readInt()
            thisList = []
            for i in range(polarizationTypeDim1):
                thisValue = PolarizationType.from_int(eis.readInt())
                thisList.append(thisValue)
            row._polarizationType = thisList

    @staticmethod
    def electronicDelayFromBin(row, eis):
        """
        Set the optional electronicDelay in row from the EndianInput (eis) instance.
        """
        row._electronicDelayExists = eis.readBool()
        if row._electronicDelayExists:

            electronicDelayDim1 = eis.readInt()
            thisList = []
            for i in range(electronicDelayDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._electronicDelay = thisList

    @staticmethod
    def electronicDelayRateFromBin(row, eis):
        """
        Set the optional electronicDelayRate in row from the EndianInput (eis) instance.
        """
        row._electronicDelayRateExists = eis.readBool()
        if row._electronicDelayRateExists:

            electronicDelayRateDim1 = eis.readInt()
            thisList = []
            for i in range(electronicDelayRateDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._electronicDelayRate = thisList

    @staticmethod
    def receiverDelayFromBin(row, eis):
        """
        Set the optional receiverDelay in row from the EndianInput (eis) instance.
        """
        row._receiverDelayExists = eis.readBool()
        if row._receiverDelayExists:

            receiverDelayDim1 = eis.readInt()
            thisList = []
            for i in range(receiverDelayDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._receiverDelay = thisList

    @staticmethod
    def IFDelayFromBin(row, eis):
        """
        Set the optional IFDelay in row from the EndianInput (eis) instance.
        """
        row._IFDelayExists = eis.readBool()
        if row._IFDelayExists:

            IFDelayDim1 = eis.readInt()
            thisList = []
            for i in range(IFDelayDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._IFDelay = thisList

    @staticmethod
    def LODelayFromBin(row, eis):
        """
        Set the optional LODelay in row from the EndianInput (eis) instance.
        """
        row._LODelayExists = eis.readBool()
        if row._LODelayExists:

            LODelayDim1 = eis.readInt()
            thisList = []
            for i in range(LODelayDim1):
                thisValue = eis.readFloat()
                thisList.append(thisValue)
            row._LODelay = thisList

    @staticmethod
    def crossPolarizationDelayFromBin(row, eis):
        """
        Set the optional crossPolarizationDelay in row from the EndianInput (eis) instance.
        """
        row._crossPolarizationDelayExists = eis.readBool()
        if row._crossPolarizationDelayExists:

            row._crossPolarizationDelay = eis.readFloat()

    @staticmethod
    def initFromBinMethods():
        global _fromBinMethods
        if len(_fromBinMethods) > 0:
            return

        _fromBinMethods["antennaId"] = DelayModelRow.antennaIdFromBin
        _fromBinMethods["spectralWindowId"] = DelayModelRow.spectralWindowIdFromBin
        _fromBinMethods["timeInterval"] = DelayModelRow.timeIntervalFromBin
        _fromBinMethods["numPoly"] = DelayModelRow.numPolyFromBin
        _fromBinMethods["phaseDelay"] = DelayModelRow.phaseDelayFromBin
        _fromBinMethods["phaseDelayRate"] = DelayModelRow.phaseDelayRateFromBin
        _fromBinMethods["groupDelay"] = DelayModelRow.groupDelayFromBin
        _fromBinMethods["groupDelayRate"] = DelayModelRow.groupDelayRateFromBin
        _fromBinMethods["fieldId"] = DelayModelRow.fieldIdFromBin

        _fromBinMethods["timeOrigin"] = DelayModelRow.timeOriginFromBin
        _fromBinMethods["atmosphericGroupDelay"] = (
            DelayModelRow.atmosphericGroupDelayFromBin
        )
        _fromBinMethods["atmosphericGroupDelayRate"] = (
            DelayModelRow.atmosphericGroupDelayRateFromBin
        )
        _fromBinMethods["geometricDelay"] = DelayModelRow.geometricDelayFromBin
        _fromBinMethods["geometricDelayRate"] = DelayModelRow.geometricDelayRateFromBin
        _fromBinMethods["numLO"] = DelayModelRow.numLOFromBin
        _fromBinMethods["LOOffset"] = DelayModelRow.LOOffsetFromBin
        _fromBinMethods["LOOffsetRate"] = DelayModelRow.LOOffsetRateFromBin
        _fromBinMethods["dispersiveDelay"] = DelayModelRow.dispersiveDelayFromBin
        _fromBinMethods["dispersiveDelayRate"] = (
            DelayModelRow.dispersiveDelayRateFromBin
        )
        _fromBinMethods["atmosphericDryDelay"] = (
            DelayModelRow.atmosphericDryDelayFromBin
        )
        _fromBinMethods["atmosphericWetDelay"] = (
            DelayModelRow.atmosphericWetDelayFromBin
        )
        _fromBinMethods["padDelay"] = DelayModelRow.padDelayFromBin
        _fromBinMethods["antennaDelay"] = DelayModelRow.antennaDelayFromBin
        _fromBinMethods["numReceptor"] = DelayModelRow.numReceptorFromBin
        _fromBinMethods["polarizationType"] = DelayModelRow.polarizationTypeFromBin
        _fromBinMethods["electronicDelay"] = DelayModelRow.electronicDelayFromBin
        _fromBinMethods["electronicDelayRate"] = (
            DelayModelRow.electronicDelayRateFromBin
        )
        _fromBinMethods["receiverDelay"] = DelayModelRow.receiverDelayFromBin
        _fromBinMethods["IFDelay"] = DelayModelRow.IFDelayFromBin
        _fromBinMethods["LODelay"] = DelayModelRow.LODelayFromBin
        _fromBinMethods["crossPolarizationDelay"] = (
            DelayModelRow.crossPolarizationDelayFromBin
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

        row = DelayModelRow(table)
        for attributeName in attributesSeq:
            if attributeName not in _fromBinMethods:
                raise ConversionException(
                    "There is not a method to read an attribute '"
                    + attributeName
                    + "'.",
                    " DelayModel",
                )

            method = _fromBinMethods[attributeName]
            method(row, eis)

        return row

    # Intrinsice Table Attributes

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

    # ===> Attribute phaseDelay

    _phaseDelay = None  # this is a 1D list of float

    def getPhaseDelay(self):
        """
        Get phaseDelay.
        return phaseDelay as float []
        """

        return copy.deepcopy(self._phaseDelay)

    def setPhaseDelay(self, phaseDelay):
        """
        Set phaseDelay with the specified float []  value.
        phaseDelay The float []  value to which phaseDelay is to be set.


        """

        # value must be a list
        if not isinstance(phaseDelay, list):
            raise ValueError("The value of phaseDelay must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(phaseDelay)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of phaseDelay is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(phaseDelay, float):
                raise ValueError(
                    "type of the first value in phaseDelay is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phaseDelay = copy.deepcopy(phaseDelay)
        except Exception as exc:
            raise ValueError("Invalid phaseDelay : " + str(exc))

    # ===> Attribute phaseDelayRate

    _phaseDelayRate = None  # this is a 1D list of float

    def getPhaseDelayRate(self):
        """
        Get phaseDelayRate.
        return phaseDelayRate as float []
        """

        return copy.deepcopy(self._phaseDelayRate)

    def setPhaseDelayRate(self, phaseDelayRate):
        """
        Set phaseDelayRate with the specified float []  value.
        phaseDelayRate The float []  value to which phaseDelayRate is to be set.


        """

        # value must be a list
        if not isinstance(phaseDelayRate, list):
            raise ValueError("The value of phaseDelayRate must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(phaseDelayRate)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of phaseDelayRate is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(phaseDelayRate, float):
                raise ValueError(
                    "type of the first value in phaseDelayRate is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._phaseDelayRate = copy.deepcopy(phaseDelayRate)
        except Exception as exc:
            raise ValueError("Invalid phaseDelayRate : " + str(exc))

    # ===> Attribute groupDelay

    _groupDelay = None  # this is a 1D list of float

    def getGroupDelay(self):
        """
        Get groupDelay.
        return groupDelay as float []
        """

        return copy.deepcopy(self._groupDelay)

    def setGroupDelay(self, groupDelay):
        """
        Set groupDelay with the specified float []  value.
        groupDelay The float []  value to which groupDelay is to be set.


        """

        # value must be a list
        if not isinstance(groupDelay, list):
            raise ValueError("The value of groupDelay must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(groupDelay)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of groupDelay is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(groupDelay, float):
                raise ValueError(
                    "type of the first value in groupDelay is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._groupDelay = copy.deepcopy(groupDelay)
        except Exception as exc:
            raise ValueError("Invalid groupDelay : " + str(exc))

    # ===> Attribute groupDelayRate

    _groupDelayRate = None  # this is a 1D list of float

    def getGroupDelayRate(self):
        """
        Get groupDelayRate.
        return groupDelayRate as float []
        """

        return copy.deepcopy(self._groupDelayRate)

    def setGroupDelayRate(self, groupDelayRate):
        """
        Set groupDelayRate with the specified float []  value.
        groupDelayRate The float []  value to which groupDelayRate is to be set.


        """

        # value must be a list
        if not isinstance(groupDelayRate, list):
            raise ValueError("The value of groupDelayRate must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(groupDelayRate)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of groupDelayRate is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(groupDelayRate, float):
                raise ValueError(
                    "type of the first value in groupDelayRate is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._groupDelayRate = copy.deepcopy(groupDelayRate)
        except Exception as exc:
            raise ValueError("Invalid groupDelayRate : " + str(exc))

    # ===> Attribute timeOrigin, which is optional
    _timeOriginExists = False

    _timeOrigin = ArrayTime()

    def isTimeOriginExists(self):
        """
        The attribute timeOrigin is optional. Return True if this attribute exists.
        return True if and only if the timeOrigin attribute exists.
        """
        return self._timeOriginExists

    def getTimeOrigin(self):
        """
        Get timeOrigin, which is optional.
        return timeOrigin as ArrayTime
        raises ValueError If timeOrigin does not exist.
        """
        if not self._timeOriginExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + timeOrigin
                + " attribute in table DelayModel does not exist!"
            )

        # make sure it is a copy of ArrayTime
        return ArrayTime(self._timeOrigin)

    def setTimeOrigin(self, timeOrigin):
        """
        Set timeOrigin with the specified ArrayTime value.
        timeOrigin The ArrayTime value to which timeOrigin is to be set.
        The value of timeOrigin can be anything allowed by the ArrayTime constructor.

        """

        self._timeOrigin = ArrayTime(timeOrigin)

        self._timeOriginExists = True

    def clearTimeOrigin(self):
        """
        Mark timeOrigin, which is an optional field, as non-existent.
        """
        self._timeOriginExists = False

    # ===> Attribute atmosphericGroupDelay, which is optional
    _atmosphericGroupDelayExists = False

    _atmosphericGroupDelay = None

    def isAtmosphericGroupDelayExists(self):
        """
        The attribute atmosphericGroupDelay is optional. Return True if this attribute exists.
        return True if and only if the atmosphericGroupDelay attribute exists.
        """
        return self._atmosphericGroupDelayExists

    def getAtmosphericGroupDelay(self):
        """
        Get atmosphericGroupDelay, which is optional.
        return atmosphericGroupDelay as float
        raises ValueError If atmosphericGroupDelay does not exist.
        """
        if not self._atmosphericGroupDelayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + atmosphericGroupDelay
                + " attribute in table DelayModel does not exist!"
            )

        return self._atmosphericGroupDelay

    def setAtmosphericGroupDelay(self, atmosphericGroupDelay):
        """
        Set atmosphericGroupDelay with the specified float value.
        atmosphericGroupDelay The float value to which atmosphericGroupDelay is to be set.


        """

        self._atmosphericGroupDelay = float(atmosphericGroupDelay)

        self._atmosphericGroupDelayExists = True

    def clearAtmosphericGroupDelay(self):
        """
        Mark atmosphericGroupDelay, which is an optional field, as non-existent.
        """
        self._atmosphericGroupDelayExists = False

    # ===> Attribute atmosphericGroupDelayRate, which is optional
    _atmosphericGroupDelayRateExists = False

    _atmosphericGroupDelayRate = None

    def isAtmosphericGroupDelayRateExists(self):
        """
        The attribute atmosphericGroupDelayRate is optional. Return True if this attribute exists.
        return True if and only if the atmosphericGroupDelayRate attribute exists.
        """
        return self._atmosphericGroupDelayRateExists

    def getAtmosphericGroupDelayRate(self):
        """
        Get atmosphericGroupDelayRate, which is optional.
        return atmosphericGroupDelayRate as float
        raises ValueError If atmosphericGroupDelayRate does not exist.
        """
        if not self._atmosphericGroupDelayRateExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + atmosphericGroupDelayRate
                + " attribute in table DelayModel does not exist!"
            )

        return self._atmosphericGroupDelayRate

    def setAtmosphericGroupDelayRate(self, atmosphericGroupDelayRate):
        """
        Set atmosphericGroupDelayRate with the specified float value.
        atmosphericGroupDelayRate The float value to which atmosphericGroupDelayRate is to be set.


        """

        self._atmosphericGroupDelayRate = float(atmosphericGroupDelayRate)

        self._atmosphericGroupDelayRateExists = True

    def clearAtmosphericGroupDelayRate(self):
        """
        Mark atmosphericGroupDelayRate, which is an optional field, as non-existent.
        """
        self._atmosphericGroupDelayRateExists = False

    # ===> Attribute geometricDelay, which is optional
    _geometricDelayExists = False

    _geometricDelay = None

    def isGeometricDelayExists(self):
        """
        The attribute geometricDelay is optional. Return True if this attribute exists.
        return True if and only if the geometricDelay attribute exists.
        """
        return self._geometricDelayExists

    def getGeometricDelay(self):
        """
        Get geometricDelay, which is optional.
        return geometricDelay as float
        raises ValueError If geometricDelay does not exist.
        """
        if not self._geometricDelayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + geometricDelay
                + " attribute in table DelayModel does not exist!"
            )

        return self._geometricDelay

    def setGeometricDelay(self, geometricDelay):
        """
        Set geometricDelay with the specified float value.
        geometricDelay The float value to which geometricDelay is to be set.


        """

        self._geometricDelay = float(geometricDelay)

        self._geometricDelayExists = True

    def clearGeometricDelay(self):
        """
        Mark geometricDelay, which is an optional field, as non-existent.
        """
        self._geometricDelayExists = False

    # ===> Attribute geometricDelayRate, which is optional
    _geometricDelayRateExists = False

    _geometricDelayRate = None

    def isGeometricDelayRateExists(self):
        """
        The attribute geometricDelayRate is optional. Return True if this attribute exists.
        return True if and only if the geometricDelayRate attribute exists.
        """
        return self._geometricDelayRateExists

    def getGeometricDelayRate(self):
        """
        Get geometricDelayRate, which is optional.
        return geometricDelayRate as float
        raises ValueError If geometricDelayRate does not exist.
        """
        if not self._geometricDelayRateExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + geometricDelayRate
                + " attribute in table DelayModel does not exist!"
            )

        return self._geometricDelayRate

    def setGeometricDelayRate(self, geometricDelayRate):
        """
        Set geometricDelayRate with the specified float value.
        geometricDelayRate The float value to which geometricDelayRate is to be set.


        """

        self._geometricDelayRate = float(geometricDelayRate)

        self._geometricDelayRateExists = True

    def clearGeometricDelayRate(self):
        """
        Mark geometricDelayRate, which is an optional field, as non-existent.
        """
        self._geometricDelayRateExists = False

    # ===> Attribute numLO, which is optional
    _numLOExists = False

    _numLO = 0

    def isNumLOExists(self):
        """
        The attribute numLO is optional. Return True if this attribute exists.
        return True if and only if the numLO attribute exists.
        """
        return self._numLOExists

    def getNumLO(self):
        """
        Get numLO, which is optional.
        return numLO as int
        raises ValueError If numLO does not exist.
        """
        if not self._numLOExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numLO
                + " attribute in table DelayModel does not exist!"
            )

        return self._numLO

    def setNumLO(self, numLO):
        """
        Set numLO with the specified int value.
        numLO The int value to which numLO is to be set.


        """

        self._numLO = int(numLO)

        self._numLOExists = True

    def clearNumLO(self):
        """
        Mark numLO, which is an optional field, as non-existent.
        """
        self._numLOExists = False

    # ===> Attribute LOOffset, which is optional
    _LOOffsetExists = False

    _LOOffset = None  # this is a 1D list of Frequency

    def isLOOffsetExists(self):
        """
        The attribute LOOffset is optional. Return True if this attribute exists.
        return True if and only if the LOOffset attribute exists.
        """
        return self._LOOffsetExists

    def getLOOffset(self):
        """
        Get LOOffset, which is optional.
        return LOOffset as Frequency []
        raises ValueError If LOOffset does not exist.
        """
        if not self._LOOffsetExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + LOOffset
                + " attribute in table DelayModel does not exist!"
            )

        return copy.deepcopy(self._LOOffset)

    def setLOOffset(self, LOOffset):
        """
        Set LOOffset with the specified Frequency []  value.
        LOOffset The Frequency []  value to which LOOffset is to be set.
        The value of LOOffset can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(LOOffset, list):
            raise ValueError("The value of LOOffset must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(LOOffset)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of LOOffset is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(LOOffset, Frequency):
                raise ValueError(
                    "type of the first value in LOOffset is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._LOOffset = copy.deepcopy(LOOffset)
        except Exception as exc:
            raise ValueError("Invalid LOOffset : " + str(exc))

        self._LOOffsetExists = True

    def clearLOOffset(self):
        """
        Mark LOOffset, which is an optional field, as non-existent.
        """
        self._LOOffsetExists = False

    # ===> Attribute LOOffsetRate, which is optional
    _LOOffsetRateExists = False

    _LOOffsetRate = None  # this is a 1D list of Frequency

    def isLOOffsetRateExists(self):
        """
        The attribute LOOffsetRate is optional. Return True if this attribute exists.
        return True if and only if the LOOffsetRate attribute exists.
        """
        return self._LOOffsetRateExists

    def getLOOffsetRate(self):
        """
        Get LOOffsetRate, which is optional.
        return LOOffsetRate as Frequency []
        raises ValueError If LOOffsetRate does not exist.
        """
        if not self._LOOffsetRateExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + LOOffsetRate
                + " attribute in table DelayModel does not exist!"
            )

        return copy.deepcopy(self._LOOffsetRate)

    def setLOOffsetRate(self, LOOffsetRate):
        """
        Set LOOffsetRate with the specified Frequency []  value.
        LOOffsetRate The Frequency []  value to which LOOffsetRate is to be set.
        The value of LOOffsetRate can be anything allowed by the Frequency []  constructor.

        """

        # value must be a list
        if not isinstance(LOOffsetRate, list):
            raise ValueError("The value of LOOffsetRate must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(LOOffsetRate)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of LOOffsetRate is not correct")

            # the type of the values in the list must be Frequency
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(LOOffsetRate, Frequency):
                raise ValueError(
                    "type of the first value in LOOffsetRate is not Frequency as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._LOOffsetRate = copy.deepcopy(LOOffsetRate)
        except Exception as exc:
            raise ValueError("Invalid LOOffsetRate : " + str(exc))

        self._LOOffsetRateExists = True

    def clearLOOffsetRate(self):
        """
        Mark LOOffsetRate, which is an optional field, as non-existent.
        """
        self._LOOffsetRateExists = False

    # ===> Attribute dispersiveDelay, which is optional
    _dispersiveDelayExists = False

    _dispersiveDelay = None

    def isDispersiveDelayExists(self):
        """
        The attribute dispersiveDelay is optional. Return True if this attribute exists.
        return True if and only if the dispersiveDelay attribute exists.
        """
        return self._dispersiveDelayExists

    def getDispersiveDelay(self):
        """
        Get dispersiveDelay, which is optional.
        return dispersiveDelay as float
        raises ValueError If dispersiveDelay does not exist.
        """
        if not self._dispersiveDelayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + dispersiveDelay
                + " attribute in table DelayModel does not exist!"
            )

        return self._dispersiveDelay

    def setDispersiveDelay(self, dispersiveDelay):
        """
        Set dispersiveDelay with the specified float value.
        dispersiveDelay The float value to which dispersiveDelay is to be set.


        """

        self._dispersiveDelay = float(dispersiveDelay)

        self._dispersiveDelayExists = True

    def clearDispersiveDelay(self):
        """
        Mark dispersiveDelay, which is an optional field, as non-existent.
        """
        self._dispersiveDelayExists = False

    # ===> Attribute dispersiveDelayRate, which is optional
    _dispersiveDelayRateExists = False

    _dispersiveDelayRate = None

    def isDispersiveDelayRateExists(self):
        """
        The attribute dispersiveDelayRate is optional. Return True if this attribute exists.
        return True if and only if the dispersiveDelayRate attribute exists.
        """
        return self._dispersiveDelayRateExists

    def getDispersiveDelayRate(self):
        """
        Get dispersiveDelayRate, which is optional.
        return dispersiveDelayRate as float
        raises ValueError If dispersiveDelayRate does not exist.
        """
        if not self._dispersiveDelayRateExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + dispersiveDelayRate
                + " attribute in table DelayModel does not exist!"
            )

        return self._dispersiveDelayRate

    def setDispersiveDelayRate(self, dispersiveDelayRate):
        """
        Set dispersiveDelayRate with the specified float value.
        dispersiveDelayRate The float value to which dispersiveDelayRate is to be set.


        """

        self._dispersiveDelayRate = float(dispersiveDelayRate)

        self._dispersiveDelayRateExists = True

    def clearDispersiveDelayRate(self):
        """
        Mark dispersiveDelayRate, which is an optional field, as non-existent.
        """
        self._dispersiveDelayRateExists = False

    # ===> Attribute atmosphericDryDelay, which is optional
    _atmosphericDryDelayExists = False

    _atmosphericDryDelay = None

    def isAtmosphericDryDelayExists(self):
        """
        The attribute atmosphericDryDelay is optional. Return True if this attribute exists.
        return True if and only if the atmosphericDryDelay attribute exists.
        """
        return self._atmosphericDryDelayExists

    def getAtmosphericDryDelay(self):
        """
        Get atmosphericDryDelay, which is optional.
        return atmosphericDryDelay as float
        raises ValueError If atmosphericDryDelay does not exist.
        """
        if not self._atmosphericDryDelayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + atmosphericDryDelay
                + " attribute in table DelayModel does not exist!"
            )

        return self._atmosphericDryDelay

    def setAtmosphericDryDelay(self, atmosphericDryDelay):
        """
        Set atmosphericDryDelay with the specified float value.
        atmosphericDryDelay The float value to which atmosphericDryDelay is to be set.


        """

        self._atmosphericDryDelay = float(atmosphericDryDelay)

        self._atmosphericDryDelayExists = True

    def clearAtmosphericDryDelay(self):
        """
        Mark atmosphericDryDelay, which is an optional field, as non-existent.
        """
        self._atmosphericDryDelayExists = False

    # ===> Attribute atmosphericWetDelay, which is optional
    _atmosphericWetDelayExists = False

    _atmosphericWetDelay = None

    def isAtmosphericWetDelayExists(self):
        """
        The attribute atmosphericWetDelay is optional. Return True if this attribute exists.
        return True if and only if the atmosphericWetDelay attribute exists.
        """
        return self._atmosphericWetDelayExists

    def getAtmosphericWetDelay(self):
        """
        Get atmosphericWetDelay, which is optional.
        return atmosphericWetDelay as float
        raises ValueError If atmosphericWetDelay does not exist.
        """
        if not self._atmosphericWetDelayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + atmosphericWetDelay
                + " attribute in table DelayModel does not exist!"
            )

        return self._atmosphericWetDelay

    def setAtmosphericWetDelay(self, atmosphericWetDelay):
        """
        Set atmosphericWetDelay with the specified float value.
        atmosphericWetDelay The float value to which atmosphericWetDelay is to be set.


        """

        self._atmosphericWetDelay = float(atmosphericWetDelay)

        self._atmosphericWetDelayExists = True

    def clearAtmosphericWetDelay(self):
        """
        Mark atmosphericWetDelay, which is an optional field, as non-existent.
        """
        self._atmosphericWetDelayExists = False

    # ===> Attribute padDelay, which is optional
    _padDelayExists = False

    _padDelay = None

    def isPadDelayExists(self):
        """
        The attribute padDelay is optional. Return True if this attribute exists.
        return True if and only if the padDelay attribute exists.
        """
        return self._padDelayExists

    def getPadDelay(self):
        """
        Get padDelay, which is optional.
        return padDelay as float
        raises ValueError If padDelay does not exist.
        """
        if not self._padDelayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + padDelay
                + " attribute in table DelayModel does not exist!"
            )

        return self._padDelay

    def setPadDelay(self, padDelay):
        """
        Set padDelay with the specified float value.
        padDelay The float value to which padDelay is to be set.


        """

        self._padDelay = float(padDelay)

        self._padDelayExists = True

    def clearPadDelay(self):
        """
        Mark padDelay, which is an optional field, as non-existent.
        """
        self._padDelayExists = False

    # ===> Attribute antennaDelay, which is optional
    _antennaDelayExists = False

    _antennaDelay = None

    def isAntennaDelayExists(self):
        """
        The attribute antennaDelay is optional. Return True if this attribute exists.
        return True if and only if the antennaDelay attribute exists.
        """
        return self._antennaDelayExists

    def getAntennaDelay(self):
        """
        Get antennaDelay, which is optional.
        return antennaDelay as float
        raises ValueError If antennaDelay does not exist.
        """
        if not self._antennaDelayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + antennaDelay
                + " attribute in table DelayModel does not exist!"
            )

        return self._antennaDelay

    def setAntennaDelay(self, antennaDelay):
        """
        Set antennaDelay with the specified float value.
        antennaDelay The float value to which antennaDelay is to be set.


        """

        self._antennaDelay = float(antennaDelay)

        self._antennaDelayExists = True

    def clearAntennaDelay(self):
        """
        Mark antennaDelay, which is an optional field, as non-existent.
        """
        self._antennaDelayExists = False

    # ===> Attribute numReceptor, which is optional
    _numReceptorExists = False

    _numReceptor = 0

    def isNumReceptorExists(self):
        """
        The attribute numReceptor is optional. Return True if this attribute exists.
        return True if and only if the numReceptor attribute exists.
        """
        return self._numReceptorExists

    def getNumReceptor(self):
        """
        Get numReceptor, which is optional.
        return numReceptor as int
        raises ValueError If numReceptor does not exist.
        """
        if not self._numReceptorExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + numReceptor
                + " attribute in table DelayModel does not exist!"
            )

        return self._numReceptor

    def setNumReceptor(self, numReceptor):
        """
        Set numReceptor with the specified int value.
        numReceptor The int value to which numReceptor is to be set.


        """

        self._numReceptor = int(numReceptor)

        self._numReceptorExists = True

    def clearNumReceptor(self):
        """
        Mark numReceptor, which is an optional field, as non-existent.
        """
        self._numReceptorExists = False

    # ===> Attribute polarizationType, which is optional
    _polarizationTypeExists = False

    _polarizationType = None  # this is a 1D list of PolarizationType

    def isPolarizationTypeExists(self):
        """
        The attribute polarizationType is optional. Return True if this attribute exists.
        return True if and only if the polarizationType attribute exists.
        """
        return self._polarizationTypeExists

    def getPolarizationType(self):
        """
        Get polarizationType, which is optional.
        return polarizationType as PolarizationType []
        raises ValueError If polarizationType does not exist.
        """
        if not self._polarizationTypeExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + polarizationType
                + " attribute in table DelayModel does not exist!"
            )

        return copy.deepcopy(self._polarizationType)

    def setPolarizationType(self, polarizationType):
        """
        Set polarizationType with the specified PolarizationType []  value.
        polarizationType The PolarizationType []  value to which polarizationType is to be set.


        """

        # value must be a list
        if not isinstance(polarizationType, list):
            raise ValueError("The value of polarizationType must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(polarizationType)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of polarizationType is not correct")

            # the type of the values in the list must be PolarizationType
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(polarizationType, PolarizationType):
                raise ValueError(
                    "type of the first value in polarizationType is not PolarizationType as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._polarizationType = copy.deepcopy(polarizationType)
        except Exception as exc:
            raise ValueError("Invalid polarizationType : " + str(exc))

        self._polarizationTypeExists = True

    def clearPolarizationType(self):
        """
        Mark polarizationType, which is an optional field, as non-existent.
        """
        self._polarizationTypeExists = False

    # ===> Attribute electronicDelay, which is optional
    _electronicDelayExists = False

    _electronicDelay = None  # this is a 1D list of float

    def isElectronicDelayExists(self):
        """
        The attribute electronicDelay is optional. Return True if this attribute exists.
        return True if and only if the electronicDelay attribute exists.
        """
        return self._electronicDelayExists

    def getElectronicDelay(self):
        """
        Get electronicDelay, which is optional.
        return electronicDelay as float []
        raises ValueError If electronicDelay does not exist.
        """
        if not self._electronicDelayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + electronicDelay
                + " attribute in table DelayModel does not exist!"
            )

        return copy.deepcopy(self._electronicDelay)

    def setElectronicDelay(self, electronicDelay):
        """
        Set electronicDelay with the specified float []  value.
        electronicDelay The float []  value to which electronicDelay is to be set.


        """

        # value must be a list
        if not isinstance(electronicDelay, list):
            raise ValueError("The value of electronicDelay must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(electronicDelay)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of electronicDelay is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(electronicDelay, float):
                raise ValueError(
                    "type of the first value in electronicDelay is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._electronicDelay = copy.deepcopy(electronicDelay)
        except Exception as exc:
            raise ValueError("Invalid electronicDelay : " + str(exc))

        self._electronicDelayExists = True

    def clearElectronicDelay(self):
        """
        Mark electronicDelay, which is an optional field, as non-existent.
        """
        self._electronicDelayExists = False

    # ===> Attribute electronicDelayRate, which is optional
    _electronicDelayRateExists = False

    _electronicDelayRate = None  # this is a 1D list of float

    def isElectronicDelayRateExists(self):
        """
        The attribute electronicDelayRate is optional. Return True if this attribute exists.
        return True if and only if the electronicDelayRate attribute exists.
        """
        return self._electronicDelayRateExists

    def getElectronicDelayRate(self):
        """
        Get electronicDelayRate, which is optional.
        return electronicDelayRate as float []
        raises ValueError If electronicDelayRate does not exist.
        """
        if not self._electronicDelayRateExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + electronicDelayRate
                + " attribute in table DelayModel does not exist!"
            )

        return copy.deepcopy(self._electronicDelayRate)

    def setElectronicDelayRate(self, electronicDelayRate):
        """
        Set electronicDelayRate with the specified float []  value.
        electronicDelayRate The float []  value to which electronicDelayRate is to be set.


        """

        # value must be a list
        if not isinstance(electronicDelayRate, list):
            raise ValueError("The value of electronicDelayRate must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(electronicDelayRate)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of electronicDelayRate is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(electronicDelayRate, float):
                raise ValueError(
                    "type of the first value in electronicDelayRate is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._electronicDelayRate = copy.deepcopy(electronicDelayRate)
        except Exception as exc:
            raise ValueError("Invalid electronicDelayRate : " + str(exc))

        self._electronicDelayRateExists = True

    def clearElectronicDelayRate(self):
        """
        Mark electronicDelayRate, which is an optional field, as non-existent.
        """
        self._electronicDelayRateExists = False

    # ===> Attribute receiverDelay, which is optional
    _receiverDelayExists = False

    _receiverDelay = None  # this is a 1D list of float

    def isReceiverDelayExists(self):
        """
        The attribute receiverDelay is optional. Return True if this attribute exists.
        return True if and only if the receiverDelay attribute exists.
        """
        return self._receiverDelayExists

    def getReceiverDelay(self):
        """
        Get receiverDelay, which is optional.
        return receiverDelay as float []
        raises ValueError If receiverDelay does not exist.
        """
        if not self._receiverDelayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + receiverDelay
                + " attribute in table DelayModel does not exist!"
            )

        return copy.deepcopy(self._receiverDelay)

    def setReceiverDelay(self, receiverDelay):
        """
        Set receiverDelay with the specified float []  value.
        receiverDelay The float []  value to which receiverDelay is to be set.


        """

        # value must be a list
        if not isinstance(receiverDelay, list):
            raise ValueError("The value of receiverDelay must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(receiverDelay)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of receiverDelay is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(receiverDelay, float):
                raise ValueError(
                    "type of the first value in receiverDelay is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._receiverDelay = copy.deepcopy(receiverDelay)
        except Exception as exc:
            raise ValueError("Invalid receiverDelay : " + str(exc))

        self._receiverDelayExists = True

    def clearReceiverDelay(self):
        """
        Mark receiverDelay, which is an optional field, as non-existent.
        """
        self._receiverDelayExists = False

    # ===> Attribute IFDelay, which is optional
    _IFDelayExists = False

    _IFDelay = None  # this is a 1D list of float

    def isIFDelayExists(self):
        """
        The attribute IFDelay is optional. Return True if this attribute exists.
        return True if and only if the IFDelay attribute exists.
        """
        return self._IFDelayExists

    def getIFDelay(self):
        """
        Get IFDelay, which is optional.
        return IFDelay as float []
        raises ValueError If IFDelay does not exist.
        """
        if not self._IFDelayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + IFDelay
                + " attribute in table DelayModel does not exist!"
            )

        return copy.deepcopy(self._IFDelay)

    def setIFDelay(self, IFDelay):
        """
        Set IFDelay with the specified float []  value.
        IFDelay The float []  value to which IFDelay is to be set.


        """

        # value must be a list
        if not isinstance(IFDelay, list):
            raise ValueError("The value of IFDelay must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(IFDelay)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of IFDelay is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(IFDelay, float):
                raise ValueError(
                    "type of the first value in IFDelay is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._IFDelay = copy.deepcopy(IFDelay)
        except Exception as exc:
            raise ValueError("Invalid IFDelay : " + str(exc))

        self._IFDelayExists = True

    def clearIFDelay(self):
        """
        Mark IFDelay, which is an optional field, as non-existent.
        """
        self._IFDelayExists = False

    # ===> Attribute LODelay, which is optional
    _LODelayExists = False

    _LODelay = None  # this is a 1D list of float

    def isLODelayExists(self):
        """
        The attribute LODelay is optional. Return True if this attribute exists.
        return True if and only if the LODelay attribute exists.
        """
        return self._LODelayExists

    def getLODelay(self):
        """
        Get LODelay, which is optional.
        return LODelay as float []
        raises ValueError If LODelay does not exist.
        """
        if not self._LODelayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + LODelay
                + " attribute in table DelayModel does not exist!"
            )

        return copy.deepcopy(self._LODelay)

    def setLODelay(self, LODelay):
        """
        Set LODelay with the specified float []  value.
        LODelay The float []  value to which LODelay is to be set.


        """

        # value must be a list
        if not isinstance(LODelay, list):
            raise ValueError("The value of LODelay must be a list")
        # check the shape
        try:
            listDims = pyasdm.utils.getListDims(LODelay)

            shapeOK = len(listDims) == 1

            if not shapeOK:
                raise ValueError("shape of LODelay is not correct")

            # the type of the values in the list must be float
            # note : this only checks the first value found
            if not pyasdm.utils.checkListType(LODelay, float):
                raise ValueError(
                    "type of the first value in LODelay is not float as expected"
                )
            # finally, (reasonably) safe to just do a deepcopy
            self._LODelay = copy.deepcopy(LODelay)
        except Exception as exc:
            raise ValueError("Invalid LODelay : " + str(exc))

        self._LODelayExists = True

    def clearLODelay(self):
        """
        Mark LODelay, which is an optional field, as non-existent.
        """
        self._LODelayExists = False

    # ===> Attribute crossPolarizationDelay, which is optional
    _crossPolarizationDelayExists = False

    _crossPolarizationDelay = None

    def isCrossPolarizationDelayExists(self):
        """
        The attribute crossPolarizationDelay is optional. Return True if this attribute exists.
        return True if and only if the crossPolarizationDelay attribute exists.
        """
        return self._crossPolarizationDelayExists

    def getCrossPolarizationDelay(self):
        """
        Get crossPolarizationDelay, which is optional.
        return crossPolarizationDelay as float
        raises ValueError If crossPolarizationDelay does not exist.
        """
        if not self._crossPolarizationDelayExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + crossPolarizationDelay
                + " attribute in table DelayModel does not exist!"
            )

        return self._crossPolarizationDelay

    def setCrossPolarizationDelay(self, crossPolarizationDelay):
        """
        Set crossPolarizationDelay with the specified float value.
        crossPolarizationDelay The float value to which crossPolarizationDelay is to be set.


        """

        self._crossPolarizationDelay = float(crossPolarizationDelay)

        self._crossPolarizationDelayExists = True

    def clearCrossPolarizationDelay(self):
        """
        Mark crossPolarizationDelay, which is an optional field, as non-existent.
        """
        self._crossPolarizationDelayExists = False

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

        """

        self._fieldId = Tag(fieldId)

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

    def getSpectralWindowUsingSpectralWindowId(self):
        """
        Returns the row in the SpectralWindow table having SpectralWindow.spectralWindowId == spectralWindowId

        """

        return (
            self._table.getContainer()
            .getSpectralWindow()
            .getRowByKey(self._spectralWindowId)
        )

    def getFieldUsingFieldId(self):
        """
        Returns the row in the Field table having Field.fieldId == fieldId

        """

        return self._table.getContainer().getField().getRowByKey(self._fieldId)

    # comparison methods

    def compareNoAutoInc(
        self,
        antennaId,
        spectralWindowId,
        timeInterval,
        numPoly,
        phaseDelay,
        phaseDelayRate,
        groupDelay,
        groupDelayRate,
        fieldId,
    ):
        """
        Compare each attribute except the autoincrementable one of this DelayModelRow with
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

        # numPoly is a int, compare using the == operator.
        if not (self._numPoly == numPoly):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseDelay) != len(phaseDelay):
            return False
        for indx in range(len(phaseDelay)):

            # phaseDelay is a list of float, compare using == operator.
            if not (self._phaseDelay[indx] == phaseDelay[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseDelayRate) != len(phaseDelayRate):
            return False
        for indx in range(len(phaseDelayRate)):

            # phaseDelayRate is a list of float, compare using == operator.
            if not (self._phaseDelayRate[indx] == phaseDelayRate[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._groupDelay) != len(groupDelay):
            return False
        for indx in range(len(groupDelay)):

            # groupDelay is a list of float, compare using == operator.
            if not (self._groupDelay[indx] == groupDelay[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._groupDelayRate) != len(groupDelayRate):
            return False
        for indx in range(len(groupDelayRate)):

            # groupDelayRate is a list of float, compare using == operator.
            if not (self._groupDelayRate[indx] == groupDelayRate[indx]):
                return False

        # fieldId is a Tag, compare using the equals method.
        if not self._fieldId.equals(fieldId):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getNumPoly(),
            otherRow.getPhaseDelay(),
            otherRow.getPhaseDelayRate(),
            otherRow.getGroupDelay(),
            otherRow.getGroupDelayRate(),
            otherRow.getFieldId(),
        )

    def compareRequiredValue(
        self, numPoly, phaseDelay, phaseDelayRate, groupDelay, groupDelayRate, fieldId
    ):

        # numPoly is a int, compare using the == operator.
        if not (self._numPoly == numPoly):
            return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseDelay) != len(phaseDelay):
            return False
        for indx in range(len(phaseDelay)):

            # phaseDelay is a list of float, compare using == operator.
            if not (self._phaseDelay[indx] == phaseDelay[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._phaseDelayRate) != len(phaseDelayRate):
            return False
        for indx in range(len(phaseDelayRate)):

            # phaseDelayRate is a list of float, compare using == operator.
            if not (self._phaseDelayRate[indx] == phaseDelayRate[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._groupDelay) != len(groupDelay):
            return False
        for indx in range(len(groupDelay)):

            # groupDelay is a list of float, compare using == operator.
            if not (self._groupDelay[indx] == groupDelay[indx]):
                return False

        # We compare two 1D arrays.
        # Compare firstly their dimensions and then their values.
        if len(self._groupDelayRate) != len(groupDelayRate):
            return False
        for indx in range(len(groupDelayRate)):

            # groupDelayRate is a list of float, compare using == operator.
            if not (self._groupDelayRate[indx] == groupDelayRate[indx]):
                return False

        # fieldId is a Tag, compare using the equals method.
        if not self._fieldId.equals(fieldId):
            return False

        return True


# initialize the dictionary that maps fields to init methods
DelayModelRow.initFromBinMethods()
