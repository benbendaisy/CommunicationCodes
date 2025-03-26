from typing import List


class Solution:
    """
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

    Note that division between two integers should truncate toward zero.

    It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

    Example 1:

    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9
    Example 2:

    Input: tokens = ["4","13","5","/","+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6
    Example 3:

    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22
    """
    def evalRPN1(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a // b
        }
        cur_pos = 0
        while len(tokens) > 1:
            # Move the current position pointer to the next operator.
            while tokens[cur_pos] not in "+-*/":
                cur_pos += 1

            # Extract the operator and numbers from the list.
            operator = tokens[cur_pos]
            num1 = int(tokens[cur_pos - 2])
            num2 = int(tokens[cur_pos - 1])

            # Calculate the result to overwrite the operator with.
            operation = operations[operator]
            tokens[cur_pos] = operation(num1, num2)

            # Remove the numbers and move the pointer to the position
            # after the new number we just added.
            tokens.pop(cur_pos - 2)
            tokens.pop(cur_pos - 2)
            cur_pos -= 1

        return tokens[0]

    def evalRPN2(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }
        stack = []
        for token in tokens:
            if token in operations:
                num2 = stack.pop()
                num1 = stack.pop()
                operation = operations[token]
                stack.append(operation(num1, num2))
            else:
                stack.append(int(token))
        return stack.pop()
    
    def evalRPN3(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b) 
        }
        stack = []
        for token in tokens:
            if token in operations:
                b = stack.pop()
                a = stack.pop()
                operation = operations[token]
                stack.append(operation(a, b))
            else:
                stack.append(int(token))
        return stack.pop()

    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }

        stack = []
        for token in tokens:
            if token in operations:
                y, x = stack.pop(), stack.pop()
                operation = operations[token]
                val = operation(x, y)
                stack.append(val)
            else:
                stack.append(int(token))
                
        return stack.pop()
