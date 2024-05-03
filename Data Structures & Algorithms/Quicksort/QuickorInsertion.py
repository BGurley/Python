#Brandon Gurley
# 10-31-2022
#CIS 360
#Lab 8b
import random
import statistics
import time

# If the size is greater than the threshold value (10), then the quicksort function is called for that portion of the array. Else insertion sort is called


#starts timer for program
startTime = time.time()

def insertionsort(array, low, high):

    for i in range ((low+1), high+1):
        x = array[i]
        j = i-1
        while (j>(low-1) and array[j]>x):
            array[j+1] = array[j]
            j= j-1
        array[j+1] = x


def partition(array, low, high):

    medArray = []
    midElement = (low+high)//2


    medArray.append(array[low])
    medArray.append(array[midElement])
    medArray.append(array[high])
    median = statistics.median(medArray)
    if (array[low] == median):
        pass
    elif(array[midElement] == median):
        (array[low], array[midElement])=(array[midElement], array[low])
    elif(array[high] == median):
        (array[low], array[high])=(array[high], array[low])

    #print('\n median is: ', median)
    pivot  = array[low]
    #print(pivot)
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
        if ((pivotpoint-low)>10):
            QuickSort(array, low, (pivotpoint-1))
        else:
            insertionsort(array, low, (pivotpoint-1))
        if ((high - pivotpoint)>10)   :
            QuickSort(array, (pivotpoint+1), high)
        else:
            insertionsort(array, (pivotpoint+1), high)


array = []
for i in range(0,50000):
    n = random.randint(1,50000)
    array.append(n)
print('\n array before sorting: ', array)
size = len(array)
QuickSort(array, 0, (size-1))
print('\n array after sorting: ', array)
print("Run time is %s seconds" % (time.time() - startTime))
