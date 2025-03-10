class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hash set solution => time O(n), space O(n)
        # unique = set()

        # for i in nums:
        #     if i in unique:
        #         return True

        #     unique.add(i)

        # return False

        #------------------------------
        # sorting solution => time O(n log n), space O(1) in python, because it's in place sorting
        
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
