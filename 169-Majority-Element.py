class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occ = {}

        for i in nums:
            if str(i) not in occ:
                occ[str(i)] = 0
            occ[str(i)] +=1
        
        ele = max(occ.values())
        for k in occ.keys():
            if occ[k] == ele and ele > len(nums)//2:
                return int(k)

        #########  Another Solution  ###############
        # occ = {}
        # for i in nums:
        #     if str(i) not in occ:
        #         occ[str(i)] = 0
        #     occ[str(i)] +=1

        # key = nums[0]
        # ele = occ[str(key)]
        # for k in occ.keys():
        #     if occ[k] > ele:
        #         ele = occ[k]
        #         key = k
        # return int(key)
        


        #########  Another Solution  ###############

            # majority_candidate = None
            # count = 0
            
            # for num in nums:
            #     if count == 0:
            #         majority_candidate = num
            #     count += (1 if num == majority_candidate else -1)
            
            # return majority_candidate