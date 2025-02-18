from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def permutation(idx):
            if idx == n:
                res.append(nums[:])
                return
            for i in range(idx, n):
                nums[i], nums[idx] = nums[idx], nums[i]
                permutation(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]
        permutation(0)
        arr = []
        for per in res:
            if per not in arr:
                arr.append(per)
        return arr
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def back_track(path, choice):
            if not choice:
                res.append(path)
                return
            for i in range(len(choice)):
                back_track(path + [choice[i]], choice[:i] + choice[i + 1:])
        back_track([], nums)
        return list(map(list, {tuple(lst) for lst in res}))

if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    ret = solution.permuteUnique(nums)
    print(ret)