#Kelsey Nguyen
#CPE 202 Section 7
#Project 4


import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTableQuadPr(7)
        self.assertEquals(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTableQuadPr(7)
        self.assertEquals(ht.get_num_items(), 0)

    def test_01c(self):
        ht = HashTableQuadPr(7)
        self.assertAlmostEquals(ht.get_load_factor(), 0)

    def test_01d(self):
        ht = HashTableQuadPr(7)
        self.assertEquals(ht.get_all_keys(), [])

    def test_01e(self):
        ht = HashTableQuadPr(7)
        self.assertEquals(ht.in_table("cat"), False)

    def test_01f(self):
        ht = HashTableQuadPr(7)
        self.assertEquals(ht.get_value("cat"), None)

    def test_01g(self):
        ht = HashTableQuadPr(7)
        self.assertEquals(ht.get_index("cat"), None)

    def test_01h(self):
        ht = HashTableQuadPr(7)
        self.assertEquals(ht.horner_hash("cat"), 3)

    def test_02a(self):
        ht = HashTableQuadPr(7)
        ht.insert("cat", 5)
        self.assertEquals(ht.get_table_size(), 7)

    def test_02b(self):
        ht = HashTableQuadPr(7)
        ht.insert("cat", 5)
        ht.insert("dog", 6)
        ht.insert("meow", 7)
        self.assertEquals(ht.get_num_items(), 3)

    def test_02c(self):
        ht = HashTableQuadPr(7)
        ht.insert("cat", 5)
        self.assertAlmostEquals(ht.get_load_factor(), 1/7)

    def test_02d(self):
        ht = HashTableQuadPr(7)
        ht.insert("cat", 5)
        self.assertEquals(ht.get_all_keys(), ["cat"])

    def test_02e(self):
        ht = HashTableQuadPr(7)
        ht.insert("cat", 5)
        self.assertEquals(ht.in_table("cat"), True)

    def test_02f(self):
        ht = HashTableQuadPr(7)
        ht.insert("cat", 5)
        self.assertEquals(ht.get_value("cat"), [5])

    def test_02g(self):
        ht = HashTableQuadPr(7)
        ht.insert("cat", 5)
        self.assertEquals(ht.get_index("cat"), 3)
        self.assertEquals(ht.get_index("dog"), None)

    def test_03(self):
        ht = HashTableQuadPr(7)
        ht.insert("cat", 5)
        ht.insert("cat", 17)
        self.assertEquals(ht.get_value("cat"), [5, 17])

    def test_04(self):
        ht = HashTableQuadPr(7)
        ht.insert("cat", 5)
        self.assertEquals(ht.get_index("cat"), 3)

        ht.insert("dog", 8)
        self.assertEquals(ht.get_num_items(), 2)
        self.assertEquals(ht.get_index("dog"), 6)
        self.assertAlmostEquals(ht.get_load_factor(), 2 / 7)

        ht.insert("mouse", 10)
        self.assertEquals(ht.get_num_items(), 3)
        self.assertEquals(ht.get_index("mouse"), 4)
        self.assertAlmostEquals(ht.get_load_factor(), 3 / 7)

        
        '''ht.insert("elephant", 12) # hash table should be resized
        self.assertEquals(ht.get_num_items(), 4)
        #self.assertEquals(ht.get_table_size(), 15)
        self.assertAlmostEquals(ht.get_load_factor(), 4 / 15)
        self.assertEquals(ht.get_index("cat"), 12)
        self.assertEquals(ht.get_index("dog"), 14)
        self.assertEquals(ht.get_index("mouse"), 13)
        self.assertEquals(ht.get_index("elephant"), 9)
        keys = ht.get_all_keys()
        keys.sort()
        self.assertEquals(keys, ["cat", "dog", "elephant", "mouse"])'''

if __name__ == '__main__':
   unittest.main()
