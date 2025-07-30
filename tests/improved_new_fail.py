import unittest

class TestDummy(unittest.TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertEqual(1, 2)
if __name__ == '__main__':
    unittest.main()
    
    
        
        #hello#