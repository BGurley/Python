# Brandon Gurley
# 9-26-2022
# CIS 360
# Lab 3 Task A

import time

startTime = time.time()
list = [2, 4, 6, 7, 3]
#print('Original List', list)
stack = []
n = len(list)
for item in list:
    stack.append(item)
print(stack)
list = []
for i in range(0, n):
    list.append(stack.pop())
    #stack.pop()
print(list)
print("%s seconds" % (time.time() - startTime))
