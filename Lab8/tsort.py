#Kelsey Nguyen
#CPE 202 Section 7
#Lab 8

from sys import argv
from stack_array import *

#Class holds the vertex's in degree and vertices that the vertex is adjacent to for use with the topological sorting of a directed acyclic graph
class Graph:

    #a degree is a positive integer, representing the in-degree (number of incoming edges) of a vertex
    #an adjacency is a list, containing the specific vertices that the vertex is adjacent to
    def __init__(self):
        self.degree = 0
        self.adjacency = []

    #self, vertex (int) --> None
    #Adds an edge to graph
    def addEdge(self, vertex):
        self.adjacency.append(vertex)
        self.degree += 1



#list --> string
#Performs a topological sort of the specified directed acyclic graph. 

'''Step 1: Raise a value error if:
    - vertices is empty with the message "input contains no edges" by checking if length of vertices list is empty
    - vertices has an odd # of vertices (incomplete pair) with the message "input conatins an odd number of tokens" by 
      checking if vertices list contains an odd number of elements
    - the graph contains a cycle (isn't acyclic) with the message "input contains a cycle" by checking if there are any vertices 
      with an in degree of zero
    Step 2: Make an adjacency list
    Step 3: Make a for loop that starts at 0 and counts by 2
    Step 4: Store the adjacency list using a dictionary where the key is the string name of the vertex and the value is some
    structure to hold the vertex's in degree and vertices that the vertex is adjacent to (use class Graph above to store the in degree and vertices that the vertex is adjacent to)
    Step 5: Make a Stack Array
    Step 6: Create two empty lists
    Step 7: Make a for loop that loops through the adjacency list. The i represents each element (not the index) in the long dictionary
    Step 8: Append the in degrees of each vertex to the first empty list
    Step 9: Push all vertices with an in degree of zero onto the Stack
    Step 10: Append any vertices that do not have an in degree of zero to the second empty list
    Step 11: Compare the two lists. If the length of the first list is equal to the length of the second list (this list contains all in degrees except 0), raise ValueError "input contains a cycle"
    Step 12: Create a new empty string
    Step 13: While the stack is not empty, pop a vertex from the Stack and concatenate it to the empty string
    Step 14: Reduce the degree of the vertices that were adjacent to the just-popped vertex
    Step 15: If reducing the in degree of a vertex results in a value of 0, push the vertex onto the Stack. Return the string'''
def tsort(vertices):
    '''
    * The graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph. The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.'''


    adjacency_list = {}
    if len(vertices) == 0:
        raise ValueError("input contains no edges")
    if len(vertices) % 2 != 0:
        raise ValueError("input contains an odd number of tokens")

    for i in range(0,len(vertices),2):
        if vertices[i+1] not in adjacency_list.keys():
            adjacency_list[vertices[i+1]] = Graph()
        if vertices[i] not in adjacency_list.keys():
            adjacency_list[vertices[i]] = Graph()
        adjacency_list[vertices[i+1]].addEdge(vertices[i])
        
    myStack = StackArray(30)
    visited_zeros = []
    visited_non_zeros = []
    for i in adjacency_list:
        visited_zeros.append(adjacency_list[i].degree)
        if adjacency_list[i].degree == 0:
            myStack.push(i)
        else:
            visited_non_zeros.append(adjacency_list[i].degree)
    if len(visited_zeros) == len(visited_non_zeros):
        raise ValueError("input contains a cycle")
    
    result = ""
    while myStack.size() != 0:
        popped = myStack.pop()
        result = result + popped + "\n"
        for i in adjacency_list:
            if popped in adjacency_list[i].adjacency:
                adjacency_list[i].degree -= 1
                if adjacency_list[i].degree == 0:
                    myStack.push(i) 
    return result


    
def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()
    
    vertices = []
    for line in f:
        vertices += line.split()
       
    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)
    
if __name__ == '__main__': 
    main()
