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
from .Representable import Representable

# All of the extended types are imported
from pyasdm.types import *

from .exceptions.ConversionException import ConversionException
from .exceptions.DuplicateKey import DuplicateKey

# using minidom instead of Parser
from xml.dom import minidom

import os


class SpectralWindowTable(Representable):
    """
    The SpectralWindowTable class is an Alma table.

     Role
     Spectral window description. The convention in ALMA is to describe the  frequency axis in the topocentric reference frame. If this is not  the case (for instance if active Doppler tracking is implemented) then  \texttt{measFreqRef} should be set accordingly.

     Generated from model's revision -1, branch

     Attributes of SpectralWindow

                  Key

    spectralWindowId Tag identifies a unique row in the table.



                  Value (Mandatory)

    basebandName BasebandName  identifies the baseband.

    netSideband NetSideband  identifies the net sideband.

    numChan int  the number of frequency channels.

    refFreq Frequency  the reference frequency.

    sidebandProcessingMode SidebandProcessingMode  identifies the sideband processing mode.

    totBandwidth Frequency  the total bandwidth.

    windowFunction WindowFunction  identifies the window function.



                  Value (Optional)

    numBin int  the number of channels used in any post-FFT averaging.

    chanFreqStart Frequency  the frequency of the first channel.

    chanFreqStep Frequency  the increment between two successive frequencies.

    chanFreqArray Frequency []   numChan  the frequencies defined as an array (\texttt{numChan} values).

    chanWidth Frequency  the nominal channel width.

    chanWidthArray Frequency []   numChan  Array of channel widths.

    correlationBit CorrelationBit  identifies the number of bits used in the signal representation.

    effectiveBw Frequency  the effective noise bandwidth.

    effectiveBwArray Frequency []   numChan  array of effective bandwidths.

    freqGroup int  the frequency group number.

    freqGroupName str  the frequency group name.

    lineArray bool []   numChan  indicates lines (true) versus baselines (false).

    measFreqRef FrequencyReferenceCode  the reference frame of the frequencies.

    name str  a name for this spectral window.

    oversampling bool  data are "oversampled" (true) or not (false).

    quantization bool  a quantization correction has been applied (true) or not applied (false).

    refChan double  the reference channel "number".

    resolution Frequency  the effective spectral resolution of one channel (see note).

    resolutionArray Frequency []   numChan  the array of frequency resolution.

    numAssocValues int  the number of associated values.

    assocNature SpectralResolutionType []   numAssocValues  the natures of the associations with the rows refered to by assocSpectralWindowId.

    assocSpectralWindowId Tag []   numAssocValues  refers to a collection of associated rows in the table.

    imageSpectralWindowId Tag  refers to a unique row in the table (image sideband description).

    dopplerId int  refers to a collection of rows in DopplerTable.


    """

    # This is True if the file is considered present in memory (nothing to be loaded).
    # The default state is True, ASDM will set this to False when it is loaded and this
    # table has non-zero rows.
    _presentInMemory = True

    # set to True while the file is loading, just in case
    _loadInProgress = False

    # the name of this table.
    _tableName = "SpectralWindow"

    # the list of field names that make up key 'key'.
    _key = ["spectralWindowId"]

    # the ASDM container that this table belongs to (set by constructor)
    _container = None

    # _archiveAsBin not used by python implementation
    # _archiveAsBin = False  # if True archive binary else archive XML
    _fileAsBin = False  # if True file binary else file XML

    # A list to store the SpectralWindowRow instances
    _privateRows = []

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
        self._refFreqEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on refFreq
    def getRefFreqEqTolerance(self):
        """
        A getter for the tolerance on refFreq
        """
        return self._refFreqEqTolerance

    # The tolerance which will be used on totBandwidth during an add operation on the table
    _totBandwidthEqTolerance = Frequency(0.0)

    def setTotBandwidthEqTolerance(self, tolerance):
        """
        A setter for the tolerance on totBandwidth
        """
        self._totBandwidthEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on totBandwidth
    def getTotBandwidthEqTolerance(self):
        """
        A getter for the tolerance on totBandwidth
        """
        return self._totBandwidthEqTolerance

    # The tolerance which will be used on chanFreqStart during an add operation on the table
    _chanFreqStartEqTolerance = Frequency(0.0)

    def setChanFreqStartEqTolerance(self, tolerance):
        """
        A setter for the tolerance on chanFreqStart
        """
        self._chanFreqStartEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on chanFreqStart
    def getChanFreqStartEqTolerance(self):
        """
        A getter for the tolerance on chanFreqStart
        """
        return self._chanFreqStartEqTolerance

    # The tolerance which will be used on chanFreqStep during an add operation on the table
    _chanFreqStepEqTolerance = Frequency(0.0)

    def setChanFreqStepEqTolerance(self, tolerance):
        """
        A setter for the tolerance on chanFreqStep
        """
        self._chanFreqStepEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on chanFreqStep
    def getChanFreqStepEqTolerance(self):
        """
        A getter for the tolerance on chanFreqStep
        """
        return self._chanFreqStepEqTolerance

    # The tolerance which will be used on chanFreqArray during an add operation on the table
    _chanFreqArrayEqTolerance = Frequency(0.0)

    def setChanFreqArrayEqTolerance(self, tolerance):
        """
        A setter for the tolerance on chanFreqArray
        """
        self._chanFreqArrayEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on chanFreqArray
    def getChanFreqArrayEqTolerance(self):
        """
        A getter for the tolerance on chanFreqArray
        """
        return self._chanFreqArrayEqTolerance

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

    # The tolerance which will be used on chanWidthArray during an add operation on the table
    _chanWidthArrayEqTolerance = Frequency(0.0)

    def setChanWidthArrayEqTolerance(self, tolerance):
        """
        A setter for the tolerance on chanWidthArray
        """
        self._chanWidthArrayEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on chanWidthArray
    def getChanWidthArrayEqTolerance(self):
        """
        A getter for the tolerance on chanWidthArray
        """
        return self._chanWidthArrayEqTolerance

    # The tolerance which will be used on effectiveBw during an add operation on the table
    _effectiveBwEqTolerance = Frequency(0.0)

    def setEffectiveBwEqTolerance(self, tolerance):
        """
        A setter for the tolerance on effectiveBw
        """
        self._effectiveBwEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on effectiveBw
    def getEffectiveBwEqTolerance(self):
        """
        A getter for the tolerance on effectiveBw
        """
        return self._effectiveBwEqTolerance

    # The tolerance which will be used on effectiveBwArray during an add operation on the table
    _effectiveBwArrayEqTolerance = Frequency(0.0)

    def setEffectiveBwArrayEqTolerance(self, tolerance):
        """
        A setter for the tolerance on effectiveBwArray
        """
        self._effectiveBwArrayEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on effectiveBwArray
    def getEffectiveBwArrayEqTolerance(self):
        """
        A getter for the tolerance on effectiveBwArray
        """
        return self._effectiveBwArrayEqTolerance

    # The tolerance which will be used on resolution during an add operation on the table
    _resolutionEqTolerance = Frequency(0.0)

    def setResolutionEqTolerance(self, tolerance):
        """
        A setter for the tolerance on resolution
        """
        self._resolutionEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on resolution
    def getResolutionEqTolerance(self):
        """
        A getter for the tolerance on resolution
        """
        return self._resolutionEqTolerance

    # The tolerance which will be used on resolutionArray during an add operation on the table
    _resolutionArrayEqTolerance = Frequency(0.0)

    def setResolutionArrayEqTolerance(self, tolerance):
        """
        A setter for the tolerance on resolutionArray
        """
        self._resolutionArrayEqTolerance = Frequency(tolerance)

    # A getter for the tolerance on resolutionArray
    def getResolutionArrayEqTolerance(self):
        """
        A getter for the tolerance on resolutionArray
        """
        return self._resolutionArrayEqTolerance

    def getKeyName(self):
        """
        Return the list of field names that make up "key" as a list of strings
        """
        return self._key

    def __init__(self, container):
        """
        Create a SpectralWindowTable attached to container, which must be a ASDM instance
        All tables must know the container to which they belong.
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

    def add(self, newrow):
        """
        Look up the table for a row whose noautoincrementable attributes are matching their
        homologues in newrow.  If a row is found return that row else autoincrement newrow.spectralWindowId,
        add newrow to its table and return newrow.

        returns a SpectralWindowRow.
        """

        aRow = self.lookup(
            newrow.getBasebandName(),
            newrow.getNetSideband(),
            newrow.getNumChan(),
            newrow.getRefFreq(),
            newrow.getSidebandProcessingMode(),
            newrow.getTotBandwidth(),
            newrow.getWindowFunction(),
        )
        if aRow is not None:
            return aRow

        # Autoincrement spectralWindowId, same as the number of this row in the table
        newrow.setSpectralWindowId(Tag(size(), TagType.SpectralWindow))

        newrow.isAdded()
        return newrow

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
        Create a new SpectralWindowRow. The new row is not added to this table, but it does know about it.
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

    def _checkAndAdd(self, newrow):
        """
        A private method to append a row to its table, used by input conversion
        methods. Not intended for external use.

        If this table has an autoincrementable attribute then check if newrow verifies the rule of uniqueness and raise an exception if not.
        Returns newrow.
        """

        if (
            self.lookup(
                newrow.getBasebandName(),
                newrow.getNetSideband(),
                newrow.getNumChan(),
                newrow.getRefFreq(),
                newrow.getSidebandProcessingMode(),
                newrow.getTotBandwidth(),
                newrow.getWindowFunction(),
            )
            is not None
        ):
            raise UniquenessViolationException(
                "Uniqueness violation exception in table SpectralWindowTable"
            )

        if self.getRowByKey(newrow.getSpectralWindowId()) is not None:
            raise DuplicateKey("Duplicate key exception in ", "SpectralWindowTable")

        self._privateRows.append(newrow)
        newrow.isAdded()
        return newrow

    # ====> methods returning rows.

    def get(self):
        """
        Get all rows as an array of SpectralWindowRow
        """
        return self._privateRows

    def getRowByKey(self, spectralWindowId):
        """
        Returns a SpectralWindowRow given a key.
        return the row having the key whose values are passed as parameters, or None if
        no row exists for that key.

        @param spectralWindowId.

        """
        for row in self._privateRows:

            if not row.getSpectralWindowId().equals(spectralWindowId):
                continue

            # this row matches these parameters
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

    # ====> conversion Methods

    def toXML(self):
        """
        Translate this table to an XML representation conforming
        to the schema defined for SpectralWindow (SpectralWindowTable.xsd).

        Returns a string containing the XML representation.
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
        xmldom = minidom.parseString(xmlstr)
        # this should have at least one child node with a name of SpectralWindowTable.
        if (
            not xmldom.hasChildNodes()
            or xmldom.firstChild.nodeName != "SpectralWindowTable"
        ):
            raise ConversionException(
                "XML is not from a the expected table", "SpectralWindowTable."
            )

        # ignore everything but the first child node
        tabdom = xmldom.firstChild

        # get the version from the schemaVersion attribute, which must be there
        if (not tabdom.hasAttributes()) or (
            tabdom.attributes.getNamedItem("schemaVersion") is None
        ):
            raise ConversionException(
                "schemaVersion not found in XML", "SpectralWindowTable"
            )
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
                    self._checkAndAdd(row)
                except DuplicateKey as exc:
                    # reraise it as a ConversionException
                    raise ConversionException(str, "SpectralWindowTable") from None

                except ValueError as exc:
                    # TBD when this turns up via template
                    msg = (
                        "UniquenessViolationException in row in SpectralWindowTable : %s"
                        % str(exc)
                    )

        if tabEntity is None:
            raise ConversionException("No Entity seen in XML", "SpectralWindowTable")
        if not hasContainerEntity:
            raise ValueError("No Container Entity seen in XL", "SpectralWindowTable")

        self.setEntity(tabEntity)

    def setFromFile(self, directory):
        """
        Reads and parses a file containing a representation of a SpectralWindowTable as those produced by the toFile method.
        This table is populated with the result of the parsing.
        The directory value is the name of the directory containing the file to be read and parsed.
        """

        # directory must exist as a directory
        if not os.path.isdir(directory):
            raise ConversionException(
                "Directory " + directory + " must be a path to an existing directory",
                "SpectralWindowTable",
            )

        if os.path.exists(os.path.join(directory, "SpectralWindow.xml")):
            self.setFromXMLFile(directory)
        elif os.path.exists(os.path.join(directory, "SpectralWindow.bin")):
            setFromMIMEFile(directory)
        else:
            raise ConversionException(
                "No file found for the SpectralWindow table", "SpectralWindowTable"
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
        with open(os.path.join(directory, "SpectralWindow.xml")) as f:
            xmlstr = f.read()

        if xmlstr is None:
            raise ConversionException(
                "SpectralWindow.xml is empty", "SpectralWindowTable"
            )

        # if the string contains '<BulkStoreRef' then this is stored in a bin file
        if xmlstr.find("<BulkStoreRef") != -1:
            self.setFromMIMEFile(directory)
        else:
            self.fromXML(xmlstr)

    def toFile(self, directory):
        """
        Stores a representation (binary or XML) of this table into a file.

        Depending on the boolean value of _fileAsBin, a binary serialization
        of this (_fileAsBin=True) will be saved in a file 'SpectralWindow.bin' or an
        XML representation (_fileAsBin==False) will be saved in a file 'SpectralWindow.xml'.
        The file is always written in a directory whose name is passed as a parameter.
        """

        if os.path.exists(directory) and not os.path.isdir(directory):
            raise ConversionException(
                "Cannot write into directory %s. This file already exists and is not a directory. (SpectralWindow)"
                % directory,
                "SpectralWindowTable",
            )

        if not os.path.exists(directory):
            # assume it can be created there, if not this will raise a FileNotFound exception here
            os.mkdir(directory)

        if self._fileAsBin:
            print("fileAsBin not yet implemented for SpectralWindow")
        else:
            # exported as an XML file.
            filePath = os.path.join(directory, "SpectralWindow.xml")
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
