#Kelsey Nguyen
#CPE 202 Section 7
#Lab4 - Queue

#Implements an array-based, efficient first-in first-out Abstract Data Type using a Python array (faked using a List)
#QueueArray is a representation of the array with fixed capacity
class QueueArray:
    #a capacity is a positive integer, representing size of Array
    #an items is an array of size capacity, which field by None
    #a num_items is a positive integer, representing number of items in the Array
    #front is a positive integer, representing where items in the queue are removed 
    #rear is a positive integer, representing where items in the queue are added

    #self, int --> QueueArray
    #Created an empty Queue with a capacity
    def __init__(self, capacity):
        self.front = 0          #front index of queue; items are removed from front
        self.rear = 0           #rear index of queue; items enter at rear of queue
        self.items = [None]*capacity    #intializing array for queue
        self.num_items = 0          #number of items in the queue array
        self.capacity = capacity    #capacity is the static size of the queue 

 
    #QueueArray --> boolean
    #Checks if queue is empty
    #Step 1. Returns True if the queue is empty, and False otherwise
    def is_empty(self):
        return self.num_items == 0

    #QueueArray --> boolean
    #Checks if queue is full
    #Step 1: Returns True if the queue is full, and False otherwise
    def is_full(self):
        return self.num_items == self.capacity


    #QueueArray --> item
    #Inserts an item into the back of the queue
    #Step 1: If Queue is not full, enqueues item on queue
    #Step 2: If Queue is full when enqueue is attempted, raise IndexError
    def enqueue(self, item):
        if self.num_items == self.capacity:
            raise IndexError("Queue is full")
        else:
            self.items[self.rear] = item
            if self.rear == (self.capacity - 1):
                self.rear = 0
            else:
                self.rear += 1
            self.num_items += 1

    #QueueArray --> item
    #Removes the least recently added item (front item)
    #Step 1: If Queue is not empty, dequeues item from queue and returns item
    #Step 2: If Queue is empty when dequeue is attempted, raise IndexError
    def dequeue(self):
        if self.num_items == 0:
            raise IndexError("Queue is empty")
        else:
            x = self.items[self.front]
            self.front = (self.front + 1) % (self.capacity)
            self.num_items -= 1
            return x 



    #QueueArray --> int
    #Returns the number of items currently in the queue, not the capacity
    #Step 1: Return number of items currently in queue
    def num_in_queue(self):
        return self.num_items

