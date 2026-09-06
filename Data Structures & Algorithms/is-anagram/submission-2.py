class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = dict()
        for c in s:
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        for c in t:
            if c in hashmap:
                count = hashmap[c]
                count -= 1
                if count >= 1:
                    hashmap[c] = count
                else:
                    hashmap.pop(c)
            else:
                return False
        return not hashmap