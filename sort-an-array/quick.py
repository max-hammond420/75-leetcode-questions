class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        s = 1
        e = len(nums) - 1

        return self.quick_sort(nums, s, e)

    def quick_sort(self, nums, s, e):
        if e - s + 1 <= 1:
            return

        pivot = nums[e]
        left = s

        for i in range(s, e):
            if nums[i] < pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

        nums[e] = nums[left]
        nums[left] = pivot

        self.quick_sort(nums, s, left + 1)
        self.quick_sort(nums, left + 1, e)

        return nums


print(Solution.sortArray(Solution, [5, 2, 3, 1]))
