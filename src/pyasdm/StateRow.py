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
# File StateRow.py
#

import pyasdm.StateTable

from .Parser import Parser

from .exceptions.ConversionException import ConversionException

# All of the extended types are imported
from pyasdm.types import *


from pyasdm.enumerations.CalibrationDevice import CalibrationDevice


from xml.dom import minidom

import copy


class StateRow:
    """
    The StateRow class is a row of a StateTable.

    Generated from model's revision -1, branch
    """

    # the table to which this row belongs.
    _table = None

    # whether this row has been added to the table or not.
    _hasBeenAdded = False

    # internal attribute values appear later, with their getters and setters

    def __init__(self, table, row=None):
        """
        Create a StateRow.
        When row is None, create an empty row attached to table, which must be a StateTable.
        When row is given, copy those values in to the new row. The row argument must be a StateRow.
        The returned new row is not yet added to table, but it knows about table.
        """
        if not isinstance(table, pyasdm.StateTable):
            raise ValueError("table must be a MainTable")

        self._table = table
        self._hasBeenAdded = False

        # initialize all attributes which have an enumerated type with the value of index 0 in the Enumeration they belong to.
        self._calDeviceName = CalibrationDevice.from_int(0)

        if row is not None:
            if not isinstance(row, StateRow):
                raise ValueError("row must be a MainRow")

            self._stateId = Tag(row._stateId)

            # We force the attribute of the result to be not None
            if row._calDeviceName is None:
                self._calDeviceName = CalibrationDevice.from_int(0)
            else:
                self._calDeviceName = CalibrationDevice(row._calDeviceName)

            self._sig = row._sig

            self._ref = row._ref

            self._onSky = row._onSky

            # by default set systematically weight's value to something not None

            if row._weightExists:

                self._weight = row._weight

                self._weightExists = True

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

        result += Parser.extendedValueToXML("stateId", self._stateId)

        result += Parser.valueToXML(
            "calDeviceName", CalibrationDevice.name(self._calDeviceName)
        )

        result += Parser.valueToXML("sig", self._sig)

        result += Parser.valueToXML("ref", self._ref)

        result += Parser.valueToXML("onSky", self._onSky)

        if self._weightExists:

            result += Parser.valueToXML("weight", self._weight)

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
                "xmlrow is not a string or a minidom.Element", "StateTable"
            )

        if rowdom.nodeName != "row":
            raise ConversionException("the argument is not a row", "StateTable")

        # intrinsic attribute values

        stateIdNode = rowdom.getElementsByTagName("stateId")[0]

        self._stateId = Tag(stateIdNode.firstChild.data)

        calDeviceNameNode = rowdom.getElementsByTagName("calDeviceName")[0]

        self._calDeviceName = CalibrationDevice.newCalibrationDevice(
            calDeviceNameNode.firstChild.data
        )

        sigNode = rowdom.getElementsByTagName("sig")[0]

        self._sig = bool(sigNode.firstChild.data)

        refNode = rowdom.getElementsByTagName("ref")[0]

        self._ref = bool(refNode.firstChild.data)

        onSkyNode = rowdom.getElementsByTagName("onSky")[0]

        self._onSky = bool(onSkyNode.firstChild.data)

        weightNode = rowdom.getElementsByTagName("weight")
        if len(weightNode) > 0:

            self._weight = float(weightNode[0].firstChild.data)

            self._weightExists = True

    def toBin(self):
        print("not yet implemented")

    # Intrinsic Table Attributes

    # ===> Attribute stateId

    _stateId = Tag()

    def getStateId(self):
        """
        Get stateId.
        return stateId as Tag
        """

        # make sure it is a copy of Tag
        return Tag(self._stateId)

    def setStateId(self, stateId):
        """
        Set stateId with the specified Tag value.
        stateId The Tag value to which stateId is to be set.
        The value of stateId can be anything allowed by the Tag constructor.

        Raises a ValueError If an attempt is made to change a part of the key after is has been added to the table.

        """

        if self._hasBeenAdded:
            raise ValueError(
                "Attempt to change the stateId field, which is part of the key, after this row has been added to this table."
            )

        self._stateId = Tag(stateId)

    # ===> Attribute calDeviceName

    _calDeviceName = CalibrationDevice.from_int(0)

    def getCalDeviceName(self):
        """
        Get calDeviceName.
        return calDeviceName as CalibrationDevice
        """

        return self._calDeviceName

    def setCalDeviceName(self, calDeviceName):
        """
        Set calDeviceName with the specified CalibrationDevice value.
        calDeviceName The CalibrationDevice value to which calDeviceName is to be set.


        """

        self._calDeviceName = CalibrationDevice(calDeviceName)

    # ===> Attribute sig

    _sig = None

    def getSig(self):
        """
        Get sig.
        return sig as bool
        """

        return self._sig

    def setSig(self, sig):
        """
        Set sig with the specified bool value.
        sig The bool value to which sig is to be set.


        """

        self._sig = bool(sig)

    # ===> Attribute ref

    _ref = None

    def getRef(self):
        """
        Get ref.
        return ref as bool
        """

        return self._ref

    def setRef(self, ref):
        """
        Set ref with the specified bool value.
        ref The bool value to which ref is to be set.


        """

        self._ref = bool(ref)

    # ===> Attribute onSky

    _onSky = None

    def getOnSky(self):
        """
        Get onSky.
        return onSky as bool
        """

        return self._onSky

    def setOnSky(self, onSky):
        """
        Set onSky with the specified bool value.
        onSky The bool value to which onSky is to be set.


        """

        self._onSky = bool(onSky)

    # ===> Attribute weight, which is optional
    _weightExists = False

    _weight = None

    def isWeightExists(self):
        """
        The attribute weight is optional. Return True if this attribute exists.
        return True if and only if the weight attribute exists.
        """
        return self._weightExists

    def getWeight(self):
        """
        Get weight, which is optional.
        return weight as float
        raises ValueError If weight does not exist.
        """
        if not self._weightExists:
            raise ValueError(
                "Attempt to access a non-existent attribute.  The "
                + weight
                + " attribute in table State does not exist!"
            )

        return self._weight

    def setWeight(self, weight):
        """
        Set weight with the specified float value.
        weight The float value to which weight is to be set.


        """

        self._weight = float(weight)

        self._weightExists = True

    def clearWeight(self):
        """
        Mark weight, which is an optional field, as non-existent.
        """
        self._weightExists = False

    # Extrinsic Table Attributes

    # Links

    # comparison methods

    def compareNoAutoInc(self, calDeviceName, sig, ref, onSky):
        """
        Compare each attribute except the autoincrementable one of this StateRow with
        the corresponding parameters and return True if there is a match and False otherwise.
        """

        # calDeviceName is a CalibrationDevice, compare using the == operator on the getValue() output
        if not (self._calDeviceName.getValue() == calDeviceName.getValue()):
            return False

        # sig is a bool, compare using the == operator.
        if not (self._sig == sig):
            return False

        # ref is a bool, compare using the == operator.
        if not (self._ref == ref):
            return False

        # onSky is a bool, compare using the == operator.
        if not (self._onSky == onSky):
            return False

        return True

    def equalByRequiredValue(self, otherRow):
        """
        Return True if all required attributes of the value part are equal to their homologues
        in otherRow and False otherwise.
        """

        return self.compareRequiredValue(
            otherRow.getCalDeviceName(),
            otherRow.getSig(),
            otherRow.getRef(),
            otherRow.getOnSky(),
        )

    def compareRequiredValue(self, calDeviceName, sig, ref, onSky):

        # calDeviceName is a CalibrationDevice, compare using the == operator on the getValue() output
        if not (self._calDeviceName.getValue() == calDeviceName.getValue()):
            return False

        # sig is a bool, compare using the == operator.
        if not (self._sig == sig):
            return False

        # ref is a bool, compare using the == operator.
        if not (self._ref == ref):
            return False

        # onSky is a bool, compare using the == operator.
        if not (self._onSky == onSky):
            return False

        return True
