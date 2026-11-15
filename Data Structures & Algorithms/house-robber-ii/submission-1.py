class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def rob_line(values):
            if not values:
                return 0
            n = len(values)
            dp = [0] * (n+1)
            dp[1] = values[0]
            for i in range(2, n+1):
                dp[i] = max(dp[i-1], values[i-1]+dp[i-2])
            return dp[n]
        line1 = rob_line(nums[1:])
        line2 = rob_line(nums[:-1])
        return max(line1, line2)