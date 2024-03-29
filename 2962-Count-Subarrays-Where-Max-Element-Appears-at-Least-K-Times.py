class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        left = right = count = max_count = result = 0
        max_element = max(nums)

        for right in range(len(nums)):

            if nums[right] == max_element:
                count += 1
        
            while count >= k:
                result += len(nums) - right

                if nums[left] == max_element:   
                    count -= 1
        
                left += 1
            
        return result
