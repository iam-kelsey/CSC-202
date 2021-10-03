#Kelsey Nguyen
#CPE 202 Section 7
#Lab3



import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import StackArray
from stack_linked import StackLinked

class TestLab3(unittest.TestCase):
    
#Test Cases for StackArray

    def test_StackArray1(self):
        stack = StackArray(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)
    def test_StackArray_is_empty(self):
        MyStack = StackArray(3)
        self.assertTrue(MyStack.is_empty())
        MyStack.push(22)
        self.assertFalse(MyStack.is_empty())
        MyStack.push(81)
        self.assertFalse(MyStack.is_empty())
    def test_StackArray_is_full(self):
        MyStack = StackArray(3)
        self.assertFalse(MyStack.is_full())
        MyStack.push(33)
        MyStack.push(46)
        self.assertFalse(MyStack.is_full())
        MyStack.push(11)
        self.assertTrue(MyStack.is_full())
    def test_StackArray_push(self):
        MyStack = StackArray(3)
        MyStack.push(1)
        MyStack.push(2)
        MyStack.push(3)
        with self.assertRaises(IndexError):     
            MyStack.push(4)
    def test_StackArray_pop(self):
        MyStack = StackArray(5)
        with self.assertRaises(IndexError):     
            MyStack.pop()
        MyStack.push(2)
        MyStack.push(4)
        MyStack.push(6)
        self.assertEqual(MyStack.pop(), 6)
        MyStack.push(8)
        self.assertEqual(MyStack.pop(), 8)
        MyStack.push(10)
        self.assertEqual(MyStack.pop(), 10)
    def test_StackArray_peek(self):
        MyStack = StackArray(5)
        with self.assertRaises(IndexError):     
            MyStack.peek()
        MyStack.push(2)
        MyStack.push(4)
        MyStack.push(6)
        self.assertEqual(MyStack.peek(), 6)
        MyStack.push(8)
        self.assertEqual(MyStack.peek(), 8)
        MyStack.push(10)
        self.assertEqual(MyStack.peek(), 10)
    def test_StackArray_size(self):
        MyStack = StackArray(5)
        self.assertEqual(MyStack.size(), 0)
        MyStack.push(2)
        MyStack.push(4)
        MyStack.push(6)
        self.assertEqual(MyStack.size(), 3)
        MyStack.push(8)
        MyStack.push(10)
        self.assertEqual(MyStack.size(), 5)

#Test Cases for StackLinked
    
    def test_StackLinked_is_empty(self):
        MyStack = StackLinked(3)
        self.assertTrue(MyStack.is_empty())
        MyStack.push(22)
        self.assertFalse(MyStack.is_empty())
        MyStack.push(81)
        self.assertFalse(MyStack.is_empty())
    def test_StackLinked_is_full(self):
        MyStack = StackLinked(3)
        self.assertFalse(MyStack.is_full())
        MyStack.push(33)
        MyStack.push(46)
        self.assertFalse(MyStack.is_full())
        MyStack.push(11)
        self.assertTrue(MyStack.is_full())
    def test_StackLinked_push(self):
        MyStack = StackLinked(3)
        MyStack.push(1)
        MyStack.push(2)
        MyStack.push(3)
        with self.assertRaises(IndexError):     
            MyStack.push(4)
    def test_StackLinked_pop(self):
        MyStack = StackLinked(5)
        with self.assertRaises(IndexError):     
            MyStack.pop()
        MyStack.push(2)
        MyStack.push(4)
        MyStack.push(6)
        self.assertEqual(MyStack.pop(), 6)
        MyStack.push(8)
        self.assertEqual(MyStack.pop(), 8)
        MyStack.push(10)
        self.assertEqual(MyStack.pop(), 10)
    def test_StackLinked_peek(self):
        MyStack = StackLinked(5)
        with self.assertRaises(IndexError):     
            MyStack.peek()
        MyStack.push(2)
        MyStack.push(4)
        MyStack.push(6)
        self.assertEqual(MyStack.peek(), 6)
        MyStack.push(8)
        self.assertEqual(MyStack.peek(), 8)
        MyStack.push(10)
        self.assertEqual(MyStack.peek(), 10)
    def test_StackLinked_size(self):
        MyStack = StackLinked(5)
        self.assertEqual(MyStack.size(), 0)
        MyStack.push(2)
        MyStack.push(4)
        MyStack.push(6)
        self.assertEqual(MyStack.size(), 3)
        MyStack.push(8)
        MyStack.push(10)
        self.assertEqual(MyStack.size(), 5)










  
  
  
  
  
  
  
  
  




if __name__ == '__main__': 
    unittest.main()
