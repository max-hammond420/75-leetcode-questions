class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if (n == 0):
            return 0

        i = 0
        j = 0
        current_greatest = 1
        substring = []

        while i < n:
            if s[i] not in substring:
                substring.append(s[i])
                i += 1
            else:
                substring.pop(0)
                j += 1

            current_greatest = max(current_greatest, i-j)


        return current_greatest
            


s = "pwwkew"
t = "abcabcbb"
u = "bbbbb"
print(Solution.lengthOfLongestSubstring(Solution, u))
