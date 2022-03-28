class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        slist = [x for x in s.split(" ") if x]
        l, r = 0, len(slist) - 1
        while l < r:
            slist[l], slist[r] = slist[r], slist[l]
            l += 1
            r -= 1

        return " ".join(slist)