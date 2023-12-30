# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        mp = {}

        for i in words:
            for j in i:
                if j in mp:
                    mp[j] += 1
                else:
                    mp[j] = 1
        
        l = len(words)

        for val in mp.values():
            if val % l != 0:
                return False
        
        return True

# T = O(N*M)
# S = O(N)