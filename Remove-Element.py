class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1

        return idx
    #-------------------------------

        # i, n = 0, len(nums) 

        # while i < n:
        #     if nums[i] == val:
        #         n -= 1
        #         nums[i] = nums[n]
        #     else:
        #         i += 1
        # return n
#-----------------------------------------------------

        # tmp = []

        # for n in nums:
        #     if n != val:
        #         tmp.append(n)
        # for i in range(len(tmp)):
        #     nums[i] = tmp[i]

        # return len(tmp)




