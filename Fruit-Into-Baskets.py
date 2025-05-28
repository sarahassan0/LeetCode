class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        max_ = 0
        basket = defaultdict(int)

        while r < len(fruits):
            basket[fruits[r]] += 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1

            max_ = max(max_, r - l + 1)
            r += 1

        return max_


# ------------ Brute force solution with time limt exeeds ---------

        # if len(fruits) == 1:
        #     return 1

        # max_ = 0
        # n = len(fruits)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if len(set(fruits[i:j+1])) <= 2:
        #             max_ = max(max_, j + 1 - i)
        #         else:
        #             break
        # return max_
        