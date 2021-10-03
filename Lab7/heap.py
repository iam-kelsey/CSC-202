#Kelsey Nguyen
#CPE 202 Section 7
#Lab 7 


#Array implementation of Max Binary Heap (Priority Queue) 
#MaxHeap is a representation of a maxheap
class MaxHeap:

    #self, capacity --> MaxHeap
    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""

        #a heapList is a list, representing an empty binary heap
        #capacity is a positive integer, representing the maximum number of a entries the heap can hold
        #currentSize is a positive integer, representing the size of the heap
        self.heapList = [None]*(capacity+1)
        self.capacity = capacity
        self.currentSize = 0
        

    #MaxHeap --> boolean
    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""
        if self.currentSize == len(self.heapList)-1:
            return False
        self.currentSize += 1
        self.heapList[self.currentSize] = item
        self.perc_up(self.currentSize)
        return True

    #MaxHeap --> int
    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""
        if self.currentSize == 0:
            return None
        

    #MaxHeap --> int
    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.currentSize == 0:
            return
        max_value = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList[self.currentSize] = max_value
        self.currentSize = self.currentSize - 1
        self.perc_down(1)
        return max_value

    #MaxHeap --> list
    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        lst_of_content = self.heapList
        lst_of_content = lst_of_content[1:self.currentSize+1]
        return lst_of_content

    #MaxHeap, list --> boolean
    def build_heap(self, alist):
        """Builds a heap from the items in alist and builds a heap using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased"""

        temp = 1
        for x in alist:
            self.heapList[temp] = alist[temp-1]
            temp = temp + 1
            self.currentSize = self.currentSize + 1
        for x in range(self.get_size()//2, 0, -1):
            self.perc_down(x)
        return True

    #MaxHeap --> boolean
    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        if self.currentSize == 0:
            return True
        else:
            return False

    #MaxHeap --> boolean
    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        if self.currentSize == self.capacity:
            return True
        else:
            return False

    #MaxHeap --> int
    def get_capacity(self):
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.capacity
    
    #MaxHeap --> int
    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.currentSize

    #MaxHeap, int --> None
    def perc_down(self, idx):
        """where the parameter idx is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        current = self.heapList[idx]
        if idx * 2 < len(self.heapList) and idx * 2 + 1 < len(self.heapList):
            node1 = self.heapList[idx * 2]
            node2 = self.heapList[idx * 2 + 1]
        while (idx * 2 <= len(self.heapList) and idx * 2 + 1 <= len(self.heapList)) and self.perc_down_helper(current, idx * 2, idx * 2 + 1):
            if node2 is None:
                temp = self.heapList[idx * 2]
                self.heapList[idx * 2] = self.heapList[idx]
                self.heapList[idx] = temp
                break
            if node1 > node2:
                temp = self.heapList[idx * 2]
                self.heapList[idx * 2] = self.heapList[idx]
                self.heapList[idx] = temp
                idx *= 2
                current = self.heapList[idx]
                if idx * 2 < len(self.heapList):
                    node1 = self.heapList[idx * 2]
                if idx * 2 + 1 < len(self.heapList):
                    node2 = self.heapList[idx * 2 + 1]
            else:
                temp = self.heapList[idx * 2 + 1]
                self.heapList[idx * 2 + 1] = self.heapList[idx]
                self.heapList[idx] = temp
                idx = idx * 2 + 1
                current = self.heapList[idx]
                if idx * 2 < len(self.heapList):
                    node1 = self.heapList[idx * 2]
                if idx * 2 + 1 < len(self.heapList):
                    node2 = self.heapList[idx * 2 + 1]

    def perc_down_helper(self, current, node1, node2):
        '''Helper function of perc_down'''
        if node1 < len(self.heapList) and node2 < len(self.heapList):
            if self.heapList[node1] is not None and self.heapList[node2] is None:
                if node1 <= self.currentSize:
                    if current <= self.heapList[node1]:
                        return True
            elif self.heapList[node1] is not None and self.heapList[node2] is not None:
                if node1 <= self.currentSize and node2 <= self.currentSize:
                    if current <= self.heapList[node1] or current <= self.heapList[node2]:
                        return True
            else:
                return False
        return False
        
    def perc_up(self, idx):
        """where the parameter idx is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        temp = idx // 2
        element = idx
        while (temp > 0) and (self.heapList[temp] <= self.heapList[element]):
            current = self.heapList[temp]
            self.heapList[temp] = self.heapList[element]
            self.heapList[element] = current
            element = temp
            temp = temp // 2

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order"""
        self.build_heap(alist)
        for x in range(self.get_size()):
            if self.currentSize == 2:
                if self.heapList[2] > self.heapList[1]:
                    break
            self.dequeue()
        return self.heapList[1:len(alist)+1]


