from functools import reduce    #Need to import this to use reduce
# =============================================================================
# def add(first, second):
#      number_types = (int,  float, complex) #allowed number tyoes for the function
#      if isinstance(first, number_types) and isinstance(second, number_types): #checks number input is allowed
#          return first + second #if input is allowed we will do the addition
#      else:
#          raise ValueError #if input is not allowed we will reaise a Value Error
#      return first + second
# =============================================================================
###############(1) Rewriting the add function using Lambda##########################
add = lambda first,second: first+second   #Rewrote Add Function using lambda
print(add(2,3))


############################################################################################################### =============================================================================
# def divide(first, second):   
#     if second == 0:     #checking if second number entered is 0
#         return 'Cannot divide by Zero'
#     return first / second #if second number is not  we perform the addition
# =============================================================================

########################(2)Using List Comprehension to divide two lists by each other#########################
# =============================================================================
def divide(first,second):               #I have used the function layout so I can reuse my tests
    if second == 0:     #checking if second number entered is 0
        return 'Cannot divide by Zero' 
    return [x/y for x,y in zip(first,second)]#I needed to use zip to produce a list of the saae size
    
# ===============######This is how I would implement it without putting it in a function:=================================================
listDivide1 = [10,8,6]          #creating two lists of numbers
listDivide2 = [2,4,3]

answerDivide = [x/y for x,y in zip(listDivide1,listDivide2)]#I needed to use zip to produce a list of the smae size
print(type(answerDivide))
print(answerDivide)

##############################################################################################################

# =============================================================================
# def exponent(first, second):
#     try:                            #try except block of code
#         return first ** second
#     except TypeError:               #if non numerics entered the exception is raised
#         return "Value entered is not numeric"
# =============================================================================
#######################(3)  Rewriting Exponent Function using list comprehension############################### 
#-=================Below is how I would write it without putting it in a fucntion
exponent1 = [2,4,6]
exponent2 = [2,3,4]    
exponentAnswer = [x**y for x,y in zip(exponent1,exponent2)]
print(exponentAnswer)   

#----------------------------Putting it in the function from CA1 so I can reuse the tests
def exponent(first, second):
    try:                            #try except block of code
        return [x**y for x,y in zip(first,second)]
    except TypeError:               #if non numerics entered the exception is raised
        return "Value entered is not numeric"


##############################################################################################################
# =============================================================================
def multiply(first, second):
     try:
         multiplyLambda = lambda first, second: first*second  #multiply formula using lambda
         return list(map(multiplyLambda, nosToMultiply1, nosToMultiply2))   #casting map output to a list
     except TypeError:
         return "Value entered is not numeric"
     

def multiply2(listToReduce):
     try:
         ReduceMultiply = reduce(lambda first,second: first*second, [1,2,3,4])
         return ReduceMultiply
     except TypeError:
         return "Value entered is not numeric"
# =============================================================================
    
#####################(4)    Rewriting the Multiply function to reduce a list of numbers###########################    
ReduceMultiply = reduce(lambda first,second: first*second, [1,2,3,4]) #for python 3 we ust ise functools.reduce
print("Reducer:")
print(ReduceMultiply)
print("Break!")


#########Rewriting thge Multiply function using map and lambda to multiply two lists and keep list format###############
nosToMultiply1 = [5,10,6,4] #list of first numbers
nosToMultiply2 = [4,9,3,2]  #list of second numbers
multiplyLambda = lambda first, second: first*second  #multiply formula using lambda
for i in map(multiplyLambda, nosToMultiply1, nosToMultiply2):   #using map without list
    print(i)
##############################################################################################################    
# =============================================================================
# =============================================================================
# def subtract(first, second):
#      return first - second
# =============================================================================

#################Rewriting Subtraction function below####################        
nosToSubtract1 = [5,10,6,4] #list of first numbers
nosToSubtract2 = [4,9,3,2]  #lst of second numbers
subtract = lambda first, second: first - second  #subtraction formula using lambda
Subtraction = list(map(subtract, nosToSubtract1, nosToSubtract2))   #using list,map  and lambda to subtracts list 2 from list 1
print(Subtraction)
##############################################################################################################
##############################################################################################################
def squared(number):
    number_types = (int, float)
    if isinstance(number, number_types):    #checks that only ints or floats are allowed
        return number*number
    else:
        raise ValueError
###############Using Map and List below to call existing squared function from CA1###################
numbersToSquare = [2,4,6,8,10] #list of numbers to pass in to squared function                 
Squared= list(map(squared, numbersToSquare))#using map to pass in a list of numbers to square. In Python 3 you must use list with map
print(Squared)
##############################################################################################################

# =============================================================================
# def cube(number):           #simple cube function
#     return number*number*number
# =============================================================================

################Rewriting Cube function below##########################################################   
cubed = lambda x: x*x*x  #using lamda to rewrite the cubed fuction
print(cubed(3))
##############################################################################################################


###################An Example of how you would use the Filter Function################################
#The filter() function in Python takes in a function and a list as arguments.
# This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True. 
#Here is a small program that returns the odd and even numbers from an input list:

numberList = [0,1,2,3,4,5,6,7,8,9,10]
odd_numbers = list(filter(lambda x: x%2, numberList))
even_numbers = list(filter(lambda x: x%2==0, numberList)) 
print(odd_numbers)
print(even_numbers) 
##############################################################################################################
##############################################################################################################

def factorial(number):      #simple factorial function
    factorial = 1           
    if number < 0:          #checks numbered eneterd
        return("Sorry, factorial does not exist for negative numbers")
    elif number == 0:
        return("The factorial of 0 is 1")
    else:
       for i in range(1,number + 1):    #for loop range specifies
           factorial = (factorial*i)        
    #print("The factorial of",str(number),"is",str(factorial))
    return factorial

########################Using Map to call existing factorial function and pass in a list of numbers###########
factorialList = [5,4,3,2,1,0]
for i in map(factorial, factorialList):
    print(i)
#########################################################################################################


def mean(*numbers):     #simple function to calculate mean, unlimited numbers allowed
    return sum(numbers)/len(numbers)    #uses the sum function to add numbers and len function to know how many are entered



def decimalFraction(number): #simple function that copies the 1/x button on the calculator
    if number != 0:
        return 1/number
    else:
        raise ZeroDivisionError #Zero Divison error if 0 entered


def decimalFractionGenerator():
    for x in range(1,10):
        yield 1/x

new_generator = decimalFractionGenerator()
for each in new_generator:
    print(each)

    

