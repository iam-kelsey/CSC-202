#Kelsey Nguyen
#CPE 202 Section 7
#Lab6 - BST


from queue_array import QueueArray

#A node is presenting an item
#Class creates node for use with a binary search tree
class TreeNode:

    #constructor initializes node
    #a key is a positive integer, representing the key value in the tree
    #an item is a value based on the given type
    #a left is a reference point to the left child/subtree 
    #a right is a reference point to the right child/subtree
    #a root is a positive integer, representing the topmost node in the tree
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.root = None



#BinarySearchTree is a representation of a binary search tree, a node-based binary tree data structure
#This class has a reference to the class TreeNode that is the root of the binary search tree
#Implements a binary search tree, with the left subtree containing keys that are less than the parent and the right subtree containing trees that are greater than the parent
class BinarySearchTree:

    #constructor creates an empty binary search tree
    #self --> BST
    def __init__(self): # Returns empty BST
        self.root = None

    #BST --> boolean
    #Checks to see if BST is empty
    #Step 1: Returns True if tree is empty, False otherwise
    def is_empty(self): # returns True if tree is empty, else False
        return self.root == None

    #BST, int --> boolean
    #Searches for the given key in a node of the tree
    #Step 1: While root is not none and key doesn't already exist, compare inserting element with root
    #Step 2: If key is less than root, make root left
    #Step 3: If key is greater than root, make root right
    #Step 4: Return True if key is in node of the tree, False otherwise
    def search(self, key):
        temp = self.root
        while (temp != None) and (temp.key != key): 
            if key < temp.key:
                temp = temp.left
            else:
                temp = temp.right
        if temp == None:
            return False
        else:
            return True
       

    #BST, int, data  -->  None
    #Inserts new node with key and data
    #Step 1: Make new node with the key and data that were passed
    #Step 2: If passed key is > than key in the currrent node, change current node to the right node
    #Step 3: If passed key is < than key in current node, change current node to the left node
    #Step 4: If passed key is < than key in current node and there is no left child, put current node there
    #Step 5: If passed key is > than key in current node and there is no right child, put current node there
    #Step 6: If passed key is < than key in current node and passed key is > than the key of the current node's left and current node has no right child, put node as right child
    #Step 7: If passed key is > than key in current node and passed key is < than the key of the current node's right and current node has no left child, put node as left child
    #Step 8: Otherwise if the passed key and key in current node are equal, update to new data
    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data if tree is empty
        temp = TreeNode(key, data)
        current = self.root
        if self.root == None:
            self.root = temp
            return
        while current.key != temp.key:
            if temp.key < current.key and current.left == None:
                current.left = temp
            elif temp.key > current.key and current.right == None:
                current.right = temp
            elif temp.key < current.key and temp.key > current.left.key and current.left.right == None:
                current.left.right = temp
            elif temp.key > current.key and temp.key < current.right.key and current.right.left == None:
                current.right.left = temp
            if temp.key < current.key:
                current = current.left
            if temp.key > current.key:
                current = current.right
        current.data = temp.data

                


    #BST --> tuple
    #Returns a tuple with min key and data in the BST
    #Step 1: If tree is empty, return None
    #Step 2: Since the minimum valued key in a BST is the leftmost child of the tree, 
            #follow the left references in each node of the subtree until it reaches a node that does not have a left child
    #Step 3: Return tuple with the minimum key and data
    def find_min(self): 
        temp = self.root
        if temp == None:
            return None
        while (temp.left != None):
            temp = temp.left
        tup1 = (temp.key, temp.data)
        return tup1


    #BST --> tuple
    #Returns a tuple with max key and data in the BST
    #Step 1: If tree is empty, return None
    #Step 2: Since the maximum valued key in a BST is the leftmost child of the tree, 
            #follow the right references in each node of the subtree until it reaches a node that does not have a right child
    #Step 3: Return tuple with the maximum key and data 
    def find_max(self):
        temp = self.root
        if temp == None:
            return None
        while (temp.right != None):
            temp = temp.right
        tup1 = (temp.key, temp.data)
        return tup1

    #BST --> int
    #Returns the height of the tree. Calls getHeight() method in class TreeNode 
    #Step 1: If tree is empty, return None
    #Step 2: Call helper function, tree_height_helper
        #Step 3: In the helper function, if there is a right child and no left child, return height of right + 1
        #Step 4: if there is a left child and no right chikd, return height of left + 1
        #Step 5: If there are no right or left children, return 1
        #Step 6: Otherwise, return the max between the height of the left and the height of the right
    #Step 7: Subtract 1 from height of root node and return it
    def tree_height(self):
        temp = self.root
        if temp == None:
            return None

        #node --> int
        #Helper function that recursively searches from the root to the deepest node in the tree
        def tree_height_helper(temp):
            if temp.left == None and temp.right != None:
                return tree_height_helper(temp.right) + 1
            if temp.left != None and temp.right == None:
                return tree_height_helper(temp.left) + 1
            if temp.left == None and temp.right == None:
                return 1
            x = 1 + tree_height_helper(temp.left)
            y = 1 + tree_height_helper(temp.right)
            if x >= y:
                return x
            else:
                return y
        return tree_height_helper(temp) - 1


    #BST --> list
    #Return Python list of BST keys representing in-order traversal of BST
    #Step 1: Make empty list
    #Step 2: Make helper function that recursively traverses through left and right subtrees
    #Step 3: Append the key of current node to the list
    #Step 4: Return list of keys
    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        lst = []
        if self.root == None:
            return None
    
        #node --> None
        #Helper function that recusively traverses through tree and append keys to the list
        def inorder_list_helper(node):
            if node != None:
                inorder_list_helper(node.left)
                lst.append(node.key)
                inorder_list_helper(node.right)
        inorder_list_helper(self.root)
        return lst



    #BST --> list
    #Returns Python list of BST keys representing pre-order traversal of BST
    #Step 1: Create empty list
    #Step 2: Call helper function that takes in a root. This helper function recursively traverses through left and right subtrees
        #Step 3: Append the key of current node to the list
    #Step 4: Have base case that returns current key as list for when there is no children
    #Step 5: Return list of keys 
    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        lst = []
        temp = self.root
        if temp == None:
            return None

        #Node --> None
        #Helper function that recursively traverses through tree and append keys to list
        def preorder_list_helper(node):
            if node != None:
                lst.append(node.key)
                preorder_list_helper(node.left)
                preorder_list_helper(node.right)
        preorder_list_helper(temp)
        return lst
        

    #BST --> list
    #Return Python list of BST keys representing level-order traversal of BST
    #Step 1: Create empty list
    #Step 2: If tree is empty, return None
    #Step 3: Create a variable and make it equal to 1
    #Step 4: Append key of node to list
    #Step 5: While the variable is less than or equal to 2 times the height of tree:
        #Step 6: Make count variable equal to the variable equal to 1
        #Step 7: While count variable is greater than 0, if queue is empty, break out of loop
        #Step 8: Dequeue and append left and right children to the list
        #Step 9: Subtract the count variable by 1
        #Step 10: When the new variable is equal to 0, make the first variable equal to 2 times its current size
    def level_order_list(self):  
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = QueueArray(25000) # Don't change this!
        lst = []
        if self.root == None:
            return None
        first_variable = 1 
        q.enqueue(self.root)
        lst.append(self.root.key)
        while first_variable <= 2 * (self.tree_height()):
            second_varaible = first_variable 
            while second_varaible > 0:
                if q.num_items == 0:
                    break
                temp = q.dequeue()
                temp1 = temp.left
                temp2 = temp.right
                if temp1 != None:
                    lst.append(temp1.key)
                    q.enqueue(temp1)
                if temp2 != None:
                    lst.append(temp2.key)
                    q.enqueue(temp2)
                second_varaible -= 1
            first_variable = 2 * first_variable
        return lst
        

