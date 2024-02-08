from tkinter import N
from turtle import left


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


# print(quickSort([4, 2, 7, 1, 4, 3]))

# refer -https://youtu.be/pM-6r5xsNEY?si=oVx19KuUEEPI0ntF
def partition(arr, left, right, pivot):
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left  # index


def quick_Sort(arr, start, end):
    if start < end:
        mid = (start+end)//2
        pivot = arr[mid]
        index = partition(arr, start, end, pivot)
        quick_Sort(arr, start, index-1)
        quick_Sort(arr, index, end)
    return arr


arr = [1, 4, 6, 2, 3, 0, 1]
#print(quick_Sort(arr, 0, len(arr)-1))



# merging two sorted list 
def merge(arr1,arr2):

    m=len(arr1)
    n=len(arr2)
    res=[0]*(m+n)
    i,j,k=0,0,0
    while i < m and j < n:
    # compares and updates the min val in result array
        if arr1[i] < arr2[j]:
            res[k] = arr1[i]
            i+=1
        else:
            res[k] = arr2[j]
            j+=1
        k+=1
    
    # sometimes arr1 may have many elements left , but arr2 has reached the end 
    while i < m:
            
            res[k] = arr1[i]
            k+=1
            i+=1
    while j < n: 
            res[k] = arr2[j]
            k+=1
            j+=1

    return res


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        
        
        # Merge the sorted halves

        i = j = k = 0  # Initialize indices for the left, right, and merged arrays

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_half (if any)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_half (if any)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)
