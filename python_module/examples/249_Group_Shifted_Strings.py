from collections import defaultdict
from typing import List


class Solution:
    def getHashKey(self, string: str):
        nums = [ord(ch) for ch in string]
        idx = 0
        key = ""
        while idx + 1 < len(nums):
            key += chr((nums[idx + 1] - nums[idx]) % 26 + ord('a'))
            idx += 1
        return key
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        stringMap = defaultdict(lambda: [])
        oneLengthString = [x for x in strings if len(x) == 1]
        res = []
        if len(oneLengthString) > 0:
            res.append(oneLengthString)

        for x in strings:
            if len(x) > 1:
                key = self.getHashKey(x)
                stringMap[key].append(x)
        for strList in stringMap.values():
            res.append(strList)

        return res

if __name__ == "__main__":
    strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
    solution = Solution()
    ret = solution.groupStrings(strings)
    print(ret)