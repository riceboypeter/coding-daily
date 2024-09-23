class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxheight = 0
        l_point = 0
        r_point = len(height) - 1
        while l_point < r_point:
            maxheight = max((min(height[l_point],height[r_point]) * (r_point - l_point)),maxheight)
            if height[l_point] < height[r_point]:
                l_point += 1
            else:
                r_point -= 1

        return maxheight
    
print(Solution.maxArea(0,[1,8,6,2,5,4,8,3,7]))

# originally I had 2 for loops for my bruteforce solution
# but leetcode is gonna cry about it so here's someone else's solution
# it's a lot more elegant instead of iterating through the entire list