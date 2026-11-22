from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = Counter(hand)
        for start in sorted(hand):
            if counts[start] == 0:
                continue
            for value in range(start, start+groupSize):
                if counts[value] == 0:
                    return False
                counts[value] -= 1
        return True
            