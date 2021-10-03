# Kelsey Nguyen
# Section 07

# recursion implementation 
def max_list_rec(tlist):  
   """ finds the max of a list of numbers and returns it, not the index"""
   if (len(tlist) == 0):
       raise ValueError('empty list')
       """ finds the max of a list of numbers and returns it, not the index"""
   elif (len(tlist) == 1):
       return tlist[0]
   else:
       templist = tlist[1:len(tlist)]
       temp= max_list_rec(templist)
       return (max(tlist[0],temp))


# int list --> int
# Returns max of a list 
def max_list_iter(tlist):
# 1. If list is empty --> return erorr 
# 2. Initialize variable (largest) to first element in list
# 3. Loop through list
# 4. if largest is greater than element checked (x), set largest to x
# 5. return largest number
   if len(tlist) == 0:
      raise ValueError('empty list')
   largest = tlist[0]
   for x in tlist:
      if largest < x:
         largest = x
   return(largest)


# str --> str
# Reverses a string - recursion implementation
def reverse_rec(tempstr):  
# 1. Base condition: If length of string is 0, return string
# 2. If not equal to 0, call reverse_rec function, slice part of the string except the first letter, and concatenate first letter of string to the end of sliced string
   """ recursively reverses a string and returns it """
   if len(tempstr) == 0:
      return tempstr
   else:
      return reverse_rec(tempstr[1:]) + tempstr[0]

   


# int, int, int, int list --> int
# Binary Search - recursion implementattion
def bin_search(target, low, high, list_val): 
# 1. if length of list is empty, return None
# 2. elif the target is not in the list, return None
# 3. elif the bounds (low & high) are mixed, return an error
# 4. else, set mid to low + high and divide by 2 
   # 5. if target is equal to middle element --> return mid index
   # 6. elif target is greater than mid element, x lies in right half subarray after mid element --> recur for right half
   # 7. elif target is smaller than mid element, recur for left half
   """ searches for target in list_val[low..high] and returns index if found"""
   if len(list_val) == 0:
      return None
   elif target not in list_val:
      return None
   elif low > high:
      raise ValueError('Bound Errors')
   else:
      mid = (low + high) // 2 
      if target == list_val[mid]:
         return mid
      elif target < list_val[mid]:
         return bin_search(target, low, mid-1, list_val)
      else:
         return bin_search(target, mid+1, high, list_val)
   



 
   