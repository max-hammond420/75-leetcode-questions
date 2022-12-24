class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operations = ['+', '-', '/', '*']

        for i in tokens:
            if i not in operations:
                stack.append(int(i))
            else:
                print(i)
                if i == '+':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1 + num2)
                elif i == '-':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 - num1)
                elif i == '*':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1 * num2)
                elif i == '/':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(num2 / num1))

            print(stack)

        return stack[0]


nums = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution.evalRPN(Solution, nums))
