class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        writing_idx = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[writing_idx] = 0, nums[i] # in thia Case [1], it gives wrong anser here if i switch the assining because it override and give answer of [0] istead of [1]

                writing_idx += 1 

        # nums[writing_idx:] = [0] * ( len(nums) - writing_idx)  #this is more safer
            