# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        nums = []

        for i in tokens:
            if i == "+" and len(nums) > 1:
                r = nums.pop()
                l = nums.pop()
                nums.append(l+r)
            elif i == "-" and len(nums) > 1:
                r = nums.pop()
                l = nums.pop()
                nums.append(l-r)
            elif i == "*" and len(nums) > 1:
                r = nums.pop()
                l = nums.pop()
                nums.append(l*r)
            elif i == "/" and len(nums) > 1:
                r = nums.pop()
                l = nums.pop()
                sign = -1 if l*r < 0 else 1    
                nums.append(sign*(abs(l)//abs(r)))
            else:
                nums.append(int(i))
    
        return nums[0]

# T = O(N)
# S = O(N)