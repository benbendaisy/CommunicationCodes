class Solution:
    """
    Given an integer num, return a string of its base 7 representation.

    Example 1:

    Input: num = 100
    Output: "202"
    Example 2:

    Input: num = -7
    Output: "-10"
    """
    def convertToBase71(self, num: int) -> str:
        if num == 0:
            return "0"
        res = []
        label = num < 0
        if label:
            num = -1 * num
        carrier = num
        while carrier:
            remain = carrier % 7
            carrier = carrier // 7
            res.insert(0, str(remain))
        if label:
            res.insert(0, "-")
        return "".join(res)
    
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        res = []
        while num > 0:
            res.append(str(num % 7))
            num = num // 7
        
        if negative:
            res.append("-")
        
        return "".join(res[::-1])