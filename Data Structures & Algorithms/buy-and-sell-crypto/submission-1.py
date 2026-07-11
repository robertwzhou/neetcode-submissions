class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # move pointer forward, tracking lowest price
        lowest = prices[0]
        for i, price in enumerate(prices):
            lowest = min(lowest, price)
            profit = max(profit, price - lowest)
        return profit