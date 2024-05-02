class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = sorted(nums)[::-1]
        print(nums)
        for num in nums:
            if num < 0:
                return -1
            elif -num in nums:
                return num
        
        return -1
        