# Brandon Gurley
# September 19th, 2022
# CIS 360
# Lab 2
import random
import time
startTime = time.time()
def MaxsubFaster(nArray, n):
    S = ([0]*(n+1))
    i=1
    for i in range (1, n):
        S[i] = S[i-1]+nArray[i]
    m = 0
    for j in range (0, n):
        for k in range (j, n):
            s = (S[k] - S[j-1])
            if s>m:
                m=s
    return m;


nArray = [random.randint(-100,100) for x in range(10)]
n = len(nArray)
result = MaxsubFaster(nArray, n)
print("Subarray Sum = ", result)
finalTime = (time.time() - startTime)
print("%s seconds" % finalTime)
col1 = finalTime/n
col2 = finalTime/(n**2)
col3 = finalTime/(n**3)
print('\n', col1)
print('\n', col2)
print('\n', col3)
