from collections import Counter


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        nums = Counter(nums)

        for k in nums:
            if nums[k] > 2:
                return k

        return -1


print(Solution.findDuplicate(Solution, [1, 2, 3, 4, 3, 3]))
