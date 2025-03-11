class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # defaultdict() dont have to check if key is present in the dict
    # if not in the {} will set it as a key

    #--------------- O(n *  k log k) time - O(n * k) space
        hashMap = defaultdict(list) 
        for s in strs:
            sorted_s = ''.join(sorted(s))
            hashMap[sorted_s].append(s)

        return list(hashMap.values())
        

#----------------- Another solution using {} ------------------

        # hashMap = {}
        # for s in strs:
        #     sorted_s = ''.join(sorted(s))

        #     if sorted_s in hashMap:
        #         hashMap[sorted_s].append(s)
        #     else:
        #         hashMap[sorted_s] = [s]