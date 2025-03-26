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
    def sortArray1(self, nums: List[int]) -> int:
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
    
    def sortArray2(self, nums: List[int]) -> int:
        n = len(nums)

        def solve(nums):
            res = 0
            for i in range(n):
                # moving first element that is in wrong position to pos '0'
                if i > 0 and nums[i] != i:
                    nums[0] = nums[i]
                    nums[i] = 0
                    res += 1
                # swap element at pos '0' until all elements are in their place
                while nums[0] != 0:
                    pos = nums[0]
                    nums[0], nums[pos] = nums[pos], nums[0]
                    res += 1
            return res
        
        # copy + shift elements one position right
        nums2 = [nums[-1]] + nums[:-1]
        
        return min(solve(nums), solve(nums2))
    
    def sortArray3(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(arr: List[int]):
            res = 0
            for i in range(n):
                if i > 0 and arr[i] != i:
                    arr[0] = arr[i]
                    arr[i] = 0
                    res += 1
                while arr[0] != 0:
                    pos = arr[0]
                    arr[0], arr[pos] = arr[pos], arr[0]
                    res += 1
            return res

        return min(helper(nums[:]), helper([nums[-1]] + nums[:-1]))
    
    def sortArray(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(arr: List[int]) -> int:
            n = len(arr)
            cnt = 0
            for i in range(n):
                # move the num that is not in the correct position to position zero
                if i > 0 and arr[i] != i:
                    arr[0] = arr[i]
                    arr[i] = 0
                    cnt += 1
                while arr[0] != 0:
                    pos = arr[0]
                    arr[0], arr[pos] = arr[pos], arr[0]
                    cnt += 1
            return cnt


        return min(helper(nums[:]), helper([nums[-1]] + nums[:-1]))