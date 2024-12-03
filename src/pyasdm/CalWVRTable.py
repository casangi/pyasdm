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
# File CalWVRTable.py
#

import pyasdm.ASDM

from .CalWVRRow import CalWVRRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class CalWVRTable(Representable):
    """
    The CalWVRTable class is an Alma table.

     Role
     Result of the water vapour radiometric  calibration performed by TelCal.

     Generated from model's revision -1, branch

     Attributes of CalWVR

                  Key

    antennaName str the name of the antenna.

    calDataId Tag refers to a unique row in CalData Table.

    calReductionId Tag refers to unique row  in CalReductionTable.



                  Value (Mandatory)

    startValidTime ArrayTime  the start time of result validity period.

    endValidTime ArrayTime  the end time of result validity period.

    wvrMethod WVRMethod  identifies the method used for the calibration.

    numInputAntennas int  the number of input antennas (i.e. equiped with functional WVRs).

    inputAntennaNames str []   numInputAntennas  the names of the input antennas (one string per antenna).

    numChan int  the number of frequency channels in the WVR receiver.

    chanFreq Frequency []   numChan  the channel frequencies (one value per channel).

    chanWidth Frequency []   numChan  the widths of the channels (one value per channel).

    refTemp Temperature []  []   numInputAntennas, numChan  the reference temperatures (one value per input antenna per channel).

    numPoly int  the number of polynomial coefficients.

    pathCoeff float []  []  []   numInputAntennas, numChan, numPoly  the path length coefficients (one value per input antenna per channel per polynomial coefficient).

    polyFreqLimits Frequency []   2  the limits of the interval of frequencies for which the path length coefficients are computed.

    wetPath float []   numPoly  The wet path as a function frequency (expressed as a polynomial).

    dryPath float []   numPoly  The dry path as a function frequency (expressed as a polynomial).

    water Length  The precipitable water vapor corresponding to the reference model.



                  Value (Optional)

    tauBaseline float  Constant opacity term (frequency independent).


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "CalWVR"

    # the list of field names that make up key 'key'.
    _key = ["antennaName", "calDataId", "calReductionId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = False  # if True archive binary else archive XML
    _fileAsBin = False  # if True file binary else file XML

    # A list to store the CalWVRRow instances
    _privateRows = []

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on chanFreq during an add operation on the table
    _chanFreqEqTolerance = Frequency(0.0)

    def setChanFreqEqTolerance(self, tolerance):
        """
        A setter for the tolerance on chanFreq
        """
        self._chanFreqEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on chanFreq
    def getChanFreqEqTolerance(self):
        """
        A getter for the tolerance on chanFreq
        """
        return self._chanFreqEqTolerance

    # The tolerance which will be used on chanWidth during an add operation on the table
    _chanWidthEqTolerance = Frequency(0.0)

    def setChanWidthEqTolerance(self, tolerance):
        """
        A setter for the tolerance on chanWidth
        """
        self._chanWidthEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on chanWidth
    def getChanWidthEqTolerance(self):
        """
        A getter for the tolerance on chanWidth
        """
        return self._chanWidthEqTolerance

    # The tolerance which will be used on refTemp during an add operation on the table
    _refTempEqTolerance = Temperature(0.0)

    def setRefTempEqTolerance(self, tolerance):
        """
        A setter for the tolerance on refTemp
        """
        self._refTempEqTolerance = Temperature(tolerance)

    # A getter for the tolerance on refTemp
    def getRefTempEqTolerance(self):
        """
        A getter for the tolerance on refTemp
        """
        return self._refTempEqTolerance

    # The tolerance which will be used on polyFreqLimits during an add operation on the table
    _polyFreqLimitsEqTolerance = Frequency(0.0)

    def setPolyFreqLimitsEqTolerance(self, tolerance):
        """
        A setter for the tolerance on polyFreqLimits
        """
        self._polyFreqLimitsEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on polyFreqLimits
    def getPolyFreqLimitsEqTolerance(self):
        """
        A getter for the tolerance on polyFreqLimits
        """
        return self._polyFreqLimitsEqTolerance

    # The tolerance which will be used on water during an add operation on the table
    _waterEqTolerance = Length(0.0)

    def setWaterEqTolerance(self, tolerance):
        """
        A setter for the tolerance on water
        """
        self._waterEqTolerance = Length(tolerance)

    # A getter for the tolerance on water
    def getWaterEqTolerance(self):
        """
        A getter for the tolerance on water
        """
        return self._waterEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    @staticmethod
    def Key(antennaName, calDataId, calReductionId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        The parameter values are assumed to be the appropriate type for that parameter.
        """
        result = ""

        result += calDataId.toString() + "_"

        result += calReductionId.toString() + "_"

        return result

    def __init__(self, container):
        """
        Create a CalWVRTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("CalWVRTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("CalWVRTable")
        self._entity.setEntityVersion("1")
        self._entity.setInstanceVersion("1")

        # the default table has no rows and so is presentInMemory
        self._presentInMemory = True
        self._loadInProgress = False

    def setNotPresentInMemory(self):
        """
        Set the state to indicate it is not present in memory and needs to be loaded before being used.
        This is used by the container class when loaded from a file and this table is present with non-zero rows.
        Tables are loaded on demand when the get function in the container for that table is used.
        """
        self._presentInMemory = False

    def checkPresenceInMemory(self):
        """
        Check if the table is present in memory. If not, load the table from the file using the
        directory of the container.
        """
        # NOTE: if setFromFile throws an exception then presentInMemory will remain False
        # and loadInProgress will remain True, preventing another attempt at loading.
        # more complex solutions are then necessary to read that file and it's not worth
        # complicating this code here to handle a need to eventually try again to reload that file
        if not self._presentInMemory and not self._loadInProgress:
            self._loadInProgress = True
            self.setFromFile(self.getContainer().getDirectory())
            self._presentInMemory = True
            self._loadInProgress = False

    def getContainer(self):
        """
        Return the container to which this table belongs.
        """
        return self._container

    def size(self):
        """
        Return the number of rows in the table.
        """
        return len(self._privateRows)

    def getName(self):
        """
        Return the name of this table.
        """
        return self._tableName

    def toString(self):
        """
        Returns "CalWVRTable" followed by the current size of the table
        between parenthesis.
        Example : CalWVRTable(12)
        """
        return "CalWVRTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = CalWVRRow(self)
        return thisRow

    def add(self, newrow):
        """
        Add a row.
        raises a DuplicateKey if the new row has a key that is already in the table.
        If newrow is a list then this method is called recursively on each element of that list.
        In that case None is returned.
        returns newrow
        """
        if isinstance(newrow, list):
            for thisrow in newrow:
                self.add(thisrow)
            # return None for the list case only
            return None

        # the single row case

        if (
            self.getRowByKey(
                newrow.getAntennaName(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey(
                "["
                + x.getAntennaName()
                + "|"
                + x.getCalDataId()
                + "|"
                + x.getCalReductionId()
                + "]",
                "CalWVR",
            )

        row.add(newrow)
        privateRows.add(newrow)
        newrow.isAdded()
        return newrow

    def newRow(
        self,
        antennaName,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        wvrMethod,
        numInputAntennas,
        inputAntennaNames,
        numChan,
        chanFreq,
        chanWidth,
        refTemp,
        numPoly,
        pathCoeff,
        polyFreqLimits,
        wetPath,
        dryPath,
        water,
    ):
        """
        Create a new CalWVRRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = CalWVRRow(self)

        thisRow.setAntennaName(antennaName)

        thisRow.setCalDataId(calDataId)

        thisRow.setCalReductionId(calReductionId)

        thisRow.setStartValidTime(startValidTime)

        thisRow.setEndValidTime(endValidTime)

        thisRow.setWvrMethod(wvrMethod)

        thisRow.setNumInputAntennas(numInputAntennas)

        thisRow.setInputAntennaNames(inputAntennaNames)

        thisRow.setNumChan(numChan)

        thisRow.setChanFreq(chanFreq)

        thisRow.setChanWidth(chanWidth)

        thisRow.setRefTemp(refTemp)

        thisRow.setNumPoly(numPoly)

        thisRow.setPathCoeff(pathCoeff)

        thisRow.setPolyFreqLimits(polyFreqLimits)

        thisRow.setWetPath(wetPath)

        thisRow.setDryPath(dryPath)

        thisRow.setWater(water)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new CalWVRRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new CalWVRRow with default values for its attributes.
        """

        return CalWVRRow(self, row)

    # ====> Append a row to its table.

    def _checkAndAdd(self, newrow):
        """
        A private method to append a row to its table, used by input conversion
        methods. Not intended for external use.

        If this table has an autoincrementable attribute then check if newrow verifies the rule of uniqueness and raise an exception if not.
        Returns newrow.
        """

        if (
            self.getRowByKey(
                newrow.getAntennaName(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey("Duplicate key exception in ", "CalWVRTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of CalWVRRow
        """
        return self._privateRows

    def getRowByKey(self, antennaName, calDataId, calReductionId):
        """
        Returns a CalWVRRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        @param antennaName.

        @param calDataId.

        @param calReductionId.

        """
        for row in self._privateRows:

            if row.getAntennaName() != antennaName:
                continue

            if not row.getCalDataId().equals(calDataId):
                continue

            if not row.getCalReductionId().equals(calReductionId):
                continue

            # this row matches these parameters
            return row
        # no match found
        return None

    def lookup(
        self,
        antennaName,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        wvrMethod,
        numInputAntennas,
        inputAntennaNames,
        numChan,
        chanFreq,
        chanWidth,
        refTemp,
        numPoly,
        pathCoeff,
        polyFreqLimits,
        wetPath,
        dryPath,
        water,
    ):
        """
                Look up the table for a row whose all attributes
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param antennaName.

        param calDataId.

        param calReductionId.

        param startValidTime.

        param endValidTime.

        param wvrMethod.

        param numInputAntennas.

        param inputAntennaNames.

        param numChan.

        param chanFreq.

        param chanWidth.

        param refTemp.

        param numPoly.

        param pathCoeff.

        param polyFreqLimits.

        param wetPath.

        param dryPath.

        param water.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                antennaName,
                calDataId,
                calReductionId,
                startValidTime,
                endValidTime,
                wvrMethod,
                numInputAntennas,
                inputAntennaNames,
                numChan,
                chanFreq,
                chanWidth,
                refTemp,
                numPoly,
                pathCoeff,
                polyFreqLimits,
                wetPath,
                dryPath,
                water,
            ):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for CalWVR (CalWVRTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<CalWVRTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clwvr="http://Alma/XASDM/CalWVRTable" xsi:schemaLocation="http://Alma/XASDM/CalWVRTable http://almaobservatory.org/XML/XASDM/4/CalWVRTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</CalWVRTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a CalWVR (CalWVRTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of CalWVRTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "CalWVRTable":
            raise ConversionException(
                "XML is not from a the expected table", "CalWVRTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException("schemaVersion not found in XML", "CalWVRTable")
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "CalWVRTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "CalWVRTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "CalWVRTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "CalWVRTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "CalWVRTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "CalWVRTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "CalWVRTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalWVRTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalWVRTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalWVRTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "CalWVRTable",
            )

        if os.path.exists(os.path.join(directory, "CalWVR.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalWVR.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalWVR table", "CalWVRTable"
            )

    def setFromMIMEFile(self, directory):
        print("setFromMIMEFile not implemented yet")

    def setFromXMLFile(self, directory):
        """
        This is the function used by setFromFile when the file is an XML file
        """

        # setFromFile has already established that this exists
        # read the entire file into a string
        xmlstr = None
        with open(os.path.join(directory, "CalWVR.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("CalWVR.xml is empty", "CalWVRTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'CalWVR.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'CalWVR.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalWVR)"
                % directory,
                "CalWVRTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for CalWVR")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "CalWVR.xml")
            if os.path.exists(filePath):
                # try to delete it, this will raise an exception if the user does not have permission to do that
                os.remove(filePath)
            with open(filePath, "w") as f:
                f.write(self.toXML())
                f.close()

    def getEntity(self):
        """
        Returns the table's entity.
        """
        return self._entity

    def setEntity(self, e):
        """
        Set the table's entity
        The parameter, e, must be an Entity
        """
        if not isinstance(e, Entity):
            raise (ValueError("setEntity must use an Entity value"))

        self._entity = Entity(e)

    def getVersion(self):
        return self._version

    def setVersion(self, version):
        if not isinstance(version, int):
            raise ValueError("version must be an int")

        self._version = version
