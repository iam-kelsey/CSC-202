#Kelsey Nguyen
#CPE 202 Section 7
#Project 1

from base_convert import *
import unittest


class TestCase(unittest.TestCase):
    def test_base_convert1(self):
        self.assertEqual(convert(30,4), "132")
    def test_base_convert2(self):
        self.assertEqual(convert(45, 2), "101101")
    def test_base_convert3(self):
        self.assertEqual(convert(316, 16), "13C")
    def test_base_convert4(self):
        self.assertEqual(convert(11,9), "12")
    def test_base_convert5(self):
        self.assertEqual(convert(0,20), "0")
    def test_base_convert6(self):
        self.assertEqual(convert(14, 10), "14")
    def test_base_convert7(self):
        self.assertEqual(convert(1453, 16), "5AD")
    def test_base_convert8(self):
        self.assertEqual(convert(10, 2), "1010")
    def test_base_convert9(self):
        self.assertEqual(convert(42, 16), "2A")
    def test_base_convert10(self):
        self.assertEqual(convert(100, 8), "144")



    

        
 
     
        
# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()
