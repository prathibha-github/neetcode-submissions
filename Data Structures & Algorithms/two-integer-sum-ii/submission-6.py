class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = dict()
        result = []
        for i, num in enumerate(numbers):
            hmap[num] = i
        for i, num in enumerate(numbers):
            other_num = (target - num)
            other_index = -1
            if other_num in hmap:
                other_index = hmap[other_num]
            if other_index <= i:
                continue
            result = [i+1, other_index+1]
            break
        return result