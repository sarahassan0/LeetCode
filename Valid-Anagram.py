class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
        if len(s) != len(t): return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for n in count:
            if n != 0:
                return False
        return True

    
#---------------------------- Another Solutions -----------

        # set_S, set_T = {}, {}
        
        # for i in range(len(s)):
            
        #     set_S[s[i]] = 1 + set_S.get(s[i], 0)
        #     set_T[t[i]] = 1 + set_T.get(t[i], 0)


        # return set_S == set_T
    
#---------------------------- Another Solutions -----------

        # set_S, set_T = defaultdict(int), defaultdict(int)
        
        # for i in range(len(s)):
            
        #     set_S[s[i]] += 1
        #     set_T[t[i]] += 1

        # return set_S == set_T
        
#---------------------------- Another Solutions -----------

        # return sorted(s) == sorted(t)
#-----------------------------------------------------
        # return Counter(s) == Counter(t)
        