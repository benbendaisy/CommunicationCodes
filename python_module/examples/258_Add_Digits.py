class Solution:
    def addDigits1(self, num: int) -> int:
        num_str = str(num)
        while len(num_str) > 1:
            nums = [int(ch) for ch in num_str]
            num_str = str(sum(nums))
        return int(num_str)

    def addDigits(self, num: int) -> int:
        while num > 9:
            sums = 0
            while num > 0:
                sums += num % 10
                num = num // 10
            num = sums
        return num