class Solution:
    def evalRPN(self, tokens: list[str]) -> int:


        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            else:
                # Truncate division toward zero
                result = int(a / b)

            stack.append(result)

        return stack[-1]
        