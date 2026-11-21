class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [0] * (n)
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
        return max(dp)
        