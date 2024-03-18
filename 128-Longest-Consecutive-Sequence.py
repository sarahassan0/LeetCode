class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        longest = 0

        for n in num_set:

            if n - 1 not in num_set:
                length = 0 
                while n + length in num_set:
                    length += 1
                
                longest = max(longest, length)
        
        return longest



# -------------------------- Another solution using sorting---------

#         if not nums:
#             return 0

#         nums = sorted(nums)
#         counter, longest = 1, 1
    
#         for i in range(len(nums)):
#             if i < len(nums)-1:
#                 if nums[i+1] - nums[i] == 1:
#                     counter += 1
#                     continue
#                 elif nums[i+1] - nums[i] == 0: continue
    
#             longest = max(counter, longest)
#             counter = 1

#         return longest 