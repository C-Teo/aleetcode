# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        
        for char in s:
            if char.isalnum() == True:
                res += char.lower()

        print(res)

        if res == "":
            return True

        l = 0
        r = len(res)-1

        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        
        return True