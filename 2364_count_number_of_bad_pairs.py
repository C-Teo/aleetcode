class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        for index, val in enumerate(nums):
            nums[index] = index - val

        mp = {}
        res = 0

        for index, val in enumerate(nums):
            if val in mp:
                mp[val] += 1
            else:
                mp[val] = 1
            res += index + 1 - mp[val]
        
        return res

# Time: O(n)
# Space: O(n)
