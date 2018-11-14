import unittest
import types

from CA5 import add, divide, exponent, reduceMultiply, multiply, subtract, subtractLambda, squared, cubed, odd, even, factorial, mean, decimalFractionGenerator

class CalculatorTest(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(4, add(2, 2))
        self.assertEqual(5, add(5, 0))
        self.assertEqual(1, add(2, -1))
        #self.assertRaises(ValueError, add, 'Two','Three') #Test to ensure Value Error is raised if non numerics are entered

    def testDivide(self):
        self.assertEqual([5,2,3], divide([10,4,6],[2,2,2])) #new test to check list input and output
        self.assertEqual([5], divide([5], [1]))
        self.assertIsInstance(divide([4.5],[4.2]), list) #Checks that a float is returned
        self.assertRaises(TypeError, divide, 'a','b') #Checks a type error is raised if strings are used
        self.assertEqual('Cannot divide by Zero', divide(5, 0)) #Test that checks "Cannot divide by Zero"mesage is displayed
  
    def testExponent(self):
        self.assertEqual([4, 64,1296], exponent([2,4,6], [2,3,4])) # new test to check list input and output
        self.assertEqual([32], exponent([2], [5]))
        self.assertRaises(TypeError, exponent("two", "one")) #Checks type eror is raised if non numerics used
        self.assertEqual("Value entered is not numeric", exponent("two", "one"))#Checks error message is being returend
        self.assertEqual([2], exponent([4], [0.5]))
        self.assertEqual([1], exponent([2], [0]))
        self.assertEqual([0.125], exponent([2],[-3]))
        self.assertEqual([0], exponent([0], [2]))
        
    def testMultiply(self):   #Simple Tests to check multiplication answers
         self.assertEqual([20,90,18,8], multiply([5,10,6,4], [4,9,3,2]))#new test to check you can multiply lists
         self.assertEqual([0], multiply([5], [0]))
         self.assertEqual([5], multiply([5], [1]))
         self.assertRaises(TypeError, multiply(['a'],['b'])) #Checks a type error is raised if strings are used
         self.assertEqual("Value entered is not numeric", multiply(["two"], ["one"]))#Checks error message is being returend
    
    def testReduceMultiply(self):   #Simple Tests to check multiplication answers
         self.assertEqual(24, reduceMultiply([1,2,3,4]))
         self.assertRaises(TypeError, reduceMultiply(['a','b']))
         
    def testSubtract(self):
         self.assertEqual([1, 1, 3, 2], subtract([5,10,6,4],[4,9,3,2]))  #testing I can subtract lists
         self.assertEqual([0], subtract([2], [2]))     #Simple tests to check subtraction answers
         self.assertEqual(5, subtractLambda(5, 0))      #testing the simple lambda function
         self.assertEqual(-1, subtractLambda(2, 3))
         self.assertEqual(0.5, subtractLambda(1,0.5))
         self.assertAlmostEqual(0.1, subtractLambda(0.5,0.4)) 
         
    def testSquared(self):
         self.assertIsInstance(squared([1,2,3,4]), types.GeneratorType)
         square = squared([2,4,6,8,10])
         self.assertEqual(4, next(square))
         self.assertEqual(16, next(square))
         self.assertEqual(36, next(square))
         self.assertEqual(64, next(square))
         self.assertEqual(100, next(square))
         
         
    def testCube(self):
        self.assertEqual(0.027,cubed(0.3))   #simple tests to check return value is correct
        self.assertEqual(27,cubed(3))
        self.assertEqual(-27,cubed(-3))
        self.assertEqual(0,cubed(0))
        
    def testOddandEven(self):                   #test to check the filter odd and even functions
        self.assertEqual([1, 3, 5, 7, 9], odd([0,1,2,3,4,5,6,7,8,9,10]))
        self.assertEqual([0, 2,4,6,8,10], even([0,1,2,3,4,5,6,7,8,9,10]))
        
    def testFactorial(self):
         self.assertEqual(6, factorial(3))
         self.assertEqual(1, factorial(1))
         self.assertEqual("The factorial of 0 is 1", factorial(0)) #checks on screen message is displaying correctly
         self.assertEqual(120, factorial(5))
         self.assertEqual("Sorry, factorial does not exist for negative numbers", factorial(-5)) #checks message is raised when a negative number is entered


    def testMean(self):
         self.assertEqual(4, mean(5,4,3))                #simple tests on mean values returned
         self.assertEqual(5, mean(9,8,7,6,5,4,3,2,1))
         self.assertEqual(0.6, mean(0.4,0.6,0.8))
         
    def testDecimalFraction(self):
         self.assertIsInstance(decimalFractionGenerator([1,2,3,4]), types.GeneratorType)
         decimalFractions = decimalFractionGenerator([2,4])
         self.assertEqual(0.5, next(decimalFractions))
         self.assertEqual(0.25, next(decimalFractions))
        
         
if __name__ == "__main__":        
    unittest.main()     
      
#         
#     
# =============================================================================

