from typing import List


class Solution:
    """
        You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

        Example 1:

        Input: nums = [5,2,6,1]
        Output: [2,1,1,0]
        Explanation:
        To the right of 5 there are 2 smaller elements (2 and 1).
        To the right of 2 there is only 1 smaller element (1).
        To the right of 6 there is 1 smaller element (1).
        To the right of 1 there is 0 smaller element.
        Example 2:

        Input: nums = [-1]
        Output: [0]
        Example 3:

        Input: nums = [-1,-1]
        Output: [0,0]

        Constraints:

        1 <= nums.length <= 105
        -104 <= nums[i] <= 104
    """
    def countSmaller1(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    cnt += 1
            res.append(cnt)
        return res

    def countSmaller(self, nums: List[int]) -> List[int]:
        # implement segment tree
        def update(index: int, value: int, tree, size):
            index += size  # shift the index to the leaf
            # update from leaf to root
            tree[index] += value
            while index > 1:
                index //= 2
                tree[index] = tree[index * 2] + tree[index * 2 + 1]

        def query(left, right, tree, size):
            # return sum of [left, right)
            res = 0
            left += size # shift the index to the leaf
            right += size
            while left < right:
                # if left is a right node
                # bring the value and move to parent's right node
                if left % 2 == 1:
                    res += tree[left]
                    left += 1
                # else directly move to parent
                left //= 2

                # if right is a right node
                # bring the value of the left node and move to parent
                if right % 2 == 1:
                    right -= 1
                    res += tree[right]
                # else directly move to parent
                right //= 2

            return res

        offset = 10**4 # offset negative to non-negative
        size = 2*10**4 + 1 # total possible values in nums
        tree = [0] * (2 * size)
        res = []
        for num in reversed(nums):
            smallerCnt = query(0, num + offset, tree, size)
            res.append(smallerCnt)
            update(num + offset, 1, tree, size)
        return reversed(res)


