#Brandon Gurley
# 9-12-2022
# Lab 1
# Binary Search
import random
import time

startTime = time.time()

def binarySearch(numList, low, high, x):

    if high >= low:

        mid = ((high+low)//2)

        if numList[mid] == x:
            return mid

        elif numList[mid] > x:
            return binarySearch(numList, low, mid-1, x)

        else:
            return binarySearch(numList, mid+1, high, x)

    else:
        return -1


numList = []
for i in range(0, 1000000):
    x = random.randint(1, 999)
    numList.append(x)

x=11

numList.sort()
result = (binarySearch(numList, 0, len(numList)-1, x))
if result != -1:
    print("Number is present in array at index", str(result))
else:
    print("Number aint in the list")
print("%s seconds" % (time.time() - startTime))
