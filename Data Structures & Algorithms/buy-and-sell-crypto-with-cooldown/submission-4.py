from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def best_profit(day, holding_coin):
            if day >= len(prices):
                return 0
            if holding_coin:
                sell = prices[day]+best_profit(day+2, False)
                wait = best_profit(day+1, True)
                return max(sell, wait)
            else:
                buy = -prices[day]+best_profit(day+1, True)
                wait = best_profit(day+1, False)
                return max(buy, wait)
        return best_profit(0, False)