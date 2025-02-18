class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

        Example 1:

        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
        Example 2:

        Input: n = 1
        Output: ["()"]
        """
        res = []
        if n < 1:
            return res
        
        def back_track(path: list, pulse: int, idx: int):
            if idx == 2 * n:
                if pulse == 0:
                    res.append("".join(path))
                return
            
            if pulse < n:
                back_track(path + ['('], pulse + 1, idx + 1)
            
            if pulse > 0:
                back_track(path + [')'], pulse - 1, idx + 1)
        back_track([], 0, 0)

        return res