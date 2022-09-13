from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = Counter(ransomNote)
        magazineDict = Counter(magazine)
        for key in ransomDict.keys():
            if key not in magazineDict or ransomDict[key] > magazineDict[key]:
                return False

        return True