# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        res = ""
        
        for char in s:
            if char.isalnum() == True:
                res += char.lower()
        
        def helper(s,bool):
            if s == "":
                return True
            if s[0] == s[len(s)-1]:
                return helper(s[1:len(s)-1],bool)
            elif bool == False:
                return helper(s[1:len(s)],True) or helper(s[0:len(s)-1],True)
            else:
                return False

        return helper(res,False)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        def helper(l,r,bool):
            if l >= r:
                return True
            if s[l] == s[r]:
                return helper(l+1,r-1,bool)
            elif bool:
                return helper(l+1,r,False) or helper(l,r-1,False)
            else:
                return False

        return helper(l,r,True)

class Solution:
    def validPalindrome(self, s: str) -> bool:
            p1=0
            p2=len(s)-1
            while p1<=p2:
                if s[p1]!=s[p2]:
                    string1=s[:p1]+s[p1+1:]
                    string2=s[:p2]+s[p2+1:]
                    return string1==string1[::-1] or string2==string2[::-1]
                p1+=1
                p2-=1
            return True