#Brandon Gurley
# 10-31-2022
#CIS 360
#Lab 8
import random
import statistics
import time

startTime = time.time()

def partition(array, low, high):
    #print('partition test')
    pivot  = array[low]

    print(pivot)
    i = low+1
    j = high
    while (i < j):
        #print('quicksort test 1')
        while (i < high and array[i] <= pivot):
            #print('quicksort test 2')
            i+=1
        while (j > low and array[j] >= pivot):
            #print('quicksort test 3')
            j-=1
        if (i < j):
            (array[i], array[j]) = (array[j], array[i])
    if(i > j):
        i-=1
    if(array[low] > array[i]):
        (array[low], array[i]) = (array[i], array[low])
    pivotpoint = i
    return pivotpoint

def QuickSort(array, low, high):
    #print('quicksort test')
    if (high > low):
        pivotpoint = partition(array, low, high)
        QuickSort(array, low, (pivotpoint-1))
        QuickSort(array, (pivotpoint+1), high)


array = []
for i in range(0,100000):
    n = random.randint(1,100000)
    array.append(n)
print('\n array before sorting: ', array)
size = len(array)
QuickSort(array, 0, (size-1))
print('\n array after sorting: ', array)
print("Run time is %s seconds" % (time.time() - startTime))
