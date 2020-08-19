# *result* = [ *transform* *iteration* *filter* ]
# name_of_list = [ item_to_append for item in list]
# name_of_list = [ item_to_append for item in list if condition ]
# name_of_list = [ item_to_append if condition else item_to_append for item in list ]

# create a list of a hundred numbers using list comprehension
print("create a list of a hundred numbers using list comprehension")
nums = [ x for x in range(100)]
print(nums)

# create a list of ten even numbers using list comprehension
print("create a list of ten even numbers using list comprehension")
nums = [ x for x in range(10) if x%2 == 0]
print(nums)

# create a list of ten numbers sorted by odd or even
print("create a list of ten numbers sorted by odd or even")
nums = [ f"Even {x}" if x%2 == 0 else f"Odd {x}" for x in range(10)]
print(nums)

# create a list of 5 numbers squared
print("create a list of 5 numbers squared")
nums = [1,2,3,4,5]
squared_nums = [num**2 for num in nums]
print(squared_nums)

# creating a dictionary of even numbers and square values using comprehension
print("creating a dictionary of even numbers and square values using comprehension")
numbers = [x for x in range(50)]
squares = {num : num **2 for num in numbers if num % 2 == 0}
print(squares)

# Degree Conversion: Using list comprehension, convert the following list to 
# Fahrenheit. Currently, the degrees are in Celsius temperatures. The conversion 
# formula is “(9/5) * C + 32”. Your output should be [ 53.6, 69.8, 59, 89.6 ].
# 
# >>> degrees = [ 12, 21, 15, 32 ]

print("Exercise 1 - Temp convertion")
celsious = [ 12, 21, 15, 32 ]
farenheit = [((temp*(9/5))+32) for temp in celsious ]
print(farenheit)

print("Exercise 2 - Divisible values")
number = int(input("Tell me a number: "))
response = [num for num in range(number, 101) if num % number == 0]
print(response)

# esto es equivalente a: 
# response = []
# for n in range(number, 101):
#    if(n % number == 0):
#        print(f"{n}: es divisible")
#        response.append(n)
#    else:
#        print(f"{n}: No es divisible")