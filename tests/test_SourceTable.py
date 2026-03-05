
import unittest
import pyasdm

class source_table_test(unittest.TestCase):

    def setUp(self):
        # nothing to do here
        pass

    def tearDown(self):
        # nothing to do here
        pass

    def test_table_row(self):
        # a simple test to add a row to an empty SourceTable directly from XML
        # nothing is written to disk
        
        test_asdm = pyasdm.ASDM()
        source_row_0_xml = """
        <row>
        <sourceId> 0 </sourceId>
        <timeInterval> 7090683272335387903 4265377529038775807 </timeInterval>
        <code> none </code>
        <direction> 1 2 1.3528024488371877 0.31436086058385826  </direction>
        <properMotion> 1 2 0.0 0.0  </properMotion>
        <sourceName> J0510+1800 </sourceName>
        <directionCode>ICRS</directionCode>
        <numFreq> 4 </numFreq>
        <numStokes> 4 </numStokes>
        <frequency> 1 4 2.1998305541101968E11 2.1800401136221878E11 2.3300428785048865E11 2.350043230298097E11  </frequency>
        <stokesParameter> 1 4 I Q U V</stokesParameter>
        <flux> 2 4 4 3.855274498565509 0.0 0.0 0.0 3.8656094704537534 0.0 0.0 0.0 3.7901533014049034 0.0 0.0 0.0 3.7805688135422617 0.0 0.0 0.0  </flux>
        <size> 2 4 2 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0  </size>
        <spectralWindowId> SpectralWindow_0 </spectralWindowId>
        </row>
        """

        source_table = test_asdm.getSource()
        source_row_0 = pyasdm.SourceRow(source_table)
        source_row_0.setFromXML(source_row_0_xml)
        source_table.add(source_row_0)
        print(source_table)

if __name__ == "__main__":

    unittest.main()
