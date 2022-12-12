class Solution:
    def trap(self, height: list[int]) -> int:
        total = 0

        max_left = []
        max_right = []

        current_max = 0
        for i in range(len(height)):
            if i == 0:
                max_left.append(0)
            else:
                current_max = max(current_max, height[i-1])
                max_left.append(current_max)


        current_max = 0
        reverse_height = height[::-1]
        for i in range(len(height)):
            if i == 0:
                max_right.append(0)
            else:
                current_max = max(reverse_height[i-1], current_max)
                max_right.append(current_max)

        max_right = max_right[::-1]

        for i in range(len(height)):
            calc = min(max_left[i], max_right[i]) - height[i]
            if calc < 0:
                continue
            else:
                total += calc


        return total


height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
# height = [4, 2, 3]
print(Solution.trap(Solution, height))
