from typing import List


class Solution:
    """
        Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

        Note that operands in the returned expressions should not contain leading zeros.

        Example 1:

        Input: num = "123", target = 6
        Output: ["1*2*3","1+2+3"]
        Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
        Example 2:

        Input: num = "232", target = 8
        Output: ["2*3+2","2+3*2"]
        Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
        Example 3:

        Input: num = "3456237490", target = 9191
        Output: []
        Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.

        Constraints:

        1 <= num.length <= 10
        num consists of only digits.
        -231 <= target <= 231 - 1
    """
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []
        def try_all_expressions(idx, exp, prev, total):
            if idx == n:
                if total == target:
                    res.append(exp)
                return
            for i in range(idx, n):
                cur_val = int(num[idx : i + 1])
                if num[idx] == '0' and i > idx:
                    return
                if idx == 0:
                    try_all_expressions(i + 1, str(cur_val), cur_val, cur_val)
                else:
                    try_all_expressions(i + 1, exp + "+" + str(cur_val), cur_val, total + cur_val)
                    try_all_expressions(i + 1, exp + "-" + str(cur_val), -cur_val, total - cur_val)
                    try_all_expressions(i + 1, exp + "*" + str(cur_val), prev * cur_val, total - prev + prev * cur_val)
        try_all_expressions(0, "", 0, 0)
        return res

if __name__ == "__main__":
    num = "123"
    target = 6
    solution = Solution()
    ret = solution.addOperators(num, target)
    print(ret)
