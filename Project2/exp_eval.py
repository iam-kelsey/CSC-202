#Kelsey Nguyen
#CPE 202 Section 7
#Project 2

from stack_array import StackArray

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

#string (postfix expression) --> int
#Step 1. Create a stack with a capacity of 30
#Step 2. Make a list containing the required operators
#Step 3. Split the postfix expression into a list
#Step 4. If the inputted postfix expression is empty, raise a RostfixFormatException error (invalid token)
#Step 5. Loop through each token in the split list
#Step 6. When an operand/value is encountered, push it onto the stack
#Step 7. When an operator is encountered, pop the required number of values from the stack
#Step 8. If size of the stack is less than 2, raise PostfixFormatException error (insufficient operands). Otherwise, perform the operation on the popped values using a helper function
#Step 9. Push the result back onto the stack
#Step 10. If size of stack is not equal to 1, raise a PostfixFormatException (too many operands)
#Step 11: Return the last value remaining on the stack
def postfix_eval(input_str):
    #This function evaluates a postfix expression with the help of a helper function, doMath(op, value1, value2)
    
    '''Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    MyStack = StackArray(30)
    operators = ['+', '-', '*', '/', '^']
    postfix = input_str.split()

    if (input_str == ""):
        raise PostfixFormatException("Invalid token")
    
    for token in postfix:
        if (token not in operators):
            MyStack.push(token)
        elif token in operators:
            if MyStack.size() < 2:
                raise PostfixFormatException("Insufficient operands")
            else:
                try:
                    value2 = MyStack.pop()
                    value1 = MyStack.pop()
                except IndexError:
                    raise PostfixFormatException("Insufficient operands")
                result = evaluateMe(token, float(value1), float(value2))
                MyStack.push(result)
        
    if MyStack.size() != 1:
        raise PostfixFormatException("Too many operands")
    return MyStack.pop()

#string, int, int --> int
#Step 1. If operator is "+", add the 2 values and return the result
#Step 2. If operator is "-", subtract the 2 values and return the result
#Step 3. If operator is "*", multiply the 2 values and return the result
#Step 4. If operator is "/", divide the 2 values and return the result
    #Step 5. If the denominator is 0, raise ValueError
#Step 6. If operator is "^", raise the first value to the power of the second value (i.e 5 raised to the 2nd power) and return the result
def evaluateMe(op, value1, value2):
    #A helper function that evaluates math expressions for postfix_eval. It takes in 2 values and performs the correct operation depending on the operator (+, -, *, /, ^)
    if op == '+':
        return value1 + value2
    elif op == '-':
        return value1 - value2
    elif op == '*':
        return value1 * value2
    elif op == '/':
        if value2 == 0:
            raise ValueError
        return value1 / value2
    elif op == '^':
        return value1**value2




#string (infix expression) --> string (postfix expression)
#Step 1. Make an empty list
#Step 2. Make an empty Stack with a capacity of 30
#Step 3. Make a list containing the required operators
#Step 4. Split the infix expression into a list
#Step 5. Loop through each token in the split list
#Step 6. When an operand/value is encountered, append the value to the empty list
#Step 7. When an opening parenthesis is encountered, push it onto the stack
#Step 8. When a closing parenthesis is encountered, pop operators off the stack and append them to 
        #the list until the top of stack is an opening parenthesis
#Step 9. Pop the opening parenthesis from the stack (but don't put it into the list)
#Step 10. When an operator, o1, is encountered:
    #Step 11. While there is an operator, o2, at the top of the stack and either o1 is left associative and its
    #precedence is <= o2, or o1 is right associative and its precedence is <= o2, pop o2 from the stack and append
    #it to the list. The associativity and precedence are deteremined by the two helper functions: left(o1, o2) and right(o1, o2)
#Step 12. Push o1 onto the stack
#Step 13. At the end of the infix expression, pop and append all remaining operators to the list
#Step 14. Join each operand and operator in the list and return the list
def infix_to_postfix(input_str):
    #Converts an infix expression to an equivalent postfix expression

    '''Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    result = []
    operators = ['+', '-', '*', '/', '^']
    MyStack = StackArray(30)
    postfix = input_str.split()
    
    for token in postfix:
        if (token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") or (token in "0123456789"):
            result.append(token)
        elif token in operators:
            if not MyStack.is_empty():
                top = MyStack.peek()
                while (top in operators) and ((left(token, top)) or (right(token, top))):
                    popped = MyStack.pop()
                    result.append(popped) 
                    top = MyStack.peek()
                MyStack.push(token)
            else:
                MyStack.push(token)
        elif token == "(":
            MyStack.push(token)
        elif token == ")":
            tokenpop = MyStack.pop()

            while tokenpop != "(":
                result.append(tokenpop)
                tokenpop = MyStack.pop()
                
    while not MyStack.is_empty():
        tokenpop = MyStack.pop()
        result.append(tokenpop) 

    return " ".join(result)

#string, string --> boolean
#Step 1. If operator, o1, is not equal to "^" (left associative) and its precedence (determined by helper funtion getPrecedence) is less than or equal to that of o2,
#return True. Otherwise, return False
def left(o1, o2):
    #A helper function that determines if an operator, o1, is left associative and has a precedence that is less than or equal to the precedence of
    #another operator, o2
    if (o1 != "^") and (getPrecedence(o1) <= getPrecedence(o2)):
        return True
    return False

#string, string --> boolean
#Step 1. If operator, o1, is "^" (right associative) and its precedence (determined by helper function getPrecedence) is less than the precedence of o2, 
#return True. Otherwise, return False
def right(o1, o2):
    #A helper function that determines if an operator, o1, is right associative and has a precedence that is less than the precedence of another operator, o2
    if (o1 == "^") and (getPrecedence(o1) < getPrecedence(o2)):
        return True
    return False

#string --> int
#Step 1: If the token is equal to "^", return 3
#Step 2: If the token is equal to "*" OR "/", return 2
#Step 3: If the token is equal to "+" OR "-", return 1
#Step 4: Else, return 0
def getPrecedence(token):
    #A helper function that determines the precedence of the operator (the higher the number, the higher the precedence)
    if token == "^":
        return 3
    elif (token == "*") or (token == "/"):
        return 2
    elif (token == "+") or (token == "-"):
        return 1
    else:
        return 0


#string (prefix expression) --> string (postfix expression)
#Step 1. Create an empty Stack with a capacity of 30
#Step 2. Reverse the prefix expression 
#Step 3. Split the infix expression into a list
#Step 4. Make a list containing the required operators
#Step 5. Loop through each token in the split list
#Step 6. When an operator is encountered and if the stack is not empty, pop two operands/strings from the stack
#Step 7. Create a string by concatenating the two operands/strings and the operator after them
#Step 8. Push the resultant string back to the stacl
#Step 9. Repeat the above steps until end of the prefix expression
#Step 10. Return whatever is left on the stack
def prefix_to_postfix(input_str):
    #Converts a prefix expression to an equivalent postfix expression
    
    '''Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    MyStack = StackArray(30)
    input_str = input_str[::-1]
    tokens = input_str.split()
    operators = ['+','-','*','/', '^']

    for x in tokens: 
        if x in operators:
            if not MyStack.is_empty():
                op1 = MyStack.pop()
                op2 = MyStack.pop()
                result = op1 + ' ' + op2 + ' ' + x
                MyStack.push(result)
            else:
                MyStack.push(x)
        else:
            MyStack.push(x)
    return MyStack.pop()

          







