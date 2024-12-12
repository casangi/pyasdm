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
# File CalFluxTable.py
#

import pyasdm.ASDM

from .CalFluxRow import CalFluxRow

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey
from .exceptions.UniquenessViolationException import UniquenessViolationException

from xml.dom import minidom

import os


class CalFluxTable:
    """
    The CalFluxTable class is an Alma table.

    Role
    Result of flux calibration performed on-line by TelCal. Atmospheric absorption is corrected for. No ionosphere correction has been applied.

    Generated from model's revision -1, branch

    Attributes of CalFlux

                 Key


    sourceName str the name of the source. </TD>



    calDataId Tag refers to a unique row in CalData Table. </TD>



    calReductionId Tag refers to a unique row in CalReduction Table. </TD>




                 Value (Mandatory)

    startValidTime  ArrayTime  the start time of result validity period.

    endValidTime  ArrayTime  the end time of result validity period.

    numFrequencyRanges (numFrequencyRanges) int  the number of frequency ranges.

    numStokes (numStokes) int  the number of Stokes parameters.

    frequencyRanges  Frequency []  []   numFrequencyRanges, 2  the frequency ranges (one pair of values per range).

    fluxMethod  FluxCalibrationMethod  identifies the flux determination method.

    flux  float []  []   numStokes, numFrequencyRanges  the flux densities (one value par Stokes parameter per frequency range) expressed in Jansky (Jy).

    fluxError  float []  []   numStokes, numFrequencyRanges  the uncertainties on the flux densities (one value per Stokes parameter per frequency range).

    stokes  StokesParameter []   numStokes  the Stokes parameter.



                 Value (Optional)

    direction  Angle []   2  the direction of the source.

    directionCode  DirectionReferenceCode  identifies the reference frame of the source's direction.

    directionEquinox  Angle  equinox associated with the reference frame of the source's direction.

    PA  Angle []  []   numStokes, numFrequencyRanges  the position's angles for the source model (one value per Stokes parameter per frequency range).

    PAError  Angle []  []   numStokes, numFrequencyRanges  the uncertainties on the position's angles (one value per Stokes parameter per frequency range).

    size  Angle []  []  []   numStokes, numFrequencyRanges, 2  the sizes of the source (one pair of angles per Stokes parameter per frequency range).

    sizeError  Angle []  []  []   numStokes, numFrequencyRanges, 2  the uncertainties of the sizes of the source (one pair of angles per Stokes parameter per frequency range).

    sourceModel  SourceModel  identifies the source model.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # The name of this table.
    _tableName = "CalFlux"

    # The list of field names that make up key 'key'.
    _key = ["sourceName", "calDataId", "calReductionId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # archive as bin not used by python implementation
    # _archiveAsBin = True # If True archive binary else archive XML
    _fileAsBin = True  # If True file binary else file XML

    # A data structure to store the CalFluxRow s.
    # In all cases we maintain a private list of CalFluxRow s.
    _privateRows = []

    # non-temporal ASDM in Java had a private row element here to also hold  CalFluxRow s. Not needed in python.

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on frequencyRanges during an add operation on the table
    _frequencyRangesEqTolerance = Frequency(0.0)

    def setFrequencyRangesEqTolerance(self, tolerance):
        """
        A setter for the tolerance on frequencyRanges
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._frequencyRangesEqTolerance = Frequency(tolerance)

    def getFrequencyRangesEqTolerance(self):
        """
        A getter for the tolerance on frequencyRanges
        Returns the tolerance as a  Frequency
        """
        return self._frequencyRangesEqTolerance

    # The tolerance which will be used on direction during an add operation on the table
    _directionEqTolerance = Angle(0.0)

    def setDirectionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on direction
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._directionEqTolerance = Angle(tolerance)

    def getDirectionEqTolerance(self):
        """
        A getter for the tolerance on direction
        Returns the tolerance as a  Angle
        """
        return self._directionEqTolerance

    # The tolerance which will be used on directionEquinox during an add operation on the table
    _directionEquinoxEqTolerance = Angle(0.0)

    def setDirectionEquinoxEqTolerance(self, tolerance):
        """
        A setter for the tolerance on directionEquinox
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._directionEquinoxEqTolerance = Angle(tolerance)

    def getDirectionEquinoxEqTolerance(self):
        """
        A getter for the tolerance on directionEquinox
        Returns the tolerance as a  Angle
        """
        return self._directionEquinoxEqTolerance

    # The tolerance which will be used on PA during an add operation on the table
    _PAEqTolerance = Angle(0.0)

    def setPAEqTolerance(self, tolerance):
        """
        A setter for the tolerance on PA
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._PAEqTolerance = Angle(tolerance)

    def getPAEqTolerance(self):
        """
        A getter for the tolerance on PA
        Returns the tolerance as a  Angle
        """
        return self._PAEqTolerance

    # The tolerance which will be used on PAError during an add operation on the table
    _PAErrorEqTolerance = Angle(0.0)

    def setPAErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on PAError
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._PAErrorEqTolerance = Angle(tolerance)

    def getPAErrorEqTolerance(self):
        """
        A getter for the tolerance on PAError
        Returns the tolerance as a  Angle
        """
        return self._PAErrorEqTolerance

    # The tolerance which will be used on size during an add operation on the table
    _sizeEqTolerance = Angle(0.0)

    def setSizeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on size
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._sizeEqTolerance = Angle(tolerance)

    def getSizeEqTolerance(self):
        """
        A getter for the tolerance on size
        Returns the tolerance as a  Angle
        """
        return self._sizeEqTolerance

    # The tolerance which will be used on sizeError during an add operation on the table
    _sizeErrorEqTolerance = Angle(0.0)

    def setSizeErrorEqTolerance(self, tolerance):
        """
        A setter for the tolerance on sizeError
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._sizeErrorEqTolerance = Angle(tolerance)

    def getSizeErrorEqTolerance(self):
        """
        A getter for the tolerance on sizeError
        Returns the tolerance as a  Angle
        """
        return self._sizeErrorEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up key key
        as a list of strings.
        """
        return self._key

    def Key(self, sourceName, calDataId, calReductionId):
        """
        Returns a string built by concatenating the ascii representation of the
        parameters values suffixed with a "_" character.
        """
        result = ""

        result += calDataId.toString() + "_"

        result += calReductionId.toString() + "_"

        return result

    def __init__(self, container):
        """
        Create a CalFluxTable attached to container.

        container must be a ASDM instance
        All tables must know the container
        """

        if not isinstance(container, pyasdm.ASDM):
            raise (ValueError("CalFluxTable constructor must use a ASDM instance"))

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("CalFluxTable")
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
            print("CalFlux is not present in memory, setting from file")
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

    def toString(self):
        """
        Returns "CalFluxTable" followed by the current size of the table
        between parenthesis.
        Example : CalFluxTable(12)
        """
        return "CalFluxTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = CalFluxRow(self)
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
        if not isinstance(x, CalFluxRow):
            raise ValueError("x must be a  CalFluxRow instance.")

        if (
            self.getRowByKey(x.getSourceName(), x.getCalDataId(), x.getCalReductionId())
            is not None
        ):
            raise DuplicateKey(
                "["
                + x.getSourceName()
                + "|"
                + x.getCalDataId()
                + "|"
                + x.getCalReductionId()
                + "]",
                "CalFlux",
            )

        self._privateRows.append(x)
        x.isAdded()
        return x

    def newRow(
        self,
        sourceName,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numFrequencyRanges,
        numStokes,
        frequencyRanges,
        fluxMethod,
        flux,
        fluxError,
        stokes,
    ):
        """
        Create a new CalFluxRow initialized to the specified values.

        The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = CalFluxRow(self)

        thisRow.setSourceName(sourceName)

        thisRow.setCalDataId(calDataId)

        thisRow.setCalReductionId(calReductionId)

        thisRow.setStartValidTime(startValidTime)

        thisRow.setEndValidTime(endValidTime)

        thisRow.setNumFrequencyRanges(numFrequencyRanges)

        thisRow.setNumStokes(numStokes)

        thisRow.setFrequencyRanges(frequencyRanges)

        thisRow.setFluxMethod(fluxMethod)

        thisRow.setFlux(flux)

        thisRow.setFluxError(fluxError)

        thisRow.setStokes(stokes)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new CalFluxRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new CalFluxRow with default values for its attributes.
        """

        return CalFluxRow(self, row)

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
            self.getRowByKey(x.getSourceName(), x.getCalDataId(), x.getCalReductionId())
            is not None
        ):
            raise DuplicateKey("Duplicate key exception in ", "CalFluxTable")

        self._privateRows.append(x)
        x.isAdded()
        return x

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows.
        return Alls rows as a list of CalFluxRow
        """
        return self._privateRows

    def getRowByKey(self, sourceName, calDataId, calReductionId):
        """
        Returns a CalFluxRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        param sourceName.

        param calDataId.

        param calReductionId.

        """
        for row in self._privateRows:

            if row.getSourceName() != sourceName:
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
        sourceName,
        calDataId,
        calReductionId,
        startValidTime,
        endValidTime,
        numFrequencyRanges,
        numStokes,
        frequencyRanges,
        fluxMethod,
        flux,
        fluxError,
        stokes,
    ):
        """
        Look up the table for a row whose all attributes
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param sourceName.

        param calDataId.

        param calReductionId.

        param startValidTime.

        param endValidTime.

        param numFrequencyRanges.

        param numStokes.

        param frequencyRanges.

        param fluxMethod.

        param flux.

        param fluxError.

        param stokes.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                sourceName,
                calDataId,
                calReductionId,
                startValidTime,
                endValidTime,
                numFrequencyRanges,
                numStokes,
                frequencyRanges,
                fluxMethod,
                flux,
                fluxError,
                stokes,
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
        to the schema defined for CalFlux (CalFluxTable.xsd).

        returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<CalFluxTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:clflx="http://Alma/XASDM/CalFluxTable" xsi:schemaLocation="http://Alma/XASDM/CalFluxTable http://almaobservatory.org/XML/XASDM/4/CalFluxTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</CalFluxTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a CalFlux (CalFluxTable.xsd).
        """
        if not isinstance(xmlstr, str):
            raise ConversionException("xmlstr must be a string")

        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of "CalFluxTable".
        if not xmldom.hasChildNodes() or xmldom.firstChild.nodeName != "CalFluxTable":
            raise ConversionException(
                "XML is not from the expected table", "CalFluxTable"
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
                "schemaVersion is not an integer", "CalFluxTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "CalFluxTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "CalFluxTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "CalFluxTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "CalFluxTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML", "CalFluxTable"
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self.checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str(exc), "CalFluxTable") from None

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "CalFluxTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "CalFluxTable")

        self.setEntity(tabEntity)

    def MIMEXMLPart(self):
        print("MIMEXMLPart not implemented for <CalFluxTable")
        return
        # the JAVA code looks like this
        # String UID = this.getEntity().getEntityId().toString();
        # String withoutUID = UID.substring(6);
        # String containerUID = this.getContainer().getEntity().getEntityId().toString();
        #
        # StringBuffer sb = new StringBuffer()
        # .append("<?xml version='1.0'  encoding='ISO-8859-1'?>")
        # .append("\n")
        # .append("<CalFluxTable xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:clflx=\"http://Alma/XASDM/CalFluxTable\" xsi:schemaLocation=\"http://Alma/XASDM/CalFluxTable http://almaobservatory.org/XML/XASDM/4/CalFluxTable.xsd\" schemaVersion=\"4\" schemaRevision=\"-1\">\n")
        # .append("<Entity entityId='")
        # .append(UID)
        # .append("' entityIdEncrypted='na' entityTypeName='CalFluxTable' schemaVersion='1' documentVersion='1'/>\n")
        # .append("<ContainerEntity entityId='")
        # .append(containerUID)
        # .append("' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n")
        # .append("<BulkStoreRef file_id='")
        # .append(withoutUID)
        # .append("' byteOrder='Big_Endian' />\n")
        # .append("<Attributes>\n")

        # .append("<sourceName/>\n")
        # .append("<calDataId/>\n")
        # .append("<calReductionId/>\n")
        # .append("<startValidTime/>\n")
        # .append("<endValidTime/>\n")
        # .append("<numFrequencyRanges/>\n")
        # .append("<numStokes/>\n")
        # .append("<frequencyRanges/>\n")
        # .append("<fluxMethod/>\n")
        # .append("<flux/>\n")
        # .append("<fluxError/>\n")
        # .append("<stokes/>\n")

        # .append("<direction/>\n")
        # .append("<directionCode/>\n")
        # .append("<directionEquinox/>\n")
        # .append("<PA/>\n")
        # .append("<PAError/>\n")
        # .append("<size/>\n")
        # .append("<sizeError/>\n")
        # .append("<sourceModel/>\n")
        # .append("</Attributes>\n")
        # .append("</CalFluxTable>\n");
        # return sb.toString();

    def toMIME(self):
        """
        Serialize this into a stream of bytes and encapsulates that stream into a MIME message.
        returns a string containing the MIME message.
        """
        print("toMIME not yet implemented for CalFlux")
        return
        # the Java code looks like this - returns a Byte array
        # ByteArrayOutputStream bos = new ByteArrayOutputStream();
        # DataOutputStream dos = new DataOutputStream(bos);

        # String UID = this.getEntity().getEntityId().toString();
        # String execBlockUID = this.getContainer().getEntity().getEntityId().toString();
        # try {
        #     // The XML Header part.
        #     dos.writeBytes("MIME-Version: 1.0");
        #     dos.writeBytes("\n");
        #    dos
        #     .writeBytes("Content-Type: Multipart/Related; boundary='MIME_boundary'; type='text/xml'; start= '<header.xml>'");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-Description: Correlator");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("alma-uid:" + UID);
        #    dos.writeBytes("\n");
        #    dos.writeBytes("\n");
        #
        #    // The MIME XML part header.
        #    dos.writeBytes("--MIME_boundary");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-Type: text/xml; charset='ISO-8859-1'");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-Transfer-Encoding: 8bit");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-ID: <header.xml>");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("\n");
        #
        #    // The MIME XML part content.
        #    dos.writeBytes(MIMEXMLPart());
        #    // have updated their code to the new XML header.
        #    //
        #    //dos.writeBytes(oldMIMEXMLPart());
        #
        #    // The MIME binary part header
        #    dos.writeBytes("--MIME_boundary");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-Type: binary/octet-stream");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("Content-ID: <content.bin>");
        #    dos.writeBytes("\n");
        #    dos.writeBytes("\n");
        #
        #    // The binary part.
        #    entity.toBin(dos);
        #    container.getEntity().toBin(dos);
        #    dos.writeInt(size());

        #    for (CalFluxRow row: privateRows) row.toBin(dos);

        #    // The closing MIME boundary
        #    dos.writeBytes("\n--MIME_boundary--");
        #    dos.writeBytes("\n");

        # } catch (IOException e) {
        #    throw new ConversionException(
        #            "Error while reading binary data , the message was "
        #            + e.getMessage(), "CalFlux");
        # }

        # return bos.toByteArray();

    # Java code looks like this
    # static private boolean binaryPartFound(DataInputStream dis, String s, int pos) throws IOException {
    #    int posl = pos;
    #    int count = 0;
    #    dis.mark(1000000);
    #    try {
    #        while (dis.readByte() != s.charAt(posl)){
    #            count ++;
    #        }
    #    }
    #    catch (EOFException e) {
    #        return false;
    #    }
    #
    #    if (posl == (s.length() - 1)) return true;
    #
    #    if (pos == 0) {
    #        posl++;
    #        return binaryPartFound(dis, s, posl);
    #    }
    #    else {
    #        if (count > 0) { dis.reset();  return binaryPartFound(dis, s, 0) ; }
    #        else {
    #            posl++;
    #            return binaryPartFound(dis, s, posl);
    #        }
    #    }
    # }

    # private String xmlHeaderPart (String s) throws ConversionException {
    #    String xmlPartMIMEHeader = "Content-ID: <header.xml>\n\n";
    #    String binPartMIMEHeader = "--MIME_boundary\nContent-Type: binary/octet-stream\nContent-ID: <content.bin>\n\n";
    #
    #    // Detect the XML header.
    #    int loc0 = s.indexOf(xmlPartMIMEHeader);
    #    if (loc0 == -1 ) throw new ConversionException("Failed to detect the beginning of the XML header", "CalFlux");
    #
    #    loc0 += xmlPartMIMEHeader.length();
    #
    #    // Look for the string announcing the binary part.
    #    int loc1 = s.indexOf(binPartMIMEHeader, loc0);
    #    if (loc1 == -1) throw new ConversionException("Failed to detect the beginning of the binary part", "CalFlux");
    #
    #    return s.substring(loc0, loc1).trim();
    # }

    # setFromMIME(byte[]   data) throws ConversionException {
    # *
    # Extracts the binary part of a MIME message and deserialize its content
    # to fill this with the result of the deserialization.
    # @param data the string containing the MIME message.
    # @throws ConversionException
    # /
    # ByteOrder byteOrder = null;
    # //
    # // Look for the part containing the XML header.
    # // Very empirically we assume that the first MIME part , the one which contains the
    # // XML header, always fits in the first 1000 bytes of the MIME message !!
    # //
    # String header = xmlHeaderPart(new String(data, 0, Math.min(10000, data.length)));
    # org.jdom.Document document = null;
    # SAXBuilder sxb = new SAXBuilder();
    #
    # // Firstly build a document out of the XML.
    # try {
    #    document = sxb.build(new ByteArrayInputStream(header.getBytes()));
    # }
    # catch (Exception e) {
    #     throw new ConversionException(e.getMessage(), "CalFlux");
    # }
    #
    # //
    # // Let's define a default order for the sequence of attributes.
    # //
    # ArrayList<String> attributesSeq = new ArrayList<String> ();

    #     attributesSeq.add("sourceName"); attributesSeq.add("calDataId"); attributesSeq.add("calReductionId"); attributesSeq.add("startValidTime"); attributesSeq.add("endValidTime"); attributesSeq.add("numFrequencyRanges"); attributesSeq.add("numStokes"); attributesSeq.add("frequencyRanges"); attributesSeq.add("fluxMethod"); attributesSeq.add("flux"); attributesSeq.add("fluxError"); attributesSeq.add("stokes");
    #     attributesSeq.add("direction");  attributesSeq.add("directionCode");  attributesSeq.add("directionEquinox");  attributesSeq.add("PA");  attributesSeq.add("PAError");  attributesSeq.add("size");  attributesSeq.add("sizeError");  attributesSeq.add("sourceModel");

    # XPath xpath = null;
    # //
    # // And then look for the possible XML contents.
    # try {
    #     // Is it an "<ASDMBinaryTable ...." document (old) ?
    #    if (XPath.newInstance("/ASDMBinaryTable")
    #            .selectSingleNode(document) != null)
    #        byteOrder = ByteOrder.BIG_ENDIAN;
    #    else {
    #        // Then it must be a "<CalFluxTable ...." document
    #        // With a BulkStoreRef child element....
    #        XPath xpa = XPath.newInstance("/CalFluxTable/BulkStoreRef/@byteOrder");
    #        Object node = xpa.selectSingleNode(document.getRootElement());
    #        if (node == null)
    #            throw new ConversionException("No element found for the XPath expression '/CalFluxTable/BulkStoreRef/@byteOrder'. Invalid XML header '"+header+"'.", "CalFlux");
    #
    #        // Yes ? then it must have a "BulkStoreRef" element with a
    #        // "byteOrder" attribute.
    #        String bo = xpa.valueOf(document.getRootElement());
    #        if (bo.equals("Little_Endian"))
    #            byteOrder = ByteOrder.LITTLE_ENDIAN;
    #        else if (bo.equals("Big_Endian"))
    #            byteOrder = ByteOrder.BIG_ENDIAN;
    #        else
    #            throw new ConversionException("No valid value retrieved for the node '/CalFluxTable/BulkStoreRef/@byteOrder'. Invalid XML header '"+header+"'.", "CalFlux");
    #
    #        // And also it must have an Attributes element with children.
    #        xpa = XPath.newInstance("/CalFluxTable/Attributes#");
    #        List nodes = xpa.selectNodes(document.getRootElement());
    #        if (nodes==null || nodes.size()==0)
    #            throw new ConversionException("No element found for the XPath expression '/CalFluxTable/Attributes#'. Invalid XML header '"+header+"'.", "CalFlux");
    #
    #        Iterator iter = nodes.iterator();
    #        attributesSeq.clear();
    #        int i = 0;
    #        while (iter.hasNext()){
    #            attributesSeq.add(((Element) iter.next()).getName());
    #            i += 1;
    #        }
    #    }
    # } catch (Exception e) {
    #    throw new ConversionException(e.getMessage(), "CalFlux");
    # }

    # //
    # // Now that we know what is the byte order of the binary data
    # // Let's extract them from the second MIME part and parse them
    # //
    # ByteArrayInputStream bis = new ByteArrayInputStream(data);
    # DataInputStream dis = new DataInputStream(bis);
    # BODataInputStream bodis = new BODataInputStream(dis, byteOrder);
    #
    # String terminator = "Content-Type: binary/octet-stream\nContent-ID: <content.bin>\n\n";
    # entity = null;
    # try {
    #    if (binaryPartFound(dis, terminator, 0) == false) {
    #        throw new ConversionException ("Failed to detect the beginning of the binary part", "CalFlux");
    #    }
    #
    #    entity = Entity.fromBin(bodis);
    #
    #    Entity containerEntity = Entity.fromBin(bodis);
    #
    #    int numRows = bodis.readInt();
    #    for (int i = 0; i < numRows; i++) {
    #    this.checkAndAdd(CalFluxRow.fromBin(bodis, this, attributesSeq.toArray(new String[0])));
    #    }
    # } catch (TagFormatException e) {
    #    throw new ConversionException( "Error while reading binary data , the message was "
    #        + e.getMessage(), "CalFlux");
    # }catch (IOException e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "CalFlux");
    # } catch (DuplicateKey e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "CalFlux");
    # }catch (Exception e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "CalFlux");
    # }
    # }

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a CalFluxTable as those produced  by the toFile method.
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
                "CalFluxTable",
            )

        if os.path.exists(os.path.join(directory, "CalFlux.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "CalFlux.bin")):
            self.setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the CalFlux table", "CalFluxTable"
            )

    def setFromMIMEFile(self, directory):
        """
        Set this table from a MIME file.
        Used internally by setFromFile. Not intented for external use.
        """
        print("setFromMIME file not yet implemented for CalFluxTable")
        return

        # java code looks like this
        # File file = new File(directory+"/CalFlux.bin");
        #
        # byte[] bytes = null;
        #
        # try {
        #     InputStream is = new FileInputStream(file);
        #     long length = file.length();
        #     if (length > Integer.MAX_VALUE)
        #         throw new ConversionException ("File " + file.getName() + " is too large", "CalFlux");
        #
        #    bytes = new byte[(int)length];
        #    int offset = 0;
        #    int numRead = 0;
        #
        #   while (offset < bytes.length && (numRead=is.read(bytes, offset, bytes.length-offset)) >= 0) {
        #       offset += numRead;
        #   }
        #
        #    if (offset < bytes.length) {
        #        throw new ConversionException("Could not completely read file "+file.getName(), "CalFlux");
        #    }
        #    is.close();
        # }
        # catch (IOException e) {
        #    throw new ConversionException("Error while reading "+file.getName()+". The message was " + e.getMessage(),
        #    "CalFlux");
        # }

        # setFromMIME(bytes);
        # // Changed 24 Sep, 2015 - The export policy cannot be changed by what has been observed at import time. M Caillat
        # // archiveAsBin = true;
        # // fileAsBin = true;

    # }

    def setFromXMLFile(self, directory):
        """
        This is the function used by setFromFile when the file is an XML file
        Not intended for external use.
        """

        # setFromFile has already established that this exists
        # read the entire file into a string
        xmlstr = None
        try:
            with open(os.path.join(directory, "CalFlux.xml")) as f:
                xmlstr = f.read()
        except Exception as exc:
            # reraise it as a ConversionException
            raise ConversionException(str(exc), "CalFluxTable") from None

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)
            # TBD: when fileAsBin is implemented this should be removed
            # this will at least preserve the case where fileAsBin was changed for
            # a table such that the archive has it in XML but the current rule is to
            # write it out as binary
            if self._fileAsBin:
                print(
                    "CalFlux found as XML but it should be written as binary, which is not yet implemetned. Setting to write as XML to preserve this content."
                )
                self._fileAsBin = False

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of its _fileAsBin data member a binary serialization
        of this (_fileAsBin==True) will be saved in a file "CalFlux.bin" or
        an XML representation (_fileAsBin==False) will be saved in a file "CalFlux.xml".
        The file is always written in a directory whose name is passed as a parameter.
        param directory The name of directory where the file containing the table's
        representation will be saved.
        raises ConversionException for any errors while writing that file.
        """
        if not isinstance(directory, str):
            raise ConversionException("directory must be a string")

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (CalFlux)"
                % directory,
                "CalFluxTable",
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
                "CalFluxTable",
            ) from None

        if self._fileAsBin:
            print("fileAsBin not yet implemented for CalFlux")
            # the Java code looks like this
            #
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)
            #
            # File xmlFile = new File(directory+"/CalFlux.xml");
            # if (xmlFile.exists())
            #    if (!xmlFile.delete())
            #        throw new ConversionException("Problem while trying to delete a previous version of '"+xmlFile.toString()+"'", "CalFlux");
            #
            # File binFile = new File(directory+"/CalFlux.bin");
            # if (binFile.exists())
            #    if (!binFile.delete())
            #        throw new ConversionException("Problem while trying to delete a previous version of '"+binFile.toString()+"'", "CalFlux");
            #
            # try {
            #    BufferedWriter out = new BufferedWriter(new FileWriter(xmlFile));
            #    out.write(MIMEXMLPart());
            #    out.close();
            #

            #  OutputStream osBin = new FileOutputStream(binFile);
            #  osBin.write(toMIME());
            #  osBin.close();

        # }
        # catch (FileNotFoundException e) {
        #     throw new ConversionException("Problem while writing the binary representation, the message was : " + e.getMessage(), "CalFlux");
        # }
        # catch (IOException e) {
        #      throw new ConversionException("Problem while writing the binary representation, the message was : " + e.getMessage(), "CalFlux");
        # }
        # }
        else:
            # The table is totally exported in a XML file.
            filePath = os.path.join(directory, "CalFlux.xml")
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
                        "CalFluxTable",
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
                    "CalFlux",
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
