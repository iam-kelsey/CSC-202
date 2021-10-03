#Kelsey Nguyen
#CPE 202 Section 7
#Lab4 - Queue

import unittest
from queue_array import QueueArray
from queue_linked import QueueLinked

class TestLab4(unittest.TestCase):

    #Test Cases for QueueArray
    def test_QueueArray1(self):                         #circular test
        MyQueue = QueueArray(5)
        MyQueue.enqueue(1)
        self.assertFalse(MyQueue.is_empty())
        self.assertFalse(MyQueue.is_full())
        self.assertEqual(MyQueue.num_in_queue(), 1)
        MyQueue.enqueue(2)
        MyQueue.enqueue(3)
        MyQueue.enqueue(4)
        MyQueue.enqueue(6)
        self.assertEqual(MyQueue.dequeue(), 1)
        self.assertEqual(MyQueue.num_in_queue(), 4)
        MyQueue.enqueue(5)
        self.assertEqual(MyQueue.dequeue(), 2)
    def test_QueueuArray_is_empty(self): 
        MyQueue = QueueArray(5)
        self.assertTrue(MyQueue.is_empty())
        MyQueue.enqueue(10)
        MyQueue.enqueue(22)
        self.assertFalse(MyQueue.is_empty())
    def test_QueueArray_is_full(self): 
        MyQueue = QueueArray(3)
        self.assertFalse(MyQueue.is_full())
        MyQueue.enqueue(33)
        self.assertFalse(MyQueue.is_full())
        MyQueue.enqueue(40)
        MyQueue.enqueue(23)
        self.assertTrue(MyQueue.is_full())
    def test_QueueArray_enqueue(self):
        MyQueue = QueueArray(3)
        MyQueue.enqueue(1)
        MyQueue.enqueue(2)
        MyQueue.enqueue(3)
        with self.assertRaises(IndexError):
            MyQueue.enqueue(4)
    def test_QueueArray_dequeue(self):
        MyQueue = QueueArray(5)
        with self.assertRaises(IndexError):
            MyQueue.dequeue()
        MyQueue.enqueue("hello")
        MyQueue.enqueue(14)
        self.assertEqual(MyQueue.dequeue(), "hello")
        MyQueue.enqueue("dog")
        self.assertEqual(MyQueue.dequeue(), 14)
        MyQueue.enqueue(11)
        self.assertEqual(MyQueue.dequeue(), "dog")
    def test_QueueArray_num_in_queue(self):
        MyQueue = QueueArray(5)
        self.assertEqual(MyQueue.num_in_queue(), 0)
        MyQueue.enqueue(2)
        MyQueue.enqueue(4)
        MyQueue.enqueue(6)
        self.assertEqual(MyQueue.num_in_queue(), 3)
        MyQueue.enqueue(8)
        MyQueue.enqueue(10)
        self.assertEqual(MyQueue.num_in_queue(), 5)
    
    #Test Cases for QueueLinked
    def test_QueueLinked1(self):                            #circular test
        MyQueue = QueueLinked(5)
        MyQueue.enqueue(1)
        self.assertFalse(MyQueue.is_empty())
        self.assertFalse(MyQueue.is_full())
        self.assertEqual(MyQueue.num_in_queue(), 1)
        MyQueue.enqueue(2)
        MyQueue.enqueue(3)
        MyQueue.enqueue(4)
        MyQueue.enqueue(6)
        self.assertEqual(MyQueue.dequeue(), 1)
        self.assertEqual(MyQueue.num_in_queue(), 4)
        MyQueue.enqueue(5)
        self.assertEqual(MyQueue.dequeue(), 2)
    def test_QueueLinked_is_empty(self):
        MyQueue = QueueLinked(3)
        self.assertTrue(MyQueue.is_empty())
        MyQueue.enqueue(22)
        self.assertFalse(MyQueue.is_empty())
        MyQueue.enqueue(81)
        self.assertFalse(MyQueue.is_empty())
    def test_QueueLinked_is_full(self):
        MyQueue = QueueLinked(3)
        self.assertFalse(MyQueue.is_full())
        MyQueue.enqueue(33)
        MyQueue.enqueue(46)
        self.assertFalse(MyQueue.is_full())
        MyQueue.enqueue(11)
        self.assertTrue(MyQueue.is_full())
    def test_QueueLinked_enqueue(self):
        MyQueue = QueueLinked(3)
        MyQueue.enqueue(1)
        MyQueue.enqueue(2)
        MyQueue.enqueue(3)
        with self.assertRaises(IndexError):     
            MyQueue.enqueue(4)
    def test_QueueLinked_dequeue(self):
        MyQueue = QueueLinked(5)
        with self.assertRaises(IndexError):
            MyQueue.dequeue()
        MyQueue.enqueue(10)
        MyQueue.enqueue(14)
        self.assertEqual(MyQueue.dequeue(), 10)
        MyQueue.enqueue("dog")
        self.assertEqual(MyQueue.dequeue(), 14)
        MyQueue.enqueue(11)
        self.assertEqual(MyQueue.dequeue(), "dog")
    def test_QueueLinked_num_in_queue(self):
        MyQueue = QueueLinked(5)
        self.assertEqual(MyQueue.num_in_queue(), 0)
        MyQueue.enqueue(2)
        MyQueue.enqueue(4)
        MyQueue.enqueue(6)
        self.assertEqual(MyQueue.num_in_queue(), 3)
        MyQueue.enqueue(8)
        MyQueue.enqueue(10)
        self.assertEqual(MyQueue.num_in_queue(), 5)
  

if __name__ == '__main__': 
    unittest.main()