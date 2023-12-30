# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}

        for x in range(len(nums)):
            if target-nums[x] in mp:
                return [x,mp[target-nums[x]]]
            else:
                mp[nums[x]] = x
        
        return False

# T = O(N)
# S = O(N)