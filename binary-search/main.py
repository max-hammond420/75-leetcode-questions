class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        if low > len(nums)-1:
            return -1
        elif nums[low] != target:
            return -1

        return low
