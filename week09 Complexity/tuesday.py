#Tuesday: Decorators

#creating and applying our own decorator using the @ symbol
def decorator(func):
    def wrap():
        print("======")
        func()
        print("======")
    return wrap

@decorator
def print_name():
    print("John!")

print_name()

# creating a decorator that takes in parameters
def run_times(num):
    def wrap(func):
        for i in range(num):
            func()
    return wrap

@run_times(4)
def say_hello():
    print("Hello!")

# When passing an argument into a decorator, the function is automatically 
# run, so we do not need to call sayHello in this instance.

# creating a decorator for a function that accepts parameters

def birthday(func):
    def wrap(name, age):
        func(name, age+1)
    return wrap

@birthday
def celebrate(name, age):
    print(f"Happy birthday {name}, you are now {age}")

celebrate("Alex", 41)

# Exercise 1
# User Input: Create a decorator that will ask the user for a number, and run
# the function it is attached to only if the number is less than 100. The function
# should simply output “Less than 100”. Use the function declaration in the
# following: 
# >>> @decorator
# >>> def numbers( ):
# >>> print("Less than 100")

def decorator2(func):
    def wrap():
        ans = int(input("enter a number!: "))
        if ans < 100:
            func()
    return wrap
            

@decorator2
def numbers():
    print("Less than 100")

numbers()

#Exercise 2

# Creating a Route: Create a decorator that takes in a string as an argument with
# a wrap function that takes in func. Have the wrap function print out the string,
# and run the function passed in. The function passed in doesn’t need to do
# anything. In Flask, you can create a page by using decorators that accept a URL
# string. Use the function declaration in the following to start:

# >>> @route("/index")
# >>> def index( ):
# >>> print("This is how web pages are made in Flask")

def route(name):
    def wrap(func):
        if(name == "/index"):
            func()
    return wrap

@route("/index")
def index():
    print("This is how web pages are made in Flask")