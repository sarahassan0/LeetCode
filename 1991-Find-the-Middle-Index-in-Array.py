class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = 0

        for i in range(len(nums)):
            if sum(nums[0:i+1]) == sum(nums[i:len(nums)+1]):
                return i

        return -1

        