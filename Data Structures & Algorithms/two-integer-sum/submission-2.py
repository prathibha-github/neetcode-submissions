class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        for i, num in enumerate(nums):
            hm[num] = i
        
        for i, num in enumerate(nums):
            remaining = target - num
            
            if remaining in hm:
                if i == hm[remaining]:
                    continue
                return [i, hm[remaining]]