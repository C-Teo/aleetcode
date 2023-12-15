class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}

        for x in range(len(nums)):
            if target-nums[x] in mp:
                return [x,mp[target-nums[x]]]
            else:
                mp[nums[x]] = x
        
        return False

# T(N) = O(N)
# S(N) = O(N)