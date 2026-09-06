class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        result = []
        for str in strs:
            sorted_str = "".join(sorted(str))
            map[sorted_str].append(str)
        for key, value in map.items():
            result.append(value)
        return result
                