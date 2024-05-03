#Brandon Gurley
#12-4-2022
#CIS 360
#Lab 6

#make heap alg
#Implement the liner-time makeheap algorithm: read in n unsorted numbers and create a heap
# - (stored as an array) to store these n number

def makeheap(array, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and array[l] > array[largest]:
        largest = l

    if r<n and array[r] > array[largest]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        makeheap(array, n, largest)

def HeapSort(array, n):
    n = len(array)

    for i in range(n//2 -1, -1, -1):
        makeheap(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        makeheap(array, i, 0)

if __name__ == '__main__':
    array = [1, 3, 5, 4, 6, 13,
           10, 9, 8, 15, 17]
    n = len(array)
    HeapSort(array, n)
    print("Sorted Array is")
    for i in range(n):
        print( array[i])
