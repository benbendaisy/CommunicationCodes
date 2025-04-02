from typing import List


class Solution:
    def combine1(self, n: int, k: int) -> List[List[int]]:
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
    
    def combine2(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(idx: int, path: []):
            if len(path) == k:
                res.append(path)
                return 
            
            if idx > n:
                return
            
            for i in range(idx, n + 1):
                helper(i + 1, path + [i])
        helper(1, [])

        return res