#Creating & Calling Functions

# def functionName( parameters ) : <- defining function
# functionName() <- calling function

# writing your first function
def printInfo():
    print("Name: John Smith")
    print("Age: 45")

printInfo()
printInfo()
    
# performing a calculation in a function

def calc(a, b):
    print(f"El resultado es: {a+b}")
calc(5,2)

# Print Name: Define a function called myName, ale
# and have it print out your name when called.

def myName(name):
    print(f"Hello {name}!")

name= input("What's your name? : ")
myName(name)

# Pizza Toppings: Define a function that prints out all your favorite pizza toppings 
# called pizzaToppings. Call the function three times.

def pizzaToppings(ingredients):
    print("you like your pizza with: ")
    for ingredient in ingredients:
        print(f"-{ingredient}")

ingredients = ["queso", "pimientos", "tomate", "champiñones"]
pizzaToppings(ingredients)
        
