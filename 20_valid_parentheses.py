# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque

        stack = deque()

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if stack:
                    if char == ')' and stack.pop() != '(':
                        return False
                    elif char == ']' and stack.pop() != '[':
                        return False
                    elif char == '}' and stack.pop() != '{':
                        return False
                else:
                    return False

        if stack:
            return False
        return True

class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False
        return len(stack) == 0

# T = O(N)
# S = O(N)