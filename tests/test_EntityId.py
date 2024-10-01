import unittest
from pyasdm.types.EntityId import EntityId

class entityid_test(unittest.TestCase):
    def setUp(self):
        # nothing to do here
        pass

    def tearDown(self):
        # nothing to do here
        pass

    def test_EntityId(self):
        # tests of the EntityId class

        # default constructor - null ID
        id = EntityId()
        self.assertTrue(id.isNull())

        # valid ALMA UID
        almaId = EntityId("uid://A002/X2a5c2f/X66")
        self.assertTrue(not almaId.isNull())
        self.assertEqual(almaId.toString(),"uid://A002/X2a5c2f/X66")

        # valid EVLA UID example 1
        evlaId1 = EntityId("uid:///evla/bdf/1329949996080")
        self.assertTrue(not evlaId1.isNull())
        self.assertEqual(evlaId1.toString(),"uid:///evla/bdf/1329949996080")

        # valid EVLA UID example 2
        evlaId2 = EntityId("uid://evla/sdm/X1329949850138")
        self.assertTrue(not evlaId2.isNull())
        self.assertEqual(evlaId2.toString(),"uid://evla/sdm/X1329949850138")

        # copy constructor
        almaIdCopy = EntityId(almaId)
        self.assertTrue(almaId.equals(almaIdCopy))
        self.assertTrue(not almaIdCopy.equals(evlaId2))

        # test exceptions are raised

        ok = False
        try:
            # invalid string value
            id = EntityId("not valid")
        except ValueError as exc:
            ok = True

        self.assertTrue(ok,"EntityId with invalid string did not raise a ValueError as expected")
        
        ok = False
        try:
            # invalid type
            id = EntityId(1)
        except ValueError as exc:
            ok = True

        self.assertTrue(ok,"EntityId with invalid type did not raise a ValueError as expected")

        ok = False
        try:
            # too many arguments, the first is a valid value
            id = EntityId("uid://evla/sdm/X1329949850138",2)
        except ValueError as exc:
            ok = True

        self.assertTrue(ok,"EntityId with too many arguments did not raise a ValueError as expected")

        

if __name__ == "__main__":

    unittest.main()
