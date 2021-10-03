#Kelsey Nguyen
#CPE 202 Section 7
#Lab3


#Class creates nodes of linked list
#data (item)
#item (none)
class Node:
    #constructor initializes node
    def __init__(self, data):
        self.data = data    #Assign data/value stored in the node
        self.next = None    #The reference pointer to the next node - Initializes next as null

#Implements an efficient last-in first-out Abstract Data Type using a Linked List
class StackLinked:
    #a capacity is an int
    #item is a list
    #num_items is an int

    
    #Creates and empty stack with a capacity
    def __init__(self, capacity):
        self.capacity = capacity    #capacity is the static size of stack
        self.head = None        #head represents the beginning node of the list
        self.num_items = 0      #number of elements in the stack
        
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
        if self.is_full():
            raise IndexError("Stack is full")
        else:
            self.num_items += 1
            newnode = Node(item)
            newnode.next = self.head
            self.head = newnode 

    #none --> int
    #Removes element that is the current head (item in the beginning of the stack)
    #Step 1: If stack is not empty, pops item from stack and returns item.
    #Step 2: If stack is empty when pop is attempted, raise IndexError
    def pop(self): 
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            self.num_items -= 1
            popped_node = self.head
            self.head = self.head.next
            return popped_node.data

    #none --> int
    #Returns the head node data/item in the beginning of the stack
    #Step 1: If stack is not empty, returns next item to be popped (but does not pop the item)
    #Step 2: If stack is empty, raises IndexError
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.head.data

    #none --> int
    #Returns the number of items currently in the stack, not the capacity
    #Step 1: Return number of items currently in stack
    def size(self):
        return self.num_items


