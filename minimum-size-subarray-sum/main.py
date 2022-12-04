import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        if (n == 0):
            return 0

        i = 0
        j = 0
        minimum = sys.maxsize
        sub_array = [nums[0]]

        while (i < n):
            if sum(sub_array) >= target:
                minimum = min(minimum, len(sub_array))
                i += 1
            else:
                pass

        return minimum
