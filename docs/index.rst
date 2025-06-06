ASDM backend for VIPER Framework
====================================

pyasdm is still under active development

.. toctree::
   :maxdepth: 2

   api

Overview
--------

pyasdm provides a pure-python interface to the ASDM content (tables and rows) and
the binary data (BDF) that is the part of that ASDM.

It follows the class design of the Java and c++ ASDM interface that is part of
ALMA software. The same c++ classes are also incorported into CASA.

Most of the pyasdm code is generated from the ASDM UML by the ALMA software build
process in the same way that the Java and c++ code is generated. The code follows
the Java implementation most closely although it does borrow from the c++ implementation
in several places.

The BDF classes in pyasdm are hand written following some of the design of the c++ code that
reads and parses BDF files. There is no Java code in ALMA that reads BDF files.

The ASDM code can write out an ASDM except for any BDF data. BDF write functionality is
planned but has not yet been started.

Documents
---------

- `SDM Tables Short Description <https://drive.google.com/file/d/16a3g0GQxgcO7N_ZabfdtexQ8r2jRbYIS/view>`_.
- `Science Data Model Binary Data Format <https://drive.google.com/file/d/1PMrZFbkrMVfe57K6AAh1dR1FalS35jP2/view>`_.

Todo
----

PackedData
    PackedData contains all of the integrations in a single data subset. The internal processing is slightly
    different. This type of data is not yet correctly handled. This not include correlator data, which is
    never packed.

Binary Tables
    Tables can be stored in binary form. These are read by the current classes but it follows the Java
    implementation which reads of the data into memory at once. For some tables (e.g. Pointing) that can
    use quite a lot of memory and can take a long time to read. See also the next item. The design of the
    ASDM allows for the size of a table stored in the ASDM.xml file to be different from what is actually
    found in that table. Since optional fields in a row of a table can come and go from row to row it's not
    possible to skip to a random row in a table without reading all of the previous rows (although it's
    not necessary to store them, see the next item) and it's not possible to be sure how many rows are in a
    table until all rows are read. The current behavior is unacceptable and so a way will be found to provide
    access to chunks of rows at a time without having all rows in memory. Stepping through a table in order
    will be efficient. Jumping to a random row will not be.

Row uniqueness checks
    The Java classes always check on row uniqueness for the required key fields when a table is ready. The
    c++ classes can optionally skip that step. Skipping that step can save considerable time when reading
    large binary tables (see the previous item). This needs to be implemented.
    
BDF write.
    This will be added.

Test code
    This will include equivalent test code for the c++ ALMA classes used by CASA and ALMA to ensure that all of the
    classes agree. There is currently no test code for the c++ (or Java) ASDM classes.

Documentation
    This obviously needs much work.
