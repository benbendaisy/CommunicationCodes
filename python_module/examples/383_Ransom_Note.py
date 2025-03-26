from collections import Counter


class Solution:
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = Counter(ransomNote)
        magazineDict = Counter(magazine)
        for key in ransomDict.keys():
            if key not in magazineDict or ransomDict[key] > magazineDict[key]:
                return False

        return True
    
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        freq1 = Counter(ransomNote)
        freq2 = Counter(magazine)
        return all((key in freq2 and freq1[key] <= freq2[key]) for key in freq1)