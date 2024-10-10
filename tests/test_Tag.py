import unittest
from pyasdm.types.Tag import Tag
from pyasdm.types.TagType import TagType

class tag_test(unittest.TestCase):

    def setUp(self):
        # nothing to do here
        pass

    def tearDown(self):
        # nothing to do here
        pass

    def test_all(self):
        nullTag = Tag()
        self.assertTrue(nullTag.isNull())
        self.assertTrue(nullTag.toString() == "null_0")
        nullTagToo = Tag.parseTag(nullTag.toString())
        self.assertTrue(nullTagToo.isNull())
        self.assertTrue(nullTagToo == nullTag)
        self.assertTrue(nullTag.getTagType() is None)
        self.assertTrue(nullTag.getTagValue() == 0)
        nullTagAlso = Tag.parseTag("")
        self.assertTrue(nullTagAlso.isNull())

        noTypeTag1 = Tag(1)
        self.assertFalse(noTypeTag1.isNull())
        self.assertTrue(noTypeTag1.toString() == "NoType_1")
        noTypeTag2 = Tag(2)
        self.assertTrue(noTypeTag2 > noTypeTag1)
        # and because types are ignored by < and >
        self.assertTrue(nullTag < noTypeTag1)
        noTypeAlso1 = Tag.parseTag(noTypeTag1.toString())
        self.assertTrue(noTypeAlso1 == noTypeTag1)
        self.assertTrue(noTypeTag2.getTagValue() == 2)

        sw4Tag = Tag(24, TagType.SpectralWindow)
        self.assertTrue(sw4Tag.getTagType().toString() == "SpectralWindow")
        ant10Tag = Tag(10, TagType.Antenna)
        self.assertTrue(ant10Tag.getTagType().toString() == "Antenna")
        sw4CopyTag = Tag(sw4Tag)
        self.assertFalse(ant10Tag == sw4Tag)
        self.assertTrue(sw4Tag.equals(sw4CopyTag))
        self.assertTrue(ant10Tag.getTag() == "10")
        self.assertTrue(sw4Tag != ant10Tag)
        dd10Tag = Tag.parseTag("DataDescription_10")
        self.assertTrue(dd10Tag.getTagType().toString() == TagType.DataDescription.toString())
        self.assertTrue(dd10Tag.getTagValue() == 10)

        # throw some exceptions with bad constructors
        ok = False
        try:
            # 3 arguments isn't a thing
            badTag = Tag(1,2,3)
        except ValueError as exc:
            ok = True
        self.assertTrue(ok,"Tag constructor accepted 3 arguments!")

        ok = False
        try:
            # single argument isn't an int or a Tag
            badTag = Tag("1")
        except ValueError as exc:
            ok = True
        self.assertTrue(ok,"Tag constructor accepted a string value as an argument")

        ok = False
        try:
            # 2 arguments, first is not an int
            badTag = Tag(1.0,TagType.DataDescription)
        except ValueError as exc:
            ok = True
        self.assertTrue(ok,"Tag constructor acccepted a float as first of 2 arguments")
        
        ok = False
        try:
            # 2 arguments, second is not a TagType
            badTag = Tag(1.0,"DataDescription")
        except ValueError as exc:
            ok = True
        self.assertTrue(ok,"Tag constructor acccepted a string as second of 2 arguments")

        ok = False
        try:
            # invalid string - missing _
            badTag = Tag.parseString("DataDescription10")
        except:
            ok = True
        self.assertTrue(ok,"parseString parsed an invalid string - DataDescription10")

        ok = False
        try:
            # invalid string - extra _
            badTag = Tag.parseString("Data_Description_10")
        except:
            ok = True
        self.assertTrue(ok,"parseString parsed an invalid string - Data_Description_10")

        ok = False
        try:
            # invalid string - invalid TagType string
            badTag = Tag.parseString("DataDescriptions_10")
        except:
            ok = True
        self.assertTrue(ok,"parseString parsed an invalid string - DataDescriptions_10")

if __name__ == "__main__":
    
    unittest.main()

