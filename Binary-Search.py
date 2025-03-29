class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
            
        return -1

#-------------------- Recursive solution, time O(logn), space O(logn)-------
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         return self.binarySearch(0, len(nums) - 1, nums, target)

#     def binarySearch(self, low, high, nums, target):
#         if low > high:
#             return -1 
#         mid = low + ((high - low) // 2)
        
#         if  target == nums[mid]:
#             return mid
#         elif target > nums[mid]:
#             return self.binarySearch(mid + 1, high, nums, target)
#         else:
#             return  self.binarySearch(low, mid - 1, nums, target)

