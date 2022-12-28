class Solution:
    def findMin(self, nums: List[int]) -> int:
        bot = 0
        top = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while bot <= top:
            mid = (bot + top) // 2

            if nums[mid-1] > nums[mid]:
                return nums[mid]

            elif nums[mid-1] < nums[mid]:
                top = mid
            else:
                bot = mid + 1

        return -1
