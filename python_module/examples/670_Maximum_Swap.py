class Solution:
    """
    You are given an integer num. You can swap two digits at most once to get the maximum valued number.

    Return the maximum valued number you can get.

    Example 1:

    Input: num = 2736
    Output: 7236
    Explanation: Swap the number 2 and the number 7.
    Example 2:

    Input: num = 9973
    Output: 9973
    Explanation: No swap.
    """
    def maximumSwap(self, num: int) -> int:
        chars = [ch for ch in str(num)]
        position_dict = {int(v):i for i, v in enumerate(chars)}
        for i in range(len(chars) - 1):
            for j in range(9, int(chars[i]), -1):
                if j in position_dict and position_dict[j] > i:
                    chars[i], chars[position_dict[j]] = chars[position_dict[j]], chars[i]
                    return int("".join(chars))
        return num