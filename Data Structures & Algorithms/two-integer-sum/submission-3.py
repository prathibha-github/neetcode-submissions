class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        
        for i, num in enumerate(nums):
            remaining = target - num
            
            if remaining in hm:
                return [hm[remaining], i]
            hm[num] = i