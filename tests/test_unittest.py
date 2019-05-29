import TraceManager as Instance # The code to test
import unittest                 # The test framework

class Test_TestEqual(unittest.TestCase):
    def test_Name(self):
        self.assertEqual(Instance.Name, "TraceManager")

    def test_Version(self):
        self.assertEqual(Instance.Version, "0.0.1")

if __name__ == '__main__':
    unittest.main()
