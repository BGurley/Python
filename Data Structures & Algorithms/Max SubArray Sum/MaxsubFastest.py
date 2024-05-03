#Brandon Gurley
# 9-25-2022
# CIS 360
# Lab 2  - MaxsubFastest.py
import random
import time
startTime = time.time()
def MaxsubFastest(A):
    n = len(A)
    M = ([0]*(n+1))
    t = 1
    for t in range (1, n):
        M[t] = max(0, (M[t-1]+A[t]))
    m = 0
    for t in range (1, n):
        m = max(m , M[t])
    return m

nArray = [random.randint(-100,100) for x in range(20)]
n = len(nArray)
result = MaxsubFastest(nArray)
print("Subarray Sum = ", result)
finalTime = (time.time() - startTime)
print("%s seconds" % finalTime)
col1 = finalTime/n
col2 = finalTime/(n**2)
col3 = finalTime/(n**3)
print('\n', col1)
print('\n', col2)
print('\n', col3)
