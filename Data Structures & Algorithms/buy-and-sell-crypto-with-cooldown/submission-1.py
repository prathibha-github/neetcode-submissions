from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def best(day, holding_coin):
            if day >= len(prices):
                return 0
            if holding_coin:
                sell = prices[day]+best(day+2, not holding_coin)
                wait = best(day+1, holding_coin)
                return max(sell, wait)
            else:
                buy = -prices[day]+best(day+1, True)
                wait = best(day+1, False)
                return max(buy, wait)
        return best(0, False)