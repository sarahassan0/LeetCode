class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = sorted(nums)
        for i in range(1, len(nums)):
            if n[i-1] == n[i]:
                return n[i]
        