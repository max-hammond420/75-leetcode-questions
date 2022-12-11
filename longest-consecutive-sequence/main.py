class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        nums_set = set(nums)
        longest_consecutive = 0

        for n in nums:
            if n - 1 not in nums_set:
                current_consecutive = 1
                while n + current_consecutive in nums_set:
                    current_consecutive += 1

                longest_consecutive = max(longest_consecutive, current_consecutive)

        return longest_consecutive
    

nums = [100,4,200,1,3,2] # = 4
print(Solution.longestConsecutive(Solution, nums))
