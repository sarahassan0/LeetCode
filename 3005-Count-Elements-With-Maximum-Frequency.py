class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        frequency = Counter(nums).values()
        max_frequency = max(frequency)

        total_freq = [freq for freq in frequency if freq == max_frequency]

        return sum(total_freq)

    