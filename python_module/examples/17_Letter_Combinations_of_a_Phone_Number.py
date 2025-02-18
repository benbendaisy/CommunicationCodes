from typing import List


class Solution:
    def letterCombinations1(self, digits: str) -> List[str]:
        if not digits:
            return []
        letter_map = {
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
        def letter_combine(idx, str_arr):
            if idx == len(digits):
                res.append("".join(str_arr))
                return
            for ch in letter_map[digits[idx]]:
                letter_combine(idx + 1, str_arr + [ch])
        letter_combine(0, [])
        return res


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num_map = {
            '0': ('_'),
            '1': (),
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z')
        }
        res = []
        def back_track(path: list, idx: int):
            if idx == len(digits):
                res.append("".join(path))
                return
            for ch in num_map[digits[idx]]:
                back_track(path + [ch], idx + 1)
        back_track([], 0)
        return res