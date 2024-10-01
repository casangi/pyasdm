import unittest
from pyasdm.types.Entity import Entity
from pyasdm.types.EntityId import EntityId

class entity_test(unittest.TestCase):
    def setUp(self):
        # an example ALMA Entity XML string
        self.ALMAEntityStr = '<Entity entityId="uid://A002/X72c1bd/X1" entityIdEncrypted="na" entityTypeName="AntennaTable" schemaVersion="1" documentVersion="1"/>'
        # an example eVLA Entity XML string
        self.eVLAEntityStr = '<Entity documentVersion="1" schemaVersion="3" entityTypeName="CalDataTable" entityIdEncrypted="na" entityId="uid://evla/sdm/X1465236651395"/>'
    def tearDown(self):
        # nothing to do here
        pass

    def test_Entity(self):
        # constructors
        eNull = Entity()
        self.assertTrue(eNull.isNull())
        # this should produce an exception
        ok = False
        try:
            s = eNull.toString()
        except Exception as exp:
            ok = True
        self.assertTrue(ok)

        # copy constructor
        eCopy = Entity(eNull)
        self.assertTrue(eCopy.isNull())
        self.assertTrue(eCopy.equals(eNull))

        # XML string
        eALMA = Entity(self.ALMAEntityStr)
        eVLA = Entity(self.eVLAEntityStr)
        self.assertTrue(not eVLA.equals(eALMA))

        eALMA2 = Entity(eALMA.getEntityId(),eALMA.getEntityIdEncrypted(),eALMA.getEntityTypeName(),eALMA.getEntityVersion(),eALMA.getInstanceVersion())
        eALMA3 = Entity(eALMA.toXML())
        self.assertTrue(eALMA2.equals(eALMA))
        self.assertTrue(eALMA3.equals(eALMA))

        eVLA2 = Entity(eVLA.toString())
        self.assertTrue(eVLA2.equals(eVLA))

        # getters and setters
        self.assertEqual(eALMA.getEntityId().toString(),"uid://A002/X72c1bd/X1")
        self.assertEqual(eALMA.getEntityIdEncrypted(),"na")
        self.assertEqual(eALMA.getEntityTypeName(),"AntennaTable")
        self.assertEqual(eALMA.getEntityVersion(),"1")
        self.assertEqual(eALMA.getInstanceVersion(),"1")
        
        eVLA2.setInstanceVersion("5")
        self.assertEqual(eVLA2.getInstanceVersion(),"5")
        self.assertTrue(not eVLA2.equals(eVLA))

        eVLA2.setEntityId("uid://evla/sdm/X1465236651400")
        self.assertTrue(eVLA2.getEntityId().equals(EntityId("uid://evla/sdm/X1465236651400")))

        eVLA2.setEntityIdEncrypted("set")
        self.assertEqual(eVLA2.getEntityIdEncrypted(),"set")

        eALMA2 = Entity(eALMA)
        eALMA2.setEntityVersion("4")
        self.assertEqual(eALMA2.getEntityVersion(),"4")
        self.assertTrue(not eALMA2.equals(eALMA))

        # expected exceptions
        # wrong number of arguments
        ok = False
        try:
            e = Entity(0,1,2)
        except Exception as exc:
            ok = True
        self.assertTrue(ok)

        # wrong type for a single argument
        ok = False
        try:
            e = Entity(0)
        except Exception as exc:
            ok = True
        self.assertTrue(ok)

        # wrong type for the last of the 5 arguments
        ok = False
        try:
            e = Entity(eALMA.getEntityId(),eALMA.getEntityIdEncrypted(),eALMA.getEntityTypeName(),eALMA.getEntityVersion(),1)
        except Exception as exc:
            ok = True
        self.assertTrue(ok)

        # non-entity XML
        ok = False
        try:
            xmlStr = "<TimeOfCreation>2016-06-06T18:10:51.000395</TimeOfCreation>"
            e = Entity(xmlStr)
        except Exception as exc:
            ok = True
        self.assertTrue(ok)

        # setting the EntityId with an invalid string
        ok = False
        try:
            e = Entity()
            e.setEntityId("not valid")
        except Exception as exc:
            ok = True
        self.assertTrue(ok)
            
if __name__ == "__main__":

    unittest.main()
