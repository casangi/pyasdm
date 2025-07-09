Examples
======================================================

Examples may eventually be found in one or more jupyter notebook(s). This is very preliminary.
Note that pyasdm can not read ASDM with versions < "3" (the schemaVersion
value in the ASDM.xml file).

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
*pyasdm* layer are the container ( *ASDM* , *enumerations* , *exceptions* , *types* , and *utils* .
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
enumeration there are 2 types.::

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
*getStatesUsingStateId* ).

For the ASDM tables and rows and types and enumerations, python
lists are used when there are multiple values (and sometimes
lists of list or lists of lists of lists when the number of
dimensions in that field is more than 1, the sdm currently has
cases up to 4 dimensions). For the binary file, the binary
data itself is returned as numpy arrays.::

    >>> mr[0].getBDFPath()
    '/users/bgarwood/casa/casatestdata/sdm/uid___A002_X71e4ae_X317_short/ASDMBinary/uid___A002_X71e4ae_X328'
    >>> bdf = pyasdm.bdf.BDFReader()
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


Here, the *getHeader* method returns a BDFHeader instance. It has getters for
each of these fields. Some of them are simple values, others are
enumerations, etc. This shows the organization of the data. Namely that there
are 4 basebands here and that each baseband has a single spectral window.
Each spectral window has an item that indicates the cross and single dish (auto)
correlation products. The scale factor is used to scale the crossData values
for that spectral window in that baseband. In general, each baseband could
have multiple spectral windows, with different scale factors and cross and
sd pol products. The baseband information summarized here is currently
available as a list of dict values with one dict valeu for each
baseband, in order, through *getBasebandsList()* .

At the end are shown the possible binary components that may be found in
this BDF. The binary components are found in data subsets. A subset is
retrieve by the *getSubset* method and the *hasSubset* method indicates
that there are still more subsets available from that bdf. After the
*open* method returns the position of the BDF is just before the first
subset. For each type of binary data the header shows the expected size
in a subset (if that type is found) and the axes used. See the BDF format
documentation for more details on the meanings.

Eventually the binary data will be available in one or more views that
are useful to downstream users. The c++ code provides views that are
appropriate when filling a single row of a MS v2 or multiple rows of a
MS v2. Neither one of those views are liable to be useful to VIPER.::

    >>> bh = bdf.getHeader()
    >>> bh.getTitle()
    'ALMA BL Correlator Spectral Data'
    >>> print(bh.getProcessorType())
    CORRELATOR
    >>> bb_dict = bh.getBasebandsList()[1]
    >>> bb_dict
    {'name': 'BB_2', 'spectralWindows': [{'crossPolProducts': [<pyasdm.enumerations.StokesParameter.StokesParameter object at 0x7f1c8f560dd0>, <pyasdm.enumerations.StokesParameter.StokesParameter object at 0x7f1c8f560e10>], 'sdPolProducts': [<pyasdm.enumerations.StokesParameter.StokesParameter object at 0x7f1c8f560ed0>, <pyasdm.enumerations.StokesParameter.StokesParameter object at 0x7f1c8f560f10>], 'scaleFactor': np.float32(168374.58), 'numSpectralPoint': 128, 'numBin': 1, 'sideband': <pyasdm.enumerations.NetSideband.NetSideband object at 0x7f1c9046b610>, 'sw': '2'}]}
    >>> bh.getBinaryTypes()
    ['flags', 'actualTimes', 'actualDurations', 'zeroLags', 'crossData', 'autoData']
    >>> bh.getAxesNames('crossData')
    ['BAL', 'BAB', 'SPP', 'POL']
    >>> bh.getSize('crossData')
    890880

This illustrates how some of these values are enumerations. It shows the
available binary types and the list of axes and size for the crossData
type. In this case, BAL is the baseline axis, BAB is the baseband axis,
SPP is the spectral axis (channels) and POL is the axes necessary to hold
all of the pol products shown for the spectral window in question. In
the more general case that can be complicated, but here there are 30
antennas so the number of BAL elements is 30x29/2 (435), there are
4 basebands, each baseband has a single spectral window with 128 channels,
and there are 2 elements along the POL axis. In addition, crossData is
stored as a pair of values, one each for the real and imaginary parts.
So the expected size here is 435x4x128x2x2 or 890880, as indicated by
the size value.::

    >>> bdf.hasSubset()
    True
    >>> ss = bdf.getSubset()
    >>> ss.keys()
    dict_keys(['projectPath', 'integrationNumber', 'subIntegrationNumber', 'midpointInNanoSeconds', 'intervalInNanoSeconds', 'aborted', 'stopTime', 'abortReason', 'actualTimes', 'actualDurations', 'crossData', 'autoData', 'flags', 'zeroLags'])
    >>> ss['projectPath']
    '1/1/1/1'
    >>> ss['actualTimes']
    {'present': False, 'startsAt': -1, 'arr': None, 'type': 'INT64_TYPE', 'np_type': dtype('int64')}
    >>> for t in bh.getBinaryTypes():
    ...     print('%s : %s' % (t,ss[t]['present']))
    ... 
    flags : True
    actualTimes : False
    actualDurations : False
    zeroLags : True
    crossData : True
    autoData : True
    >>> ss['crossData']
    {'present': True, 'startsAt': 18130, 'arr': array([ 13,  43,  72, ...,  29, -59,  26], shape=(890880,), dtype=int16), 'type': 'INT16_TYPE', 'np_type': dtype('int16')}

    >>> # iterate through to the end with (not all shown, there are 5 subsets in this BDF)
    >>> bdf.hasSubset()
    True
    >>> ss = bdf.getSubset()
    >>> # until bdf.hasSubset() return False

The subset is a dictionary at the moment. It may become a class
as development of pyasdm continues. The dictionary has several
fields that describe the subset and then it has a field for each
of the binary types indicated by the global header. Each of those
is itself a dictionary. Not all binary types will be found in each
subset. Here, this subset has flags, zeroLags, crossData and autoData.
The *present* field indicates whether it's present in that subset.
The *arr* field is the array of values found, when present and
*startsAt* is the starting location of those bytes in the file (that
could be used to skip to that location and read just those values
once the type and byte order is known). Note that crossData can be
stored as a scaled integer (either 16 or 32 bit integers). The
floating point values are recovered by dividing the integer values
by the scaleFactor from the global header for that spectral window
and baseband. The format also allows crossData to be stored as 32 bit
floating point values.

Eventually additional code will exist that will serve these values
up in a form that is useful for downstream processing, with the
accompanying meta information from ASDM as necessary (the views
discussed earlier).

Example 2
---------

The WSU data will have a single spectral window in each BDF and so
extracting and scaling the crossData will be simplified because
the BAB axis will always have a single element and the SPP axis
will then be a single number instead of something that depends
on the BAB element being used.

This example is from an SDM that where the BDFs were split to look
like how we think WSU data will look like. The script to split a
BDF is not robust for general use and is not part of pyasdm. The
data used here is from a personal copy to illustrate the difference.

Note: eventually it will be possible to close and reopen an ASDM, as
it already is with a BDF. Tests indicate that something isn't being
cleared properly so that does not yet work. If trying another
ASDM or BDF you should currently create one each time, as in
this example.
::

    >>> asdm = pyasdm.ASDM()
    >>> asdm.setFromFile('~/casa/split_data/uid___A002_X10d9399_X6279')
    >>> mt = asdm.getMain()
    >>> mr = mt.get()
    >>> bdf = pyasdm.bdf.BDFReader()
    >>> bdf.open(mr[4].getBDFPath())
    >>> bh = bdf.getHeader()
    >>> print(bh)
    XML Schema version = 2
    Byte order = Little_Endian
    startTime = 5202971372592000000
    dataOID = uid://A002/X10d9399/Xe6d
    title = ALMA ACA Correlator Spectral Data
    dimensionality = 1
    execBlockUID = uid://A002/X10d9399/X6279
    execBlockNum = 1
    scanNum = 1
    subscanNum = 1
    numAntenna = 9
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
    flags:
	    size = 90
	    axes = BAL ANT BAB POL
    actualTimes:
	    size = 90
	    axes = BAL ANT BAB POL
    actualDurations
	    size = 90
	    axes = BAL ANT BAB POL
    crossData
            size = 18432
	    axes = BAL BAB SPP POL
    autoData
	    size = 2304
	    axes = ANT BAB SPP POL
	    normalized = True

    >>> ss = bdf.getSubset()
    >>> ss['crossData']
    {'present': True, 'startsAt': 4200, 'arr': array([ 81,   6, -46, ...,  25,  53, -44], shape=(18432,), dtype=int16), 'type': 'INT16_TYPE', 'np_type': dtype('int16')}
    >>> import numpy as np
    >>> farr = ss['crossData']['arr'].astype(np.float32)
    >>> spw = bh.getBasebandsList()[0]['spectralWindows'][0]
    >>> scaleFactor = spw['scaleFactor']
    >>> farr /= scaleFactor
    >>> nAnt = bh.getNumAntenna()
    >>> nbl = int(nAnt*(nAnt-1)/2)
    >>> nchan = spw['numSpectralPoint']
    >>> npol = len(spw['crossPolProducts'])
    >>> shape = (nbl,nchan,npol,2)
    >>> farr_shaped = farr.reshape(shape)
    >>> carr_shaped = farr_shaped[:,:,:,0] + 1j * farr_shaped[:,:,:,1]
    >>> carr_shaped.shape
    (36, 128, 2)
    >>> carr_shaped[0,0,0]
    np.complex64(0.00048107025+3.5634832e-05j)

    

This subset also has actualTimes and actualDurations and does not have
flags or zeroLags data.

Knowing that there is a single baseband here with a single spectral window
simplifies extracting the data. Here, the crossData array is converted
to a 32-bit float array and the scale factor is applied. The array is
then reshaped, including the real and imaginary array implied as the
final axis (note that the baseband axis is skipped in makeing the shape
as it as a single element here). Then a complex array is created from the
real and imaginary parts of the floating point values and the value at the
origin of the resulting array is printed. The axes are baseline, channel,
and polarization (here "XX" and "YY"). See the BDF documentation for
how baseline are ordered.

All of this illustrates the need for well-defined views that are useful for
VIPER use. Presenting the data in such a view isn't difficult, but
that detail obviously needs to be hidden from the user.


    

