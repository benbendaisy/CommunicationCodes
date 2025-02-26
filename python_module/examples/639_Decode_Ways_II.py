class Solution:
    """
    A message containing letters from A-Z can be encoded into numbers using the following mapping:

    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"
    To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)
    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

    In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

    Given a string s consisting of digits and '*' characters, return the number of ways to decode it.

    Since the answer may be very large, return it modulo 109 + 7.

    Example 1:

    Input: s = "*"
    Output: 9
    Explanation: The encoded message can represent any of the encoded messages "1", "2", "3", "4", "5", "6", "7", "8", or "9".
    Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F", "G", "H", and "I" respectively.
    Hence, there are a total of 9 ways to decode "*".
    Example 2:

    Input: s = "1*"
    Output: 18
    Explanation: The encoded message can represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19".
    Each of these encoded messages have 2 ways to be decoded (e.g. "11" can be decoded to "AA" or "K").
    Hence, there are a total of 9 * 2 = 18 ways to decode "1*".
    Example 3:

    Input: s = "2*"
    Output: 15
    Explanation: The encoded message can represent any of the encoded messages "21", "22", "23", "24", "25", "26", "27", "28", or "29".
    "21", "22", "23", "24", "25", and "26" have 2 ways of being decoded, but "27", "28", and "29" only have 1 way.
    Hence, there are a total of (6 * 2) + (3 * 1) = 12 + 3 = 15 ways to decode "2*".
    """
    def numDecodings1(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        if n == 0:
            return 0

        # DP variables (instead of array to save space)
        dp1, dp2 = 1, 1  # dp1 = dp[i-1], dp2 = dp[i-2]

        # Helper function: ways to decode a single character
        def decode_single(ch):
            if ch == '*':
                return 9  # Can be '1' to '9'
            return 1 if ch != '0' else 0  # '0' alone is invalid

        # Helper function: ways to decode a two-character pair
        def decode_double(ch1, ch2):
            if ch1 == '*' and ch2 == '*':
                return 15  # ('11-19', '21-26')
            elif ch1 == '*':
                if '0' <= ch2 <= '6':
                    return 2  # ('10-16', '20-26')
                else:
                    return 1  # ('17-19')
            elif ch2 == '*':
                if ch1 == '1':
                    return 9  # ('11-19')
                elif ch1 == '2':
                    return 6  # ('21-26')
                else:
                    return 0  # No valid mapping
            else:
                return 1 if 10 <= int(ch1 + ch2) <= 26 else 0  # Regular two-digit check

        # DP Iteration
        for i in range(1, n + 1):
            temp = dp1 * decode_single(s[i - 1]) % MOD
            if i > 1:
                temp = (temp + dp2 * decode_double(s[i - 2], s[i - 1])) % MOD
            dp2, dp1 = dp1, temp  # Move DP state forward

        return dp1
    
    def numDecodings2(self, s: str) -> int:
        """
        Count the number of ways to decode a string with digits and '*' characters using recursion.
        
        Args:
            s: A string of digits and '*' characters
            
        Returns:
            The number of ways to decode the string, modulo 10^9 + 7
        """
        MOD = 10**9 + 7
        memo = {}
        
        def decode(index):
            """
            Helper function to recursively count ways to decode the substring starting at index.
            
            Args:
                index: The current position in the string
                
            Returns:
                Number of ways to decode from this position onwards
            """
            # Base case: empty string (successful decoding)
            if index == len(s):
                return 1
            
            # Base case: leading zero or already reached the end
            if index > len(s) or s[index] == '0':
                return 0
            
            # Check if we've already computed this subproblem
            if index in memo:
                return memo[index]
            
            # Initialize ways for current position
            ways = 0
            
            # Option 1: Decode a single digit
            if s[index] == '*':
                # '*' can be any digit from 1-9
                ways = (ways + 9 * decode(index + 1)) % MOD
            else:
                # Regular digit
                ways = (ways + decode(index + 1)) % MOD
            
            # Option 2: Decode two digits
            if index + 1 < len(s):
                if s[index] == '*' and s[index + 1] == '*':
                    # "**" can be any valid two-digit number from 11-19 and 21-26 (15 possibilities)
                    ways = (ways + 15 * decode(index + 2)) % MOD
                elif s[index] == '*':
                    # "*d" where d is a digit
                    if '0' <= s[index + 1] <= '6':
                        # "*" can be 1 or 2 (11-16, 21-26)
                        ways = (ways + 2 * decode(index + 2)) % MOD
                    else:
                        # "*" can only be 1 (17-19)
                        ways = (ways + decode(index + 2)) % MOD
                elif s[index + 1] == '*':
                    # "d*" where d is a digit
                    if s[index] == '1':
                        # "1*" can be 11-19 (9 possibilities)
                        ways = (ways + 9 * decode(index + 2)) % MOD
                    elif s[index] == '2':
                        # "2*" can be 21-26 (6 possibilities)
                        ways = (ways + 6 * decode(index + 2)) % MOD
                else:
                    # Two regular digits
                    two_digit = int(s[index]) * 10 + int(s[index + 1])
                    if 10 <= two_digit <= 26:
                        ways = (ways + decode(index + 2)) % MOD
            
            # Store the result for this subproblem
            memo[index] = ways
            return ways
            
        return decode(0)
    
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        
        n = len(s)
        @cache
        def decode(idx: int):
            if idx == n:
                return 1
            
            if idx > n or s[idx] == '0':
                return 0
            
            num_ways = 0

            # Option 1: Decode a single digit
            if s[idx] == '*':
                num_ways = (num_ways + 9 * decode(idx + 1)) % MOD
            else:
                num_ways = (num_ways + decode(idx + 1)) % MOD
            
            # Option 2: Decode two digits
            if idx + 1 < n:
                if s[idx] == '*' and s[idx + 1] == '*':
                    num_ways = (num_ways + 15 * decode(idx + 2)) % MOD
                elif s[idx] == '*':
                    if '0' <= s[idx + 1] <= '6':
                        num_ways = (num_ways + 2 * decode(idx + 2)) % MOD
                    else:
                        num_ways = (num_ways + decode(idx + 2))
                elif s[idx + 1] == '*':
                    # "d*" where d is a digit
                    if s[idx] == '1':
                        num_ways = (num_ways + 9 * decode(idx + 2)) % MOD
                    elif s[idx] == '2':
                        num_ways = (num_ways + 6 * decode(idx + 2)) % MOD
                else:
                    two_digit = int(s[idx]) * 10 + int(s[idx + 1])
                    if 10 <= two_digit <= 26:
                        num_ways = (num_ways + decode(idx + 2)) % MOD
            return num_ways
        return decode(0)