class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(path, remaining):
            if not remaining:
                result.append(path)
                return
            for i in range(len(remaining)):
                    helper(path+[remaining[i]], remaining[:i]+remaining[i+1:])
        helper([], nums)
        return result