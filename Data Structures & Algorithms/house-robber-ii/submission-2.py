class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def rob_line(start, end):
            two = 0
            one = 0
            for i in range(start, end+1):
                current = max(one, nums[i-1]+two)
                two = one
                one = current
            return one
        n = len(nums)
        line1 = rob_line(1, n-1)
        line2 = rob_line(0, n-2)
        return max(line1, line2)