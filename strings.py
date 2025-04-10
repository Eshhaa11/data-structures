#STRINGS

"""
-> Python offers a variety of built-in string methods for manipulating strings
"""

message = "Hello, greetings from Rift Koders, We are busy typing code"
message.lower() #Converts to lowercase
message.upper() #Converts to uppercase
message.split(", ") #Splits comma into separated text

#CHECKING CONTENT
print("greetings" in message)
print(message.startswith("Hello"))

#STRIPPING WHITESPACE

msg = " Hello "
msg.strip()

#REPLACE
message.replace("Hello", "Yellow")

#COUNT AND FIND

message.count("are") # Counts the number of times the substring appears
message.find("code") # Finds the first occurrence of the substring

#STRING FORMATTING

name = "Joseph"
print(f"Hello, {name}")
