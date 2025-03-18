class Solution:
    """
    An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

    A number is valid if each digit remains a digit after rotation. For example:

    0, 1, and 8 rotate to themselves,
    2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
    6 and 9 rotate to each other, and
    the rest of the numbers do not rotate to any other number and become invalid.
    Given an integer n, return the number of good integers in the range [1, n].

    Example 1:

    Input: n = 10
    Output: 4
    Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
    Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
    Example 2:

    Input: n = 1
    Output: 0
    Example 3:

    Input: n = 2
    Output: 1
    """
    def rotatedDigits1(self, n: int) -> int:
        str_n = str(n)
        valid_digits = {0, 1, 2, 5, 6, 8, 9}  # Allowed digits
        good_digits = {2, 5, 6, 9}  # Digits that actually change upon rotation

        @cache
        def dp(idx: int, is_tight: bool, has_good_digit: bool) -> int:
            """
            idx: Current position in the number
            is_tight: Whether we are still bounded by n
            has_good_digit: Whether we have at least one 'good' digit
            """
            if idx == len(str_n):
                return 1 if has_good_digit else 0

            upper_limit = int(str_n[idx]) if is_tight else 9
            count = 0

            for digit in range(upper_limit + 1):
                if digit in valid_digits:
                    count += dp(
                        idx + 1,
                        is_tight and (digit == upper_limit),
                        has_good_digit or (digit in good_digits),
                    )

            return count

        return dp(0, True, False)
    
    def rotatedDigits(self, n: int) -> int:
        str_n = str(n)
        valid_digits = {0, 1, 2, 5, 6, 8, 9}
        good_digits = {2, 5, 6, 9}

        @cache
        def helper(idx: int, is_prefix_limit: bool, has_good_digit: bool) -> int:
            if idx == len(str_n):
                return 1 if has_good_digit else 0
            
            cnt = 0
            for digit in valid_digits:
                if is_prefix_limit and str(digit) > str_n[idx]:
                    continue
                cnt += helper(idx + 1, is_prefix_limit and str(digit) == str_n[idx], has_good_digit or digit in good_digits)
            return cnt
        return helper(0, True, False)