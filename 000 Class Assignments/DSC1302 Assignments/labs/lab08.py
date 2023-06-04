import random

def binary_search(array: list, target: int):
    low = 0
    high = len(array) - 1
    mid = (low + high) // 2
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid
        else:
            return mid
        
    if array[mid] == target:
        return mid
    
    return -1



def mergesort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]
    
    left = mergesort(left)
    right = mergesort(right)

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
    
    return array





def generate_list(n = 10, lower_bound = 0, upper_bound = 10):
    res = []
    for i in range(n):
        res += [int(random.random() * upper_bound) + lower_bound]
    return res


binary_search_list = [6, 1, 0, 9, 5, 3, 0, 5, 4, 1]
binary_search_list.sort()
print()
print('binary search list:\n', binary_search_list)
print('searching for value: 9\nValue found at index: ', binary_search(binary_search_list,6))
print('end of Q1 ------------------------------------------------------------')
print()

input_list = generate_list()
print('before sorting: ', input_list)
print('after sorting:', mergesort(input_list))



