from typing import List


class Solution:
    """
        An additive number is a string whose digits can form an additive sequence.

        A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

        Given a string containing only digits, return true if it is an additive number or false otherwise.

        Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

        Example 1:

        Input: "112358"
        Output: true
        Explanation:
        The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
        1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
        Example 2:

        Input: "199100199"
        Output: true
        Explanation:
        The additive sequence is: 1, 99, 100, 199.
        1 + 99 = 100, 99 + 100 = 199

        Constraints:

        1 <= num.length <= 35
        num consists only of digits.
    """
    def isAdditiveNumber1(self, num: str) -> bool:
        def checkAdditiveNums(arr: List):
            if len(arr) < 3:
                return False
            elif (len(arr[0]) > 1 and arr[0].startswith("0")) or (len(arr[1]) > 1 and arr[1].startswith("0")):
                return False
            for i in range(2, len(arr)):
                if len(arr[i]) > 1 and arr[i].startswith("0"):
                    return False
                elif int(arr[i - 1]) + int(arr[i - 2]) != int(arr[i]):
                    return False

            return True

        def validateAllSubstrSequences(idx: int, arr: List):
            if idx == len(num):
                if checkAdditiveNums(arr):
                    return True
                return False

            for i in range(idx, len(num)):
                if validateAllSubstrSequences(i + 1, arr + [num[idx: i + 1]]):
                    return True

            return False

        return validateAllSubstrSequences(0, [])

    def isAdditiveNumber(self, num: str) -> bool:
        def validateAllSubstrings(idx: int, prev1: int, prev2: int, cnt: int):
            if idx >= len(num):
                return cnt >= 3    # make sure substring is greater than 3
            for i in range(idx + 1, len(num) + 1):
                curNum = int(num[idx:i])
                if prev1 is None or prev2 is None or curNum == prev1 + prev2:
                    if validateAllSubstrings(i, prev2, curNum, cnt + 1):
                        return True
                if num[idx] == "0":
                    break
            return False

        return validateAllSubstrings(0, None, None, 0)



if __name__ == "__main__":
    num = "11111111111011111111111"
    solution = Solution()
    ret = solution.isAdditiveNumber(num)
    print(ret)
