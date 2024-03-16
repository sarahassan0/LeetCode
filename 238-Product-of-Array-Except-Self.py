class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [0] * len(nums)
        n, zero = 1, 0
        for i in range(len(nums)):
            if nums[i] != 0:
                n *= nums[i]
            if nums[i] == 0:
                zero += 1

        if zero > 1:
            return answer

        for j in range(len(nums)):
            if zero == 0:
                answer[j] = (n//nums[j])
            elif zero == 1 and nums[j] == 0:
                answer = [0] * len(nums)
                answer[j] = n

        return answer




################ valid but O(n)square ########

        # answer = [1] * len(nums) 
        # for i in range(len(nums)):
        #     n = 1
        #     for j in range(len(nums)):
        #         if j != i and nums[j] != 1:
        #             n *= nums[j]
        #             answer[i] = (n)
        # return answer