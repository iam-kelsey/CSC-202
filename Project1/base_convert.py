#Kelsey Nguyen
#CPE 202 Section 7
#Project 1

#int (number), int (base) --> str
#Recursive function that returns a string representing num in the base b
def convert(num, b):
#Step 1: Make string variable (digits, in this case) that allows user to index into a table of characters to support bases greater than 10
#Step 2: Base condition - if num is less than b, convert single digit number to a string using a lookup (digits) & append to list
    #Step 3: Concatenate number in list to a string and return the concatenated string
#Step 4: Else, let x be equal to the recursive call (convert function) + the string representation of the reaminder
    #Step 5: Append x to list
    #Step 6: Concatenate numbers in list to a string and return the concatenated string

    digits = "0123456789ABCDEF"        #string variable holding a sequence of characters to represent digits past 9
    recur_lst = []      #recur_lst represents an empty list
    remainder = num%b   #remainder variable represents the remainder num%b
    if num < b:         #base case
        recur_lst.append(digits[num])
        return "".join(recur_lst)
    else:
        x = convert(num // b, b) + digits[remainder]
        recur_lst.append(x)
        return "".join(recur_lst)


