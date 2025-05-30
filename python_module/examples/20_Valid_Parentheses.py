class Solution:
    """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.

        Example 1:

        Input: s = "()"
        Output: true
        Example 2:

        Input: s = "()[]{}"
        Output: true
        Example 3:

        Input: s = "(]"
        Output: false
    """
    def isValid1(self, s: str) -> bool:
        if not s:
            return False
        stack = []
        for ch in s:
            if ch == "}" or ch == ")" or ch == "]":
                if not stack:
                    return False
                chr = stack.pop()
                if (ch == "}" and chr != "{") or (ch == ")" and chr != "(") or (ch == "]" and chr != "["):
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0

    def isValid2(self, s: str) -> bool:
        if not s:
            return False
        char_map = {'}':'{', ']':'[', ')':'('}
        stack = []
        for ch in s:
            if ch in char_map:
                top = stack.pop() if stack else '#'
                if char_map[ch] != top:
                    return False
            else:
                stack.append(ch)
        return not stack 
    
    def isValid3(self, s: str) -> bool:
        close_characters = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch in close_characters:
                if not stack or stack[-1] != close_characters[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
    
    def isValid4(self, s: str) -> bool:
        mappings = {"}":"{", ")":"(", "]":"["}
        stack = []
        for ch in s:
            if ch in mappings:
                if not stack or stack[-1] != mappings[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
    
    def isValid(self, s: str) -> bool:
        mappings = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for ch in s:
            if ch not in mappings:
                stack.append(ch)
            else:
                if not stack or mappings[ch] != stack[-1]:
                    return False
                stack.pop()
        return not stack