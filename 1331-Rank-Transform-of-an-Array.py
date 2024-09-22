class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n =  sorted(set(arr))
        rank = []
        hashMap = {}
        for i in range(len(n)):
            hashMap[n[i]] = i + 1

        for num in arr:
            rank.append(hashMap[num])
                

        return rank

        

        