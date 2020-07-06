# passing a single parameter into a function

def printName(fullName):
    print(f"your name is {fullName}")
    
printName("Alex")
printName("chido")

# passing multiple parameters into a function
def addNums(num1, num2):
    result = num1 + num2
    print(f"{num1} + {num2} = {num1+num2}")
    
addNums(44,12)

# using a function to square all information

numbers1 = [ 2, 4, 5, 10 ]
numbers2 = [ 1, 3, 6 ]

def squares(nums):
    for num in nums:
        print(f"{num**2}")
    
squares(numbers1)
squares(numbers2)

# setting default parameter values

def calcArea(r, pi=3.1415):
    area = pi *(r**2)
    print(f"Area: {area}")
    
calcArea(3)

# setting default parameter values

def printName(first, last, middle = "."):
    print(f"{first} {middle} {last}")

printName("alex", "calzada", "algravez")
printName("alex", "calzada")
    
# *args
# using args parameter to take in a tuple of arbitrary values

def outputData(name, *args):
    print(type(args))
    for arg in args:
        print(arg)

outputData("alex", 5, True, "Elemental")

# **kwargs

# using kwargs parameter to take in a dictionary of arbitrary values

def outputData(**kwargs):
    print(type(kwargs))
    print(kwargs["name"])
    print(kwargs["num"])
outputData(name = "John Smith", num = 5, b = True)

# User Input: Ask the user to input a word, and pass that word into a function 
# that checks if the word starts with an uppercase. If it does output “True”, 
# otherwise “False”.

word = input("Enter a word: ")
def checkUpperCase(word):
    if word[0].isupper():
        print("True")
    else: 
        print("False")
checkUpperCase(word)

# No Name: Define a function that takes in two arguments, first_name and last_ 
# name, and makes both optional. If no values are passed into the parameters, it 
# should output “No name passed in”; otherwise, it should print out the name.

name1 = input("write a name: ")
name2 = input("write another name: ")

def namesPassed(name1="", name2=""):
    if(len(name1) == 0 and len(name2)==0):
        print("No name passed in")
    else:
        print(f"{name1}, {name2}")

namesPassed(name1, name2)