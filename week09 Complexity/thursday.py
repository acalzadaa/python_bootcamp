# Thursday: Understanding Algorithmic Complexity

a = "a"
b = "b"
print(hash(a))
print(hash(b))
c = b
print(hash(c))

# creating data collections to test for time complexity

import time

d = {} # fake dictionary
for i in range(1000000):
    d[i] = "value"
big_list = [x for x in range(10000000)] # fake list


# retrieving information and tracking time to see which is faster

start_time = time.time()
if 999999 in d:
    print("Found in dictionary")
end_time = time.time() - start_time
print(f"Dictionary took: {end_time} to execute")

start_time = time.time()
if 999999 in big_list:
    print("Found in list")
end_time = time.time() - start_time
print(f"List took {end_time} to execute")