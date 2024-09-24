# this solution exceeds leetcode's timer but the implemetation surely is good enough for an interview
# cannibalized someone else's code for my submission ~(￣▽￣)~*

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()
        
        for left in range(0, len(nums)):
            middle = left + 1
            right = len(nums)-1

            while middle < right:
                total = nums[left] + nums[middle] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    middle += 1
                else:
                    if [nums[left],nums[middle],nums[right]] in triplets:
                        middle += 1
                    else:
                        triplets.append([nums[left],nums[middle],nums[right]])
                        middle += 1

        return triplets
    

print(Solution.threeSum(True, [-1,0,1,3,-1,-4]))