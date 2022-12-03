class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        if (n == 1):
            return nums[0]

        greatest_sum = nums[0]

        for i in range(n):
            for j in range(n+1):
                if len(nums[i:j+1]) == 0:
                    continue
                current_sum = sum(nums[i:j+1])
                if current_sum > greatest_sum:
                    greatest_sum = current_sum

        return greatest_sum

print(Solution.maxSubArray(Solution, [-2, -1]))
