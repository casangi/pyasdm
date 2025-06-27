Examples
======================================================

Examples may eventually be found in one or more jupyter notebook(s). This is very preliminary.

.. toctree::
   :maxdepth: 2

Example 1
---------

Import the pyasdm module and open an existing ASDM. The pyasdm method
*setFromFile* uses *os.path.expanduser* to expand this path to the
full path. This example uses an SDM from the casatestdata repository,
use an appropriate path for where you have already installed casatestdata.::

  >>> import pyasdm
  >>> asdm = pyasdm.ASDM()
  >>> asdm.setFromFile("~/casa/casatestdata/sdm/uid___A002_X71e4ae_X317_short")

Following the c++ and Java class design, an ASDM is always instantiated
first and then set to a specific ASDM by giving it the path to the directory
containing that ASDM as shown here. Table instances are then fetched from
that ASDM and individual rows can be gotten from a table. The classes at the
*pyasdm* layer are the container (*ASDM*) and the tables and rows (e.g.
*MainTable* and *MainRow* are the classes that handle the Main table and
the individual rows within that table.

Below *pyasdm* are *bdf*, *enumerations*, *exceptions, *types*, and *utils*.
The *bdf* classes deal with reading a BDF (binary data file/format) file
(eventually that will also include classes to write a BDF to a file).
The *enumerations* are classes that handle the enumerations found in the SDM
by limiting the set of allowed values to those known to the model and translating
between how the enumerations are stored in an SDM (generally as integers). The
*types* are specific types known to the model, built on top of the standard
types (this is largely so that they can be read and written correctly) and
the *utils* and *exceptions* hold utility methods and the specific exceptions
added and used by pyasdm.

Note that only the ASDM container is loaded in that first example. None of the
contained tables that may exist have been read yet. In pyasdm, tables
are always loaded on demand.::

   >>> asdm.status()
   'Main' : IS present in _tableEntity, presentInMemory = False size = 0
   'AlmaRadiometer' : IS present in _tableEntity, presentInMemory = False size = 0
   'Annotation' : IS NOT present in _tableEntity, presentInMemory = True size = 0
   'Antenna' : IS present in _tableEntity, presentInMemory = False size = 0
   'CalAmpli' : IS present in _tableEntity, presentInMemory = False size = 0
   'CalAntennaSolutions' : IS NOT present in _tableEntity, presentInMemory = True size = 0
   'CalAppPhase' : IS NOT present in _tableEntity, presentInMemory = True size = 0
   'CalAtmosphere' : IS present in _tableEntity, presentInMemory = False size = 0
   'CalBandpass' : IS NOT present in _tableEntity, presentInMemory = True size = 0

Shown here is the first few lines of the output of *status* for this SDM. There
is one output line for each possible table that might exist in an SDM. The
line indicates "IS present" for a table that is already present (it exists) in that
SDM and "IS NOT present" if that table does not exist on disk. Note that initially
the tables that exist have *False* for "presentInMemory". That's because they have
not yet been loaded. That is also why their size is 0. For tables that do not exist
on disk, they DO exist as a zero-sized table. Rows could be added. If that SDM
is then written to disk that table with newly added rows would then be written
to disk. That's not shown in this example.::

  >>> mt = asdm.getMain()
  >>> mt.size()
  30
  >>> mt.getName()
  'Main'
  >>> mt.getKeyName()
  ['time', 'configDescriptionId', 'fieldId']
  >>> mr = mt.get()
  >>> len(mr)
  30
  >>> print(mr[0].toXML())
  <row> 
  <time> 4890409738560000000 </time> <numAntenna> 30 </numAntenna> <timeSampling> INTEGRATION </timeSampling> <interval> 10080000000 </interval> <numIntegration> 5 </numIntegration> <scanNumber> 1 </scanNumber> <subscanNumber> 1 </subscanNumber> <dataSize> 9610595 </dataSize> <dataUID> <EntityRef entityId="uid://A002/X71e4ae/X328" partId="X00000000" entityTypeName="Main" documentVersion="1"/> </dataUID> <configDescriptionId> ConfigDescription_0 </configDescriptionId> <execBlockId> ExecBlock_0 </execBlockId> <fieldId> Field_0 </fieldId> <stateId> 1 30 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 State_0 </stateId> </row>

This first gets the Main table. You can see that it's size is 30 rows and it's name is "Main".
The *getKeyName* method returns the list of key fields in the table. These can be
used to select the row that matches a specific set of Key values but that method doesn't
support wildcards or ranges and so for a table like Main is not terribly useful. The
full listof rows found in Main is returned by *get* and this example shows that it returned
30 rows. Each element is a MainRow instance. The *toXML* method returns the full row
as an XML string (this is what is used to write the rows of a table to disk).::

  >>> mr[0].getDataSize()
  9610595
  >>> mr[0].getNumAntenna()
  30
  >>> mr[0].getConfigDescriptionId()
  <pyasdm.types.Tag.Tag object at 0x7f0d936af200>
  >>> print(mr[0].getConfigDescriptionId())
  ConfigDescription_0
  >>> print(mr[0].getDataUID())
  <EntityRef entityId="uid://A002/X71e4ae/X328" partId="X00000000" entityTypeName="Main" documentVersion="1"/>
  >>> print(mr[0].getTimeSampling())
  INTEGRATION
  >>> pyasdm.enumerations.TimeSampling.names()
  ['SUBINTEGRATION', 'INTEGRATION']


There are getters and setters for each of the fields in a row. For standard types, they return
a value as shown here for *dataSize* and *numAntenna* (note that the method name for
a get function is the field name with the first letter in upper case).

Here, *configDescriptionId* is stored as a *Tag* type (which is how fields that
indicate rows in other tables are stored) and *dataUID* is an *EntityRef* type.
Specific types have *__str__* method so they should print out in a useful
form.

Note also that *stateId* is a 1-D array of values. In this case, there
is 1 value for each antenna. In the XML form the dimensionality is shown first
followed by the number of values and then the individual values. In this case,
the values are all *Tag* types indicating a row in the State table and they
all have the same value.

The *timeSampling* field is an example of an *enumeration* instance. The
static member *names* can be used for any enumeration class to show all of
the allowed names for that type of enumeration. For the *TimeSampling*
enumeration there are 2 types.

    >>> frow = mr[0].getFieldUsingFieldId()
    >>> print(frow.toXML())
    <row> 
    <fieldId> Field_0 </fieldId> <fieldName> J1924-2914 </fieldName> <numPoly> 1 </numPoly> <delayDir> 2 1 2 5.082621016035585 -0.5103639492133764 </delayDir> <phaseDir> 2 1 2 5.082621016035585 -0.5103639492133764 </phaseDir> <referenceDir> 2 1 2 5.082621016035585 -0.5103639492133764 </referenceDir> <time> 4890409733520000000 </time> <code> none </code> <directionCode> J2000 </directionCode> <sourceId> 0 </sourceId> </row>
    >>> srow = mr[0].getStateUsingStateId(10)
    >>> print(srow.toXML())
    <row> 
    <stateId> State_0 </stateId> <calDeviceName> NONE </calDeviceName> <sig> True </sig> <ref> True </ref> <onSky> True </onSky> <weight> 1.0 </weight> </row>

Some fields in a row indicate a row in another table. The row class has methods that can be used to get
the instance of the indicated row as shown here for *fieldId*. For cases
like *stateId* you can either get a single StateRow instance as shown
here (getting the one for element 10 in that list of stateId values)
or you can get all of the rows as a list of rows using the
appropriate getter for that field in that row (here it is
*getStatesUsingStateId*)

For the ASDM tables and rows and types and enumerations, python
lists are used when there are multiple values (and sometimes
lists of list or lists of lists of lists when the number of
dimensions in that field is more than 1, the sdm currently has
cases up to 4 dimensions). For the binary file, the binary
data itself is returned as numpy arrays.

    >>> mr[0].getBDFPath()
    '/users/bgarwood/casa/casatestdata/sdm/uid___A002_X71e4ae_X317_short/ASDMBinary/uid___A002_X71e4ae_X328'
    >>> bdf = pyasdm.bfd.BDFReader()
    >>> bdf.open(mr[0].getBDFPath())
    >>> print(bdf.getHeader())
    XML Schema version = 2
    Byte order = Little_Endian
    startTime = 4890409733520000000
    dataOID = uid://A002/X71e4ae/X328
    title = ALMA BL Correlator Spectral Data
    dimensionality = 1
    execBlockUID = uid://A002/X71e4ae/X317
    execBlockNum = 1
    scanNum = 1
    subscanNum = 1
    numAntenna = 30
    correlationMode = CROSS_AND_AUTO
    spectralResolutionType = FULL_RESOLUTION
    processorType = CORRELATOR
    atmospheric phase correction = AP_UNCORRECTED
    baseband #0:
	    name = BB_1
	    spectralWindow #0:
	    	    sw = 1
		    crossPolProducts = XX YY
		    sdPolProducts = XX YY
		    scaleFactor = 168374.57812
		    numSpectralPoint = 128
		    numBin = 1
		    sideband = LSB
    baseband #1:
            name = BB_2
            spectralWindow #0:
		    sw = 2
		    crossPolProducts = XX YY
		    sdPolProducts = XX YY
		    scaleFactor = 168374.57812
		    numSpectralPoint = 128
		    numBin = 1
		    sideband = LSB
    baseband #2:
	    name = BB_3
	    spectralWindow #0:
		    sw = 3
		    crossPolProducts = XX YY
		    sdPolProducts = XX YY
		    scaleFactor = 168374.57812
		    numSpectralPoint = 128
		    numBin = 1
		    sideband = USB
    baseband #3:
	    name = BB_4
	    spectralWindow #0:
	    	    sw = 4
		    crossPolProducts = XX YY
		    sdPolProducts = XX YY
		    scaleFactor = 168374.57812
		    numSpectralPoint = 128
		    numBin = 1
		    sideband = USB
    flags:
	    size = 3720
	    axes = BAL ANT BAB POL
    actualTimes:
	    size = 3720
	    axes = BAL ANT BAB POL
    actualDurations
	    size = 3720
	    axes = BAL ANT BAB POL
    zeroLags
	    size = 240
	    axes = BAL BAB POL
	    correlatorType = FXF
    crossData
	    size = 890880
	    axes = BAL BAB SPP POL
    autoData
	    size = 30720
	    axes = ANT BAB SPP POL
	    normalized = True




    

