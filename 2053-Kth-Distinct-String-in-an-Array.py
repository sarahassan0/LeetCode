class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)

        for c, n in count.items():
            if n == 1:
                k -= 1
                if k == 0 :
                    return c
        
        return ""
        
        