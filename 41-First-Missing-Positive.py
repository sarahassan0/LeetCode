class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)

        for i in range(len(nums)):
            if i+1 not in nums:
                return i+1

        return i+2