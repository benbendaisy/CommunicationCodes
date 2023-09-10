from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(idx, temp_arr, ans):
            length = len(temp_arr)
            if length == k:
                ans.append(temp_arr[:])
                return
            if idx == n:
                return
            # do not include idx
            helper(idx + 1, temp_arr, ans)

            temp_arr.append(idx + 1) # get rid of 0
            helper(idx + 1, temp_arr, ans)
            temp_arr.pop()
        temp_arr = []
        ans = []
        helper(0, temp_arr, ans)
        return ans