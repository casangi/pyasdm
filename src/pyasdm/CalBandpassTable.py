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
# File CalBandpassTable.py
#

import pyasdm.ASDM

from .CalBandpassRow import CalBandpassRow

# All of the extended types are imported
from pyasdm.types import *

# for BIN input and output
from pyasdm.ByteOrder import ByteOrder
from pyasdm.EndianInput import EndianInput
from pyasdm.EndianOutput import EndianOutput

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey
from .exceptions.UniquenessViolationException import UniquenessViolationException

from xml.dom import minidom

import os
import io


class CalBandpassTable:
    """
    The CalBandpassTable class is an Alma table.

    Role
    Result of passband calibration performed on-line by TelCal.

    Generated from model's revision -1, branch

    Attributes of CalBandpass

                 Key


    basebandName BasebandName identifies the baseband. </TD>



    sideband NetSideband identifies the first LO sideband. </TD>



    atmPhaseCorrection AtmPhaseCorrection qualifies how the atmospheric phase correction has been applied. </TD>



    typeCurve CalCurveType identifies the type of curve. </TD>



    receiverBand ReceiverBand identifies the receiver band. </TD>



    calDataId Tag refers to a unique row in CalData Table. </TD>



    calReductionId Tag refers to a unique row in CalReduction Table. </TD>




                 Value (Mandatory)

    startValidTime  ArrayTime  the start time of result validity period.

    endValidTime  ArrayTime  the end time of result validity period.

    numAntenna (numAntenna) int  the number of antennas.

    numPoly (numPoly) int  the number of coefficients of the polynomial.

    numReceptor (numReceptor) int  the number of receptors.

    antennaNames  str []   numAntenna  the names of the antennas.

    refAntennaName  str  the name of the reference antenna.

    freqLimits  Frequency []   2  the frequency range for the polynomial description of the passband.

    polarizationTypes  PolarizationType []   numReceptor  the polarizations of the receptors (one value per receptor).

    curve  float []  []  []   numAntenna, numReceptor, numPoly  the amplitude or phase coefficients, depending on the value of typeCurve (one array of numPoly values per antenna per receptor).

    reducedChiSquared  float []   numReceptor  measures the quality of the least squares fits (one value per receptor).



                 Value (Optional)

    numBaseline (numBaseline) int  the number of baselines.

    numFreq (numFreq) int  the number of frequency points.

    rms  float []  []   numReceptor, numBaseline  the amplitude or phase residuals ( one array of numBaseline values per receptor).

    frequencyRange  Frequency []   2  the frequency range over which the result is valid.

    numSpectralWindow (numSpectralWindow) int  The number of spectral windows.

    chanFreqStart  Frequency []   numSpectralWindow  the frequency of the first channel.

    chanFreqStep  Frequency []   numSpectralWindow  the increment between two successive frequencies.

    numSpectralWindowChan (numSpectralWindowChan) int []   numSpectralWindow  The number of channels for each spectral window.

    spectrum  float []  []  []   numAntenna, numReceptor, numFreq  The antenna-based spectrum per receptor averaging over the entire scan range.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # The name of this table.
    _tableName = "CalBandpass"

    # The list of field names that make up key 'key'.
    _key = [
        "basebandName",
        "sideband",
        "atmPhaseCorrection",
        "typeCurve",
        "receiverBand",
        "calDataId",
        "calReductionId",
    ]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # archive as bin not used by python implementation
    # _archiveAsBin = True # If True archive binary else archive XML
    _fileAsBin = True  # If True file binary else file XML

    # A data structure to store the CalBandpassRow s.
    # In all cases we maintain a private list of CalBandpassRow s.
    _privateRows = []

    # non-temporal ASDM in Java had a private row element here to also hold  CalBandpassRow s. Not needed in python.

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on freqLimits during an add operation on the table
    _freqLimitsEqTolerance = Frequency(0.0)

    def setFreqLimitsEqTolerance(self, tolerance):
        """
        A setter for the tolerance on freqLimits
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._freqLimitsEqTolerance = Frequency(tolerance)

    def getFreqLimitsEqTolerance(self):
        """
        A getter for the tolerance on freqLimits
        Returns the tolerance as a  Frequency
        """
        return self._freqLimitsEqTolerance

    # The tolerance which will be used on frequencyRange during an add operation on the table
    _frequencyRangeEqTolerance = Frequency(0.0)

    def setFrequencyRangeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on frequencyRange
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._frequencyRangeEqTolerance = Frequency(tolerance)

    def getFrequencyRangeEqTolerance(self):
        """
        A getter for the tolerance on frequencyRange
        Returns the tolerance as a  Frequency
        """
        return self._frequencyRangeEqTolerance

    # The tolerance which will be used on chanFreqStart during an add operation on the table
    _chanFreqStartEqTolerance = Frequency(0.0)

    def setChanFreqStartEqTolerance(self, tolerance):
        """
        A setter for the tolerance on chanFreqStart
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._chanFreqStartEqTolerance = Frequency(tolerance)

    def getChanFreqStartEqTolerance(self):
        """
        A getter for the tolerance on chanFreqStart
        Returns the tolerance as a  Frequency
        """
        return self._chanFreqStartEqTolerance

    # The tolerance which will be used on chanFreqStep during an add operation on the table
    _chanFreqStepEqTolerance = Frequency(0.0)

    def setChanFreqStepEqTolerance(self, tolerance):
        """
        A setter for the tolerance on chanFreqStep
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._chanFreqStepEqTolerance = Frequency(tolerance)

    def getChanFreqStepEqTolerance(self):
        """
        A getter for the tolerance on chanFreqStep
        Returns the tolerance as a  Frequency
        """
        return self._chanFreqStepEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up key key
        as a list of strings.
        """
        return self._key

    def Key(
        self,
        basebandName,
        sideband,
        atmPhaseCorrection,
        typeCurve,
        receiverBand,
        calDataId,
        calReductionId,
    ):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        """
        result = ""

        result += str(calDataId) + "_"

        result += str(calReductionId) + "_"

        return result

    def __init__(self, container):
        """
        Create a CalBandpassTable attached to container.

        container must be a ASDM instance
        All tables must know the container
        """

        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("CalBandpassTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("CalBandpassTable")
        self._entity.setEntityVersion("1")
        self._entity.setInstanceVersion("1")

        # the default table has no rows and so is presentInMemory
        self._presentInMemory = True
        self._loadInProgress = False

        self._privateRows = []

        self._version = 0

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
        # NOTE: if setFromFile raises an exception then presentInMemory will remain False
        # and loadInProgress will remain True, preventing another attempt at loading.
        # more complex solutions are then necessary to read that file and it's not worth
        # complicating this code here to handle a need to eventually try again to reload that file
        if not self._presentInMemory and not self._loadInProgress:
            # print("CalBandpass is not present in memory, setting from file")
            self._loadInProgress = True
            self.setFromFile(self.getContainer().getDirectory())
            self._presentInMemory = True
            self._loadInProgress = False

    def getContainer(self):
        """
        Return the container to which this table belongs.
        return a ASDM.
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

    def __str__(self):
        """
        Returns "CalBandpassTable" followed by the current size of the table
        between parenthesis.
        Example : CalBandpassTable(12)
        """
        return "CalBandpassTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = CalBandpassRow(self)
        return thisRow

    def add(self, x):
        """
        Add a row.
        raises a DuplicateKey Thrown if the new row has a key that is already in the table.
        If x is a list then this method is called recursively on each element of that list.
        In that case, None is returned.
        returns the row that was added.
        """

        if isinstance(x, list):
            for thisrow in x:
                # check on correct type of thisrow happens in add
                self.add(thisrow)
            # return None fo the list case only
            return None

        # the single row case
        if not isinstance(x, CalBandpassRow):
            raise ValueError("x must be a  CalBandpassRow instance.")

        if (
            self.getRowByKey(
                x.getBasebandName(),
                x.getSideband(),
                x.getAtmPhaseCorrection(),
                x.getTypeCurve(),
                x.getReceiverBand(),
                x.getCalDataId(),
                x.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey(
                "["
                + x.getBasebandName()
                + "|"
                + x.getSideband()
                + "|"
                + x.getAtmPhaseCorrection()
                + "|"
                + x.getTypeCurve()
                + "|"
                + x.getReceiverBand()
                + "|"
                + x.getCalDataId()
                + "|"
                + x.getCalReductionId()
                + "]",
                "CalBandpass",
            )

        self._privateRows.append(x)
        x.isAdded()
        return x

    def newRow(
        self,
        basebandName,
        sideband,
        atmPhaseCorrection,
        typeCurve,
        receiverBand,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numAntenna,
        numPoly,
        numReceptor,
        antennaNames,
        refAntennaName,
        freqLimits,
        polarizationTypes,
        curve,
        reducedChiSquared,
    ):
        """
        Create a new CalBandpassRow initialized to the specified values.

        The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = CalBandpassRow(self)

        thisRow.setBasebandName(basebandName)

        thisRow.setSideband(sideband)

        thisRow.setAtmPhaseCorrection(atmPhaseCorrection)

        thisRow.setTypeCurve(typeCurve)

        thisRow.setReceiverBand(receiverBand)

        thisRow.setCalDataId(calDataId)

        thisRow.setCalReductionId(calReductionId)

        thisRow.setStartValidTime(startValidTime)

        thisRow.setEndValidTime(endValidTime)

        thisRow.setNumAntenna(numAntenna)

        thisRow.setNumPoly(numPoly)

        thisRow.setNumReceptor(numReceptor)

        thisRow.setAntennaNames(antennaNames)

        thisRow.setRefAntennaName(refAntennaName)

        thisRow.setFreqLimits(freqLimits)

        thisRow.setPolarizationTypes(polarizationTypes)

        thisRow.setCurve(curve)

        thisRow.setReducedChiSquared(reducedChiSquared)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new CalBandpassRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new CalBandpassRow with default values for its attributes.
        """

        return CalBandpassRow(self, row)

    # ====> Append a row to its table.

    def checkAndAdd(self, x):
        """
        A method to append a row to it's table, used by input conversion methods.
        Not indended for external use.

        If this table has an autoincrementable attribute then check if
        x verifies the rule of uniqueness and raise an exception if not.

        Append x to its table.
        x is the row to be appended.
        returns x.
        """

        if (
            self.getRowByKey(
                x.getBasebandName(),
                x.getSideband(),
                x.getAtmPhaseCorrection(),
                x.getTypeCurve(),
                x.getReceiverBand(),
                x.getCalDataId(),
                x.getCalReductionId(),
            )
            is not None
        ):
            raise DuplicateKey("Duplicate key exception in ", "CalBandpassTable")

        self._privateRows.append(x)
        x.isAdded()
        return x

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows.
        return Alls rows as a list of CalBandpassRow
        """
        return self._privateRows

    def getRowByKey(
        self,
        basebandName,
        sideband,
        atmPhaseCorrection,
        typeCurve,
        receiverBand,
        calDataId,
        calReductionId,
    ):
        """
        Returns a CalBandpassRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        param basebandName.

        param sideband.

        param atmPhaseCorrection.

        param typeCurve.

        param receiverBand.

        param calDataId.

        param calReductionId.

        """
        for row in self._privateRows:

            if row.getBasebandName() != basebandName:
                continue

            if row.getSideband() != sideband:
                continue

            if row.getAtmPhaseCorrection() != atmPhaseCorrection:
                continue

            if row.getTypeCurve() != typeCurve:
                continue

            if row.getReceiverBand() != receiverBand:
                continue

            if not row.getCalDataId().equals(calDataId):
                continue

            if not row.getCalReductionId().equals(calReductionId):
                continue

            return row

        # no match found
        return None

    def lookup(
        self,
        basebandName,
        sideband,
        atmPhaseCorrection,
        typeCurve,
        receiverBand,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numAntenna,
        numPoly,
        numReceptor,
        antennaNames,
        refAntennaName,
        freqLimits,
        polarizationTypes,
        curve,
        reducedChiSquared,
    ):
        """
        Look up the table for a row whose all attributes
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param basebandName.

        param sideband.

        param atmPhaseCorrection.

        param typeCurve.

        param receiverBand.

        param calDataId.

        param calReductionId.

        param startValidTime.

        param endValidTime.

        param numAntenna.

        param numPoly.

        param numReceptor.

        param antennaNames.

        param refAntennaName.

        param freqLimits.

        param polarizationTypes.

        param curve.

        param reducedChiSquared.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                basebandName,
                sideband,
                atmPhaseCorrection,
                typeCurve,
                receiverBand,
                calDataId,
                calReductionId,
                startValidTime,
                endValidTime,
                numAntenna,
                numPoly,
                numReceptor,
                antennaNames,
                refAntennaName,
                freqLimits,
                polarizationTypes,
                curve,
                reducedChiSquared,
            ):
                return row

        return None

    def getRows(self):
        """
        get the rows, synonymous with the get method.
        """
        return self.get()

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for CalBandpass (CalBandpassTable.xsd).

        returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<CalBandpassTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clbndp="http://Alma/XASDM/CalBandpassTable" xsi:schemaLocation="http://Alma/XASDM/CalBandpassTable http://almaobservatory.org/XML/XASDM/4/CalBandpassTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</CalBandpassTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a CalBandpass (CalBandpassTable.xsd).
        """
        if not isinstance(xmlstr, str):
            raise ConversionException("xmlstr must be a string")

        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of "CalBandpassTable".
        if (
            not xmldom.hasChildNodes()
            or xmldom.firstChild.nodeName != "CalBandpassTable"
        ):
            raise ConversionException(
                "XML is not from the expected table", "CalBandpassTable"
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which is not always there
        versionStr = "-1"
        if tabdom.hasAttributes() and (
            tabdom.attributes.getNamedItem("schemaVersion") is not None
        ):
            versionStr = tabdom.attributes.getNamedItem("schemaVersion").value
        # raises a ValueError if not an integer
        try:
            self.setVersion(int(versionStr))
        except Exception as ex:
            # reraise it as a ConversionException
            raise ConversionException(
                "schemaVersion is not an integer", "CalBandpassTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "CalBandpassTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "CalBandpassTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "CalBandpassTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "CalBandpassTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "CalBandpassTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self.checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str(exc), "CalBandpassTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalBandpassTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalBandpassTable")

        self.setEntity(tabEntity)

    def MIMEXMLPart(self, byteOrder):
        """
        Used in both the small XML file as well as the bin file when writing out as binary.
        The byte order is set by byteOrder.
        """
        uidStr = str(self.getEntity().getEntityId())
        withoutUID = uidStr[6:]
        containerUID = str(self.getContainer().getEntity().getEntityId())

        result = ""
        result += "<?xml version='1.0'  encoding='ISO-8859-1'?>"
        result += "\n"
        result += '<CalBandpassTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clbndp="http://Alma/XASDM/CalBandpassTable" xsi:schemaLocation="http://Alma/XASDM/CalBandpassTable http://almaobservatory.org/XML/XASDM/4/CalBandpassTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += "<Entity entityId='"
        result += uidStr
        result += "' entityIdEncrypted='na' entityTypeName='CalBandpassTable' schemaVersion='1' documentVersion='1'/>\n"
        result += "<ContainerEntity entityId='"
        result += containerUID
        result += "' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n"
        result += "<BulkStoreRef file_id='"
        result += withoutUID
        result += "' byteOrder='" + str(byteOrder) + "' />\n"
        result += "<Attributes>\n"

        result += "<basebandName/>\n"
        result += "<sideband/>\n"
        result += "<atmPhaseCorrection/>\n"
        result += "<typeCurve/>\n"
        result += "<receiverBand/>\n"
        result += "<calDataId/>\n"
        result += "<calReductionId/>\n"
        result += "<startValidTime/>\n"
        result += "<endValidTime/>\n"
        result += "<numAntenna/>\n"
        result += "<numPoly/>\n"
        result += "<numReceptor/>\n"
        result += "<antennaNames/>\n"
        result += "<refAntennaName/>\n"
        result += "<freqLimits/>\n"
        result += "<polarizationTypes/>\n"
        result += "<curve/>\n"
        result += "<reducedChiSquared/>\n"

        result += "<numBaseline/>\n"
        result += "<numFreq/>\n"
        result += "<rms/>\n"
        result += "<frequencyRange/>\n"
        result += "<numSpectralWindow/>\n"
        result += "<chanFreqStart/>\n"
        result += "<chanFreqStep/>\n"
        result += "<numSpectralWindowChan/>\n"
        result += "<spectrum/>\n"
        result += "</Attributes>\n"
        result += "</CalBandpassTable>\n"

        return result

    def toMIME(self, mimeFilePath, mimeXMLpart, byteOrder):
        """
        Write this out to mimeFilePath as a serialized MIME file with
        a leading XML part and a following binary part.

        The mimeXMLpart is a string that should have already been written
        to the corresponding small XML file (and is returned by the
        MIMEXMLPart method here). The byteOrder is a ByteOrder instance
        that gives the byte order to use when writing the binary data.
        That instance should have also been used to generate mimeXMLpart.
        """

        # mimeFilePath should have already been removed if it already existed.

        with open(mimeFilePath, "wb") as outBuffer:

            uidStr = str(self.getEntity().getEntityId())

            # The XML Header part.
            outBuffer.write(bytes("MIME-Version: 1.0", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(
                bytes(
                    "Content-Type: Multipart/Related; boundary='MIME_boundary'; type='text/xml'; start= '<header.xml>'",
                    "utf-8",
                )
            )
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-Description: Correlator", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("alma-uid:" + uidStr, "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))

            # The MIME XML part header.
            outBuffer.write(bytes("--MIME_boundary", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(
                bytes("Content-Type: text/xml; charset='ISO-8859-1'", "utf-8")
            )
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-Transfer-Encoding: 8bit", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-ID: <header.xml>", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))

            # The MIME XML part content.
            outBuffer.write(bytes(mimeXMLpart, "utf-8"))

            # The MIME binary part header
            outBuffer.write(bytes("--MIME_boundary", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-Type: binary/octet-stream", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("Content-ID: <content.bin>", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))

            # The binary part, needs an EndianOutput instance

            eos = EndianOutput(outBuffer, byteOrder)
            self.getEntity().toBin(eos)
            self.getContainer().getEntity().toBin(eos)
            eos.writeInt(len(self._privateRows))

            # and all of the rows
            for thisRow in self._privateRows:
                thisRow.toBin(eos)

            # The closing MIME boundary
            outBuffer.write(bytes("\n--MIME_boundary--", "utf-8"))
            outBuffer.write(bytes("\n", "utf-8"))

            # close the eos, also closes outBuffer, no penalty for doing that more than once
            eos.close()

    def setFromMIME(self, byteStream):
        """
        Extracts the binary part of a MIME message and deserialize its content
        to fill this with the result of the deserialization.
        param byteStream the previously opened io.BufferedReader instance
        containing the data to be extracted.

        It is the responsibility of this method to close byteStream.
        """

        if not (isinstance(byteStream, io.BufferedReader) and byteStream.seekable()):
            byteStream.close()
            raise ConversionException(
                "opened byteStream is not the expected io.BufferedReader or it is not seekable, this should never happen.",
                "CalBandpass",
            )

        xmlPartMIMEHeader = bytes(str("Content-ID: <header.xml>\n\n").encode())
        binPartMIMEHeader = bytes(
            str(
                "--MIME_boundary\nContent-Type: binary/octet-stream\nContent-ID: <content.bin>\n\n"
            ).encode()
        )

        # follow the Java example and grab the first 10000 bytes, which will always contain the header
        headerBytes = byteStream.read(10000)

        # Detect the XML header.
        loc0 = headerBytes.find(xmlPartMIMEHeader)
        # c++ code also looks for a string with an additional CRLF after each newline if the above fails, but Java
        # doesn't and even c++ doesn't follow that up when failing to find the binPartMIMEHeader, so go with the Java example
        if loc0 < 0:
            byteStream.close()
            raise ConversionException(
                "Failed to detect the begining of the XML header.", "CalBandpass"
            )

        loc0 += len(xmlPartMIMEHeader)

        # Look for the string announcing the binary part.
        loc1 = headerBytes.find(binPartMIMEHeader, loc0)
        if loc1 < 0:
            byteStream.close()
            raise ConversionException(
                "Failed to detect the begining of the binary part.", "CalBandpass"
            )

        # extract the XML header as a string
        xmlHeader = headerBytes[loc0:loc1].decode()

        xmldom = minidom.parseString(xmlHeader)
        if not xmldom.hasChildNodes():
            byteStream.close()
            raise ConversionException("XML is not properly structured.", "CalBandpass")

        attributesSeq = []
        byteOrderStr = None
        versionStr = "-1"

        hdrdom = xmldom.firstChild
        if hdrdom.nodeName == "ASDMBinaryTable":
            # old style of binary data
            # assume Big_Endian and the default order of the elements
            byteOrderStr = "Big_Endian"

            attributesSeq.append("basebandName")

            attributesSeq.append("sideband")

            attributesSeq.append("atmPhaseCorrection")

            attributesSeq.append("typeCurve")

            attributesSeq.append("receiverBand")

            attributesSeq.append("calDataId")

            attributesSeq.append("calReductionId")

            attributesSeq.append("startValidTime")

            attributesSeq.append("endValidTime")

            attributesSeq.append("numAntenna")

            attributesSeq.append("numPoly")

            attributesSeq.append("numReceptor")

            attributesSeq.append("antennaNames")

            attributesSeq.append("refAntennaName")

            attributesSeq.append("freqLimits")

            attributesSeq.append("polarizationTypes")

            attributesSeq.append("curve")

            attributesSeq.append("reducedChiSquared")

            attributesSeq.append("numBaseline")

            attributesSeq.append("numFreq")

            attributesSeq.append("rms")

            attributesSeq.append("frequencyRange")

            attributesSeq.append("numSpectralWindow")

            attributesSeq.append("chanFreqStart")

            attributesSeq.append("chanFreqStep")

            attributesSeq.append("numSpectralWindowChan")

            attributesSeq.append("spectrum")

            versionStr = "2"

        else:
            # c++ and Java just assume it then must be a CalBandpass table
            # this is more insistant, just in case
            if hdrdom.nodeName != "CalBandpassTable":
                byteStream.close()
                raise ConversionException(
                    "XML Header is not from the expected table.", "CalBandpass"
                )

            # schemaVersion becomes versionStr
            if (
                hdrdom.hasAttributes()
                and hdrdom.attributes.getNamedItem("schemaVersion") is not None
            ):
                versionStr = hdrdom.attributes.getNamedItem("schemaVersion").value

            if not hdrdom.hasChildNodes():
                byteStream.close()
                raise ConversionException(
                    "THe XML header is missing all of the expected elements.",
                    "CalBandpass",
                )

            # loop through the child nodes, looking for BulkStoreRef and Attributes
            for hdrnode in hdrdom.childNodes:
                if hdrnode.nodeName == "BulkStoreRef":
                    if byteOrderStr is not None:
                        byteStream.close()
                        raise ConversionException(
                            "More than one BulkStoreRef element seen. Invalid XML header.",
                            "CalBandpass",
                        )
                    if not hdrnode.hasAttributes():
                        byteStream.close()
                        raise ConversionException(
                            "BulkStoreRef does not contain any attributes. Invalid XML header.",
                            "CalBandpass",
                        )
                    byteOrderAttr = hdrnode.attributes.getNamedItem("byteOrder")
                    if byteOrderAttr is None:
                        byteStream.close()
                        raise ConversionException(
                            "byteOrder attribute not found in BulkStoreRef element. Invalid XML header.",
                            "CalBandpass",
                        )
                    byteOrderStr = byteOrderAttr.value
                elif hdrnode.nodeName == "Attributes":
                    if len(attributesSeq) > 0:
                        byteStream.close()
                        raise ConversionException(
                            "More than one Attributes node seen. Invalid XML header.",
                            "CalBandpass",
                        )
                    if not hdrnode.hasChildNodes():
                        byteStream.close()
                        raise ConversionException(
                            "Attributes element has no child nodes. Invalid XML header.",
                            "CalBandpass",
                        )
                    for attrnode in hdrnode.childNodes:
                        if attrnode.nodeType == attrnode.ELEMENT_NODE:
                            attributesSeq.append(str(attrnode.nodeName))

        if byteOrderStr is None:
            byteStream.close()
            raise ConversionException(
                "BulkStoreRef element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "CalBandpass",
            )

        if len(attributesSeq) == 0:
            byteStream.close()
            raise ConversionException(
                "Attributes element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "CalBandpass",
            )

        byteOrder = ByteOrder(byteOrderStr)

        # seek to the start of the binary part
        byteStream.seek(loc1 + len(binPartMIMEHeader))

        # and create the class that manages that stream and returns values as requested
        eis = EndianInput(byteStream, byteOrder)

        self._entity = Entity.fromBin(eis)

        # containerEntity is not used, but it is next
        containerEntity = Entity.fromBin(eis)

        # the number of rows
        numRows = eis.readInt()

        # c++ checks numRows against what is reported in the ASDM for this table, this is what Java does
        try:
            for i in range(numRows):
                self.checkAndAdd(CalBandpassRow.fromBin(eis, self, attributesSeq))
                # print("row %s added, loc = %s" % (i, eis.tell()))
        except Exception as exc:
            byteStream.close()
            eis.close()
            raise ConversionException(
                "Error while reading binary data, the exception was " + str(exc),
                "CalBandpass",
            ) from None

        # there is no harm in closing both
        # print("closing")
        eis.close()
        byteStream.close()
        # print("checking")
        # print("eis : %s" % eis.closed())
        # print("byteStream : %s" % byteStream.closed)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalBandpassTable as those produced  by the toFile method.
        This table is populated with the result of the parsing.
        param directory The name of the directory containing the file te be read and parsed.
        raises ConversionException If any error occurs while reading the
        files in the directory or parsing them.
        """
        if not isinstance(directory, str):
            print("directory must be a string")

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "CalBandpassTable",
            )

        if os.path.exists(os.path.join(directory, "CalBandpass.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalBandpass.bin")):
            self.setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalBandpass table", "CalBandpassTable"
            )

    def setFromMIMEFile(self, directory):
        """
        Set this table from a MIME file.
        Used internally by setFromFile. Not intended for external use.
        """
        # The java and c++ versions read all of the contents into a byte array.
        # This uses a buffered byte stream. Created here and then
        # handed off to the setFromMIME method, which is responsible for closing it.

        filename = os.path.join(directory, "CalBandpass.bin")
        byteStream = None
        try:
            byteStream = open(filename, "rb")
        except Exception as exc:
            raise ConversionException(
                "Error while opening " + filename + ". The exception was " + str(exc),
                "CalBandpass",
            )

        self.setFromMIME(byteStream)

    def setFromXMLFile(self, directory):
        """
        This is the function used by setFromFile when the file is an XML file
        Not intended for external use.
        """

        # setFromFile has already established that this exists
        # read the entire file into a string
        xmlstr = None
        try:
            with open(os.path.join(directory, "CalBandpass.xml")) as f:
                xmlstr = f.read()
        except Exception as exc:
            # reraise it as a ConversionException
            raise ConversionException(str(exc), "CalBandpassTable") from None

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of its _fileAsBin data member a binary serialization
        of this (_fileAsBin==True) will be saved in a file "CalBandpass.bin" or
        an XML representation (_fileAsBin==False) will be saved in a file "CalBandpass.xml".
        The file is always written in a directory whose name is passed as a parameter.
        param directory The name of directory where the file containing the table's
        representation will be saved.
        raises ConversionException for any errors while writing that file.
        """
        if not isinstance(directory, str):
            raise ConversionException("directory must be a string")

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalBandpass)"
                % directory,
                "CalBandpassTable",
            )

        # if not let's create it.
        try:
            if not os.path.exists(directory):
                # if it can't be created a FileNotFound exception is the most likely result
                os.mkdir(directory)
        except Exception as exc:
            # reraise any exception as a ConversionException
            raise ConversionException(
                "Could not create directory "
                + directory
                + " exception caught "
                + str(exc),
                "CalBandpassTable",
            ) from None

        if self._fileAsBin:
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)

            # Java defaults to Big_Endian
            # c++ defaults to Machine, go with c++
            byteOrder = ByteOrder()

            # first, just the short XML file
            xmlFilePath = os.path.join(directory, "CalBandpass.xml")
            if os.path.exists(xmlFilePath):
                try:
                    os.remove(xmlFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + xmlFilePath
                        + ", exception caught "
                        + str(exc),
                        "CalBandpass",
                    ) from None

            # used in both files
            mimeXMLpart = self.MIMEXMLPart(byteOrder)

            # this is all that is written to the XML file
            with open(xmlFilePath, "w") as xmlfile:
                xmlfile.write(mimeXMLpart)

            # now open the possibly much longer MIME file
            mimeFilePath = os.path.join(directory, "CalBandpass.bin")
            if os.path.exists(mimeFilePath):
                try:
                    os.remove(mimeFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + mimeFilePath
                        + ", exception caught "
                        + str(exc),
                        "CalBandpass",
                    ) from None

            # the details are all handled in toMIME
            self.toMIME(mimeFilePath, mimeXMLpart, byteOrder)
        else:
            # The table is totally exported in a XML file.
            filePath = os.path.join(directory, "CalBandpass.xml")
            if os.path.exists(filePath):
                try:
                    # try to delete it, this will raise an exception if the user does not have permission to do that
                    os.remove(filePath)
                except Exception as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(
                        "Could not remove existing "
                        + filePath
                        + " exception caught "
                        + str(exc),
                        "CalBandpassTable",
                    ) from None

            try:
                with open(filePath, "w") as f:
                    f.write(self.toXML())
                    f.close()

                    # Java code uses a BufferedWriter to capture the output of toXML to the file
            except Exception as exc:
                # reraise it as a ConversionException
                raise ConversionException(
                    "Problem while writing the XML representation, the message was : "
                    + str(exc),
                    "CalBandpass",
                ) from None

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
