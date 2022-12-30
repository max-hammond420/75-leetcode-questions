class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []
        for i in operations:
            print(i)
            if i == "+":
                stack.append(stack[-1] + stack[-2])
            elif i == "D":
                a = stack.pop()
                stack.append(a)
                stack.append(a*2)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
            print(stack)

        return sum(stack)
