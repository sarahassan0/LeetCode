class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count, candidate = 0, None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate 
        
#------------------------------------

        # count  = defaultdict(int)
        # candidate, maxCount = 0, 0

        # for num in nums:
        #     count[num] += 1
        #     if count[num] > maxCount:
        #         candidate = num
        #         maxCount = count[num]
        # return candidate


#---------------------------------
        # count  = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        
        # ele = max(count.values())
        # for k, v in count.items():
        #     if v == ele:
        #         return k


#------------------------------------

        # return Counter(nums).most_common()[0][0]
#------------------------------------
        # nums.sort()
        # return nums[len(nums) // 2]

