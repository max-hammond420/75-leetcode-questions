class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            if nums[i] in new_nums:
                return True
        return False
