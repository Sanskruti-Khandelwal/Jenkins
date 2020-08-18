import unittest
import sys
sys.path.append('../source/')

import details


class TestStringMethods(unittest.TestCase):
    ''' Test class.'''

    def test_email_invalid1(self):
        self.assertEqual("Invalid Phone Number", details.get_phone_number("1234"))

    def test_email_invalid2(self):
        self.assertEqual("Invalid Phone Number", details.get_phone_number("S123JJ"))

    def test_email_valid1(self):
        self.assertEqual("7000350561", details.get_phone_number("7000350561"))

if __name__ == '__main__':
    unittest.main()

