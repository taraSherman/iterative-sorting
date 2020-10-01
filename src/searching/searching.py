def linear_search(arr, target):
    # Your code here
    # iterate over array,
    for i in range( 0, len(arr) ):
        # if target is equal to index [i]
        if target == arr[i]:
            # return index
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) -1
    mid = 0
    # so long as left is less than or equal to right... follow these steps
    while left <= right:
        # set middle to half the sum of left and right (i.e. the average)
        mid = (left + right)//2
        # if mid is less than target,
        if arr[mid] < target:
            # then remove right
            left = mid - 1
        # or if mid is greater than target,
        elif arr[mid] > target:
            # then remove left
            right = mid + 1
        else:
            # otherwise, vtarget must == mid, so return mid
            return mid
    return -1  # not found
