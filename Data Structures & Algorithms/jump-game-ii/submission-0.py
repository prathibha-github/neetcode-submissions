class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        start = 0
        end = 0
        farthest = 0
        count = 0
        while end < n-1:
            farthest = end
            for i in range(start, end+1):
                farthest = max(farthest, i + nums[i])
            start = end + 1
            end = farthest
            count += 1
        return count