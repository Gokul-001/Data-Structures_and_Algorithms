def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        flag = False   # Adaptive check
        for j in range(0, n-i-1):  # coz last (n-i) is sorted in every i passes
            if arr[j] > arr[j+1]:
                flag = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if flag == False:  # check if sorting occurred in the entire array
            break
    return arr
# O(n)2


def bubble_sort_reverse(arr):
    # arr = [1, 5, 3, 2]
    for i in range(len(arr)-1, -1, -1):
        for j in range(0, i+1):
            if arr[i] <= arr[j]:  # arr[j]>=arr[i] -> [5,3,2,1] (reversed)
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)


def insertion_sort(arr):  # O(n^2)  [STABLE / ADAPTIVE IN NATURE]
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        # j should not be neg idx and comparing temp and arr[j]
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr
# print(insertion_sort([2, 1, 4, 0, 5]))


def selection_sort(arr):
    for i in range(0, len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):  # can use same i index
            if arr[j] < arr[min_idx]:
                min_idx = j
        (arr[min_idx], arr[i]) = (arr[i], arr[min_idx])
    return arr


# print(selection_sort([2, 1, 8, 4]))


# this is Similar to merge sort implementation
def quickSort(arr):
    if len(arr) <= 1:
        return arr

    # pivot = arr[len(arr)//2]

    # optimisation -> using the median of three (avoid worst-case behavior for already sorted or nearly sorted arrays )

    pivot = sorted([arr[0], arr[len(arr)//2], arr[-1]])[1]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return (quickSort(left) + middle + quickSort(right))


print(quickSort([4, 2, 7, 1, 4, 3]))

def partition(arr,left,right,pivot):
        while left <=right :
            while arr[left]>
def quick_Sort(arr, start, end):
    if start < end:
        pivot = (start+end)//2
        index = partition(arr,)