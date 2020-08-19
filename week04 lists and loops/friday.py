# Pyramids: Use a for loop to build a pyramid of x’s. It should be
# modular so that if you loop to 5 or 50, it still creates evenly spaced
# rows.
# Hint: Multiply the string “x” by the row. For example, if you
# loop to the range of 4, it should produce the following result:
# >>>   x
# >>>  x x
# >>> x x x

ans = input("Your pyramid... how high?: ")
steps = int(ans)
print(steps)
for i in range(steps):
    index = i + 1
    x = list(index * "x")
    level = (" " * (steps - index)) + " ".join(x)
    print(level)

# Output Names: Write a loop that will iterate over a list of items
# and only output items which have letters inside of a string. Take
# the following list, for example, only “John” and “Amanda” should
# be output:
# >>> names = ['John', ' ', 'Amanda', 5]

exitFlag = False
elements = []
words = []
while not exitFlag:
    ans = input("Enter something or write quit to end: ")
    if(ans == "quit"):
        exitFlag = True
    else:        
        elements.append(ans)

for element in elements:
    if(element.isalpha()):
        words.append(element)
    
print(f"These are the only valid words {words}")

# Convert Celsius: Given a list of temperatures that are in Celsius, write
# a loop that iterates over the list and outputs the temperature converted
# into Fahrenheit.
# Hint: The conversion is “F = (9/5) ∗ C + 32”:
# >>> temps = [32, 12, 44, 29]
# Output would be [89.6, 53.6, 111.2, 84.2]

exitFlag = False
temps = []

while not exitFlag:
    ans = input("Enter a celsius temp or write quit to end: ")
    if(ans == "quit"):
        exitFlag = True
    else:        
        temps.append( (float(ans)*(9/5)) +32)

print(f"These are the temps in Fahrenheit: {temps}")