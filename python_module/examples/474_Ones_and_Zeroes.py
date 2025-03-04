from typing import List


class Solution:
    def findMaxForm1(self, strs: List[str], m: int, n: int) -> int:
        # def countOnes(string: str):
        #     num = int(string)
        #     cnt = 0
        #     while num > 0:
        #         digit = num & 1
        #         if digit == 1:
        #             cnt += 1
        #         num = num >> 1
        #     return cnt

        def countOnes(string: str):
            cnt = 0
            for i in range(len(string)):
                if string[i] == "1":
                    cnt += 1
            return cnt

        oneLists = [countOnes(x) for x in strs]

        def findMaxOnes(idx: int, cntOne, cntZero):
            if idx >= len(oneLists) or cntOne > n or cntZero > m:
                return 0

            maxCnt = 0
            for i in range(idx, len(oneLists)):
                if cntOne + oneLists[i] > n or cntZero + len(strs[i]) - oneLists[i] > m:
                    continue
                taken = 1 + findMaxOnes(i + 1, cntOne + oneLists[i], cntZero + len(strs[i]) - oneLists[i])
                notTaken = findMaxOnes(i + 1, cntOne, cntZero)
                maxCnt = max(maxCnt, taken, notTaken)
            return maxCnt


        return findMaxOnes(0, 0, 0)

    def findMaxForm2(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        def countOnes(string: str):
            cnt = 0
            for i in range(len(string)):
                if string[i] == "1":
                    cnt += 1
            return cnt
        oneLists = [countOnes(x) for x in strs]
        for i in range(len(oneLists)):
            one, zero = oneLists[i], len(strs[i]) - oneLists[i]
            for zeros in range(m,  zero - 1, -1):
                for ones in range(n, one - 1, -1):
                    dp[zeros][ones] = max(1 + dp[zeros - zero][ones - one], dp[zeros][ones])
        return dp[m][n]
    

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if not strs:
            return 0
        
        length = len(strs)
        @cache
        def helper(idx: int, zeros: int, ones: int) -> int:
            # Base case: If we've processed all strings
            if idx == length:
                return 0 # No more selections possible
            
            # Choice 1: Skip the current string
            max_cnt = helper(idx + 1, zeros, ones)
            # Count zeros and ones in the current string
            one, zero = strs[idx].count("1"), strs[idx].count("0")
            # Choice 2: Take the current string (only if it doesn't exceed constraints)
            if zeros + zero <= m and ones + one <= n:
                max_cnt = max(max_cnt, 1 + helper(idx + 1, zeros + zero, ones + one))
                
            return max_cnt
        
        return helper(0, 0, 0)


if __name__ == "__main__":
    strs = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
    solution = Solution()
    ret = solution.findMaxForm(strs, 9, 80)
    print(ret)

