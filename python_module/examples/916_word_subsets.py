from collections import defaultdict
from typing import List


class Solution:
    def countChars(self, word: str):
        ans = [0] * 26
        for c in word:
            ans[ord(c) - ord('a')] += 1
        return ans

    def wordSubsets1(self, words1: List[str], words2: List[str]) -> List[str]:
        if not words1 or not words2:
            return False

        bmax = [0] * 26
        for word in words2:
            lbs = self.countChars(word)
            for i in range(len(bmax)):
                bmax[i] = max(bmax[i], lbs[i])

        arr = []
        for word in words1:
            bword = self.countChars(word)
            for i in range(len(bmax)):
                if bword[i] < bmax[i]:
                    break
            else:
                arr.append(word)
        return arr

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def countChars(word):
            ans = [0] * 26
            for ch in word:
                ans[ord(ch) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for word in words2:
            for i, v in enumerate(countChars(word)):
                bmax[i] = max(bmax[i], v)
        res = []
        for word in words1:
            if all( x >= y  for x, y in zip(countChars(word), bmax)):
                res.append(word)
        return res


if __name__ == "__main__":
    words1 = ["qqwhoukghj","kmbayiceou","jthwqqqkoh","oqkwqjhazh","khhxytwfiq","bjkkqdkrgw","hijnoloklj","extoeolpqq","qcacxjcxhf","ynvvryants","jobqhhhqxo","zjqymohahq","zrktnhtzhy","bvzbxlgnoc","txoonmefcs","xvvuotbhvq","cfuodgncor","ksgczljelb","mqonqjzhho","pcbbvciewh","qrltzbvpqu","asqdeptwyh","utzjbjkmjd","sgcdrkmvdw","hwhxqjqoqt","qohjqxsqho","hhjojqvitq","vhbzlfwjew","yjuttemdqj","jhqhtnotqz","vnyuymfzse","jrjipriynq","ougdbgetxf","mumpcemhpa","oqtqhmjhwo","ivvlfwangk","ebttyeozxb","hxsmukftfv","qjhzbquoah","hjbefqioqh","cjwjybkaqe","jsahaijmnl","ljoqhqldhe","usqdtaklfi","qqvrdjkubx","yktktzhctc","oyitcaorwq","qhoqjpvhnh","kkrriqxjgn","mpfdfiwwvf","imzdcndewz","buvmbdwxmn","hqhoyjqdwk","jygfdcqxzl","qmtdrikffl","mhclcrvxho","uhqookmquv","hogqtjwqhc","ybvdiptaib","oxulzljaio","klrzxizftd","dxipngdecx","heocjqdqhr","xnkegfpeea","vvelvfizbq","uesssoqroy","qqkvzgxxcp","rgpkzkdqzv","zgpabolxrd","muavkymyvw","qohjsqhjnx","xtsqwweffj","dqhhgoiqrj","liujhuqeaj","oqjhhhqodi","jcvxdxortu","mwnbrdrshl"]
    words2 = ["loeo"]
    solution = Solution()
    ret = solution.wordSubsets(words1, words2)
    print(ret)
