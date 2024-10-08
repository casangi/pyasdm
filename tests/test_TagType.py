import unittest
from pyasdm.types.TagType import TagType

class tagtype_test(unittest.TestCase):

    def setUp(self):
        # nothing to do here
        pass

    def tearDown(self):
        # nothing to do here
        pass

    def test_all(self):
        # a simple class to test

        # check that a few of the expected attributes are there, the code generation takes care of including all of them
        notype = TagType.NoType
        self.assertTrue(isinstance(notype,TagType))
        self.assertEqual(notype.toString(),"NoType")
        obstype = TagType.Observation
        self.assertTrue(isinstance(obstype,TagType))
        self.assertEqual(obstype.toString(),"Observation")

        # get obstype by name
        obstype2 = TagType.getTagType("Observation")
        self.assertEqual(obstype.toString(),obstype2.toString())

        # an unknown name returns None
        unknown = TagType.getTagType("whatever")
        self.assertTrue(unknown is None)

        # and doing that by the constructor makes a TagType of that name, that's now an attribute of TagTyp
        whateverType = TagType("whatever")
        self.assertTrue(isinstance(whateverType,TagType))
        self.assertEqual(whateverType.toString(),"whatever")
        self.assertEqual(TagType.whatever.toString(),whateverType.toString())

        # and any other type in the constuctor is a ValueError
        ok = False
        try:
            badType = TagType(False)
        except ValueError as exc:
            ok = True
        self.assertTrue(ok,"TagType constructor with a boolean did not raise a ValueError as expected")

if __name__ == "__main__":
    
    unittest.main()
