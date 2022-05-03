class Solution:
    def backspaceCompare1(self, s: str, t: str) -> bool:
        def normalizedString(str1: str) -> str:
            chars = list(str1)
            for i in range(1, len(str1)):
                if chars[i] == "#":
                    r = i
                    while r > 0 and chars[r] == "#":
                        r -= 1
                    chars[r] = "#"

            res = [x for x in chars if x != "#"]
            return "".join(res)

        s1 = normalizedString(s)
        t1 = normalizedString(t)

        return s1 == t1

    def backspaceCompare(self, s: str, t: str) -> bool:
        def normalizeString(str1: str):
            res = []
            for ch in str1:
                if ch != "#":
                    res.append(ch)
                elif res:
                    res.pop()
            return "".join(res)

        return normalizeString(s) == normalizeString(t)

