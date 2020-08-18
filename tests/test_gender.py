import unittest
import sys
sys.path.append('Jenkins/source/')

import details


class TestStringMethods(unittest.TestCase):
    ''' Test class.'''

    def test_email_invalid1(self):
        self.assertEqual("Invalid Gender", details.get_gender("T"))

    def test_email_valid1(self):
        self.assertEqual("M", details.get_gender("M"))

    def test_email_valid2(self):
        self.assertEqual("Male", details.get_gender("Male"))

if __name__ == '__main__':
    unittest.main()

