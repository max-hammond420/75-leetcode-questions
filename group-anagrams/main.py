from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict = defaultdict(list)
        ls = []
        for s in strs:
            count = [0] * 26 # a .. z
            for c in s:
                count[ord(c) - ord('a')] += 1

            dict[tuple(count)].append(s)

        for v in dict.values():
            ls.append(v)

        return ls


strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(Solution, strs))

