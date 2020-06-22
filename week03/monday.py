# accepting and outputting user input
print(input("What's your name?"))

ans = input("What city do you live in?")
print(f"Hello {ans.upper()}!")

# how to check the data type of a variable
num = 5
print( type(num))

num = "2"
num = int(num)
print(type(num))

# working with user input to perform calculations
ans = input("type a number to add to 100: ")
print(type(ans)) #default is a string must convert to int
result = 100 + int(ans)
print(f"100 + {ans} = {result}")

# handling errors using the try and except block
try:
    ans = float(input("Type a number to add: "))
    print(f"100 + {ans} = {100+ans}")
except:
    print("Hey Only Numbers!")
# without try/except print statement would no get hit if error occurs
print("the program didn't break")

