# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index # as the first index, it is currently the smallest
        # loop through the unsorted part of the array (skip last), find the smallest, make it current, compare it with the smallest already sorted
        # if this current index is smaller than smallest_index, swap it with smallest_index
        # continue looping through unsorted part (which gets smaller with each loop), setting cur_index and swapping it with smallest_index, until unsorted are all removed
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                # TO-DO: swap
                # Your code here
                arr[i], arr[j] = arr[j], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
# def bubble_sort(arr):
#     # Your code here
def bubble_sort(arr):
    # first pass: compare n −1 pairs, range is from last item [-1] to first item [0] and back to last item [-1]
    for i in range(len(arr) -1, 0, -1):
        # iterate within that set range
        for j in range(i):
            # compare current index [j] to the
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # for i in range(0, len(array) - 1):
                #     for j in range(0, len(array) - 2):
                #         if array[i] > array[i + 1]:
                #             array[i], array[i + 1] = array[i + 1], array[i]
#
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
