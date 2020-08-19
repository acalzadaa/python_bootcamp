# Monday: Dictionaries

# declaring a dictionary variable

# empty dictionary
empty = {}
empty_dict = dict()

# dictionary with one key/value pair
person = { "name": "John Smith"}

# dictionary with two key/value pairs
customer = { "name": "Morty", "age": 26}

print(person)
print(customer)

# Accessing Dictionary Information

# accessing dictionary information through keys
print(person["name"])

# Using the Get Method

print(person.get("name"))
print(person.get("address","Not Available"))

# Dictionaries with Lists

# storing a dictionary within a list and accessing it

data = [ "John", "Dennis", { "name": "Kirsten" } ]
print(data[2]) 
print(data[2]["name"])

# Dictionaries with Dictionaries

# storing a dictionary within a dictionary and accessing it

data = {
    "team" : "Boston Red Sox",
    "wins" : { "2018" : 108, "2017" : 93}
}

print(data["wins"])
print(data["wins"]["2018"])

# Creating a Dictionary

# User Input: Ask the user for their name and age, and then create a dictionary
# with those key-value pairs. Output the dictionary once created.

root = dict()
exit_code = False
index = 0
while not exit_code:
    index += 1
    name = input("What's your name?: ")
    age = input("How old are you?: ")
    element = dict()
    element["name"] = name
    element["age"] = int(age)
    element_name = "element" + str(index)
    root[element_name] = element
    ans = input("Exit (y/n)?: ").lower()
    if ans == "y":
        exit_code = True

print(root)

# Accessing Ingredients: Output all the ingredients from the following list within 
# the “ingredients” key using a for loop:
# >>> pizza = { 
# >>> 'ingredients': ['cheese', 'sausage', 'peppers']
# >>> }

pizza = { 'ingredients': ['cheese', 'sausage', 'peppers'] }

for ingredient in pizza["ingredients"]:
    print(ingredient)
    
    