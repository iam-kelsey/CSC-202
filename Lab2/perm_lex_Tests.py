# CPE 202 Lab 2
# Kelsey Nguyen
# Section 07

#Test Cases for lab 2
import unittest
from perm_lex import *

class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(len(perm_gen_lex ("")), 0)
    def test_2(self):
        self.assertEqual(len(perm_gen_lex ("a")), 1)
    def test_3(self):
        self.assertEqual(len(perm_gen_lex ("ab")), 2)
    def test_4(self):
        self.assertEqual(len(perm_gen_lex ("abc")), 6)
    def test_5(self):
        self.assertEqual(len(perm_gen_lex ("abcd")), 24)
    def test_6(self):
        self.assertEqual(len(perm_gen_lex ("abcde")), 120)
    def test_7(self):
        self.assertEqual(len(perm_gen_lex ("abcdef")), 720)
        
if (__name__ == '__main__'):
  unittest.main()
