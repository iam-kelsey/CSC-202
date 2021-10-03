#Kelsey Nguyen
#CPE 202 Section 7
#Lab 7 

import unittest
import random
import time


#list --> int
#Sorts a list using quick sort with the first element always chosen as pivot
#Step 1: Call the quicksort helper function, passing in the list, 0, and length of list -1 
def quicksort(alist):
    return quicksort_helper(alist, 0, len(alist)-1)

#list, int, int --> int
#Helper function of quicksort. The purpose of this function is to ensure that we have sorted only this section using recursion.
#Step 1: Make a counter variable
#Step 2: If first is less than last, partition the array
#Step 3: Make recursive calls on the sub-parts
#Step 4: Return counter
def quicksort_helper(alist, first, last):
    counter = 0
    if first < last:
        splitpoint, counter = partition(alist, first, last)        
        counter += quicksort_helper(alist, first, splitpoint - 1)
        counter += quicksort_helper(alist, splitpoint + 1, last)
    return counter

#list, int, int --> int, int
#Partition function places pivot in sorted array. It finds the split point and at the same time move other items to the appropraite side of the list, either less than or greater than the pivot value
#Step 1: Make a counter variable to keep track of the number of comparisons 
#Step 2: Choose a pivot
#Step 3: Divide the array so that everything smaller than the pivot is in the first part of the array
#Step 4: After inserting the pivot, get the larger elements
#Step 5: Remember to add to counter varaiable everytime we compare values from the away
#Step 6: Return the position and counter
def partition(alist, first, last):
    counter = 0
    leftmark = first
    rightmark = last
    for i in range(leftmark, rightmark):
        counter += 1
        if alist[i] < alist[rightmark]:
            alist[i], alist[leftmark] = alist[leftmark], alist[i]
            leftmark += 1

    alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    return leftmark, counter

#list --> int
#Sort an array using quick sort and uses the median element from the first, middle and last elemeents as the pivot 
#Step 1: Call quick sort helper function passing in the list, 0, and length of the list
def quicksort_med(alist):
    return quicksort_med_helper(alist, 0, len(alist))

#list, int, int --> int
#Helper function of quicksort_med. 
#Step 1: Make a counter variable
#Step 2: If first is less than last, partition the array
#Step 3: Make recursive calls on the sub-parts
#Step 4: Return counter
def quicksort_med_helper(alist, first, last): 
    counter = 0
    if first < last: 
        pivot, counter = partition_med(alist, first, last)
        counter += quicksort_med_helper(alist, first, pivot)  
        counter += quicksort_med_helper(alist, pivot + 1, last)
    return counter

#list, int, int --> int
#Partition function reorders the array so that all items less than the one you picked are before it in the array and all of those greater than it are after it
#Step 1: Make a counter variable to keep track of the number of comparisons 
#Step 2: Call find_median function to choose median of the three elements as the pivot
#Step 3: Divide the array so that everything smaller than the pivot is in the first part of the array
#Step 4: After inserting the pivot, get the larger elements
#Step 5: Remember to add to counter varaiable everytime we compare values from the away
#Step 6: Return the position and counter
def partition_med(alist, first, last):
    stop = True
    counter = 0 
    pivot, x = find_median(alist, first, last)
    alist[first], alist[x] = alist[x], alist[first]
    left = first + 1
    for right in range(first+1, last):
        counter += 1
        if (stop == True and alist[right] < pivot) or (stop != True and alist[right] > pivot):
            alist[left], alist[right] = alist[right], alist[left]  
            left += 1
    alist[first], alist[left-1] = alist[left-1], alist[first] 
    return left - 1, counter

#list, int, int --> int, int
#Helper function that finds the median element from the first, middle, and last elements
#Step 1: Calculate the middle index by averging the given left and right indices
#Step 2: Swap these indices if necessary so that alist[left] = smallest, alist[right] = largest, alist[middle] = median of three 
#Step 3: If alist[left] <= alist[middle] <= alist[right-1], return alist[middle] and middle index
#Step 4: If alist[right-1] <= alist[middle] <= alist[left], return alist[middle] and middle index
#Step 5: If alist[left] <= alist[right-1] <= alist[middle], return alist[right-1] and right-1
#Step 6: If alist[middle] <= alist[right-1] <= alist[left], return alist[right-1] and right-1
#Step 7: Return alist[left] and left value                                              
def find_median(alist, left, right):
    middle = (left+right-1)//2
    a = alist[left]
    b = alist[middle]
    c = alist[right-1]
    if a <= b <= c:
        return b, middle
    if c <= b <= a:
        return b, middle
    if a <= c <= b:
        return c, right-1
    if b <= c <= a:
        return c, right-1
    return a, left

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 100)
    start_time = time.time() 
    comps = quicksort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

class TestQuickSort(unittest.TestCase):
    def test_quicksort1(self):
        nums = [2, 3, 1]
        count = quicksort(nums)
        self.assertEqual(count, 3)
        self.assertEqual(nums, [1, 2, 3])
    def test_quicksort2(self):
        nums = [3, 4, 2, 6, 10]
        count = quicksort(nums)
        self.assertEqual(count, 10)
        self.assertEqual(nums, [2, 3, 4, 6, 10])
    def test_quicksort3(self):
        nums = [8, 7, 6, 5, 4]
        count = quicksort(nums)
        self.assertEqual(count, 10)
        self.assertEqual(nums, [4, 5, 6, 7, 8])
    def test_quicksort4(self):
        nums = [8, 7, 6, 5, 4]
        count = quicksort(nums)
        self.assertEqual(count, 10)
        self.assertEqual(nums, [4, 5, 6, 7, 8])
    def test_quicksort5(self):
        nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        count = quicksort(nums)
        self.assertEqual(count, 25)
        self.assertEqual(nums, [17, 20, 26, 31, 44, 54, 55, 77, 93])
    def test_quicksort_med1(self):
        nums = [3, 4, 2, 6, 10]
        count = quicksort_med(nums)
        self.assertEqual(count, 6)
        self.assertEqual(nums, [2, 3, 4, 6, 10])
    def test_quicksort_med2(self):
        nums = [5, 3, 1, 7, 9]
        count = quicksort_med(nums)
        self.assertEqual(count, 6)
        self.assertEqual(nums, [1, 3, 5, 7, 9])
    def test_quicksort_med3(self):
        nums = [8, 2, 4, 5, 7, 1, 0]
        count = quicksort_med(nums)
        self.assertEqual(count, 11)
        self.assertEqual(nums, [0, 1, 2, 4, 5, 7, 8])
    def test_quicksort_med4(self):
        nums = [10, 11, 12]
        count = quicksort_med(nums)
        self.assertEqual(count, 2)
        self.assertEqual(nums, [10, 11, 12])
    def test_quicksort_med5(self):
        nums = [40, 80, 10, 25]
        count = quicksort_med(nums)
        self.assertEqual(count, 4)
        self.assertEqual(nums, [10, 25, 40, 80])


if __name__ == '__main__': 
    main()
    unittest.main()
