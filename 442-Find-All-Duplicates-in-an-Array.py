class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        result = []
        
        for i in range(1,len(nums)):
            if sorted_nums[i] == sorted_nums[i-1]:
                    result.append(sorted_nums[i])

        return result




#-------------- good solution but it runs in O(n^2) --------------

        # result = []
        # for i in range(len(nums)):
        #     if nums[i] in nums[i+1:]:
        #         result.append(nums[i])
        
        # return result