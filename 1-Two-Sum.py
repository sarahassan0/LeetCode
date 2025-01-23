class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashMap:
                return [i, hashMap[comp]]
        
            hashMap[nums[i]] = i
        return []

################
        # for i in range(len(nums)):
        #     comp = target - nums[i]
        #     if comp in nums[i+1:]:
        #         return [i, nums.index(comp, i+1)]

        # return []
        