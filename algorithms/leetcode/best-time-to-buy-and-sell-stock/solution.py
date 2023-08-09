class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = 0
        sell = 1
        max_profit = 0

        while sell < n:
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)
            if profit < 0:
                buy = sell
            sell += 1
        return max_profit