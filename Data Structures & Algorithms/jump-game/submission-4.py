from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        if len(nums) == 1:
            return True
        n = len(nums)
        i = 0
        farthest = 0
        while i < n:
            if farthest < i:
                return False
            farthest = max(farthest, i + nums[i])
            i += 1
        return True