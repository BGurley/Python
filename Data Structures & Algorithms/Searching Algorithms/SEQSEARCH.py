# Brandon Gurley
# 9-9-22
# CIS 360
# Lab 1
import random
import time

startTime = time.time()

def sequential_search (dlist, n):

    position = 1
    found = False

    while position < len(dlist) and not found:
        if dlist[position] == n:
            found = True
        else:
            position = position+1
    return found, position


numList = []
for i in range(0, 1000000):
    x = random.randint(1, 1000)
    numList.append(x)

print(sequential_search(numList, 11))
print("%s seconds" % (time.time() - startTime))
