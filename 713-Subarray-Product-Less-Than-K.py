class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        counter = 0
        left , right = 0, 0
        product = 1

        while right < len(nums):
            product *= nums[right]

            while product >= k and left <= right:
                product /= nums[left]
                left += 1

            counter += right - left + 1
            right += 1

        return counter
