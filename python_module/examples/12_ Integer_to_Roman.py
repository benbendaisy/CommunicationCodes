class Solution:
    """
        oman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

        Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        Given an integer, convert it to a roman numeral.

        Example 1:

        Input: num = 3
        Output: "III"
        Explanation: 3 is represented as 3 ones.
        Example 2:

        Input: num = 58
        Output: "LVIII"
        Explanation: L = 50, V = 5, III = 3.
        Example 3:

        Input: num = 1994
        Output: "MCMXCIV"
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """
    def intToRoman1(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]
    
    def intToRoman2(self, num: int) -> str:
        roman_numerals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = ""
        for value, symbol in roman_numerals:
            while num >= value:
                result += symbol
                num -= value
        
        return result
    
    def intToRoman3(self, num: int) -> str:
        roman_numerics = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), 
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        res = ""
        for value, symbol in roman_numerics:
            while num >= value:
                res += symbol
                num -= value
        return res
    
    def intToRoman(self, num: int) -> str:
        roman_numerics = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), 
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        res = ""
        for value, symbol in roman_numerics:
            while num >= value:
                res += symbol
                num -= value
        return res
