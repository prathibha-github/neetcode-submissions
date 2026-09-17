class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxPrice = float('-inf')
        profit = -1
        for i, price in enumerate(prices):
            if price < minPrice:
                minPrice = price
            profit = max(profit, price-minPrice)
        return profit
        