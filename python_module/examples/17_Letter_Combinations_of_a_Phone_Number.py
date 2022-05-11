from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letterMap = {
            "0": ["_"],
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []

        def letterCombs(dits: str, strArr: list):
            if not dits:
                res.append("".join(strArr))
                return
            letter = dits[0]
            for ch in letterMap[letter]:
                letterCombs(dits[1:], strArr + [ch])

        letterCombs(digits, [])
        return res
