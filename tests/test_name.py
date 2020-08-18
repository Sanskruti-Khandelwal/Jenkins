import unittest
import sys
sys.path.append('../source/')

import details


class TestStringMethods(unittest.TestCase):
    ''' Test class.'''

    def test_name_invalid(self):
        self.assertEqual("Invalid Name", details.get_name("Sans1234"))

    def test_name_valid(self):
        self.assertEqual("Sanskruti", details.get_name("Sanskruti"))

if __name__ == '__main__':
    unittest.main()

