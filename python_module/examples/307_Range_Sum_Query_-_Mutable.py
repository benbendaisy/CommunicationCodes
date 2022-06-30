from typing import List


class NumArray:
    """
        Given an integer array nums, handle multiple queries of the following types:

        Update the value of an element in nums.
        Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
        Implement the NumArray class:

        NumArray(int[] nums) Initializes the object with the integer array nums.
        void update(int index, int val) Updates the value of nums[index] to be val.
        int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
    """
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0] * len(nums)
        self.sums[0] = nums[0]
        for i in range(1, len(nums)):
            self.sums[i] = self.sums[i - 1] + nums[i]

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        for i in range(index, len(self.nums)):
            self.sums[i] += delta

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left - 1]

class NumArray1:
    def __init__(self, nums: List[int]):
        self.length = len(nums)
        self.tree = [0] * self.length + nums
        for i in range(self.length - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, index: int, val: int) -> None:
        self.tree[index + self.length] = val
        i = index + self.length
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        left, right = left + self.length, right + self.length
        while left <= right:
            if left % 2 == 1:
                res += self.tree[left]
                left += 1

            if right % 2 == 0:
                res += self.tree[right]
                right -= 1

            left >>= 1
            right >>= 1
        return res

# Driver Code
if __name__ == "__main__" :

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    solution = NumArray1(a)

    # print the sum in range(1,2) index-based
    print(solution.sumRange(1, 3))

    # modify element at 2nd index
    solution.update(2, 1)

    # print the sum in range(1,2) index-based
    print(solution.sumRange(1, 3))


