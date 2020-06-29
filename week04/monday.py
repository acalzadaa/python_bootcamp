# declaring a list of numbers
nums = [5,10,15.2,20]
print(nums)

# accessing elements within a list
print(nums[1])
num = nums[2]
print(num)

# declaring a list of mixed data types
num = 4.3
data = [num, "word", True]
print(data)

# understanding lists within lists
data = [5,"book", [34,"hello"], True]
print(data)
print(data[1][0]) # PRINT THE B
print(data[2])

# using double bracket notation to access lists within lists
print(data[2][0])
inner_list = data[2]
print(inner_list[1])

# changing values in a list through index
data = [5,10,15,20]
print(data)
data[0] = 100
print(data)

# understanding how lists are stored
a = [5,10]
b= a
print(f"a: {a}\t b:{b}")
print(f"Location a[0]: {a[0]} \t Location b[0] {b[0]}")
a[0] = 20
print(f"a: {a}\t b:{b}")

# using [:] to copy a list
data = [5,10,15,20]
data_copy = data[:]
data[0] = 50
print(f"{data} , {data_copy}")



data2 = [5,10,15,20]
data_copy2 = data2.copy()
print(f"{data2} , {data_copy2}")
data2[0] = "hola"
print(f"{data2} , {data_copy2}")


#Exercise 1
sports_list = ["baseball", "basketball", "football", "hockey"]
for sport in sports_list:
    print(f"I like to play {sport}")
    
#Exercise 2
names_list = ["John", "Abraham", "Sam", "Kelly"]
for names in names_list:
    print(names[0])
