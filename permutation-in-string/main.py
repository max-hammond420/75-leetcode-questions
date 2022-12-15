from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        start, end = 0, len(s1)

        while end <= len(s2):
            if Counter(s2[start:end]) == Counter(s1):
                return True
            start += 1
            end += 1
        return False

# s1 = "ba"
# s2 = "eidboaoo"


s1 = "adc"
s2 = "dcda"

print(Solution.checkInclusion(Solution, s1, s2))
