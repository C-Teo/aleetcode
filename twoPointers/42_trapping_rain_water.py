# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: list[int]) -> int:
        vol = 0
        
        i = 0
        j = len(height)-1
        min_val = 0

        if j+1 < 3:
            return 0

        h = 0

        while i < j:
            min_val = min(height[i],height[j])
            if min_val > 0:
                if min_val > h:
                    vol += (min_val-h)*(j-i+1)
                    h = min_val

            if height[i] > height[j]:
                if height[j] <= h:
                    vol -= height[j]
                else:
                    vol -= h
                j -= 1
            else:
                if height[i] <= h:
                    vol -= height[i]
                else:
                    vol -= h
                i += 1
        
        if height[i] <= h:
            vol -= height[i]
        else:
            vol -= h

        return vol

# T = O(N)
# S = O(1)

output = Solution.trap(self=Solution,height=[0,1,0,2,1,0,1,3,2,1,2,1])
print(output)