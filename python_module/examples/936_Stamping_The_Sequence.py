from collections import deque
from typing import List


class Solution:
    """
        You are given two strings stamp and target. Initially, there is a string s of length target.length with all s[i] == '?'.

        In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.

        For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
        place stamp at index 0 of s to obtain "abc??",
        place stamp at index 1 of s to obtain "?abc?", or
        place stamp at index 2 of s to obtain "??abc".
        Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).
        We want to convert s to target using at most 10 * target.length turns.

        Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain target from s within 10 * target.length turns, return an empty array.

        Example 1:

        Input: stamp = "abc", target = "ababc"
        Output: [0,2]
        Explanation: Initially s = "?????".
        - Place stamp at index 0 to get "abc??".
        - Place stamp at index 2 to get "ababc".
        [1,0,2] would also be accepted as an answer, as well as some other answers.
        Example 2:

        Input: stamp = "abca", target = "aabcaca"
        Output: [3,0,1]
        Explanation: Initially s = "???????".
        - Place stamp at index 3 to get "???abca".
        - Place stamp at index 0 to get "abcabca".
        - Place stamp at index 1 to get "aabcaca".

        Constraints:

        1 <= stamp.length <= target.length <= 1000
        stamp and target consist of lowercase English letters.
    """
    def movesToStamp1(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        que = deque()
        done = [False] * n
        ans = []
        arr = []
        for i in range(n - m + 1):
            # For each window [i, i+M),
            # arr[i] will contain info on what needs to change
            # before we can reverse stamp at i.
            made, todo = set(), set()
            for j, c in enumerate(stamp):
                a = target[i + j]
                if a == c:
                    made.add(i + j)
                else:
                    todo.add(i + j)
            arr.append((made, todo))

            # If we can reverse stamp at i immediately,
            # enqueue letters from this window.
            if not todo:
                ans.append(i)
                for j in range(i, i + len(stamp)):
                    if not done[j]:
                        que.append(j)
                        done[j] = True

        while que:
            i = que.popleft()
            for j in range(max(0, i - m + 1), min(n - m, i) + 1):
                if i in arr[j][1]: # This window is affected
                    arr[j][1].discard(i) # Remove it from todo list of this window
                    if not arr[j][1]: # Todo list of this window is empty
                        ans.append(j)
                        for k in arr[j][0]: # For each letter to potentially enqueue,
                            if not done[k]:
                                que.append(k)
                                done[k] = True
        return ans[::-1] if all(done) else []

    def movesToStamp2(self, stamp: str, target: str) -> List[int]:
        if stamp == target:
            return [0]

        st, ta = list(stamp), list(target)
        slen, tlen = len(st), len(ta) - len(st) + 1
        ans, sdiff, tdiff = [], True, True
        while tdiff:
            tdiff = False
            for i in range(tlen):
                sdiff = False
                for j in range(slen):
                    if ta[i + j] == "*":
                        continue

                    if ta[i + j] != st[j]:
                        break

                    sdiff = True
                else:
                    if sdiff:
                        tdiff = True
                        for j in range(i, i + slen):
                            ta[j] = "*"
                        ans.append(i)

            for i in range(len(ta)):
                if ta[i] != "*":
                    return []

            return ans[::-1]

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        memoCache, ls, lt = {}, len(stamp), len(target)
        def dfs(sIdx, tIdx, seqs):
            """
            Calculate the nums of overrides
            :param sIdx:
            :param tIdx:
            :param seqs:
            :return:
            """
            if tIdx == lt: # complete the validate
                memoCache[sIdx, tIdx] = seqs if sIdx == ls else [] # check if complete the stamp
            if (sIdx, tIdx) not in memoCache: # verify if we already validate (sIdx, tIdx)
                if sIdx == ls: # check if we already validate the stamp
                    for i in range(ls):
                        cand = dfs(i, tIdx, [tIdx - i] + seqs) # find the sequence of overrides
                        if cand: # find the first sequence of overrides
                            memoCache[sIdx, tIdx] = cand
                            break
                    else: # if we could not find any override
                        memoCache[sIdx, tIdx] = []
                elif target[tIdx] == stamp[sIdx]: # if stamp matches the target
                    cand = dfs(sIdx + 1, tIdx + 1, seqs) # recursively validate the stamp and the target
                    # restart to evaluate the stamp and target
                    memoCache[sIdx, tIdx] = cand if cand else dfs(0, tIdx + 1, seqs + [tIdx + 1])
                else:
                    # if we could not any match or not verify before
                    memoCache[sIdx, tIdx] = []
            return memoCache[sIdx, tIdx]
        return dfs(0, 0, [0])

if __name__ == "__main__":
    solution = Solution()
    stamp = "abc"
    target = "ababc"
    ret = solution.movesToStamp(stamp, target)
    print(ret)


