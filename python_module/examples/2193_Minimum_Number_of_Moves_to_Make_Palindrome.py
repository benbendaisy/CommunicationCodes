class Solution:
    def minMovesToMakePalindrome1(self, s: str) -> int:
        if not s:
            return 0

        chars = [ch for ch in s]

        l, r = 0, len(chars) - 1
        cnt = 0
        while l < r:
            if chars[l] == chars[r]:
                l, r = l + 1, r - 1
                continue

            k = r
            while chars[k] != chars[l]:
                k -= 1

            if k == l: #only one element that should be in the middle
                cnt += 1
                chars[l], chars[l + 1] = chars[l + 1], chars[l]
            else:
                while k < r:
                    cnt += 1
                    chars[k], chars[k + 1] = chars[k + 1], chars[k]
                    k += 1
        return cnt

    def minMovesToMakePalindrome(self, s: str) -> int:
        if not s:
            return 0

        chars = list(s)
        cnt = 0
        while chars:
            idx = chars.index(chars[-1])
            if idx == len(chars) - 1:  # the only character in the middle
                cnt += idx // 2
            else:
                cnt += idx # swap idx times to move the element to the first position
                chars.pop(idx) # remove the element that pairs with the last element
            chars.pop() # remove the last element
        return cnt