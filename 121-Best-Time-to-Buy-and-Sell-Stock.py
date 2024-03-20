class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        less_price = prices[0]
        max_profit =  0 
    
        for today_price in prices:
            if today_price < less_price:
                less_price = today_price 
            else:
                cur_profit = today_price - less_price
                max_profit = max(max_profit, cur_profit)

        return max_profit


# ---------------- Solution using two pointers technique ----

        # l, r = 0, 1        
        # max_profit = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         cur_profit = prices[r] - prices[l]
        #         max_profit = max(max_profit , cur_profit)
        #     else:
        #         l = r
        #     r += 1
         
        # return max_profit
        