class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}

        for char in s:
            if char in mp:
                mp[char] = mp[char] + 1
            else:
                mp[char] = 1
        
        for char in t:
            if char in mp:
                mp[char] = mp[char] - 1
            else:
                return False

        for val in mp.values():
            if val != 0:
                return False
        
        return True

# T(N) = O(N)
# S(N) = O(N)

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)