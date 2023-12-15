class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        s = set()

        # Sacrifice Space complexity to Decrease Time Complexity
        temp = []
        for word in strs:
            temp.append(sorted(word))

        output = []

        for x in range(len(strs)):
            if x not in s:
                layer = [strs[x]]

                for y in range(x+1,len(strs)):
                    if y not in s:
                        if temp[x] == temp[y]:
                            s.add(y)
                            layer.append(strs[y])
                
                output.append(layer)
        
        return output

# T(N) = O(N^3)
# S(N) = O(N)

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word)) # Make it into String
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())

class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss in hm:
                hm[ss].append(s)
            else:
                hm[ss] = [s]
        
        return [v for k,v in hm.items()]