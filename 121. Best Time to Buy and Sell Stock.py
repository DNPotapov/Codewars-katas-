'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if sorted(prices) == prices[::-1]:
            return 0
        buy = 0
        sell = 1
        res = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                if (prices[sell] - prices[buy]) > res:
                    res = prices[sell] - prices[buy]
            else:
                buy = sell
            sell += 1
        return res