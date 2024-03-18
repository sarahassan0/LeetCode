class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current_length = 0                
                while num + current_length  in num_set:
                    current_length += 1
                
                longest = max(longest, current_length)
        
        return longest
