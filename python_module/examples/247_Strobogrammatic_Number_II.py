from typing import List


class Solution:
    def findStrobogrammatic1(self, n: int) -> List[str]:
        reversedPairs = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}

        q = ["0", "1", "8"] if n % 2 != 0 else [""]
        currLength = n % 2

        while currLength < n:
            currLength += 2
            newQ = []
            for item in q:
                for key in reversedPairs:
                    if key != "0" or currLength < n:
                        newQ.append(key + item + reversedPairs[key])
            q = newQ

        return q

    def findStrobogrammatic(self, n: int) -> List[str]:
        reversedPairs = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        def strobogrammatic(curLength: int):
            if curLength == 0:
                return [""]
            if curLength == 1:
                return ["0", "1", "8"]

            prevStrobogrammatic = strobogrammatic(curLength - 2)
            arr = []
            for key in reversedPairs:
                if key != "0" or curLength < n:
                    for item in prevStrobogrammatic:
                        arr.append(key + item + reversedPairs[key])
            return arr

        return strobogrammatic(n)



