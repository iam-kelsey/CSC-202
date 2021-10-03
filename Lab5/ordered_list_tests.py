#Kelsey Nguyen
#CPE 202 Section 7
#Lab5 - Ordered List

import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
    def test_OrderedList_is_empty(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(20)
        t_list.add(40)
        self.assertFalse(t_list.is_empty())
    def test_OrderedList_index(self):
        t_list = OrderedList()
        t_list.add(20)
        t_list.add(40)
        self.assertEqual(t_list.index(20), 0)
        self.assertEqual(t_list.index(40), 1)
        self.assertEqual(t_list.index(10), None)
    def test_OrderedList_pop(self):
        t_list = OrderedList()
        t_list.add(20)
        t_list.add(40)
        self.assertEqual(t_list.pop(0), 20)
        with self.assertRaises(IndexError):
            t_list.pop(-2)
        t_list.add(60)
        with self.assertRaises(IndexError):
            t_list.pop(5)
    def test_OrderedList_pop2(self):
        t_list = OrderedList()
        t_list.add(20)
        t_list.add(40)
        t_list.add(60)
        t_list.add(80)
        self.assertEqual(t_list.pop(0), 20)
        self.assertEqual(t_list.pop(2), 60)
        self.assertEqual(t_list.pop(1), 40)
    def test_OrderedList_size(self):
        t_list = OrderedList()
        t_list.add(20)
        t_list.add(40)
        self.assertEqual(t_list.size(), 2) 
        t_list.add(10)
        self.assertEqual(t_list.size(), 3) 
    def test_python_list(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(2)
        t_list.add(3)
        self.assertEqual(t_list.python_list(), [1, 2, 3])
    def test_add(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(2)
        t_list.add(3)
        self.assertFalse(t_list.is_empty())
    def test_add2(self):
        t_list = OrderedList()
        self.assertTrue(t_list.add(1))
        t_list.add(2)
        t_list.add(3)
        self.assertFalse(t_list.add(1))
        self.assertEqual(t_list.size(), 3)
    def test_remove(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(2)
        t_list.add(3)
        self.assertTrue(t_list.remove(2))
        self.assertFalse(t_list.remove(8))
        self.assertEqual(t_list.size(), 2)
        t_list.remove(1)
        t_list.remove(3)
        self.assertEqual(t_list.size(), 0)
    def test_search(self):
        t_list = OrderedList()
        t_list.add(10)   
        t_list.add(15)
        t_list.add(20)
        self.assertTrue(t_list.search(10))
        self.assertTrue(t_list.search(15))
        self.assertTrue(t_list.search(20))
        self.assertFalse(t_list.search(18))
    def test_python_list_reversed(self):
        t_list = OrderedList()
        t_list.add(1)   
        t_list.add(2)
        t_list.add(3)
        self.assertEqual(t_list.python_list_reversed(), [3, 2, 1])
    def test_python_list_reversed2(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list_reversed(), [10])
        t_list.add(11)
        self.assertEqual(t_list.python_list_reversed(), [11, 10])
        t_list.remove(10)
        self.assertEqual(t_list.python_list_reversed(), [11])
        


    
        

if __name__ == '__main__': 
    unittest.main()
