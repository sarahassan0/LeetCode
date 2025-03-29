class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l


#------------ linear search , O(n) ------
        # for i in range(len(nums)):
        #     if target <= nums[i]:
        #         return i
        # return len(nums)
        