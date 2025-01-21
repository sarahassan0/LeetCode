class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        set_S, set_T = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            set_S[s[i]] += 1
            set_T[t[i]] += 1

        return set_S == set_T
         
#---------------------------- Another Solutions -----------

        # return sorted(s) == sorted(t)
#-----------------------------------------------------
        # return Counter(s) == Counter(t)
        