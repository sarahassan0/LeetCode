class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        for i in range(k):
            n = nums.pop()
            nums.insert(0, n)
        return nums

#-------------------------------------------------------------

        # k %= len(nums)
        # nums[:] = nums[-k:] + nums[:-k]


