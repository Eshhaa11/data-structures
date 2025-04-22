#INHERITANCE

"""
->Inheritance allows a class (class/subclass) to inherit attributes and methods from another class (parent/superclass)
->This promotes code reuse and establishes a hierachial relationship

"""

class Parent:
    pass
class Child(Parent):
    pass


"""
-> The child class inherits all methods and attributes of the parent but can override or extend them 

"""

#POLYMORPHISM

"""
->Polymorphism (many forms) allows objects of different classes to be treated as objects of a commom parent classs
->Its often achieved by ovveriding methods in child classes, so each class can implement the same method differently.
** How it works:
-> Child classes ovveride parent method
-> You can call the same method on different objects and python executes the approproate version

"""

#ENCAPSULATION

"""
-> Encapsulation bundles data(attributes) and methods within a class and controls access to them
-> It hides internal details and protects data from unintended modifications using private attributes
**How it works:
->Public attributes/methods: indicated by a single underscore (e.g self.__name) a convention for dont touch
this unless youre a subclass
-> Private attributes/methods: indicated by double underscore (e.g self.__name) which triggers name mangling to prevent direct access outside the class
-> Use getters and setters to access or modify attributes safely.
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""