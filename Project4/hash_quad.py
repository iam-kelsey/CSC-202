#Kelsey Nguyen
#CPE 202 Section 7
#Project 4

#Implements a Hash Table
class HashTableQuadPr:

    #Constructor creates and initializes the hash table size to size 
    #table_size is a positive integer, representing the initial table size of the HashTable
    #hash_table is a list, representing the hash table
    #num_items is a positive integer, representing the number of items in the hash empty 
    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table


    #Inserts an entry into the hash table (using Horner hash function to determine index and quadratic probing to resolve collisions)
    #HashTable, string, int --> None
    def insert(self, key, value):
        '''The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first 
        line number in the list of line numbers. If the key is in the table, then the value is appended to that 
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1).'''
        index = self.horner_hash(key)
        i = 0
        if value != None:
            while (self.hash_table[index] is not None) and (self.hash_table[index][0] is not key):
                i += 1
                index = (i ** 2 + index)%self.table_size

            if self.hash_table[index] == None:
                self.hash_table[index] = (key, [value])
                self.num_items += 1
            if (value not in self.hash_table[index][1]) and (self.hash_table[index][0] == key):
                self.hash_table[index][1].append(value)
        else:
            while self.hash_table[index] != None:
                if self.hash_table[index] == None:
                    self.hash_table[index + (i ** 2)] = (key, [value])
                    self.num_items += 1



    #Compute and return an integer from 0 to the (size of the hash table) - 1. Compute the hash value by using Horner's rule
    #HashTable, string --> int
    def horner_hash(self, key):
        n = 0
        if len(key) > 8:            #find min
            n = 8
        else:
            n = len(key)

        value = 0
        for x in range(n):          
            value = (ord(key[x])) + (31*value)       #compute hash value
        return value % self.table_size
            
    #Returns True if key is in an entry of the hash table, False otherwise
    #HashTable, string --> boolean
    def in_table(self, key):
        entry = self.get_index(key)
        if entry != None:
            return True
        else:
            return False

    #Returns the index of the hash table entry containing the provided key. Returns None if there is not an entry with the provided key
    #HashTable, string --> int
    def get_index(self, key):
        pos = self.horner_hash(key)
        i = tmp = 0

        found = False
        while self.hash_table[pos + (i ** 2) - tmp] != None:
            new_pos = pos + (i**2) % self.table_size
            if self.hash_table[new_pos][0] == key:
                found = True
            else:
                found = False
            i += 1
            if (pos + (i ** 2)) - tmp >= self.table_size:
                tmp = tmp + self.table_size
        if found == True:
            return new_pos
        else:
            return None
            


    #Returns a Python list of all keys in the hash table
    #HashTable --> list
    def get_all_keys(self):
        keys = [i[0] for i in self.hash_table if i != None]
        return keys


    #Returns the value (list of line numbers) associated with the key
    #HashTable, string --> list
    def get_value(self, key):
        if self.get_index(key) != None:
            return self.hash_table[self.get_index(key)][1]
        else:
            return None
        
    #Returns the number of entries (words) in the table
    #HashTable --> int
    def get_num_items(self):
        return self.num_items

    #Returns the size of the hash table
    #HashTable --> int 
    def get_table_size(self):
        return self.table_size

    #Returns the load factor of the has table 
    #HashTable --> int
    def get_load_factor(self):
        return self.num_items / self.table_size
