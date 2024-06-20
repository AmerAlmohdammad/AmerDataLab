userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")
    
else:
    print("Please come back when you need to ship a package. Thank you.")

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    

# this is explaining the {}
# The format() method allows you to insert values into a string with placeholders {}.
name = "Alice"
age = 30
print("Hello, my name is {} and I am {} years old.".format(name, age))

# F-strings are a more concise way to format strings, introduced in Python 3.6.
# You prefix the string with f and place the variables inside {}
name = "Bob"
age = 25
print(f"Hello, my name is {name} and I am {age} years old.")



