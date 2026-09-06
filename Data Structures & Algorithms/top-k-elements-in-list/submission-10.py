class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        
        for num in nums:
            map[num] = map[num] + 1
        
        buckets = [[] for i in range(len(nums)+1)] 
        
        for key, value in map.items():
            buckets[value].append(key)
        
        result = []
        
        for i in range(len(buckets)-1, 0, -1):
            result.extend(buckets[i])
        return result[:k]