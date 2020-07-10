# Return Statement

def addNums(num1, num2):
    return num1 + num2

num = addNums(3, 4)
print(num)

# Ternary Operator
# shorthand syntax using a ternary operator

def searchList(aList, el):
    return True if el in aList else False

result = searchList(["one", 2, "three"], 3)
print(f"deberia ser falso: {result}")

result = searchList(["one", 2, "three"], 2)
print(f"deberia ser verdadero: {result}")

# Full Name: Create a function that takes in a first and last name 
# and returns the two names joined together.

def joinNames(firstName, lastName):
    return firstName + " " + lastName

print(joinNames("Alex", "Calzada"))

# User Input: Within a function, ask for user input. 
# Have this function return that input to be stored in a variable outside of the function. 
# Then print out the input.

def returnTheInput():
    return input("Write a word!: ")

print(returnTheInput())

