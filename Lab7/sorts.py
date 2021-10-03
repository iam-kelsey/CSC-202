#Kelsey Nguyen
#CPE 202 Section 7
#Lab 7 


import random
import time

#list --> int
#Sort an array of integers using selection sort and return the number of comparisons

#Step 1: Make a variable that keeps track of the number of comparisons
#Step 2: Make a for loop that starts at the length of list - 1 (second to last item in the list), stops at 0, and the step is -1
#Step 3: Make a variable that keeps track of the position of the largest value as it makes a pass
#Step 4: Make an inner for loop that starts at 1 and stops at the unsorted part of the list 
#Step 5: Add 1 to the number of comparison
#Step 6: Do a comparison to find the max item using an if statement. If we find something bigger, replace the position of the largest value with that
#Step 7: Return the number of comparisons
def selection_sort(lst):
    num = 0
    for x in range(len(lst)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, x+1):
            num += 1
            if lst[positionOfMax] < lst[location]:
                positionOfMax = location
        temp = lst[x]
        lst[x] = lst[positionOfMax]
        lst[positionOfMax] = temp
    return num


#list --> int
#Sort an array of integers using insertion sort and return the number of comparisons

#Step 1: Make a variable that keeps track of the number of comparisons
#Step 2: Make a for loop that starts at 1 and stops at the length of the list
#Step 3: Make a current value and set it equal to list in the current index position 
#Step 4: Create a position variable and set it equal the current index
#Step 5: Add 1 to the number of comparisons
#Step 6: Make a while loop that have the conditions -- if the value to the left is higher than the current value we're trying to sort and if current position is greater than 0
#Step 7: Go into the while loop and do the switch. Make list in the current position index equal to list in the position - 1 index
#Step 8: Continue doing comparisons down the list by saying the current position is equal to the current position - 1
#Step 9: Add 1 to the number of comparisons
#Step 10: Make an if statement that says if position is less than or equal to 0, subtract 1 from the number of comparisons. This is to fix the short-circuiting problem 
          #where in the while loop, if position is not greater than 0, it would not do the comparison but still incremement number of comparisons by 1
#Step 11: Make list in the current position index equal to the current value 
#Step 12: Return number of comparisons
def insertion_sort(lst):
    num = 0
    for x in range(1, len(lst)):
        currentValue = lst[x]
        position = x

        num += 1
        while position > 0 and (currentValue < lst[position-1]):
            lst[position] = lst[position -1]
            position = position - 1
            num += 1
        if position <= 0:
            num -= 1

        lst[position] = currentValue
    return num


   

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 9)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)




if __name__ == '__main__': 
    main()

