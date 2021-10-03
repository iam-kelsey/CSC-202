#Kelsey Nguyen
#CPE 202 Section 7
#Project 1

from bears import *
import unittest


class TestCase(unittest.TestCase):
    def test_bear_1(self):
        self.assertTrue(bears(250))
    def test_bear_2(self):
        self.assertTrue(bears(42))
    def test_bear_3(self):
        self.assertFalse(bears(53))
    def test_bear_4(self):
        self.assertFalse(bears(41))
    def test_bear_5(self):
        self.assertFalse(bears(1249))
    def test_bear_6(self):
        self.assertTrue(bears(1260))
    def test_bear_7(self):
        self.assertTrue(bears(420))
    def test_bear_8(self):
        self.assertFalse(bears(95))
    def test_bear_9(self):
        self.assertFalse(bears(53))       
    def test_bear10(self):
        self.assertFalse(bears(10))








    

        
 
     
        
# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()
