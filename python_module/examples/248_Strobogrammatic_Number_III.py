from typing import List


class Solution:
    def compareTwoStrs(self, str1: str, str2: str):
        return int(str1) >= int(str2)

    def strobogrammaticInRange(self, low: str, high: str) -> int:
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

if __name__ == "__main__":
    low = "0"
    high = "100"
    solution = Solution()
    ret = solution.strobogrammaticInRange(low, high)
    print(ret)