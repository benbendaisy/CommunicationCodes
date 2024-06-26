class Solution:
    """
    You are given an integer array nums of size n containing each element from 0 to n - 1 (inclusive). Each of the elements from 1 to n - 1 represents an item, and the element 0 represents an empty space.

    In one operation, you can move any item to the empty space. nums is considered to be sorted if the numbers of all the items are in ascending order and the empty space is either at the beginning or at the end of the array.

    For example, if n = 4, nums is sorted if:

    nums = [0,1,2,3] or
    nums = [1,2,3,0]
    ...and considered to be unsorted otherwise.

    Return the minimum number of operations needed to sort nums.
    """
    def sortArray(self, nums: List[int]) -> int:
        def helper(arr):
            cnt = 0
            visited = set()
            for i, item in enumerate(arr):
                if i == item or item in visited:
                    continue
                cnt += 1
                while not item in visited:
                    visited.add(item)
                    item = arr[item]
            if 0 in visited:
                cnt -= 2
            return cnt + len(visited)
        return min(helper(nums), helper([nums[-1]] + nums[:-1]))