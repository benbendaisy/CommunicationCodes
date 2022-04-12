from collections import defaultdict, Counter


class Solution:

    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0

        strCntMap = Counter(s)
        maxOdd = 0
        longestLength = 0
        for key, value in strCntMap.items():
            if value % 2 == 0:
                longestLength += value
            else:
                maxOdd = max(maxOdd, value)
                longestLength += value - 1

        return longestLength + 1 if maxOdd > 0 else longestLength

    def longestPalindrome1(self, s: str) -> int:
        if not s:
            return 0

        strCntMap = defaultdict(int)
        for ch in s:
            strCntMap[ch] += 1

        maxOdd = 0
        longestLength = 0
        for key, value in strCntMap.items():
            if value % 2 == 0:
                longestLength += value
            else:
                maxOdd = max(maxOdd, value)
                longestLength += value - 1

        return longestLength + 1 if maxOdd > 0 else longestLength

if __name__ == "__main__":
    s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    solution = Solution()
    ret = solution.longestPalindrome(s)
    print(ret)