# FUNCTIONS

"""
= A function is a reusable block of code that performs a specific task.
= Functions can take parameters (inputs) to work with data and can return values (outputs) to provide results.
= Functions in python are defined using the def keyword and can take parameters.
"""
def greet(name):
    return (f"Hello, {Vansh}!")
greet("Vansh")

"""
= Parameters are variables listed in the function defination that act as placeholder for the values (arguments) 
passed to the function when it is called.
= Return value is the value a function sends back to the caller using the return statement, if no return statement is 
specified, the function returns None by default
"""
def add_sum(a, b): #parameters a and b
    result = a + b
    return result # results the sum of a and b
#calling the function
add_sum(10, 20) #arguments 10 and 20
"""
= above
    * a,b are parameters
    * 10,12 are arguments (actual values passed to the function)
= The function returns result which stores the sun of  a and b
"""

# DEFAULT PARAMETERS
def greetUser(name="Guest"): # default parameter value set to name variable
    print(f"Greetings {name}")
greetUser() # Greetings, Guest
greetUser("Joseph") #Greetings Joseph

"""
= Functions can habve multiple return values, often as a tuple.
"""

def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder 
q, r = divide_and_remainder(10, 3)
print(q,r)

"""
= Parameters allow flexibility by letting functions work together with diffrent inputs.
= The return statement sends a value back, without it, the functions returns None.
= You can call a function anywhere in your code ( after defining it) and uses its return value.
"""

#FUNCTION SCOPE, GLOBAL VS LOCAL VARIABLES
"""
= Variables declared inside a function are local to that function.
= They exist within the function and are destroyed whewn the function finishes executing.
= They cannot be accessed outside the fucntion.
"""

def calculate_area(length, width):
    area = length * width # local variable area
    return area
print(calculate_area(10,12))
#print(area) # error "area" is not defined (it's local to the function)
#area is local and cannot be accessed outside the function

#  GLOBAL VARIABLES
"""
= variables declared outside any function are global
= they are accessible throughout the entire program, including inside functions (unless shadowed by a local variable)
= they cab be read inside functions by modifying them requires the global keywords
"""

count = 0
def increment():
    global count # declare count as a global to modify it
    count += 1
increment()
print (count) # 1

"""
= without global count, trying to modify count inside the function would create a new local variable insted, leading to 
an erroe or unexpected behaviour
"""
x = 5
def my_function():
    x = 10
    print ("inside function", x)
my_function()
print ("outside function", x)

"""

-> The local x doesnt affect the global x
-> To modify a variable inside a function use the global keyword
-> For nested functions, nonlocal keyword
"""

def outer() :
    x= 'outer'
    def inner ():
        nonlocal x
        x = "inner"
    inner()
    print(x)
outer() #output = inner

"""
-> Local variables are confined to their function and disappear after execution
-> Global  variables are accessible everywhere but should be modified carefully to avoid confusion
-> Use global to modfiy global variables inside functions, use nonlocal,for outer scope variables in nested functions
-> avoid overusing global variables, as they can make code harder to debug and maintain, prefer using parameters and passing return values
-> use parametersto make functions reusable and return values to communicate results
-> be mindful of where variables are defined , use local variables for temporary data within functions and global variables sparingly for shared data
-> IF A VARIABLE ISNT WORKING AS EXPECTED, CHECK ITS SCOPE(LOCAL) VS GLOBAL AND WETHER ITS BEING SHADOWED
"""
