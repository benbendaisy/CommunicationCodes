class Solution:
    """
        Given an encoded string, return its decoded string.

        The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

        You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

        The test cases are generated so that the length of the output will never exceed 105.

        Example 1:

        Input: s = "3[a]2[bc]"
        Output: "aaabcbc"
        Example 2:

        Input: s = "3[a2[c]]"
        Output: "accaccacc"
        Example 3:

        Input: s = "2[abc]3[cd]ef"
        Output: "abcabccdcdcdef"

        Constraints:

        1 <= s.length <= 30
        s consists of lowercase English letters, digits, and square brackets '[]'.
        s is guaranteed to be a valid input.
        All the integers in s are in the range [1, 300].
    """
    def decodeString1(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                subStr = ""
                while stack and stack[-1] != "[":
                    subStr = stack.pop() + subStr
                stack.pop() # skip [
                n = ""
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                stack.append(int(n) * subStr)
        return "".join(stack)
    
    def decodeString2(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                sub_str = ""
                while stack and stack[-1] != "[":
                    sub_str = stack.pop() + sub_str
                stack.pop() # pop out "["
                cnt = ""
                while stack and stack[-1].isdigit():
                    cnt = stack.pop() + cnt
                cnt = int(cnt)
                stack.append(sub_str * cnt)
        return "".join(stack)

    def decodeString3(self, s: str) -> str:
        if not s:
            return s
        
        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                chars = ""
                while stack and  stack[-1] != "[":
                    chars = stack.pop() + chars
                stack.pop() # skip '['
                digits = ""
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits
                stack.append(chars * int(digits))
        return "".join(stack)

