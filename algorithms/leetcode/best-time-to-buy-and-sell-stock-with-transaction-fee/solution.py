class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = -(2 ** 31 + 1)
        sell = 0

        for price in prices:
            sell = max(sell, buy + price)
            buy = max(buy, sell - price - fee)

        return sell