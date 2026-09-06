class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        max_value = float('-inf')
        for num in nums:
            count = map.get(num, 0)
            map[num] = count + 1
            if map[num] > max_value:
                max_value = map[num]
        
        buckets = [[] for i in range(max_value+1)] 
        
        for key, value in map.items():
            buckets[value].append(key)
        print(buckets)
        count = 0
        result = []
        
        for i in range(len(buckets)-1, 0, -1):
            result.extend(buckets[i])
            if len(result) == k:
                break
        return result