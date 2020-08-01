# Friday: Writing a Binary Search

# setting up imports and generating a list of random numbers to work with

import random

nums = [random.randint(0,20) for i in range(10)]

def binarySearch(aList, num):
    #step 1 - sort the list
    aList.sort()

    # step 6: setup a loop to repeat steps 2 through 6 until list is empty
    while aList:
        #step 2 - find the middle index
        mid = len(aList) // 2
        
        #step 3 - check the value at middle index, if it's equal to num return True
        if aList[mid] == num:
            return True

        #step 4 - check if value is greater, cut off right half of list
        elif aList[mid]> num:
            aList = aList[:mid]

        #step 5 - check if value is lesser, cut of left half of list
        elif aList[mid]< num:
            aList = aList[mid+1:]
    return False

print(sorted(nums))
print(binarySearch(nums, 3))

