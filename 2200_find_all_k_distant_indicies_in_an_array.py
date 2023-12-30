# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l = len(nums)
        mp = {}

        for i in range(l):
            if nums[i] == key:
                mp[i] = 1
        
        keys = list(mp.keys())

        for i in keys:
            for j in range(1,k+1):
                if i+j < l and i+j not in mp:
                    mp[i+j] = 1
                if i-j > -1 and i-j not in mp:
                    mp[i-j] = 1
        
        return sorted(list(mp.keys()))