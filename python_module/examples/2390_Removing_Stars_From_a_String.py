class Solution:
    """
        You are given a string s, which contains stars *.

        In one operation, you can:

        Choose a star in s.
        Remove the closest non-star character to its left, as well as remove the star itself.
        Return the string after all stars have been removed.

        Note:

        The input will be generated such that the operation is always possible.
        It can be shown that the resulting string will always be unique.

        Example 1:

        Input: s = "leet**cod*e"
        Output: "lecoe"
        Explanation: Performing the removals from left to right:
        - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
        - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
        - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
        There are no more stars, so we return "lecoe".
        Example 2:

        Input: s = "erase*****"
        Output: ""
        Explanation: The entire string is removed, so we return an empty string.
    """
    def removeStars_1(self, s: str) -> str:
        stack = []
        i, n = 0, len(s)
        while i < n:
            if s[i] != "*":
                stack.append(s[i])
            else:
                stack.pop()
            i += 1
        return "".join(stack)

    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != "*":
                stack.append(ch)
            else:
                stack.pop()
        return "".join(stack)
