class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in nums1:
            
            greater = -1
            index = nums2.index(i)
    
            for num in nums2[index+1:]:
                if num > i:
                    greater = num
                    break
 
            ans.append(greater)

        return ans