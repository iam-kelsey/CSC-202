#Kelsey Nguyen
#CPE 202 Section 7
#Lab3


#Implements an efficient last-in first-out Abstract Data Type using a Python List
class StackArray:
    #a capacity is an int
    #an item is a list
    #num_items are int

#Creates and empty stack with a capacity
    def __init__(self, capacity):
        self.capacity = capacity        #capacity is the static size of stack
        self.items = [None]*capacity    #initializing the stack
        self.num_items = 0              #number of elements in the stack

    #none --> boolean
    #Checks if stack is empty
    #Step 1. Returns True if the stack is empty, and False otherwise
    def is_empty(self):
        return self.num_items == 0
            

    #none --> boolean
    #Checks if stack is full
    #Step 1: Returns True if the stack is full, and False otherwise
    def is_full(self):
        return self.num_items == self.capacity
           

    #item --> none
    #Adds data to the start of the stack
    #Step 1: If stack is not full, push item on stack. 
    #Step 2: If stack is full when push is attempted, raise IndexError "Stack is full"
    def push(self, item):
        if self.num_items == self.capacity:
            raise IndexError('Stack is full')
        self.items[self.num_items] = item
        self.num_items += 1
        

    #none --> int
    #Removes element that is the current head (item in the beginning of the stack)
    #Step 1: If stack is not empty, pops item from stack and returns item.
    #Step 2: If stack is empty when pop is attempted, raise IndexError
    def pop(self): 
        if self.num_items == 0:
            raise IndexError('Stack is empty')
        popped = self.items[self.num_items -1]
        self.items[self.num_items -1] = None
        self.num_items -= 1
        return popped
		    


    #none --> int
    #Returns the head node data/item in the beginning of the stack
    #Step 1: If stack is not empty, returns next item to be popped (but does not pop the item)
    #Step 2: If stack is empty, raises IndexError
    def peek(self):
        if self.num_items == 0:
            raise IndexError("Stack is empty")
        else:
            return self.items[self.num_items-1]

        
    #none --> int
    #Returns the number of items currently in the stack, not the capacity
    #Step 1: Return number of items currently in stack
    def size(self):
        return self.num_items



