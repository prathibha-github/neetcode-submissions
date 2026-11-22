class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_positions = {}
        for index, ch in enumerate(s):
            last_positions[ch] = index
        result = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, last_positions[s[i]])
            if i == end:
                length = (end - start +1)
                start = i+1
                result.append(length)
        return result
                