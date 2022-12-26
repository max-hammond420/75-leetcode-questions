class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def find_row(matrix, target):
            for i in range(len(matrix)):
                if matrix[i][0] <= target and matrix[i][-1] >= target:
                    return i

            return None

        def binary_search(arr, target):
            low = 0
            high = len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid

            if low > len(arr) - 1:
                return False
            if arr[low] != target:
                return False
            return True

        if len(matrix) == 1:
            return binary_search(matrix[0], target)

        row = find_row(matrix, target)
        print(row)
        if row is None:
            return False

        return binary_search(matrix[row], target)
