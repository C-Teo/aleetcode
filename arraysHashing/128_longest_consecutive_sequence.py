class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        output = 1

        temp = 1
        for x in range(1,len(nums)):
            if nums[x] == nums[x-1]+1:
                temp += 1
            elif nums[x] != nums[x-1]:
                if temp > output:
                    output = temp
                temp = 1
        
        return max(output,temp)

# T = O(N log N)
# S = O(1)