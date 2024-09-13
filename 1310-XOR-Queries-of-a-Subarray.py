class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        XOR = []
        hashMap = {}

        for q in queries:
            if str(q) in hashMap:
                XOR.append(hashMap[str(q)])
            else:
                nums = arr[q[0]: q[1]+1]
                n = 0
                for num in nums:
                    n ^= num
                XOR.append(n)

                hashMap[str(q)] = n

        return XOR

                

        