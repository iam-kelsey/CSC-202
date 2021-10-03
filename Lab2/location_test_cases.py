# CPE 202 Lab 2
# Kelsey Nguyen
# Section 07

import unittest
from location import *

#Test Cases for location

class TestLab1(unittest.TestCase):

    def test_repr1(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")  
    def test_repr2(self):
        loc = Location("Las Vegas", 36.1, -115.2)
        self.assertEqual(repr(loc),"Location('Las Vegas', 36.1, -115.2)")      
    def test_repr3(self):
        loc = Location("Huntington Beach", 33.7, -118.0)
        self.assertEqual(repr(loc),"Location('Huntington Beach', 33.7, -118.0)")   
    def test_repr4(self):
        loc = Location("Los Angeles", 34.1, -118.2)
        self.assertEqual(repr(loc),"Location('Los Angeles', 34.1, -118.2)")      
    def test_repr5(self):
        loc = Location("Irvine", 33.7, -117.8)
        self.assertEqual(repr(loc),"Location('Irvine', 33.7, -117.8)")   
    def test_repr6(self):
        loc = Location("New York", 40.7, -74.0)
        self.assertEqual(repr(loc),"Location('New York', 40.7, -74.0)") 
    def test_repr7(self):
        loc = Location("Orland", 28.5, -81.4)
        self.assertEqual(repr(loc),"Location('Orland', 28.5, -81.4)") 


if __name__ == "__main__":
        unittest.main()
