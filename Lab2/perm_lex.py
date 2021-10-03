# CPE 202 Lab 2
# Kelsey Nguyen
# Section 07

#str --> list of strings
#This function generates all the permutations of the characters in a string in lexicographic order
def perm_gen_lex(word):
#1. if string is empty --> return an empty list
#2. if length of string is 1 --> return a list containing that string
#3. Loop through character posititions of the string containing the characters to be permuted
    #4. For each character of the strin --> remove the character and form a simpler string
    #5. Generate all permutations of simpler string recursively (call per_gen_lex func)
    #6. Add removed character to the front of each permutation of the simpler word
    #7. Append permutation to a list 
#8. Return newly constructed permutations

	lst_perm = []           #empty list
	if len(word) == 1:      #word is string
		return [word]
	if len(word) == 0:
		return []
	for x in word:
		removed_string = ""     #empty string
		for y in word:
			if(y != x):
				removed_string += y
		new_word = perm_gen_lex(removed_string)
		for j in new_word:
			lst_perm.append(x+j)
	return lst_perm