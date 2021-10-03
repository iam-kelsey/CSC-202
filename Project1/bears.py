#Kelsey Nguyen
#CPE 202 Section 7
#Project1

#int --> boolean
#A recursive function that returns True when it is possible to end up with exactly 42 bears by starting with n bears and False when it is not possible to end up with 42 bears
def bears(n):
#n represents number of bears

#Step 1: If number of bears (n) is equal to 42, return True
#Step 2: If number of bears (n) is less than 42, return False
#Step 3: Else if number of bears (n) is even OR divisble by 3, 4, or 5, execute following code
    #Step 4: If number of bears (n) is even, give back n/2 bears and call bears recursively on new number of bears
    #Step 5: If nuumber of bears (n) is divisible by 3 or 4, multiply last two digits of n and give back this many bears (return False if one or both of the digits are 0)
    #Step 6: IF number of bears (n) is divisible by 5, give back 42 bears (n-42) and call bears recursively on new number of bears
#Step 4: If number of bears (n) is not equal to 42, not less than 42, not even, and not divisible by 3, 4, or 5, return False
   
    if n == 42:     #base case
        return True     
    elif n < 42:
        return False
    elif (n%2 == 0 or n%3 == 0 or n%4 == 0 or n%5 == 0):
        if (n%2 == 0):
            if bears(n/2):
                return True
        if (n%3 == 0 or n%4 == 0):
            last_num = n%10            #this variable represents the last number in digit
            second_num = (n%100)//10    #this variable represents the second to last number
            if (last_num and second_num) != 0:
                if bears(n - last_num*second_num):
                    return True
            if (last_num or second_num) == 0:
                return False
        if (n%5 == 0):
            if bears(n-42):
                return True
    else:
        return False
        

    


        

            


