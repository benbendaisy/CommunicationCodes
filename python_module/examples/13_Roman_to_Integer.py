class Solution:
    """
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

        Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        Given a roman numeral, convert it to an integer.

        Example 1:

        Input: s = "III"
        Output: 3
        Explanation: III = 3.
        Example 2:

        Input: s = "LVIII"
        Output: 58
        Explanation: L = 50, V= 5, III = 3.
        Example 3:

        Input: s = "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

        Constraints:

        1 <= s.length <= 15
        s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
        It is guaranteed that s is a valid roman numeral in the range [1, 3999].
    """
    def romanToInt1(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total
    
    def romanToInt2(self, s: str) -> int:
        value_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        cnt, idx = 0, 0
        n = len(s)
        while idx < n:
            if idx + 1 < n and value_map[s[idx]] < value_map[s[idx + 1]]:
                cnt += value_map[s[idx + 1]] - value_map[s[idx]]
                idx += 2
            else:
                cnt += value_map[s[idx]]
                idx += 1
        return cnt
    
    def romanToInt3(self, s: str) -> int:
        value_map = {
            "I" : 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        idx, n, res = 0, len(s), 0
        while idx < n:
            if idx + 1 < n and value_map[s[idx]] < value_map[s[idx + 1]]:
                res += value_map[s[idx + 1]] - value_map[s[idx]]
                idx += 2
            else:
                res += value_map[s[idx]]
                idx += 1
        return res
    
    def romanToInt4(self, s: str) -> int:
        mappings = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        n, idx = len(s), 0
        res = 0
        while idx < n:
            if idx < n - 1 and mappings[s[idx]] < mappings[s[idx + 1]]:
                res += mappings[s[idx + 1]] - mappings[s[idx]]
                idx += 2
            else:
                res += mappings[s[idx]]
                idx += 1
        return res
    
    def romanToInt5(self, s: str) -> int:
        mappings = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        idx, n = 0, len(s)
        res = 0
        while idx < n:
            if idx < n - 1 and mappings[s[idx]] < mappings[s[idx + 1]]:
                res += mappings[s[idx + 1]] - mappings[s[idx]]
                idx += 2
            else:
                res += mappings[s[idx]]
                idx += 1
        return res
    
    def romanToInt6(self, s: str) -> int:
        mappings = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        n, idx = len(s), 0
        res = 0
        while idx < n:
            if idx < n - 1 and mappings[s[idx]] < mappings[s[idx + 1]]:
                res += mappings[s[idx + 1]] - mappings[s[idx]]
                idx += 2
            else:
                res += mappings[s[idx]]
                idx += 1
        return res