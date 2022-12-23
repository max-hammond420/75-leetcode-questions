class Solution:
    def isValid(self, s: str) -> bool:
        ls = []

        for i in s:
            if i in ['(', '[', '{']:
                ls.append(i)
            elif len(ls) == 0:
                return False
            elif i == ')' and ls[-1] == '(':
                ls.pop()
            elif i == '}' and ls[-1] == '{':
                ls.pop()
            elif i == ']' and ls[-1] == '[':
                ls.pop()
            else:
                return False

        if len(ls) == 0:
            return True
        return False
