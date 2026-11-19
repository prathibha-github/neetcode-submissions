class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount == 0:
            return 0
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for current_amount in range(1, amount+1):
            for coin in coins:
                if coin <= current_amount:
                    dp[current_amount] = min(dp[current_amount], 1+dp[current_amount-coin])
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
