#Kelsey Nguyen
#CPE 202 Section 7
#Lab5 - Ordered List


#Class creates nodes for use with doubly-linked list
#A node is the presenting an item 
class Node:
    #constructor initializes node
    

    #an item is a value based on the given type
    #a next is the reference pointer to the next node 
    #a prev is the reference pointer to the previous node
    def __init__(self, item):
        self.item = item    #Assign data/value stored in the node
        self.next = None    #initialized to none
        self.prev = None    #initialized to none
    
    def __eq__(self, other):
        return type(self) == type(other) and self.item == other.item

    def __lt__(self, other):
        return self.item < other.item

#Implements a doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)
#Orderedlist is a represetation of an ordered list
class OrderedList:
    #head is a positive integer, representing the first node in the ordered list

    #self --> OrderedList
    #Creates an empty list 
    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.head = None
        
 

    #OrderedList --> boolean
    #Checks if list is empty
    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.head.item == None
        

    #OrderedList --> boolean
    #Adds an item to OrderedList in the proper location based on ordering of items from lowest to highest
    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''

        temp = Node(item)
        if self.head == None:
            self.head = temp
            return True
        #elif temp == self.head:
            #return False
        elif temp < self.head:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
            return True
        else:
            previous = self.head
            current = self.head.next 

            while current != None:
                if temp < current:
                    previous.next = temp
                    temp.prev = previous
                    temp.next = current
                    current.prev = temp
                    return True
                else:
                    previous = current
                    current = current.next

            previous.next = temp
            temp.prev = previous
            return True


    #OrderedList, item (int) --> boolean
    #Removes the first occurrence of an item from OrderedList
    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        current = self.head
        previous = None
        found = False
        while not found:
            if current == None:
                return False
            elif current.item == item:
                found = True
            else:
                previous = current
                current = current.next
        if not found:
            return False
        if current == self.head:
            self.head = current.next
        else:
            previous.next = current.next
        return True


    #OrderedList, item (int) --> index (int)
    #Returns index of the first occurrence of an item in OrderedList
    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''

        current = self.head
        idx = 0
        if item == current.item:
            return 0 
        while current.item != item:
            if current.next is None:
                return None
            current = self.head.next
            idx += 1
        return idx


    #OrderedList, index (int) --> item (int)
    #Removes and returns item at index
    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''

        current = self.head
        counter = 0
        if (index < 0) or (index >= self.size()):
            raise IndexError
        if index == 0:
            item = self.head.item
            self.head = self.head.next
            return item
        while counter is not index:
            current = current.next
            counter += 1
        item = current.item
        previous = current.prev
        next = current.next
        previous.next = next
        if next is not None:
            next.prev = previous
        return item
       
    
    #OrderedList, index (int) --> boolean
    #Searches OrderedList for item and returns True if item is in list, False otherwise. Calls helper function, search_helper
    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.search_helper(self.head, item)

    #Orderedlist, Node, int --> boolean
    #Helper method for search method, uses recursion
    def search_helper(self, temp, item):
        if temp.item == item:
            return True
        elif temp.item > item:
            return False
        return self.search_helper(temp.next, item)

    #OrderedList --> list
    #Returns a Python list representation of OrderedList, from head to tail
    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        current = self.head
        python_lst = []

        for x in range(self.size()):
            python_lst.append(current.item)
            current = current.next
            
        return python_lst
    
    #OrderedList --> list
    #Returns a reversed Python list representation of OrderedList. Calls helper method, python_list_reversed_helper
    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.python_list_reversed_helper(self.python_list())
    
    #OrderedList, list --> list
    #Helper method for python_list_reversed, uses recursion
    def python_list_reversed_helper(self, python_lst):
        '''if len(python_lst) <= 1:
            return python_lst
        reversed_lst = [python_lst[-1]] + self.python_list_reversed_helper(python_lst[:-1])
        return reversed_lst'''
        if len(python_lst) == 1:
            return [python_lst[0]]
        return self.python_list_reversed_helper(python_lst[1:]) + [python_lst[0]] 

    #OrderedList --> int
    #Returns the number of items in the OrderedList. Calls helper method, size_helper
    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.head)

    #Orderedlist, Node --> int
    #Helper method for size method, uses recursion
    def size_helper(self, temp):
        if (temp == None) or (temp.item == None):
            return 0
        return self.size_helper(temp.next) + 1

