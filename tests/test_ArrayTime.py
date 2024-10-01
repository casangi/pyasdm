import unittest
import time
from pyasdm.types.ArrayTime import ArrayTime

class arraytime_test(unittest.TestCase):

    def setUp(self):
        # create an ArrayTime using the current time
        gmnow = time.gmtime()
        self.atnow = ArrayTime(gmnow.tm_year, gmnow.tm_mon, gmnow.tm_mday, gmnow.tm_hour, gmnow.tm_min, gmnow.tm_sec)

    def tearDown(self):
        # nothing to do here, placeholder in case that changes
        pass

    def test_now(self):
        # this just prints out the values from atnow, matches c++ test program behavior, this should never fail
        print("\nToday in FITS format : " + self.atnow.toFITS())
        print("Today in nanoseconds : " + str(self.atnow.get()))

    def test_known_results(self):
        # create an ArrayTime using a known date with known results
        # verified first using the c++ ArrayTime class
        fitsdate = "2024-09-16T14:30:21.35235"
        at = ArrayTime(fitsdate)
        self.assertEqual(at.toFITS(),fitsdate+"0000","toFITS")
        self.assertAlmostEqual(at.getJD(),2460570.10441380041,18,"getJD")
        self.assertAlmostEqual(at.getMJD(),60569.6044138003417,18,"getMJD")
        self.assertAlmostEqual(at.getTimeOfDay(),14.5059312097728252,"getTimeOfDay")
        self.assertEqual(at.getDayOfWeek(),1,"getDayOfWeek")
        self.assertEqual(at.getDayOfYear(),260,"getDayOfYear")
        self.assertEqual(at.timeOfDayToString(),"14:30:21","timeOfDayToString")
        self.assertAlmostEqual(at.getLocalSiderealTime(-5.0),19.2413337437319569,18,"getLocalSiderealTime");
        self.assertAlmostEqual(at.getGreenwichMeanSiderealTime(),14.2413337437319569,18,"getGreenwichMeanSiderealTime");
        expectedDateTime = (2024,9,16,14,30,21,352350000)
        self.assertEqual(at.getDateTime(),expectedDateTime,"getDateTime")

    def test_constructors(self):
        fitsdate = "2024-09-16T14:30:21.35235"
        at = ArrayTime(fitsdate)
        atCheck = ArrayTime(2024,9,16,14,30,21.35235)
        self.assertEqual(at, atCheck,"ArrayTime via FITS vs y,m,d,h,m,s")

        # these tests use self.atnow to avoid bias in the tests by using a new value each time

        # copy constructor
        at = ArrayTime(self.atnow)
        self.assertEqual(at, self.atnow, "copy constructor")

        # from the string representation of an MJD
        at = ArrayTime(str(self.atnow.getMJD()));
        # the conversion to a double and then a string looses some precision
        self.assertTrue((abs(at.get()-self.atnow.get())<1000), "ArrayTime from a string MJD")

        # from the string representation of the ArrayTime value as an integer (ns)
        at = ArrayTime(str(self.atnow.get()))
        self.assertEqual(at, self.atnow, "ArrayTime from an string integer (ns)")

        # from the DateTime integer values, y, mon, day, h, m, float(sec)
        vDateTime = self.atnow.getDateTime()
        fsec = vDateTime[5] + vDateTime[6]/1000000000.0
        at = ArrayTime(vDateTime[0],vDateTime[1],vDateTime[2],vDateTime[3],vDateTime[4], fsec)
        self.assertEqual(at, self.atnow,"ArrayTime from y,mon,day,hr,min,float(sec)")

        # from the DateTime integer values, y, mon, float(day)
        fday = vDateTime[2] + (vDateTime[3] + (vDateTime[4] + (vDateTime[5] + vDateTime[6]/1000000000.0)/60.0)/60.0)/24.0
        at = ArrayTime(vDateTime[0],vDateTime[1],fday)
        self.assertEqual(at, self.atnow, "ArrayTime from y,mon, float(day)")

        # from the MJD directly
        at = ArrayTime(self.atnow.getMJD())
        self.assertTrue((abs(at.get()-self.atnow.get())<1000),"ArrayTime from MJD (float)")

        # a non-leap year, to check day of year and initialization
        at = ArrayTime(1983,7,14,22,2,5.7528)
        self.assertEqual(at.toFITS(), "1983-07-14T22:02:05.752800000","non leap year test, toFITS")
        self.assertEqual(at.getDayOfYear(),195,"non leap year test, getDayOfYear")

if __name__ == "__main__":

    unittest.main()
