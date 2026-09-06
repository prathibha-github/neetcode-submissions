class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        for i, num in enumerate(nums):
            hm[num] = i
        print(hm)
        for i, num in enumerate(nums):
            remaining = target - num
            print("num=", num, "remaining=", remaining)
            if remaining in hm:
                if i == hm[remaining]:
                    continue
                print(i, hm[remaining])
                return [i, hm[remaining]]