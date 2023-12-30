# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)

        for x in nums:
            mp[x] = mp[x] + 1

        output = []
        for key,value in mp.items():
            output.append((key,value))
        s_output = sorted(output, key=lambda x: x[1])

        if len(s_output) >= k:
            return [item[0] for item in s_output[len(output)-k:]]
        
        return False

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] = frequency[num] + 1
        
        frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
        result = list(frequency.keys())[:k]

        return result

# T = O(n * log(n))
# S = O(n)

# Bucket Sort
# Quicksort