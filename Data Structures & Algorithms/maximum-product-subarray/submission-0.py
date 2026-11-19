class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        previous_max = nums[0]
        previous_min = nums[0]
        result = nums[0]
        for i in range(1, n):
            candidates = (nums[i], nums[i]*previous_max, nums[i]*previous_min)
            current_max = max(candidates)
            current_min = min(candidates)
            previous_max = current_max
            previous_min = current_min
            result = max(result, current_max)
        return result