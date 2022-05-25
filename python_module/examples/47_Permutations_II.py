from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permutation(cur = 0):
            if cur == n:
                res.append(nums[:])
                return

            for i in range(cur, n):
                nums[cur], nums[i] = nums[i], nums[cur]
                permutation(cur + 1)
                nums[cur], nums[i] = nums[i], nums[cur]

        n = len(nums)
        res = []
        permutation()
        kl=[]
        kl.extend(x for x in res if x not in kl)
        k=list(kl)
        return k

if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    ret = solution.permuteUnique(nums)
    print(ret)