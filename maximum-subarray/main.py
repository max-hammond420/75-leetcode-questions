import sys


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        greatest_sum = -sys.maxsize - 1
        n = len(nums)

        begin = 0
        end = 0

        while end < n:
            current_sum = sum(nums[begin:end+1])
            if current_sum > greatest_sum:
                greatest_sum = current_sum
                begin += 1
                current_sum = nums[begin:end+1]
            end += 1

        return greatest_sum


ls = [5, 4, -1, 7, 8]
print(ls)
print(Solution.maxSubArray(Solution, ls))
