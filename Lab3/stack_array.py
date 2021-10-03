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



def hash(s):
    return ord(s[0])


def main():
    q = QueueArray(5)
    MyStack = StackArray(5)
    MyQueue.enqueue('A')

    MyQueue.enqueue('B')

    MyStack.push(MyQueue.dequeue())

    MyQueue.enqueue('C')

    MyStack.push('D')

    MyQueue.enqueue(MyStack.pop())

    MyStack.push(MyQueue.dequeue())

    print(MyStack.pop())
    print(MyQueue.dequeue())


    

   





if __name__ == '__main__':
   main()



