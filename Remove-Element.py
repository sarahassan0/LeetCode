class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        writing_idx = 0
        for n in nums:
            if n != val:
                nums[writing_idx] = n
                writing_idx += 1
        return writing_idx

    #-------------------------------

        # i, n = 0, len(nums)-1

        # while i <= n:
        #     if nums[i] == val:
        #         nums[i] = nums[n]
        #         n -= 1
        #     else:
        #         i += 1
        # return i 
#-----------------------------------------------------

        # tmp = []

        # for n in nums:
        #     if n != val:
        #         tmp.append(n)
        # for i in range(len(tmp)):
        #     nums[i] = tmp[i]

        # return len(tmp)

        



       