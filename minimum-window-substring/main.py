import sys

class Solution:


    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if n > m:
            return ""
        if s == t:
            return s

        output = ""
        minimum = sys.maxsize

        start, end = 0, 0

        def containsAll(str, set):
            """ Check whether sequence str contains ALL of the items in set. """
            return 0 not in [c in str for c in set]

        while end < m-1:

            while (not containsAll(s[start:end+1], t)):
                end += 1
            while (containsAll(s[start:end+1], t)):
                current_output = s[start:end+1]
                start += 1

            if (end-start + 1) < minimum:
                minimum = end-start + 1
                output = current_output

        return output


s = "ab"
t = "a"
print(Solution.minWindow(Solution, s, t))
