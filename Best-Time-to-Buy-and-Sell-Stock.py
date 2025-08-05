class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        less_price, max_profit = prices[0], 0

        for price in prices:
            if price < less_price:
                less_price = price
            else:
                profit = price - less_price 
                max_profit = max(profit, max_profit)
        return max_profit


# ---------------- Solution using two pointers technique ----

        # l, r = 0, 1
        # max_profit = 0

        # while r < len(prices):
        #     if prices[r] > prices[l]:
        #         profit = prices[r] - prices[l]
        #         max_profit = max(profit, max_profit)
        #     else:
        #         l = r
        #     r += 1
        # return max_profit

#-------------------- Time limit in case 200 -----------

        # maxi = 0
        
        # for i in range(1, len(prices)):
        #     profit =  max(prices[i:]) - prices[i-1]
        #     maxi = max(profit, maxi)
        

        # return 0 if maxi <= 0 else maxi


        