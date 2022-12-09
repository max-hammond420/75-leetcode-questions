from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        count = Counter(nums)
        count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1])}

        return list(count)[::-1][:k]

nums = [1,1,1,2,2,3]
k = 2
print(Solution.topKFrequent(Solution, nums, k))

