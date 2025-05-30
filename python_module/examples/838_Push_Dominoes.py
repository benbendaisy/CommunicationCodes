from filecmp import cmp


class Solution:
    """
        There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

        After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

        When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

        For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

        You are given a string dominoes representing the initial state where:

        dominoes[i] = 'L', if the ith domino has been pushed to the left,
        dominoes[i] = 'R', if the ith domino has been pushed to the right, and
        dominoes[i] = '.', if the ith domino has not been pushed.
        Return a string representing the final state.

        Example 1:

        Input: dominoes = "RR.L"
        Output: "RR.L"
        Explanation: The first domino expends no additional force on the second domino.
        Example 2:

        Input: dominoes = ".L.R...LR..L.."
        Output: "LL.RR.LLRRLL.."

        Constraints:

        n == dominoes.length
        1 <= n <= 105
        dominoes[i] is either 'L', 'R', or '.'.
    """
    def pushDominoes1(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            elif x > y:
                while i < j:
                    ans[i] = 'R'
                    ans[j] = 'L'
                    i += 1
                    j -= 1
        return "".join(ans)
    
    def pushDominoes2(self, dominoes: str) -> str:
        def recur(state):
            # Convert to list for mutability
            new_state = list(state)
            changed = False

            for i in range(len(state)):
                if state[i] == '.':
                    left = state[i - 1] if i > 0 else None
                    right = state[i + 1] if i < len(state) - 1 else None

                    if left == 'R' and right != 'L':
                        new_state[i] = 'R'
                        changed = True
                    elif right == 'L' and left != 'R':
                        new_state[i] = 'L'
                        changed = True

            new_state_str = ''.join(new_state)
            if changed:
                return recur(new_state_str)
            else:
                return new_state_str

        return recur(dominoes)
    
    def pushDominoes3(self, dominoes: str) -> str:
        @cache
        def helper(state: str) -> str:
            new_state = list(state)
            changed = False

            for i, v in enumerate(state):
                if v == '.':
                    left = state[i - 1] if i > 0 else None
                    right = state[i + 1] if i < len(state) - 1 else None
                    
                    if left == 'R' and right != 'L':
                        new_state[i] = 'R'
                        changed = True
                    elif right == 'L' and left != 'R':
                        new_state[i] = 'L'
                        changed = True
            new_state_str = "".join(new_state)
            if changed:
                return helper(new_state_str)
            else:
                return new_state_str
        return helper(dominoes)


if __name__ == "__main__":
    dominoes = ".L.R...LR..L.."
    solution = Solution()
    ret = solution.pushDominoes(dominoes)
    print(ret)
