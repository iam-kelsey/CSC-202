#Kelsey Nguyen
#CPE 202 Section 7
#Project3 - Huffman Coding

import unittest
import filecmp
from huffman import *

class TestList(unittest.TestCase):
   def test_character_order1(self):
       first_node = HuffmanNode("a", 2)
       second_node = HuffmanNode("b", 3)
       self.assertTrue(character_order(first_node, second_node))
   def test_character_order2(self):
       first_node = HuffmanNode("a", 3)
       second_node = HuffmanNode("b", 3)
       self.assertTrue(character_order(first_node, second_node))
   def test_character_order3(self):
       first_node = HuffmanNode("d", 3)
       second_node = HuffmanNode("b", 3)
       self.assertFalse(character_order(first_node, second_node))
   def test_character_order4(self):
       first_node = HuffmanNode("a", 4)
       second_node = HuffmanNode("b", 3)
       self.assertFalse(character_order(first_node, second_node))









if __name__ == '__main__': 
   unittest.main()