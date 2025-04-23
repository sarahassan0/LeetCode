class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        for i in range(n):
            if nums[i] not in nums[i+1:] and  nums[i] not in nums[:i]:
                return nums[i]


################### Another solution using XOR operator

        res = 0

        for num in nums:
            res ^= num
        
        return res