class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if  total % 2 == 1:
            return False
        reachable_sums = {0}
        target = sum(nums) // 2
        for num in nums:
            new_sums = set()
            for previous_sum in reachable_sums:
                new_sum = num + previous_sum
                new_sums.add(new_sum)
                if new_sum > target:
                    break
            reachable_sums.update(new_sums)
        return target in reachable_sums