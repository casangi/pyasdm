import unittest
from pyasdm.types.Interval import Interval

class interval_test(unittest.TestCase):
    def setUp(self):
        # nothing to do here
        pass

    def tearDown(self):
        # nothing to do here
        pass

    def test_Interval(self):
        # test the Interval basics, everything except the operators
        # constructors

        # empty, value should be 0
        int0 = Interval()
        self.assertEqual(int0.get(), 0)
        self.assertTrue(int0.isZero())

        # from an integer
        int10 = Interval(10)
        self.assertEqual(int10.get(),10)
        self.assertFalse(int10.isZero())
        self.assertFalse(int10.equals(int0))

        # from another Interval
        intcopy = Interval(int10)
        self.assertTrue(int10.equals(intcopy))

        # from a string
        intstr = Interval("12345")
        self.assertEqual(intstr.get(),12345)
        intstrcopy10 = Interval(int10.string())
        self.assertEqual(intstrcopy10.get(),int10.get())

        # invalid constructor values - should throw exceptions
        ok = False
        try:
            badint = Interval(0.0)
        except ValueError as exc:
            ok = True
        self.assertTrue(ok,"Interval with float did not raise a ValueError as expected")
        try:
            badint = Interval("not ok")
        except ValueError as exc:
            ok = True
        self.assertTrue(ok,"Interval with non-int string value did not raise a ValueEror as expected")

        self.assertEqual(int0.unit(),"nanosec")

        intstrcopy = intstr.copy()
        self.assertEqual(intstrcopy,intstr)
        intstrcopy.fromString("54321")
        self.assertNotEqual(intstrcopy, intstr)

    def test_Interval_operators(self):
        tint = Interval()
        tint += 10
        self.assertEqual(tint.get(),10)

        tint2 = Interval(tint)
        tint2 *= tint
        self.assertEqual(tint2.get(),100)

        tint2 -= 50
        self.assertEqual(tint2.get(),50)

        # this works, but it forces it to be an integer so it loses precision
        tint2 /= 3
        self.assertEqual(tint2.get(),16)
        tint2 *= 3
        self.assertEqual(tint2.get(),48)

        tint3 = tint + tint2
        self.assertEqual(tint3.get(),58)
        tint4 = tint3 + 10
        self.assertEqual(tint4.get(),68)
        # tint3 is unchanged
        self.assertEqual(tint3.get(),58)

        tint4 = tint4 * tint3
        self.assertEqual(tint4,3944)
        tint4 = tint4 - tint3
        self.assertEqual(tint4,3886)
        tint5 = tint4 / tint3
        self.assertEqual(tint5.get(),67)
        # this turns out to be accurate as integers
        self.assertEqual((tint5*tint3).get(), 3886)

        self.assertTrue(tint5 < tint4)
        self.assertFalse(tint5 > tint4)
        tintcopy = tint5.copy()
        self.assertTrue(tintcopy == tint5)
        self.assertTrue(tintcopy >= tint5)
        self.assertTrue(tintcopy <= tint5)
        self.assertFalse(tintcopy != tint5)

        tint5val = tint5.get()
        negtint = -tint5
        self.assertEqual(tint5.get(),tint5val)
        self.assertTrue(negtint.get()==-tint5.get())

        # the __pos__ operator is equivalent to the copy constructor
        postint = +tint5
        self.assertEqual(postint,tint5)

if __name__ == "__main__":

    unittest.main()
