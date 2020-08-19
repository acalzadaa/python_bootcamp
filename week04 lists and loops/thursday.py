# checking the number of items within a list
print("\nExercise 1 ---------------------")

nums = [5, 10, 15]
length = len(nums)
print(length)

# accessing specific items of a list with slices (start,stop,step)
print("\nExercise 2 ---------------------")

print(nums[1:3])
print(nums[:2])
print(nums[::2])
print(nums[-2:])

# adding an item to the back of a list using append
print("\nExercise 3 ---------------------")

nums = [10, 20]
nums.append(5)
print(nums)

# adding a value to the beginning of the list
print("\nExercise 4 ---------------------")

words = ["ball", "base"]
words.insert(0, "glove")
print(words)

# using pop to remove items and saving to a variable to use later
print("\nExercise 5 ---------------------")

items = [5, "ball", True, 44]
items.pop()
removed_item = items.pop()
print(removed_item, "\n", items)

# using the remove method with a try and except
print("\nExercise 6 ---------------------")

sports = ["baseball", "soccer", "football", "hockey"]
try:
    sports.remove("soccer")
except ValueError:
    print("the item doesn't exists")
print(sports)

# using min, max, and sum
print("\nExercise 7 ---------------------")

nums = [5,3,9]
print(min(nums))
print(max(nums))
print(sum(nums))

# using sorted on lists for numerical and alphabetical data
print("\nExercise 8 ---------------------")

nums = [5,8,0,2]
sorted_nums = sorted(nums)
print(nums, sorted_nums)

# sorting a list with .sort() in-place
print("\nExercise 9 ---------------------")

nums = [5,0,8,3]
nums.sort()
print(nums)

# using conditional statements on a list
print("\nExercise 10 ---------------------")

names=["jack", "robert", "mary"]
if "mary" in names:
    print("found")
if "jimmy" not in names:
    print("not found")

# using conditionals to see if a list is empty
print("\nExercise 11 ---------------------")

nums = []
if not nums:
    print("empty")

if nums == []:
    print("still empty")
    
# using a for loop to print all items in a list
print("\nExercise 11 ---------------------")

sports = [ "Baseball", "Hockey", "Football", "Basketball" ]
for sport in sports:
    print(sport)

# using the while loop to remove a certain value
print("\nExercise 12 ---------------------")

names = [ "Bob", "Jack", "Rob", "Bob", "Robert" ]

while "Bob" in names:
    names.remove("Bob")
print(names)

# Remove Duplicates: Remove all duplicates from the list below. 
# Hint: Use the .count( ) method. 
# The output should be [‘Bob’, ‘Kenny’, ‘Amanda’] 
# >>> names = ['Bob', 'Kenny', 'Amanda', 'Bob', 'Kenny']
print("\nExercise A ---------------------")

names = ['Bob', 'Kenny', 'Amanda', 'Bob', 'Kenny', 'Bob', 'Amanda', 'Elm', 'Epigeo']
unique = []
for name in names:
    if unique.count(name) == 0:
        unique.append(name)
print(unique)

# User Input: Use a while loop to continually ask the user to input a word, until 
# they type “quit ”. Once they type a word in, add it to a list. Once they quit the 
# loop, use a for loop to output all items within the list.
print("\nExercise B ---------------------")

quit = False
word = ''
words = []
while not quit:
    word = input("say a word!: ")
    if word.lower() == 'quit':
        quit = True
    else:
        words.append(word)
print(words)
    
    



