class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s in hashMap:
                hashMap[sorted_s].append(s)
            else:
                hashMap[sorted_s] = [s]

        return [i for i in hashMap.values()]
        