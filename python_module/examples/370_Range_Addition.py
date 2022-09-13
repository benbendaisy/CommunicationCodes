from typing import List


class Solution:
    """
        You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

        You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

        Return arr after applying all the updates.

        Example 1:

        Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
        Output: [-2,0,3,5,3]
        Example 2:

        Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
        Output: [0,-4,2,2,2,4,4,-4,-4,-4]

        Constraints:

        1 <= length <= 105
        0 <= updates.length <= 104
        0 <= startIdxi <= endIdxi < length
        -1000 <= inci <= 1000
    """
    def getModifiedArray1(self, length: int, updates: List[List[int]]) -> List[int]:
        if length < 1:
            return []

        res = [0] * length
        for start, end, val in updates:
            for i in range(start, end + 1):
                res[i] += val

        return res

    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        #construct result & difference array
        diff = nums = [0] * length
        #record differency array changes
        #based on requirement, start index, end index, change value
        for start, end, change in updates:
            diff[start] += change
            #if end > than diff.lengh - 1 means changes until end of array, then no adjustment need
            if end < length - 1:
                diff[end + 1] -= change

        #based on differency array to reflect original num array
        nums[0] = diff[0]
        for i in range(1, length):
            nums[i] = nums[i - 1] + diff[i]

        return nums
