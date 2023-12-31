# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol = 0

        i = 0
        j = len(height)-1

        while i < j:
            if min(height[i],height[j])*(j-i) > vol:
                vol = min(height[i],height[j])*(j-i)
            
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        
        return vol

# T = O(N)
# S = O(1)