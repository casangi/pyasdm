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
            # print("SpectralWindow is not present in memory, setting from file")
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
        result += '<SpectralWindowTable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:spctrw="http://Alma/XASDM/SpectralWindowTable" xsi:schemaLocation="http://Alma/XASDM/SpectralWindowTable http://almaobservatory.org/XML/XASDM/4/SpectralWindowTable.xsd" schemaVersion="4" schemaRevision="-1">\n'
        result += "<Entity entityId='"
        result += uidStr
        result += "' entityIdEncrypted='na' entityTypeName='SpectralWindowTable' schemaVersion='1' documentVersion='1'/>\n"
        result += "<ContainerEntity entityId='"
        result += containerUID
        result += "' entityIdEncrypted='na' entityTypeName='ASDM' schemaVersion='1' documentVersion='1'/>\n"
        result += "<BulkStoreRef file_id='"
        result += withoutUID
        result += "' byteOrder='" + str(byteOrder) + "' />\n"
        result += "<Attributes>\n"

        result += "<spectralWindowId/>\n"
        result += "<basebandName/>\n"
        result += "<netSideband/>\n"
        result += "<numChan/>\n"
        result += "<refFreq/>\n"
        result += "<sidebandProcessingMode/>\n"
        result += "<totBandwidth/>\n"
        result += "<windowFunction/>\n"

        result += "<numBin/>\n"
        result += "<chanFreqStart/>\n"
        result += "<chanFreqStep/>\n"
        result += "<chanFreqArray/>\n"
        result += "<chanWidth/>\n"
        result += "<chanWidthArray/>\n"
        result += "<correlationBit/>\n"
        result += "<effectiveBw/>\n"
        result += "<effectiveBwArray/>\n"
        result += "<freqGroup/>\n"
        result += "<freqGroupName/>\n"
        result += "<lineArray/>\n"
        result += "<measFreqRef/>\n"
        result += "<name/>\n"
        result += "<oversampling/>\n"
        result += "<quantization/>\n"
        result += "<refChan/>\n"
        result += "<resolution/>\n"
        result += "<resolutionArray/>\n"
        result += "<numAssocValues/>\n"
        result += "<assocNature/>\n"
        result += "<assocSpectralWindowId/>\n"
        result += "<imageSpectralWindowId/>\n"
        result += "<dopplerId/>\n"
        result += "</Attributes>\n"
        result += "</SpectralWindowTable>\n"

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
                "SpectralWindow",
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
                "Failed to detect the begining of the XML header.", "SpectralWindow"
            )

        loc0 += len(xmlPartMIMEHeader)

        # Look for the string announcing the binary part.
        loc1 = headerBytes.find(binPartMIMEHeader, loc0)
        if loc1 < 0:
            byteStream.close()
            raise ConversionException(
                "Failed to detect the begining of the binary part.", "SpectralWindow"
            )

        # extract the XML header as a string
        xmlHeader = headerBytes[loc0:loc1].decode()

        xmldom = minidom.parseString(xmlHeader)
        if not xmldom.hasChildNodes():
            byteStream.close()
            raise ConversionException(
                "XML is not properly structured.", "SpectralWindow"
            )

        attributesSeq = []
        byteOrderStr = None
        versionStr = "-1"

        hdrdom = xmldom.firstChild
        if hdrdom.nodeName == "ASDMBinaryTable":
            # old style of binary data
            # assume Big_Endian and the default order of the elements
            byteOrderStr = "Big_Endian"

            attributesSeq.append("spectralWindowId")

            attributesSeq.append("basebandName")

            attributesSeq.append("netSideband")

            attributesSeq.append("numChan")

            attributesSeq.append("refFreq")

            attributesSeq.append("sidebandProcessingMode")

            attributesSeq.append("totBandwidth")

            attributesSeq.append("windowFunction")

            attributesSeq.append("numBin")

            attributesSeq.append("chanFreqStart")

            attributesSeq.append("chanFreqStep")

            attributesSeq.append("chanFreqArray")

            attributesSeq.append("chanWidth")

            attributesSeq.append("chanWidthArray")

            attributesSeq.append("correlationBit")

            attributesSeq.append("effectiveBw")

            attributesSeq.append("effectiveBwArray")

            attributesSeq.append("freqGroup")

            attributesSeq.append("freqGroupName")

            attributesSeq.append("lineArray")

            attributesSeq.append("measFreqRef")

            attributesSeq.append("name")

            attributesSeq.append("oversampling")

            attributesSeq.append("quantization")

            attributesSeq.append("refChan")

            attributesSeq.append("resolution")

            attributesSeq.append("resolutionArray")

            attributesSeq.append("numAssocValues")

            attributesSeq.append("assocNature")

            attributesSeq.append("assocSpectralWindowId")

            attributesSeq.append("imageSpectralWindowId")

            attributesSeq.append("dopplerId")

            versionStr = "2"

        else:
            # c++ and Java just assume it then must be a SpectralWindow table
            # this is more insistant, just in case
            if hdrdom.nodeName != "SpectralWindowTable":
                byteStream.close()
                raise ConversionException(
                    "XML Header is not from the expected table.", "SpectralWindow"
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
                    "SpectralWindow",
                )

            # loop through the child nodes, looking for BulkStoreRef and Attributes
            for hdrnode in hdrdom.childNodes:
                if hdrnode.nodeName == "BulkStoreRef":
                    if byteOrderStr is not None:
                        byteStream.close()
                        raise ConversionException(
                            "More than one BulkStoreRef element seen. Invalid XML header.",
                            "SpectralWindow",
                        )
                    if not hdrnode.hasAttributes():
                        byteStream.close()
                        raise ConversionException(
                            "BulkStoreRef does not contain any attributes. Invalid XML header.",
                            "SpectralWindow",
                        )
                    byteOrderAttr = hdrnode.attributes.getNamedItem("byteOrder")
                    if byteOrderAttr is None:
                        byteStream.close()
                        raise ConversionException(
                            "byteOrder attribute not found in BulkStoreRef element. Invalid XML header.",
                            "SpectralWindow",
                        )
                    byteOrderStr = byteOrderAttr.value
                elif hdrnode.nodeName == "Attributes":
                    if len(attributesSeq) > 0:
                        byteStream.close()
                        raise ConversionException(
                            "More than one Attributes node seen. Invalid XML header.",
                            "SpectralWindow",
                        )
                    if not hdrnode.hasChildNodes():
                        byteStream.close()
                        raise ConversionException(
                            "Attributes element has no child nodes. Invalid XML header.",
                            "SpectralWindow",
                        )
                    for attrnode in hdrnode.childNodes:
                        if attrnode.nodeType == attrnode.ELEMENT_NODE:
                            attributesSeq.append(str(attrnode.nodeName))

        if byteOrderStr is None:
            byteStream.close()
            raise ConversionException(
                "BulkStoreRef element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "SpectralWindow",
            )

        if len(attributesSeq) == 0:
            byteStream.close()
            raise ConversionException(
                "Attributes element not seen and this is not an older version 2 XML header. Invalid XML header.",
                "SpectralWindow",
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
                self.checkAndAdd(SpectralWindowRow.fromBin(eis, self, attributesSeq))
                # print("row %s added, loc = %s" % (i, eis.tell()))
        except Exception as exc:
            byteStream.close()
            eis.close()
            raise ConversionException(
                "Error while reading binary data, the exception was " + str(exc),
                "SpectralWindow",
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
        Used internally by setFromFile. Not intended for external use.
        """
        # The java and c++ versions read all of the contents into a byte array.
        # This uses a buffered byte stream. Created here and then
        # handed off to the setFromMIME method, which is responsible for closing it.

        filename = os.path.join(directory, "SpectralWindow.bin")
        byteStream = None
        try:
            byteStream = open(filename, "rb")
        except Exception as exc:
            raise ConversionException(
                "Error while opening " + filename + ". The exception was " + str(exc),
                "SpectralWindow",
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
            # The table is exported in a binary format.
            # (actually a short XML file + a possibly long MIME file)

            # Java defaults to Big_Endian
            # c++ defaults to Machine, go with c++
            byteOrder = ByteOrder()

            # first, just the short XML file
            xmlFilePath = os.path.join(directory, "SpectralWindow.xml")
            if os.path.exists(xmlFilePath):
                try:
                    os.remove(xmlFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + xmlFilePath
                        + ", exception caught "
                        + str(exc),
                        "SpectralWindow",
                    ) from None

            # used in both files
            mimeXMLpart = self.MIMEXMLPart(byteOrder)

            # this is all that is written to the XML file
            with open(xmlFilePath, "w") as xmlfile:
                xmlfile.write(mimeXMLpart)

            # now open the possibly much longer MIME file
            mimeFilePath = os.path.join(directory, "SpectralWindow.bin")
            if os.path.exists(mimeFilePath):
                try:
                    os.remove(mimeFilePath)
                except Exception as exc:
                    raise ConversionException(
                        "Could not remove existing "
                        + mimeFilePath
                        + ", exception caught "
                        + str(exc),
                        "SpectralWindow",
                    ) from None

            # the details are all handled in toMIME
            self.toMIME(mimeFilePath, mimeXMLpart, byteOrder)
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
