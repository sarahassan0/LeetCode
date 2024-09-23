class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answers = []

        for num in nums:
            answers.extend([ int(digit) for digit in str(num) ])

        return answers