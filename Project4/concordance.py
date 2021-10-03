#Kelsey Nguyen
#CPE 202 Section 7
#Project 4


from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance


    #HashTable, string --> None
    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 251: self.stop_table = HashTable(251)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTableQuadPr(251)
        try:
            with open(filename) as f:
                read_data = f.read()
                for x in read_data:
                    self.stop_table.insert(x.strip(),1)
            f.close()
        except FileNotFoundError:
            raise FileNotFoundError


    #HashTable, string --> None        
    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 251: self.concordance_table = HashTable(251)
        If file does not exist, raise FileNotFoundError"""


    #HashTable, string --> None
    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
