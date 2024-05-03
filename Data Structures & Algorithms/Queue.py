# Brandon Gurley
# 9-26-2022
# CIS 360
# Lab 3 Task B

import time

startTime = time.time()
list = [2, 4, 6, 7, 3, 8]
#print('Original List', list)
queue = []
n = len(list)
for item in list:
    queue.append(item)
print(queue)
list = []
for i in range(0, n):
    list.append(queue.pop())
    #stack.pop()
print(list)
print("%s seconds" % (time.time() - startTime))
