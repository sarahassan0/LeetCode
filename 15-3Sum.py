class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # dic = {}
        # arr = []

        # for i, num in enumerate(nums):

        #     if num not in dic:
        #         dic[num] = i

        #     for j in range(i+1, len(nums)):
        #         complete = 0 - (num + nums[j])

        #         if complete in dic and  len(set([i, j, dic[complete]])) == 3:
        #             sub_arr = sorted([num, nums[j], complete])
        #             if  sub_arr not in arr:
        #                 arr.append(sub_arr)
        # return arr


# ------------------------- 2 Pointers Solution


        nums.sort()
        result = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
        return result


