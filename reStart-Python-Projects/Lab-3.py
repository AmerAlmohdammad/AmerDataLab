mySring = "This is a string. "
print(mySring)
print(type(mySring))
print(mySring + "is of the data type " + str(type(mySring)))

firstString = "Water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
print("welcome to this lab " + name)

color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))
print(name,',' "you like a", color + animal)