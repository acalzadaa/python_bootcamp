# writing your first for loop using range,
# COUNTS UP TO... BUT NOT INCLUDING
print("1st Exercise ---------------------")

for num in range(5):
    print(f"Value: {num}")

# providing the start, stop, and step for the range function
print("2nd Exercise ---------------------")
for num in range(2, 10, 2):
    print(f"Value: {num}")

# printing all characters in a name using the 'in' keyword
print("3rd Exercise ---------------------")
name = "John Smith"
for letter in name:
    print(f"Value: {letter}")

# using the continue statement within a foor loop
print("4th Exercise ---------------------")
for num in range(5):
    if num == 3:
        continue
    print(num)

# breaking out of a loop using the 'break' keyword
print("5th Exercise ---------------------")
for num in range(5):
    if num == 3:
        break
    print(num)

# setting a placeholder using the 'pass' keyword
print("6th Exercise ---------------------")
for i in range(5):
    # TODO: add code to print number
    pass

# Divisible by Three:
# Write a for loop that prints out all numbers from 1 to 100
# that are divisible by three.
print("Test 1 Exercise ---------------------")

for num in range(100):
    if num % 3 == 0:
        print(num)


# Only Vowels: Ask for user input, and write a for loop
# that will output all the vowels within it.
# For example:
# >>> "Hello" ➔ "eo"
print("Test 2 Exercise ---------------------")

vowels = ["a", "e", "i", "o", "u"]
word = input("Dime una palabra: ")
for letter in word:
    if letter in vowels:
        print(letter)
        
