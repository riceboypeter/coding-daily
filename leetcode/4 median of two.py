# TIL: python's built-in sort function is O(nlogn)

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:        
        combine = nums1 + nums2
        combine.sort()

        length = len(combine)

        if length % 2 == 1:
            median = combine[round(length//2)-1]
        elif length % 2 == 0:
            median = (combine[length//2-1] + combine[length//2])/2

        return median