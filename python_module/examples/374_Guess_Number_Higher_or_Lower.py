# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return -1
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            pick = guess(mid)
            if pick == 0:
                return mid
            elif pick == 1:
                left = mid + 1
            else:
                right = mid - 1
        return left
