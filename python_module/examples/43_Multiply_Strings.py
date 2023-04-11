class Solution:
    """
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

    Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

    Example 1:

    Input: num1 = "2", num2 = "3"
    Output: "6"
    Example 2:

    Input: num1 = "123", num2 = "456"
    Output: "56088"
    """
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num_dict = {str(i) : i for i in range(10)}
        val1 = 0
        for i in num1:
            val1 = 10 * val1 + num_dict[i]
        val2 = 0
        for j in num2:
            val2 = val2 * 10 + val1 * num_dict[j]
        return str(val2)

