import unittest

class TestDummy(unittest.TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
    
    def test_fail_on_purpose(self):
        self.assertEqual(1, 2)