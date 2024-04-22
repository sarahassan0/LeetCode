class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        set_S, set_T = defaultdict(int), defaultdict(int)
        
        for i in s:
            
            set_S[i] += 1

        for i in t:
            
            set_T[i] += 1


        return set_S == set_T
        
###################################################
        # return sorted(s) == sorted(t)
##############################################
        return Counter(s) == Counter(t)
        