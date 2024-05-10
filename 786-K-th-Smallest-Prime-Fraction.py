class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = []

        for i in range(len(arr)):
            for j in arr[i+1:]:
                heappush(fractions, (arr[i] / j, (arr[i], j)))        

        for _ in range(k - 1):
            heappop(fractions)

        return heappop(fractions)[1]
        