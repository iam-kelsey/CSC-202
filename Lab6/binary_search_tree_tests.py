#Kelsey Nguyen
#CPE 202 Section 7
#Lab6 - BST

import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):
    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertFalse(bst.is_empty())
        self.assertTrue(bst.search(10))
        self.assertFalse(bst.search(11))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])
  
    def test_is_empty(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(20, 'thing')
        self.assertFalse(bst.is_empty())
   
    def test_insert(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(3, 'stuff')
        self.assertFalse(bst.is_empty())
        bst.insert(2, 'thing')
        bst.insert(9, "other")
        bst.insert(10, "first")
        self.assertFalse(bst.search(12))
        self.assertTrue(bst.search(2))
   
    def test_search(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(3, 'stuff')
        self.assertFalse(bst.search(2))
        self.assertFalse(bst.is_empty())
        bst.insert(2, 'thing')
        bst.insert(9, "other")
        self.assertTrue(bst.search(9))
        bst.insert(10, "first")
        self.assertFalse(bst.search(12))
        self.assertTrue(bst.search(2))
   
    def test_find_max(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.find_max(), None)
        self.assertTrue(bst.is_empty())
        bst.insert(30, 'stuff')
        self.assertFalse(bst.is_empty())
        bst.insert(12, "fun")
        self.assertEqual(bst.find_max(), (30, 'stuff'))
        bst.insert(17, "thing")
        self.assertEqual(bst.find_max(), (30, 'stuff'))
   
    def test_find_min(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.find_min(), None)
        self.assertTrue(bst.is_empty())
        bst.insert(30, 'stuff')
        self.assertFalse(bst.is_empty())
        bst.insert(12, "fun")
        bst.insert(1, "thing")
        self.assertEqual(bst.find_min(), (1, 'thing'))
   
    def test_tree_height(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.tree_height(), None)
        bst.insert(30, 'stuff')
        self.assertEqual(bst.tree_height(), 0)
        bst.insert(8, 'first1')
        self.assertEqual(bst.tree_height(), 1)
        bst.insert(35, 'first2')
        bst.insert(9, 'first3')
        self.assertEqual(bst.tree_height(), 2)
        bst.insert(36, 'first4')
        bst.insert(37, 'first5')
        bst.insert(38, 'first6')
        self.assertEqual(bst.tree_height(), 4)
  
    def test_preorder_list(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.preorder_list(), None)
        bst.insert(4, 'stuff')
        bst.insert(6, 'other')
        bst.insert(9, 'yes')
        bst.insert(7, 'no')
        self.assertEqual(bst.preorder_list(), [4, 6, 9, 7])
        bst.insert(20, 's')
        bst.insert(21, 'ma')
        bst.insert(19.6, 'yesm')
        bst.insert(1.1, 'not')
        self.assertEqual(bst.preorder_list(), [4, 1.1, 6, 9, 7, 20, 19.6, 21])
        bst.insert(10, 'other')
        bst.insert(8.9, 'other1')
        bst.insert(33, 'other2')
        self.assertEqual(bst.preorder_list(), [4, 1.1, 6, 9, 7, 8.9, 20, 19.6, 10, 21, 33])

    def test_inorder_list(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.inorder_list(), None)
        bst.insert(20, 'stuff')
        bst.insert(21, 'other')
        bst.insert(22, 'yes')
        bst.insert(23, 'no')
        self.assertEqual(bst.inorder_list(), [20, 21, 22, 23])
        bst.insert(21, 'key')
        bst.insert(24, 'key1')
        bst.insert(25, 'key2')
        self.assertEqual(bst.inorder_list(), [20, 21, 22, 23, 24, 25])
        bst.insert(19, 'key3')
        bst.insert(8, 'key4')
        bst.insert(15, 'key5')
        bst.insert(10, 'key6')
        self.assertEqual(bst.inorder_list(), [8, 10, 15, 19, 20, 21, 22, 23, 24, 25])

    def test_level_order_list(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.level_order_list(), None)
        bst.insert(20, 'stuff')
        bst.insert(20, 'other')
        bst.insert(22, 'yes')
        bst.insert(11, 'no')
        self.assertEqual(bst.level_order_list(), [20, 11, 22])
        bst.insert(5.3, "key1")
        bst.insert(7.5, "key2" )
        bst.insert(39, 'key3')
        bst.insert(41, "key4")
        bst.insert(80, "key5" )
        bst.insert(28, 'key6')
        self.assertEqual(bst.level_order_list(), [20, 11, 22, 5.3, 39, 7.5, 28, 41, 80])
        bst.insert(19, 'key6')
        self.assertEqual(bst.level_order_list(), [20, 11, 22, 5.3, 19, 39, 7.5, 28, 41, 80])




        



if __name__ == '__main__': 
    unittest.main()
