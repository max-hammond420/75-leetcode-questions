class Solution:
    def maxArea(self, height: list[int]) -> int:
        greatest = 0
        l, r = 0, len(height) - 1

        while l < r:
            b = r - l
            h = min(height[l], height[r])
            print(b * h)
            if height[l] < height[r]:
                l += 1
            else:
                r += -1
            greatest = max((b * h), greatest)
            
        return greatest

height = [1,2,3,4,5,25,24,3,4]
print(Solution.maxArea(Solution, height))
