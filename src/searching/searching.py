# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end is None:
        end = len(arr) - 1

    if start > end:
        return -1
        
    mid = (start + end) // 2

    if target is arr[mid]:
        return mid 

    if target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)

    return binary_search(arr, target, mid + 1, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def descending_binary_search(arr, target, left, right):
    # base case 
    # or we searched the whole array, i.e. when left > right
    if left > right:
        return -1
    # how do we move closer to a base case? 
    # we'll stop when we either find the target 
    else:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            # rule out the right side
            return descending_binary_search(arr, target, left, mid - 1)
        else:
            # rule out the left side 
            return descending_binary_search(arr, target, mid + 1, right)


def agnostic_binary_search(arr, target):
    # Your code here
    # figure out whether the input array is sorted in ascending or descending order 
    # keep a boolean to indicate the order of the array 
    # compare arr[0] and arr[1] 
    if arr[0] > arr[-1]:
        is_ascending = False
    else:
        is_ascending = True

    # if the input array is ascending, call `binary_search` with the array and target 
    if is_ascending:
        return binary_search(arr, target, 0, len(arr) - 1)
    # otherwise, call `descending_binary_search` with the array and target 
    else:
        return descending_binary_search(arr, target, 0, len(arr) - 1)
