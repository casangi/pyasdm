# a benchmark test for a named asdm
#
# python bencmark_asdm.py [--skip-uniqueness] path_to_asdm
#
# open the named asdm (with the uniqueness check turned off if the optional --skip-uniqueness
# parameter is set) and get each table present in the sdm and then get the full set of rows in
# each table.
# Summarize the time and sizes by table name. The to get the table from the
# asdm (open and read the rows into the internal lists), and the time to get the full set of rows
# from the table is shown. The size of the table object and
# the size of the returned rows are shown. Sizes are in bytes. The time is in seconds.
# the total number of rows read is shown and the number of expected rows (from the ASDM.xml file)
# are shown.

import argparse
import os
import sys
import time
from pympler import asizeof

import pyasdm

from pyasdm.exceptions.ConversionException import ConversionException

def benchmarkTable(container, tableName, tableNameWidth, checkRowUniqueness):
    startTime = time.perf_counter()
    thisTable = container.getTable(tableName)
    endTime = time.perf_counter()
    deltaGetTableTime = endTime - startTime
    timePerRow_in_ms = 1000.0 * deltaGetTableTime/thisTable.size()
    if thisTable.getCheckRowUniqueness() != checkRowUniqueness:
        print(f"Warning: mismatch checkRowUniqueness for {tableName}")
    
    rows = thisTable.get()

    # this breaks the table for some uses but it keeps asizeof from going
    # through the container and finding all of the other tables
    thisTable._container = None
    
    sizeTable = asizeof.asizeof(thisTable)
    sizeRows = asizeof.asizeof(rows)

    tablePath = os.path.join(container.getDirectory(),tableName)
    tableType = "xxx"
    if (os.path.exists(tablePath+".bin")):
        tableType = "bin"
        tablePath = tablePath+".bin"
    else:
        tableType = "xml"
        tablePath = tablePath+".xml"

    strFileSize = "unknown"
    if os.path.exists(tablePath):
        fileSize = os.path.getsize(tablePath)
        strFileSize = str(fileSize)

    print(f"{tableName:^{tableNameWidth}} {tableType:>4} {thisTable.size():>6} {container.getExpectedTableSize(tableName):>6} {strFileSize:>10} {sizeRows:>11} {sizeTable:>11} {deltaGetTableTime:08.4f} {timePerRow_in_ms:07.3f}")

    return (deltaGetTableTime, fileSize, sizeTable)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Benchmark ASDM memory and load times by table.")

    parser.add_argument("asdm_path", type=str, help="The path to the ASDM")

    parser.add_argument("--skip_uniqueness", action="store_true", 
                        help="Skip uniqueness checking (default: False)")

    args = parser.parse_args()

    # Access the values
    print(f"\nASDM Path: {args.asdm_path}")
    print(f"Skip Uniqueness: {args.skip_uniqueness}")

    sdmPath = os.path.expanduser(args.asdm_path)
    if not os.path.exists(sdmPath) or not os.path.isdir(sdmPath):
        print(f"{sdmPath} does not exist or is not a directory")
        sys.exit(1)

    checkRowUniqueness = not args.skip_uniqueness

    try:
        sdm = pyasdm.ASDM(checkRowUniqueness)
        sdm.setFromFile(sdmPath)
        if sdm.getCheckRowUniqueness() != checkRowUniqueness:
            print("Warning: mismatch in checkRowUniqueness in ASDM")
    except ConversionException as e:
        print(f"Conversion Exception seen when setting sdm to path: {sdmPath}. Exception : {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"Unknown exception seen when setting the sdm to path: {sdmPath}. {str(e)}")
        sys.exit(1)

    maxTableNameLen = len(max(sdm.getOnDemandTables(), key=len))

    tableHeader = "Table"
    emptyString = ""
    print(f"{tableHeader:^{maxTableNameLen}} type  nrows exrows  file_size rowobj_size tabobj_size get_time   t/row")
    print(f"{emptyString:^{maxTableNameLen}}                        bytes      bytes       bytes       s        ms")

    onDemandTables = sorted(sdm.getOnDemandTables())

    totalTime = 0.0
    totalSize = 0
    totalObjectSize = 0
    
    for tblName in onDemandTables:
        try:
            thisTableTime, tableSize, tableObjectSize = benchmarkTable(sdm, tblName, maxTableNameLen, checkRowUniqueness)
            totalTime += thisTableTime
            totalSize += tableSize
            totalObjectSize += tableObjectSize
        except Exception as e:
            print(f"Unexpected exception while trying to benchmark {tblName} in {sdmPath}: {str(e)}")
            # just continue until all the table names have been tried

    print("")
    print(f"Total time (s) : {totalTime:10.4f}")
    print(f"Total table file size (bytes)   : {totalSize:>12}")
    print(f"Total table object size (bytes) : {totalObjectSize:>12}")
    print("\n")

    sys.exit(0)
