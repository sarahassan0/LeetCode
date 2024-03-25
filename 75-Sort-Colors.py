class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        for i in range(length):
            for j in range(i+1 , length):
                if nums[i] > nums[j]:
                    min = nums[j]
                    nums[j] = nums[i]
                    nums[i] = min