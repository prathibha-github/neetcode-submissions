class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ways = {0: 1}
        for num in nums:
            next_ways = defaultdict(int)
            for current_sum, count in ways.items():
                next_ways[current_sum + num] += count
                next_ways[current_sum - num] += count
            ways = next_ways
        return ways[target] if target in ways else 0