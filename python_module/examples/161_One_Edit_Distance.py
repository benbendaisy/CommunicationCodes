class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        if abs(ns - nt) > 1:
            return False

        l = 0
        length = min(ns, nt)
        while l < length and s[l] == t[l]:
            l += 1

        if l == ns and l == nt:
            return False

        if ns > nt:
            return s[l + 1:] == t[l:]
        elif ns < nt:
            return s[l:] == t[l + 1:]
        else:
            return s[l + 1:] == t[l + 1:]

    def isOneEditDistance1(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        if ns > nt:
            return self.isOneEditDistance(t, s)

        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]

        return ns + 1 == nt



