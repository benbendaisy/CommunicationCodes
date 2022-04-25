from audioop import reverse


class Solution:
    def nextPermutation(self, num: str):
        nums = [int(x) for x in num]

        idx = len(num) - 2
        while idx >= 0 and nums[idx] >= nums[idx + 1]:
            idx -= 1

        if idx >= 0:
            r = len(num) - 1
            while r > idx and nums[r] <= nums[idx]:
                r -= 1
            nums[idx], nums[r] = nums[r], nums[idx]
        else:
            return num

        left, right = idx + 1, len(num) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1

        return "".join([str(x) for x in nums])

    def nextPalindrome1(self, num: str) -> str:
        charSet = set()
        charSet.add(num)
        nextPerm = num
        while True:
            nextPerm = self.nextPermutation(nextPerm)
            if nextPerm in charSet:
                return ""
            charSet.add(nextPerm)
            if nextPerm == nextPerm[::-1]:
                return nextPerm

    def nextPalindrome(self, num: str) -> str:
        if not num:
            return ""
        mid = len(num) // 2
        center = ""
        if len(num) % 2 != 0:
            center = num[mid]
        chars = list(num[:mid])
        idx = len(chars) - 2
        while idx >= 0 and chars[idx] >= chars[idx + 1]:
            idx -= 1

        if idx < 0:
            return ""

        r = len(chars) - 1
        while r > idx and chars[idx] >= chars[r]:
            r -= 1
        chars[idx], chars[r] = chars[r], chars[idx]

        chars[idx + 1:] = reversed(chars[idx + 1:])

        return "".join(chars) + center + "".join(reversed(chars))


if __name__ == "__main__":
    num = "49841828400482814894"
    solution = Solution()
    ret = solution.nextPalindrome(num)
    print(ret)