class Solution:
    def trap(self, height: list[int]) -> int:
        total = 0

        i = 0
        while i < len(height):
            offset = 1
            local_total = 0
            while i + offset < len(height):
                # print(height[i])
                # print(max(height[i+1:]))
                # print()
                if height[i+offset] < height[i] and height[i] <= max(height[i+1:]):
                    print(height[i] - height[i+offset])
                    local_total += height[i] - height[i+offset]

                else:
                    break

                offset += 1

            total += local_total
            i += offset

        return total


# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4, 2, 3]
print(Solution.trap(Solution, height))
