class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        freq = defaultdict(int)
        left = max_good = 0
    
        for right in range(len(nums)):

            freq[nums[right]] += 1

            while freq[nums[right]] > k :
                freq[nums[left]] -= 1
                left +=1

            max_good = max(max_good, right - left + 1 )  

        return max_good
        