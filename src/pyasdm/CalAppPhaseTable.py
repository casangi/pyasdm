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
# File CalAppPhaseTable.py
#

import pyasdm.ASDM

from .CalAppPhaseRow import CalAppPhaseRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class CalAppPhaseTable(Representable):
    """
    The CalAppPhaseTable class is an Alma table.

     Role
     The CalAppPhase table is relevant to the ALMA observatory when the antennas are being phased to form a coherent sum during the observation. For each scan, the table provides information about which antennas are included in the sum, their relative phase adjustments, the efficiency of the sum (relative to best performance) and the quality of each antenna participating in the system. This data is used in real-time to provide the phased sum signal, and after the observation to analyze the result.

     Generated from model's revision -1, branch

     Attributes of CalAppPhase

                  Key

    basebandName BasebandName identifies the baseband.

    scanNumber int The number of the scan processed by TELCAL. Along with an ExecBlock Id (which should be ExecBlock\_0 most of the time), the value of scanNumber can be used as the key to retrieve informations related to the scan (e.g. its start time).

    calDataId Tag identifies a unique row in the CalData table.

    calReductionId Tag identifies a unique row in the CalReduction table.



                  Value (Mandatory)

    startValidTime ArrayTime  start of phasing solution validity.

    endValidTime ArrayTime  end of phasing solution validity.

    adjustTime ArrayTime  The time of the last adjustment to the phasing analysis via the \c ParameterTuning  interface.

    adjustToken str  A parameter supplied via the \c ParameterTuning interface to indicate the form of adjustment(s) made at adjustTime. Note that TELCAL merely passes this datum and adjustTime through to this table.

    phasingMode str  The mode in which the phasing system is being operated.

    numPhasedAntennas int  the number of antennas in phased sum, \f$N_p\f$.

    phasedAntennas str []   numPhasedAntennas  the names of the phased antennas.

    refAntennaIndex int  the index of the reference antenna in the array \c phasedAntennas . It must be an integer value in the interval \f$ [0, N_p-1]\f$.

    candRefAntennaIndex int  tne index of a candidate (new) reference antenna in the array phasedAntennas; it must be a integer in the interval \f$[0, N_p-1]\f$.

    phasePacking str  how to unpack \c phaseValues.

    numReceptors int  the number of receptors per antenna, \f$N_r\f$.The number (\f$N_r \le 2 \f$) of receptors per antenna, usually two (polarizations), but it might be one in special cases.

    numChannels int  the number of data channels, \f$N_d\f$.

    numPhaseValues int  The number  of phase data values present in the table, \f$N_v\f$.

    phaseValues float []   numPhaseValues  the array of phase data values.

    numCompare int  the number of comparison antennas, \f$N_c\f$.

    numEfficiencies int  the number of efficiencies, \f$N_e\f$.

    compareArray str []   numCompare  the names of the comparison antennas.

    efficiencyIndices int []   numEfficiencies  indices of the antenna(s) in \c compareArray used to calculate \c efficiencies; they must be distinct integers in the interval \f$[0, N_c]\f$.

    efficiencies float []  []   numEfficiencies, numChannels  an array of efficiencies of phased sum.

    quality float []   numPhasedAntennas+numCompare  quality of phased antennas.

    phasedSumAntenna str  the name of the phased sum antenna.



                  Value (Optional)

    typeSupports str  encoding of supporting data values.

    numSupports int  the number of supporting data values, \f$N_s\f$.

    phaseSupports float []   numSupports  an array of supporting data values.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "CalAppPhase"

    # the list of field names that make up key 'key'.
    _key = ["basebandName", "scanNumber", "calDataId", "calReductionId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = True  # if True archive binary else archive XML
    _fileAsBin = True  # if True file binary else file XML

    # A list to store the CalAppPhaseRow instances
    _privateRows = []

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    @staticmethod
    def Key(basebandName, scanNumber, calDataId, calReductionId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        The parameter values are assumed to be the appropriate type for that parameter.
        """
        result = ""

        result += scanNumber() + "_"

        result += calDataId.toString() + "_"

        result += calReductionId.toString() + "_"

        return result

    def __init__(self, container):
        """
        Create a CalAppPhaseTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("CalAppPhaseTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("CalAppPhaseTable")
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
        Returns "CalAppPhaseTable" followed by the current size of the table
        between parenthesis.
        Example : CalAppPhaseTable(12)
        """
        return "CalAppPhaseTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = CalAppPhaseRow(self)
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
                newrow.getBasebandName(),
                newrow.getScanNumber(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey(
                "["
                + x.getBasebandName()
                + "|"
                + x.getScanNumber()
                + "|"
                + x.getCalDataId()
                + "|"
                + x.getCalReductionId()
                + "]",
                "CalAppPhase",
            )

        row.add(newrow)
        privateRows.add(newrow)
        newrow.isAdded()
        return newrow

    def newRow(
        self,
        basebandName,
        scanNumber,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        adjustTime,
        adjustToken,
        phasingMode,
        numPhasedAntennas,
        phasedAntennas,
        refAntennaIndex,
        candRefAntennaIndex,
        phasePacking,
        numReceptors,
        numChannels,
        numPhaseValues,
        phaseValues,
        numCompare,
        numEfficiencies,
        compareArray,
        efficiencyIndices,
        efficiencies,
        quality,
        phasedSumAntenna,
    ):
        """
        Create a new CalAppPhaseRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = CalAppPhaseRow(self)

        thisRow.setBasebandName(basebandName)

        thisRow.setScanNumber(scanNumber)

        thisRow.setCalDataId(calDataId)

        thisRow.setCalReductionId(calReductionId)

        thisRow.setStartValidTime(startValidTime)

        thisRow.setEndValidTime(endValidTime)

        thisRow.setAdjustTime(adjustTime)

        thisRow.setAdjustToken(adjustToken)

        thisRow.setPhasingMode(phasingMode)

        thisRow.setNumPhasedAntennas(numPhasedAntennas)

        thisRow.setPhasedAntennas(phasedAntennas)

        thisRow.setRefAntennaIndex(refAntennaIndex)

        thisRow.setCandRefAntennaIndex(candRefAntennaIndex)

        thisRow.setPhasePacking(phasePacking)

        thisRow.setNumReceptors(numReceptors)

        thisRow.setNumChannels(numChannels)

        thisRow.setNumPhaseValues(numPhaseValues)

        thisRow.setPhaseValues(phaseValues)

        thisRow.setNumCompare(numCompare)

        thisRow.setNumEfficiencies(numEfficiencies)

        thisRow.setCompareArray(compareArray)

        thisRow.setEfficiencyIndices(efficiencyIndices)

        thisRow.setEfficiencies(efficiencies)

        thisRow.setQuality(quality)

        thisRow.setPhasedSumAntenna(phasedSumAntenna)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new CalAppPhaseRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new CalAppPhaseRow with default values for its attributes.
        """

        return CalAppPhaseRow(self, row)

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
                newrow.getBasebandName(),
                newrow.getScanNumber(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey("Duplicate key exception in ", "CalAppPhaseTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of CalAppPhaseRow
        """
        return self._privateRows

    def getRowByKey(self, basebandName, scanNumber, calDataId, calReductionId):
        """
        Returns a CalAppPhaseRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        @param basebandName.

        @param scanNumber.

        @param calDataId.

        @param calReductionId.

        """
        for row in self._privateRows:

            if row.getBasebandName() != basebandName:
                continue

            if row.getScanNumber() != scanNumber:
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
        basebandName,
        scanNumber,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        adjustTime,
        adjustToken,
        phasingMode,
        numPhasedAntennas,
        phasedAntennas,
        refAntennaIndex,
        candRefAntennaIndex,
        phasePacking,
        numReceptors,
        numChannels,
        numPhaseValues,
        phaseValues,
        numCompare,
        numEfficiencies,
        compareArray,
        efficiencyIndices,
        efficiencies,
        quality,
        phasedSumAntenna,
    ):
        """
                Look up the table for a row whose all attributes
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param basebandName.

        param scanNumber.

        param calDataId.

        param calReductionId.

        param startValidTime.

        param endValidTime.

        param adjustTime.

        param adjustToken.

        param phasingMode.

        param numPhasedAntennas.

        param phasedAntennas.

        param refAntennaIndex.

        param candRefAntennaIndex.

        param phasePacking.

        param numReceptors.

        param numChannels.

        param numPhaseValues.

        param phaseValues.

        param numCompare.

        param numEfficiencies.

        param compareArray.

        param efficiencyIndices.

        param efficiencies.

        param quality.

        param phasedSumAntenna.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                basebandName,
                scanNumber,
                calDataId,
                calReductionId,
                startValidTime,
                endValidTime,
                adjustTime,
                adjustToken,
                phasingMode,
                numPhasedAntennas,
                phasedAntennas,
                refAntennaIndex,
                candRefAntennaIndex,
                phasePacking,
                numReceptors,
                numChannels,
                numPhaseValues,
                phaseValues,
                numCompare,
                numEfficiencies,
                compareArray,
                efficiencyIndices,
                efficiencies,
                quality,
                phasedSumAntenna,
            ):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for CalAppPhase (CalAppPhaseTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<CalAppPhaseTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:calaph="http://Alma/XASDM/CalAppPhaseTable" xsi:schemaLocation="http://Alma/XASDM/CalAppPhaseTable http://almaobservatory.org/XML/XASDM/4/CalAppPhaseTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</CalAppPhaseTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a CalAppPhase (CalAppPhaseTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of CalAppPhaseTable.
        if (
            not xmldom.hasChildNodes()
            or xmldom.firstChild.nodeName != "CalAppPhaseTable"
        ):
            raise ConversionException(
                "XML is not from a the expected table", "CalAppPhaseTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException(
                "schemaVersion not found in XML", "CalAppPhaseTable"
            )
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "CalAppPhaseTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "CalAppPhaseTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "CalAppPhaseTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "CalAppPhaseTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "CalAppPhaseTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "CalAppPhaseTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "CalAppPhaseTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalAppPhaseTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalAppPhaseTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalAppPhaseTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "CalAppPhaseTable",
            )

        if os.path.exists(os.path.join(directory, "CalAppPhase.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalAppPhase.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalAppPhase table", "CalAppPhaseTable"
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
        with open(os.path.join(directory, "CalAppPhase.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("CalAppPhase.xml is empty", "CalAppPhaseTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'CalAppPhase.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'CalAppPhase.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalAppPhase)"
                % directory,
                "CalAppPhaseTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for CalAppPhase")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "CalAppPhase.xml")
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
