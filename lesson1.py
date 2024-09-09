# print statement displays text in the console
# speechmarks around words means string (string of characters)
print("hello world")

# we assign a string "Mr Davies" to a variable
name = "Mr Davies"

# umm so basically, the input the user types to the question "what is your name" will be assigned to the name variable.
name = input("what is your name? ")

# if statement, if the condition is true, then do the code below
# double equals check for equality
if name == "Mr Davies":
    print("no not you!?!")
elif name == "Louis Leung": # elif: it is just a combination of else and if
    print("please no, very sus")
else: # if anything else do this!
    print("welcome", name) # two parameters (two things in the brackets!)
    print("welcome " + name) # concatenation, joining together two strings, using the + symbol
    print(f"Welcome {name}") # format strings, use of f before a string, then use of curly brackets inside the string to put variables or math or other things...
