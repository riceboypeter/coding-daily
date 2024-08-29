'''
August 29, 2024


Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
Do this in O(N) time.
'''

'''
silly little webdev forgot what time complexity was so my first solution
was actually O(n^2) 🤭 yay recursion

def findmax(subL, subR, maxval):
    currmax = sum(arr[subL:subR])
    if currmax > maxval:
        maxval = currmax
    if subL < len(arr) - 1:
        return findmax(subL + 1, subR, maxval)
    elif subR > 0:
        return findmax(subL, subR - 1, maxval)
    return maxval

print(findmax(0, len(arr), 0))

'''

arr = [34, -50, 42, 14, -5, 86]

# so apparently there's a thing called kadane's algorithm (probably forgot it from first year tbh)
def kadane(arr):
    max_so_far = 0
    max_here = 0
    for i in arr:
        max_here = max(0,max_here+i)
        max_so_far = max(max_so_far,max_here)
    return max_so_far

print(kadane(arr))