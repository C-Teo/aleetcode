# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        track = []

        for index in range(len(position)):
            track.append((position[index],speed[index]))

        track.sort(key=lambda x: x[0])

        stack = []

        for index in range(len(track)-1,-1,-1):
            if stack:
                if (target-track[index][0])/track[index][1] > stack[-1]:
                    stack.append((target-track[index][0])/track[index][1])
            else:
                stack.append((target-track[index][0])/track[index][1])
        
        return len(stack)

# T = O(N log n)
# S = O(N)