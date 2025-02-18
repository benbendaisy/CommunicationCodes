class Solution:
    """
    Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

    Return a list of all possible strings we could create. Return the output in any order.

    Example 1:

    Input: s = "a1b2"
    Output: ["a1b2","a1B2","A1b2","A1B2"]
    Example 2:

    Input: s = "3z4"
    Output: ["3z4","3Z4"]
    """
    def letterCasePermutation(self, s: str) -> List[str]:
        if not s:
            return []
        
        res, m = [], len(s)
        def back_track(path: list, idx: int):
            if idx == m:
                res.append("".join(path))
                return
            
            if s[idx].isalpha():
                back_track(path + [s[idx]], idx + 1)
                match s[idx].isupper():
                    case True:
                        back_track(path + [s[idx].lower()], idx + 1)
                    case _:
                        back_track(path + [s[idx].upper()], idx + 1)
                        
            else:
                back_track(path + [s[idx]], idx + 1)

        back_track([], 0)
        return res