#Kelsey Nguyen
#CPE 202 Section 7
#Lab 7 
#Kelsey Nguyen
#CPE 202 Section 7
#Lab 7 


import unittest
from sorts import *

class TestLab7(unittest.TestCase):

    def test_selection1(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])
    def test_selection2(self):
        nums = [3, 1, 41, 59, 26, 53, 59]
        comps = selection_sort(nums)
        self.assertEqual(comps, 21)
        self.assertEqual(nums, [1, 3, 26, 41, 53, 59, 59])
    def test_selection3(self):
        nums = [20, 12, 10, 15, 2]
        comps = selection_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [2, 10, 12, 15, 20])
    def test_selection4(self):
        nums = [64, 25, 12, 22, 11]
        comps = selection_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [11, 12, 22, 25, 64])
    def test_insert1(self):
        nums = [6, 5, 4, 3, 2, 1]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 15)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6])
    def test_insert2(self):
        nums = [4, 3, 2, 10, 12, 1, 5, 6]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 16)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 10, 12])
    def test_insert3(self):
        nums = [25, 17, 31, 13, 2]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 9)
        self.assertEqual(nums, [2, 13, 17, 25, 31])
    def test_insert4(self):
        nums = [50, 40, 30, 20, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [10, 20, 30, 40, 50])
    def test_worstCase_selection(self):
        '''Worst case of selection sort would be any case because it is comparing every element with every other element in the array. It performs the same
           number of element comparisons in its best, average, and worst cases because it does not take advantange of existing order in the input

           It finds the minimum element of the array and shifts it to the first position (here, the input size is n).
           Next, it finds the minimum element from the remaining array and places the element in the second position (here, the input size is n-1).
           This procedure continues until the end of the array.
           As the active input size gradually reduces by 1 after every pass, the worst case time complexity would be O(n^2)'''

        '''This is an example of a worst case for selection sort because suppose the array in this case is unsorted in such a way that we have to 
           iterate over each of the n elements of the array just to find out the smallest value, and in selection sort, only 1 element is sorted out
           each time, so we need to repeat n times'''
        nums = [5, 2, 1, 3, 6, 4]
        comps = selection_sort(nums)
        self.assertEqual(comps, 15)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6])
    def test_worstCase_insert(self):
        '''Worst case of insertion sort would be when the array is in reversed order. 

           For the first item, you make 0 comparisons.
           For the second item, you compare it to the first item and find that they are not in the right position; you make 1 comparison.
           For the third item, you compare it with both, and find that the third has to go to the top; you make 2 comparisons.
           This goes on; for every following value, you make one more comparison.
           Lastly, for the nth term, you make n - 1 comparisons.
           Adding up the number of comparisons, it is 0 + 1 + 2 + ... + n - 1, which is equal to (n^2 - n) / 2 comparisons for the worst case, which is O(n^2).'''

        '''This is an example of a worst case for insertion sort beacuse it is a reverse sorted ordered list (list is in the exact opposite order you need).
           Since the  list is reverse sorted, the element at the (i-1)th position is always greater than the element at the ith position, and thus
           comparing and swapping will have to occur all the time'''
        nums = [72, 50, 45, 28, 15, 14, 2]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 21)
        self.assertEqual(nums, [2, 14, 15, 28, 45, 50, 72])

        



                
    
    
    

    

if __name__ == '__main__': 
    unittest.main()
