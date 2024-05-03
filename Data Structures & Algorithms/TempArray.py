# Brandon Gurley
# 10-3-2022
# CIS 360
# Lab 3 Task C

import time

startTime = time.time()
i=1
arrA = [1, 2, 3, 4, 5, 6]
n = len(arrA)
for i in range (0, (n//2)):
    temp = arrA[i]
    arrA[i]=arrA[(n-i-1)]
    arrA[(n-i-1)] = temp

print(arrA)
print("%s seconds" % (time.time() - startTime))
