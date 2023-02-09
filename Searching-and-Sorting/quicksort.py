"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

"""
Approach:
1. Pick a pivot and return it
2. Create two lists, one for items lower than pivot and one for greater
3. Apply same algo to subarrays until we reach base case
"""

def quicksort(array):
    length = len(array)
    if length <= 1:
        return array
        
    else:
        pivot = array.pop()
        
        items_greater = []
        items_lower = []
        
        for item in array:
            if item < pivot:
                items_lower.append(item)
            else:
                items_greater.append(item)
    
    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)