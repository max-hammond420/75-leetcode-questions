class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        s = 0
        e = len(nums) - 1

        return self.merge_sort(nums, s, e)

    def merge_sort(self, nums, s, e):
        if e - s + 1 <= 1:
            return nums

        m = (s + e) // 2

        # divide and conquor
        self.merge_sort(nums, s, m)
        self.merge_sort(nums, m+1, e)

        # merge sorted halves
        self.merge(nums, s, m, e)

        return nums

    # merge in place
    def merge(self, nums, s, m, e):
        L = nums[s:m+1]
        R = nums[m+1:e+1]

        i = 0
        j = 0
        k = s

        # merge 2 lists
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1
