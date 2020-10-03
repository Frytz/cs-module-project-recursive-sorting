# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    crawler = 0
    a = 0
    b = 0
    while a + b < elements:

        if a > len(arrA) - 1:
            merged_arr[crawler] = arrB[b]
            b += 1
            crawler += 1
        elif b > len(arrB) - 1:
            merged_arr[crawler] = arrA[a]
            a += 1
            crawler += 1
        elif arrA[a] < arrB[b]:
            merged_arr[crawler] = arrA[a]
            a += 1
            crawler += 1
        else:
            merged_arr[crawler] = arrB[b]
            b += 1
            crawler += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    elements = len(arr)
    mid = elements // 2

    if mid > 0:
        arrA = merge_sort(arr[0:mid])
        arrB = merge_sort(arr[mid:])
        return merge(arrA, arrB)
    else:
        return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid +1
    #If the direct merge is already sorted
    if arr[mid] <= arr[start2]:
        return
    
    #Two pointers to maintain start of both array merges
    while start <= mid and start2 <=end:
        
        #if ele 1 is in the right place
        if arr[start] <= arr[start2]:
            start += 1
        
        else:
            value = arr[start2]
            index = start2

            #shift all the ele between ele 1 , ele 2, right by 1
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value

            #updates all pointers
            start += 1
            mid += 1
            start2 += 1


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        #helps avoid overflow of large l and r
        m = l + (r - l) // 2
        #sort first and second halves
        merge_sort_in_place(arr , l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)

