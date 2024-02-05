from functools import lru_cache


class Solution:
    def countPalindromicSubsequence1(self, s: str) -> int:
        def palindromicSubs(str1: str):
            if len(str1) == 3:
                if str1 == str1[::-1]:
                    resSet.add(str1)
                return

            for i in range(1, len(str1)):
                subSeq = str1[:i] + str1[i + 1:]
                palindromicSubs(subSeq)

        resSet = set()
        palindromicSubs(s)
        return len(resSet)

    def countPalindromicSubsequence2(self, s: str) -> int:
        resSet = set()
        def palindromicSubs(str1, str2):
            if len(str1) == 0 or len(str2) == 3:
                if len(str2) == 3 and str2 == str2[::-1]:
                    resSet.add(str2)
                return
            palindromicSubs(str1[1:], str2 + str1[0])
            palindromicSubs(str1[1:], str2)

        palindromicSubs(s, "")
        return len(resSet)

    def countPalindromicSubsequence(self, s: str) -> int:
        def palindromicSubs(idx: int, curStr: str):
            if idx == len(s) or len(curStr) == 3:
                if len(curStr) == 3 and curStr == curStr[::-1]:
                    resSet.add(curStr)
                return
            i = idx + 1
            while i < len(s):
                curStr += s[i]
                palindromicSubs(i, curStr)
                curStr = curStr[:-1]
                i += 1

        resSet = set()
        palindromicSubs(-1, "")
        return len(resSet)
    
    def countPalindromicSubsequence3(self, s: str) -> int:
        res_set = set()
        n = len(s)
        @cache
        def helper(idx: int, cur_str: str):
            if idx == n or len(cur_str) == 3:
                if len(cur_str) == 3 and cur_str[0] == cur_str[-1]:
                    res_set.add(cur_str)
                return
            for i in range(idx, n):
                helper(i + 1, cur_str + s[i])
        helper(0, "")
        return len(res_set)

    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        chars = set(s)
        for ch in chars:
            i, j = s.find(ch), s.rfind(ch)
            res += len(set(s[i + 1:j]))
        return res



if __name__ == "__main__":
    s = "nhzosdwmwomlebymvkbqbdohzdtpufnllwzhqptyffreebalphgsslryuqryloqxvbehtohdrsynmcbligczvoyzrhbtmqxepqmcjirwishyvoliizknzrokejtqtfoylsdzpgeooczxldvmsnhvzgojxnwwhukynvhhpzmdoiooliesogubtsvkrvzmanpwwlnlskremzisqwwwjistwabqxztlcqwlsxbuhjdnouecwqgxdlggauxrelipqlgvfkmgoozhzrhortbpmxhupjqqrsrvqxqilptchtedoznxvgvmuticzdzwszzujuanlrrpvycgawoxfbvxhkdyhmcxdlrtyktekcmkyajlywcrozjkedwlrqpaugdobtffwidxawddgeraaugiebtntmuncnybuwnlzbmkrmxbcpbhqoiznlpcswqtsflfilkclrjdxbvcctvopoidjrtwszpjpfrfcvjtouvzvpqayvgesiiawokdqatfkijsuocbeqrhrmlhtclhrmrbkpahfdgiatejsnvubwbaxwooskcaiuqvxcvgpnkiiiencnxjsvvgdfptreumttlyoqqwqdblhhbnilbvbwwpnmouxlvqimdbcxisnegllnejhkipuqbcrhsrxwipdjzskpyijuvrvtrnqljjefymfdcvcuvwaitdjevuvelkrglhtlnivmvjyzmhjnzvudgqwocvwhthxdlyfljabngzjayvqudhvsdslacgvosnchhbkulcxpangdlpgkrczbnnzokmqzgauitqutiboveumsqvbulhbfbynzogtejuwi"
    solution = Solution()
    ret = solution.countPalindromicSubsequence(s)
    print(ret)
