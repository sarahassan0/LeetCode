class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappeared_numbers = []
        n = len(nums)
        nums = set(nums)

        for i in range(n):
            if i+1 not in nums:
               disappeared_numbers.append(i+1)

        return disappeared_numbers 
        