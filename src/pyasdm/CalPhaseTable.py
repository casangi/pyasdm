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
# File CalPhaseTable.py
#

import pyasdm.ASDM

from .CalPhaseRow import CalPhaseRow
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class CalPhaseTable(Representable):
    """
    The CalPhaseTable class is an Alma table.

     Role
     Result of the phase calibration performed by TelCal.

     Generated from model's revision -1, branch

     Attributes of CalPhase

                  Key

    basebandName BasebandName identifies the baseband.

    receiverBand ReceiverBand identifies the receiver band.

    atmPhaseCorrection AtmPhaseCorrection  describes how the atmospheric phase correction has been applied.

    calDataId Tag refers to a unique row in CalData Table.

    calReductionId Tag refers to a unique row in CalReduction Table.



                  Value (Mandatory)

    startValidTime ArrayTime  the start time of result validity period.

    endValidTime ArrayTime  the end time of result validity period.

    numBaseline int  the number of baselines.

    numReceptor int  the number of receptors.

    ampli float []  []   numReceptor, numBaseline  the amplitudes (one value per receptor per baseline).

    antennaNames str []  []   numBaseline, 2  the names of the antennas (one pair of strings per baseline).

    baselineLengths Length []   numBaseline  the physical lengths of the baselines (one value per baseline).

    decorrelationFactor float []  []   numReceptor, numBaseline  the decorrelation factors (one value per receptor per baseline).

    direction Angle []   2  the direction of the source.

    frequencyRange Frequency []   2  the frequency range over which the result is valid.

    integrationTime Interval  the integration duration for a data point.

    phase float []  []   numReceptor, numBaseline  the phases of the averaged interferometer signal (one value per receptor per baseline).

    polarizationTypes PolarizationType []   numReceptor  identifies the polarization types of the receptors (one value per receptor).

    phaseRMS float []  []   numReceptor, numBaseline  the RMS of phase fluctuations relative to the average signal (one value per receptor per baseline).

    statPhaseRMS float []  []   numReceptor, numBaseline  the RMS of phase deviations expected from the thermal fluctuations (one value per receptor per baseline).



                  Value (Optional)

    correctionValidity bool []   numBaseline  the deduced validity of atmospheric path length correction (from water vapor radiometers).

    numAntenna int  the number of antennas. Defines the size \texttt{singleAntennaName}, \texttt{phaseAnt}, \texttt{phaseAntRMS}. One must pay attention to the fact that \numBaseline  and  \numAntenna  must verify the the relation  : \numBaseline == \numAntenna * (  \numAntenna - 1 )  / 2



    singleAntennaName str []   numAntenna  the ordered list of antenna names. The size of the array must be equal to the number of antennas.

    refAntennaName str   the name of the antenna used as a reference to get the antenna-based phases.

    phaseAnt float []  []   numReceptor, numAntenna  the antenna based phase solution averaged over the scan (one value per receptor per antenna). See singleAntennaName for the association of the values of this array with the antennas.

    phaseAntRMS float []  []   numReceptor, numAntenna  the RMS of the phase fluctuations relative to the antenna based average phase (one value per receptor per antenna). See singleAntennaName for the association of the values of this array with the antennas.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "CalPhase"

    # the list of field names that make up key 'key'.
    _key = [
        "basebandName",
        "receiverBand",
        "atmPhaseCorrection",
        "calDataId",
        "calReductionId",
    ]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = False  # if True archive binary else archive XML
    _fileAsBin = False  # if True file binary else file XML

    # A list to store the CalPhaseRow instances
    _privateRows = []

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on baselineLengths during an add operation on the table
    _baselineLengthsEqTolerance = Length(0.0)

    def setBaselineLengthsEqTolerance(self, tolerance):
        """
        A setter for the tolerance on baselineLengths
        """
        self._baselineLengthsEqTolerance = Length(tolerance)

    # A getter for the tolerance on baselineLengths
    def getBaselineLengthsEqTolerance(self):
        """
        A getter for the tolerance on baselineLengths
        """
        return self._baselineLengthsEqTolerance

    # The tolerance which will be used on direction during an add operation on the table
    _directionEqTolerance = Angle(0.0)

    def setDirectionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on direction
        """
        self._directionEqTolerance = Angle(tolerance)

    # A getter for the tolerance on direction
    def getDirectionEqTolerance(self):
        """
        A getter for the tolerance on direction
        """
        return self._directionEqTolerance

    # The tolerance which will be used on frequencyRange during an add operation on the table
    _frequencyRangeEqTolerance = Frequency(0.0)

    def setFrequencyRangeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on frequencyRange
        """
        self._frequencyRangeEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on frequencyRange
    def getFrequencyRangeEqTolerance(self):
        """
        A getter for the tolerance on frequencyRange
        """
        return self._frequencyRangeEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    @staticmethod
    def Key(basebandName, receiverBand, atmPhaseCorrection, calDataId, calReductionId):
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
        Create a CalPhaseTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
        """
        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("CalPhaseTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("CalPhaseTable")
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
        Returns "CalPhaseTable" followed by the current size of the table
        between parenthesis.
        Example : CalPhaseTable(12)
        """
        return "CalPhaseTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = CalPhaseRow(self)
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
                newrow.getReceiverBand(),
                newrow.getAtmPhaseCorrection(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey(
                "["
                + x.getBasebandName()
                + "|"
                + x.getReceiverBand()
                + "|"
                + x.getAtmPhaseCorrection()
                + "|"
                + x.getCalDataId()
                + "|"
                + x.getCalReductionId()
                + "]",
                "CalPhase",
            )

        row.add(newrow)
        privateRows.add(newrow)
        newrow.isAdded()
        return newrow

    def newRow(
        self,
        basebandName,
        receiverBand,
        atmPhaseCorrection,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numBaseline,
        numReceptor,
        ampli,
        antennaNames,
        baselineLengths,
        decorrelationFactor,
        direction,
        frequencyRange,
        integrationTime,
        phase,
        polarizationTypes,
        phaseRMS,
        statPhaseRMS,
    ):
        """
        Create a new CalPhaseRow. The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = CalPhaseRow(self)

        thisRow.setBasebandName(basebandName)

        thisRow.setReceiverBand(receiverBand)

        thisRow.setAtmPhaseCorrection(atmPhaseCorrection)

        thisRow.setCalDataId(calDataId)

        thisRow.setCalReductionId(calReductionId)

        thisRow.setStartValidTime(startValidTime)

        thisRow.setEndValidTime(endValidTime)

        thisRow.setNumBaseline(numBaseline)

        thisRow.setNumReceptor(numReceptor)

        thisRow.setAmpli(ampli)

        thisRow.setAntennaNames(antennaNames)

        thisRow.setBaselineLengths(baselineLengths)

        thisRow.setDecorrelationFactor(decorrelationFactor)

        thisRow.setDirection(direction)

        thisRow.setFrequencyRange(frequencyRange)

        thisRow.setIntegrationTime(integrationTime)

        thisRow.setPhase(phase)

        thisRow.setPolarizationTypes(polarizationTypes)

        thisRow.setPhaseRMS(phaseRMS)

        thisRow.setStatPhaseRMS(statPhaseRMS)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new CalPhaseRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new CalPhaseRow with default values for its attributes.
        """

        return CalPhaseRow(self, row)

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
                newrow.getReceiverBand(),
                newrow.getAtmPhaseCorrection(),
                newrow.getCalDataId(),
                newrow.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey("Duplicate key exception in ", "CalPhaseTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of CalPhaseRow
        """
        return self._privateRows

    def getRowByKey(
        self, basebandName, receiverBand, atmPhaseCorrection, calDataId, calReductionId
    ):
        """
        Returns a CalPhaseRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        @param basebandName.

        @param receiverBand.

        @param atmPhaseCorrection.

        @param calDataId.

        @param calReductionId.

        """
        for row in self._privateRows:

            if row.getBasebandName() != basebandName:
                continue

            if row.getReceiverBand() != receiverBand:
                continue

            if row.getAtmPhaseCorrection() != atmPhaseCorrection:
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
        receiverBand,
        atmPhaseCorrection,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numBaseline,
        numReceptor,
        ampli,
        antennaNames,
        baselineLengths,
        decorrelationFactor,
        direction,
        frequencyRange,
        integrationTime,
        phase,
        polarizationTypes,
        phaseRMS,
        statPhaseRMS,
    ):
        """
                Look up the table for a row whose all attributes
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param basebandName.

        param receiverBand.

        param atmPhaseCorrection.

        param calDataId.

        param calReductionId.

        param startValidTime.

        param endValidTime.

        param numBaseline.

        param numReceptor.

        param ampli.

        param antennaNames.

        param baselineLengths.

        param decorrelationFactor.

        param direction.

        param frequencyRange.

        param integrationTime.

        param phase.

        param polarizationTypes.

        param phaseRMS.

        param statPhaseRMS.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                basebandName,
                receiverBand,
                atmPhaseCorrection,
                calDataId,
                calReductionId,
                startValidTime,
                endValidTime,
                numBaseline,
                numReceptor,
                ampli,
                antennaNames,
                baselineLengths,
                decorrelationFactor,
                direction,
                frequencyRange,
                integrationTime,
                phase,
                polarizationTypes,
                phaseRMS,
                statPhaseRMS,
            ):
                return row

        return None

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for CalPhase (CalPhaseTable.xsd).

        Returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<CalPhaseTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clphas="http://Alma/XASDM/CalPhaseTable" xsi:schemaLocation="http://Alma/XASDM/CalPhaseTable http://almaobservatory.org/XML/XASDM/4/CalPhaseTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</CalPhaseTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a CalPhase (CalPhaseTable.xsd).
        """
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of CalPhaseTable.
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "CalPhaseTable":
            raise ConversionException(
                "XML is not from a the expected table", "CalPhaseTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException("schemaVersion not found in XML", "CalPhaseTable")
        versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "CalPhaseTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "CalPhaseTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "CalPhaseTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "CalPhaseTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "CalPhaseTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "CalPhaseTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "CalPhaseTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalPhaseTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalPhaseTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalPhaseTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "CalPhaseTable",
            )

        if os.path.exists(os.path.join(directory, "CalPhase.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalPhase.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalPhase table", "CalPhaseTable"
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
        with open(os.path.join(directory, "CalPhase.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException("CalPhase.xml is empty", "CalPhaseTable")

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'CalPhase.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'CalPhase.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalPhase)"
                % directory,
                "CalPhaseTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for CalPhase")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "CalPhase.xml")
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
