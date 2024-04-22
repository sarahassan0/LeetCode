class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w = Counter(s1), len(s1)   

        for i in range(len(s2)):
            if s2[i] in cntr: 
                cntr[s2[i]] -= 1
            if i >= w and s2[i-w] in cntr: 
                cntr[s2[i-w]] += 1

            if all([cntr[i] == 0 for i in cntr]): # see optimized code below
                return True

        return False






    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     cntr, w, match = Counter(s1), len(s1), 0     

    #     for i in range(len(s2)):
    #         if s2[i] in cntr:
    #             if not cntr[s2[i]]:
    #                 match -= 1
    #                 print(s2[i],cntr)
    #             cntr[s2[i]] -= 1
    #             if not cntr[s2[i]]: match += 1

    #         if i >= w and s2[i-w] in cntr:
    #             if not cntr[s2[i-w]]: match -= 1
    #             cntr[s2[i-w]] += 1
    #             if not cntr[s2[i-w]]: match += 1

    #         if match == len(cntr):
    #             return True

    #     return False