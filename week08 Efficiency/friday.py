# Friday: Writing a Binary Search

# setting up imports and generating a list of random numbers to work with

import random

nums = [random.randint(0,20) for i in range(10)]

def binarySearch(aList, num):
    #step 1 - sort the list
    aList.sort()
    
    print(list(dict.fromkeys(aList)))
    aList = list(dict.fromkeys(aList))
    if(not aList):
        return False
    elif aList[len(aList) // 2] == num:
        return True
    elif aList[len(aList) // 2] > num:
        return binarySearch(aList[:len(aList) // 2], num)
    elif aList[len(aList) // 2] < num:
        return binarySearch(aList[(len(aList) // 2)+1:], num)

print(sorted(nums))
print(binarySearch(nums, 3))

