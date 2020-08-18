import unittest
import sys
sys.path.append('../source/')

import details


class TestStringMethods(unittest.TestCase):
    ''' Test class.'''

    def test_email_invalid(self):
        self.assertEqual("Invalid Email", details.get_email("gmail.com1234"))

    def test_email_valid1(self):
        self.assertEqual("sk@q.com", details.get_email("sk@q.com"))

    def test_email_valid1(self):
        self.assertEqual("sanskruti.khandelwal@quantiphi.com", details.get_email("sanskruti.khandelwal@quantiphi.com"))

if __name__ == '__main__':
    unittest.main()

