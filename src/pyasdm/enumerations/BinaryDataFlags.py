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
# /////////////////////////////////////////////////////////////////
# // WARNING!  DO NOT MODIFY THIS FILE!                          //
# //  ---------------------------------------------------------  //
# // | This is generated code!  Do not modify this file.       | //
# // | Any changes will be lost when the file is re-generated. | //
# //  ---------------------------------------------------------  //
# /////////////////////////////////////////////////////////////////
#
# File BinaryDataFlags.py

# to keep track of the attributes added to this class for each value of this enumeration

_binaryDataFlagsDict = {}

# the possible enumerations

_INTEGRATION_FULLY_BLANKED = 0  # All dumps within an integration duration are blanked. When this flag is raised the effect is to have the bin part actualDurations containing zeros? In other words it means 'all dumps affected'.  Bit position \f$==0\f$

_WVR_APC = 1  # Coefficients not received.Apply to all BAL involving the antenna. Bit position \f$==1\f$

_CORRELATOR_MISSING_STATUS = 2  # Correlator status was not retrieved for the period. So  yielded data are not reliable. Apply to all  BBs handled by the correlator. Bit position \f$==2\f$

_MISSING_ANTENNA_EVENT = 3  # Antenna delay event was not retrieved for the period. So  yielded data are not reliable. BALs including the antenna. Bit position \f$==3\f$

_DELTA_SIGMA_OVERFLOW = 4  # In data transmission between the MTI cards, there are one or more channels whose absolute value differences between adjacent channel values are bigger than the maximum number. Bit position \f$==4\f$

_DELAY_CORRECTION_NOT_APPLIED = 5  # no residual delay correction was applied. It implies that either base-band offset delays from TMCDB were not available or that delay events from the delay server were not received on time to compute and apply a phase rotation to base-lines in the array. \f$==5\f$

_SYNCRONIZATION_ERROR = 6  # cdp node(s) not properly synchronized to the array timing signal (48ms.) All data produced by that node(s) are suspicious.Lags and spectral processing goes as normal, it is just the flag presence in the bdf what indicates that something is suspicious. Bit position \f$==6\f$

_FFT_OVERFLOW = 7  # Overflowed POL and derived outputs from it. Dumps between the timestamp marked as FFT overflowed and the time back to 96msec before. Bit position \f$==7\f$

_TFB_SCALING_FACTOR_NOT_RETRIEVED = 8  # CCC cannot retrieve scaling factors during calibration for specific antennas the calibration would still end successfully but the cdp will record the faulty scaling factors and add a flag to all involved base-lines. Bit position \f$==8\f$

_ZERO_LAG_NOT_RECEIVED = 9  # CDP node handling only cross antenna intersections did  not receive lag zero information from node(s) handling auto intersections for involved antennas in that cross intersection. Bit position \f$==9\f$

_SIGMA_OVERFLOW = 10  # Auto-correlation sigma levels makes impossible any 2 bits quantization correction on lags data. One sigma value out of range affects that antenna itself and all base-lines containing that antenna. Is it possible to merge this flags with DELTA_SIGMA_OVERFLOW? The difference seems to be the granularity. If it is POL ACACORR would have to repeat the flag for every POL  because per baseband there are several POL. Bit position \f$==10\f$

_UNUSABLE_CAI_OUTPUT = 11  # The output spectra are made from invalid input signals, e.g., broken optical frames, missing synchronization or no input signal power. Bit position \f$==11\f$

_QC_FAILED = 12  # Quantization correction not applied due to unsuitable lag zero value. BL-CORR note: every possible signal level should be actually accepted (too small or too big), the presence of this bit signals more a software problem than an antenna signal problem. Bit position \f$==12\f$

_NOISY_TDM_CHANNELS = 13  # First TDM channels are normally noisy and they have a  large amplitude. If that excess of amplitude in those channels would be the sole reason for keeping the integration storage at 32 bits integers then the software clips those channels and flags the data. Thus preventing large storage for otherwise 16 bits friendly dynamic range. Bit position \f$==13\f$

_SPECTRAL_NORMALIZATION_FAILED = 14  # Auto-correlation and zero-lags figures are required to normalize cross-correlation spectra as prescribed in Scott's 'Specifications and Clarifications of ALMA Correlator Details'. If those figures are not available on time during on-line processing then crosscorrelations are not normalized and the integration flagged. Bit position \f$==14\f$

_DROPPED_PACKETS = 15  # T.B.D. Bit position \f$==15\f$

_DETECTOR_SATURATED = 16  # T.B.D. Bit position \f$==16\f$

_NO_DATA_FROM_DIGITAL_POWER_METER = 17  # The current data from digital power meter are available for the calculation of the 3-bit linearity correction. An old correction factor is applied. Bit position \f$==17\f$

_RESERVED_18 = 18  # Not assigned.

_RESERVED_19 = 19  # Not assigned.

_RESERVED_20 = 20  # Not assigned.

_RESERVED_21 = 21  # Not assigned.

_RESERVED_22 = 22  # Not assigned.

_RESERVED_23 = 23  # Not assigned.

_RESERVED_24 = 24  # Not assigned.

_RESERVED_25 = 25  # Not assigned.

_RESERVED_26 = 26  # Not assigned.

_RESERVED_27 = 27  # Not assigned.

_RESERVED_28 = 28  # Not assigned.

_RESERVED_29 = 29  # Not assigned.

_RESERVED_30 = 30  # Not assigned.

_ALL_PURPOSE_ERROR = 31  # This bit designates data flagged in the correlator but does not provide information as to the reason for the flag. Readers are expected not to process the data when this bit is set. Bit position \f$ ==31 \f$.


# their names in a dictionary
_binaryDataFlagsNames = {}

_binaryDataFlagsNames[_INTEGRATION_FULLY_BLANKED] = "INTEGRATION_FULLY_BLANKED"

_binaryDataFlagsNames[_WVR_APC] = "WVR_APC"

_binaryDataFlagsNames[_CORRELATOR_MISSING_STATUS] = "CORRELATOR_MISSING_STATUS"

_binaryDataFlagsNames[_MISSING_ANTENNA_EVENT] = "MISSING_ANTENNA_EVENT"

_binaryDataFlagsNames[_DELTA_SIGMA_OVERFLOW] = "DELTA_SIGMA_OVERFLOW"

_binaryDataFlagsNames[_DELAY_CORRECTION_NOT_APPLIED] = "DELAY_CORRECTION_NOT_APPLIED"

_binaryDataFlagsNames[_SYNCRONIZATION_ERROR] = "SYNCRONIZATION_ERROR"

_binaryDataFlagsNames[_FFT_OVERFLOW] = "FFT_OVERFLOW"

_binaryDataFlagsNames[_TFB_SCALING_FACTOR_NOT_RETRIEVED] = (
    "TFB_SCALING_FACTOR_NOT_RETRIEVED"
)

_binaryDataFlagsNames[_ZERO_LAG_NOT_RECEIVED] = "ZERO_LAG_NOT_RECEIVED"

_binaryDataFlagsNames[_SIGMA_OVERFLOW] = "SIGMA_OVERFLOW"

_binaryDataFlagsNames[_UNUSABLE_CAI_OUTPUT] = "UNUSABLE_CAI_OUTPUT"

_binaryDataFlagsNames[_QC_FAILED] = "QC_FAILED"

_binaryDataFlagsNames[_NOISY_TDM_CHANNELS] = "NOISY_TDM_CHANNELS"

_binaryDataFlagsNames[_SPECTRAL_NORMALIZATION_FAILED] = "SPECTRAL_NORMALIZATION_FAILED"

_binaryDataFlagsNames[_DROPPED_PACKETS] = "DROPPED_PACKETS"

_binaryDataFlagsNames[_DETECTOR_SATURATED] = "DETECTOR_SATURATED"

_binaryDataFlagsNames[_NO_DATA_FROM_DIGITAL_POWER_METER] = (
    "NO_DATA_FROM_DIGITAL_POWER_METER"
)

_binaryDataFlagsNames[_RESERVED_18] = "RESERVED_18"

_binaryDataFlagsNames[_RESERVED_19] = "RESERVED_19"

_binaryDataFlagsNames[_RESERVED_20] = "RESERVED_20"

_binaryDataFlagsNames[_RESERVED_21] = "RESERVED_21"

_binaryDataFlagsNames[_RESERVED_22] = "RESERVED_22"

_binaryDataFlagsNames[_RESERVED_23] = "RESERVED_23"

_binaryDataFlagsNames[_RESERVED_24] = "RESERVED_24"

_binaryDataFlagsNames[_RESERVED_25] = "RESERVED_25"

_binaryDataFlagsNames[_RESERVED_26] = "RESERVED_26"

_binaryDataFlagsNames[_RESERVED_27] = "RESERVED_27"

_binaryDataFlagsNames[_RESERVED_28] = "RESERVED_28"

_binaryDataFlagsNames[_RESERVED_29] = "RESERVED_29"

_binaryDataFlagsNames[_RESERVED_30] = "RESERVED_30"

_binaryDataFlagsNames[_ALL_PURPOSE_ERROR] = "ALL_PURPOSE_ERROR"


class BinaryDataFlags:
    """
    A class for the BinaryDataFlags enumeration.
    """

    # The value of this BinaryDataFlags, one of the possible enumerations.
    _value = None

    # its name
    _name = None

    def __init__(self, binaryDataFlags):
        # construct a BinaryDataFlags from an integer, a string, or another BinaryDataFlags
        # if binaryDataFlags is a string, convert it to an instance of this class using literal
        if isinstance(binaryDataFlags, BinaryDataFlags):
            # copy constructor
            self._value = binaryDataFlags.getValue()
            self._name = binaryDataFlags.getName()
        elif isinstance(binaryDataFlags, str):
            # convert it to an instance of this class using literal
            thisEnum = BinaryDataFlags.literal(binaryDataFlags)
            self._value = thisEnum.getValue()
            self._name = thisEnum.getName()
        else:
            # it must be in the names dictionary
            if binaryDataFlags not in _binaryDataFlagsNames:
                raise ValueError("unrecognized BinaryDataFlags")
            self._value = binaryDataFlags
            self._name = _binaryDataFlagsNames[binaryDataFlags]
            if self._name not in _binaryDataFlagsDict:
                # add this BinaryDataFlags as an attribute to this class using its name
                setattr(BinaryDataFlags, self._name, self)
                _binaryDataFlagsDict[self._name] = getattr(BinaryDataFlags, self._name)

    def getValue(self):
        """
        Return the integer value of this enumeration.
        """
        return self._value

    def getName(self):
        """
        Return the name of this enumeration.
        """
        return self._name

    def __str__(self):
        """
        Equivalent to getName()
        """
        return self.getName()

    def __eq__(self, other):
        """
        Returns True if other is a BinaryDataFlags and its value is the same as this one.
        """
        return isinstance(other, BinaryDataFlags) and (
            other.getValue() == self.getValue()
        )

    def __ne__(self, other):
        """
        Returns True if other is not equal to self
        """
        return not (self == other)

    # by convention with the code in java and c++, these are all static methods
    @staticmethod
    def revision():
        """
        revision as a string.
        """
        return "-1"

    @staticmethod
    def version():
        """
        the major version number as an int.
        """
        return 1

    @staticmethod
    def size():
        """
        the number of known enumerators in BinaryDataFlags
        """
        return len(_binaryDataFlagsNames)

    @staticmethod
    def name(binaryDataFlags):
        """
        Returns the string form of binaryDataFlags
        """
        return str(binaryDataFlags)

    @staticmethod
    def names():
        """
        Return the list of all known BinaryDataFlags enumeration names
        """
        return list(_binaryDataFlagsNames.values())

    @staticmethod
    def newBinaryDataFlags(name):
        """
        Equivalent to the literal method
        """
        return BinaryDataFlags.literal(name)

    @staticmethod
    def literal(name):
        """
        Return the BinaryDataFlags enumerator value given a string
        """
        # it must be available as an attribute
        if not hasattr(BinaryDataFlags, name):
            raise ValueError("Unrecognized BinaryDataFlags name")
        return BinaryDataFlags(getattr(BinaryDataFlags, name).getValue())

    @staticmethod
    def from_int(i):
        """
        Return a BinaryDataFlags from an integration matching an enumeration.
        """
        return BinaryDataFlags(i)


INTEGRATION_FULLY_BLANKED = BinaryDataFlags(_INTEGRATION_FULLY_BLANKED)

WVR_APC = BinaryDataFlags(_WVR_APC)

CORRELATOR_MISSING_STATUS = BinaryDataFlags(_CORRELATOR_MISSING_STATUS)

MISSING_ANTENNA_EVENT = BinaryDataFlags(_MISSING_ANTENNA_EVENT)

DELTA_SIGMA_OVERFLOW = BinaryDataFlags(_DELTA_SIGMA_OVERFLOW)

DELAY_CORRECTION_NOT_APPLIED = BinaryDataFlags(_DELAY_CORRECTION_NOT_APPLIED)

SYNCRONIZATION_ERROR = BinaryDataFlags(_SYNCRONIZATION_ERROR)

FFT_OVERFLOW = BinaryDataFlags(_FFT_OVERFLOW)

TFB_SCALING_FACTOR_NOT_RETRIEVED = BinaryDataFlags(_TFB_SCALING_FACTOR_NOT_RETRIEVED)

ZERO_LAG_NOT_RECEIVED = BinaryDataFlags(_ZERO_LAG_NOT_RECEIVED)

SIGMA_OVERFLOW = BinaryDataFlags(_SIGMA_OVERFLOW)

UNUSABLE_CAI_OUTPUT = BinaryDataFlags(_UNUSABLE_CAI_OUTPUT)

QC_FAILED = BinaryDataFlags(_QC_FAILED)

NOISY_TDM_CHANNELS = BinaryDataFlags(_NOISY_TDM_CHANNELS)

SPECTRAL_NORMALIZATION_FAILED = BinaryDataFlags(_SPECTRAL_NORMALIZATION_FAILED)

DROPPED_PACKETS = BinaryDataFlags(_DROPPED_PACKETS)

DETECTOR_SATURATED = BinaryDataFlags(_DETECTOR_SATURATED)

NO_DATA_FROM_DIGITAL_POWER_METER = BinaryDataFlags(_NO_DATA_FROM_DIGITAL_POWER_METER)

RESERVED_18 = BinaryDataFlags(_RESERVED_18)

RESERVED_19 = BinaryDataFlags(_RESERVED_19)

RESERVED_20 = BinaryDataFlags(_RESERVED_20)

RESERVED_21 = BinaryDataFlags(_RESERVED_21)

RESERVED_22 = BinaryDataFlags(_RESERVED_22)

RESERVED_23 = BinaryDataFlags(_RESERVED_23)

RESERVED_24 = BinaryDataFlags(_RESERVED_24)

RESERVED_25 = BinaryDataFlags(_RESERVED_25)

RESERVED_26 = BinaryDataFlags(_RESERVED_26)

RESERVED_27 = BinaryDataFlags(_RESERVED_27)

RESERVED_28 = BinaryDataFlags(_RESERVED_28)

RESERVED_29 = BinaryDataFlags(_RESERVED_29)

RESERVED_30 = BinaryDataFlags(_RESERVED_30)

ALL_PURPOSE_ERROR = BinaryDataFlags(_ALL_PURPOSE_ERROR)
