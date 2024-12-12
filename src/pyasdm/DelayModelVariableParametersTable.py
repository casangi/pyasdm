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
# File DelayModelVariableParametersTable.py
#

import pyasdm.ASDM

from .DelayModelVariableParametersRow import DelayModelVariableParametersRow

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey
from .exceptions.UniquenessViolationException import UniquenessViolationException

from xml.dom import minidom

import os


class DelayModelVariableParametersTable:
    """
    The DelayModelVariableParametersTable class is an Alma table.

    Role


    Generated from model's revision -1, branch

    Attributes of DelayModelVariableParameters

                 Key


    delayModelVariableParametersId Tag (auto-incrementable)     identifies a unique row in the table. </TD>




                 Value (Mandatory)

    time  ArrayTime  the day and time relevant for the data in this row.

    ut1_utc  float  \f$ UT1 - UTC \f$ in \f$ second \f$.

    iat_utc  float  \f$ IAT - UTC \f$ in \f$ second \f$.

    timeType  DifferenceType  the type of the two time differences expressed in ut1_utc and iat_utc

    gstAtUt0  Angle  in \f$ radian \f$.

    earthRotationRate  AngularRate  in \f$ radian \ s^{-1} \f$ (the seconds are in \f$ IAT \f$).

    polarOffsets  float []   2  the \f$ X, Y \f$ polar offsets in \f$ arcsec \f$.

    polarOffsetsType  DifferenceType  the type of the polar offsets (values found in polarOffsets).

    delayModelFixedParametersId  Tag  refers to a unique row of the DelayModelFixedParameters table.



                 Value (Optional)

    nutationInLongitude  Angle  the nutation in longitude ( the part parallel to the ecliptic) in \f$ radian \f$.

    nutationInLongitudeRate  AngularRate  the rate of nutation in longitude in \f$ radian \ s^{-1} \f$.

    nutationInObliquity  Angle  the nutation in obliquity (the part perpendicular to the ecliptic) in \f$ radian \f$.

    nutationInObliquityRate  AngularRate  the rate of nutation in obliquity in \f$ radian \ s^{-1} \f$.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # The name of this table.
    _tableName = "DelayModelVariableParameters"

    # The list of field names that make up key 'key'.
    _key = ["delayModelVariableParametersId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # archive as bin not used by python implementation
    # _archiveAsBin = False # If True archive binary else archive XML
    _fileAsBin = False  # If True file binary else file XML

    # A data structure to store the DelayModelVariableParametersRow s.
    # In all cases we maintain a private list of DelayModelVariableParametersRow s.
    _privateRows = []

    # non-temporal ASDM in Java had a private row element here to also hold  DelayModelVariableParametersRow s. Not needed in python.

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on gstAtUt0 during an add operation on the table
    _gstAtUt0EqTolerance = Angle(0.0)

    def setGstAtUt0EqTolerance(self, tolerance):
        """
        A setter for the tolerance on gstAtUt0
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._gstAtUt0EqTolerance = Angle(tolerance)

    def getGstAtUt0EqTolerance(self):
        """
        A getter for the tolerance on gstAtUt0
        Returns the tolerance as a  Angle
        """
        return self._gstAtUt0EqTolerance

    # The tolerance which will be used on earthRotationRate during an add operation on the table
    _earthRotationRateEqTolerance = AngularRate(0.0)

    def setEarthRotationRateEqTolerance(self, tolerance):
        """
        A setter for the tolerance on earthRotationRate
        """
        if not isinstance(tolerance, AngularRate):
            print("tolerance must be a  AngularRate instance")

        self._earthRotationRateEqTolerance = AngularRate(tolerance)

    def getEarthRotationRateEqTolerance(self):
        """
        A getter for the tolerance on earthRotationRate
        Returns the tolerance as a  AngularRate
        """
        return self._earthRotationRateEqTolerance

    # The tolerance which will be used on nutationInLongitude during an add operation on the table
    _nutationInLongitudeEqTolerance = Angle(0.0)

    def setNutationInLongitudeEqTolerance(self, tolerance):
        """
        A setter for the tolerance on nutationInLongitude
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._nutationInLongitudeEqTolerance = Angle(tolerance)

    def getNutationInLongitudeEqTolerance(self):
        """
        A getter for the tolerance on nutationInLongitude
        Returns the tolerance as a  Angle
        """
        return self._nutationInLongitudeEqTolerance

    # The tolerance which will be used on nutationInLongitudeRate during an add operation on the table
    _nutationInLongitudeRateEqTolerance = AngularRate(0.0)

    def setNutationInLongitudeRateEqTolerance(self, tolerance):
        """
        A setter for the tolerance on nutationInLongitudeRate
        """
        if not isinstance(tolerance, AngularRate):
            print("tolerance must be a  AngularRate instance")

        self._nutationInLongitudeRateEqTolerance = AngularRate(tolerance)

    def getNutationInLongitudeRateEqTolerance(self):
        """
        A getter for the tolerance on nutationInLongitudeRate
        Returns the tolerance as a  AngularRate
        """
        return self._nutationInLongitudeRateEqTolerance

    # The tolerance which will be used on nutationInObliquity during an add operation on the table
    _nutationInObliquityEqTolerance = Angle(0.0)

    def setNutationInObliquityEqTolerance(self, tolerance):
        """
        A setter for the tolerance on nutationInObliquity
        """
        if not isinstance(tolerance, Angle):
            print("tolerance must be a  Angle instance")

        self._nutationInObliquityEqTolerance = Angle(tolerance)

    def getNutationInObliquityEqTolerance(self):
        """
        A getter for the tolerance on nutationInObliquity
        Returns the tolerance as a  Angle
        """
        return self._nutationInObliquityEqTolerance

    # The tolerance which will be used on nutationInObliquityRate during an add operation on the table
    _nutationInObliquityRateEqTolerance = AngularRate(0.0)

    def setNutationInObliquityRateEqTolerance(self, tolerance):
        """
        A setter for the tolerance on nutationInObliquityRate
        """
        if not isinstance(tolerance, AngularRate):
            print("tolerance must be a  AngularRate instance")

        self._nutationInObliquityRateEqTolerance = AngularRate(tolerance)

    def getNutationInObliquityRateEqTolerance(self):
        """
        A getter for the tolerance on nutationInObliquityRate
        Returns the tolerance as a  AngularRate
        """
        return self._nutationInObliquityRateEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up key key
        as a list of strings.
        """
        return self._key

    # a dictionary for the autoincrementation algorithm
    # the key is the key, excluding that auto-incrementable
    # the value is an integer that's the largest auto-incrementable for that key
    _noAutoIncIds = {}

    def autoIncrement(self, key, x):
        """
        For internal use.
        key is a key string
        x is a row.
        """
        if key not in self._noAutoIncIds:
            # There is not yet a combination of the non autoinc attributes values in the dict

            # Initialize  delayModelVariableParametersId to Tag(0).
            x.setDelayModelVariableParametersId(
                Tag(0, TagType.DelayModelVariableParameters)
            )

            # Record it in the dict.
            self._noAutoIncIds[key] = 0
        else:
            # There is already a combination of the non autoinc attributes values in the dict
            nextInt = int(self._noAutoIncIds[key]) + 1

            # Initialize  delayModelVariableParametersId to Tag(nextInt).
            x.setDelayModelVariableParametersId(
                Tag(nextInt, TagType.DelayModelVariableParameters)
            )

            # Record it in the hashtable.
            self._noAutoIncIds[key] = nextInt

    def __init__(self, container):
        """
        Create a DelayModelVariableParametersTable attached to container.

        container must be a ASDM instance
        All tables must know the container
        """

        if not isinstance(container, pyasdm.ASDM):
            raise (
                ValueError(
                    "DelayModelVariableParametersTable constructor must use a ASDM instance"
                )
            )

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("DelayModelVariableParametersTable")
        self._entity.setEntityVersion("1")
        self._entity.setInstanceVersion("1")

        # the default table has no rows and so is presentInMemory
        self._presentInMemory = True
        self._loadInProgress = False

        self._privateRows = []

        self._noAutoIncIds = {}

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
            print(
                "DelayModelVariableParameters is not present in memory, setting from file"
            )
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
        Returns "DelayModelVariableParametersTable" followed by the current size of the table
        between parenthesis.
        Example : DelayModelVariableParametersTable(12)
        """
        return "DelayModelVariableParametersTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = DelayModelVariableParametersRow(self)
        return thisRow

    def add(self, x):
        """
        Look up the table for a row whose noautoincrementable attributes are matching their
        homologues in x.  If a row is found that row else autoincrement x.\delayModelVariableParametersId,
        add x to its table and returns x.

        returns a DelayModelVariableParametersRow.
        x. A row to be added.
        """
        if not isinstance(x, DelayModelVariableParametersRow):
            raise ValueError("x must be a  DelayModelVariableParametersRow instance.")

        aRow = self.lookup(
            x.getTime(),
            x.getUt1_utc(),
            x.getIat_utc(),
            x.getTimeType(),
            x.getGstAtUt0(),
            x.getEarthRotationRate(),
            x.getPolarOffsets(),
            x.getPolarOffsetsType(),
            x.getDelayModelFixedParametersId(),
        )
        if aRow is not None:
            return aRow

        # Autoincrement delayModelVariableParametersId
        x.setDelayModelVariableParametersId(
            Tag(self.size(), TagType.DelayModelVariableParameters)
        )

        self._privateRows.add(x)
        x.isAdded()
        return x

    def newRow(
        self,
        time,
        ut1_utc,
        iat_utc,
        timeType,
        gstAtUt0,
        earthRotationRate,
        polarOffsets,
        polarOffsetsType,
        delayModelFixedParametersId,
    ):
        """
        Create a new DelayModelVariableParametersRow initialized to the specified values.

        The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = DelayModelVariableParametersRow(self)

        thisRow.setTime(time)

        thisRow.setUt1_utc(ut1_utc)

        thisRow.setIat_utc(iat_utc)

        thisRow.setTimeType(timeType)

        thisRow.setGstAtUt0(gstAtUt0)

        thisRow.setEarthRotationRate(earthRotationRate)

        thisRow.setPolarOffsets(polarOffsets)

        thisRow.setPolarOffsetsType(polarOffsetsType)

        thisRow.setDelayModelFixedParametersId(delayModelFixedParametersId)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new DelayModelVariableParametersRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new DelayModelVariableParametersRow with default values for its attributes.
        """

        return DelayModelVariableParametersRow(self, row)

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
            self.lookup(
                x.getTime(),
                x.getUt1_utc(),
                x.getIat_utc(),
                x.getTimeType(),
                x.getGstAtUt0(),
                x.getEarthRotationRate(),
                x.getPolarOffsets(),
                x.getPolarOffsetsType(),
                x.getDelayModelFixedParametersId(),
            )
            is not None
        ):
            raise UniquenessViolationException(
                "Uniqueness violation exception in table DelayModelVariableParametersTable"
            )

        if self.getRowByKey(x.getDelayModelVariableParametersId()) is not None:
            raise DuplicateKey(
                "Duplicate key exception in ", "DelayModelVariableParametersTable"
            )

        self._privateRows.append(x)
        x.isAdded()
        return x

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows.
        return Alls rows as a list of DelayModelVariableParametersRow
        """
        return self._privateRows

    def getRowByKey(self, delayModelVariableParametersId):
        """
        Returns a DelayModelVariableParametersRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        param delayModelVariableParametersId.

        """
        for row in self._privateRows:

            if not row.getDelayModelVariableParametersId().equals(
                delayModelVariableParametersId
            ):
                continue

            return row

        # no match found
        return None

    def lookup(
        self,
        time,
        ut1_utc,
        iat_utc,
        timeType,
        gstAtUt0,
        earthRotationRate,
        polarOffsets,
        polarOffsetsType,
        delayModelFixedParametersId,
    ):
        """
        Look up the table for a row whose all attributes  except the autoincrementable one
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param time.

        param ut1_utc.

        param iat_utc.

        param timeType.

        param gstAtUt0.

        param earthRotationRate.

        param polarOffsets.

        param polarOffsetsType.

        param delayModelFixedParametersId.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                time,
                ut1_utc,
                iat_utc,
                timeType,
                gstAtUt0,
                earthRotationRate,
                polarOffsets,
                polarOffsetsType,
                delayModelFixedParametersId,
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
        to the schema defined for DelayModelVariableParameters (DelayModelVariableParametersTable.xsd).

        returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<DelayModelVariableParametersTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dmvp="http://Alma/XASDM/DelayModelVariableParametersTable" xsi:schemaLocation="http://Alma/XASDM/DelayModelVariableParametersTable http://almaobservatory.org/XML/XASDM/4/DelayModelVariableParametersTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</DelayModelVariableParametersTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a DelayModelVariableParameters (DelayModelVariableParametersTable.xsd).
        """
        if not isinstance(xmlstr, str):
            raise ConversionException("xmlstr must be a string")

        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of "DelayModelVariableParametersTable".
        if (
            not xmldom.hasChildNodes()
            or xmldom.firstChild.nodeName != "DelayModelVariableParametersTable"
        ):
            raise ConversionException(
                "XML is not from the expected table",
                "DelayModelVariableParametersTable",
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
                "schemaVersion is not an integer", "DelayModelVariableParametersTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements",
                "DelayModelVariableParametersTable",
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML",
                        "DelayModelVariableParametersTable",
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (
                    tabEntity.getEntityTypeName() == "DelayModelVariableParametersTable"
                ):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "DelayModelVariableParametersTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML",
                        "DelayModelVariableParametersTable",
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self.checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(
                        str(exc), "DelayModelVariableParametersTable"
                    ) from None

                except UniquenessViolationException as exc:
                    msg = (
                        "UniquenessViolationException in row in DelayModelVariableParametersTable : %s"
                        % str(exc)
                    )

        if tabEntity is None:
            raise ConversionException(
                "No Entity seen in XML", "DelayModelVariableParametersTable"
            )
        if not hasContainerEntity:
            raise ValueError(
                "No Container Entity seen in XL", "DelayModelVariableParametersTable"
            )

        self.setEntity(tabEntity)

    def MIMEXMLPart(self):
        print("MIMEXMLPart not implemented for <DelayModelVariableParametersTable")
        return
        # the JAVA code looks like this
        # String UID = this.getEntity().getEntityId().toString();
        # String withoutUID = UID.substring(6);
        # String containerUID = this.getContainer().getEntity().getEntityId().toString();
        #
        # StringBuffer sb = new StringBuffer()
        # .append("<?xml version='1.0'  encoding='ISO-8859-1'?>")
        # .append("\n")
        # .append("<DelayModelVariableParametersTable xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:dmvp=\"http://Alma/XASDM/DelayModelVariableParametersTable\" xsi:schemaLocation=\"http://Alma/XASDM/DelayModelVariableParametersTable http://almaobservatory.org/XML/XASDM/4/DelayModelVariableParametersTable.xsd\" schemaVersion=\"4\" schemaRevision=\"-1\">\n")
        # .append("<Entity entityId='")
        # .append(UID)
        # .append("' entityIdEncrypted='na' entityTypeName='DelayModelVariableParametersTable' schemaVersion='1' documentVersion='1'/>\n")
        # .append("<ContainerEntity entityId='")
        # .append(containerUID)
        # .append("' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n")
        # .append("<BulkStoreRef file_id='")
        # .append(withoutUID)
        # .append("' byteOrder='Big_Endian' />\n")
        # .append("<Attributes>\n")

        # .append("<delayModelVariableParametersId/>\n")
        # .append("<time/>\n")
        # .append("<ut1_utc/>\n")
        # .append("<iat_utc/>\n")
        # .append("<timeType/>\n")
        # .append("<gstAtUt0/>\n")
        # .append("<earthRotationRate/>\n")
        # .append("<polarOffsets/>\n")
        # .append("<polarOffsetsType/>\n")
        # .append("<delayModelFixedParametersId/>\n")

        # .append("<nutationInLongitude/>\n")
        # .append("<nutationInLongitudeRate/>\n")
        # .append("<nutationInObliquity/>\n")
        # .append("<nutationInObliquityRate/>\n")
        # .append("</Attributes>\n")
        # .append("</DelayModelVariableParametersTable>\n");
        # return sb.toString();

    def toMIME(self):
        """
        Serialize this into a stream of bytes and encapsulates that stream into a MIME message.
        returns a string containing the MIME message.
        """
        print("toMIME not yet implemented for DelayModelVariableParameters")
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

        #    for (DelayModelVariableParametersRow row: privateRows) row.toBin(dos);

        #    // The closing MIME boundary
        #    dos.writeBytes("\n--MIME_boundary--");
        #    dos.writeBytes("\n");

        # } catch (IOException e) {
        #    throw new ConversionException(
        #            "Error while reading binary data , the message was "
        #            + e.getMessage(), "DelayModelVariableParameters");
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
    #    if (loc0 == -1 ) throw new ConversionException("Failed to detect the beginning of the XML header", "DelayModelVariableParameters");
    #
    #    loc0 += xmlPartMIMEHeader.length();
    #
    #    // Look for the string announcing the binary part.
    #    int loc1 = s.indexOf(binPartMIMEHeader, loc0);
    #    if (loc1 == -1) throw new ConversionException("Failed to detect the beginning of the binary part", "DelayModelVariableParameters");
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
    #     throw new ConversionException(e.getMessage(), "DelayModelVariableParameters");
    # }
    #
    # //
    # // Let's define a default order for the sequence of attributes.
    # //
    # ArrayList<String> attributesSeq = new ArrayList<String> ();

    #     attributesSeq.add("delayModelVariableParametersId"); attributesSeq.add("time"); attributesSeq.add("ut1_utc"); attributesSeq.add("iat_utc"); attributesSeq.add("timeType"); attributesSeq.add("gstAtUt0"); attributesSeq.add("earthRotationRate"); attributesSeq.add("polarOffsets"); attributesSeq.add("polarOffsetsType"); attributesSeq.add("delayModelFixedParametersId");
    #     attributesSeq.add("nutationInLongitude");  attributesSeq.add("nutationInLongitudeRate");  attributesSeq.add("nutationInObliquity");  attributesSeq.add("nutationInObliquityRate");

    # XPath xpath = null;
    # //
    # // And then look for the possible XML contents.
    # try {
    #     // Is it an "<ASDMBinaryTable ...." document (old) ?
    #    if (XPath.newInstance("/ASDMBinaryTable")
    #            .selectSingleNode(document) != null)
    #        byteOrder = ByteOrder.BIG_ENDIAN;
    #    else {
    #        // Then it must be a "<DelayModelVariableParametersTable ...." document
    #        // With a BulkStoreRef child element....
    #        XPath xpa = XPath.newInstance("/DelayModelVariableParametersTable/BulkStoreRef/@byteOrder");
    #        Object node = xpa.selectSingleNode(document.getRootElement());
    #        if (node == null)
    #            throw new ConversionException("No element found for the XPath expression '/DelayModelVariableParametersTable/BulkStoreRef/@byteOrder'. Invalid XML header '"+header+"'.", "DelayModelVariableParameters");
    #
    #        // Yes ? then it must have a "BulkStoreRef" element with a
    #        // "byteOrder" attribute.
    #        String bo = xpa.valueOf(document.getRootElement());
    #        if (bo.equals("Little_Endian"))
    #            byteOrder = ByteOrder.LITTLE_ENDIAN;
    #        else if (bo.equals("Big_Endian"))
    #            byteOrder = ByteOrder.BIG_ENDIAN;
    #        else
    #            throw new ConversionException("No valid value retrieved for the node '/DelayModelVariableParametersTable/BulkStoreRef/@byteOrder'. Invalid XML header '"+header+"'.", "DelayModelVariableParameters");
    #
    #        // And also it must have an Attributes element with children.
    #        xpa = XPath.newInstance("/DelayModelVariableParametersTable/Attributes#");
    #        List nodes = xpa.selectNodes(document.getRootElement());
    #        if (nodes==null || nodes.size()==0)
    #            throw new ConversionException("No element found for the XPath expression '/DelayModelVariableParametersTable/Attributes#'. Invalid XML header '"+header+"'.", "DelayModelVariableParameters");
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
    #    throw new ConversionException(e.getMessage(), "DelayModelVariableParameters");
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
    #        throw new ConversionException ("Failed to detect the beginning of the binary part", "DelayModelVariableParameters");
    #    }
    #
    #    entity = Entity.fromBin(bodis);
    #
    #    Entity containerEntity = Entity.fromBin(bodis);
    #
    #    int numRows = bodis.readInt();
    #    for (int i = 0; i < numRows; i++) {
    #    this.checkAndAdd(DelayModelVariableParametersRow.fromBin(bodis, this, attributesSeq.toArray(new String[0])));
    #    }
    # } catch (TagFormatException e) {
    #    throw new ConversionException( "Error while reading binary data , the message was "
    #        + e.getMessage(), "DelayModelVariableParameters");
    # }catch (IOException e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "DelayModelVariableParameters");
    # } catch (DuplicateKey e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "DelayModelVariableParameters");
    # }catch (Exception e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "DelayModelVariableParameters");
    # }
    # }

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a DelayModelVariableParametersTable as those produced  by the toFile method.
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
                "DelayModelVariableParametersTable",
            )

        if os.path.exists(os.path.join(directory, "DelayModelVariableParameters.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(
            os.path.join(directory, "DelayModelVariableParameters.bin")
        ):
            self.setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the DelayModelVariableParameters table",
                "DelayModelVariableParametersTable",
            )

    def setFromMIMEFile(self, directory):
        """
        Set this table from a MIME file.
        Used internally by setFromFile. Not intented for external use.
        """
        print(
            "setFromMIME file not yet implemented for DelayModelVariableParametersTable"
        )
        return

        # java code looks like this
        # File file = new File(directory+"/DelayModelVariableParameters.bin");
        #
        # byte[] bytes = null;
        #
        # try {
        #     InputStream is = new FileInputStream(file);
        #     long length = file.length();
        #     if (length > Integer.MAX_VALUE)
        #         throw new ConversionException ("File " + file.getName() + " is too large", "DelayModelVariableParameters");
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
        #        throw new ConversionException("Could not completely read file "+file.getName(), "DelayModelVariableParameters");
        #    }
        #    is.close();
        # }
        # catch (IOException e) {
        #    throw new ConversionException("Error while reading "+file.getName()+". The message was " + e.getMessage(),
        #    "DelayModelVariableParameters");
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
            with open(os.path.join(directory, "DelayModelVariableParameters.xml")) as f:
                xmlstr = f.read()
        except Exception as exc:
            # reraise it as a ConversionException
            raise ConversionException(
                str(exc), "DelayModelVariableParametersTable"
            ) from None

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
                    "DelayModelVariableParameters found as XML but it should be written as binary, which is not yet implemetned. Setting to write as XML to preserve this content."
                )
                self._fileAsBin = False

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of its _fileAsBin data member a binary serialization
        of this (_fileAsBin==True) will be saved in a file "DelayModelVariableParameters.bin" or
        an XML representation (_fileAsBin==False) will be saved in a file "DelayModelVariableParameters.xml".
        The file is always written in a directory whose name is passed as a parameter.
        param directory The name of directory where the file containing the table's
        representation will be saved.
        raises ConversionException for any errors while writing that file.
        """
        if not isinstance(directory, str):
            raise ConversionException("directory must be a string")

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (DelayModelVariableParameters)"
                % directory,
                "DelayModelVariableParametersTable",
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
                "DelayModelVariableParametersTable",
            ) from None

        if self._fileAsBin:
            print("fileAsBin not yet implemented for DelayModelVariableParameters")
            # the Java code looks like this
            #
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)
            #
            # File xmlFile = new File(directory+"/DelayModelVariableParameters.xml");
            # if (xmlFile.exists())
            #    if (!xmlFile.delete())
            #        throw new ConversionException("Problem while trying to delete a previous version of '"+xmlFile.toString()+"'", "DelayModelVariableParameters");
            #
            # File binFile = new File(directory+"/DelayModelVariableParameters.bin");
            # if (binFile.exists())
            #    if (!binFile.delete())
            #        throw new ConversionException("Problem while trying to delete a previous version of '"+binFile.toString()+"'", "DelayModelVariableParameters");
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
        #     throw new ConversionException("Problem while writing the binary representation, the message was : " + e.getMessage(), "DelayModelVariableParameters");
        # }
        # catch (IOException e) {
        #      throw new ConversionException("Problem while writing the binary representation, the message was : " + e.getMessage(), "DelayModelVariableParameters");
        # }
        # }
        else:
            # The table is totally exported in a XML file.
            filePath = os.path.join(directory, "DelayModelVariableParameters.xml")
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
                        "DelayModelVariableParametersTable",
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
                    "DelayModelVariableParameters",
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
