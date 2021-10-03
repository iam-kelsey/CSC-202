#Kelsey Nguyen
#CPE 202 Section 7
#Lab4 - Queue
 

#Class creates nodes of linked list
#A node is the presenting an item
class Node:
    #constructor initializes node
    

    #an item is a value based on the given type
    #a next is the reference pointer to the next node 
    def __init__(self, item):
        self.item = item   #Assign data/value stored in the node
        self.next = None  

#Implements an link-based,efficient first-in first-out Abstract Data Type
#Queuelinked is a representation of the list with fixed capacity
class QueueLinked:
    #a capacity is a positive integer, representing size of queue
    #a num_items is a positive integer, representing number of items in queue
    #front is a positive integer, representing where items in the queue are removed
    #rear is a positive integer, representing where items in the queue are added
    
    #self, int --> QueueList
    #Creates an empty queue with a capacity
    def __init__(self, capacity):
        self.front = None        
        self.rear = None          
        self.num_items = 0        
        self.capacity = capacity   



    #QueueLinked (list) --> boolean
    #Checks if queue is empty
    #Step 1. Returns True if the queue is empty, and False otherwise
    def is_empty(self):
        return self.num_items == 0

    #QueueLinked (List) --> boolean
    #Checks if queue is full
    #Step 1: Returns True if the queue is full, and False otherwise
    def is_full(self):
        return self.num_items == self.capacity

    #QueueLinked (List) --> item
    #Inserts an item into the back of the queue
    #Step 1: If Queue is not full, enqueues item on queue. 
    #Step 2: If Queue is full when enqueue is attempted, raise IndexError
    def enqueue(self, item):
        if self.num_items == self.capacity:
            raise IndexError("Queue is full")
        if self.num_items == 0:
            new_node = Node(item)
            self.front = new_node
            self.rear = new_node
            self.num_items += 1
        else:
            new_node = Node(item)
            self.rear.next = new_node
            self.rear = new_node
            self.num_items += 1
        
        
    #QueueLinked (List) --> item
    #Removes the least recently added item (front item)
    #Step 1: If Queue is not empty, dequeues item from queue and returns item.
    #Step 2: If Queue is empty when dequeue is attempted, raise IndexError
    def dequeue(self):
        if self.num_items == 0:
            raise IndexError("Queue is empty")
        else:
            temp = self.front.item
            self.front = self.front.next
            self.num_items -= 1
            return temp
            

    #QueueLinked (List) --> int
    #Returns the number of items currently in the queue, not the capacity
    #Step 1: Return number of items currently in queue     
    def num_in_queue(self):
        return self.num_items
