#Kelsey Nguyen
#CPE 202 Section 7
#Project3 - Huffman Coding

import unittest
import filecmp
from huffman import *

class TestList(unittest.TestCase):
   def test_cnt_freq1(self):
      freqlist	= cnt_freq("file2.txt")
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0] 
      self.assertListEqual(freqlist[97:104], anslist[97:104])

   def test_cnt_freq2(self):
      freqlist	= cnt_freq("empty_file.txt")
      anslist = [0]*256
      anslist[97:104] = [0, 0, 0, 0, 0, 0, 0] 
      self.assertListEqual(freqlist[97:104], anslist[97:104])

   '''def test_cnt_freq3(self):
      freqlist	= cnt_freq("file1.txt")
      anslist = [0]*256
      anslist[97:104] = [4, 3, 2, 1, 0, 0, 0] 
      self.assertListEqual(freqlist[97:104], anslist[97:104])'''    

   def test_cnt_freq4(self):
      with self.assertRaises(FileNotFoundError):
         freqlist	= cnt_freq("file123.txt")
 
      
   def test_create_huff_tree1(self):
      freqlist = cnt_freq("file2.txt")
      hufftree = create_huff_tree(freqlist)
      numchars = 13
      charforroot = "a"
      self.assertEqual(hufftree.freq, 32)
      self.assertEqual(hufftree.char, 'a')
      left = hufftree.left
      self.assertEqual(left.freq, 16)
      self.assertEqual(left.char, 'a')
      right = hufftree.right
      self.assertEqual(right.freq, 16)
      self.assertEqual(right.char, 'd')

   '''def test_create_huff_tree2(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      numchars = 32
      charforroot = " "
      self.assertEqual(hufftree.freq, 13)
      self.assertEqual(hufftree.char, ' ')
      left = hufftree.left
      self.assertEqual(left.freq, 6)
      self.assertEqual(left.char, ' ')
      right = hufftree.right
      self.assertEqual(right.freq, 7)
      self.assertEqual(right.char, 'd')'''

   def test_create_huff_tree3(self):
      freqlist = cnt_freq("file3.txt")
      hufftree = create_huff_tree(freqlist)
      self.assertEqual(hufftree.freq, 9)
      self.assertEqual(hufftree.char, 'b')
      left = hufftree.left
      self.assertEqual(left.freq, 4)
      self.assertEqual(left.char, 'b')
      right = hufftree.right
      self.assertEqual(right.freq, 5)
      self.assertEqual(right.char, 'c')

   def test_create_code1(self):
      freqlist = cnt_freq("file2.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('d')], '1')
      self.assertEqual(codes[ord('a')], '0000')
      self.assertEqual(codes[ord('f')], '0001')

   def test_create_code2(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('d')], '100')
      self.assertEqual(codes[ord('a')], '11')
      self.assertEqual(codes[ord('c')], '101')
      self.assertEqual(codes[ord('b')], '01')
      self.assertEqual(codes[ord(' ')], '00')

   def test_create_code3(self):
      freqlist = cnt_freq("file3.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('a')], '11')
      self.assertEqual(codes[ord('c')], '10')
      self.assertEqual(codes[ord('b')], '0')


   def test_create_header1(self):
      freqlist = cnt_freq("file3.txt")
      ans = "97 3 98 4 99 2"
      self.assertEqual(create_header(freqlist), ans)

   def test_create_header2(self):
      freqlist = cnt_freq("file2.txt")
      ans = "97 2 98 4 99 8 100 16 102 2"
      self.assertEqual(create_header(freqlist), ans)  
   
   '''def test_create_header3(self):
      freqlist = cnt_freq("file1.txt")
      ans = "32 3 97 4 98 3 99 2 100 1"
      self.assertEqual(create_header(freqlist), ans)


   def test_01_encodefile1(self):
      huffman_encode("file2.txt", "output1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("output1.txt", "output1_soln.txt"))

   def test_01_encodefile2(self):
      with self.assertRaises(FileNotFoundError):
         huffman_encode("hello.txt", "hello_out.txt")

   def test_01_encodefile3(self):
      with self.assertRaises(FileNotFoundError):
         huffman_encode("files123.txt", "output1_soln.txt")

   def test_01_encodefile4(self):
      huffman_encode("empty_file.txt", "empty_out.txt")
      self.assertTrue(filecmp.cmp("empty_out.txt", "empty_file_soln.txt"))'''




   
   def test_01_decodefile(self):
      freqlist = cnt_freq("file2.txt")
      huffman_decode(freqlist,"output1.txt", "decodefile1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodefile1.txt", "file2.txt"))'''

if __name__ == '__main__': 
   unittest.main()
