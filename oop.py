#OBJECT ORIENTED PROGRAMMING
"""
-> OOP is a programming paradigm that organizes code around objects rather than functions or procedures.
-> Objects are instances of classes, which act as blueprints defining the properties(data) and behaviors (function/methods) of those objects
-> OOP models real world entities, making code more intuitive and modular
"""
#CONCEPTS OF OOP
"""
-> Classes and objects
  * A class is a template and an object is an instance of that class
-> Encapsulation
  * Building data (attributes) and methods (functions) within a class, controlling access to protect data integrity
-> Inheritance
  * A class can inherit attributes and methods from another class promoting code reuse
-> Polymorphism
  * Objects of different classes can be treated as objects of a common base class, allowing flexibility.
-> Abstraction
  * Hiding complex implementation details and exposing only neccessary features to the user
"""

#BENEFITS OF OOP
"""
# MODULARITY
-> Code is organized into classes, making it easier to manage and update
# RE-USABILITY
-> Inheritance and polymorphism allow code to be reused across projects
# SCALABILITY
-> OOP suits large, complex systems by breaking them into manageable pieces
# MAINTAINABILITY
-> Encapsulation isolates changes reducing bugs and simplifyinng debugging
# REAL-WORLD MODELLING
-> OOP mimics real-world relationships, making system intuitive to design and understand
"""
#DEFINING CLASSES & CREATING OBJECTS

"""
-> A class is created using the class keyword, and objects are created by instantiating the class
-> You can create an object by calling the class like a function
"""
class Cat:
    def meow(self): #simple method
        return "meow"
#Create objects/instances
cat1 = Cat()
cat2 = Cat()
#Calling the meow method
cat1.meow()
cat2.meow()
"""
->Cat 1 and 2 are objects
-> Each objects can access the classes methods independently

"""

# ATTRIBUTES AND METHODS WITHIN CLASSES

"""
-> Attributes
 * Variable that store data specific to an object or class
-> Methods
 * Functions defined inside a class that describe the behavior of objects
"""

#ATTRIBUTES

"""
-> Attributes can be:
a) Instance attributes: Unique to each object, defined using self in the init method
b) Class attributes: Shared across all objects of the class, defined directly in the class body

-> The _init_ method:
* A special method(constructor) called when an object is created, used to initialize instance attributes
"""
class Dog:
    #Species attribute shared by all dogs
    species = "German Shepherd"
    def __init__(self, name, age):
        self.name = name #instance attribute unique to each dog
        self.age = age
dog1 = Dog("Simba", 2)
dog2 = Dog("Bruno", 5)
"""
-> Species is a class attribute, same for all dogs
-> name and age are instances attributes,

"""
#METHODS

"""
Methods are functions defined in a class
They typically take self as the first parameter to access 
"""


