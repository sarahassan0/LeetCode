class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l, r = 0, 1
    
        while r < len(nums): 
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]

            r += 1
        return l +1
#-------------------------------

        # l, r, writing_idx = 0,1,1

        # while r < len(nums):
        #     if nums[r] != nums[l]:
        #         nums[writing_idx] = nums[r]
        #         l += 1
        #         writing_idx = l+1
        #     r += 1
        # return writing_idx