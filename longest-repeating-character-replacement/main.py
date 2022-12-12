class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        begin, end = 0, 0

        count = {}
        longest = 0

        while end < len(s):
            count[s[end]] = 1 + count.get(s[end], 0)

            while (end - begin + 1) - max(count.values()) > k:
                count[s[begin]] += -1
                begin += 1

            longest = max(longest, end - begin + 1)

            end += 1

        return longest

s = "ABABBA"
k = 2
print(Solution.characterReplacement(Solution, s, k))
