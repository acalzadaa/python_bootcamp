# Declaring a Tuple

# To declare a tuple, you use a comma to separate two or more items. 
# Lists are denoted by their square brackets on the outside, 
# whereas tuples can be declared with optional parenthesis.

t1 = ("hello", 2, "hello")
t2 = True, 1
print(type(t1), type(t2))

# What Are Sets?

# Sets share the same characteristics of lists and dictionaries. A set is a collection of
# information like a list; however, like a key in a dictionary, sets can only contain unique 
# values. They are also an unordered collection. This means that they cannot be accessed 
# by index but rather by the value itself like dictionary keys. They can be iterated through 
# though, like how dictionary keys can be looped over. Sets are practical in situations of 
# storing unique items.

# Declaring a Set

s1 = set([1,2,3,1,2])
s2 = {4,5}
print(type(s1), type(s2))
s1.add(5)
s1.remove(1)
print(s1)

# remember: 
# listValue = ["hola", 5, True] 
# listValue[0] 
# for list in listValue
# listValue[3] = "new"

# What Are Frozensets?

# Frozensets are essentially the combination of a set and a tuple. They are immutable, 
# unordered, and unique. These are perfect for sensitive information like bank account numbers, 
# as you wouldn’t want to alter those. They can be iterated over, but not indexed.

# declaring a frozenset

fset = frozenset([1,2,3])
print(type(fset))
