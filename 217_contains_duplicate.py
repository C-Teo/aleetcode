# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        S = set()

        for x in nums:
            if x in S:
                return True
            else:
                S.add(x)
        
        return False

# T = O(N)
# S = O(N)