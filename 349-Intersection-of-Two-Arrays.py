class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        intersect = []

        for num in nums1:
            if num in nums2 and num not in intersect:
                intersect.append(num)

        return intersect


#####################################################

    # def intersection(self, nums1, nums2):
    #     s1 = set(nums1)
    #     s2 = set(nums2)
    #     return s1.intersection(s2)


        # return s1 & s2


        