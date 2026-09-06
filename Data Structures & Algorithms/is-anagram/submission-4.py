class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = dict()
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        for c in t:
            if c not in hashmap:
                return False
            hashmap[c] -= 1
            if hashmap[c] == 0:
                del hashmap[c]
        return not hashmap