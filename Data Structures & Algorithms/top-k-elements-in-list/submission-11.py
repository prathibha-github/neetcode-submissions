class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] = counts[num] + 1
        
        buckets = [[] for i in range(len(nums)+1)] 
        
        for key, value in counts.items():
            buckets[value].append(key)
        
        result = []
        
        for i in range(len(buckets)-1, 0, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                break
        return result[:k]