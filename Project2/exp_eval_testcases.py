#Kelsey Nguyen
#CPE 202 Section 7
#Project 2

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval(self):
        self.assertEqual(postfix_eval("5 1 2 + 4 ^ + 3 -"), 83)
        self.assertEqual(postfix_eval("2 3 * 5 4 * + 9 -"), 17)
        self.assertEqual(postfix_eval("13 3 -"), 10)
        self.assertEqual(postfix_eval("4 5 +"), 9)
        self.assertEqual(postfix_eval("100 5 *"), 500)
        self.assertEqual(postfix_eval("3 1 /"), 3.0)
        self.assertEqual(postfix_eval("4 2 ^"), 16)
        self.assertEqual(postfix_eval("1 2 + 3 *"), 9)
        
    def test_postfix_eval_insufficient_operands1(self):
        try:
            postfix_eval("9 -")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
        with self.assertRaises(PostfixFormatException):
            postfix_eval('3 4 + 2 / +')
    
    def test_postfix_eval_insufficient_operands2(self):
        try:
            postfix_eval("1 2 + 3 * *")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_too_many_operands(self):
        try:
            postfix_eval("1 2 3 4 + +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
        with self.assertRaises(PostfixFormatException):
            postfix_eval('10 8 / 2')

        
    def test_postfix_eval_divide_by_zero(self):
        with self.assertRaises(ValueError):
            postfix_eval('1 0 /')
        with self.assertRaises(ValueError):
            postfix_eval('8 3 - 0 /')
        with self.assertRaises(ValueError):
            postfix_eval("9 0 /")
        with self.assertRaises(ValueError):
            postfix_eval("100 12 + 0 /")

    def test_postfix_eval_invalid_token(self):
        try:
            postfix_eval("")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")
        

    def test_evaluateMe(self):
        self.assertEqual(evaluateMe("+", 18, 5), 23)
        self.assertEqual(evaluateMe("+", 2, 3), 5)
        self.assertEqual(evaluateMe("-", 5, 5), 0)
        self.assertEqual(evaluateMe("-", 30, 12), 18)
        self.assertEqual(evaluateMe("*", 10, 9), 90)
        self.assertEqual(evaluateMe("*", 5, 4), 20)
        self.assertEqual(evaluateMe("/", 12, 4), 3)
        self.assertEqual(evaluateMe("/", 100, 10), 10)
        self.assertEqual(evaluateMe("^", 5, 3), 125)
        self.assertEqual(evaluateMe("^", 6, 2), 36)

    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"), "3 4 2 * 1 5 - 2 3 ^ ^ / +") 
        self.assertEqual(infix_to_postfix("1 + 4"), "1 4 +")
        self.assertEqual(infix_to_postfix("6 * ( 8 + 2 )"), "6 8 2 + *")
        self.assertEqual(infix_to_postfix("2 + 2 * 5"), "2 2 5 * +")
        self.assertEqual(infix_to_postfix("1 * ( 2 + 3 )"), "1 2 3 + *")

    def test_left(self):
        self.assertTrue(left("-", "+"))
        self.assertFalse(left("^", "-"))
        self.assertTrue(left("+", "*"))
        self.assertFalse(left("^", "/"))
    
    def test_right(self):
        self.assertFalse(right("^", "/"))
        self.assertFalse(right("-", "+"))
        self.assertFalse(right("*", "^"))
        self.assertFalse(right("^", "^"))

    def test_getPrecedence(self):
        self.assertEqual(getPrecedence("^"), 3)
        self.assertEqual(getPrecedence("*"), 2)
        self.assertEqual(getPrecedence("/"), 2)
        self.assertEqual(getPrecedence("+"), 1)
        self.assertEqual(getPrecedence("-"), 1)
        self.assertEqual(getPrecedence("**"), 0)

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("* + 3 2 1"), "3 2 + 1 *")
        self.assertEqual(prefix_to_postfix("+ + 8 * 4 1 9"), "8 4 1 * + 9 +")
        self.assertEqual(prefix_to_postfix("+ * 6 7 * 9 8"), "6 7 * 9 8 * +")
        self.assertEqual(prefix_to_postfix("+ + + 1 2 3 4"), "1 2 + 3 + 4 +")



  

	


		

if __name__ == "__main__":
    unittest.main()