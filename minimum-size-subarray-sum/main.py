import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        if (n == 0):
            return 0

        i = 0
        j = 0
        minimum = sys.maxsize
        sub_array = []

        while (j < n):
            if sum(sub_array) < target and i < n:
                sub_array.append(nums[i])
                i += 1
            elif sum(sub_array) >= target:
                minimum = min(minimum, len(sub_array))
                sub_array.pop(0)
                j += 1
            else:
                j += 1

        if (minimum == sys.maxsize):
            return 0

        return minimum

t = [1, 4, 4]
u = [2,3,1,2,4,3]
v = [1,1,1,1,1,1,1,1]
print(Solution.minSubArrayLen(Solution, 11, v))
