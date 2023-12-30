# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        checked = {}
        l = len(nums)

        for k in range(len(nums)-2):
            if nums[k] not in checked:
                checked[nums[k]] = True
                i = k + 1
                target = 0 - nums[k]
                mp = {}
                for i in range(k+1,l):
                    if target-nums[i] in mp and mp[target-nums[i]]:
                        output.append([nums[k],nums[i],target-nums[i]])
                        mp[nums[i]] = False
                        mp[target-nums[i]] = False
                    elif nums[i] not in mp:
                        mp[nums[i]] = True
        
        return output

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        l = len(nums)
        visited = {}

        for k in range(len(nums)-2):
            if nums[k] not in visited:
                visited[nums[k]] = True
                target = 0 - nums[k]
                mp = {}
                for i in range(k+1,l):
                    if target-nums[i] in mp:
                        output.add(tuple(sorted([nums[k],nums[i],(target-nums[i])])))
                    else:
                        mp[nums[i]] = 1
        
        return output

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        p, n, z = [], [], []

        for val in nums:
            if val > 0:
                p.append(val)
            elif val < 0:
                n.append(val)
            else:
                z.append(0)
        
        P = set(p)
        N = set(n)

        # Complement Duplicates with 0
        if z:
            for val in P:
                if -val in N:
                    out.add((-val,0,val))

        # Three 0's
        if len(z) > 2:
            out.add((0,0,0))

        # Complements of Positive Pairs
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if -(p[i] + p[j]) in N:
                    out.add(tuple(sorted([p[i],p[j],-(p[i]+p[j])])))
        
        # Complements of Negative Pairs
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if -(n[i] + n[j]) in P:
                    out.add(tuple(sorted([n[i],n[j],-(n[i]+n[j])])))
        
        return out