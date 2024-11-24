# ALMA - Atacama Large Millimeter Array
# (c) European Southern Observatory, 2024
# (c) Associated Universities Inc., 2024
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
# File Parser.py

from pyasdm.exceptions.ConversionException import ConversionException


class Parser:
    """
    A collection of static methods used by the pyasdm classes in producing and consuming XML.
    This is different from how the strongly typed languages use Parser, but it's similar enough
    that it's been kept in a class of the same name.
    This is not generated code.
    """

    def __init__(self):
        # there are no non-static members, so there should be no need to create a Parser object
        raise RuntimeError("A Parser instance makes no sense")

    @staticmethod
    def nameStringToXML(name, strval):
        """
        A method to produce XML using the name and a string value.
        <name>strval</name>
        The returned value has a trailing space so that it can be used to add
        these strings together without worrying about spacing.
        """
        return "<%s> %s </%s> " % (name, strval, name)

    @staticmethod
    def valueToXML(name, value):
        """
        Return a string of the form '<name> value </name>' to be used in the XML output.
        The value must be convertable to a string using the simple str(value) method.
        A value that is an instance of a class with a toString method should use
        the extendedValuetoXML method.
        """
        return Parser.nameStringToXML(name, str(value))

    @staticmethod
    def extendedValueToXML(name, value):
        """
        Return a string of the form '<name> value </name>' to be used in the XML output.
        The value must have a toString member used to convert that value to a string
        representation. Extended type values all have that function.
        """
        return Parser.nameStringToXML(name, value.toString())

    @staticmethod
    def getListDims(thisList):
        """
        Given a list that may be an ND array of lists where all of the lists
        at each element for the ndim > 1 case has the same shape, this returns
        a list of the shape of the list of lists (and ND array shape)
        """
        result = [len(thisList)]
        if len(thisList) > 0 and isinstance(thisList[0], list):
            subdims = Parser.getListDims(thisList[0])
            result[1:] = subdims
        return result

    @staticmethod
    def checkListType(thisList, atype):
        """
        Returns True if and only if thisList is a list and the type of
        the first non-list value found in thisList is an instance of atype
        or the length of that list is 0.
        """
        result = False
        if isinstance(thisList, list):
            if len(thisList) > 0:
                if isinstance(thisList[0], atype):
                    return True
                if isinstance(thisList[0], list):
                    return Parser.checkListType(thisList[0], atype)
            else:
                # zero length list is True
                return True
        # it's not a list, this means it's not the expected type
        # I think it can't get here recursively, only if called with a non-list argument
        return False

    @staticmethod
    def listXMLPrefix(dims):
        """
        Return a string with the dimensions list encoded as expected for XML storage of the associated list.
        'no_dims dim0 dim1 ... dimn '
        """
        result = "%s " % len(dims)
        for thisDim in dims:
            result += "%s " % thisDim
        return result

    @staticmethod
    def listValuesAsString(theList, dims):
        """
        Turns a list (including a list of lists as used here) into a string for use in an XML output
        Values in the list are turned into a string by use of str(value).
        """
        if len(dims) > 1:
            for kk in range(dims[0]):
                result += Parser.listValuesAsString(theList[kk], dims[1:])
        else:
            # these are actual values
            for jj in range(dims[0]):
                result += str(theList[jj]) + " "
        return result

    @staticmethod
    def listExtendedValuesAsString(theList, dims):
        """
        Turns a list (including a list of lists as used here) into a string for use in an XML output
        Values in the list extended type values and are turned into a string by use of
        the toString method that is part of extended types.
        """
        result = ""
        if len(dims) > 1:
            for kk in range(dims[0]):
                result += Parser.listExtendedValuesAsString(theList[kk], dims[1:])
        else:
            # these are actual values
            for jj in range(dims[0]):
                result += theList[jj].toString() + " "
        return result

    @staticmethod
    def listValueToXML(name, value):
        """
        Return a string of the form '<name> list values </name>' to be used in the XML
        output. The list values are encoded such that they can be read and the list
        (which may be a list of lists, i.e. an ND array of values) be fully reconstructed
        from that XML.
        For use with standard types which can be expressed as a string using str(value).
        Arrays are encoded here as <name> ndim dim1 dim2 dim... dimn value value value ... </name>
        and the most rapidly varying dimension among the values is the last dimension.
        """
        listDims = Parser.getListDims(value)
        result = "<%s> " % name
        result += Parser.listXMLPrefix(listDims)
        result += Parser.listValuesAsString(value, listDims)
        result += "</%s> " % name
        return result

    @staticmethod
    def listExtendedValueToXML(name, value):
        """
        Return a string of the form '<name> list values </name>' to be used in the XML
        output. The list values are encoded such that they can be read and the list
        (which may be a list of lists, i.e. an ND array of values) be fully reconstructed
        from that XML.
        For use with extended types which can be expressed as a string using their toString() member function.
        Arrays are encoded here as <name> ndim dim1 dim2 dim... dimn value value value ... </name>
        and the most rapidly varying dimension among the values is the last dimension.
        """
        listDims = Parser.getListDims(value)
        result = "<%s> " % name
        result += Parser.listXMLPrefix(listDims)
        result += Parser.listExtendedValuesAsString(value, listDims)
        result += "</%s> " % name
        return result

    @staticmethod
    def splitStrToClassLists(splitStr, dims, ListClass):
        result = []
        if len(dims) == 1:
            # this is the result
            # pull the values off of splitStr and return the altered splitStr and the list it made
            for k in range(dims[0]):
                result.append(ListClass(splitStr[k]))
            splitStr = splitStr[dims[0] :]
            return (splitStr, result)
        # else loop through this value and then recursively call this
        for k in range(dims[0]):
            splitStr, thisResult = Parser.splitStrToClassLists(
                splitStr, dims[1:], ListClass
            )
            result.append(thisResult)
        return (splitStr, result)

    @staticmethod
    def stringListToLists(strlist, ListClass, tableName):
        """
        Parse an array expessed in strlist into a list (including lists of list)
        made up of elements of ListClass that can all be constructed
        from a single string in that list.
        The tableName is used when raising ConversionException to indicate the responsible table.
        """
        splitStr = strlist.split()
        # parse the dimensions, which must be integers
        # there must be at least 2 elements
        if len(splitStr) < 2:
            raise ConversionException(
                "invalid strlist, must be at least 2 elements. ListClass is "
                + type(ListClass),
                tableName,
            )
        ndim = int(splitStr[0])
        # now there must be at least (ndim+1) elements
        if len(splitStr) < (ndim + 1):
            raise ConversionException(
                "invalid strlist, not enough elements given first value. ListClass is "
                + type(ListClass),
                tableName,
            )
        dims = []
        count = 1
        for i in range(1, (ndim + 1)):
            dims.append(int(splitStr[i]))
            count *= dims[i - 1]
        if len(splitStr) < (count + 2):
            raise ConversionException(
                "invalid strlist, not enough elements in string, ListClass is "
                + type(ListClass),
                tableName,
            )
        try:
            str, result = Parser.splitStrToClassLists(
                splitStr[(ndim + 1) :], dims, ListClass
            )
        except Exception as exc:
            # raise a ConversionException for anything this unexpected
            raise ConversionException(
                "Unexpected exception "
                + str(exc)
                + ", ListClass is "
                + type(ListClass),
                tableName,
            ) from None

        return result
