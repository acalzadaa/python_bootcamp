# where global variables can be accessed
number = 5
def scopetest():
    print("hola") # number += 1
scopetest()

# accessing variables defined in a function
def scopetest2():
    word = "function"
    return word
value = scopetest2()
print(value)

# changing list item values by index
sports = [ "baseball", "football", "hockey", "basketball" ]

def change(alist):
    alist[0] = "soccer"
print(f"Before altering: {sports}")
change(sports)
print(f"After Altering: {sports}")

# Names: Create a function that will change the list passed in with a parameter 
# of name at a given index. 
# Such that if I were to pass in “Bill” and index 1, it would change “Rich” to “Bill.” 
# Use the list and function definition in the following:
# >>> names = ['Bob', 'Rich', 'Amanda'] 
# >>> def changeValue(aList, name, index):

names = ['Bob', 'Rich', 'Amanda'] 
def changevalue(alist, name, index):
    alist[index] = name
print(names)
changevalue(names, "Alex", 0)
print(names)
changevalue(names, "Conny", 1)
print(names)
changevalue(names, "Sam", 2)
print(names)