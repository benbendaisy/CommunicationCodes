class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}
        for ch in s:
            if ch in mp:
                mp[ch] += 1
            else:
                mp[ch] = 1
        for ch in t:
            if ch not in mp or mp[ch] - 1 < 0:
                return False
            elif ch in mp:
                mp[ch] -= 1
        for ch in mp.keys():
            if mp[ch] != 0:
                return False
        return True
