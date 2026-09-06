class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(str))
            map[sorted_str].append(str)
        
        result = []
        for value in map.values():
            result.append(value)
        return result
                