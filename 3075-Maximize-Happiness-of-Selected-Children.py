class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        _sum = 0
        happiness = sorted(happiness)

        for i in range(1, k+1):
            happy = happiness.pop()

            if happy > 0:
                _sum = _sum + happy
            else:
                _sum += 0

            if happiness:
                happiness[-1] = happiness[-1] - i

        return _sum
