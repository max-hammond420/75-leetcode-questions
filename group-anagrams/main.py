from collections import Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        counters =  []
        ls = []
        for i in strs:
            if Counter(i) not in counters:
                counters.append(Counter(i))
                ls.append([i])
            else:
                for j in ls:
                    if Counter(j[0]) == Counter(i):
                        j.append(i)
        return ls


strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(Solution, strs))

