# Lambda functions, otherwise known as anonymous functions, 
# are one-line functions within 
# >>> lambda arguments : expression
# >>> lambda arguments : value_to_return if condition else value_to_return

# Using a Lambda

# using a lambda to square a number
print( ( lambda x : x**2) (4) )

# Passing Multiple Arguments

# passing multiple arguments into a lambda
print( (lambda x, y  : x * y) (2,3))

# Saving Lambda Functions

# saving a lambda function into a variable
square = lambda x,y : x*y
print(square)
result = square(4,6)
print(result)

#Conditional Statements

# using if/else statements within a lambda to return the greater number
greater = lambda x, y : x if x > y else y
result = greater(2,7)
print(result)

# Returning a Lambda

# returning a lambda function from another function

def my_func(n):
    return lambda x : x * n

doubler = my_func(2)
print(doubler(3))

tripler = my_func(3)
print(tripler(3))

# Fill in the Blanks: Fill in the blanks for the following code so that it takes in a
# parameter of “x” and returns “True” if it is greater than 50; otherwise, it should
# return “False”:
# >>> ____ x _ True if x _ 50 ____ False

print("Exercise 1")
def greater_than_50(n):
    return  (lambda x : "True" if x > 50 else "False")(n) 

print(greater_than_50(51))

# Degree Conversion: Write a lambda function that takes in a degree value in
# Celsius and returns the degree converted into Fahrenheit.

print("Exercise 2")

def celsius_to_fahrenheit(degrees):
    return (lambda x : (x*(9/5)+32))(degrees)

print(celsius_to_fahrenheit(40))