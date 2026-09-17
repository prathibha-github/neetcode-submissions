class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        profit = -1
        for price in prices:
            if price < minPrice:
                minPrice = price
            profit = max(profit, price-minPrice)
        return profit
        