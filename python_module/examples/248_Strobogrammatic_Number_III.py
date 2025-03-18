from typing import List


class Solution:
    def compareTwoStrs(self, str1: str, str2: str):
        return int(str1) >= int(str2)

    def strobogrammaticInRange0(self, low: str, high: str) -> int:
        n1, n2 = len(low), len(high)
        res = []
        oddArray = ["0", "1", "8"]
        evenArray = [""]
        def generateStroboGrammatic(n: int, arr: List, isOdd: bool):
            reversePairs = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
            currentLength = 1 if isOdd else 0
            currentArray = oddArray if isOdd else evenArray

            while currentLength < n:
                currentLength += 2
                newQ = []
                for item in currentArray:
                    for key in reversePairs:
                        temp = key + item + reversePairs[key]
                        if self.compareTwoStrs(temp, low) and self.compareTwoStrs(high, temp) and temp[0] != "0":
                            arr.append(temp)
                        newQ.append(temp)
                currentArray = newQ
        for x in oddArray:
            if self.compareTwoStrs(x, low) and self.compareTwoStrs(high, x):
                res.append(x)

        generateStroboGrammatic(n2, res, True)
        generateStroboGrammatic(n2, res, False)
        return len(res)



    def strobogrammaticInRange1(self, low: str, high: str) -> int:
        def compareTwoStrs(str1: str, str2: str):
            return int(str1) >= int(str2)
        reversePairs = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        n1, n2 = len(low), len(high)
        oddArray = ["0", "1", "8"]
        if n2 < 2:
            return len([x for x in oddArray if x <= high and x >= low])
        evenArray = [""]
        res = []
        for item in oddArray:
            if compareTwoStrs(item, low) and compareTwoStrs(high, item):
                res.append(item)

        currentLength = 1
        while currentLength < n2:
            currentLength += 2
            newQ = []
            for item in oddArray:
                for key in reversePairs:
                    if key != 0 or currentLength < n2:
                        temp = key + item + reversePairs[key]
                        if compareTwoStrs(temp, low) and compareTwoStrs(high, temp) and temp[0] != "0":
                            res.append(temp)
                        newQ.append(temp)
            oddArray = newQ

        currentLength = 0
        while currentLength < n2:
            currentLength += 2
            newQ = []
            for item in evenArray:
                for key in reversePairs:
                    if key != 0 or currentLength < n2:
                        temp = key + item + reversePairs[key]
                        if compareTwoStrs(temp, low) and compareTwoStrs(high, temp) and temp[0] != "0":
                            res.append(temp)
                        newQ.append(temp)
            evenArray = newQ

        return len(res)
    
    def strobogrammaticInRange2(self, low: str, high: str) -> int:
        def generateStrobogrammaticNumbers(n, length):
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]
            
            smallerNumbers = generateStrobogrammaticNumbers(n - 2, length)
            result = []
            
            for num in smallerNumbers:
                if n != length:
                    result.append("0" + num + "0")
                result.append("1" + num + "1")
                result.append("6" + num + "9")
                result.append("8" + num + "8")
                result.append("9" + num + "6")
            
            return result
        
        low_len = len(low)
        high_len = len(high)
        strobogrammaticNumbers = []
        
        for length in range(low_len, high_len + 1):
            strobogrammaticNumbers += generateStrobogrammaticNumbers(length, length)
        
        # Filter numbers that are within the range [low, high]
        validNumbers = [num for num in strobogrammaticNumbers if (len(num) == low_len and num >= low or len(num) > low_len) and (len(num) == high_len and num <= high or len(num) < high_len)]
        
        return len(validNumbers)
    
    def strobogrammaticInRange3(self, low: str, high: str) -> int:
        pairs = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    
        def is_valid(num: str) -> bool:
            return (len(num) == 1 or num[0] != "0") and int(low) <= int(num) <= int(high)

        @lru_cache(maxsize=None)
        def count_strobogrammatic(n: int, current: str) -> int:
            if n == 0:
                return 1 if is_valid(current) else 0
            
            cnt = 0
            for digit, rotated in pairs.items():
                new_num = digit + current + rotated
                if len(new_num) <= len(high):
                    cnt += count_strobogrammatic(n - 2, new_num)
            return cnt
        
        cnt = 0
        for length in range(len(low), len(high) + 1):
            if length % 2 == 0:
                cnt += count_strobogrammatic(length, "")
            else:
                for mid in ["0", "1", "8"]:
                    cnt += count_strobogrammatic(length - 1, mid)
        return cnt
    
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        pairs = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    
        def is_valid(curr: str) -> bool:
            return (len(curr) == 1 or curr[0] != "0") and int(low) <= int(curr) <= int(high)
        
        @cache
        def helper(idx: int, curr: str):
            if idx == 0:
                return 1 if is_valid(curr) else 0
            
            cnt = 0
            for digit, rotated in pairs.items():
                new_num = digit + curr + rotated
                if len(new_num) <= len(high):
                    cnt += helper(idx - 2, new_num)
            return cnt
        
        cnt = 0
        for length in range(len(low), len(high) + 1):
            if length % 2 == 0:
                cnt += helper(length, "")
            else:
                for mid in ["0", "1", "8"]:
                    cnt += helper(length - 1, mid) # 3 represents [0, 1, 8]
        return cnt

if __name__ == "__main__":
    low = "0"
    high = "100"
    solution = Solution()
    ret = solution.strobogrammaticInRange(low, high)
    print(ret)