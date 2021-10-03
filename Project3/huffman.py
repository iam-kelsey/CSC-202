#Kelsey Nguyen
#CPE 202 Section 7
#Project3 - Huffman Coding

from ordered_list import OrderedList

#Class creates nodes for use with binary tree
#Class represents either a leaf node or an internal node (including root node) of a Huffman tree
#A node is the presenting an item 
class HuffmanNode:

    #constructor initializes a node
    #a char is a positive integer, representing the ASCII character code value
    #a freq is a positive integer, representing an occurence count
    #a left is a positive integer, representing the left node of the Huffman tree
    #a right is a positive integer, representing the right node of the Huffman tree
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right
        
    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        return type(self) == type(other) and self.freq == other.freq and self.char == other.char and self.left == other.left and self.right == other.right
        
    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        return character_order(self, other)

    
#string --> list
#Opens a text file with a given file name (passed as a string) and returns a list of the frequency of occurrences of all the characters within that file
#Step 1: Create an empty list of size 256 to store the counts of occurences of characters. Intialize with 0's in the list so that if 
#the file passed is empty, it will return a list filled with 0's 
#Step 2: Open text file that was passed and read the content of the file
#Step 3: Make a for loop that loops through the characters in the file 
#Step 4: If the ascii value of the character is less than 256, make it the index of python list and add 1
#Step 5: Close the opened file
#Step 6: Return list 
def cnt_freq(filename):
    wordfreq = [0]*256
    try:
        with open(filename) as f:
                read_data = f.read()
                for x in read_data:
                    ascii_value = ord(x)
                    if ascii_value < 256:
                        wordfreq[ascii_value] += 1
        f.close()    
        return wordfreq
    except:
        raise FileNotFoundError


#node, node --> boolean
#Determines the order of the nodes in list of HuffmanNodes
#Step 1: If frequency of node "a" is equal to frequency of node "b", make another if statement that says if the ASCII value of the character
#in node "a" is smaller than that of node "b", return True
    #Step 2: Else if the ASCII value of character in node "a" is greater than character in node "b", return False
#Step 3: If frequency of node "a" is smaller than frequency of node "b", retun True
#Step 4: Else, return False
def character_order(a,b):
    if a.freq == b.freq:
        if a.char < b.char:
            return True
        elif a.char > b.char:
            return False
    elif a.freq < b.freq:
        return True
    else:
        return False

#list --> root node of Huffman tree (int)
#Create a Huffman tree for characters with non-zero frequency. Returns the root node of the Huffman tree
#Step 1: Create an OrderedList 
#Step 2: Make a for loop with a range of the length of the freqency list that was passed in
#Step 3: If 
#Step 4: While size of OrderedList is greater than 1, pop two nodes with the lowest fequency count from list
#Step 5: Add freqencies of the two popped nodes together
#Step 6: Get the char of the first popped node
#Step 7: Create a new HuffmanNode (parent node) using the char in Step 6 and the combined frequency of two popped nodes in Step 5
#Step 8: Make the first popped node (the one with the lowest frequency) the left child and the second popped node the right child
#Step 9: Insert the parent node, which has been created from the two nodes with the lowest frequency, into the list of sorted nodes
#Step 10: Continue to do this until there is a single node left in the list, which is the root node of the Huffman tree
#Step 11: Return the root node
def create_huff_tree(char_freq):

    t_list = OrderedList()

    for x in range(len(char_freq)):
        if char_freq[x] != 0:
            new_node = HuffmanNode(chr(x), char_freq[x])
            t_list.add(new_node)
    while t_list.size() > 1:
        first_node = t_list.pop(0)
        second_node = t_list.pop(0)
        combine_freq = first_node.freq + second_node.freq
        combine_char = first_node.char
        hufftree = HuffmanNode(combine_char, combine_freq)
        hufftree.left = first_node
        hufftree.right = second_node
        t_list.add(hufftree)
    return t_list.pop(0)


    

#Node --> list
#Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation as the index into the arrary, with the resulting Huffman code for that character stored at that location
    #Calls helper function (create_code_helper)
#Step 1: Initialize a Python list of strings that initally consists of 256 empty strings
#Step 2: Make an empty string
#Step 3: Call the helper function, create_code_helper, passing in the huffman tree, empty string, and Python list
#Step 4: Return Python list
def create_code(node):

    huffman_codes = [""]*256
    new_string = ""
    create_code_helper(node, new_string, huffman_codes)
    return huffman_codes


#node, string, list --> list
#Traverses through the huffman tree to find the leaves and gets the correct code of the character in the leaf
#Step 1: If there are no left or right child (reached the leaf), then use ASCII value of that node as index of Python list and make it equal to the empty string
    #Step 2: Return the Python list
#Step 3: Else, recursive call down node.left and node.right. Add "0" when we go left and "1" if we go right 
    #Step 4: Return the Python list 
def create_code_helper(node, new_code, huffman_codes):
    if (node.left == None) and (node.right == None):
        huffman_codes[ord(node.char)] = new_code
        return huffman_codes
    else:
        huffman_codes = create_code_helper(node.right, new_code + "1", huffman_codes)
        huffman_codes = create_code_helper(node.left, new_code + "0", huffman_codes)
        return huffman_codes


#list --> string
#Creates and returns a header of the output file
#Step 1: Create an empty string
#Step 2: Make a for loop with a range of 0-255
#Step 3: if frequency is greater than 0, concatenate the index (ascii value) + space + frequency of character to the empty list
#Step 4: Return empty string
def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list associated with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    
    empty_str = ""

    for x in range(256):
        if freqs[x] > 0:
            empty_str = empty_str + str(x) + " " + str(freqs[x]) + " "
    return empty_str[:-1]
        





#string, string --> string
#Encodes the input file and writes it out to an output file
#Step 1: Create a HuffmanTree by calling create_huff_tree and passing in the list of freqencies of the input file 
            #(which can be done by passing in the input file into cnt_feq)
#Step 2: Create codes by passing the HuffmanTree into create_code
#Step 3: Create the header by passing the list of frequencies of the input file into create_header
#Step 4: Declare a variable to open the out_file (output). Use "w" to write to the file
#Step 5: Try opening in_file (input) and then read the data in the file
    #Step 6: If the file is empty, write an empty file
    #Step 7: If the file is not empty, write the header on the first line. Then, skip a line
    #Step 8: Make a for loop that loops through the content. Write out the codes on the second line to the output file
#Step 6: If the in_file does not exist, raise FileNotFoundError
#Step 7: Close the in_file and out_file
def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''
    huff_tree = create_huff_tree(cnt_freq(in_file))
    huff_codes = create_code(huff_tree)
    huff_header = create_header(cnt_freq(in_file))

    output_file = open(out_file, "w")

    try:
        with open(in_file) as f:
            read_data = f.read()
            if not read_data:
                output_file.write("")       #write an empty file if input file is empty
            else:
                output_file.write(huff_header) 
                output_file.write("\n")
                for x in read_data:
                    output_file.write(str(huff_codes[ord(x)]))
    except:
        raise FileNotFoundError
    f.close()
    output_file.close()




















