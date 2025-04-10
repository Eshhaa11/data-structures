# WHY DATA STRUCTURES MATTER

"""

= They organize, store and manage data in ways that make your program more efficient, readable, and powerful.
= Diffrent problems need diffrent way to store and retrieve data.
= Lists are a great way for ordered collection you change .
= Tuples are like lists but immutable, perfect for mixed data.
= Dictionaries gives you fast access to data using keys.
= Using the right data structures makes your code faster.
= Looking up at an item in a dictionary is much faster thab a searching list
= A set is great when  you want to remove duplicates
= Well chosen data structures make code easier to understand

 e.g.
   Instead of:
      names = ["Tilak", "Ansh", "Esha"]
      ages = [18, 18, 20]

    We can do this:
      students = {"Tilak": 18, "Ansh": 20, "Esha": 18}

-> Python data structures come with powerful built-in methods
-> Advanced data structures like queues, stacks, graphs and trees can be built using lists, dictionaries or classes. Understanding basic data structures prepares you for more complex ones


"""

#LISTS

"""
    Lists are ordered collections that contain elements of different data types
    Properties:
       * Ordered
       * Mutable
       * They allow duplicates

"""

names = ["Esha", "Tilak", "Saleh", "Vansh", "Ansh", "Natasha", "Ansh"]

#INDEXING

print(names[0]) #Esha

#SLICING

print(names[1:2]) #Tilak

#APPEND

names.append("Janet") #[Esha", "Tilak", "Saleh", "Vansh", "Ansh", "Natasha", "Ansh", "Janet"]

#INSERT

names.insert(1, "Joseph") #[Esha", "Joseph", "Tilak", "Saleh", "Vansh", "Ansh", "Natasha", "Ansh", "Janet"]

#REMOVE

names.remove(0)  #["Joseph", "Tilak", "Saleh", "Vansh", "Ansh", "Natasha", "Ansh", "Janet"]

#POP

last_item = names.pop()

#LOOPING

for name in names:
      print(name)\
      
#LENGTH

print(len(names))

#LIST METHODS

names.sort() #Sorts in ascending order
names.reverse() #reverses elements in list
