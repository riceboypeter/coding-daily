class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if (i!=j) and (nums[i]+nums[j]==target):
                    return [i,j]


print(Solution.twoSum(nums=[2,7,11,15],target=9))