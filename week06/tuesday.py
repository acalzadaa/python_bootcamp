# Tuesday: Working with Dictionaries

#Adding New Information

# adding new key/value pairs to a dictionary
car = {"year" : 2018}
car["color"] = "Blue"
print(f'year {car["year"]} , color {car["color"]}')

#Changing Information

# updating a value for a key/value pair that already exists
car["color"] = "Red"
print(f'year {car["year"]} , color {car["color"]}')

#Deleting Information

# deleting a key/value pair from a dictionary
try:
    del car["year"]
    print(car)
except:
    print("That key doesnt exist")
    
#Looping a Dictionary

for key in car.keys():
    print(key)
    print(car[key])

#Looping Only Values

for value in car.values():
    print(value)
    
#Looping Key-Value Pairs

for key, value in car.items():
    print(f"{key} : {value}")    
    
#TUESDAY EXERCISES

# User Input: Declare an empty dictionary. Ask the user for their name, address, 
# and number. Add that information to the dictionary and iterate over it to show 
# the user.

root = dict()
exit_code = False
index = 0
while not exit_code:
    index += 1
    name = input("What's your name?: ")
    address = input("what's your address?: ")
    phone = input("what's your number?: ")
    
    element = dict()
    element["name"] = name
    element["address"] = address
    element["phone"] = int(phone)
    element_name = "element" + str(index)
    root[element_name] = element
    ans = input("Exit (y/n)?: ").lower()
    if ans == "y":
        exit_code = True
        
print("Show the Dictionary!")
for elem in root.keys():
    print(elem)
    print(root[elem])
    print(root[elem]["name"])
    print(root[elem]["address"])
    print(root[elem]["phone"])

# Problem-Solving: What is wrong with the following code: 
# >>> person = { 'name', 'John Smith' } 
# >>> print(person['name'])

person = { 'name' : 'John Smith' } 
print(person['name'])

# Remember that adding and altering key-value pairs are the same syntax.

