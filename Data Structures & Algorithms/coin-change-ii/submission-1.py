class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0] * (amount + 1)
        ways[0] = 1
        for coin in coins:
            # print("outside the loop coin = ", coin)
            for total in range(coin, amount+1):
                ways[total] += ways[total - coin]
                # print(ways)
        return ways[amount]