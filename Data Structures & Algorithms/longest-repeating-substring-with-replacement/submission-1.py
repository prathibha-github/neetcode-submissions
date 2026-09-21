class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counts = defaultdict(int)
        max_count = 0
        start = 0
        for end, char in enumerate(s):
            counts[char] = counts[char]+1
            max_count = max(max_count, counts[char])
            while (end - start + 1) - max_count > k:
                counts[s[start]] -= 1
                start += 1
            longest = max(longest, end - start +1)
        return longest