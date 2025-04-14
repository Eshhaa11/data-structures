#ARRAYS

"""
-> Arrays are fundamental data structures that store elements in a continous block of memory.
-> Each element in an array , is identified by an index, starting from 0.
-> Arrays provide constant time access to any elemtn using its index

LEY CHARACTERISTICS
->  Arrays can have a fixed size or be dynamic
-> In strict arrays, all elements must be of the same type, in  pythons lists, they can store elements of different types (integers, strings, objects) i.e Heterogenous
-> Elements are accessed using their index
-> Elements are stored next to each other in memory (Contigous Memory), allowing fast access but potentially costly when resizing
-> Lists can grow or shrink as needed by using methods like append() or pop()
-> Lists can have references to objects, not raw data, so they use more memory than traditional arrays.

HOW WE CAN IMPLEMENT ARRAYS IN PYTHON:

1. Lists: Dynamic, flexible and commonly used as array-like structures.
2. Array Module : Provides a more traditional array with a fixed type elements
3. Numpy Arrays : Specialized for numerical and scientific computing
"""
 #OPERATIONS ON LISTS
"""
-> Arrays support a variety of operations that allow you to manipulate and access data stored within them.
"""

#INITIALIZATION
"""
my_list = [] #empty list
my_list = [1,2,3,4,5] #list with intial elements

"""
#ACCESSING ELEMENTS

"""

-> Elements can be accessed using the index, with a time complexity of 0(1) - Constant time
"""
my_list[2] #3

#APPENDING ELEMENTS

my_list.append(6) #add 6 to the end of the list

#INSERTING ELEMENTS

"""
-> Inserting elements can be done at the beggining, end or any specified index in the array with a time complexity of 0(n)
/Linear Time for insertion at the beginning or middle, 0(1)/Constant time for insertionat the end (armotized)
"""
my_list.insert(1,1.3) #inserts 1.3 at index 1
#DELETING ELEMENTS
"""
->Deletion can be done fromthe beginning, end or any specified index in the array with a time complexity  of 0(n)
/Linear Time for insertion at the beginning or middle, 0(1)/Constant time for deletion from the end

"""
my_list.pop(1) #removes the element at index 1
my_list.pop() #removes last element in the array

#SLICING
my_list[1:3]

#TRAVERSING THE ARRAY/ITERATION

"""
-> Traversing involves accessing each element of the array sequentially with a time complexity of 0(n)
"""

#CODE FOR TRANVERSING



#SEARCHING ELEMENTS
"""
-> Searching the array can be done using linear search, or binary search(if the array is sorted)
-> Time complexity: 0(n) for linear search, 0(log n) for binary search

"""

#Python array module
"""
->The array module provides a clear implementation to traditional arrays, enforcing a single data type and using less memory than lists
-> Its used for scenarios requiring compact storage homogenous data like numerical processing
"""

#CHARACTERISTICS OF PYTHON ARRAY MODULE
"""
->Elements must be of specific type, defined using type codes.
-> Arrays are not truly fixed but reuire manual resizing
-> It stores raw data, not object references , making it memory efficient
-> It supports fewer operations than lists but its not optimized for basic array tasks
"""

#