class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

#------------------- O(n log n) time, O(n) space -----

        indices = []

        for i, n in enumerate(nums):
            indices.append([n, i])
        indices.sort()

        r, l = 0, len(nums) - 1

        while r < l:
            summ = indices[r][0] + indices[l][0]
            if summ == target:
                return [indices[r][1], indices[l][1]]
            elif summ > target:
                l -= 1
            else:
                r += 1
        return []
#------------------- O(n) time, O(n) space -----
        # diffs = {}
        
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in diffs:
        #         return [diffs[diff], i]
        #     diffs[n] = i


# ------------------- O(n2) time ------------------ 
        # n = len(nums)

        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

