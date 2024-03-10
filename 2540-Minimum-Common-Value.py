class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        nums1_S = set(nums1)
        nums2_S = set(nums2)
        common = nums1_S.intersection(nums2_S)
        return min(common) if common else -1
        

#---------------------- Another Solution --------

        # if nums1[-1] < nums2[0] or nums2[-1] < nums1[0]:
        #     return -1
        # i = nums1 if nums1[0]> nums2[0] else nums2
        # j = nums1 if i == nums2 else nums2
        # for num in i:
        #     if num in j:
        #         return num

        # return -1