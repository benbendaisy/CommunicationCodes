class Solution:
    """
    Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

    The following rules define a valid string:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
    
    Example 1:

    Input: s = "()"
    Output: true
    Example 2:

    Input: s = "(*)"
    Output: true
    Example 3:

    Input: s = "(*))"
    Output: true
    """
    def checkValidString(self, s: str) -> bool:
        if not s:
            return False
        
        n = len(s)
        @cache
        def helper(idx: int, balance: int) -> int:
            # Base case: if we've processed all characters, check if balance is 0
            if idx == n:
                return balance == 0
            # If balance goes negative, we have too many closing parentheses
            if balance < 0:
                return False
            match s[idx]:
                case "(":
                    return helper(idx + 1, balance + 1)
                case ")":
                    return helper(idx + 1, balance - 1)
                case "*": # s[i] == '*', we have 3 choices: '(', ')', ''
                    return helper(idx + 1, balance + 1) or helper(idx + 1, balance - 1) or helper(idx + 1, balance)
        
        return helper(0, 0)