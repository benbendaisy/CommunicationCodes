class Solution:
    """
        Convert a non-negative integer num to its English words representation.

        Example 1:

        Input: num = 123
        Output: "One Hundred Twenty Three"
        Example 2:

        Input: num = 12345
        Output: "Twelve Thousand Three Hundred Forty Five"
        Example 3:

        Input: num = 1234567
        Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

        Constraints:

        0 <= num <= 231 - 1
    """
    def __init__(self):
        self.number_dic = {
            0: 'Zero',     1: 'One',
            2: 'Two',      3: 'Three',
            4: 'Four',     5: 'Five',
            6: 'Six',      7: 'Seven',
            8: 'Eight',    9: 'Nine',
           10: 'Ten',     11: 'Eleven',
           12: 'Twelve',  13: 'Thirteen',
           14: 'Fourteen',15: 'Fifteen',
           16: 'Sixteen', 17: 'Seventeen',
           18: 'Eighteen',19: 'Nineteen',
           20: 'Twenty',  30: 'Thirty',
           40: 'Forty',   50: 'Fifty',
           60: 'Sixty',   70: 'Seventy',
           80: 'Eighty',  90: 'Ninety'
        }
    def smallnumbersToWords(self, num: int) -> str:
        words = ""

        hundreds = num // 100
        if hundreds > 0:
            words += self.number_dic[hundreds]
            words += ' Hundred'
        num = num % 100
        tens = num // 10
        ones = num % 10
        if tens == 0 and ones == 0:
            return words
        if hundreds > 0 and (tens > 0 or ones > 0):
            words += ' '

        if tens == 1 and ones >= 0:
            words += self.number_dic[num]
        elif tens >= 2 and ones == 0:
            words += self.number_dic[num]
        elif tens >= 2 and ones > 0:
            words += self.number_dic[tens*10]
            words += ' '
            words += self.number_dic[ones]
        else:
            words += self.number_dic[ones]

        return words

    def numberToWords(self, num: int) -> str:
        words = ""
        temp = num
        billions = temp // (10**9)
        temp = temp % (10**9)
        millions = temp // (10**6)
        temp = temp % (10**6)
        thousands = temp // (10**3)
        hundreds = temp % (10**3)


        # billions
        if billions > 0:
            words += self.smallnumbersToWords(billions)
            words += ' Billion'
            if millions + thousands + hundreds > 0:
                words += ' '

        # millions
        if millions > 0:
            words += self.smallnumbersToWords(millions)
            words += ' Million'
            if thousands + hundreds > 0:
                words += ' '

        # thousands
        if thousands > 0:
            words += self.smallnumbersToWords(thousands)
            words += ' Thousand'
            if hundreds > 0:
                words += ' '

        # hundreds
        if hundreds > 0:
            words += self.smallnumbersToWords(hundreds)

        # Zero
        if num == 0:
            words += self.number_dic[num]

        return words
