class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        reachable_sums = {0}
        target = sum(nums) // 2
        print("target = ", target)
        for num in nums:
            new_sums = set()
            for previous_sum in reachable_sums:
                new_sum = num + previous_sum
                new_sums.add(new_sum)
            reachable_sums.update(new_sums)
        print(reachable_sums)
        return target in reachable_sums