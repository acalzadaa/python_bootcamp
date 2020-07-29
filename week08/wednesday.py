# Wednesday: Map, Filter, and Reduce

# The map function is used when you need to alter
# all items within an iterable data collection

# using the map function without lambdas
def convert_deg(c):
    return (9 / 5) * c + 32


temps = [12.5, 13.6, 15, 9.2]

converted_temps = map(convert_deg, temps)
print(converted_temps)

converted_temps = list(converted_temps)
print(converted_temps)

# Map with Lambdas

temps = [12.5, 13.6, 15, 9.2]

converted_temps = list(map(lambda C: (9 / 5) * C + 32, temps))
print(converted_temps)

# Filter Without Lambdas

# using the filter function without lambda functions, filter out temps below 55F


def filter_temps(C):
    converted = (9 / 5) * C + 32
    return True if converted > 55 else False

temps = [12.5, 13.6, 15, 9.2]

filtered_temps = filter(filter_temps, temps)
print(filtered_temps)

filtered_temps = list(filtered_temps)
print(filtered_temps)

# Filter with Lambdas

# using the filter function with lambda functions, filter out temps below 55F

temps = [12.5, 13.6, 15, 9.2]

filtered_temps = list(filter(lambda C : True if (9/5) * C + 32 > 55 else False, temps))
print(filtered_temps)

# Mapping Names: Use a lambda and map function to map over the list of 
# names in the following to produce the following result “[ “Ryan”, “Paul”, 
# “Kevin Connors” ]. 
# 
# >>> names = [ " ryan", "PAUL", "kevin connors " ]

names = [ " ryan", "PAUL", "kevin connors " ]

# create a scaffold using for
for name in names:
    print(name.strip().lower().title())

# convert the for to map/lambda
corrected_names = list(map(lambda name: name.strip().lower().title(),names))
print(corrected_names)


# Filter Names: Using a lambda and filter function, filter out all the names that 
# start with the letter “A.” Make it case insensitive, so it filters out the name 
# whether it’s uppercase or not. The output of the following list should be 
# [ “Frank”, “Ripal” ]. 
# 
# >>> names = [ "Amanda", "Frank", "abby", "Ripal", "Adam" ]

names = [ "Amanda", "Frank", "abby", "Ripal", "Adam" ]

for name in names:
    if name.lower().startswith("a"):
        print(name)

filtered_names = list(filter( lambda name : name if name.lower().startswith("a") else "", names))
print(filtered_names)