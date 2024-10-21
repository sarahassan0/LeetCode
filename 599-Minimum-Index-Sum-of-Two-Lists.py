class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        dic = {}

        for i, v in enumerate(list1):
            if v in list2:
                dic[v] = i + list2.index(v)

        dic = sorted(dic.items(), key=lambda x: x[1])
        minimum = dic[0][1]
        return [x[0] for x in dic if x[1]==minimum]

