class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(scratch: List[int], nums):
            if len(nums) == 0:
                result.append(scratch)
            else:
                for i in range(len(nums)):
                    helper(scratch+[nums[i]], nums[:i]+nums[i+1:])
        helper([], nums)
        return result