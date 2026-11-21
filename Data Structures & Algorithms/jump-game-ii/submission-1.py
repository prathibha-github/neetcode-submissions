class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        current_end = 0
        farthest = 0
        count = 0
        for i in range(n-1):
            farthest = max(farthest, i+nums[i])
            if i == current_end:
                count += 1
                current_end = farthest
        return count