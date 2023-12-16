class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)

        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            output[i] *= prefix
            output[len(output)-1-i] *= suffix

            prefix *= nums[i]
            suffix *= nums[len(nums)-1-i]
        
        return output

# T(N) = O(N)
# S(N) = O(1) # Since we can ignore the array output