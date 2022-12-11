class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        index_1 = 0
        index_2 = len(numbers) - 1

        while index_1 < len(numbers):
            if numbers[index_1] + numbers[index_2] > target:
                index_2 += -1
            elif numbers[index_1] + numbers[index_2] < target:
                index_1 += 1
            else:
                return [index_1 + 1, index_2 + 1]
                

