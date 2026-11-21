class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        current_possible_reach = 0
        max_possible_reach = 0
        jumps = 0

        for index in range(n-1):
            max_possible_reach = max(max_possible_reach, index+nums[index])
            if index == current_possible_reach:
                jumps += 1
                current_possible_reach = max_possible_reach
        return jumps