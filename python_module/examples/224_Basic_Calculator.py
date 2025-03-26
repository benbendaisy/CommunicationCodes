class Solution:
    """
        Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

        Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

        Example 1:

        Input: s = "1 + 1"
        Output: 2
        Example 2:

        Input: s = " 2-1 + 2 "
        Output: 3
        Example 3:

        Input: s = "(1+(4+5+2)-3)+(6+8)"
        Output: 23
    """
    def calculate1(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative
        for ch in s:
            if ch.isdigit():
                # Forming operand, since it could be more than one digit
                operand = operand * 10 + int(ch)
            elif ch == "+":
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == "-":
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == "(":
                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)
                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0
            elif ch == ")":
                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0
        return res + sign * operand

    def calculate2(self, s: str) -> int:
        def evaluate_expr(stack):
            # If stack is empty or the expression starts with
            # a symbol, then append 0 to the stack.
            # i.e. [1, '-', 2, '-'] becomes [1, '-', 2, '-', 0]
            if not stack or type(stack[-1]) == str:
                stack.append(0)

            res = stack.pop()

            # Evaluate the expression till we get corresponding ')'
            while stack and stack[-1] != ')':
                sign = stack.pop()
                if sign == '+':
                    res += stack.pop()
                else:
                    res -= stack.pop()
            return res

        stack = []
        n, operand = 0, 0
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch.isdigit():
                # Forming the operand - in reverse order.
                operand += (10 ** n * int(ch))
                n += 1
            elif ch != " ":
                if n:
                    # Save the operand on the stack
                    # As we encounter some non-digit.
                    stack.append(operand)
                    n, operand = 0, 0
                if ch == "(":
                    res = evaluate_expr(stack)
                    stack.pop()
                    # Append the evaluated result to the stack.
                    # This result could be of a sub-expression within the parenthesis.
                    stack.append(res)
                # For other non-digits just push onto the stack.
                else:
                    stack.append(ch)
        # Push the last operand to stack, if any.
        if n:
            stack.append(operand)

        # Evaluate any left overs in the stack.
        return evaluate_expr(stack)
    
    def calculate3(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1  # 1 for positive, -1 for negative
        result = 0
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in "+-":
                result += sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result += sign * num
                num = 0
                result *= stack.pop()  # pop sign
                result += stack.pop()  # pop previous result
        
        return result + (sign * num)
    
    def calculate4(self, s: str) -> int:
        stack, num = [], 0
        sign, res = 1, 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in "+-":
                res += sign * num
                num = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        return res + (sign * num)
    
    def calculate(self, s: str) -> int:
        stack, num = [], 0
        sign, res = 1, 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in "+-":
                res += sign * num
                num = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res = 0 # starting calculating expression within ()
                sign = 1
            elif ch == ")":
                res += sign * num
                num = 0
                res *= stack.pop() # handle sign
                res += stack.pop() # handle value
        return res + (sign * num)



