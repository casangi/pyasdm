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
# File SpectralWindowTable.py
#

import pyasdm.ASDM

from .SpectralWindowRow import SpectralWindowRow

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey
from .exceptions.UniquenessViolationException import UniquenessViolationException

from xml.dom import minidom

import os


class SpectralWindowTable:
    """
    The SpectralWindowTable class is an Alma table.

    Role
    Spectral window description. The convention in ALMA is to describe the  frequency axis in the topocentric reference frame. If this is not  the case (for instance if active Doppler tracking is implemented) then  \texttt{measFreqRef} should be set accordingly.

    Generated from model's revision -1, branch

    Attributes of SpectralWindow

                 Key


    spectralWindowId Tag (auto-incrementable)     identifies a unique row in the table. </TD>




                 Value (Mandatory)

    basebandName  BasebandName  identifies the baseband.

    netSideband  NetSideband  identifies the net sideband.

    numChan (numChan) int  the number of frequency channels.

    refFreq  Frequency  the reference frequency.

    sidebandProcessingMode  SidebandProcessingMode  identifies the sideband processing mode.

    totBandwidth  Frequency  the total bandwidth.

    windowFunction  WindowFunction  identifies the window function.



                 Value (Optional)

    numBin (numBin) int  the number of channels used in any post-FFT averaging.

    chanFreqStart  Frequency  the frequency of the first channel.

    chanFreqStep  Frequency  the increment between two successive frequencies.

    chanFreqArray  Frequency []   numChan  the frequencies defined as an array (\texttt{numChan} values).

    chanWidth  Frequency  the nominal channel width.

    chanWidthArray  Frequency []   numChan  Array of channel widths.

    correlationBit  CorrelationBit  identifies the number of bits used in the signal representation.

    effectiveBw  Frequency  the effective noise bandwidth.

    effectiveBwArray  Frequency []   numChan  array of effective bandwidths.

    freqGroup  int  the frequency group number.

    freqGroupName  str  the frequency group name.

    lineArray  bool []   numChan  indicates lines (true) versus baselines (false).

    measFreqRef  FrequencyReferenceCode  the reference frame of the frequencies.

    name  str  a name for this spectral window.

    oversampling  bool  data are "oversampled" (true) or not (false).

    quantization  bool  a quantization correction has been applied (true) or not applied (false).

    refChan  float  the reference channel "number".

    resolution  Frequency  the effective spectral resolution of one channel (see note).

    resolutionArray  Frequency []   numChan  the array of frequency resolution.

    numAssocValues (numAssocValues) int  the number of associated values.

    assocNature  SpectralResolutionType []   numAssocValues  the natures of the associations with the rows refered to by assocSpectralWindowId.

    assocSpectralWindowId  Tag []   numAssocValues  refers to a collection of associated rows in the table.

    imageSpectralWindowId  Tag  refers to a unique row in the table (image sideband description).

    dopplerId  int  refers to a collection of rows in DopplerTable.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # The name of this table.
    _tableName = "SpectralWindow"

    # The list of field names that make up key 'key'.
    _key = ["spectralWindowId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # archive as bin not used by python implementation
    # _archiveAsBin = False # If True archive binary else archive XML
    _fileAsBin = False  # If True file binary else file XML

    # A data structure to store the SpectralWindowRow s.
    # In all cases we maintain a private list of SpectralWindowRow s.
    _privateRows = []

    # non-temporal ASDM in Java had a private row element here to also hold  SpectralWindowRow s. Not needed in python.

    # the Entity of this table
    _entity = None

    # from the schemaVersion string found in the table, must be an integer
    _version = 0

    # The tolerance which will be used on refFreq during an add operation on the table
    _refFreqEqTolerance = Frequency(0.0)

    def setRefFreqEqTolerance(self, tolerance):
        """
        A setter for the tolerance on refFreq
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._refFreqEqTolerance = Frequency(tolerance)

    def getRefFreqEqTolerance(self):
        """
        A getter for the tolerance on refFreq
        Returns the tolerance as a  Frequency
        """
        return self._refFreqEqTolerance

    # The tolerance which will be used on totBandwidth during an add operation on the table
    _totBandwidthEqTolerance = Frequency(0.0)

    def setTotBandwidthEqTolerance(self, tolerance):
        """
        A setter for the tolerance on totBandwidth
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._totBandwidthEqTolerance = Frequency(tolerance)

    def getTotBandwidthEqTolerance(self):
        """
        A getter for the tolerance on totBandwidth
        Returns the tolerance as a  Frequency
        """
        return self._totBandwidthEqTolerance

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

    # The tolerance which will be used on chanFreqArray during an add operation on the table
    _chanFreqArrayEqTolerance = Frequency(0.0)

    def setChanFreqArrayEqTolerance(self, tolerance):
        """
        A setter for the tolerance on chanFreqArray
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._chanFreqArrayEqTolerance = Frequency(tolerance)

    def getChanFreqArrayEqTolerance(self):
        """
        A getter for the tolerance on chanFreqArray
        Returns the tolerance as a  Frequency
        """
        return self._chanFreqArrayEqTolerance

    # The tolerance which will be used on chanWidth during an add operation on the table
    _chanWidthEqTolerance = Frequency(0.0)

    def setChanWidthEqTolerance(self, tolerance):
        """
        A setter for the tolerance on chanWidth
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._chanWidthEqTolerance = Frequency(tolerance)

    def getChanWidthEqTolerance(self):
        """
        A getter for the tolerance on chanWidth
        Returns the tolerance as a  Frequency
        """
        return self._chanWidthEqTolerance

    # The tolerance which will be used on chanWidthArray during an add operation on the table
    _chanWidthArrayEqTolerance = Frequency(0.0)

    def setChanWidthArrayEqTolerance(self, tolerance):
        """
        A setter for the tolerance on chanWidthArray
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._chanWidthArrayEqTolerance = Frequency(tolerance)

    def getChanWidthArrayEqTolerance(self):
        """
        A getter for the tolerance on chanWidthArray
        Returns the tolerance as a  Frequency
        """
        return self._chanWidthArrayEqTolerance

    # The tolerance which will be used on effectiveBw during an add operation on the table
    _effectiveBwEqTolerance = Frequency(0.0)

    def setEffectiveBwEqTolerance(self, tolerance):
        """
        A setter for the tolerance on effectiveBw
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._effectiveBwEqTolerance = Frequency(tolerance)

    def getEffectiveBwEqTolerance(self):
        """
        A getter for the tolerance on effectiveBw
        Returns the tolerance as a  Frequency
        """
        return self._effectiveBwEqTolerance

    # The tolerance which will be used on effectiveBwArray during an add operation on the table
    _effectiveBwArrayEqTolerance = Frequency(0.0)

    def setEffectiveBwArrayEqTolerance(self, tolerance):
        """
        A setter for the tolerance on effectiveBwArray
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._effectiveBwArrayEqTolerance = Frequency(tolerance)

    def getEffectiveBwArrayEqTolerance(self):
        """
        A getter for the tolerance on effectiveBwArray
        Returns the tolerance as a  Frequency
        """
        return self._effectiveBwArrayEqTolerance

    # The tolerance which will be used on resolution during an add operation on the table
    _resolutionEqTolerance = Frequency(0.0)

    def setResolutionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on resolution
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._resolutionEqTolerance = Frequency(tolerance)

    def getResolutionEqTolerance(self):
        """
        A getter for the tolerance on resolution
        Returns the tolerance as a  Frequency
        """
        return self._resolutionEqTolerance

    # The tolerance which will be used on resolutionArray during an add operation on the table
    _resolutionArrayEqTolerance = Frequency(0.0)

    def setResolutionArrayEqTolerance(self, tolerance):
        """
        A setter for the tolerance on resolutionArray
        """
        if not isinstance(tolerance, Frequency):
            print("tolerance must be a  Frequency instance")

        self._resolutionArrayEqTolerance = Frequency(tolerance)

    def getResolutionArrayEqTolerance(self):
        """
        A getter for the tolerance on resolutionArray
        Returns the tolerance as a  Frequency
        """
        return self._resolutionArrayEqTolerance

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

            # Initialize  spectralWindowId to Tag(0).
            x.setSpectralWindowId(Tag(0, TagType.SpectralWindow))

            # Record it in the dict.
            self._noAutoIncIds[key] = 0
        else:
            # There is already a combination of the non autoinc attributes values in the dict
            nextInt = int(self._noAutoIncIds[key]) + 1

            # Initialize  spectralWindowId to Tag(nextInt).
            x.setSpectralWindowId(Tag(nextInt, TagType.SpectralWindow))

            # Record it in the hashtable.
            self._noAutoIncIds[key] = nextInt

    def __init__(self, container):
        """
        Create a SpectralWindowTable attached to container.

        container must be a ASDM instance
        All tables must know the container
        """

        if not isinstance(container, pyasdm.ASDM):
            raise (
                ValueError("SpectralWindowTable constructor must use a ASDM instance")
            )

        self._container = container

        self._entity = Entity()
        self._entity.setEntityId(EntityId("uid://X0/X0/X0"))
        self._entity.setEntityIdEncrypted("na")
        self._entity.setEntityTypeName("SpectralWindowTable")
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
            print("SpectralWindow is not present in memory, setting from file")
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
        Returns "SpectralWindowTable" followed by the current size of the table
        between parenthesis.
        Example : SpectralWindowTable(12)
        """
        return "SpectralWindowTable(" + size() + ")"

    # ====> Row creation.

    def newRowDefault(self):
        """
        Create a new row with default values.
        The new row is not added to this table but it knows about it.
        """
        thisRow = SpectralWindowRow(self)
        return thisRow

    def add(self, x):
        """
        Look up the table for a row whose noautoincrementable attributes are matching their
        homologues in x.  If a row is found that row else autoincrement x.\spectralWindowId,
        add x to its table and returns x.

        returns a SpectralWindowRow.
        x. A row to be added.
        """
        if not isinstance(x, SpectralWindowRow):
            raise ValueError("x must be a  SpectralWindowRow instance.")

        aRow = self.lookup(
            x.getBasebandName(),
            x.getNetSideband(),
            x.getNumChan(),
            x.getRefFreq(),
            x.getSidebandProcessingMode(),
            x.getTotBandwidth(),
            x.getWindowFunction(),
        )
        if aRow is not None:
            return aRow

        # Autoincrement spectralWindowId
        x.setSpectralWindowId(Tag(self.size(), TagType.SpectralWindow))

        self._privateRows.add(x)
        x.isAdded()
        return x

    def newRow(
        self,
        basebandName,
        netSideband,
        numChan,
        refFreq,
        sidebandProcessingMode,
        totBandwidth,
        windowFunction,
    ):
        """
        Create a new SpectralWindowRow initialized to the specified values.

        The new row is not added to this table, but it does know about it.
        (the autoincrementable attribute, if any, is not in the parameter list)
        """

        thisRow = SpectralWindowRow(self)

        thisRow.setBasebandName(basebandName)

        thisRow.setNetSideband(netSideband)

        thisRow.setNumChan(numChan)

        thisRow.setRefFreq(refFreq)

        thisRow.setSidebandProcessingMode(sidebandProcessingMode)

        thisRow.setTotBandwidth(totBandwidth)

        thisRow.setWindowFunction(windowFunction)

        return thisRow

    def newRowCopy(self, row):
        """
        Create a new row using a copy constructor mechanism.

        The method creates a new SpectralWindowRow which knows about this table.
        Each attribute of the created row is a (deep) copy of the corresponding
        attribute of row. The method does not add the created row to this,
        it simply parents it to this, a call to the add method
        has to be done in order to get the row added (very likely after having modified
        some of its attributes.
        If row is None then the method returns a new SpectralWindowRow with default values for its attributes.
        """

        return SpectralWindowRow(self, row)

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
                x.getBasebandName(),
                x.getNetSideband(),
                x.getNumChan(),
                x.getRefFreq(),
                x.getSidebandProcessingMode(),
                x.getTotBandwidth(),
                x.getWindowFunction(),
            )
            is not None
        ):
            raise UniquenessViolationException(
                "Uniqueness violation exception in table SpectralWindowTable"
            )

        if self.getRowByKey(x.getSpectralWindowId()) is not None:
            raise DuplicateKey("Duplicate key exception in ", "SpectralWindowTable")

        self._privateRows.append(x)
        x.isAdded()
        return x

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows.
        return Alls rows as a list of SpectralWindowRow
        """
        return self._privateRows

    def getRowByKey(self, spectralWindowId):
        """
        Returns a SpectralWindowRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        param spectralWindowId.

        """
        for row in self._privateRows:

            if not row.getSpectralWindowId().equals(spectralWindowId):
                continue

            return row

        # no match found
        return None

    def lookup(
        self,
        basebandName,
        netSideband,
        numChan,
        refFreq,
        sidebandProcessingMode,
        totBandwidth,
        windowFunction,
    ):
        """
        Look up the table for a row whose all attributes  except the autoincrementable one
        are equal to the corresponding parameters of the method.
        return this row if any, None otherwise.


        param basebandName.

        param netSideband.

        param numChan.

        param refFreq.

        param sidebandProcessingMode.

        param totBandwidth.

        param windowFunction.

        """
        for row in self._privateRows:
            if row.compareNoAutoInc(
                basebandName,
                netSideband,
                numChan,
                refFreq,
                sidebandProcessingMode,
                totBandwidth,
                windowFunction,
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
        to the schema defined for SpectralWindow (SpectralWindowTable.xsd).

        returns a string containing the XML representation.
        """
        result = ""
        result += '<?xml version="1.0" encoding="ISO-8859-1"?> '
        result += '<SpectralWindowTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:spctrw="http://Alma/XASDM/SpectralWindowTable" xsi:schemaLocation="http://Alma/XASDM/SpectralWindowTable http://almaobservatory.org/XML/XASDM/4/SpectralWindowTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += self._entity.toXML()
        s = self._container.getEntity().toXML()
        # Change the "Entity" tag to "ContainerEntity".
        result += "<Container" + s[1:]
        for thisRow in self._privateRows:
            result += thisRow.toXML()
            result += " "
        result += "</SpectralWindowTable>"
        return result

    def fromXML(self, xmlstr):
        """
        Populate this table from the content of a XML document that is required to
        conform to the XML schema defined for a SpectralWindow (SpectralWindowTable.xsd).
        """
        if not isinstance(xmlstr, str):
            raise ConversionException("xmlstr must be a string")

        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of "SpectralWindowTable".
        if (
            not xmldom.hasChildNodes()
            or xmldom.firstChild.nodeName != "SpectralWindowTable"
        ):
            raise ConversionException(
                "XML is not from the expected table", "SpectralWindowTable"
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
                "schemaVersion is not an integer", "SpectralWindowTable"
            ) from None

        # go through the child nodes of tabdom
        # get Entity and rows, require ContainerEntity but don't get anything from that
        tabEntity = None
        hasContainerEntity = False

        if not tabdom.hasChildNodes():
            raise ConversionException(
                "XML is missing all of the expected elements", "SpectralWindowTable"
            )

        for thisNode in tabdom.childNodes:
            nodeName = thisNode.nodeName
            if nodeName == "Entity":
                if tabEntity is not None:
                    raise ConversionException(
                        "More than one Entity found in XML", "SpectralWindowTable"
                    )
                tabEntity = Entity(thisNode.toxml())
                if not (tabEntity.getEntityTypeName() == "SpectralWindowTable"):
                    raise ConversionException(
                        "Entity type name in XML is not the expected value of the table name",
                        "SpectralWindowTable",
                    )
            elif nodeName == "ContainerEntity":
                # there must be one, but no more than one
                if hasContainerEntity:
                    raise ConversionException(
                        "More than one ContainerEntity found in XML",
                        "SpectralWindowTable",
                    )
                hasContainerEntity = True
            elif nodeName == "row":
                try:
                    row = self.newRowDefault()
                    row.setFromXML(thisNode)
                    self.checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str(exc), "SpectralWindowTable") from None

                except UniquenessViolationException as exc:
                    msg = (
                        "UniquenessViolationException in row in SpectralWindowTable : %s"
                        % str(exc)
                    )

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "SpectralWindowTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "SpectralWindowTable")

        self.setEntity(tabEntity)

    def MIMEXMLPart(self):
        print("MIMEXMLPart not implemented for <SpectralWindowTable")
        return
        # the JAVA code looks like this
        # String UID = this.getEntity().getEntityId().toString();
        # String withoutUID = UID.substring(6);
        # String containerUID = this.getContainer().getEntity().getEntityId().toString();
        #
        # StringBuffer sb = new StringBuffer()
        # .append("<?xml version='1.0'  encoding='ISO-8859-1'?>")
        # .append("\n")
        # .append("<SpectralWindowTable xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:spctrw=\"http://Alma/XASDM/SpectralWindowTable\" xsi:schemaLocation=\"http://Alma/XASDM/SpectralWindowTable http://almaobservatory.org/XML/XASDM/4/SpectralWindowTable.xsd\" schemaVersion=\"4\" schemaRevision=\"-1\">\n")
        # .append("<Entity entityId='")
        # .append(UID)
        # .append("' entityIdEncrypted='na' entityTypeName='SpectralWindowTable' schemaVersion='1' documentVersion='1'/>\n")
        # .append("<ContainerEntity entityId='")
        # .append(containerUID)
        # .append("' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n")
        # .append("<BulkStoreRef file_id='")
        # .append(withoutUID)
        # .append("' byteOrder='Big_Endian' />\n")
        # .append("<Attributes>\n")

        # .append("<spectralWindowId/>\n")
        # .append("<basebandName/>\n")
        # .append("<netSideband/>\n")
        # .append("<numChan/>\n")
        # .append("<refFreq/>\n")
        # .append("<sidebandProcessingMode/>\n")
        # .append("<totBandwidth/>\n")
        # .append("<windowFunction/>\n")

        # .append("<numBin/>\n")
        # .append("<chanFreqStart/>\n")
        # .append("<chanFreqStep/>\n")
        # .append("<chanFreqArray/>\n")
        # .append("<chanWidth/>\n")
        # .append("<chanWidthArray/>\n")
        # .append("<correlationBit/>\n")
        # .append("<effectiveBw/>\n")
        # .append("<effectiveBwArray/>\n")
        # .append("<freqGroup/>\n")
        # .append("<freqGroupName/>\n")
        # .append("<lineArray/>\n")
        # .append("<measFreqRef/>\n")
        # .append("<name/>\n")
        # .append("<oversampling/>\n")
        # .append("<quantization/>\n")
        # .append("<refChan/>\n")
        # .append("<resolution/>\n")
        # .append("<resolutionArray/>\n")
        # .append("<numAssocValues/>\n")
        # .append("<assocNature/>\n")
        # .append("<assocSpectralWindowId/>\n")
        # .append("<imageSpectralWindowId/>\n")
        # .append("<dopplerId/>\n")
        # .append("</Attributes>\n")
        # .append("</SpectralWindowTable>\n");
        # return sb.toString();

    def toMIME(self):
        """
        Serialize this into a stream of bytes and encapsulates that stream into a MIME message.
        returns a string containing the MIME message.
        """
        print("toMIME not yet implemented for SpectralWindow")
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

        #    for (SpectralWindowRow row: privateRows) row.toBin(dos);

        #    // The closing MIME boundary
        #    dos.writeBytes("\n--MIME_boundary--");
        #    dos.writeBytes("\n");

        # } catch (IOException e) {
        #    throw new ConversionException(
        #            "Error while reading binary data , the message was "
        #            + e.getMessage(), "SpectralWindow");
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
    #    if (loc0 == -1 ) throw new ConversionException("Failed to detect the beginning of the XML header", "SpectralWindow");
    #
    #    loc0 += xmlPartMIMEHeader.length();
    #
    #    // Look for the string announcing the binary part.
    #    int loc1 = s.indexOf(binPartMIMEHeader, loc0);
    #    if (loc1 == -1) throw new ConversionException("Failed to detect the beginning of the binary part", "SpectralWindow");
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
    #     throw new ConversionException(e.getMessage(), "SpectralWindow");
    # }
    #
    # //
    # // Let's define a default order for the sequence of attributes.
    # //
    # ArrayList<String> attributesSeq = new ArrayList<String> ();

    #     attributesSeq.add("spectralWindowId"); attributesSeq.add("basebandName"); attributesSeq.add("netSideband"); attributesSeq.add("numChan"); attributesSeq.add("refFreq"); attributesSeq.add("sidebandProcessingMode"); attributesSeq.add("totBandwidth"); attributesSeq.add("windowFunction");
    #     attributesSeq.add("numBin");  attributesSeq.add("chanFreqStart");  attributesSeq.add("chanFreqStep");  attributesSeq.add("chanFreqArray");  attributesSeq.add("chanWidth");  attributesSeq.add("chanWidthArray");  attributesSeq.add("correlationBit");  attributesSeq.add("effectiveBw");  attributesSeq.add("effectiveBwArray");  attributesSeq.add("freqGroup");  attributesSeq.add("freqGroupName");  attributesSeq.add("lineArray");  attributesSeq.add("measFreqRef");  attributesSeq.add("name");  attributesSeq.add("oversampling");  attributesSeq.add("quantization");  attributesSeq.add("refChan");  attributesSeq.add("resolution");  attributesSeq.add("resolutionArray");  attributesSeq.add("numAssocValues");  attributesSeq.add("assocNature");  attributesSeq.add("assocSpectralWindowId");  attributesSeq.add("imageSpectralWindowId");  attributesSeq.add("dopplerId");

    # XPath xpath = null;
    # //
    # // And then look for the possible XML contents.
    # try {
    #     // Is it an "<ASDMBinaryTable ...." document (old) ?
    #    if (XPath.newInstance("/ASDMBinaryTable")
    #            .selectSingleNode(document) != null)
    #        byteOrder = ByteOrder.BIG_ENDIAN;
    #    else {
    #        // Then it must be a "<SpectralWindowTable ...." document
    #        // With a BulkStoreRef child element....
    #        XPath xpa = XPath.newInstance("/SpectralWindowTable/BulkStoreRef/@byteOrder");
    #        Object node = xpa.selectSingleNode(document.getRootElement());
    #        if (node == null)
    #            throw new ConversionException("No element found for the XPath expression '/SpectralWindowTable/BulkStoreRef/@byteOrder'. Invalid XML header '"+header+"'.", "SpectralWindow");
    #
    #        // Yes ? then it must have a "BulkStoreRef" element with a
    #        // "byteOrder" attribute.
    #        String bo = xpa.valueOf(document.getRootElement());
    #        if (bo.equals("Little_Endian"))
    #            byteOrder = ByteOrder.LITTLE_ENDIAN;
    #        else if (bo.equals("Big_Endian"))
    #            byteOrder = ByteOrder.BIG_ENDIAN;
    #        else
    #            throw new ConversionException("No valid value retrieved for the node '/SpectralWindowTable/BulkStoreRef/@byteOrder'. Invalid XML header '"+header+"'.", "SpectralWindow");
    #
    #        // And also it must have an Attributes element with children.
    #        xpa = XPath.newInstance("/SpectralWindowTable/Attributes#");
    #        List nodes = xpa.selectNodes(document.getRootElement());
    #        if (nodes==null || nodes.size()==0)
    #            throw new ConversionException("No element found for the XPath expression '/SpectralWindowTable/Attributes#'. Invalid XML header '"+header+"'.", "SpectralWindow");
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
    #    throw new ConversionException(e.getMessage(), "SpectralWindow");
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
    #        throw new ConversionException ("Failed to detect the beginning of the binary part", "SpectralWindow");
    #    }
    #
    #    entity = Entity.fromBin(bodis);
    #
    #    Entity containerEntity = Entity.fromBin(bodis);
    #
    #    int numRows = bodis.readInt();
    #    for (int i = 0; i < numRows; i++) {
    #    this.checkAndAdd(SpectralWindowRow.fromBin(bodis, this, attributesSeq.toArray(new String[0])));
    #    }
    # } catch (TagFormatException e) {
    #    throw new ConversionException( "Error while reading binary data , the message was "
    #        + e.getMessage(), "SpectralWindow");
    # }catch (IOException e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "SpectralWindow");
    # } catch (DuplicateKey e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "SpectralWindow");
    # }catch (Exception e) {
    #    throw new ConversionException(
    #        "Error while reading binary data , the message was "
    #        + e.getMessage(), "SpectralWindow");
    # }
    # }

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a SpectralWindowTable as those produced  by the toFile method.
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
                "SpectralWindowTable",
            )

        if os.path.exists(os.path.join(directory, "SpectralWindow.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "SpectralWindow.bin")):
            self.setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the SpectralWindow table", "SpectralWindowTable"
            )

    def setFromMIMEFile(self, directory):
        """
        Set this table from a MIME file.
        Used internally by setFromFile. Not intented for external use.
        """
        print("setFromMIME file not yet implemented for SpectralWindowTable")
        return

        # java code looks like this
        # File file = new File(directory+"/SpectralWindow.bin");
        #
        # byte[] bytes = null;
        #
        # try {
        #     InputStream is = new FileInputStream(file);
        #     long length = file.length();
        #     if (length > Integer.MAX_VALUE)
        #         throw new ConversionException ("File " + file.getName() + " is too large", "SpectralWindow");
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
        #        throw new ConversionException("Could not completely read file "+file.getName(), "SpectralWindow");
        #    }
        #    is.close();
        # }
        # catch (IOException e) {
        #    throw new ConversionException("Error while reading "+file.getName()+". The message was " + e.getMessage(),
        #    "SpectralWindow");
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
            with open(os.path.join(directory, "SpectralWindow.xml")) as f:
                xmlstr = f.read()
        except Exception as exc:
            # reraise it as a ConversionException
            raise ConversionException(str(exc), "SpectralWindowTable") from None

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
                    "SpectralWindow found as XML but it should be written as binary, which is not yet implemetned. Setting to write as XML to preserve this content."
                )
                self._fileAsBin = False

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of its _fileAsBin data member a binary serialization
        of this (_fileAsBin==True) will be saved in a file "SpectralWindow.bin" or
        an XML representation (_fileAsBin==False) will be saved in a file "SpectralWindow.xml".
        The file is always written in a directory whose name is passed as a parameter.
        param directory The name of directory where the file containing the table's
        representation will be saved.
        raises ConversionException for any errors while writing that file.
        """
        if not isinstance(directory, str):
            raise ConversionException("directory must be a string")

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (SpectralWindow)"
                % directory,
                "SpectralWindowTable",
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
                "SpectralWindowTable",
            ) from None

        if self._fileAsBin:
            print("fileAsBin not yet implemented for SpectralWindow")
            # the Java code looks like this
            #
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)
            #
            # File xmlFile = new File(directory+"/SpectralWindow.xml");
            # if (xmlFile.exists())
            #    if (!xmlFile.delete())
            #        throw new ConversionException("Problem while trying to delete a previous version of '"+xmlFile.toString()+"'", "SpectralWindow");
            #
            # File binFile = new File(directory+"/SpectralWindow.bin");
            # if (binFile.exists())
            #    if (!binFile.delete())
            #        throw new ConversionException("Problem while trying to delete a previous version of '"+binFile.toString()+"'", "SpectralWindow");
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
        #     throw new ConversionException("Problem while writing the binary representation, the message was : " + e.getMessage(), "SpectralWindow");
        # }
        # catch (IOException e) {
        #      throw new ConversionException("Problem while writing the binary representation, the message was : " + e.getMessage(), "SpectralWindow");
        # }
        # }
        else:
            # The table is totally exported in a XML file.
            filePath = os.path.join(directory, "SpectralWindow.xml")
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
                        "SpectralWindowTable",
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
                    "SpectralWindow",
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
