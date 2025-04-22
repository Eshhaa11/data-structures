#MULTIPLE INHERITACNE METHOD RESOLUTION ORDER (MRO)
"""
-> Multiple resolution allows a class to inherit from more than one parent class, combining their attributes and methods
-> MRO determines the order in which python searches for methods and attributes in a class hierachy
-> Python uses the C3 linearization algorithm to create a consistent, predictable order
** How it works:
  -> When you call a method on an object, python looks for it in the class and then follows the MRO
     to parent classes
  -> The MRO is computed to avoid ambiguity ensuring each class is visited only once and respecting the inheritance hierachy

"""
#PITFALLS AND BEST PRACTICES
"""
-> Diamond Problem: When two parent classes inherit from a common base class, leading to potential
ambiguity
-> Complexity: Multiple inheritance can make code hard to follow. Prefer composition using objects as attributes unless multiple inheritcance in clearly justified.
-> Explicit super() usage: in complex hierachies, super() can behave unexpectedly unless you understand the MRO. Always check __MRO__ when debugging

"""