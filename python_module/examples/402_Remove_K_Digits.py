class Solution:
    """
        Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

        Example 1:

        Input: num = "1432219", k = 3
        Output: "1219"
        Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
        Example 2:

        Input: num = "10200", k = 1
        Output: "200"
        Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
        Example 3:

        Input: num = "10", k = 2
        Output: "0"
        Explanation: Remove all the digits from the number and it is left with nothing which is 0.
    """
    def removeKdigits1(self, num: str, k: int) -> str:
        numStack = []
        # Construct a monotone increasing sequence of digits
        for digit in num:
            while k > 0 and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)
        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        finalStack = numStack[:-k] if k > 0 else numStack

        # trip the leading zeros
        return "".join(finalStack).lstrip("0") or "0"
    
    def removeKdigits2(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        final_stack = stack[:-k] if k > 0 else stack
        return "".join(final_stack).lstrip("0") or "0"
    
    def removeKdigits3(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        res = stack[:-k] if k > 0 else stack
        return "".join(res).lstrip("0") or "0"
    
    def removeKdigits4(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        
        stack = stack[:-k] if k > 0 else stack
        return "".join(stack).lstrip("0") or "0"