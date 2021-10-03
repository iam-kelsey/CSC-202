# Kelsey Nguyen
# Section 07

#Test Cases for Lab1
from Lab1 import *

import unittest

class TestCase(unittest.TestCase):
    def test_max_list_rec1(self):
        tlist = [10, 9, 8 ,4, 9]
        self.assertEqual(max_list_rec(tlist),10)
        tlist = []
        with self.assertRaises(ValueError):  # magic - uses context manager
            max_list_rec(tlist)  
    def test_max_list_rec2(self):
        tlist = [2, -1, 0, 4, 12]
        self.assertEqual(max_list_rec(tlist), 12)
    def test_max_list_rec3(self):
        tlist = []
        with self.assertRaises(ValueError):
            max_list_rec(tlist)
    def test_max_list_rec4(self):
        tlist = [-5, -4, -3, -2, -1, 0]
        self.assertEqual(max_list_rec(tlist), 0)

    def test_max_list_iter1(self):
        tlist = []
        with self.assertRaises(ValueError):
            max_list_rec(tlist)
    def test_max_list_iter2(self):
        tlist = [6, 10, 20, 30, -4, 100] 
        self.assertEqual(max_list_iter(tlist), 100)
    def test_max_list_iter3(self):
        tlist = [-5, -4, -3, -2, -1, 0]
        self.assertEqual(max_list_iter(tlist), 0)
       
    def test_reverse_rec1(self):
        self.assertEqual(reverse_rec("abcd"),"dcba")
    def test_reverse_rec2(self):
        self.assertEqual(reverse_rec("Coachella"), "allehcaoC")
    def test_reverse_rec3(self):
        self.assertEqual(reverse_rec("EDCLV"), "VLCDE")
    def test_reverse_rec4(self):
        self.assertEqual(reverse_rec("CalPoly"), "yloPlaC")
        
    
    def test_bin_search1(self):
        list_val = [15, 21, 47, 84, 96]
        self.assertEqual( bin_search(8, 0, 5, list_val), None)
    def test_bin_search2(self):    
        list_val = [2, 3, 5, 10, 40]
        self.assertEqual( bin_search(10, 0, len(list_val)-1, list_val), 3)
    def test_bin_search3(self):
        list_val = [-100, -90, -75, -60, -20, -5, 0]
        self.assertEqual( bin_search(0, 0, len(list_val)-1, list_val),6)
    def test_bin_search4(self):
        list_val = []
        self.assertEqual( bin_search(45,0,len(list_val)-1,list_val), None)
    def test_bin_search5(self):
        list_val =[18, 90, 15, 29, 70]
        self.assertEqual( bin_search(22, 0, len(list_val)-1, list_val), None)
    def test_bin_search6(self):
        list_val =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        with self.assertRaises(ValueError):
            bin_search(1, len(list_val)-1, 0, list_val)
 
     
        
# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()
