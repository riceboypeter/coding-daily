'''
August 22nd, 2024
QS took a while to implement because i forgot how to do it 💀

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.
Integers can appear more than once in the list. You may assume all numbers in the list are positive.
For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
'''

s = [12, 12, 1, 61, 5, 9, 2, 1, 1]
k = 24

# first, just for fun, i'm gonna implement quicksort
def pivot(array, low, high):
    piv = array[high]
    i = low-1
    for j in range(low, high):
        if array[j] <= piv:
            i = i+1
            (array[i],array[j]) = (array[j],array[i])
        
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1

def quicksort(array, low, high):
    if low < high:
        piv = pivot(array,low,high)
        quicksort(array, low, piv-1)
        quicksort(array, piv+1, high)

quicksort(s, 0, len(s)-1)

# ok. Now that the list is sorted, let's do the actual operation. I'm thinking we just check recursively?

def subset_sum(S, k):
    # Base case: if k is 0, return an empty list (because an empty list sums to 0)
    if k == 0:
        return []
    # If S is empty and k is not 0, no subset can be formed
    if not S:
        return None

    # Recursively check if the first element can be part of the subset
    # Include the first element
    first = S[0]
    remaining = S[1:]
    
    with_first = subset_sum(remaining, k - first)
    if with_first is not None:
        return [first] + with_first
    
    # Exclude the first element
    without_first = subset_sum(remaining, k)
    
    return without_first

print(subset_sum(s,k))