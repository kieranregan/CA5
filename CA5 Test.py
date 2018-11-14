import unittest

from CA5 import add ,answerDivide#, exponent, multiply, subtract, squared, cube, factorial, mean, decimalFraction

class CalculatorTest(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(4, add(2, 2))
        self.assertEqual(5, add(5, 0))
        self.assertEqual(1, add(2, -1))
        #self.assertRaises(ValueError, add, 'Two','Three') #Test to ensure Value Error is raised if non numerics are entered

    def testDivide(self):
         assert all([x/y for x,y in zip(listDivide1,listDivide2)])
         self.assertEqual([5,2,3], answerDivide([10,4,6]),([2,2,2]))
# =============================================================================
#          self.assertEqual(4, divide(2, 0.5))
#          self.assertEqual(5, divide(5, 1))
#          self.assertIsInstance(divide(4.5,4.2), float) #Checks that a float is returned
#          self.assertRaises(TypeError, divide, 'a','b') #Checks a type error is raised if strings are used
#          self.assertEqual('Cannot divide by Zero', divide(5, 0)) #Test that checks "Cannot divide by Zero"mesage is displayed
# =============================================================================
# 
#     def testExponent(self):
#         self.assertEqual(32, exponent(2, 5))
#         self.assertRaises(TypeError, exponent("two", "one")) #Checks type eror is raised if non numerics used
#         self.assertEqual("Value entered is not numeric", exponent("two", "one"))#Checks error message is being returend
#         self.assertEqual(2, exponent(4, 0.5))
#         self.assertEqual(1, exponent(2, 0))
#         self.assertEqual(0.125, exponent(2,-3))
#         self.assertEqual(0, exponent(0, 2))
#         
#     def testMultiply(self):
#         self.assertEqual(4, multiply(2, 2))     #Simple Tests to check multiplication answers
#         self.assertEqual(0, multiply(5, 0))
#         self.assertEqual(5, multiply(5, 1))
#         self.assertRaises(TypeError, multiply('a','b')) #Checks a type error is raised if strings are used
#         self.assertEqual("Value entered is not numeric", multiply("two", "one"))#Checks error message is being returend
#         
#     def testSubtract(self):
#         self.assertEqual(0, subtract(2, 2))     #Simple tests to check subtraction answers
#         self.assertEqual(5, subtract(5, 0))
#         self.assertEqual(-1, subtract(2, 3))
#         self.assertEqual(0.5, subtract(1,0.5))
#         self.assertAlmostEqual(0.1, subtract(0.5,0.4))  #I had to use alnost equal as floats were giving me 0.9999
#         
#     def testSquared(self):
#         self.assertEqual(25, squared(5))
#         self.assertEqual(16,squared(-4.0))
#         self.assertRaises(ValueError, squared, 'Five') #test that value error is raised if type entered is not float or int
#         
#     def testCube(self):
#         self.assertEqual(0.027,cube(0.3))   #simple tests to check return value is correct
#         self.assertEqual(27,cube(3))
#         self.assertEqual(-27,cube(-3))
#         self.assertEqual(0,cube(0))
#         
#     def testFactorial(self):
#         self.assertEqual(6, factorial(3))
#         self.assertEqual(1, factorial(1))
#         self.assertEqual("The factorial of 0 is 1", factorial(0)) #checks on screen message is displaying correctly
#         self.assertEqual(120, factorial(5))
#         self.assertEqual("Sorry, factorial does not exist for negative numbers", factorial(-5)) #checks message is raised when a negative number is entered
#     
#     def testMean(self):
#         self.assertEqual(4, mean(5,4,3))                #simple tests on mean values returned
#         self.assertEqual(5, mean(9,8,7,6,5,4,3,2,1))
#         self.assertEqual(0.6, mean(0.4,0.6,0.8))
#         
#     def testDecimalFraction(self):
#         self.assertEqual(0.5, decimalFraction(2))
#         self.assertEqual(0.2, decimalFraction(subtract(10,5))) #test using two functions subtract and decimal fraction
#         self.assertRaises(ZeroDivisionError, decimalFraction, 0) #Test that zerodivison error will be raised
# =============================================================================

if __name__ == "__main__":
    unittest.main() 