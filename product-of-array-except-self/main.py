class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        if n == 1:
            return 0

        left = [1] * n
        right = [1] * n
        
        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]


        for i in range(n-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]


        for i in range(n):
            right[i] *= left[i]

        return right

