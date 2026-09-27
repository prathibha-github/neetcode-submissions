class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(path, remaining):
            if not remaining:
                result.append(path)
            else:
                helper(path, remaining[1:])
                helper(path+[remaining[0]], remaining[1:])
        helper([], nums)
        return result