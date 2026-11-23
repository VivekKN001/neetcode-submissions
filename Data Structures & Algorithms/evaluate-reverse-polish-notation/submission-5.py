class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in operators:
                print
                stack.append(int(i))
            else:
                number1 = stack.pop(-1)
                number2 = stack.pop(-1)
                if i == "+":
                    result = number1 + number2
                elif i == "-":
                    result = number2 - number1
                elif i == "*":
                    result = number1 * number2
                else:
                    result = int(number2 / number1)
                    print(result)
                stack.append(result)
        return round(stack[-1])