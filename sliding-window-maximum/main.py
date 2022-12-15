class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)

        start, end = 0, 0 + k

        ls = []
        while end <= n:
            window = nums[start:end]
            ls.append(max(window))
            start += 1
            end += 1

        return ls
